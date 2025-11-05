## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture`

```diff

-587.81.10.0.0
-  __TEXT.__text: 0x33ec00
-  __TEXT.__auth_stubs: 0x3be0
-  __TEXT.__objc_methlist: 0x1f7d4
-  __TEXT.__const: 0x1420e8
-  __TEXT.__cstring: 0x48ded
-  __TEXT.__oslogstring: 0x17593
-  __TEXT.__gcc_except_tab: 0x1064
+587.101.4.0.0
+  __TEXT.__text: 0x33fa1c
+  __TEXT.__auth_stubs: 0x3c40
+  __TEXT.__objc_methlist: 0x20ce4
+  __TEXT.__const: 0x1420c8
+  __TEXT.__cstring: 0x48d1a
+  __TEXT.__oslogstring: 0x184b2
+  __TEXT.__gcc_except_tab: 0x10c8
   __TEXT.__dlopen_cstrs: 0xa8
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x7728
-  __TEXT.__objc_classname: 0x4685
-  __TEXT.__objc_methname: 0x72315
-  __TEXT.__objc_methtype: 0xd217
-  __TEXT.__objc_stubs: 0x2d360
-  __DATA_CONST.__got: 0x5158
-  __DATA_CONST.__const: 0x4dc8
-  __DATA_CONST.__objc_classlist: 0x1018
+  __TEXT.__unwind_info: 0x7dc0
+  __TEXT.__objc_classname: 0x469f
+  __TEXT.__objc_methname: 0x72d91
+  __TEXT.__objc_methtype: 0xd1d1
+  __TEXT.__objc_stubs: 0x2d7c0
+  __DATA_CONST.__got: 0x5588
+  __DATA_CONST.__const: 0x4990
+  __DATA_CONST.__objc_classlist: 0x1020
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe070
+  __DATA_CONST.__objc_selrefs: 0xe2b0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xf38
-  __DATA_CONST.__objc_arraydata: 0x12c0
-  __AUTH_CONST.__auth_got: 0x1e00
-  __AUTH_CONST.__const: 0x48b0
-  __AUTH_CONST.__cfstring: 0x2d9a0
-  __AUTH_CONST.__objc_const: 0x5e368
-  __AUTH_CONST.__objc_intobj: 0x2f40
+  __DATA_CONST.__objc_superrefs: 0xf40
+  __DATA_CONST.__objc_arraydata: 0x12b0
+  __AUTH_CONST.__auth_got: 0x1e30
+  __AUTH_CONST.__const: 0x4860
+  __AUTH_CONST.__cfstring: 0x2d0a0
+  __AUTH_CONST.__objc_const: 0x5caf8
+  __AUTH_CONST.__objc_intobj: 0x2fa0
   __AUTH_CONST.__objc_arrayobj: 0xf18
   __AUTH_CONST.__objc_doubleobj: 0x1c0
   __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x3c50
+  __AUTH.__objc_data: 0x3ca0
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0x6d80
-  __DATA.__data: 0x2c34
+  __DATA.__objc_ivar: 0x6e38
+  __DATA.__data: 0x2c04
   __DATA.__common: 0xa40
-  __DATA.__bss: 0x188b
+  __DATA.__bss: 0x18a3
   __DATA_DIRTY.__objc_data: 0x64a0
   __DATA_DIRTY.__data: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/Versions/A/AggregateDictionary
   - /System/Library/PrivateFrameworks/AudioSession.framework/Versions/A/AudioSession
   - /System/Library/PrivateFrameworks/CMCaptureCore.framework/Versions/A/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/Versions/A/CMCaptureDevice
   - /System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging
   - /System/Library/PrivateFrameworks/CMPhoto.framework/Versions/A/CMPhoto
   - /System/Library/PrivateFrameworks/CinematicFraming.framework/Versions/A/CinematicFraming

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90AE4E83-D3A9-324D-B57E-02208BCD5719
-  Functions: 14423
-  Symbols:   37917
+  UUID: ABFAB96F-0618-34A6-9651-BE0AD5C8839C
+  Functions: 18252
+  Symbols:   42788
   CStrings:  32664
 
Symbols:
+ +[BWAggdDataReporter sharedInstance].cold.1
+ +[BWAutoFocusPositionSensorMonitor sharedInstance].cold.1
+ +[BWCoreAnalyticsReporter sharedInstance].cold.1
+ +[BWDeferredCaptureContainer captureRequestIdentifierForManifest:].cold.1
+ +[BWDeferredCaptureContainerManager sharedInstance].cold.1
+ +[BWDeferredContainer archiveObject:error:].cold.1
+ +[BWDeferredContainer archiveObject:error:].cold.2
+ +[BWDeferredContainer initialize].cold.1
+ +[BWDeferredContainer manifestDictionaryForApplicationIdentifier:captureRequestIdentifier:photoDescriptors:].cold.1
+ +[BWDeferredContainer manifestDictionaryForApplicationIdentifier:captureRequestIdentifier:photoDescriptors:].cold.2
+ +[BWDeferredContainer manifestDictionaryForApplicationIdentifier:captureRequestIdentifier:photoDescriptors:].cold.3
+ +[BWDeferredContainer validateManifestURLSize:].cold.1
+ +[BWDeferredProcessingContainerManager sharedInstance].cold.1
+ +[BWDeferredTransactionBroker sharedInstance].cold.1
+ +[BWFigCaptureAttachedAccessoriesMonitor sharedAttachedAccessoriesMonitor].cold.1
+ +[BWFigCaptureDeviceVendor sharedCaptureDeviceVendorWithDefaultDeviceCreateFunction:].cold.1
+ +[BWIOSurfacePoller defaultPoller].cold.1
+ +[BWIOSurfaceTracking defaultSurfaceTracking].cold.1
+ +[BWIrisMovieGenerator _addNewMetadataTrackToAssetWriter:forTrackTimeScale:yieldingTrackID:].cold.1
+ +[BWIrisMovieGenerator _addNewMetadataTrackToAssetWriter:forTrackTimeScale:yieldingTrackID:].cold.2
+ +[BWIrisMovieGenerator _addNewMetadataTrackToAssetWriter:forTrackTimeScale:yieldingTrackID:].cold.3
+ +[BWMemoryPool sharedMemoryPool].cold.1
+ +[BWMetalColorCubeRenderer bundle].cold.1
+ +[BWMetalColorCubeRenderer bundle].cold.2
+ +[BWNodeInput newSampleDataToBeDroppedMarkerBufferFromSampleBuffer:].cold.1
+ +[BWPipelineStage _currentPipelineStage].cold.1
+ +[BWPipelineStage _setCurrentPipelineStage:].cold.1
+ +[BWVideoFormat formatByResolvingRequirements:printErrors:].cold.1
+ +[BWVideoFormat formatByResolvingRequirements:printErrors:].cold.2
+ +[CMCaptureFrameSenderEndpointsServerSideSingleton addEndpoint:endpointUniqueID:endpointType:endpointPID:endpointProxyPID:endpointAuditToken:endpointProxyAuditToken:endpointCameraUniqueID:].cold.1
+ +[CMCaptureFrameSenderEndpointsServerSideSingleton createXPCArrayOfFrameSenderEndpoints].cold.1
+ +[CMCaptureFrameSenderEndpointsServerSideSingleton endpointsByPID].cold.1
+ +[CMCaptureFrameSenderEndpointsServerSideSingleton removeAllEndpointsWithPID:].cold.1
+ +[CMCaptureFrameSenderEndpointsServerSideSingleton removeEndpointWithUniqueID:].cold.1
+ +[CMCaptureFrameSenderServiceBrokerSingleton frameSenderServiceBrokerSingleton].cold.1
+ +[FigCaptureCIFilterUnarchiverDelegate sharedInstance].cold.1
+ +[FigCaptureCMIOExtensionProvider sharedInstance].cold.1
+ +[FigCaptureCameraParameters cinematicFramingVirtualCameraConfigurationForPortType:sensorIDString:].cold.1
+ +[FigCaptureCameraParameters cinematicFramingVirtualCameraConfigurationForPortType:sensorIDString:].cold.2
+ +[FigCaptureCameraParameters cinematicFramingVirtualCameraConfigurationForPortType:sensorIDString:].cold.3
+ +[FigCaptureCameraParameters temporalFilterSessionConfigurationForPortType:sensorIDString:].cold.1
+ +[FigCaptureCameraParameters temporalFilterSessionConfigurationForPortType:sensorIDString:].cold.2
+ +[FigCaptureCameraParameters temporalFilterSessionConfigurationForPortType:sensorIDString:].cold.3
+ +[FigCaptureClientApplicationStateMonitor initialize].cold.1
+ +[FigCaptureDeviceLockStateMonitor sharedDeviceLockStateMonitor].cold.1
+ +[FigCaptureDisplayLayoutMonitor sharedContinuityDisplayLayoutMonitor].cold.1
+ +[FigCaptureDisplayLayoutMonitor sharedDisplayLayoutMonitor].cold.1
+ +[FigCaptureDisplayLayoutMonitor sharedExternalDisplayLayoutMonitor].cold.1
+ +[FigCaptureSessionObservatory sharedObservatory].cold.1
+ +[FigCaptureSourceBackings initialize].cold.1
+ +[FigCaptureSourceBackings sharedCaptureSourceBackings].cold.1
+ +[FigCaptureSystemStatus sharedInstance].cold.1
+ -[BWActionCameraFlickerAvoidanceMonitor initWithDefaultMaxExposureDurationFrameworkOverrideByPortType:].cold.1
+ -[BWActionCameraSceneMonitor initWithTuningParametersByPortType:videoStabilizationStrength:bravoTelephotoEnabled:attachDebugFrameStatistics:].cold.1
+ -[BWAdaptiveCorrectionPreviewRegistrationProvider initWithCameraInfoByPortType:excludeStaticComponentFromAlignmentShifts:].cold.1
+ -[BWApplySmartStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:originalPixelBuffer:processedPixelBuffer:completionHandler:].cold.1
+ -[BWApplySmartStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:originalPixelBuffer:processedPixelBuffer:completionHandler:].cold.2
+ -[BWAttachedMediaSwapNode renderSampleBuffer:forInput:].cold.1
+ -[BWAttachedMediaSwapNode renderSampleBuffer:forInput:].cold.2
+ -[BWAudioConverterNode renderSampleBuffer:forInput:].cold.1
+ -[BWAudioConverterNode renderSampleBuffer:forInput:].cold.2
+ -[BWAudioConverterNode renderSampleBuffer:forInput:].cold.3
+ -[BWAudioConverterNode renderSampleBuffer:forInput:].cold.4
+ -[BWAudioFileSinkNode renderSampleBuffer:forInput:].cold.1
+ -[BWAudioFileSinkNode renderSampleBuffer:forInput:].cold.2
+ -[BWAudioFileSinkNode renderSampleBuffer:forInput:].cold.3
+ -[BWAudioFileSinkNode renderSampleBuffer:forInput:].cold.4
+ -[BWAudioFormat _initForAVAudioSettings:inputFormat:].cold.1
+ -[BWAudioFormat _initForAVAudioSettings:inputFormat:].cold.2
+ -[BWAudioFormat _initForAVAudioSettings:inputFormat:].cold.3
+ -[BWAudioFormat _initForAVAudioSettings:inputFormat:].cold.4
+ -[BWAudioSourceNode start:].cold.1
+ -[BWAudioSplitNode didSelectFormat:forInput:forAttachedMediaKey:].cold.1
+ -[BWAudioSplitNode initWithInputChannelLayoutTag:output1ChannelLayoutTag:output2ChannelLayoutTag:].cold.1
+ -[BWBackgroundBlurNode didChangeSuppressedGesturesEnabled:]
+ -[BWBackgroundBlurNode renderSampleBuffer:forInput:].cold.1
+ -[BWBackgroundBlurNode renderSampleBuffer:forInput:].cold.2
+ -[BWBackgroundBlurNode renderSampleBuffer:forInput:].cold.3
+ -[BWBackgroundBlurNode renderSampleBuffer:forInput:].cold.4
+ -[BWBackgroundBlurNode setSuppressedGestureHandler:]
+ -[BWBreadthFirstEnumerator nextObject].cold.1
+ -[BWCMPhotoEncoderManager addAuxImage:type:auxImageMetadata:options:parentImageHandle:auxImageHandleOut:].cold.1
+ -[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:].cold.1
+ -[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:].cold.2
+ -[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:].cold.3
+ -[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:].cold.4
+ -[BWCMPhotoEncoderManager tagStereoPairGroupWithStereoPhotoImageHandles:groupMetadata:].cold.5
+ -[BWCameraInfoMetadataNode didSelectFormat:forInput:].cold.1
+ -[BWCameraInfoMetadataNode didSelectFormat:forInput:].cold.2
+ -[BWCinematicFramingNode _isSampleBufferFromPrimaryStream:metadataDict:]
+ -[BWColorLookupCache blackColorLookupTable].cold.1
+ -[BWColorLookupCache identityColorLookupTable].cold.1
+ -[BWColorLookupCache whiteColorLookupTable].cold.1
+ -[BWCoreAnalyticsReporter _sendAutoFocusROIEventToBiome:].cold.2
+ -[BWCoreImageFilterRendererParameters depthTypeForFilter:].cold.1
+ -[BWDataBufferPool setCapacity:].cold.1
+ -[BWDeferredArrayIntermediate archive:].cold.1
+ -[BWDeferredArrayIntermediate archive:].cold.2
+ -[BWDeferredArrayIntermediate archive:].cold.3
+ -[BWDeferredArrayIntermediate flush].cold.1
+ -[BWDeferredArrayIntermediate flush].cold.2
+ -[BWDeferredArrayIntermediate flush].cold.3
+ -[BWDeferredArrayIntermediate initWithArray:tag:URL:].cold.1
+ -[BWDeferredArrayIntermediate setArchive:].cold.1
+ -[BWDeferredArrayIntermediate setArchive:].cold.2
+ -[BWDeferredArrayIntermediate setArchive:].cold.3
+ -[BWDeferredArrayIntermediate setURL:prefetchQueue:].cold.1
+ -[BWDeferredBufferIntermediate archive:].cold.1
+ -[BWDeferredBufferIntermediate archive:].cold.2
+ -[BWDeferredBufferIntermediate archive:].cold.3
+ -[BWDeferredBufferIntermediate flush].cold.1
+ -[BWDeferredBufferIntermediate flush].cold.2
+ -[BWDeferredBufferIntermediate flush].cold.3
+ -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:portType:compressionProfile:URL:].cold.1
+ -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:portType:compressionProfile:URL:].cold.2
+ -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:portType:compressionProfile:URL:].cold.3
+ -[BWDeferredBufferIntermediate setBuffer:].cold.1
+ -[BWDeferredBufferIntermediate setBuffer:].cold.2
+ -[BWDeferredCaptureContainer abort].cold.1
+ -[BWDeferredCaptureContainer abort].cold.2
+ -[BWDeferredCaptureContainer commitCaptureSettings:settings:].cold.1
+ -[BWDeferredCaptureContainer commitCaptureSettings:settings:].cold.2
+ -[BWDeferredCaptureContainer commitCaptureSettings:settings:].cold.3
+ -[BWDeferredCaptureContainer commitInference:tag:inferenceAttachmentKey:portType:].cold.1
+ -[BWDeferredCaptureContainer commit].cold.1
+ -[BWDeferredCaptureContainer copyXPCEncoding:].cold.1
+ -[BWDeferredCaptureContainer copyXPCEncoding:].cold.2
+ -[BWDeferredCaptureContainer copyXPCEncoding:].cold.3
+ -[BWDeferredCaptureContainer copyXPCEncoding:].cold.4
+ -[BWDeferredCaptureContainer copyXPCEncoding:].cold.5
+ -[BWDeferredCaptureContainer flush].cold.1
+ -[BWDeferredCaptureContainer flush].cold.2
+ -[BWDeferredCaptureContainer flush].cold.3
+ -[BWDeferredCaptureContainer flush].cold.4
+ -[BWDeferredCaptureContainer initWithApplicationID:captureRequestIdentifier:baseFolderURL:flushBuffersUponCommit:err:].cold.1
+ -[BWDeferredCaptureContainer preflush].cold.1
+ -[BWDeferredCaptureContainer preflush].cold.2
+ -[BWDeferredCaptureContainerManager abortContainer:error:].cold.1
+ -[BWDeferredCaptureContainerManager abortContainer:error:].cold.2
+ -[BWDeferredCaptureContainerManager abortContainer:error:].cold.3
+ -[BWDeferredCaptureContainerManager addBufferPool:].cold.1
+ -[BWDeferredCaptureContainerManager addCaptureContainer:].cold.1
+ -[BWDeferredCaptureContainerManager commitContainer:].cold.1
+ -[BWDeferredCaptureContainerManager commitContainer:].cold.2
+ -[BWDeferredCaptureContainerManager commitContainer:].cold.3
+ -[BWDeferredCaptureContainerManager copyRemoteContainerForApplicationID:captureRequestIdentifier:err:].cold.1
+ -[BWDeferredCaptureContainerManager copyRemoteContainerForApplicationID:captureRequestIdentifier:err:].cold.2
+ -[BWDeferredCaptureContainerManager createCaptureContainerWithApplicationID:captureRequestIdentifier:err:].cold.1
+ -[BWDeferredCaptureContainerManager flush:toMinimumCapacity:].cold.1
+ -[BWDeferredCaptureContainerManager manifestsForApplicationID:err:].cold.1
+ -[BWDeferredCaptureContainerManager newPixelBuffer:].cold.1
+ -[BWDeferredCaptureContainerManager newPixelBuffer:].cold.2
+ -[BWDeferredCaptureContainerManager releaseRemoteContainerForApplicationID:captureRequestIdentifier:].cold.1
+ -[BWDeferredCaptureContainerManager releaseRemoteContainerForApplicationID:captureRequestIdentifier:].cold.2
+ -[BWDeferredCaptureContainerManager removeBufferPool:].cold.1
+ -[BWDeferredCaptureControllerInput addBuffer:bufferType:captureFrameFlags:metadata:rawThumbnailsBuffer:rawThumbnailsMetadata:].cold.1
+ -[BWDeferredCaptureControllerInput addBuffer:bufferType:captureFrameFlags:metadata:rawThumbnailsBuffer:rawThumbnailsMetadata:].cold.2
+ -[BWDeferredCaptureControllerInput addBuffer:bufferType:captureFrameFlags:metadata:rawThumbnailsBuffer:rawThumbnailsMetadata:].cold.3
+ -[BWDeferredCaptureControllerInput addBuffer:bufferType:captureFrameFlags:metadata:rawThumbnailsBuffer:rawThumbnailsMetadata:].cold.4
+ -[BWDeferredContainerManagerBase deleteContainerForApplicationID:captureRequestIdentifier:].cold.1
+ -[BWDeferredContainerManagerBase deleteContainerForApplicationID:captureRequestIdentifier:].cold.2
+ -[BWDeferredContainerManagerBase manifestForApplicationID:captureRequestIdentifier:err:].cold.1
+ -[BWDeferredContainerManagerBase manifestForApplicationID:captureRequestIdentifier:err:].cold.2
+ -[BWDeferredDictionaryIntermediate archive:].cold.1
+ -[BWDeferredDictionaryIntermediate archive:].cold.2
+ -[BWDeferredDictionaryIntermediate archive:].cold.3
+ -[BWDeferredDictionaryIntermediate flush].cold.1
+ -[BWDeferredDictionaryIntermediate flush].cold.2
+ -[BWDeferredDictionaryIntermediate flush].cold.3
+ -[BWDeferredDictionaryIntermediate initWithDictionary:tag:URL:].cold.1
+ -[BWDeferredDictionaryIntermediate setArchive:].cold.1
+ -[BWDeferredDictionaryIntermediate setArchive:].cold.2
+ -[BWDeferredDictionaryIntermediate setArchive:].cold.3
+ -[BWDeferredDictionaryIntermediate setURL:prefetchQueue:].cold.1
+ -[BWDeferredIntermediate initWithCoder:].cold.1
+ -[BWDeferredIntermediate initWithTag:URL:].cold.1
+ -[BWDeferredIntermediate initWithTag:URL:].cold.2
+ -[BWDeferredMetadataIntermediate initWithMetadata:tag:bufferTag:URL:].cold.1
+ -[BWDeferredProcessingContainer abortingProcessingDueToError:].cold.1
+ -[BWDeferredProcessingContainer abortingProcessingDueToError:].cold.2
+ -[BWDeferredProcessingContainer copyBufferForTag:err:].cold.1
+ -[BWDeferredProcessingContainer copyBufferForTag:err:].cold.2
+ -[BWDeferredProcessingContainer copyBufferForType:portType:metadata:err:].cold.1
+ -[BWDeferredProcessingContainer copyInferenceBufferForKey:portType:err:].cold.1
+ -[BWDeferredProcessingContainer copyInferenceForKey:customClasses:portType:err:].cold.1
+ -[BWDeferredProcessingContainer copyMetadataForBufferTag:err:].cold.1
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.1
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.10
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.11
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.12
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.13
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.2
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.3
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.4
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.5
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.6
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.7
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.8
+ -[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:].cold.9
+ -[BWDeferredProcessingContainerManager createProcessingContainerWithApplicationID:captureRequestIdentifier:openForPeeking:err:].cold.1
+ -[BWDeferredProcessingContainerManager createProcessingContainerWithApplicationID:captureRequestIdentifier:openForPeeking:err:].cold.2
+ -[BWDeferredProcessingContainerManager createProcessingContainerWithApplicationID:captureRequestIdentifier:openForPeeking:err:].cold.3
+ -[BWDeferredProcessingContainerManager deleteContainerForApplicationID:captureRequestIdentifier:].cold.1
+ -[BWDeferredProcessingContainerManager manifestsForApplicationID:err:].cold.1
+ -[BWDeferredProcessingContainerManager manifestsForApplicationID:err:].cold.2
+ -[BWDeferredProcessingContainerManager manifestsForApplicationID:err:].cold.3
+ -[BWDeferredProcessingContainerManager releaseProcessingContainer:].cold.1
+ -[BWDeferredProcessingContainerManager waitForShaderCompilation].cold.1
+ -[BWDeferredTransactionBroker _openTransaction:pid:name:].cold.2
+ -[BWDepthConverterNode convertToFloatAndRotateAndCrop:outputPixelBuffer:]
+ -[BWDepthConverterNode rotateAndScaleAndCropImagePixelBuffer:depthPixelBuffer:to:rotationAngle:flip:]
+ -[BWDepthFirstEnumerator nextObject].cold.1
+ -[BWDepthFirstEnumerator nextObject].cold.2
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.1
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.2
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.3
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.4
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.5
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.6
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.7
+ -[BWDepthRotatorNode renderSampleBuffer:forInput:].cold.8
+ -[BWDepthSynchronizerNode handleNodeError:forInput:].cold.1
+ -[BWDeskCamNode renderSampleBuffer:forInput:].cold.1
+ -[BWDeskCamNode renderSampleBuffer:forInput:].cold.2
+ -[BWDeskCamNode renderSampleBuffer:forInput:].cold.3
+ -[BWDeskCamNode renderSampleBuffer:forInput:].cold.4
+ -[BWDeskCamNode renderSampleBuffer:forInput:].cold.5
+ -[BWDetectedFacesRingBuffer addFacesFromSampleBuffer:].cold.1
+ -[BWDetectedFacesRingBuffer transferFacesToSampleBuffer:totalSensorCropRect:].cold.1
+ -[BWDetectedObjectsInfoRingBuffer addObjectsFromSampleBuffer:].cold.1
+ -[BWDetectedObjectsInfoRingBuffer transferObjectsToSampleBuffer:totalSensorCropRect:].cold.1
+ -[BWDeviceMotionActivityDetector init].cold.1
+ -[BWDeviceMotionActivityDetector processSampleBuffer:].cold.1
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.1
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.2
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.3
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.4
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.5
+ -[BWFaceDetectionNode initWithObjectMetadataIdentifiers:movieFileOutputMetadataIdentifierGroups:].cold.6
+ -[BWFaceDetectionNode renderSampleBuffer:forInput:].cold.1
+ -[BWFaceDetectionNode renderSampleBuffer:forInput:].cold.2
+ -[BWFaceDetectionNode renderSampleBuffer:forInput:].cold.3
+ -[BWFaceDetectionNode renderSampleBuffer:forInput:].cold.4
+ -[BWFaceTrackingNode initWithFigThreadPriority:pearlModuleType:useUnfilteredDepth:queueDepth:passthroughInputs:allowPixelTransfer:].cold.1
+ -[BWFigCaptureDevice _bwSyncGroupArrayFromFig:]
+ -[BWFigCaptureDevice _copyBWMultiCamConfigurationFromFig:]
+ -[BWFigCaptureDevice _copyFigMultiCamConfigurationFromBW:]
+ -[BWFigCaptureDevice _figSyncGroupArrayFromBW:]
+ -[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:]
+ -[BWFigCaptureDevice _removeFigCaptureDeviceListeners]
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.1
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.2
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.3
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.4
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.5
+ -[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:].cold.6
+ -[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:]
+ -[BWFigCaptureDeviceClient clientType]
+ -[BWFigCaptureDeviceClient initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:]
+ -[BWFigCaptureDeviceVendor _copyStreamsFromDevice:positions:deviceTypes:requestControl:deviceClientPriority:allowsStreamControlLoss:error:].cold.1
+ -[BWFigCaptureDeviceVendor _copyStreamsFromDevice:positions:deviceTypes:requestControl:deviceClientPriority:allowsStreamControlLoss:error:].cold.2
+ -[BWFigCaptureDeviceVendor _copyStreamsFromDevice:positions:deviceTypes:requestControl:deviceClientPriority:allowsStreamControlLoss:error:].cold.3
+ -[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:figCaptureDevice:]
+ -[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClients:available:postNotifications:reason:canShareWithFlashlight:cameraStolenInterruptor:]
+ -[BWFigCaptureDeviceVendor _deviceWithID:].cold.1
+ -[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:]
+ -[BWFigCaptureDeviceVendor _registerForDeviceNotifications:]
+ -[BWFigCaptureDeviceVendor _unregisterForDeviceNotifications:]
+ -[BWFigCaptureDeviceVendor activeDeviceClients]
+ -[BWFigCaptureDeviceVendor controlledStreamsForDevice:]
+ -[BWFigCaptureDeviceVendor copyStreamsWithUniqueIDs:forDevice:deviceClientPriority:error:].cold.1
+ -[BWFigCaptureDeviceVendor osStatePropertyList].cold.1
+ -[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:]
+ -[BWFigCaptureDeviceVendor registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:]
+ -[BWFigCaptureDeviceVendorDeviceState figCaptureDevice]
+ -[BWFigCaptureDeviceVendorDeviceState initWithDevice:figCaptureDevice:]
+ -[BWFigCaptureDeviceVendorDeviceState setTakeBackDeviceCalledForActiveClientID:]
+ -[BWFigCaptureDeviceVendorDeviceState takeBackDeviceCalledForActiveClientID]
+ -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:].cold.1
+ -[BWFigCaptureSession imageQueueSinkNodeDidDisplayFirstFrame:timedOut:]
+ -[BWFigCaptureSession stillImageCoordinator:willPrepareStillImageCaptureWithSettings:clientInitiated:].cold.1
+ -[BWFigCaptureStream initWithFigCaptureStream:deviceID:errOut:].cold.1
+ -[BWFigCaptureStream initWithFigCaptureStream:deviceID:errOut:].cold.2
+ -[BWFigCaptureStream initWithFigCaptureStream:deviceID:errOut:].cold.3
+ -[BWFigCaptureStream initWithFigCaptureStream:deviceID:errOut:].cold.4
+ -[BWFigCaptureStream setSuppressedGestureHandler:]
+ -[BWFigCaptureStream suppressedGestureHandler]
+ -[BWFigCaptureStreamsMapper bwFigCaptureStreamForFigCaptureStream:]
+ -[BWFigCaptureStreamsMapper bwFigCaptureStreamsForFigCaptureStreams:]
+ -[BWFigCaptureStreamsMapper dealloc]
+ -[BWFigCaptureStreamsMapper figCaptureStreamForBWFigCaptureStream:]
+ -[BWFigCaptureStreamsMapper figCaptureStreamsForBWFigCaptureStreams:]
+ -[BWFigCaptureStreamsMapper initWithBWFigCaptureStreams:figCaptureStreams:]
+ -[BWFigCaptureSynchronizedStreamsGroup initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:]
+ -[BWFigCaptureSynchronizedStreamsGroup initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:].cold.1
+ -[BWFigCaptureSynchronizedStreamsGroup stop].cold.1
+ -[BWFigVideoCaptureDevice _deviceWillStartStreaming].cold.1
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.1
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.2
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.3
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.4
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.5
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.6
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.7
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.8
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:deviceClientPriority:error:].cold.9
+ -[BWFigVideoCaptureDevice _postNotificationWithPayload:notificationPayload:].cold.1
+ -[BWFigVideoCaptureDevice _resetSDOFEffectAndStagePreviewStatus]
+ -[BWFigVideoCaptureDevice _resolveStillImageCaptureTypeFromStatisticsByPortType:masterCaptureStream:flashMode:hdrMode:qualityPrioritization:stereoFusionMode:depthDataDeliveryEnabled:bravoConstituentImageDeliveryDeviceTypes:burstQualityCaptureEnabled:clientBracketMode:forSceneMonitoring:captureFlags:].cold.1
+ -[BWFigVideoCaptureDevice _sendMacroFocusChangedNotification:]
+ -[BWFigVideoCaptureDevice _stillImageCaptureSettingsWithID:captureType:deliverOriginalImage:deliverSushiRaw:bravoConstituentImageDeliveryDeviceTypes:clientBracketSettings:captureFlags:userInitiatedRequestPTS:frameStatisticsByPortType:].cold.1
+ -[BWFigVideoCaptureDevice _stillImageCaptureSettingsWithID:captureType:deliverOriginalImage:deliverSushiRaw:bravoConstituentImageDeliveryDeviceTypes:clientBracketSettings:captureFlags:userInitiatedRequestPTS:frameStatisticsByPortType:].cold.2
+ -[BWFigVideoCaptureDevice _teardownAutoFocusSampleBufferProcessor].cold.1
+ -[BWFigVideoCaptureDevice _updateSensorRawPools].cold.1
+ -[BWFigVideoCaptureDevice _updateSensorRawPools].cold.2
+ -[BWFigVideoCaptureDevice _updateSensorRawPools].cold.3
+ -[BWFigVideoCaptureDevice _updateThermalPressureStatsWithOldSDOFEffectStatus:newSDOFEffectStatus:]
+ -[BWFigVideoCaptureDevice projectorModeMaskForProjectorMode:]
+ -[BWFigVideoCaptureDevice secureMetadataEnabled]
+ -[BWFigVideoCaptureDevice sensorRawPixelFormat].cold.1
+ -[BWFigVideoCaptureDevice sensorRawPixelFormat].cold.2
+ -[BWFigVideoCaptureDevice setContinuousAutoFocusRect:isFocusRectInOverscanSpace:].cold.1
+ -[BWFigVideoCaptureDevice setDeepFusionEnabled:].cold.1
+ -[BWFigVideoCaptureDevice setDepthMaxFrameRate:].cold.1
+ -[BWFigVideoCaptureDevice setDepthWithDeepFusionEnabled:].cold.1
+ -[BWFigVideoCaptureDevice setDigitalFlashEnabled:].cold.1
+ -[BWFigVideoCaptureDevice setFaceDetectionDrivenImageProcessingMode:].cold.1
+ -[BWFigVideoCaptureDevice setFocusModeAutoWithRect:restrictToRect:continuous:smooth:rangeRestrictionNear:rangeRestrictionFar:isFocusRectInOverscanSpace:].cold.1
+ -[BWFigVideoCaptureDevice setLearnedNRMode:].cold.1
+ -[BWFigVideoCaptureDevice setMemoryPool:].cold.1
+ -[BWFigVideoCaptureDevice setNondisruptiveSwitchingFormatIndicesByPortType:maximumAllowedFrameRate:minimumFrameRate:maximumFrameRate:].cold.1
+ -[BWFigVideoCaptureDevice setPortraitEffectPropertiesDelegate:].cold.1
+ -[BWFigVideoCaptureDevice setSecureMetadataEnabled:]
+ -[BWFigVideoCaptureDevice setSuppressedGesturesEnabled:]
+ -[BWFigVideoCaptureDevice setTorchLevel:].cold.1
+ -[BWFigVideoCaptureDevice suppressedGesturesEnabled]
+ -[BWFigVideoCaptureDevice updatePortraitSceneMonitoringRequiresStageThresholds:].cold.1
+ -[BWFigVideoCaptureDevice updateSmartCameraStreamPropertiesWithInferenceResult:].cold.1
+ -[BWFigVideoCaptureDevice updateSmartCameraStreamPropertiesWithInferenceResult:].cold.2
+ -[BWFigVideoCaptureDevice updateStillImageSensorRawBufferPoolsWithRetainedBufferCount:zoomBasedRetainedBufferCount:ultraHighResolutionRetainedBufferCount:].cold.1
+ -[BWFigVideoCaptureDevice updateStillImageSensorRawBufferPoolsWithRetainedBufferCount:zoomBasedRetainedBufferCount:ultraHighResolutionRetainedBufferCount:].cold.2
+ -[BWFigVideoCaptureDevice updateStillImageSensorRawBufferPoolsWithRetainedBufferCount:zoomBasedRetainedBufferCount:ultraHighResolutionRetainedBufferCount:].cold.3
+ -[BWFigVideoCaptureDevice updateStillImageSensorRawBufferPoolsWithRetainedBufferCount:zoomBasedRetainedBufferCount:ultraHighResolutionRetainedBufferCount:].cold.4
+ -[BWFigVideoCaptureDevice updateStillImageSensorRawBufferPoolsWithRetainedBufferCount:zoomBasedRetainedBufferCount:ultraHighResolutionRetainedBufferCount:].cold.5
+ -[BWFigVideoCaptureStream captureStillImageFromTimeMachineWithStillImageSettings:].cold.1
+ -[BWFigVideoCaptureStream captureStillImageFromTimeMachineWithStillImageSettings:].cold.2
+ -[BWFigVideoCaptureStream didChangeSuppressedGesturesEnabled:]
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.1
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.10
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.11
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.12
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.13
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.2
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.3
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.4
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.5
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.6
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.7
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.8
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:].cold.9
+ -[BWFigVideoCaptureStream serviceNondisruptiveSwitchingFormatForZoomFactor:frameStatistics:imageControlMode:stillImageDigitalFlashMode:isStationary:binnedSIFROnSecondaryStreamAllowed:ignoreZoomFactorAndQuadraSubPixelSceneMonitoring:ultraHighResolutionZeroShutterLagEnabled:].cold.1
+ -[BWFigVideoCaptureStream setActiveFormatIndex:].cold.1
+ -[BWFigVideoCaptureStream setActiveFormatIndex:].cold.2
+ -[BWFigVideoCaptureStream setActiveFormatIndex:].cold.3
+ -[BWFigVideoCaptureStream setCmioZoomFactor:].cold.1
+ -[BWFigVideoCaptureStream setDeskCamActive:].cold.1
+ -[BWFigVideoCaptureStream setDetectedObjectTypes:].cold.1
+ -[BWFigVideoCaptureStream setFaceDetectionConfiguration:].cold.1
+ -[BWFigVideoCaptureStream setSuppressedGestureHandler:]
+ -[BWFigVideoCaptureStream setSuppressedGesturesEnabled:]
+ -[BWFigVideoCaptureStream suppressedGesturesEnabled]
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.1
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.2
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.3
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.4
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.5
+ -[BWFigVideoCaptureSynchronizedStreamsGroup initWithSynchronizedStreamsGroup:activeStreams:readOnly:baseZoomFactorOverrides:clientBaseZoomFactorsByPortType:error:].cold.6
+ -[BWFileCoordinatorNode _logNumBuffersReceivedDuringStartingRecording]
+ -[BWFileCoordinatorNode cancelStartRecordingWithSettings:].cold.1
+ -[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:].cold.1
+ -[BWFileCoordinatorNode pauseRecording].cold.1
+ -[BWFlashlightAnalyticsPayload luxLevel]
+ -[BWFlashlightAnalyticsPayload setLuxLevel:]
+ -[BWFrameRateGovernorNode renderSampleBuffer:forInput:].cold.1
+ -[BWFrameRateGovernorNode renderSampleBuffer:forInput:].cold.2
+ -[BWFrameStatistics isValid]
+ -[BWFrameStatisticsByPortType initWithPortTypes:autoFocusRecommendedMasterPortTypeEnabled:].cold.1
+ -[BWGraph cancelDeferredNodePrepare].cold.1
+ -[BWGraph commitConfigurationWithID:error:].cold.1
+ -[BWGraph commitConfigurationWithID:error:].cold.2
+ -[BWGraph commitConfigurationWithID:error:].cold.3
+ -[BWGraph safelyConnectOutput:toInput:pipelineStage:deferredAttach:].cold.1
+ -[BWGraph safelyConnectOutput:toInput:pipelineStage:deferredAttach:].cold.2
+ -[BWGraph safelyConnectOutput:toInput:pipelineStage:deferredAttach:].cold.3
+ -[BWGraph safelyConnectOutput:toInput:pipelineStage:deferredAttach:].cold.4
+ -[BWGraph start:].cold.1
+ -[BWGraph start:].cold.2
+ -[BWGraph start:].cold.3
+ -[BWGraph start:].cold.4
+ -[BWImageQueueSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:].cold.1
+ -[BWImageQueueSinkNode renderSampleBuffer:forInput:].cold.1
+ -[BWIrisMovieGenerator _getAdjustedRefMovieEndTime:].cold.1
+ -[BWIrisMovieGenerator _getAdjustedRefMovieEndTime:].cold.2
+ -[BWIrisMovieGenerator _getAdjustedRefMovieEndTime:].cold.3
+ -[BWIrisMovieGenerator _getAdjustedRefMovieStartTime:].cold.1
+ -[BWIrisMovieGenerator _getAdjustedRefMovieStartTime:].cold.2
+ -[BWIrisMovieGenerator _getAdjustedRefMovieStartTime:].cold.3
+ -[BWIrisMovieInfo isHardCut]
+ -[BWIrisMovieInfo setIsHardCut:]
+ -[BWIrisSequenceAdjuster dequeueAndRetainAdjustedSampleBufferForMediaTypeWithIndex:].cold.1
+ -[BWIrisSequenceAdjuster enqueueSampleBuffer:forMediaTypeWithIndex:].cold.1
+ -[BWIrisSequenceAdjuster enqueueSampleBuffer:forMediaTypeWithIndex:].cold.2
+ -[BWIrisSequenceAdjuster enqueueSampleBuffer:forMediaTypeWithIndex:].cold.3
+ -[BWIrisStagingNode _adjustedStartTimeForSmartStyle:allowSearchBackward:searchEndPTS:adjustedStartBufferIndexOut:].cold.1
+ -[BWIrisStagingNode _adjustedStartTimeForTrimmedStartTime:ensuringAtLeast3FramesBeforeStillTime:ensuringFrameIsAfterTrimmedStartTime:butNotEarlierThanOriginalStartTime:adjustedStartBufferIndexOut:].cold.1
+ -[BWIrisStagingNode _mostRecentCuttingBufferPTSBeforePTS:cuttingBufferIndexOut:].cold.1
+ -[BWIrisStagingNode _mostRecentCuttingBufferPTSBeforePTS:cuttingBufferIndexOut:].cold.2
+ -[BWMRCNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWMemoryPool newMTLBufferWithLength:forDevice:].cold.1
+ -[BWMemoryPool newMTLBufferWithLength:forDevice:].cold.2
+ -[BWMetadataDetectorGatingNode didSelectFormat:forInput:].cold.1
+ -[BWMetadataDetectorGatingNode initWithSceneClassifierVersion:mrcEnabled:appClipCodeEnabled:textLocalizationEnabled:lowPowerModeEnabled:compressed8BitInputEnabled:].cold.1
+ -[BWMetadataSynchronizerNode didReachEndOfDataForInput:].cold.1
+ -[BWMetadataSynchronizerNode initWithArraysOfMetadataInputs:propagateSampleBufferAttachmentKeys:propagateSampleBufferMetadataDictKeys:syncMetadataForPortTypes:syncOnlyIfMetadataEnabledForKeys:].cold.1
+ -[BWMetadataSynchronizerNode initWithArraysOfMetadataInputs:propagateSampleBufferAttachmentKeys:propagateSampleBufferMetadataDictKeys:syncMetadataForPortTypes:syncOnlyIfMetadataEnabledForKeys:].cold.2
+ -[BWMetadataTimeMachine reset].cold.1
+ -[BWMetalColorCubeRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:].cold.1
+ -[BWMetalColorCubeRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:].cold.2
+ -[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:errorOut:].cold.1
+ -[BWMotionAttachmentsNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWMotionDataPreserver prependPreservedMotionDataToSampleBuffer:].cold.1
+ -[BWMotionDataTimeMachine copyMotionDataForStartingSerialNumber:endingSerialNumber:].cold.1
+ -[BWMultiCamConfiguration _initWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:withCaptureDevice:readCurrentStateFromCaptureDevice:stereoVideoCaptureEnabled:].cold.1
+ -[BWMultiCamConfiguration _initWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:withCaptureDevice:readCurrentStateFromCaptureDevice:stereoVideoCaptureEnabled:].cold.2
+ -[BWMultiCamConfiguration copyActiveSynchronizedStreamsGroupsForDevice:errorOut:].cold.1
+ -[BWMultiCamConfiguration copyActiveSynchronizedStreamsGroupsForDevice:errorOut:].cold.2
+ -[BWMultiCamConfiguration multiCamConfigurationForDevice:errorOut:].cold.1
+ -[BWMultiCamConfiguration multiCamConfigurationForDevice:errorOut:].cold.2
+ -[BWMultiCamConfiguration multiCamConfigurationForDevice:errorOut:].cold.3
+ -[BWMultiStreamCameraSourceNode _bringStreamUpToDate].cold.1
+ -[BWMultiStreamCameraSourceNode _bringStreamUpToDate].cold.2
+ -[BWMultiStreamCameraSourceNode _bringStreamUpToDate].cold.3
+ -[BWMultiStreamCameraSourceNode _bringStreamUpToDate].cold.4
+ -[BWMultiStreamCameraSourceNode _bringStreamUpToDate].cold.5
+ -[BWMultiStreamCameraSourceNode _updateOutputIDMappingsForStreamingOutputs].cold.1
+ -[BWMultiStreamCameraSourceNode _updateOutputIDMappingsForStreamingOutputs].cold.2
+ -[BWMultiStreamCameraSourceNode _updateOutputIDMappingsForStreamingOutputs].cold.3
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.1
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.2
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.3
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.4
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.5
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.6
+ -[BWMultiStreamCameraSourceNode _updateOutputRequirements].cold.7
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.1
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.10
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.11
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.12
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.13
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.14
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.15
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.2
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.3
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.4
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.5
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.6
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.7
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.8
+ -[BWMultiStreamCameraSourceNode allocateOrReuseBufferPoolsFromSourceNode:].cold.9
+ -[BWMultiStreamCameraSourceNode colorInfoForOutput:].cold.1
+ -[BWMultiStreamCameraSourceNode colorInfoForOutput:].cold.2
+ -[BWMultiStreamCameraSourceNode colorInfoForOutput:].cold.3
+ -[BWMultiStreamCameraSourceNode faceIDReadinessOutput]
+ -[BWMultiStreamCameraSourceNode motionToWakeOutput]
+ -[BWMultiStreamCameraSourceNode requestedZoomFactorChanged:].cold.1
+ -[BWMultiStreamCameraSourceNode secureMetadataOutputConfigurationDidChange:].cold.1
+ -[BWMultiStreamCameraSourceNode secureMetadataOutputConfigurationDidChange:].cold.2
+ -[BWMultiStreamCameraSourceNode setMotionToWakeTargetFrameRate:forSessionID:]
+ -[BWMultiStreamCameraSourceNode start:].cold.1
+ -[BWMultiStreamCameraSourceNode start:].cold.2
+ -[BWNodeOutput prepareForConfiguredFormatToBecomeLive].cold.1
+ -[BWNoiseReductionAndSharpeningParameters noiseReductionAndSharpeningConfigurationForType:gain:qSub:].cold.1
+ -[BWNoiseReductionAndSharpeningParameters noiseReductionAndSharpeningConfigurationForType:gain:qSub:].cold.2
+ -[BWOverCaptureAttachedMediaSplitNode _handleIrisMovieRequestForInput:sbuf:].cold.2
+ -[BWOverCaptureAttachedMediaSplitNode renderSampleBuffer:forInput:].cold.1
+ -[BWOverCaptureAttachedMediaSplitNode renderSampleBuffer:forInput:].cold.2
+ -[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundle].cold.1
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.1
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.10
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.11
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.12
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.13
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.14
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.15
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.2
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.3
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.4
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.5
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.6
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.7
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.8
+ -[BWPersonSegmentationFilteringNode renderSampleBuffer:forInput:].cold.9
+ -[BWPhotoDecompressor initWithOutputPixelBufferPool:].cold.1
+ -[BWPhotoEncoderController _newAuxiliaryImagePropertiesFromPortraitEffectsMatteMetadata:].cold.1
+ -[BWPhotoEncoderController _newAuxiliaryImagePropertiesFromPortraitEffectsMatteMetadata:].cold.2
+ -[BWPhotoEncoderController _newAuxiliaryImagePropertiesFromSemanticMatteSampleBuffer:].cold.1
+ -[BWPhotoEncoderController _newAuxiliaryImagePropertiesFromSemanticMatteSampleBuffer:].cold.2
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.1
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.2
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.3
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.4
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.5
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.6
+ -[BWPhotoEncoderController _updateSmartStyleDeltaMapForSampleBufferIfNeeded:decompressedStyledPixelBuffer:stillImageSettings:encodingScheme:processingFlags:].cold.7
+ -[BWPhotoEncoderController _waitForPiecemealEncodingQueueToComplete].cold.1
+ -[BWPhotoEncoderController _waitForPreviewGenerationQueueToComplete].cold.1
+ -[BWPhotoEncoderController _waitForPrewarmingQueueToComplete].cold.1
+ -[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:].cold.1
+ -[BWPhotoEncoderNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:].cold.1
+ -[BWPhotoEncoderNode renderSampleBuffer:forInput:].cold.1
+ -[BWPipelineStage sendMessage:toInput:].cold.1
+ -[BWPixelBufferPool preallocate].cold.1
+ -[BWPixelBufferPool setCapacity:].cold.1
+ -[BWPixelBufferPool waitForAvailablePixelBuffer].cold.1
+ -[BWPixelTransferNode _ensureRotationSession].cold.2
+ -[BWPixelTransferNode _ensureRotationSession].cold.3
+ -[BWPixelTransferNode renderSampleBuffer:forInput:].cold.1
+ -[BWPixelTransferNode renderSampleBuffer:forInput:].cold.2
+ -[BWPixelTransferNode renderSampleBuffer:forInput:].cold.3
+ -[BWPixelTransferNode setPreferredOutputPixelFormats:].cold.1
+ -[BWPreviewGyroStabilization _computeMotionStatisticsWithQuaternion:focalLength:maxAngleAccumulateOut:maxAngleInstantOut:translationOut:].cold.1
+ -[BWPreviewGyroStabilization _computeMotionStatisticsWithQuaternion:focalLength:maxAngleAccumulateOut:maxAngleInstantOut:translationOut:].cold.2
+ -[BWPreviewGyroStabilization _computeMotionStatisticsWithQuaternion:focalLength:maxAngleAccumulateOut:maxAngleInstantOut:translationOut:].cold.3
+ -[BWPreviewRegistration initWithCameraInfoByPortType:sensorBinningFactor:registrationType:metalCommandQueue:excludeStaticComponentFromAlignmentShifts:].cold.1
+ -[BWPreviewRegistration initWithCameraInfoByPortType:sensorBinningFactor:registrationType:metalCommandQueue:excludeStaticComponentFromAlignmentShifts:].cold.2
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:].cold.1
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:].cold.2
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:].cold.3
+ -[BWPreviewStitcherNode renderSampleBuffer:forInput:].cold.1
+ -[BWPreviewStitcherNode renderSampleBuffer:forInput:].cold.2
+ -[BWPreviewStitcherNode renderSampleBuffer:forInput:].cold.3
+ -[BWPreviewStitcherNode renderSampleBuffer:forInput:].cold.4
+ -[BWPreviewStitcherNode renderSampleBuffer:forInput:].cold.5
+ -[BWPreviewTimeMachineSinkNode dealloc].cold.1
+ -[BWPreviewTimeMachineSinkNode renderSampleBuffer:forInput:].cold.1
+ -[BWPreviewTimeMachineSinkNode suspendWithPTSRange:completionHandler:].cold.1
+ -[BWPreviewTimeMachineSinkNode suspendWithPTSRange:completionHandler:].cold.2
+ -[BWQuickTimeMovieFileSinkNode _buildIrisRefMovieGeneratorAndWriteFirstIrisAsRefMovie].cold.3
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.10
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.11
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.12
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.13
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.14
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.15
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.2
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.3
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.4
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.5
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.6
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.7
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.8
+ -[BWQuickTimeMovieFileSinkNode _doEndRecordingAtTime:earlyTerminationErrCode:].cold.9
+ -[BWQuickTimeMovieFileSinkNode _findMarkers:].cold.1
+ -[BWQuickTimeMovieFileSinkNode _findMarkers:].cold.2
+ -[BWQuickTimeMovieFileSinkNode _findStartMarkersWithMatchedStagedSetting:sensorVideoPort:captureDeviceType:].cold.1
+ -[BWQuickTimeMovieFileSinkNode _findStartMarkersWithMatchedStagedSetting:sensorVideoPort:captureDeviceType:].cold.2
+ -[BWQuickTimeMovieFileSinkNode _findStartMarkersWithMatchedStagedSetting:sensorVideoPort:captureDeviceType:].cold.3
+ -[BWQuickTimeMovieFileSinkNode _findStartMarkersWithMatchedStagedSetting:sensorVideoPort:captureDeviceType:].cold.4
+ -[BWQuickTimeMovieFileSinkNode dealloc].cold.1
+ -[BWQuickTimeMovieFileSinkNode dealloc].cold.2
+ -[BWQuickTimeMovieFileSinkNode dealloc].cold.3
+ -[BWRemoteQueueSinkNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWRemoteQueueSinkNode renderSampleBuffer:forInput:].cold.1
+ -[BWRenderList _continueOptimizingRendererList:parameterList:withFilter:fromProvider:context:].cold.1
+ -[BWRenderList prepareWithParameters:forInputVideoFormat:inputMediaPropertiesByAttachedMediaKey:].cold.1
+ -[BWRenderListAnimator prepareWithInputVideoFormat:inputMediaPropertiesByAttachedMediaKey:].cold.1
+ -[BWReverseBreadthFirstEnumerator nextObject].cold.1
+ -[BWReverseDepthFirstEnumerator nextObject].cold.1
+ -[BWReverseDepthFirstEnumerator nextObject].cold.2
+ -[BWSecureMetadataOutputConfiguration faceIDReadinessAttentionRequired]
+ -[BWSecureMetadataOutputConfiguration faceIDReadinessEnabled]
+ -[BWSecureMetadataOutputConfiguration faceIDReadinessPeriocularEnabled]
+ -[BWSecureMetadataOutputConfiguration faceOcclusionDetectionEnabled]
+ -[BWSecureMetadataOutputConfiguration faceTrackingEnabled]
+ -[BWSecureMetadataOutputConfiguration faceTrackingFailureFieldOfViewModifier]
+ -[BWSecureMetadataOutputConfiguration faceTrackingMaxNumTrackedFaces]
+ -[BWSecureMetadataOutputConfiguration faceTrackingNetworkFailureThresholdMultiplier]
+ -[BWSecureMetadataOutputConfiguration motionToWakeEnabled]
+ -[BWSecureMetadataOutputConfiguration motionToWakeTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration setFaceIDReadinessAttentionRequired:]
+ -[BWSecureMetadataOutputConfiguration setFaceIDReadinessEnabled:]
+ -[BWSecureMetadataOutputConfiguration setFaceIDReadinessPeriocularEnabled:]
+ -[BWSecureMetadataOutputConfiguration setFaceOcclusionDetectionEnabled:]
+ -[BWSecureMetadataOutputConfiguration setFaceTrackingEnabled:]
+ -[BWSecureMetadataOutputConfiguration setFaceTrackingFailureFieldOfViewModifier:]
+ -[BWSecureMetadataOutputConfiguration setFaceTrackingMaxNumTrackedFaces:]
+ -[BWSecureMetadataOutputConfiguration setFaceTrackingNetworkFailureThresholdMultiplier:]
+ -[BWSecureMetadataOutputConfiguration setMotionToWakeEnabled:]
+ -[BWSecureMetadataOutputConfiguration setMotionToWakeTargetFrameRate:]
+ -[BWSinkNode initWithSinkID:].cold.1
+ -[BWSlaveFrameSynchronizerNode didReachEndOfDataForInput:].cold.1
+ -[BWSlaveFrameSynchronizerNode renderSampleBuffer:forInput:].cold.1
+ -[BWSlaveFrameSynchronizerNode renderSampleBuffer:forInput:].cold.2
+ -[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundle].cold.1
+ -[BWSmartStyleLearningNode _extractANSTMasks:forPTS:].cold.1
+ -[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle].cold.1
+ -[BWSmartStyleLearningNode renderSampleBuffer:forInput:].cold.1
+ -[BWStereoVideoMetadataNode initWithPorts:secondaryPort:cameraInfoByPortType:errStatus:].cold.1
+ -[BWStereoVideoMetadataNode initWithPorts:secondaryPort:cameraInfoByPortType:errStatus:].cold.2
+ -[BWStereoVideoMetadataNode initWithPorts:secondaryPort:cameraInfoByPortType:errStatus:].cold.3
+ -[BWStillImageCoordinatorNode _configureCurrentCaptureRequestStateForFigCaptureStillImageSettings].cold.1
+ -[BWStillImageCoordinatorNode _enqueueRequestWithSettings:serviceRequestsIfNecessary:].cold.1
+ -[BWStillImageCoordinatorNode _enqueueRequestWithSettings:serviceRequestsIfNecessary:].cold.2
+ -[BWStillImageCoordinatorNode _unpackNextRequest].cold.1
+ -[BWStillImageCoordinatorNode beginStillImageMomentCaptureWithSettings:].cold.1
+ -[BWStillImageCoordinatorNode initiateStillImageCaptureNowWithSettings:].cold.1
+ -[BWStillImageCoordinatorNode initiateStillImageCaptureNowWithSettings:].cold.2
+ -[BWStillImageScalerNode renderSampleBuffer:forInput:].cold.1
+ -[BWStillImageSmartStyleAttachmentTransferNode renderSampleBuffer:forInput:].cold.1
+ -[BWStillImageSmartStyleAttachmentTransferNode renderSampleBuffer:forInput:].cold.2
+ -[BWStillImageTimeMachine copyBestFrame].cold.1
+ -[BWStillImageTimeMachine insertFrame:].cold.1
+ -[BWStreamStartStopSynchronizer initWithStreams:timeoutInSeconds:].cold.1
+ -[BWStreamStartStopSynchronizer initWithStreams:timeoutInSeconds:].cold.2
+ -[BWStreamingCVAFilterRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:].cold.1
+ -[BWStreamingCVAFilterRendererParameters updateByInterpolatingFromParameters:toParameters:withFractionComplete:].cold.2
+ -[BWStreamingFilterNode changeToSemanticStyle:animated:].cold.1
+ -[BWStreamingFilterNode didSelectFormat:forInput:forAttachedMediaKey:].cold.1
+ -[BWStreamingFilterNode renderSampleBuffer:forInput:].cold.1
+ -[BWStreamingFilterNode renderSampleBuffer:forInput:].cold.2
+ -[BWStreamingFilterNode renderSampleBuffer:forInput:].cold.3
+ -[BWStreamingSessionAnalyticsPayload hitPortraitInPhotoPreviewThermalPressure]
+ -[BWStreamingSessionAnalyticsPayload longestContinuousPortraitInPhotoPreviewInMS]
+ -[BWStreamingSessionAnalyticsPayload secureMetadataEnabled]
+ -[BWStreamingSessionAnalyticsPayload setHitPortraitInPhotoPreviewThermalPressure:]
+ -[BWStreamingSessionAnalyticsPayload setLongestContinuousPortraitInPhotoPreviewInMS:]
+ -[BWStreamingSessionAnalyticsPayload setSecureMetadataEnabled:]
+ -[BWSubjectSelectionNode renderSampleBuffer:forInput:].cold.1
+ -[BWSubjectSelectionNode renderSampleBuffer:forInput:].cold.2
+ -[BWSubjectSelectionNode renderSampleBuffer:forInput:].cold.3
+ -[BWSubjectSelectionNode renderSampleBuffer:forInput:].cold.4
+ -[BWSynchronizerNode renderSampleBuffer:forInput:].cold.1
+ -[BWSynchronizerNode renderSampleBuffer:forInput:].cold.2
+ -[BWSynchronizerNode renderSampleBuffer:forInput:].cold.3
+ -[BWTemporalFilterNode renderSampleBuffer:forInput:].cold.1
+ -[BWUBCaptureParameters initWithPortType:sensorIDDictionary:].cold.1
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.1
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.2
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.3
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.4
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.5
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.6
+ -[BWVISNode didSelectFormat:forInput:forAttachedMediaKey:].cold.7
+ -[BWVISNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWVISNode renderSampleBuffer:forInput:].cold.1
+ -[BWVISNode renderSampleBuffer:forInput:].cold.2
+ -[BWVISNode renderSampleBuffer:forInput:].cold.3
+ -[BWVISNode setStabilizeDepthAttachments:].cold.1
+ -[BWVISProcessorController prepareToProcess].cold.1
+ -[BWVideoCompressorNode configurationWithID:updatedFormat:didBecomeLiveForInput:].cold.1
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.1
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.10
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.2
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.3
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.4
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.5
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.6
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.7
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.8
+ -[BWVideoCompressorNode renderSampleBuffer:forInput:].cold.9
+ -[BWVideoDefringingNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWVideoDefringingNode renderSampleBuffer:forInput:].cold.1
+ -[BWVideoFormat formatDescription].cold.1
+ -[BWVideoOrientationMetadataNode updateVideoOrientation:].cold.1
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.1
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.2
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.3
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.4
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.5
+ -[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:].cold.6
+ -[BWZoomCommandHandler predictRampZoomFactorAfterNumberOfFrames:settingZoomFactorOfInterest:].cold.1
+ -[CMCaptureFrameSenderService initWithEndpointType:endpointPID:endpointProxyPID:endpointAuditToken:endpointProxyAuditToken:endpointCameraUniqueID:].cold.1
+ -[CMIOUserNotification _createOrUpdate:withTimeout:flags:dictionary:].cold.1
+ -[CMIOUserNotification cancel].cold.1
+ -[CMIOUserNotification cancel].cold.2
+ -[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataSourceDimensions]
+ -[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataTargetDimensions]
+ -[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataSourceDimensions:]
+ -[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataTargetDimensions:]
+ -[FigCaptureCMIOExtensionStream configureStream].cold.1
+ -[FigCaptureCameraParameters actionCameraSceneMonitoringParametersForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters actionCameraSceneMonitoringParametersForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters actionCameraSceneMonitoringParametersForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters chromaticDefringingParametersForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters chromaticDefringingParametersForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters disparityRefinementTypeForPortType:sensorIDString:zoomFactor:].cold.1
+ -[FigCaptureCameraParameters disparityRefinementTypeForPortType:sensorIDString:zoomFactor:].cold.2
+ -[FigCaptureCameraParameters disparityRefinementTypeForPortType:sensorIDString:zoomFactor:].cold.3
+ -[FigCaptureCameraParameters disparityRefinementTypeForPortType:sensorIDString:zoomFactor:].cold.4
+ -[FigCaptureCameraParameters disparityVersionForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters disparityVersionForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters disparityVersionForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters focalLengthCharacterizationForStream:].cold.1
+ -[FigCaptureCameraParameters focusPixelDisparityVersionForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters focusPixelDisparityVersionForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters focusPixelDisparityVersionForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters mattingVersionForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters mattingVersionForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters mattingVersionForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters panoramaRequiresLTMLockingForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters panoramaRequiresLTMLockingForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters panoramaRequiresLTMLockingForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.1
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.2
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.3
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.4
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.5
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.6
+ -[FigCaptureCameraParameters portraitPreviewForegroundBlurEnabledForPortType:sensorIDString:zoomFactor:].cold.7
+ -[FigCaptureCameraParameters quadraSubPixelSwitchingParametersForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters quadraSubPixelSwitchingParametersForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters quadraSubPixelSwitchingParametersForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters sensorIDDictionaryForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters sensorIDDictionaryForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters sensorIDDictionaryForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters sensorIDDictionaryForStream:].cold.1
+ -[FigCaptureCameraParameters sensorIDDictionaryForStream:].cold.2
+ -[FigCaptureCameraParameters stereoPhotoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters stereoPhotoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters stereoPhotoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraParameters stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.1
+ -[FigCaptureCameraParameters stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.2
+ -[FigCaptureCameraParameters stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:].cold.3
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.1
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.10
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.11
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.12
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.13
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.14
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.15
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.16
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.17
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.18
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.19
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.2
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.20
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.21
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.22
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.23
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.24
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.25
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.26
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.27
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.28
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.29
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.3
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.30
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.31
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.32
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.4
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.5
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.6
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.7
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.8
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.9
+ -[FigCaptureCameraSourcePipeline faceIDReadinessOutputForSourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline motionToWakeOutputForSourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline nextPreviewOutputForSourceDeviceType:intendedForVideoDataSinkPipeline:]
+ -[FigCaptureCameraSourcePipeline setMotionToWakeTargetFrameRate:forSessionID:]
+ -[FigCaptureConnectionConfiguration initWithXPCEncoding:].cold.1
+ -[FigCaptureConnectionConfiguration initWithXPCEncoding:].cold.2
+ -[FigCaptureFlatPlist objectAtOffset:].cold.1
+ -[FigCaptureFlatPlist objectAtOffset:].cold.2
+ -[FigCaptureImageSensorTemperatureMonitor initWithPortType:sensorThermalLevelsByTemperature:].cold.1
+ -[FigCaptureLogSmartCameraGating logGateClosed].cold.1
+ -[FigCaptureMetadataSinkPipeline _buildMetadataSinkPipeline:graph:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:faceIDReadinessSourceOutput:motionToWakeSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
+ -[FigCaptureMetadataSinkPipeline initWithConfiguration:graph:name:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:faceIDReadinessSourceOutput:motionToWakeSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
+ -[FigCaptureMovieFileSinkHeadPipeline initWithConfiguration:videoSourceCaptureOutput:audioSourceCaptureOutput:audioSourceCinematicAudioCaptureOutput:smartCameraInferenceOutput:detectedObjectBoxedMetadataOutputs:objectDetectionSourceOutput:metadataSourcePipelineOutputs:graph:parentPipeline:inferenceScheduler:captureDevice:audioSourceDelegate:fileCoordinatorStatusDelegate:irisRequestDelegate:masterClock:workgroup:videoGreenGhostMitigationEnabled:].cold.1
+ -[FigCaptureMovieFileSinkHeadPipeline setSceneClassifierSuspended:].cold.1
+ -[FigCaptureMovieFileSinkHeadPipeline setSceneClassifierSuspended:].cold.2
+ -[FigCaptureMovieFileSinkMiddlePipeline initWithConfiguration:graph:parentPipeline:headPipeline:captureDevice:workgroup:].cold.1
+ -[FigCaptureMovieFileSinkMiddlePipeline initWithConfiguration:graph:parentPipeline:headPipeline:captureDevice:workgroup:].cold.2
+ -[FigCaptureMovieFileSinkPipeline setRecording:forTailPipelineIndex:].cold.2
+ -[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevice:inferenceScheduler:recordingStatusDelegate:workgroup:].cold.1
+ -[FigCaptureOSStateHandle _osStateData:].cold.1
+ -[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:].cold.1
+ -[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:].cold.2
+ -[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:].cold.3
+ -[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:].cold.4
+ -[FigCapturePixelConverter convertPixelBuffer:cropRect:allocateOutputFromBufferPool:outputPixelBuffer:].cold.5
+ -[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:].cold.1
+ -[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:].cold.2
+ -[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:].cold.3
+ -[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:].cold.4
+ -[FigCapturePixelConverter convertSampleBuffer:cropRect:outputSampleBuffer:].cold.5
+ -[FigCapturePixelConverter updateOutputPixelFormat:dimensions:poolCapacity:colorSpaceProperties:].cold.1
+ -[FigCapturePixelConverter updateOutputPixelFormat:dimensions:poolCapacity:colorSpaceProperties:].cold.2
+ -[FigCapturePixelConverter updateOutputPixelFormat:dimensions:poolCapacity:colorSpaceProperties:].cold.3
+ -[FigCapturePowerMonitor init].cold.1
+ -[FigCapturePowerMonitor init].cold.2
+ -[FigCapturePowerMonitor init].cold.3
+ -[FigCapturePreviewSinkPipeline setSceneClassifierSuspended:].cold.1
+ -[FigCapturePreviewSinkPipeline setSceneClassifierSuspended:].cold.2
+ -[FigCaptureProcessHandle _initWithAuditToken:error:].cold.1
+ -[FigCaptureProcessHandle _initWithPID:error:].cold.1
+ -[FigCaptureProprietaryDefaults objectForKey:].cold.1
+ -[FigCaptureProprietaryDefaults objectsForWildcardKey:].cold.1
+ -[FigCaptureProprietaryDefaults objectsForWildcardKey:].cold.2
+ -[FigCaptureProprietaryDefaults observeChangesForKey:].cold.1
+ -[FigCaptureProprietaryDefaults sendNotificationOfNewTransientValue:forKey:].cold.1
+ -[FigCaptureProprietaryDefaults setObject:forKey:].cold.1
+ -[FigCaptureProprietaryDefaults setObject:forWildcardKey:].cold.1
+ -[FigCaptureProprietaryDefaults stopObservingChangesForKey:].cold.1
+ -[FigCaptureRemoteQueueSinkPipeline setSinkNode:].cold.1
+ -[FigCaptureSemanticStyle _initWithToneBias:warmthBias:].cold.1
+ -[FigCaptureSemanticStyle _initWithToneBias:warmthBias:].cold.2
+ -[FigCaptureSessionConfiguration initWithXPCEncoding:].cold.1
+ -[FigCaptureSessionConfiguration initWithXPCEncoding:].cold.2
+ -[FigCaptureSessionParsedConfiguration initWithSessionConfiguration:clientSetsUserInitiatedCaptureRequestTime:restrictions:].cold.1
+ -[FigCaptureSessionParsedConfigurationRestrictions initWithClientAuditToken:].cold.1
+ -[FigCaptureSessionProxy closePreviewTap].cold.1
+ -[FigCaptureSessionProxy openPreviewTapWithDelegate:].cold.1
+ -[FigCaptureSessionProxy openPreviewTapWithDelegate:].cold.2
+ -[FigCaptureSinkPipeline setUpstreamOutput:].cold.1
+ -[FigCaptureSmartStyle _initWithCast:intensity:toneBias:colorBias:].cold.1
+ -[FigCaptureSourceConfiguration description].cold.1
+ -[FigCaptureSourceConfiguration initWithXPCEncoding:].cold.1
+ -[FigCaptureSourceConfiguration initWithXPCEncoding:].cold.2
+ -[FigCaptureSourceConfiguration initWithXPCEncoding:].cold.3
+ -[FigCaptureSourceConfiguration initWithXPCEncoding:].cold.4
+ -[FigCaptureSourceConfiguration isEqual:].cold.1
+ -[FigCaptureSourceVideoFormat geometricDistortionCorrectedFieldOfView].cold.1
+ -[FigCaptureSourceVideoFormat initWithXPCEncoding:].cold.1
+ -[FigCaptureSourceVideoFormat initWithXPCEncoding:].cold.2
+ -[FigCaptureStillImageSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:captureStatusDelegate:inferenceScheduler:graph:name:].cold.1
+ -[FigCaptureStillImageSinkPipelineConfiguration isEqual:].cold.1
+ -[FigCaptureThermalMonitor init].cold.1
+ -[FigCaptureThermalMonitor init].cold.2
+ -[FigCaptureThermalMonitor init].cold.3
+ -[FigCaptureVideoConverter _newSampleBufferForPixelBuffer:pts:duration:].cold.1
+ -[FigCaptureVideoConverter _newSampleBufferForPixelBuffer:pts:duration:].cold.2
+ -[FigCaptureVideoThumbnailSinkConfiguration initWithXPCEncoding:].cold.1
+ -[FigIrisAutoTrimmer processCountOfVisibleVitalityObjects:forHostTime:].cold.1
+ -[FigIrisAutoTrimmer processISPMotionData:forHostTime:].cold.1
+ -[FigIrisAutoTrimmer processISPMotionData:forHostTime:].cold.2
+ -[FigMetadataObjectCaptureConnectionConfiguration attentionForFaceIDReadinessRequired]
+ -[FigMetadataObjectCaptureConnectionConfiguration faceOcclusionDetectionEnabled]
+ -[FigMetadataObjectCaptureConnectionConfiguration motionToWakeTargetFrameRate]
+ -[FigMetadataObjectCaptureConnectionConfiguration periocularForFaceIDReadinessEnabled]
+ -[FigMetadataObjectCaptureConnectionConfiguration setAttentionForFaceIDReadinessRequired:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setFaceOcclusionDetectionEnabled:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setMotionToWakeTargetFrameRate:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setPeriocularForFaceIDReadinessEnabled:]
+ -[FigSmartcamDiagnostics addMotionStats:].cold.1
+ -[GVSOverscanPredictor computeFocalLength:fromMetadata:].cold.1
+ -[GVSOverscanPredictor computeFocalLength:fromMetadata:].cold.2
+ -[GVSOverscanPredictor computeFocalLength:fromMetadata:].cold.3
+ -[GVSOverscanPredictor computeFocalLength:fromMetadata:].cold.4
+ -[GVSOverscanPredictor computeFocalLength:fromMetadata:].cold.5
+ -[GVSOverscanPredictor estimateOverscanUseFromMetadata:finalCropRect:].cold.1
+ -[GVSOverscanPredictor estimateOverscanUseFromMetadata:finalCropRect:].cold.2
+ -[GVSOverscanPredictor estimateOverscanUseFromMetadata:finalCropRect:].cold.3
+ -[GVSOverscanPredictor estimateOverscanUseFromMetadata:finalCropRect:].cold.4
+ -[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:].cold.1
+ -[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:].cold.2
+ -[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:].cold.3
+ -[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:].cold.4
+ -[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:].cold.5
+ -[GVSOverscanPredictor parseCameraInfoByPortType:].cold.1
+ -[GVSOverscanPredictor predictOverscanFitsFromMetadata:finalCropRect:boundingRect:].cold.1
+ -[GVSOverscanPredictor predictOverscanFitsFromMetadata:finalCropRect:boundingRect:].cold.2
+ -[GVSOverscanPredictor predictOverscanFitsFromMetadata:finalCropRect:boundingRect:].cold.3
+ -[GVSOverscanPredictor predictOverscanFitsFromMetadata:finalCropRect:boundingRect:].cold.4
+ BWCMSampleBufferCopyMetadataToSampleBuffer.cold.1
+ BWCMSampleBufferCopyMetadataToSampleBuffer.cold.2
+ BWCMSampleBufferCopyReattachAndReturnMutableMetadata.cold.1
+ BWCMSampleBufferCreateCopyIncludingMetadata.cold.1
+ BWCMSampleBufferCreateCopyWithNewTimingIncludingMetadata.cold.1
+ BWCMSampleBufferCreateCopyWithNewTimingIncludingMetadata.cold.2
+ BWCMSampleBufferCreateCopyWithNewTimingIncludingMetadata.cold.3
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.1
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.2
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.3
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.4
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.5
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.6
+ BWCMSampleBufferCreateDeepCopyWithNewPixelBuffer.cold.7
+ BWCaptureIsRunningInIOSAppOnMacEnvironment.cold.1
+ BWCaptureIsRunningInMacCatalystEnvironment.cold.1
+ BWCleanupRawStillImageSampleBuffer.cold.1
+ BWCreateDNGDictionaryForZoom.cold.1
+ BWCreateDNGDictionaryForZoom.cold.2
+ BWCreateDNGDictionaryForZoom.cold.3
+ BWCreateSampleBufferFromSemanticMasksDictionary.cold.1
+ BWCreateSampleBufferFromSemanticMasksDictionary.cold.2
+ BWCreateSampleBufferFromSemanticMasksDictionary.cold.3
+ BWCreateSampleBufferWithDetectedObjectsInfo.cold.1
+ BWCreateSampleBufferWithEyeReliefResultDictionary.cold.1
+ BWCreateSampleBufferWithFaceIDReadinessDictionary.cold.1
+ BWCreateSampleBufferWithMotionToWakeDictionary.cold.1
+ BWCreateSampleBufferWithTrackedFacesDictionary.cold.1
+ BWCropRectDimensionsForZoomFactor.cold.1
+ BWDetectedFacesConvertSampleBufferFacesFromSensorToBufferCoordinateSpace.cold.1
+ BWDetectedFacesConvertSampleBufferFacesFromSensorToBufferCoordinateSpace.cold.2
+ BWDetectedFacesConvertSampleBufferFacesFromSensorToBufferCoordinateSpace.cold.3
+ BWDetectedObjectsConvertSampleBufferDetectedObjectsFromSensorToBufferCoordinateSpace.cold.1
+ BWDetectedObjectsConvertSampleBufferDetectedObjectsFromSensorToBufferCoordinateSpace.cold.2
+ BWDetectedObjectsConvertSampleBufferDetectedObjectsFromSensorToBufferCoordinateSpace.cold.3
+ BWDeviceIsiPad.cold.1
+ BWDeviceIsiPhone.cold.1
+ BWDeviceSupportsCoreMediaFaceTracking.cold.1
+ BWDeviceSupportsDeferredPhotoProcessorPrewarming.cold.1
+ BWGetCurrentTotalNANDReadAndWriteBytes.cold.1
+ BWGetCurrentTotalNANDReadAndWriteBytes.cold.2
+ BWGetDataCapacityInBytes.cold.1
+ BWGetDiskCapacityInGB.cold.1
+ BWGetMaximumDisplayFrequency.cold.1
+ BWGetPixelBufferRotationAndMirroring.cold.1
+ BWOverCaptureSampleBufferUnpackAndRetain.cold.1
+ BWPreviewRegistrationTypeFromShortString.cold.1
+ BWPreviewSynchronizerCreate.cold.1
+ BWPreviewSynchronizerGetInsertionTime.cold.1
+ BWProcessorTuningParametersWithStandardStructure.cold.1
+ BWProcessorTuningParametersWithStandardStructure.cold.2
+ BWProcessorTuningParametersWithStandardStructure.cold.3
+ BWSampleBufferCreateAttachedMediaFromPixelBuffer.cold.1
+ BWSampleBufferCreateAttachedMediaFromPixelBuffer.cold.2
+ BWSampleBufferCreateAttachedMediaFromPixelBuffer.cold.3
+ BWSampleBufferCreateAttachedMediaFromPixelBuffer.cold.4
+ BWSampleBufferCreateAttachedMediaFromPixelBuffer.cold.5
+ BWSampleBufferCreateForDroppedFrame.cold.1
+ BWSampleBufferCreateForDroppedFrame.cold.2
+ BWSampleBufferCreateForDroppedFrame.cold.3
+ BWSampleBufferCreateFromBlockBuffer.cold.1
+ BWSampleBufferCreateFromBlockBuffer.cold.2
+ BWSampleBufferCreateFromBlockBuffer.cold.3
+ BWSampleBufferCreateFromBlockBuffer.cold.4
+ BWSampleBufferCreateFromDataBufferWithNumberOfPoints.cold.1
+ BWSampleBufferCreateFromDataBufferWithNumberOfPoints.cold.2
+ BWSampleBufferCreateFromDataBufferWithNumberOfPoints.cold.3
+ BWSampleBufferCreateFromDataBufferWithNumberOfPoints.cold.4
+ BWSampleBufferCreateFromDataBufferWithNumberOfPoints.cold.5
+ BWSampleBufferCreateFromEncodedImageSurface.cold.1
+ BWSampleBufferCreateFromEncodedImageSurface.cold.2
+ BWSampleBufferCreateFromEncodedImageSurface.cold.3
+ BWSampleBufferCreateFromEncodedImageSurface.cold.4
+ BWSampleBufferCreateFromEncodedImageSurface.cold.5
+ BWSampleBufferCreateFromEncodedImageSurface.cold.6
+ BWSampleBufferCreateFromEncodedImageSurface.cold.7
+ BWSampleBufferCreateFromPixelBufferWithTimingInfo.cold.1
+ BWSampleBufferCreateFromPixelBufferWithTimingInfo.cold.2
+ BWSampleBufferCreateFromPixelBufferWithTimingInfo.cold.3
+ BWSampleBufferCreateFromPixelBufferWithTimingInfo.cold.4
+ BWSampleBufferCreateFromPixelBufferWithTimingInfo.cold.5
+ BWSampleBufferSetAttachedMediaFromPixelBuffer.cold.1
+ BWStereoUtilitiesComputeRectificationQuaternion.cold.1
+ CMIOFigCaptureDeviceCreate.cold.1
+ CMIOFigCaptureDeviceCreate.cold.2
+ CMIOFigCaptureStreamCopyProperty.cold.1
+ CMIOFigCaptureStreamCopyProperty.cold.2
+ CMIOFigCaptureStreamCopyProperty.cold.3
+ CMIOFigCaptureStreamCopyProperty.cold.4
+ CMIOFigCaptureStreamCopyProperty.cold.5
+ CMIOFigCaptureStreamCreate.cold.1
+ CMIOFigCaptureStreamCreate.cold.10
+ CMIOFigCaptureStreamCreate.cold.11
+ CMIOFigCaptureStreamCreate.cold.12
+ CMIOFigCaptureStreamCreate.cold.13
+ CMIOFigCaptureStreamCreate.cold.14
+ CMIOFigCaptureStreamCreate.cold.15
+ CMIOFigCaptureStreamCreate.cold.2
+ CMIOFigCaptureStreamCreate.cold.3
+ CMIOFigCaptureStreamCreate.cold.4
+ CMIOFigCaptureStreamCreate.cold.5
+ CMIOFigCaptureStreamCreate.cold.6
+ CMIOFigCaptureStreamCreate.cold.7
+ CMIOFigCaptureStreamCreate.cold.8
+ CMIOFigCaptureStreamCreate.cold.9
+ CMIOFigCaptureStreamDoppelgangerCreate.cold.1
+ CMIOFigCaptureStreamNullCameraCreate.cold.1
+ CMIOFigCaptureStreamNullCameraCreate.cold.2
+ CMIOFigCaptureStreamNullCameraCreate.cold.3
+ CMIOFigCaptureStreamNullCameraCreate.cold.4
+ CMIOFigCaptureStreamNullCameraCreate.cold.5
+ FODMGTimeInMilliseconds.cold.1
+ FigAudioCaptureSourceCreateWithSourceInfo.cold.1
+ FigAudioCaptureSourceCreateWithSourceInfo.cold.2
+ FigCaptureBuildMotionAttachmentsNode.cold.1
+ FigCaptureBuildMotionAttachmentsNode.cold.2
+ FigCaptureBuildMotionAttachmentsNode.cold.3
+ FigCaptureBuildObjectDetectionPipeline.cold.1
+ FigCaptureBuildObjectDetectionPipeline.cold.2
+ FigCaptureCFCreatePropertyList.cold.1
+ FigCaptureCameraRequires180DegreesRotation.cold.1
+ FigCaptureCameracapturedEnabled.cold.1
+ FigCaptureCreateSourceInfoArrayFromDeviceAndGenericPlist.cold.1
+ FigCaptureDeferredContainerManagerGetClassID.cold.1
+ FigCaptureDeferredContainerManagerGetTypeID.cold.1
+ FigCaptureDeferredPhotoProcessorGetClassID.cold.1
+ FigCaptureDeferredPhotoProcessorGetTypeID.cold.1
+ FigCaptureDeviceCoreRepairStatusesByKeys.cold.1
+ FigCaptureDeviceCoreRepairStatusesByKeys.cold.2
+ FigCaptureDeviceIORegValuesByKeys.cold.1
+ FigCaptureDeviceIORegValuesByKeys.cold.2
+ FigCaptureExternalCameraReplacesBuiltIn.cold.1
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.1
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.2
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.3
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.4
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.5
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.6
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.7
+ FigCaptureFrameMetadataIsUsableForPTSBasedReferenceFrameSelection.cold.8
+ FigCaptureGetCameraDriverServiceName.cold.1
+ FigCaptureGetCaptureDeviceCreateFunction.cold.1
+ FigCaptureGetCurrentProcessAuditToken.cold.1
+ FigCaptureGetMacModelMajorVersion.cold.1
+ FigCaptureGetMacModelMinorVersion.cold.1
+ FigCaptureGetModelSpecificName.cold.1
+ FigCaptureGetTCCServer.cold.1
+ FigCaptureInitializeSingletons.cold.1
+ FigCaptureMetadataUtilitiesAddMissingDutyCycleMetadata.cold.1
+ FigCaptureMetadataUtilitiesAddSampleBufferMetadataUsedByVideoEncoderToPixelBuffer.cold.1
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRect.cold.1
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRect.cold.2
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRect.cold.3
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRect.cold.4
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRectForAttachedMedia.cold.1
+ FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRectForAttachedMedia.cold.2
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.1
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.10
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.11
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.12
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.13
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.14
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.15
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.16
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.17
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.18
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.19
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.2
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.20
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.3
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.4
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.5
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.6
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.7
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.8
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromDepthMetadata.cold.9
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromGainMapSampleBuffer.cold.1
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromGainMapSampleBuffer.cold.2
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromGainMapSampleBuffer.cold.3
+ FigCaptureMetadataUtilitiesCreateAuxiliaryImagePropertiesFromGainMapSampleBuffer.cold.4
+ FigCaptureMetadataUtilitiesCreateClientSpecifiedMetadataForAggd.cold.1
+ FigCaptureMetadataUtilitiesCreateClientSpecifiedMetadataForAggd.cold.2
+ FigCaptureMetadataUtilitiesCreateClientSpecifiedMetadataForOfflineStillImageVideoStabilization.cold.1
+ FigCaptureMetadataUtilitiesCreateClientSpecifiedMetadataForPanorama.cold.1
+ FigCaptureMetadataUtilitiesCreateDetectedObjectsInfoForCropRect.cold.1
+ FigCaptureMetadataUtilitiesCreateMakerNoteFlatDictionary.cold.1
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.1
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.2
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.3
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.4
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.5
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.6
+ FigCaptureMetadataUtilitiesCreateMetadataAttachments.cold.7
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.1
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.10
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.11
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.2
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.3
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.4
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.5
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.6
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.7
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.8
+ FigCaptureMetadataUtilitiesCreateQuickTimeMovieStillImageTimeSampleBuffer.cold.9
+ FigCaptureMetadataUtilitiesDevicePropertiesLockedForPanorama.cold.1
+ FigCaptureMetadataUtilitiesDevicePropertiesLockedForPanorama.cold.2
+ FigCaptureMetadataUtilitiesDevicePropertiesLockedForPanorama.cold.3
+ FigCaptureMetadataUtilitiesEnforceAspectRatioWithStillImageDimensions.cold.1
+ FigCaptureMetadataUtilitiesExifOrientationFromOrientationAndCameraPosition.cold.1
+ FigCaptureMetadataUtilitiesGetIrisAssetIdentifierForSettingsAndSampleBuffer.cold.1
+ FigCaptureMetadataUtilitiesGetStillImageMetadataInSettingsForSampleBuffer.cold.1
+ FigCaptureMetadataUtilitiesNormalizedBufferPointFromNormalizedSensorPoint.cold.1
+ FigCaptureMetadataUtilitiesNormalizedBufferPointFromNormalizedSensorPoint.cold.2
+ FigCaptureMetadataUtilitiesNormalizedBufferRectFromNormalizedSensorRect.cold.1
+ FigCaptureMetadataUtilitiesNormalizedBufferRectFromNormalizedSensorRect.cold.2
+ FigCaptureMetadataUtilitiesNormalizedSensorRectFromNormalizedBufferRect.cold.1
+ FigCaptureMetadataUtilitiesNormalizedSensorRectFromNormalizedBufferRect.cold.2
+ FigCaptureMetadataUtilitiesUpdateMetadataForNewFinalDimensions.cold.1
+ FigCaptureMetadataUtilitiesUpdateMetadataForStillImageCrop.cold.1
+ FigCaptureMetadataUtilitiesUpdateMetadataForStillImageCrop.cold.2
+ FigCaptureMetadataUtilitiesUpdateMetadataForStillImageCrop.cold.3
+ FigCaptureMetadataUtilitiesUpdateMetadataForStillImageCrop.cold.4
+ FigCapturePTSBasedReferenceFrameSelection.cold.1
+ FigCapturePTSBasedReferenceFrameSelection.cold.10
+ FigCapturePTSBasedReferenceFrameSelection.cold.11
+ FigCapturePTSBasedReferenceFrameSelection.cold.2
+ FigCapturePTSBasedReferenceFrameSelection.cold.3
+ FigCapturePTSBasedReferenceFrameSelection.cold.4
+ FigCapturePTSBasedReferenceFrameSelection.cold.5
+ FigCapturePTSBasedReferenceFrameSelection.cold.6
+ FigCapturePTSBasedReferenceFrameSelection.cold.7
+ FigCapturePTSBasedReferenceFrameSelection.cold.8
+ FigCapturePTSBasedReferenceFrameSelection.cold.9
+ FigCapturePlatformChipRevisionIdentifier.cold.1
+ FigCapturePlatformChipRevisionIdentifierString.cold.1
+ FigCapturePlatformGetISPHardwareCharacteristics.cold.1
+ FigCapturePlatformGetVariant.cold.1
+ FigCapturePlatformIOSurfaceWiringAssertionEnabled.cold.1
+ FigCapturePlatformIdentifier.cold.1
+ FigCapturePlatformIdentifierString.cold.1
+ FigCapturePlatformReconfigure.cold.1
+ FigCapturePlatformSupportsExclaves.cold.1
+ FigCapturePlatformSupportsHTPC16x8Compression.cold.1
+ FigCapturePlatformSupportsHTPC32x4Compression.cold.1
+ FigCapturePlatformSupportsUniversalCompression.cold.1
+ FigCapturePlatformSupportsUniversalLossyCompression.cold.1
+ FigCaptureReferenceFrameSelection.cold.1
+ FigCaptureReferenceFrameSelection.cold.2
+ FigCaptureReferenceFrameSelection.cold.3
+ FigCaptureReferenceFrameSelection.cold.4
+ FigCaptureSessionCreate.cold.1
+ FigCaptureSessionCreate.cold.2
+ FigCaptureSessionCreate.cold.3
+ FigCaptureSessionCreate.cold.4
+ FigCaptureSessionGetClassID.cold.1
+ FigCaptureSessionGetTypeID.cold.1
+ FigCaptureSessionPrewarm.cold.1
+ FigCaptureSessionPrewarm.cold.2
+ FigCaptureSmartStyleSettingsClearSystemStyleAndBackgroundedTimestampForBundleID.cold.1
+ FigCaptureSmartStyleSettingsGetSystemStyle.cold.1
+ FigCaptureSmartStyleSettingsGetSystemStyleBackgroundedTimestamp.cold.1
+ FigCaptureSmartStyleSettingsSetSystemStyle.cold.1
+ FigCaptureSmartStyleSettingsSetSystemStyleBackgroundedTimestamp.cold.1
+ FigCaptureSourceCopySourcesForClientAuditToken.cold.1
+ FigCaptureSourceGetClassID.cold.1
+ FigCaptureSourceGetTypeID.cold.1
+ FigCaptureSourceInitialize.cold.1
+ FigCaptureSourceInitialize.cold.2
+ FigCreateRGBAPixelBufferFromSegmentationMask.cold.1
+ FigCreateRGBAPixelBufferFromSegmentationMask.cold.2
+ FigCreateRGBAPixelBufferFromSegmentationMask.cold.3
+ FigCreateRGBAPixelBufferFromSegmentationMask.cold.4
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.1
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.2
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.3
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.4
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.5
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.6
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.7
+ FigDepthBlurEffectRenderingMaximumSimulatedAperture.cold.8
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.1
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.2
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.3
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.4
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.5
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.6
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.7
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.8
+ FigDepthBlurEffectRenderingMinimumSimulatedAperture.cold.9
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.1
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.2
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.3
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.4
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.5
+ FigDepthBlurEffectRenderingParametersV1FromCFData.cold.6
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.1
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.2
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.3
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.4
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.5
+ FigDepthBlurEffectRenderingParametersV2FromCFData.cold.6
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.1
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.2
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.3
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.4
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.5
+ FigDepthBlurEffectRenderingParametersV3FromCFData.cold.6
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.1
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.2
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.3
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.4
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.5
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.6
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.7
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.8
+ FigDepthBlurEffectRenderingParametersV4FromCFData.cold.9
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.1
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.2
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.3
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.4
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.5
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.6
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.7
+ FigDepthBlurEffectRenderingVersion4_GetParameter.cold.8
+ FigDepthConvertBuffer.cold.1
+ FigDepthConvertBuffer.cold.10
+ FigDepthConvertBuffer.cold.11
+ FigDepthConvertBuffer.cold.12
+ FigDepthConvertBuffer.cold.2
+ FigDepthConvertBuffer.cold.3
+ FigDepthConvertBuffer.cold.4
+ FigDepthConvertBuffer.cold.5
+ FigDepthConvertBuffer.cold.6
+ FigDepthConvertBuffer.cold.7
+ FigDepthConvertBuffer.cold.8
+ FigDepthConvertBuffer.cold.9
+ FigDepthConvertToRGBA.cold.1
+ FigDepthConvertToRGBA.cold.2
+ FigDepthConvertToRGBA.cold.3
+ FigDepthConvertToRGBA.cold.4
+ FigDepthConvertToRGBA.cold.5
+ FigDepthConvertToRGBA.cold.6
+ FigDepthConvertToRGBA.cold.7
+ FigDepthCreateRGBAPixelBufferFromInfraredPixelBuffer.cold.1
+ FigDepthCreateRGBAPixelBufferFromInfraredPixelBuffer.cold.2
+ FigDepthCreateRGBAPixelBufferFromInfraredPixelBuffer.cold.3
+ FigDepthRotateBuffer.cold.1
+ FigDepthRotateBuffer.cold.2
+ FigDepthRotateBuffer.cold.3
+ FigDepthRotateBuffer.cold.4
+ FigDepthRotateBuffer.cold.5
+ FigDepthRotateBuffer.cold.6
+ FigDepthRotateBuffer.cold.7
+ FigDepthRotateBuffer.cold.8
+ FigDepthRotateCalibrationData.cold.1
+ FigDepthRotateCalibrationData.cold.2
+ FigDepthScaleBufferWithCrop.cold.1
+ FigDepthScaleBufferWithCrop.cold.2
+ FigDepthScaleBufferWithCrop.cold.3
+ FigDepthScaleBufferWithCrop.cold.4
+ FigDraw420Rectangle.cold.1
+ FigFlashlightCreate.cold.1
+ FigFlashlightGetClassID.cold.1
+ FigFlashlightGetTypeID.cold.1
+ FigFlatDictionaryGetMakerNoteKeySpace.cold.1
+ FigFlatDictionaryKeySpaceRegister.cold.1
+ FigImageControl_Exposure.cold.1
+ FigImageControl_Exposure.cold.10
+ FigImageControl_Exposure.cold.11
+ FigImageControl_Exposure.cold.12
+ FigImageControl_Exposure.cold.13
+ FigImageControl_Exposure.cold.14
+ FigImageControl_Exposure.cold.15
+ FigImageControl_Exposure.cold.16
+ FigImageControl_Exposure.cold.17
+ FigImageControl_Exposure.cold.18
+ FigImageControl_Exposure.cold.19
+ FigImageControl_Exposure.cold.2
+ FigImageControl_Exposure.cold.20
+ FigImageControl_Exposure.cold.21
+ FigImageControl_Exposure.cold.22
+ FigImageControl_Exposure.cold.23
+ FigImageControl_Exposure.cold.24
+ FigImageControl_Exposure.cold.25
+ FigImageControl_Exposure.cold.26
+ FigImageControl_Exposure.cold.3
+ FigImageControl_Exposure.cold.4
+ FigImageControl_Exposure.cold.5
+ FigImageControl_Exposure.cold.6
+ FigImageControl_Exposure.cold.7
+ FigImageControl_Exposure.cold.8
+ FigImageControl_Exposure.cold.9
+ FigImageControl_Focus.cold.10
+ FigImageControl_Focus.cold.2
+ FigImageControl_Focus.cold.3
+ FigImageControl_Focus.cold.4
+ FigImageControl_Focus.cold.5
+ FigImageControl_Focus.cold.6
+ FigImageControl_Focus.cold.7
+ FigImageControl_Focus.cold.8
+ FigImageControl_Focus.cold.9
+ FigImageControl_Sharpness.cold.1
+ FigImageControl_Sharpness.cold.2
+ FigImageControl_Sharpness.cold.3
+ FigImageControl_Sharpness.cold.4
+ FigImageControl_VideoModeChange.cold.1
+ FigImageControl_VideoModeChange.cold.2
+ FigImageControl_VideoModeChange.cold.3
+ FigImageControl_VideoModeChange.cold.4
+ FigLivePhotoMetadataComputeDeserializationSize.cold.1
+ FigLivePhotoMetadataComputeDeserializationSize.cold.2
+ FigLivePhotoMetadataComputeDeserializationSize.cold.3
+ FigLivePhotoMetadataComputeDeserializationSize.cold.4
+ FigLivePhotoMetadataComputeDeserializationSize.cold.5
+ FigLivePhotoMetadataComputeDeserializationSize.cold.6
+ FigLivePhotoMetadataComputeDeserializationSize.cold.7
+ FigLivePhotoMetadataComputeDeserializationSize.cold.8
+ FigLivePhotoMetadataComputeDeserializationSize.cold.9
+ FigLivePhotoMetadataComputeSerializationSizeV3.cold.1
+ FigLivePhotoMetadataComputeSerializationSizeV3.cold.2
+ FigLivePhotoMetadataComputeSerializationSizeV3.cold.3
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.1
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.2
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.3
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.4
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.5
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.6
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.7
+ FigLivePhotoMetadataCreateSoftwareVersionSetupDataWithAtomHeader.cold.8
+ FigLocalQueueCreate.cold.1
+ FigLocalQueueCreate.cold.2
+ FigLocalQueueCreate.cold.3
+ FigLocalQueueCreate.cold.4
+ FigMotionAdjustPointForSphereMovement.cold.1
+ FigMotionAdjustPointForSphereMovement.cold.2
+ FigMotionCalculateAdjustedLensPosition.cold.1
+ FigMotionCalculateAdjustedLensPosition.cold.2
+ FigMotionCalculateAdjustedLensPosition.cold.3
+ FigMotionClearFocalLengthData.cold.1
+ FigMotionComputeAverageQuaternionFromArray.cold.1
+ FigMotionComputeAverageQuaternionFromArray.cold.2
+ FigMotionComputeAverageQuaternionFromArray.cold.3
+ FigMotionComputeAverageQuaternionFromArray.cold.4
+ FigMotionComputeAverageSpherePosition.cold.1
+ FigMotionComputeAverageSpherePosition.cold.2
+ FigMotionComputeAverageSpherePosition.cold.3
+ FigMotionComputeBlurScores.cold.1
+ FigMotionComputeBlurScores.cold.10
+ FigMotionComputeBlurScores.cold.11
+ FigMotionComputeBlurScores.cold.12
+ FigMotionComputeBlurScores.cold.13
+ FigMotionComputeBlurScores.cold.2
+ FigMotionComputeBlurScores.cold.3
+ FigMotionComputeBlurScores.cold.4
+ FigMotionComputeBlurScores.cold.5
+ FigMotionComputeBlurScores.cold.6
+ FigMotionComputeBlurScores.cold.7
+ FigMotionComputeBlurScores.cold.8
+ FigMotionComputeBlurScores.cold.9
+ FigMotionComputeBravoTranslation.cold.1
+ FigMotionComputeDistortionCenter.cold.1
+ FigMotionComputeDistortionCenter.cold.2
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.1
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.2
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.3
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.4
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.5
+ FigMotionComputeFramePTSOffsetFromISPCrop.cold.6
+ FigMotionComputeLensMovementAndSagForTimeStamp.cold.1
+ FigMotionComputeLensPositionScalingFactor.cold.1
+ FigMotionComputeLensPositionScalingFactor.cold.2
+ FigMotionComputeLensPositionScalingFactor.cold.3
+ FigMotionComputeLensPositionScalingFactor.cold.4
+ FigMotionComputeLensPositionScalingFactor.cold.5
+ FigMotionComputeQuaternionAndAttitudeFromArray.cold.1
+ FigMotionComputeQuaternionAndAttitudeFromArray.cold.2
+ FigMotionComputeQuaternionAndAttitudeFromArray.cold.3
+ FigMotionComputeRawSensorCenterInBuffer.cold.1
+ FigMotionComputeRawSensorCenterInBuffer.cold.2
+ FigMotionComputeRawSensorCenterInBuffer.cold.3
+ FigMotionComputeWideToNarrowShift.cold.1
+ FigMotionComputeWideToNarrowShift.cold.10
+ FigMotionComputeWideToNarrowShift.cold.11
+ FigMotionComputeWideToNarrowShift.cold.2
+ FigMotionComputeWideToNarrowShift.cold.3
+ FigMotionComputeWideToNarrowShift.cold.4
+ FigMotionComputeWideToNarrowShift.cold.5
+ FigMotionComputeWideToNarrowShift.cold.6
+ FigMotionComputeWideToNarrowShift.cold.7
+ FigMotionComputeWideToNarrowShift.cold.8
+ FigMotionComputeWideToNarrowShift.cold.9
+ FigMotionExtractCameraInfo.cold.1
+ FigMotionExtractCameraInfo.cold.2
+ FigMotionExtractCameraInfo.cold.3
+ FigMotionExtractCameraInfo.cold.4
+ FigMotionExtractCameraInfo.cold.5
+ FigMotionExtractCameraInfo.cold.6
+ FigMotionExtractCameraInfo.cold.7
+ FigMotionExtractCameraInfo.cold.8
+ FigMotionExtractCameraInfo.cold.9
+ FigMotionGetBravoDataFromDictionary.cold.1
+ FigMotionGetBravoDataFromDictionary.cold.2
+ FigMotionGetBravoDataFromDictionary.cold.3
+ FigMotionGetBravoDataFromDictionary.cold.4
+ FigMotionGetBravoDataFromDictionary.cold.5
+ FigMotionGetBravoDataFromDictionary.cold.6
+ FigMotionGetCameraCharacterizationData.cold.1
+ FigMotionGetCameraCharacterizationData.cold.2
+ FigMotionGetCameraCharacterizationData.cold.3
+ FigMotionGetCameraCharacterizationData.cold.4
+ FigMotionGetCameraCharacterizationData.cold.5
+ FigMotionGetCameraCharacterizationData.cold.6
+ FigMotionGetGravityFactor.cold.1
+ FigMotionGetGravityFactor.cold.2
+ FigMotionGetGravityFactor.cold.3
+ FigMotionGetGravityFactor.cold.4
+ FigMotionGetGravityZ.cold.1
+ FigMotionGetGravityZ.cold.2
+ FigMotionGetGravityZ.cold.3
+ FigMotionGetISPHallData.cold.1
+ FigMotionGetISPHallData.cold.2
+ FigMotionGetISPHallData.cold.3
+ FigMotionGetISPHallData.cold.4
+ FigMotionGetMotionDataFromISP.cold.1
+ FigMotionGetMotionDataFromISP.cold.2
+ FigMotionGetMotionDataFromISP.cold.3
+ FigMotionGetTimeStampAtPositionRatio.cold.1
+ FigMotionGetTimeStampAtPositionRatio.cold.2
+ FigMotionGetTimeStampAtPositionRatio.cold.3
+ FigMotionGetTimeStampAtPositionRatio.cold.4
+ FigMotionGetTimeStampAtPositionRatio.cold.5
+ FigMotionISPMotionDataFromCFData.cold.1
+ FigMotionISPMotionDataFromCFData.cold.2
+ FigMotionISPMotionDataFromCFData.cold.3
+ FigMotionISPMotionDataFromCFData.cold.4
+ FigMotionISPMotionDataFromCFData.cold.5
+ FigMotionMapPointFromRawToBuffer.cold.1
+ FigMotionMapPointFromRawToBuffer.cold.2
+ FigMotionNormalizeQuaternion.cold.1
+ FigMotionNormalizeQuaternion.cold.2
+ FigMotionSphereShiftStateInitialize.cold.1
+ FigMotionSphereShiftStateInitialize.cold.2
+ FigMotionSphereShiftStateUpdateWithMetadata.cold.1
+ FigMotionStashFocalLengthData.cold.1
+ FigMotionStashQuadraBinningFactor.cold.1
+ FigMotionUpdateBaseZoomFactorAdjustment.cold.1
+ FigProprietaryDefaultsCaptureSourceCreateWithSourceInfo.cold.1
+ FigProprietaryDefaultsCaptureSourceCreateWithSourceInfo.cold.2
+ FigRemoteOperationCleanupMessageData.cold.1
+ FigRemoteOperationCleanupMessageData.cold.2
+ FigRemoteOperationGetType.cold.1
+ FigRemoteOperationGetType.cold.2
+ FigRemoteOperationGetType.cold.3
+ FigRemoteOperationReceiverCreateMessageReceiver.cold.1
+ FigRemoteQueueIOSurfaceReceiver_ReleaseIOSurface.cold.1
+ FigRemoteQueueIOSurfaceReceiver_ReleaseIOSurface.cold.2
+ FigRemoteQueueIOSurfaceReceiver_ShareIOSurface.cold.1
+ FigRemoteQueueIOSurfaceReceiver_ShareIOSurface.cold.2
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.1
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.10
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.11
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.12
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.13
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.14
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.2
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.3
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.4
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.5
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.6
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.7
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.8
+ FigRemoteQueueReceiverCreateFromXPCObject.cold.9
+ FigRemoteQueueReceiverSetHandler.cold.1
+ FigRemoteQueueSenderCreate.cold.1
+ FigRemoteQueueSenderCreate.cold.10
+ FigRemoteQueueSenderCreate.cold.11
+ FigRemoteQueueSenderCreate.cold.12
+ FigRemoteQueueSenderCreate.cold.13
+ FigRemoteQueueSenderCreate.cold.14
+ FigRemoteQueueSenderCreate.cold.15
+ FigRemoteQueueSenderCreate.cold.16
+ FigRemoteQueueSenderCreate.cold.17
+ FigRemoteQueueSenderCreate.cold.18
+ FigRemoteQueueSenderCreate.cold.19
+ FigRemoteQueueSenderCreate.cold.2
+ FigRemoteQueueSenderCreate.cold.20
+ FigRemoteQueueSenderCreate.cold.3
+ FigRemoteQueueSenderCreate.cold.4
+ FigRemoteQueueSenderCreate.cold.5
+ FigRemoteQueueSenderCreate.cold.6
+ FigRemoteQueueSenderCreate.cold.7
+ FigRemoteQueueSenderCreate.cold.8
+ FigRemoteQueueSenderCreate.cold.9
+ FigRemoteQueueSenderCreateXPCObject.cold.1
+ FigRemoteQueueSenderCreateXPCObject.cold.2
+ FigRemoteQueueSenderCreateXPCObject.cold.3
+ FigRemoteQueueSenderCreateXPCObject.cold.4
+ FigRemoteQueueSenderCreateXPCObject.cold.5
+ FigRemoteQueueSenderCreateXPCObject.cold.6
+ FigRemoteQueueSenderCreateXPCObject.cold.7
+ FigSampleBufferAutofocusProcessorAddTimestampedMetadata.cold.1
+ FigSampleBufferAutofocusProcessorAddTimestampedMetadata.cold.2
+ FigSampleBufferAutofocusProcessorAddTimestampedMetadata.cold.3
+ FigSampleBufferProcessorCreateForAutofocus.cold.1
+ FigSampleBufferProcessorCreateForAutofocus.cold.2
+ FigSampleBufferProcessorCreateForAutofocus.cold.3
+ FigSampleBufferProcessorCreateForAutofocus.cold.4
+ FigSampleBufferProcessorCreateForAutofocus.cold.5
+ FigSampleBufferProcessorCreateForAutofocus.cold.6
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.1
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.10
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.11
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.12
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.13
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.14
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.15
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.16
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.17
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.2
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.3
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.4
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.5
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.6
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.7
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.8
+ FigSampleBufferProcessorCreateForMotionAttachments.cold.9
+ FigSerializedDepthImageBufferMetadataDeserializeIntoCVPixelBuffer.cold.1
+ FigSerializedDepthImageBufferMetadataDeserializeIntoCVPixelBuffer.cold.2
+ FigSerializedDepthImageBufferMetadataDeserializeIntoCVPixelBuffer.cold.3
+ FigSerializedDepthImageBufferMetadataDeserializeIntoCVPixelBuffer.cold.4
+ FigSerializedDepthImageBufferMetadataDeserializeIntoCVPixelBuffer.cold.5
+ FigSerializedDepthImageBufferMetadataSerializeIntoBuffer.cold.1
+ FigSharedMemBlockAllocate.cold.1
+ FigSharedMemBlockAllocate.cold.2
+ FigSharedMemBlockAllocate.cold.3
+ FigSharedMemBlockGetRegion.cold.1
+ FigSharedMemBlockGetRegion.cold.2
+ FigSharedMemBlockRelease.cold.1
+ FigSharedMemBlockRelease.cold.2
+ FigSharedMemBlockRetain.cold.1
+ FigSharedMemBlockRetain.cold.2
+ FigSharedMemPoolCreate.cold.1
+ FigSharedMemPoolCreate.cold.2
+ FigSharedMemPoolCreate.cold.3
+ FigSharedMemPoolCreate.cold.4
+ FigSharedMemPoolCreate.cold.5
+ FigSharedMemPoolCreate.cold.6
+ FigSharedMemPoolCreate.cold.7
+ FigSharedMemPoolCreate.cold.8
+ FigSharedMemPoolSharedRegionCreateFromXPCObject.cold.1
+ FigSharedMemPoolSharedRegionCreateFromXPCObject.cold.2
+ FigSharedMemPoolSharedRegionCreateFromXPCObject.cold.3
+ FigSharedMemPoolSharedRegionCreateFromXPCObject.cold.4
+ FigSharedMemPoolSharedRegionCreateFromXPCObject.cold.5
+ FigSharedMemPoolSharedRegionCreateXPCObject.cold.1
+ FigSharedMemPoolSharedRegionCreateXPCObject.cold.2
+ FigSharedMemPoolSharedRegionCreateXPCObject.cold.3
+ FigSharedMemPoolSharedRegionCreateXPCObject.cold.4
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.1
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.10
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.11
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.12
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.13
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.14
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.15
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.16
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.17
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.2
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.3
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.4
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.5
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.6
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.7
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.8
+ FigVideoCaptureSourceCreateWithSourceInfo.cold.9
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.1
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.10
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.11
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.12
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.13
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.14
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.15
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.2
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.3
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.4
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.5
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.6
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.7
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.8
+ FigVideoCaptureSourcesActivateAndCreateDevices.cold.9
+ FigVideoCaptureSourcesDeactivateWithDevices.cold.1
+ FigVideoCaptureSourcesDeactivateWithDevices.cold.2
+ GCC_except_table113
+ GCC_except_table126
+ GCC_except_table151
+ GCC_except_table18
+ GCC_except_table197
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table232
+ GCC_except_table258
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table326
+ GCC_except_table335
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table375
+ GCC_except_table395
+ GCC_except_table435
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table89
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.1
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.2
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.3
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.4
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.5
+ GetFocalLengthParametersFromArrayUsingModuleInfo.cold.6
+ GetFocalLengthParametersFromArrayUsingModuleLensID.cold.1
+ GetFocalLengthParametersFromArrayUsingModuleLensID.cold.2
+ GetFocalLengthParametersFromArrayUsingModuleLensID.cold.3
+ OBJC_IVAR_$_BWBackgroundBlurNode._suppressedGestureObserver
+ OBJC_IVAR_$_BWBackgroundBlurNode._suppressedGesturesEnabled
+ OBJC_IVAR_$_BWDepthConverterNode._inputCropRect
+ OBJC_IVAR_$_BWFigCaptureDevice._figCaptureSynchronizedStreamsGroups
+ OBJC_IVAR_$_BWFigCaptureDevice._streamsMapper
+ OBJC_IVAR_$_BWFigCaptureDeviceClient._clientType
+ OBJC_IVAR_$_BWFigCaptureDeviceVendorDeviceState._figCaptureDevice
+ OBJC_IVAR_$_BWFigCaptureDeviceVendorDeviceState._takeBackDeviceCalledForActiveClientID
+ OBJC_IVAR_$_BWFigCaptureStream._suppressedGestureHandler
+ OBJC_IVAR_$_BWFigCaptureStreamsMapper._bwFigCaptureStreams
+ OBJC_IVAR_$_BWFigCaptureStreamsMapper._figCaptureStreams
+ OBJC_IVAR_$_BWFigCaptureSynchronizedStreamsGroup._streamsMapper
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._hitPortraitInPhotoPreviewThermalPressure
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._latestPortraitInPhotoPreviewStartTime
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._longestContinuousPortraitInPhotoPreviewInMS
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._secureMetadataEnabled
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._suppressedGesturesEnabled
+ OBJC_IVAR_$_BWFigVideoCaptureStream._streamNotificationQueue
+ OBJC_IVAR_$_BWFigVideoCaptureStream._suppressedGesturesEnabled
+ OBJC_IVAR_$_BWFigVideoCaptureStream._willStopStreaming
+ OBJC_IVAR_$_BWFileCoordinatorNode._earliestPTSReceivedDuringStartingRecording
+ OBJC_IVAR_$_BWFileCoordinatorNode._latestPTSReceivedDuringStartingRecording
+ OBJC_IVAR_$_BWFileCoordinatorNode._numBuffersReceivedDuringStartingRecording
+ OBJC_IVAR_$_BWFlashlightAnalyticsPayload._luxLevel
+ OBJC_IVAR_$_BWGraph._preventSystemSleepAssertion
+ OBJC_IVAR_$_BWGraph._preventingSystemSleep
+ OBJC_IVAR_$_BWImageQueueSinkNode._triggerDisplayTimeout
+ OBJC_IVAR_$_BWIrisMovieInfo._isHardCut
+ OBJC_IVAR_$_BWMultiStreamCameraSourceNode._faceIDReadinessOutput
+ OBJC_IVAR_$_BWMultiStreamCameraSourceNode._motionToWakeOutput
+ OBJC_IVAR_$_BWNodeConnection._bypassConnection
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceIDReadinessAttentionRequired
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceIDReadinessEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceIDReadinessPeriocularEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceOcclusionDetectionEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceTrackingEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceTrackingFailureFieldOfViewModifier
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceTrackingMaxNumTrackedFaces
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._faceTrackingNetworkFailureThresholdMultiplier
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._motionToWakeEnabled
+ OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._motionToWakeTargetFrameRate
+ OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._hitPortraitInPhotoPreviewThermalPressure
+ OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._longestContinuousPortraitInPhotoPreviewInMS
+ OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._secureMetadataEnabled
+ OBJC_IVAR_$_FigCaptureBaseStillImageSinkPipelineConfiguration._depthDataSourceDimensions
+ OBJC_IVAR_$_FigCaptureBaseStillImageSinkPipelineConfiguration._depthDataTargetDimensions
+ OBJC_IVAR_$_FigCaptureCameraSourcePipeline._configuration
+ OBJC_IVAR_$_FigCaptureCameraSourcePipeline._faceIDReadinessOutputsBySourceDeviceType
+ OBJC_IVAR_$_FigCaptureCameraSourcePipeline._motionToWakeOutputsBySourceDeviceType
+ OBJC_IVAR_$_FigCaptureDeviceLockStateMonitor._notificationQueue
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._attentionForFaceIDReadinessRequired
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._faceOcclusionDetectionEnabled
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._motionToWakeTargetFrameRate
+ OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._periocularForFaceIDReadinessEnabled
+ _BWCreateSampleBufferWithFaceIDReadinessDictionary
+ _BWCreateSampleBufferWithMotionToWakeDictionary
+ _BWCreateSampleBufferWithTrackedFacesDictionary
+ _BWFigCaptureDeviceNotification_DeviceNoLongerAvailable
+ _BWFigCaptureDeviceNotification_UnrecoverableError
+ _BWFigVideoCaptureDeviceSuppressedGestureNotification
+ _BWStringForCacheMode
+ _FigCaptureClientApplicationIdentifierBiometricKitd
+ _FigCaptureClientLayoutStateToString
+ _FigCaptureMetadataObjectConfigurationRequiresFaceIDReadiness
+ _FigCaptureMetadataObjectConfigurationRequiresMotionToWake
+ _FigSampleBufferProcessorCopyProperty
+ _OBJC_CLASS_$_BWFigCaptureStreamsMapper
+ _OBJC_METACLASS_$_BWFigCaptureStreamsMapper
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_124
+ _OUTLINED_FUNCTION_125
+ _OUTLINED_FUNCTION_126
+ _OUTLINED_FUNCTION_127
+ _OUTLINED_FUNCTION_128
+ _OUTLINED_FUNCTION_129
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_130
+ _OUTLINED_FUNCTION_131
+ _OUTLINED_FUNCTION_132
+ _OUTLINED_FUNCTION_133
+ _OUTLINED_FUNCTION_134
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_136
+ _OUTLINED_FUNCTION_137
+ _OUTLINED_FUNCTION_138
+ _OUTLINED_FUNCTION_139
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_140
+ _OUTLINED_FUNCTION_141
+ _OUTLINED_FUNCTION_142
+ _OUTLINED_FUNCTION_143
+ _OUTLINED_FUNCTION_144
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_146
+ _OUTLINED_FUNCTION_147
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_149
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_150
+ _OUTLINED_FUNCTION_151
+ _OUTLINED_FUNCTION_152
+ _OUTLINED_FUNCTION_153
+ _OUTLINED_FUNCTION_154
+ _OUTLINED_FUNCTION_155
+ _OUTLINED_FUNCTION_156
+ _OUTLINED_FUNCTION_157
+ _OUTLINED_FUNCTION_158
+ _OUTLINED_FUNCTION_159
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_160
+ _OUTLINED_FUNCTION_161
+ _OUTLINED_FUNCTION_162
+ _OUTLINED_FUNCTION_163
+ _OUTLINED_FUNCTION_164
+ _OUTLINED_FUNCTION_165
+ _OUTLINED_FUNCTION_166
+ _OUTLINED_FUNCTION_167
+ _OUTLINED_FUNCTION_168
+ _OUTLINED_FUNCTION_169
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_170
+ _OUTLINED_FUNCTION_171
+ _OUTLINED_FUNCTION_172
+ _OUTLINED_FUNCTION_173
+ _OUTLINED_FUNCTION_174
+ _OUTLINED_FUNCTION_175
+ _OUTLINED_FUNCTION_176
+ _OUTLINED_FUNCTION_177
+ _OUTLINED_FUNCTION_178
+ _OUTLINED_FUNCTION_179
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_180
+ _OUTLINED_FUNCTION_181
+ _OUTLINED_FUNCTION_182
+ _OUTLINED_FUNCTION_183
+ _OUTLINED_FUNCTION_184
+ _OUTLINED_FUNCTION_185
+ _OUTLINED_FUNCTION_186
+ _OUTLINED_FUNCTION_187
+ _OUTLINED_FUNCTION_188
+ _OUTLINED_FUNCTION_189
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_190
+ _OUTLINED_FUNCTION_191
+ _OUTLINED_FUNCTION_192
+ _OUTLINED_FUNCTION_193
+ _OUTLINED_FUNCTION_194
+ _OUTLINED_FUNCTION_195
+ _OUTLINED_FUNCTION_196
+ _OUTLINED_FUNCTION_197
+ _OUTLINED_FUNCTION_198
+ _OUTLINED_FUNCTION_199
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_200
+ _OUTLINED_FUNCTION_201
+ _OUTLINED_FUNCTION_202
+ _OUTLINED_FUNCTION_203
+ _OUTLINED_FUNCTION_204
+ _OUTLINED_FUNCTION_205
+ _OUTLINED_FUNCTION_206
+ _OUTLINED_FUNCTION_207
+ _OUTLINED_FUNCTION_208
+ _OUTLINED_FUNCTION_209
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_210
+ _OUTLINED_FUNCTION_211
+ _OUTLINED_FUNCTION_212
+ _OUTLINED_FUNCTION_213
+ _OUTLINED_FUNCTION_214
+ _OUTLINED_FUNCTION_215
+ _OUTLINED_FUNCTION_216
+ _OUTLINED_FUNCTION_217
+ _OUTLINED_FUNCTION_218
+ _OUTLINED_FUNCTION_219
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_220
+ _OUTLINED_FUNCTION_221
+ _OUTLINED_FUNCTION_222
+ _OUTLINED_FUNCTION_223
+ _OUTLINED_FUNCTION_224
+ _OUTLINED_FUNCTION_225
+ _OUTLINED_FUNCTION_226
+ _OUTLINED_FUNCTION_227
+ _OUTLINED_FUNCTION_228
+ _OUTLINED_FUNCTION_229
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_230
+ _OUTLINED_FUNCTION_231
+ _OUTLINED_FUNCTION_232
+ _OUTLINED_FUNCTION_233
+ _OUTLINED_FUNCTION_234
+ _OUTLINED_FUNCTION_235
+ _OUTLINED_FUNCTION_236
+ _OUTLINED_FUNCTION_237
+ _OUTLINED_FUNCTION_238
+ _OUTLINED_FUNCTION_239
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_240
+ _OUTLINED_FUNCTION_241
+ _OUTLINED_FUNCTION_242
+ _OUTLINED_FUNCTION_243
+ _OUTLINED_FUNCTION_244
+ _OUTLINED_FUNCTION_245
+ _OUTLINED_FUNCTION_246
+ _OUTLINED_FUNCTION_247
+ _OUTLINED_FUNCTION_248
+ _OUTLINED_FUNCTION_249
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_250
+ _OUTLINED_FUNCTION_251
+ _OUTLINED_FUNCTION_252
+ _OUTLINED_FUNCTION_253
+ _OUTLINED_FUNCTION_254
+ _OUTLINED_FUNCTION_255
+ _OUTLINED_FUNCTION_256
+ _OUTLINED_FUNCTION_257
+ _OUTLINED_FUNCTION_258
+ _OUTLINED_FUNCTION_259
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_260
+ _OUTLINED_FUNCTION_261
+ _OUTLINED_FUNCTION_262
+ _OUTLINED_FUNCTION_263
+ _OUTLINED_FUNCTION_264
+ _OUTLINED_FUNCTION_265
+ _OUTLINED_FUNCTION_266
+ _OUTLINED_FUNCTION_267
+ _OUTLINED_FUNCTION_268
+ _OUTLINED_FUNCTION_269
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_270
+ _OUTLINED_FUNCTION_271
+ _OUTLINED_FUNCTION_272
+ _OUTLINED_FUNCTION_273
+ _OUTLINED_FUNCTION_274
+ _OUTLINED_FUNCTION_275
+ _OUTLINED_FUNCTION_276
+ _OUTLINED_FUNCTION_277
+ _OUTLINED_FUNCTION_278
+ _OUTLINED_FUNCTION_279
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_280
+ _OUTLINED_FUNCTION_281
+ _OUTLINED_FUNCTION_282
+ _OUTLINED_FUNCTION_283
+ _OUTLINED_FUNCTION_284
+ _OUTLINED_FUNCTION_285
+ _OUTLINED_FUNCTION_286
+ _OUTLINED_FUNCTION_287
+ _OUTLINED_FUNCTION_288
+ _OUTLINED_FUNCTION_289
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_290
+ _OUTLINED_FUNCTION_291
+ _OUTLINED_FUNCTION_292
+ _OUTLINED_FUNCTION_293
+ _OUTLINED_FUNCTION_294
+ _OUTLINED_FUNCTION_295
+ _OUTLINED_FUNCTION_296
+ _OUTLINED_FUNCTION_297
+ _OUTLINED_FUNCTION_298
+ _OUTLINED_FUNCTION_299
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_300
+ _OUTLINED_FUNCTION_301
+ _OUTLINED_FUNCTION_302
+ _OUTLINED_FUNCTION_303
+ _OUTLINED_FUNCTION_304
+ _OUTLINED_FUNCTION_305
+ _OUTLINED_FUNCTION_306
+ _OUTLINED_FUNCTION_307
+ _OUTLINED_FUNCTION_308
+ _OUTLINED_FUNCTION_309
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_310
+ _OUTLINED_FUNCTION_311
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_9
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ __112-[BWQuickTimeMovieFileSinkNode _generateThumbnailSurfaceFromPixelBuffer:physicallyMirroredHorizontallyUpstream:]_block_invoke.cold.1
+ __112-[BWQuickTimeMovieFileSinkNode _generateThumbnailSurfaceFromPixelBuffer:physicallyMirroredHorizontallyUpstream:]_block_invoke.cold.2
+ __112-[BWQuickTimeMovieFileSinkNode _generateThumbnailSurfaceFromPixelBuffer:physicallyMirroredHorizontallyUpstream:]_block_invoke.cold.3
+ __112-[BWQuickTimeMovieFileSinkNode _generateThumbnailSurfaceFromPixelBuffer:physicallyMirroredHorizontallyUpstream:]_block_invoke.cold.4
+ __114-[BWMultiStreamCameraSourceNode _updateOutputStorageWithSecureMetadataOutputConfiguration:propagateToNodeOutputs:]_block_invoke.cold.1
+ __115-[BWFigVideoCaptureDevice _serviceDeferredAutofocusProcessorPropertiesFromCaptureStream:frameStatisticsByPortType:]_block_invoke.cold.1
+ __115-[BWFigVideoCaptureDevice _serviceDeferredAutofocusProcessorPropertiesFromCaptureStream:frameStatisticsByPortType:]_block_invoke.cold.2
+ __35-[BWPhotoEncoderController prepare]_block_invoke.cold.1
+ __47-[BWFigVideoCaptureDevice setImageControlMode:]_block_invoke.cold.1
+ __51-[BWMetadataTimeMachine waitUntilCapacity:timeout:]_block_invoke.cold.1
+ __52-[BWDeferredDataIntermediate _setURL:prefetchQueue:]_block_invoke.cold.1
+ __53-[BWDeferredBufferIntermediate setURL:prefetchQueue:]_block_invoke.cold.1
+ __53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.965
+ __53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.965.cold.1
+ __53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.965.cold.2
+ __53-[BWStreamingFilterNode renderSampleBuffer:forInput:]_block_invoke.cold.1
+ __53-[BWStreamingFilterNode renderSampleBuffer:forInput:]_block_invoke.cold.2
+ __54-[FigCaptureSessionConfiguration initWithXPCEncoding:]_block_invoke.cold.1
+ __58-[BWFigCaptureSession _continuityDisplay:didUpdateLayout:]_block_invoke.cold.1
+ __59-[FigCaptureClientApplicationStateMonitor _initWithClient:]_block_invoke.276
+ __60-[BWFigCaptureDeviceVendor _setupDeviceCloseTimerForDevice:]_block_invoke.279
+ __60-[BWPreviewTimeMachineSinkNode renderSampleBuffer:forInput:]_block_invoke.cold.1
+ __62-[BWMultiStreamCameraSourceNode _registerStreamOutputHandlers]_block_invoke.1035
+ __62-[BWVideoOrientationMetadataNode renderSampleBuffer:forInput:]_block_invoke.cold.1
+ __70-[BWFigVideoCaptureDevice _setAutoImageControlMode:completionHandler:]_block_invoke.cold.1
+ __72-[BWPreviewRegistration allocateResourcesAsynchronouslyWithVideoFormat:]_block_invoke.cold.1
+ __76-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:figCaptureDevice:]_block_invoke.320
+ __77-[FigCaptureVideoConverter _newSampleBufferWithTargetFormatFromSampleBuffer:]_block_invoke.cold.1
+ __78-[BWStillImageConditionalRouterPersonSegmentationAndMattingConfiguration init]_block_invoke.cold.1
+ __80-[BWFigCaptureDeviceVendor structuredLightProjectorStandbyTemperatureWithError:]_block_invoke.cold.1
+ __80-[BWFigCaptureDeviceVendor structuredLightProjectorStandbyTemperatureWithError:]_block_invoke.cold.2
+ __80-[BWFigVideoCaptureDevice _sendInitialValuesToPortraitEffectPropertiesDelegate:]_block_invoke.822
+ __81-[BWFigCaptureDeviceVendor _handleStreamControlTakenByAnotherClientNotification:]_block_invoke.291
+ __81-[BWFigCaptureDeviceVendor _handleStreamRelinquishedByAnotherClientNotification:]_block_invoke.293
+ __82-[BWFigVideoCaptureDevice _initiateCaptureStillImageNowWithPTS:completionHandler:]_block_invoke.cold.1
+ __82-[BWFigVideoCaptureDevice _initiateCaptureStillImageNowWithPTS:completionHandler:]_block_invoke.cold.2
+ __87-[FigCaptureSystemPressureMonitor startMonitoringPearlProjectorTemperatureUntilNominal]_block_invoke.cold.1
+ __89-[BWFigVideoCaptureDevice _updateStreamingImageIntentForChangedMasterStreamWithPortType:]_block_invoke.cold.1
+ __FigCaptureExternalCameraReplacesBuiltIn_block_invoke.cold.1
+ __FigCaptureSourceInitialize_block_invoke.cold.1
+ __FigFlashlightCreate_block_invoke.23
+ __FigFlashlightCreate_block_invoke.32
+ __FigRemoteOperationReceiverCreateMessageReceiver_block_invoke.cold.1
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_BWFigCaptureStreamsMapper
+ __OBJC_$_INSTANCE_VARIABLES_BWFigCaptureStreamsMapper
+ __OBJC_CLASS_RO_$_BWFigCaptureStreamsMapper
+ __OBJC_METACLASS_RO_$_BWFigCaptureStreamsMapper
+ ___145-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithFlashlight:cameraStolenInterruptor:]_block_invoke
+ ___220-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:]_block_invoke
+ ___47-[BWFigCaptureDeviceVendor activeDeviceClients]_block_invoke
+ ___54-[BWFigVideoCaptureStream sourceNodeDidStopStreaming:]_block_invoke
+ ___55-[BWFigCaptureDeviceVendor controlledStreamsForDevice:]_block_invoke
+ ___63-[FigCaptureDeviceLockStateMonitor addDeviceLockStateObserver:]_block_invoke_2
+ ___76-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:figCaptureDevice:]_block_invoke
+ ___block_descriptor_101_e8_32o40o48r56r64r72r80r88r_e5_v8?0l
+ ___block_descriptor_48_e8_32o_e27_v28?0i8B12i16"NSString"20l
+ ___block_descriptor_49_e8_32o40o_e5_v8?0l
+ ___block_descriptor_55_e8_32o40o_e5_v8?0l
+ ___block_descriptor_86_e8_32o40o48o56b64r_e5_v8?0l
+ ___captureSession_cancelMemoryPoolPrewarmingLocked_block_invoke
+ ___cmiofcs_propertyListenerProc_block_invoke_3
+ ___copy_helper_block_e8_32o40o48r56r64r72r80r88r
+ ___destroy_helper_block_e8_32o40o48r56r64r72r80r88r
+ __block_literal_global.184
+ __block_literal_global.188
+ __block_literal_global.244
+ __block_literal_global.245
+ __block_literal_global.266
+ __block_literal_global.287
+ __block_literal_global.322
+ __block_literal_global.480
+ __block_literal_global.521
+ __block_literal_global.565
+ __block_literal_global.795
+ __block_literal_global.821
+ __block_literal_global.824
+ __block_literal_global.832
+ __block_literal_global.849
+ __block_literal_global.905
+ __block_literal_global.948
+ __block_literal_global.971
+ __captureSession_FileSinkPauseRecording_block_invoke.cold.1
+ __captureSession_FileSinkPauseRecording_block_invoke.cold.2
+ __captureSession_FileSinkResumeRecording_block_invoke.cold.1
+ __captureSession_FileSinkResumeRecording_block_invoke.cold.2
+ __captureSession_FileSinkStopRecording_block_invoke.cold.1
+ __captureSession_FileSinkStopRecording_block_invoke.cold.2
+ __captureSession_IrisStillImageSinkBeginMomentCapture_block_invoke.881
+ __captureSession_IrisStillImageSinkBeginMomentCapture_block_invoke.cold.1
+ __captureSession_IrisStillImageSinkBeginMomentCapture_block_invoke.cold.2
+ __captureSession_IrisStillImageSinkBeginMomentCapture_block_invoke.cold.3
+ __captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.903
+ __captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.cold.1
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.899
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.cold.1
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.893
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.cold.1
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.cold.2
+ __captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.cold.3
+ __captureSession_IrisStillImageSinkPrepareToCapture_block_invoke.cold.1
+ __captureSession_IrisStillImageSinkPrepareToCapture_block_invoke.cold.2
+ __captureSession_IrisStillImageSinkPrepareToCapture_block_invoke.cold.3
+ __captureSession_IrisStillImageSinkPrepareToCapture_block_invoke.cold.4
+ __captureSession_IrisStillImageSinkPrepareToCapture_block_invoke.cold.5
+ __captureSession_SetConfiguration_block_invoke.cold.1
+ __captureSession_SetConfiguration_block_invoke.cold.2
+ __captureSession_SetConfiguration_block_invoke.cold.3
+ __captureSession_SetConfiguration_block_invoke.cold.4
+ __captureSession_SetConfiguration_block_invoke.cold.5
+ __captureSession_StillImageSinkPrepareToCaptureBracket_block_invoke.cold.1
+ __captureSession_StillImageSinkPrepareToCaptureBracket_block_invoke.cold.2
+ __captureSession_StillImageSinkPrepareToCaptureBracket_block_invoke.cold.3
+ __captureSession_StillImageSinkPrepareToCaptureBracket_block_invoke.cold.4
+ __captureSession_StillImageSinkPrepareToCaptureBracket_block_invoke.cold.5
+ __captureSession_VisionDataSinkTriggerBurst_block_invoke.cold.1
+ __captureSession_VisionDataSinkTriggerBurst_block_invoke.cold.2
+ __captureSession_startAVConferenceBackgroundRunningTrackingTimerIfNeeded_block_invoke.cold.1
+ __captureSession_updateRunningCondition_block_invoke.587
+ __captureSession_updateRunningCondition_block_invoke.cold.1
+ __captureSession_updateRunningCondition_block_invoke.cold.2
+ __captureSource_LockForConfiguration_block_invoke.cold.1
+ __captureSource_UnlockForConfiguration_block_invoke.cold.1
+ __captureSource_handleDeviceNotification_block_invoke.113
+ __captureSource_handleDeviceNotification_block_invoke.114
+ __csu_removeUnsupportedDeviceFormatsAndDependentPresets_block_invoke.976
+ __csu_removeUnsupportedDeviceFormatsAndDependentPresets_block_invoke.976.cold.1
+ __csu_resolveSessionPresetAliases_block_invoke.cold.1
+ __fcmss_extractMacModelMajorAndMinorVersions_block_invoke.cold.1
+ _bwfcd_handleFigCaptureDeviceNotification
+ _captureSession_cancelMemoryPoolPrewarmingLocked
+ _captureSession_generateStateDump
+ _captureSession_updateSavedPreviewImageQueueUpdatedNotificationSent
+ _csu_addMetadataAttributes
+ _fcn_stringForRecordingState
+ _fcs_suppressedGesture
+ _fvcd_streamingImageIntentToString
+ _kCMContinuityCaptureProperty_SuppressedGesturesEnabled
+ _kFigCaptureMetadata_CorrespondingMetadataIdentifiers
+ _kFigCaptureSampleBufferAttachmentKey_FaceIDReadiness
+ _kFigCaptureSampleBufferAttachmentKey_MotionToWake
+ _kFigCaptureSessionNotificationPayloadKey_CameraStolenInterruptor
+ _kFigCaptureSourceAttributeKey_AvailableMetadataKeyGroups
+ _kFigCaptureSourceAttributeKey_AvailableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization
+ _kFigCaptureSourceAttributeKey_FaceOcclusionDetectionSupported
+ _kFigCaptureSourceMetadataKeyGroup_MRC
+ _kFigCaptureSourceMetadataKeyGroup_Misc
+ _kFigCaptureSourceMetadataKeyGroup_ObjectDetection
+ _kFigCaptureSourceMetadataKeyGroup_SecureMetadata
+ _kFigCaptureSourceNotification_SuppressedGestureNotification
+ _kFigCaptureSourceProperty_SuppressedGesturesEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureFaceIDReadiness
+ _kFigCaptureStreamMetadataOutputKey_SecureMotionToWake
+ _kFigCaptureStreamMetadataOutputKey_SecureTrackedFaces
+ _kFigCaptureStreamNotification_SuppressedGesture
+ _kFigCaptureStreamProperty_CMIOSuppressedGesturesEnabled
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_AttentionRequired
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_PeriocularEnabled
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NumTrackedFaces
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_TrackingFailureFieldOfViewModifier
+ _kFigCaptureStreamSecureMotionToWakeConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
+ _kFigCaptureSynchronizedStreamsGroupProperty_SynchronizationPrimaryStream
+ _kFigMetadataIdentifier_QuickTimeMetadataFaceIDReadiness
+ _kFigMetadataIdentifier_QuickTimeMetadataMotionToWake
+ _multiStreamCameraSourceNode_secureFaceIDReadinessServiceQueueCallback
+ _multiStreamCameraSourceNode_secureMotionToWakeServiceQueueCallback
+ _multiStreamCameraSourceNode_secureTrackedFacesServiceQueueCallback
+ _objc_msgSend$attentionForFaceIDReadinessRequired
+ _objc_msgSend$depthDataSourceDimensions
+ _objc_msgSend$depthDataTargetDimensions
+ _objc_msgSend$didChangeSuppressedGesturesEnabled:
+ _objc_msgSend$faceIDReadinessAttentionRequired
+ _objc_msgSend$faceIDReadinessEnabled
+ _objc_msgSend$faceIDReadinessOutput
+ _objc_msgSend$faceIDReadinessPeriocularEnabled
+ _objc_msgSend$faceOcclusionDetectionEnabled
+ _objc_msgSend$faceTrackingMaxNumTrackedFaces
+ _objc_msgSend$gestureCount
+ _objc_msgSend$imageQueueSinkNodeDidDisplayFirstFrame:timedOut:
+ _objc_msgSend$initWithDevice:figCaptureDevice:
+ _objc_msgSend$initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:
+ _objc_msgSend$initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:
+ _objc_msgSend$invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:
+ _objc_msgSend$isHardCut
+ _objc_msgSend$motionToWakeEnabled
+ _objc_msgSend$motionToWakeOutput
+ _objc_msgSend$motionToWakeTargetFrameRate
+ _objc_msgSend$periocularForFaceIDReadinessEnabled
+ _objc_msgSend$rebuildingGraphForTrueVideoTransition
+ _objc_msgSend$registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:
+ _objc_msgSend$registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:
+ _objc_msgSend$setAttentionForFaceIDReadinessRequired:
+ _objc_msgSend$setDepthDataSourceDimensions:
+ _objc_msgSend$setDepthDataTargetDimensions:
+ _objc_msgSend$setFaceIDReadinessAttentionRequired:
+ _objc_msgSend$setFaceIDReadinessEnabled:
+ _objc_msgSend$setFaceIDReadinessPeriocularEnabled:
+ _objc_msgSend$setFaceOcclusionDetectionEnabled:
+ _objc_msgSend$setFaceTrackingMaxNumTrackedFaces:
+ _objc_msgSend$setHitPortraitInPhotoPreviewThermalPressure:
+ _objc_msgSend$setIsHardCut:
+ _objc_msgSend$setLongestContinuousPortraitInPhotoPreviewInMS:
+ _objc_msgSend$setMotionToWakeEnabled:
+ _objc_msgSend$setMotionToWakeTargetFrameRate:
+ _objc_msgSend$setMotionToWakeTargetFrameRate:forSessionID:
+ _objc_msgSend$setPeriocularForFaceIDReadinessEnabled:
+ _objc_msgSend$setSecureMetadataEnabled:
+ _objc_msgSend$setSuppressGestureTriggeredReactions:
+ _objc_msgSend$setSuppressedGestureHandler:
+ _objc_msgSend$setSuppressedGesturesEnabled:
+ _objc_msgSend$setTakeBackDeviceCalledForActiveClientID:
+ _objc_msgSend$suppressGestureTriggeredReactions
+ _objc_msgSend$suppressedGestureHandler
+ _objc_msgSend$takeBackDeviceCalledForActiveClientID
+ _objc_msgSend$trackedFacesOutput
+ asn_audioUnitRenderProc.cold.1
+ asn_audioUnitRenderProc.cold.2
+ bbn_StringForPTEffectReactionType.cold.1
+ bravoTransitionCameraIndexFromPortType.cold.1
+ bravoTransitionCameraIndexFromPortType.cold.2
+ bwfcd_figCaptureDeviceStreamArrayChangedNoficationCallback.cold.1
+ bwfcd_figCaptureDeviceStreamArrayChangedNoficationCallback.cold.2
+ bwfcd_figCaptureDeviceStreamArrayChangedNoficationCallback.cold.3
+ bwfcd_figCaptureDeviceStreamArrayChangedNoficationCallback.cold.4
+ bwfcd_figCaptureDeviceStreamArrayChangedNoficationCallback.cold.5
+ bwfcd_handleFigCaptureDeviceNotification.cold.1
+ bwfcd_handleFigCaptureDeviceNotification.cold.2
+ bwfcd_handleFigCaptureDeviceNotification.cold.3
+ captureSession_CopyProperty.cold.1
+ captureSession_CopyProperty.cold.2
+ captureSession_FileSinkPauseRecording.cold.1
+ captureSession_FileSinkResumeRecording.cold.1
+ captureSession_FileSinkStartRecording.cold.1
+ captureSession_FileSinkStartRecording.cold.2
+ captureSession_FileSinkStartRecording.cold.3
+ captureSession_FileSinkStopRecording.cold.1
+ captureSession_IrisStillImageSinkBeginMomentCapture.cold.1
+ captureSession_IrisStillImageSinkBeginMomentCapture.cold.2
+ captureSession_IrisStillImageSinkBeginMomentCapture.cold.3
+ captureSession_IrisStillImageSinkCancelMomentCapture.cold.1
+ captureSession_IrisStillImageSinkCaptureImage.cold.1
+ captureSession_IrisStillImageSinkCaptureImage.cold.2
+ captureSession_IrisStillImageSinkCaptureImage.cold.3
+ captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording.cold.1
+ captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording.cold.2
+ captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording.cold.3
+ captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording.cold.4
+ captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture.cold.1
+ captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture.cold.2
+ captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture.cold.3
+ captureSession_IrisStillImageSinkEndMomentCapture.cold.1
+ captureSession_IrisStillImageSinkPrepareToCapture.cold.1
+ captureSession_IrisStillImageSinkPrepareToCapture.cold.2
+ captureSession_IrisStillImageSinkPrepareToCapture.cold.3
+ captureSession_SetConfiguration.cold.1
+ captureSession_SetConfiguration.cold.2
+ captureSession_SetProperty.cold.1
+ captureSession_SetProperty.cold.2
+ captureSession_SetProperty.cold.3
+ captureSession_StillImageSinkCaptureImage.cold.1
+ captureSession_StillImageSinkCaptureImage.cold.2
+ captureSession_StillImageSinkCaptureImage.cold.3
+ captureSession_StillImageSinkCaptureImage.cold.4
+ captureSession_StillImageSinkPrepareToCaptureBracket.cold.1
+ captureSession_StillImageSinkPrepareToCaptureBracket.cold.2
+ captureSession_StillImageSinkPrepareToCaptureBracket.cold.3
+ captureSession_VisionDataSinkTriggerBurst.cold.1
+ captureSession_buildGraphWithConfiguration.cold.1
+ captureSession_buildGraphWithConfiguration.cold.10
+ captureSession_buildGraphWithConfiguration.cold.11
+ captureSession_buildGraphWithConfiguration.cold.12
+ captureSession_buildGraphWithConfiguration.cold.13
+ captureSession_buildGraphWithConfiguration.cold.14
+ captureSession_buildGraphWithConfiguration.cold.15
+ captureSession_buildGraphWithConfiguration.cold.16
+ captureSession_buildGraphWithConfiguration.cold.17
+ captureSession_buildGraphWithConfiguration.cold.18
+ captureSession_buildGraphWithConfiguration.cold.19
+ captureSession_buildGraphWithConfiguration.cold.2
+ captureSession_buildGraphWithConfiguration.cold.20
+ captureSession_buildGraphWithConfiguration.cold.21
+ captureSession_buildGraphWithConfiguration.cold.22
+ captureSession_buildGraphWithConfiguration.cold.23
+ captureSession_buildGraphWithConfiguration.cold.24
+ captureSession_buildGraphWithConfiguration.cold.25
+ captureSession_buildGraphWithConfiguration.cold.26
+ captureSession_buildGraphWithConfiguration.cold.27
+ captureSession_buildGraphWithConfiguration.cold.28
+ captureSession_buildGraphWithConfiguration.cold.29
+ captureSession_buildGraphWithConfiguration.cold.3
+ captureSession_buildGraphWithConfiguration.cold.4
+ captureSession_buildGraphWithConfiguration.cold.5
+ captureSession_buildGraphWithConfiguration.cold.6
+ captureSession_buildGraphWithConfiguration.cold.7
+ captureSession_buildGraphWithConfiguration.cold.8
+ captureSession_buildGraphWithConfiguration.cold.9
+ captureSession_captureStillImageNow.cold.1
+ captureSession_captureStillImageNow.cold.2
+ captureSession_captureStillImageNow.cold.3
+ captureSession_captureStillImageNow.cold.4
+ captureSession_captureStillImageNow.cold.5
+ captureSession_captureStillImageNow.cold.6
+ captureSession_captureStillImageNow.cold.7
+ captureSession_captureStillImageNow.cold.8
+ captureSession_commitInflightConfiguration.cold.1
+ captureSession_createCameraSourcePipelineConfigurationFromParsedConfiguration.cold.1
+ captureSession_createCameraSourcePipelineConfigurationFromParsedConfiguration.cold.2
+ captureSession_createCameraSourcePipelineConfigurationFromParsedConfiguration.cold.3
+ captureSession_createMetadataSinkPipelineConfiguration.cold.1
+ captureSession_didCaptureIrisStill.cold.1
+ captureSession_fileStartRecording.cold.1
+ captureSession_fileStartRecording.cold.2
+ captureSession_fileStartRecording.cold.3
+ captureSession_fileStartRecording.cold.4
+ captureSession_fileStartRecording.cold.5
+ captureSession_generateStateDump.cold.1
+ captureSession_generateStateDump.cold.2
+ captureSession_generateStateDump.cold.3
+ captureSession_performBlockOnWorkerQueue.cold.1
+ captureSession_performBlockOnWorkerQueueSynchronously.cold.1
+ captureSession_postNotificationWithPayload.cold.1
+ captureSession_servicePendingIrisRecordings.cold.1
+ captureSession_servicePendingIrisRecordings.cold.2
+ captureSession_servicePendingIrisRecordings.cold.3
+ captureSession_setPreviewSinkProperty.cold.1
+ captureSession_setPreviewSinkProperty.cold.2
+ captureSession_setPreviewSinkProperty.cold.3
+ captureSession_shouldEnableDeferredNodePrepare.cold.1
+ captureSession_startDeferredGraphSetup.cold.1
+ captureSession_startDeferredGraphSetupWork.cold.1
+ captureSession_startGraph.cold.1
+ captureSession_startGraph.cold.2
+ captureSession_startGraph.cold.3
+ captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary.cold.1
+ captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary.cold.2
+ captureSession_stopGraph.cold.1
+ captureSession_stopRunningInternal.cold.1
+ captureSession_teardownGraph.cold.1
+ captureSession_teardownGraph.cold.2
+ captureSession_teardownGraph.cold.3
+ captureSession_transitionToSessionStatus.cold.1
+ captureSession_updateDeferredGraphSetupStartCondition.cold.1
+ captureSession_updateGraphConfiguration.cold.1
+ captureSession_updateGraphConfiguration.cold.10
+ captureSession_updateGraphConfiguration.cold.2
+ captureSession_updateGraphConfiguration.cold.3
+ captureSession_updateGraphConfiguration.cold.4
+ captureSession_updateGraphConfiguration.cold.5
+ captureSession_updateGraphConfiguration.cold.6
+ captureSession_updateGraphConfiguration.cold.7
+ captureSession_updateGraphConfiguration.cold.8
+ captureSession_updateGraphConfiguration.cold.9
+ captureSession_updateGraphConnectionEnabledState.cold.1
+ captureSession_updateGraphForVideoPreviewSinkConfigurationChanges.cold.1
+ captureSession_updateInflightConfigurationWithIrisSinkPropertyForKey.cold.1
+ captureSession_updateRunningCondition.cold.1
+ captureSession_waitForGraphToStart.cold.1
+ captureSource_CopyProperty.cold.1
+ captureSource_CopyProperty.cold.2
+ captureSource_CopyProperty.cold.3
+ captureSource_CopyProprietaryDefault.cold.1
+ captureSource_CopyProprietaryDefault.cold.2
+ captureSource_CopyWildcardProprietaryDefault.cold.1
+ captureSource_CopyWildcardProprietaryDefault.cold.2
+ captureSource_Invalidate.cold.1
+ captureSource_Invalidate.cold.2
+ captureSource_PerformReactionEffect.cold.1
+ captureSource_RegisterNotificationForProprietaryDefaultChanges.cold.1
+ captureSource_SetProprietaryDefault.cold.1
+ captureSource_SetWildcardProprietaryDefault.cold.1
+ captureSource_SetWildcardProprietaryDefault.cold.2
+ captureSource_UnregisterNotificationForProprietaryDefaultChanges.cold.1
+ captureSource_handleDeviceNotification.cold.1
+ captureSource_handleDeviceNotification.cold.2
+ captureSource_handleThirdPartyTorchLevelCommand.cold.1
+ captureSource_handleThirdPartyTorchLevelCommand.cold.2
+ captureSource_handleThirdPartyTorchLevelCommand.cold.3
+ captureSource_handleThirdPartyTorchLevelCommand.cold.4
+ captureSource_postNotificationWithPayload.cold.1
+ captureSource_postNotificationWithPayload.cold.2
+ captureSource_setDeskViewEnabled.cold.1
+ captureSource_setDeskViewEnabled.cold.2
+ captureSource_setExposureOperation.cold.1
+ captureSource_setExposureOperation.cold.2
+ captureSource_setExposureOperation.cold.3
+ captureSource_setExposureOperation.cold.4
+ captureSource_setExposureOperation.cold.5
+ captureSource_setExposureOperation.cold.6
+ captureSource_setExposureOperation.cold.7
+ captureSource_setExposureOperation.cold.8
+ captureSource_setExposureOperation.cold.9
+ captureSource_setExposureTargetBiasOperation.cold.1
+ captureSource_setFaceDrivenAEAFMode.cold.1
+ captureSource_setFaceDrivenAEAFMode.cold.2
+ captureSource_setFocusOperation.cold.1
+ captureSource_setFocusOperation.cold.2
+ captureSource_setFocusOperation.cold.3
+ captureSource_setFocusOperation.cold.4
+ captureSource_setFocusOperation.cold.5
+ captureSource_setPropertyInternal.cold.1
+ captureSource_setPropertyInternal.cold.10
+ captureSource_setPropertyInternal.cold.11
+ captureSource_setPropertyInternal.cold.12
+ captureSource_setPropertyInternal.cold.13
+ captureSource_setPropertyInternal.cold.14
+ captureSource_setPropertyInternal.cold.15
+ captureSource_setPropertyInternal.cold.16
+ captureSource_setPropertyInternal.cold.17
+ captureSource_setPropertyInternal.cold.18
+ captureSource_setPropertyInternal.cold.19
+ captureSource_setPropertyInternal.cold.2
+ captureSource_setPropertyInternal.cold.20
+ captureSource_setPropertyInternal.cold.21
+ captureSource_setPropertyInternal.cold.22
+ captureSource_setPropertyInternal.cold.23
+ captureSource_setPropertyInternal.cold.24
+ captureSource_setPropertyInternal.cold.25
+ captureSource_setPropertyInternal.cold.26
+ captureSource_setPropertyInternal.cold.27
+ captureSource_setPropertyInternal.cold.28
+ captureSource_setPropertyInternal.cold.29
+ captureSource_setPropertyInternal.cold.3
+ captureSource_setPropertyInternal.cold.30
+ captureSource_setPropertyInternal.cold.31
+ captureSource_setPropertyInternal.cold.32
+ captureSource_setPropertyInternal.cold.33
+ captureSource_setPropertyInternal.cold.34
+ captureSource_setPropertyInternal.cold.35
+ captureSource_setPropertyInternal.cold.36
+ captureSource_setPropertyInternal.cold.37
+ captureSource_setPropertyInternal.cold.38
+ captureSource_setPropertyInternal.cold.39
+ captureSource_setPropertyInternal.cold.4
+ captureSource_setPropertyInternal.cold.40
+ captureSource_setPropertyInternal.cold.41
+ captureSource_setPropertyInternal.cold.42
+ captureSource_setPropertyInternal.cold.43
+ captureSource_setPropertyInternal.cold.44
+ captureSource_setPropertyInternal.cold.45
+ captureSource_setPropertyInternal.cold.46
+ captureSource_setPropertyInternal.cold.47
+ captureSource_setPropertyInternal.cold.48
+ captureSource_setPropertyInternal.cold.49
+ captureSource_setPropertyInternal.cold.5
+ captureSource_setPropertyInternal.cold.50
+ captureSource_setPropertyInternal.cold.51
+ captureSource_setPropertyInternal.cold.52
+ captureSource_setPropertyInternal.cold.53
+ captureSource_setPropertyInternal.cold.54
+ captureSource_setPropertyInternal.cold.55
+ captureSource_setPropertyInternal.cold.6
+ captureSource_setPropertyInternal.cold.7
+ captureSource_setPropertyInternal.cold.8
+ captureSource_setPropertyInternal.cold.9
+ captureSource_setPropertyWithDeviceCheck.cold.1
+ captureSource_setPropertyWithDeviceCheck.cold.2
+ captureSource_setPropertyWithDeviceCheck.cold.3
+ captureSource_setPropertyWithDeviceCheck.cold.4
+ captureSource_setPropertyWithDeviceCheck.cold.5
+ captureSource_setWhiteBalanceOperation.cold.1
+ captureSource_setWhiteBalanceOperation.cold.2
+ captureSource_setWhiteBalanceOperation.cold.3
+ captureSource_setWhiteBalanceOperation.cold.4
+ cmiofcs_captureAsyncStillImage.cold.1
+ cmiofcs_captureAsyncStillImage.cold.2
+ cmiofcs_captureAsyncStillImage.cold.3
+ cmiofcs_copyMaxFrameRate.cold.1
+ cmiofcs_copyMinFrameRate.cold.1
+ cmiofcs_copyMinFrameRate.cold.2
+ cmiofcs_copySupportedFormatsArray.cold.1
+ cmiofcs_copySupportedFormatsArray.cold.2
+ cmiofcs_copySupportedFormatsArray.cold.3
+ cmiofcs_copySupportedFormatsArray.cold.4
+ cmiofcs_copySupportedPropertiesDict.cold.1
+ cmiofcs_copySupportedPropertiesDict.cold.2
+ cmiofcs_copySupportedPropertiesDict.cold.3
+ cmiofcs_copySupportedPropertiesDict.cold.4
+ cmiofcs_createTargetFormatDescription.cold.1
+ cmiofcs_createTargetFormatDescription.cold.2
+ cmiofcs_emitBlackSampleBuffer.cold.1
+ cmiofcs_emitBlackSampleBuffer.cold.2
+ cmiofcs_emitBlackSampleBuffer.cold.3
+ cmiofcs_emitBlackSampleBuffer.cold.4
+ cmiofcs_emitBlackSampleBuffer.cold.5
+ cmiofcs_processConvertedSampleBuffer.cold.1
+ cmiofcs_propertyListenerProc.cold.1
+ cmiofcs_propertyListenerProc.cold.2
+ cmiofcs_propertyListenerProc.cold.3
+ cmiofcs_propertyListenerProc.cold.4
+ cmiofcs_propertyListenerProc.cold.5
+ cmiofcs_propertyListenerProc.cold.6
+ cmiofcs_propertyListenerProc.cold.7
+ cmiofcs_propertyListenerProc.cold.8
+ cmiofcs_propertyListenerProc.cold.9
+ cmiofcs_setAsyncStillCaptureConfigurations.cold.1
+ cmiofcs_setAsyncStillCaptureConfigurations.cold.2
+ cmiofcs_setAsyncStillCaptureConfigurations.cold.3
+ cmiofcs_setContinuousAutoExposureEnabled.cold.1
+ cmiofcs_setContinuousAutoExposureEnabled.cold.2
+ cmiofcs_setContinuousAutoFocusEnabled.cold.1
+ cmiofcs_setContinuousAutoFocusEnabled.cold.2
+ cmiofcs_setContinuousAutoWhiteBalanceEnabled.cold.1
+ cmiofcs_setContinuousAutoWhiteBalanceEnabled.cold.2
+ cmiofcs_setContinuousAutoWhiteBalanceEnabled.cold.3
+ cmiofcs_setFormatIndex.cold.1
+ cmiofcs_setFormatIndex.cold.2
+ cmiofcs_setManualFocusWithLensPosition.cold.1
+ cmiofcs_setManualFocusWithLensPosition.cold.2
+ cmiofcs_setManualFocusWithLensPosition.cold.3
+ cmiofcs_setManualFocusWithLensPosition.cold.4
+ cmiofcs_setManualFocusWithLensPosition.cold.5
+ cmiofcs_setObjectDetectionConfiguration.cold.1
+ cmiofcs_setObjectDetectionConfiguration.cold.2
+ cmiofcs_setVideoOutputConfigurations.cold.1
+ cmiofcs_setVideoOutputConfigurations.cold.2
+ cmiofcs_setVideoOutputHandlers.cold.1
+ cmiofcs_setVideoOutputHandlers.cold.2
+ cmiofcs_setVideoOutputsEnabled.cold.1
+ cmiofcs_setVideoOutputsEnabled.cold.2
+ cmiofcs_setVideoOutputsEnabled.cold.3
+ cmiofcs_setVideoOutputsEnabled.cold.4
+ cmiofcs_setVideoZoomFactor.cold.1
+ cmiofcs_streamAsyncStillCaptureCallback.cold.1
+ cmiofcs_streamAsyncStillCaptureCallback.cold.2
+ cmiofcs_streamAsyncStillCaptureCallback.cold.3
+ cmiofcs_streamAsyncStillCaptureCallback.cold.4
+ cmiofcs_streamAsyncStillCaptureCallback.cold.5
+ configureDevice.cold.1
+ configureDevice.cold.2
+ configureDevice.cold.3
+ configureDevice.cold.4
+ configureDevice.cold.5
+ configureDevice.cold.6
+ configureDevice.cold.7
+ configureDevice.cold.8
+ cs_IrisStillImageSinkPrepareMovieRecording.cold.1
+ cs_actionCamera2p8kOutputDimensions.cold.1
+ cs_applyCompressionPropertiesOverridesForSmartStyleReversibility.cold.1
+ cs_removeEmptyPendingIrisRecording.cold.1
+ cs_shouldEnableOverCapture.cold.1
+ cs_structuredLightAFAssistHandleStructuredLightAFAssistStreamControlRelinquishedByAnotherClientNotification.cold.1
+ cs_structuredLightAFAssistHandleStructuredLightAFAssistStreamControlRelinquishedByAnotherClientNotification.cold.2
+ cs_structuredLightAFAssistHandleStructuredLightAFAssistStreamControlRelinquishedByAnotherClientNotification.cold.3
+ cs_structuredLightAFAssistHandleStructuredLightAFAssistStreamControlTakenByAnotherClientNotification.cold.1
+ cs_structuredLightAFAssistHandleStructuredLightAFAssistStreamControlTakenByAnotherClientNotification.cold.2
+ cs_structuredLightAFAssistHandleStructuredLightAFTargetStreamStartedNotification.cold.1
+ cs_structuredLightAFAssistHandleStructuredLightAFTargetStreamStoppedNotification.cold.1
+ cs_updateStructuredLightAFEnabledStatus.cold.1
+ cs_updateStructuredLightAFEnabledStatus.cold.2
+ cs_updateTimeOfFlightAFEnabledStatus.cold.1
+ cso_postDeferredmediadImmediateTerminationNotificationIfNecessary.cold.1
+ csp_configureMultiStreamCameraNode.cold.1
+ csp_configureMultiStreamCameraNode.cold.10
+ csp_configureMultiStreamCameraNode.cold.11
+ csp_configureMultiStreamCameraNode.cold.12
+ csp_configureMultiStreamCameraNode.cold.2
+ csp_configureMultiStreamCameraNode.cold.3
+ csp_configureMultiStreamCameraNode.cold.4
+ csp_configureMultiStreamCameraNode.cold.5
+ csp_configureMultiStreamCameraNode.cold.6
+ csp_configureMultiStreamCameraNode.cold.7
+ csp_configureMultiStreamCameraNode.cold.8
+ csp_configureMultiStreamCameraNode.cold.9
+ csu_createBackingsFromAVCaptureSessionPlistForCaptureDeviceIDs.cold.1
+ csu_createSourceFormatDictFromDeviceFormat.cold.1
+ csu_createVideoCaptureSourceInfoForCaptureDeviceFromModelSpecificPlist.cold.1
+ csu_streamArrayChangedNotificationCallback.cold.1
+ csu_streamArrayChangedNotificationCallback.cold.2
+ csu_streamArrayChangedNotificationCallback.cold.3
+ dcn_convertU16toFloatForImage_NEON.cold.1
+ dcn_convertU16toFloatForImage_NEON.cold.2
+ doAutofocusNow.cold.1
+ doAutofocusNow.cold.2
+ doFocusNow.cold.1
+ doFocusNow.cold.2
+ doPeakTrackingAutofocusNow.cold.1
+ doPeakTrackingAutofocusNow.cold.2
+ exposure_table_create_lookup_table.cold.1
+ exposure_table_create_lookup_table.cold.2
+ exposure_table_create_lookup_table.cold.3
+ exposure_table_create_lookup_table.cold.4
+ exposure_table_fill_metric.cold.1
+ exposure_table_fill_metric.cold.2
+ exposure_table_fill_metric.cold.3
+ exposure_table_initialize.cold.1
+ exposure_table_initialize.cold.10
+ exposure_table_initialize.cold.2
+ exposure_table_initialize.cold.3
+ exposure_table_initialize.cold.4
+ exposure_table_initialize.cold.5
+ exposure_table_initialize.cold.6
+ exposure_table_initialize.cold.7
+ exposure_table_initialize.cold.8
+ exposure_table_initialize.cold.9
+ fcmu_makerNoteMetadata.cold.1
+ fcmu_makerNoteMetadata.cold.2
+ fcsc_deserializeDataUsingNSSecureCoding.cold.1
+ figDepthClampAndInvertFloat32_C.cold.1
+ figDepthClampAndInvertFloat32_C.cold.2
+ figDepthConvertBufferFloat16ToFloat32.cold.1
+ figDepthConvertBufferFloat32ToFloat16.cold.1
+ findOffsetFromSums.cold.1
+ findOffsetFromSums.cold.2
+ flashlight_SetBeamWidth.cold.1
+ flashlight_SetLevel.cold.1
+ flashlight_SetLevel.cold.2
+ flashlight_SetLevel.cold.3
+ flashlight_postNotificationWithPayload.cold.1
+ flashlight_setLevelInternal.cold.1
+ flashlight_setupDevice.cold.1
+ flashlight_setupDevice.cold.2
+ fvcd_handleAutofocusProcessorNotification.cold.1
+ fvcd_handleAutofocusProcessorNotification.cold.2
+ gr_countOfBuffersRetainedOutsideEmitCallbackOfOutputWithDelay.cold.1
+ hallPositionIndexFromPortType.cold.1
+ hallPositionIndexFromPortType.cold.2
+ mfsp_buildMovieFileScalerNode.cold.1
+ mfsp_buildMovieFileScalerNode.cold.2
+ mrcn_createSampleBufferProcessor.cold.1
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.1
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.10
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.11
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.12
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.2
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.3
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.4
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.5
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.6
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.7
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.8
+ mscsn_createScaledAndZoomedSampleBufferFromSampleBuffer.cold.9
+ mscsn_streamOutputIndexForOutputID.cold.1
+ multiStreamCameraSourceNode_serviceQueue.cold.1
+ multiStreamCameraSourceNode_serviceQueue.cold.10
+ multiStreamCameraSourceNode_serviceQueue.cold.11
+ multiStreamCameraSourceNode_serviceQueue.cold.12
+ multiStreamCameraSourceNode_serviceQueue.cold.13
+ multiStreamCameraSourceNode_serviceQueue.cold.14
+ multiStreamCameraSourceNode_serviceQueue.cold.15
+ multiStreamCameraSourceNode_serviceQueue.cold.16
+ multiStreamCameraSourceNode_serviceQueue.cold.17
+ multiStreamCameraSourceNode_serviceQueue.cold.18
+ multiStreamCameraSourceNode_serviceQueue.cold.2
+ multiStreamCameraSourceNode_serviceQueue.cold.3
+ multiStreamCameraSourceNode_serviceQueue.cold.4
+ multiStreamCameraSourceNode_serviceQueue.cold.5
+ multiStreamCameraSourceNode_serviceQueue.cold.6
+ multiStreamCameraSourceNode_serviceQueue.cold.7
+ multiStreamCameraSourceNode_serviceQueue.cold.8
+ multiStreamCameraSourceNode_serviceQueue.cold.9
+ nrasp_interpolateValueForGain.cold.1
+ nrasp_interpolateValueForGain.cold.2
+ pgs_computeTransformFromCameraMotion.cold.1
+ pixelSumForROI.cold.1
+ pixelSumForROI.cold.2
+ pixelSumForROI.cold.3
+ pixelSumForROI.cold.4
+ pixelSumForROI.cold.5
+ pixelSumForROI.cold.6
+ pixelSumForROI.cold.7
+ portIndexFromPortType.cold.1
+ portIndexFromPortType.cold.2
+ processBuffer.cold.1
+ processBuffer.cold.10
+ processBuffer.cold.11
+ processBuffer.cold.12
+ processBuffer.cold.13
+ processBuffer.cold.2
+ processBuffer.cold.3
+ processBuffer.cold.4
+ processBuffer.cold.5
+ processBuffer.cold.6
+ processBuffer.cold.7
+ processBuffer.cold.8
+ processBuffer.cold.9
+ qtrmg_getTrackTimescale.cold.1
+ qtrmg_getTrackTimescale.cold.2
+ qtrmg_metadataTrackWithIDShouldBePropagated.cold.1
+ qtrmg_metadataTrackWithIDShouldBePropagated.cold.2
+ qtrmg_metadataTrackWithIDShouldBePropagated.cold.3
+ qtrmg_setupMetadataTrackReferences.cold.1
+ qtrmg_trackIDForNextTrackBelowWater.cold.1
+ qtrmg_writeStillImageTimeMetadataSample.cold.1
+ qtrmg_writeStillImageTimeMetadataSample.cold.2
+ qtrmg_writeStillImageTimeMetadataSample.cold.3
+ qtrmg_writeVideoOrientationMetadataSamples.cold.1
+ qtrmg_writeVideoOrientationMetadataSamples.cold.2
+ qtrmg_writeVideoOrientationMetadataSamples.cold.3
+ roCleanupConfigurationLiveOperation.cold.1
+ roCleanupDictionaryPayloadOperation.cold.1
+ roCleanupFormatDescriptionOperation.cold.1
+ roCleanupIOSurfaceOperation.cold.1
+ roCleanupSampleBufferOperation.cold.1
+ roCreateBlockBufferWrapper.cold.1
+ roCreateBlockBufferWrapper.cold.2
+ roCreateBlockBufferWrapper.cold.3
+ roDeserializeConfigurationLive.cold.1
+ roDeserializeConfigurationLive.cold.2
+ roDeserializeConfigurationLive.cold.3
+ roDeserializeConfigurationLive.cold.4
+ roDeserializeDictionaryPayload.cold.1
+ roDeserializeDictionaryPayload.cold.2
+ roDeserializeDictionaryPayload.cold.3
+ roDeserializeDictionaryPayload.cold.4
+ roDeserializeDictionaryPayload.cold.5
+ roDeserializeDictionaryPayload.cold.6
+ roDeserializeDictionaryPayload.cold.7
+ roDeserializeDictionaryPayload.cold.8
+ roDeserializeFormatDescription.cold.1
+ roDeserializeFormatDescription.cold.2
+ roDeserializeFormatDescription.cold.3
+ roDeserializeFormatDescription.cold.4
+ roDeserializeIOSurface.cold.1
+ roDeserializeIOSurface.cold.2
+ roDeserializeIOSurface.cold.3
+ roDeserializeIOSurface.cold.4
+ roDeserializeIOSurface.cold.5
+ roDeserializePropertyListData.cold.1
+ roDeserializePropertyListData.cold.2
+ roDeserializePropertyListData.cold.3
+ roDeserializeSampleBuffer.cold.1
+ roDeserializeSampleBuffer.cold.2
+ roDeserializeSampleBuffer.cold.3
+ roEnqueue.cold.1
+ roEnqueue.cold.2
+ roEnqueue.cold.3
+ roEnqueueConfigurationLive.cold.1
+ roEnqueueConfigurationLive.cold.2
+ roEnqueueConfigurationLive.cold.3
+ roEnqueueConfigurationLive.cold.4
+ roEnqueueConfigurationLive.cold.5
+ roEnqueueConfigurationLive.cold.6
+ roEnqueueDictionaryPayload.cold.1
+ roEnqueueDictionaryPayload.cold.10
+ roEnqueueDictionaryPayload.cold.11
+ roEnqueueDictionaryPayload.cold.12
+ roEnqueueDictionaryPayload.cold.2
+ roEnqueueDictionaryPayload.cold.3
+ roEnqueueDictionaryPayload.cold.4
+ roEnqueueDictionaryPayload.cold.5
+ roEnqueueDictionaryPayload.cold.6
+ roEnqueueDictionaryPayload.cold.7
+ roEnqueueDictionaryPayload.cold.8
+ roEnqueueDictionaryPayload.cold.9
+ roEnqueueFormatDescription.cold.1
+ roEnqueueFormatDescription.cold.2
+ roEnqueueFormatDescription.cold.3
+ roEnqueueFormatDescription.cold.4
+ roEnqueueFormatDescription.cold.5
+ roEnqueueFormatDescription.cold.6
+ roEnqueueIOSurface.cold.1
+ roEnqueueIOSurface.cold.2
+ roEnqueueIOSurface.cold.3
+ roEnqueueIOSurface.cold.4
+ roEnqueueIOSurface.cold.5
+ roEnqueueSampleBuffer.cold.1
+ roEnqueueSampleBuffer.cold.2
+ roEnqueueSampleBuffer.cold.3
+ roEnqueueSampleBuffer.cold.4
+ roEnqueueSampleBuffer.cold.5
+ roSerializationContextGetCacheForName.cold.1
+ roSerializationContextGetCacheForName.cold.2
+ roSerializationContextGetNameForCache.cold.1
+ roSerializePropertyListData.cold.1
+ roSerializePropertyListData.cold.2
+ roSerializePropertyListData.cold.3
+ roSerializePropertyListData.cold.4
+ rqReceiverDequeue.cold.1
+ rqSenderEnqueue.cold.1
+ rqSenderEnqueue.cold.2
+ rqSenderEnqueue.cold.3
+ rqSenderFinalize.cold.1
+ rqSenderHandleDequeue.cold.1
+ rqSenderHandleDequeue.cold.2
+ rqSenderReset.cold.1
+ rqSenderReset.cold.2
+ rqSenderReset.cold.3
+ rqSenderReset.cold.4
+ sbp_ma_addMotionDataToMetadataDictionary.cold.1
+ sbp_ma_addMotionDataToMetadataDictionary.cold.10
+ sbp_ma_addMotionDataToMetadataDictionary.cold.11
+ sbp_ma_addMotionDataToMetadataDictionary.cold.12
+ sbp_ma_addMotionDataToMetadataDictionary.cold.13
+ sbp_ma_addMotionDataToMetadataDictionary.cold.14
+ sbp_ma_addMotionDataToMetadataDictionary.cold.15
+ sbp_ma_addMotionDataToMetadataDictionary.cold.2
+ sbp_ma_addMotionDataToMetadataDictionary.cold.3
+ sbp_ma_addMotionDataToMetadataDictionary.cold.4
+ sbp_ma_addMotionDataToMetadataDictionary.cold.5
+ sbp_ma_addMotionDataToMetadataDictionary.cold.6
+ sbp_ma_addMotionDataToMetadataDictionary.cold.7
+ sbp_ma_addMotionDataToMetadataDictionary.cold.8
+ sbp_ma_addMotionDataToMetadataDictionary.cold.9
+ sbp_ma_attachMotionData.cold.1
+ sbp_ma_attachMotionData.cold.2
+ sbp_ma_attachMotionData.cold.3
+ sbp_ma_attachMotionData.cold.4
+ sbp_ma_extractAndBufferISPMotionDataFromMetadataDictionary.cold.1
+ sbp_ma_extractAndBufferISPMotionDataFromMetadataDictionary.cold.2
+ sbp_ma_finishPendingProcessing.cold.1
+ sbp_ma_processInitialCinematicFutureMetadata.cold.1
+ sbp_ma_processInitialCinematicFutureMetadata.cold.2
+ sbp_ma_processInitialCinematicFutureMetadata.cold.3
+ sbp_ma_processSampleBuffer.cold.1
+ sbp_ma_processSampleBuffer.cold.10
+ sbp_ma_processSampleBuffer.cold.2
+ sbp_ma_processSampleBuffer.cold.3
+ sbp_ma_processSampleBuffer.cold.4
+ sbp_ma_processSampleBuffer.cold.5
+ sbp_ma_processSampleBuffer.cold.6
+ sbp_ma_processSampleBuffer.cold.7
+ sbp_ma_processSampleBuffer.cold.8
+ sbp_ma_processSampleBuffer.cold.9
+ setupMeteringFaceDetection.cold.1
+ setupMeteringFaceDetection.cold.2
+ setupMeteringFaceDetection.cold.3
+ setupMeteringFaceDetection.cold.4
+ shmemRegionFinalize.cold.1
+ shmemRegionRegisterSharedRegion.cold.1
+ su_getViewMatrixInCameraCoordinates.cold.1
+ su_getViewMatrixInCameraCoordinates.cold.2
+ su_getViewMatrixInCameraCoordinates.cold.3
+ unlockAEnow.cold.1
+ unlockAEnow.cold.2
+ unlockAEnow.cold.3
+ unlockAEnow.cold.4
+ unlockAEnow.cold.5
+ unlockAEnow.cold.6
+ unlockAEnow.cold.7
+ unlockAEnow.cold.8
- -[BWDepthConverterNode convertToFloatAndRotate:inputSampleBuffer:outputPixelBuffer:]
- -[BWDepthConverterNode rotateAndScaleImagePixelBuffer:depthPixelBuffer:to:rotationAngle:flip:]
- -[BWFigCaptureDevice copyStreamForFigCaptureStream:error:]
- -[BWFigCaptureDevice copySyncGroupForFigCaptureSynchronizedStreamsGroup:error:]
- -[BWFigCaptureDevice figCaptureDevice]
- -[BWFigCaptureDevice registerForNotification:listener:callback:]
- -[BWFigCaptureDevice unregisterForNotification:listener:]
- -[BWFigCaptureDeviceClient clientIsShareableFlashlight]
- -[BWFigCaptureDeviceClient deviceSharingWithFlashlightAllowed]
- -[BWFigCaptureDeviceClient initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]
- -[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:]
- -[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClients:available:postNotifications:reason:canShareWithFlashlight:]
- -[BWFigCaptureDeviceVendor _invalidateAndReleaseDevice:]
- -[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]
- -[BWFigCaptureDeviceVendor registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]
- -[BWFigCaptureDeviceVendorDeviceState initWithDevice:]
- -[BWFigCaptureSession imageQueueSinkNodeDidDisplayFirstFrame:]
- -[BWFigCaptureStream figCaptureStream]
- -[BWFigCaptureSynchronizedStreamsGroup figCaptureSynchronizedStreamsGroup]
- -[BWFigCaptureSynchronizedStreamsGroup initWithFigCaptureSynchronizedStreamsGroup:captureDevice:]
- -[BWFigVideoCaptureDevice _currentSceneAllowsMotionFreezing:]
- -[BWFigVideoCaptureDevice _globalToneMappingEnabled]
- -[BWFigVideoCaptureDevice _isSwitchOverPreventingStillImageCaptureInProgress]
- -[BWIrisSequenceAdjuster _adjustedTimeForMetadataBufferWithTime:]
- -[BWMultiStreamCameraSourceNodeConfiguration gesturesEnabled]
- -[BWMultiStreamCameraSourceNodeConfiguration setGesturesEnabled:]
- -[BWPreviewStitcherNode _scale30FPSFrameCount:toFrameRate:]
- -[FigCaptureBaseStillImageSinkPipelineConfiguration depthDataDimensions]
- -[FigCaptureBaseStillImageSinkPipelineConfiguration setDepthDataDimensions:]
- -[FigCaptureCameraSourcePipeline nextPreviewOutputForSourceDeviceType:]
- -[FigCaptureMetadataSinkPipeline _buildMetadataSinkPipeline:graph:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
- -[FigCaptureMetadataSinkPipeline initWithConfiguration:graph:name:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
- CMIOFigCaptureStreamSetProperty.noOpProperties
- CMIOFigCaptureStreamSetProperty.sOnceToken
- FigCaptureClientApplicationIDIsMagnifier.onceToken
- FigCaptureClientApplicationIDIsMagnifier.sMatchedBundleIdentifiers
- FigCaptureDeviceGetClassID.sRegisterFigCaptureDeviceTypeOnce
- FigCaptureISPProcessingSessionGetClassID.onceToken
- FigCaptureISPProcessingSessionGetClassID.sFigCaptureISPProcessingSessionClassID
- FigCaptureStreamGetClassID.sRegisterFigCaptureStreamTypeOnce
- FigCaptureSynchronizedStreamsGroupGetClassID.sRegisterFigCaptureSynchronizedStreamsGroupTypeOnce
- GCC_except_table110
- GCC_except_table122
- GCC_except_table147
- GCC_except_table189
- GCC_except_table196
- GCC_except_table198
- GCC_except_table200
- GCC_except_table204
- GCC_except_table212
- GCC_except_table227
- GCC_except_table257
- GCC_except_table263
- GCC_except_table264
- GCC_except_table328
- GCC_except_table334
- GCC_except_table358
- GCC_except_table360
- GCC_except_table374
- GCC_except_table393
- GCC_except_table433
- GCC_except_table481
- GCC_except_table482
- GCC_except_table74
- GCC_except_table78
- GCC_except_table90
- OBJC_IVAR_$_BWFigCaptureDeviceClient._clientIsShareableFlashlight
- OBJC_IVAR_$_BWFigCaptureDeviceClient._deviceSharingWithFlashlightAllowed
- OBJC_IVAR_$_BWFigVideoCaptureDevice._streamingSessionAnalyticsAudioMixWithOthersEnabled
- OBJC_IVAR_$_BWFigVideoCaptureStream._stillImageCaptureDelegateDispatchGroup
- OBJC_IVAR_$_BWFigVideoCaptureStream._streamNotificationDispatchQueue
- OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._gesturesEnabled
- OBJC_IVAR_$_BWNodeConnection._bypassPipelineStage
- OBJC_IVAR_$_FigCaptureBaseStillImageSinkPipelineConfiguration._depthDataDimensions
- _FigCaptureDeviceCopyFormattingDesc
- _FigCaptureDeviceGetTypeID
- _FigCaptureISPProcessingSessionCopyFormattingDesc
- _FigCaptureISPProcessingSessionGetClassID
- _FigCaptureISPProcessingSessionGetTypeID
- _FigCaptureStreamCopyFormattingDesc
- _FigCaptureStreamGetTypeID
- _FigCaptureSynchronizedStreamsGroupCopyFormattingDesc
- _FigCaptureSynchronizedStreamsGroupGetClassID
- _FigCaptureSynchronizedStreamsGroupGetTypeID
- _FigMotionUpdateSagPositionUsingOISShift
- _RegisterFigCaptureDeviceType
- _RegisterFigCaptureStreamType
- _RegisterFigCaptureSynchronizedStreamsGroupType
- __53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.961
- __59-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:]_block_invoke.288
- __59-[FigCaptureClientApplicationStateMonitor _initWithClient:]_block_invoke.279
- __60-[BWFigCaptureDeviceVendor _setupDeviceCloseTimerForDevice:]_block_invoke.251
- __62-[BWMultiStreamCameraSourceNode _registerStreamOutputHandlers]_block_invoke.1025
- __81-[BWFigCaptureDeviceVendor _handleStreamControlTakenByAnotherClientNotification:]_block_invoke.257
- __81-[BWFigCaptureDeviceVendor _handleStreamRelinquishedByAnotherClientNotification:]_block_invoke.259
- __FigFlashlightCreate_block_invoke.22
- __FigFlashlightCreate_block_invoke.31
- ___121-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithFlashlight:]_block_invoke
- ___272-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]_block_invoke
- ___59-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:]_block_invoke
- ___FigCaptureISPProcessingSessionGetClassID_block_invoke
- ___block_descriptor_47_e8_32o_e5_v8?0l
- ___block_descriptor_48_e8_32o_e14_v20?0i8B12i16l
- ___block_descriptor_84_e8_32o40o48o56b64r_e5_v8?0l
- ___block_descriptor_93_e8_32o40o48r56r64r72r80r_e5_v8?0l
- ___captureSession_cancelMemoryPoolPrewarming_block_invoke
- ___copy_helper_block_e8_32o40o48r56r64r72r80r
- ___destroy_helper_block_e8_32o40o48r56r64r72r80r
- __block_literal_global.213
- __block_literal_global.217
- __block_literal_global.220
- __block_literal_global.239
- __block_literal_global.269
- __block_literal_global.282
- __block_literal_global.290
- __block_literal_global.462
- __block_literal_global.497
- __block_literal_global.547
- __block_literal_global.770
- __block_literal_global.796
- __block_literal_global.799
- __block_literal_global.813
- __block_literal_global.830
- __block_literal_global.901
- __block_literal_global.944
- __captureSession_IrisStillImageSinkBeginMomentCapture_block_invoke.862
- __captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.884
- __captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.880
- __captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.874
- __captureSession_updateRunningCondition_block_invoke.570
- __captureSource_handleDeviceNotification_block_invoke.142
- __captureSource_handleDeviceNotification_block_invoke.143
- __csu_removeUnsupportedDeviceFormatsAndDependentPresets_block_invoke.985
- _avfcAttributes.onceToken
- _avfcAttributes.sInternalKeys
- _captureSession_cancelMemoryPoolPrewarming
- _kFigCaptureAddAttachmentsOptionsKey_SelectedAttachmentKeys
- _kFigCaptureDeviceNotification_SensorAccessRevoked
- _kFigCaptureDeviceProperty_BatteryLevel
- _kFigCaptureDeviceProperty_BatteryState
- _kFigCaptureDeviceProperty_CMIOExtensionDeviceID
- _kFigCaptureISPProcessingSessionOutputID_IntermediateTap
- _kFigCaptureISPProcessingSessionOutputID_PrimaryScalerLowRes
- _kFigCaptureISPProcessingSessionOutputID_Vision
- _kFigCaptureISPProcessingSessionOutputParameterKey_InputCropRect
- _kFigCaptureISPProcessingSessionParameterKey_MetadataDictionary
- _kFigCaptureISPProcessingSessionParameterKey_OutputParameters
- _kFigCaptureISPProcessingSessionParameterKey_SessionTypeSpecificParameters
- _kFigCaptureISPProcessingSessionProperty_DefaultProcessingParameters
- _kFigCaptureISPProcessingSessionProperty_DeferAdditionOfAttachments
- _kFigCaptureISPProcessingSessionProperty_OutputHandler
- _kFigCaptureISPProcessingSessionProperty_SupportedOutputs
- _kFigCapturePropertyShouldBeSerializedKey
- _kFigCapturePropertyType_Allocator
- _kFigCapturePropertyType_BufferQueue
- _kFigCapturePropertyType_Enumeration
- _kFigCapturePropertyType_FormatDescription
- _kFigCapturePropertyType_Unused
- _kFigCaptureSourceAttributeKey_EyeReliefSupported
- _kFigCaptureSourceAttributeKey_FaceTracking
- _kFigCaptureSourceAttributeKey_ObjectsDetectionSupportedConfigurationKeys
- _kFigCaptureSourceAttributeKey_VideoPreviewHistogram
- _kFigCaptureSourceProperty_AvailableMetadataKeyGroups
- _kFigCaptureStreamNotificationCMIOExtensionPropertyKey_Attribute_MaxValue
- _kFigCaptureStreamNotificationCMIOExtensionPropertyKey_Attribute_MinValue
- _kFigCaptureStreamNotificationCMIOExtensionPropertyKey_Attribute_Settable
- _kFigCaptureStreamNotificationCMIOExtensionPropertyKey_Name
- _kFigCaptureStreamNotificationCMIOExtensionPropertyKey_Value
- _kFigCaptureStreamNotification_OverflowDetected
- _kFigCaptureStreamNotification_StreamInterruption_InterruptionEnded
- _kFigCaptureStreamNotification_StreamInterruption_StopNow
- _kFigCaptureStreamProperty_BufferQueue
- _kFigCaptureStreamProperty_FormatDescription
- _kFigCaptureStreamProperty_ManualFramingDeviceType
- _kFigCaptureStreamProperty_StillImageBufferQueue
- _kFigCaptureSynchronizedStreamsGroupProperty_SynchronizationMaster
- _kFigSupportedFormat_AudioMaxSampleRate
- _kFigSupportedFormat_AudioMinSampleRate
- _kFigSupportedFormat_VideoScaleFactor
- _objc_msgSend$addPAMDecisionPreliminary:
- _objc_msgSend$clientIsShareableFlashlight
- _objc_msgSend$copyStreamForFigCaptureStream:error:
- _objc_msgSend$copySyncGroupForFigCaptureSynchronizedStreamsGroup:error:
- _objc_msgSend$deviceSharingWithFlashlightAllowed
- _objc_msgSend$figCaptureStream
- _objc_msgSend$figCaptureSynchronizedStreamsGroup
- _objc_msgSend$imageQueueSinkNodeDidDisplayFirstFrame:
- _objc_msgSend$initWithDevice:
- _objc_msgSend$initWithFigCaptureSynchronizedStreamsGroup:captureDevice:
- _objc_msgSend$initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:
- _objc_msgSend$registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:
- _objc_msgSend$registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:
- _rqSurfacesRemoveAll
- _sActiveVideoCaptureSourceLock
- _sBufferometerTotalCount
- _sBufferometerTotalSize
- _sBufferometerTrackingSerialNumber
- _sDefaultSphereModes
- _sDepthSphereModes
- _sFigCaptureDeviceDesc
- _sFigCaptureDeviceID
- _sFigCaptureISPProcessingSessionDesc
- _sFigCaptureStreamDesc
- _sFigCaptureStreamID
- _sFigCaptureSynchronizedStreamsGroupDesc
- _sFigCaptureSynchronizedStreamsGroupID
- _sLatestForegroundXPCServiceApplicationStateMonitorsByHostApplicationID
- _sLatestForegroundedXPCServiceLock
- _sOverCaptureStillSphereModes
- _sOverCaptureVideoSphereModes
- _sPTEffectSuspensionLock
- _sStillSphereModes
- _sSuspendedPTEffect
- _sSystemPressureMonitor
- _sTimeOfFlightAFEnabled
- _sTimeOfFlightAFSuspended
- _sVideo30SphereModes
- _sVideo60SphereModes
- _sZSLStillSphereModes
- _sZSLStillStationarySphereModes
- _servicePropertyChangeNotifications:.sAlwaysSendManualPropertyNotifications
- _servicePropertyChangeNotifications:.sSendManualPropertyNotificationsOnceToken
- _setUpClientInfoWithAuditToken:.onceToken
- _setUpClientInfoWithAuditToken:.sApplicationIDsEligibleForBackgroundCameraAccess
- _setUpClientInfoWithAuditToken:.sExtensionApplicationIDsEligibleForCameraUsage
- _setUpClientInfoWithAuditToken:.sExtensionPointIDsEligibleForCameraUsage
- _setUpClientInfoWithAuditToken:.sHostApplicationIDsEligibleForCameraUsageInExtension
- _setUpClientInfoWithAuditToken:.sLaunchAngelApplicationIDsEligibleForCameraUsage
- _setUpClientInfoWithAuditToken:.sNonstandardClientCodeSigningIDsEligibleForCameraUsage
- bbn_PTEffectReactionTypeForString.onceToken
- bbn_PTEffectReactionTypeForString.sMapNameToReactionType
- cs_metadataIdentifierKeyForObjectsDetectionConfigurationKey.onceToken
- cs_metadataIdentifierKeyForObjectsDetectionConfigurationKey.sMetadataKeysByConfigurationKeysDict
- fcu_initializeTrace.sInitializeTraceOnceToken
- qtmfsn_minFreeDiskSpaceLimit.onceToken
- qtmfsn_minFreeDiskSpaceLimit.sMinFreeDiskSpaceLimit
- simu_createDNGDictionary.sMobileGestaltOnceToken
- simu_createDNGDictionary.sProductTypeString
CStrings:
+ "!( ((void*)0) == pixelBuffer || xStart < 0 || yStart < 0 || xStart >= width || yStart >= height || xSize < 1 || ySize < 1 )"
+ "%@ :: A:%d (%.4lf - %.4lf)"
+ "%@ :: M:%d (%.4lf - %.4lf)"
+ "%@ :: V:%d (%.4lf - %.4lf)"
+ "( AFIsLocked != ((void*)0) ) && ( AEIsLocked != ((void*)0) ) && ( AWBIsLocked != ((void*)0) ) && ( dynamicToneCurveIsLocked != ((void*)0) ) && ( LTMLocked != ((void*)0) )"
+ "( v1Flags || v2Flags || v3Flags )"
+ "((void*)0) != atomWrappedSetupData"
+ "((void*)0) != setupDataData"
+ "+[BWDeferredContainer manifestDictionaryForURL:err:]"
+ "+[BWDeferredContainer validateManifestURLSize:]"
+ ", motionToWakeTargetFrameRate:%.2f"
+ ", occlusionDetection:%d"
+ ", periocular:%d, attention:%d"
+ "-[BWDeferredContainer _validate]"
+ "-[BWDeferredProcessingContainer copyArrayForTag:customClasses:err:]"
+ "-[BWDeferredProcessingContainer copyDictionaryForTag:customClasses:err:]"
+ "-[BWDeferredProcessingContainer copyMetadataForTag:err:]"
+ "-[BWDeferredProcessingContainer initWithXPCEncoding:applicationID:captureRequestIdentifier:baseFolderURL:err:]"
+ "-[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:]"
+ "-[BWFigCaptureDevice _removeFigCaptureDeviceListeners]"
+ "-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:]"
+ "-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:figCaptureDevice:]"
+ "-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithFlashlight:cameraStolenInterruptor:]_block_invoke"
+ "-[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:]"
+ "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:]_block_invoke"
+ "-[BWFigCaptureStreamsMapper bwFigCaptureStreamsForFigCaptureStreams:]"
+ "-[BWFigCaptureStreamsMapper figCaptureStreamsForBWFigCaptureStreams:]"
+ "-[BWFigCaptureSynchronizedStreamsGroup initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:]"
+ "-[BWFileCoordinatorNode _logNumBuffersReceivedDuringStartingRecording]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
+ "/System/AppleInternal/Library/Frameworks/FusionTracker.framework/FusionTracker"
+ "/System/AppleInternal/Library/Frameworks/Portrait.framework/Portrait"
+ "/System/AppleInternal/Library/Frameworks/Vision.framework/Vision"
+ "<<<< BWDeferredContainer >>>> %s: Asset for tag %{public}@ is not an NSArray; class is %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Asset for tag %{public}@ is not an NSDictionary; class is %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Could not fetch manifest attributes (error: %d, description %{public}@)"
+ "<<<< BWDeferredContainer >>>> %s: Could not open manifest"
+ "<<<< BWDeferredContainer >>>> %s: Could not open manifest due to error: %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Error %ld creating unarchiver: %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Error unarchiving session dictionary: %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode application ID, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode photo descriptors, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode still image capture settings, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode still image settings, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Incompatible manifest version (manifest version %ld, minimum compatible version %ld)"
+ "<<<< BWDeferredContainer >>>> %s: Invalid capture request identifier %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Invalid number of intermediates"
+ "<<<< BWDeferredContainer >>>> %s: Invalid photo descriptors"
+ "<<<< BWDeferredContainer >>>> %s: Invalid processing count, %@"
+ "<<<< BWDeferredContainer >>>> %s: Invalid still image capture settings"
+ "<<<< BWDeferredContainer >>>> %s: Invalid still image settings"
+ "<<<< BWDeferredContainer >>>> %s: Malformed captureRequestIdentifierString in manifest %{public}@, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Manifest failed to decode version number, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Mismatched intermediate type for %{public}@ (asset name %{public}@)"
+ "<<<< BWDeferredContainer >>>> %s: Missing asset for tag %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: No matching asset for tag %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Too many processing attempts for container %{public}@: %d out of %d"
+ "<<<< BWDeferredContainer >>>> %s: URL for manifest %{public}@ is invalid"
+ "<<<< BWDeferredContainer >>>> %s: captureRequestIdentifier in manifest %{public}@ is not a valid UUID"
+ "<<<< BWFigCaptureDevice >>>> %s: %{public}@ Device (%@) %@ notification fired."
+ "<<<< BWFigCaptureDevice >>>> %s: %{public}@: translated %{public}@, to: %{public}@"
+ "<<<< BWFigCaptureDevice >>>> %s: Keep %@ for the next client"
+ "<<<< BWFigCaptureDevice >>>> %s: Removing FigCaptureDevice listeners."
+ "<<<< BWFigCaptureDevice >>>> %s: SynchronizationPrimaryStream is nil for syncGroup: %@"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: %@ BWFigCaptureDeviceVendorDeviceAvailabilityChangedNotification: %{public}@"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Device %p usage count is %i. Device client %@ was removed, remaining active device clients: %@."
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Device became available again - calling out to deviceAvailabilityChangedHandler for pid %d."
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Device unavailable (%@) - calling out to deviceAvailabilityChangedHandler of pid %d."
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Reusing FigCaptureDeviceRef (%p)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Stealing the device (invalidate the former device and create new device) took %i ms. keepFigCaptureDeviceAlive: %i."
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: The device should not have control of streams but it has: %@ "
+ "<<<< BWFigCaptureStream >>>> %s: Failed to lookup BWFigCaptureStream for %@ - camera likely unplugged"
+ "<<<< BWFigCaptureStream >>>> %s: Failed to lookup FigCaptureStreamRef for %@ - camera likely unplugged"
+ "<<<< BWFigCaptureSynchronizedStreamsGroup >>>> %s: SynchronizationPrimaryStream is nil for syncGroup: %@"
+ "<<<< BWFigVideoCaptureStream >>>> %s: ISP posted '%{public}@' %{public}@ (captureID:%{public}lld)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: ISP posted '%{public}@'. No still image capture in progress, ignoring"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: %@"
+ "<<<< BWGraph >>>> %s: <%p> (%p) Released assertion for BWGraph"
+ "<<<< BWGraph >>>> %s: <%p> Created assertion for BWGraph (%@)"
+ "<<<< BWGraph >>>> %s: <%p> Released assertion for BWGraph"
+ "<<<< BWImageQueueSinkNode >>>> %s: %{public}@: Did display first frame (timeout) (numFramesReceived: %ld, imageQueueSlot = %d)"
+ "<<<< FigCaptureClientApplicationStateMonitor >>>> %s: %{public}@ Cannot store reference to %{public}@[%d] without a root host application ID"
+ "@\"BWFigCaptureStreamsMapper\""
+ "@\"FigCaptureCameraSourcePipelineConfiguration\""
+ "@32@0:8@16^{OpaqueFigCaptureDevice=}24"
+ "@40@0:8^{OpaqueFigCaptureSynchronizedStreamsGroup=}16@24@32"
+ "@60@0:8i16@20@28i36B40B44i48@?52"
+ "AVMetadataObjectTypeFaceIDReadiness"
+ "AVMetadataObjectTypeMotionToWake"
+ "AvailableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization"
+ "BWCorrespondingMetadataIdentifiers"
+ "BWFigCaptureCMIODeviceNotification_TrackingActiveChanged"
+ "BWFigCaptureDeviceNotification_DeviceNoLongerAvailable"
+ "BWFigCaptureDeviceNotification_HiddenStateChanged"
+ "BWFigCaptureDeviceNotification_UnrecoverableError"
+ "BWFigCaptureStreamsMapper"
+ "BWFigVideoCaptureDeviceSuppressedGestureNotification"
+ "Buffers received on each input during starting"
+ "CGImageMetadataSetTagWithPath( auxiliaryImageProperties, ((void*)0), (CFStringRef)path, tag )"
+ "CameraStolenInterruptor"
+ "DisplayFirstFrameTimeout"
+ "ExtraHigh"
+ "FaceIDReadiness"
+ "FaceOcclusionDetectionSupported"
+ "FigRemoteQueueReceiverGetContext( recver ) == ((void*)0)"
+ "FigSharedMemPoolSharedRegionGetOwner(region) == ((void*)0)"
+ "ImageQueueUpdatedInfo"
+ "ImageQueueUpdatedPayload"
+ "ImageQueueUpdatedTime"
+ "J713"
+ "J715"
+ "Localizable-CMIOExtension"
+ "MACBOOKAIR_BUILT_IN_CAMERA_NAME"
+ "MACBOOKAIR_BUILT_IN_DESKVIEW_CAMERA_NAME"
+ "MetadataGroup-Misc"
+ "MetadataGroup-SecureMetadata"
+ "MotionToWake"
+ "Not sending"
+ "NotShareable"
+ "Sending"
+ "ShareableFlashlight"
+ "SourceSuppressedGesture"
+ "SuppressedGesturesEnabled"
+ "T@\"BWNodeOutput\",R,V_faceIDReadinessOutput"
+ "T@\"BWNodeOutput\",R,V_motionToWakeOutput"
+ "T@?,C,N,V_suppressedGestureHandler"
+ "TB,N,V_attentionForFaceIDReadinessRequired"
+ "TB,N,V_faceIDReadinessAttentionRequired"
+ "TB,N,V_faceIDReadinessEnabled"
+ "TB,N,V_faceIDReadinessPeriocularEnabled"
+ "TB,N,V_faceOcclusionDetectionEnabled"
+ "TB,N,V_hitPortraitInPhotoPreviewThermalPressure"
+ "TB,N,V_isHardCut"
+ "TB,N,V_motionToWakeEnabled"
+ "TB,N,V_periocularForFaceIDReadinessEnabled"
+ "TB,N,V_secureMetadataEnabled"
+ "TB,R,N,GisValid"
+ "TI,N,V_longestContinuousPortraitInPhotoPreviewInMS"
+ "T^{OpaqueFigCaptureDevice=},R,N,V_figCaptureDevice"
+ "Tf,N,V_motionToWakeTargetFrameRate"
+ "Ti,N,V_faceTrackingMaxNumTrackedFaces"
+ "Ti,N,V_takeBackDeviceCalledForActiveClientID"
+ "TrackedFaces"
+ "T{?=ii},N,V_depthDataSourceDimensions"
+ "T{?=ii},N,V_depthDataTargetDimensions"
+ "UnknownDeviceClientType"
+ "VibeMitigation"
+ "[parentPipeline addNode:visNode error:((void*)0)]"
+ "_attentionForFaceIDReadinessRequired"
+ "_audioCompressionSBP != ((void*)0)"
+ "_audioCompressionSBP == ((void*)0)"
+ "_autofocusProcessor == ((void*)0)"
+ "_bwFigCaptureStreams"
+ "_bypassConnection"
+ "_createAutofocusSampleBufferProcessorFunction != ((void*)0)"
+ "_createSampleBufferProcessorFunction != ((void*)0)"
+ "_depthDataSourceDimensions"
+ "_depthDataTargetDimensions"
+ "_earliestPTSReceivedDuringStartingRecording"
+ "_faceIDReadinessAttentionRequired"
+ "_faceIDReadinessEnabled"
+ "_faceIDReadinessOutput"
+ "_faceIDReadinessOutputsBySourceDeviceType"
+ "_faceIDReadinessPeriocularEnabled"
+ "_faceOcclusionDetectionEnabled"
+ "_faceTrackingMaxNumTrackedFaces"
+ "_figCaptureDevice"
+ "_figCaptureStreams"
+ "_figCaptureSynchronizedStreamsGroups"
+ "_hitPortraitInPhotoPreviewThermalPressure"
+ "_isHardCut"
+ "_latestPTSReceivedDuringStartingRecording"
+ "_latestPortraitInPhotoPreviewStartTime"
+ "_longestContinuousPortraitInPhotoPreviewInMS"
+ "_motionToWakeEnabled"
+ "_motionToWakeOutput"
+ "_motionToWakeOutputsBySourceDeviceType"
+ "_motionToWakeTargetFrameRate"
+ "_numBuffersReceivedDuringStartingRecording"
+ "_periocularForFaceIDReadinessEnabled"
+ "_preventSystemSleepAssertion"
+ "_preventingSystemSleep"
+ "_secureMetadataEnabled"
+ "_sensorIDDictionaryByPortType != ((void*)0)"
+ "_streamNotificationQueue"
+ "_streamsMapper"
+ "_suppressedGestureHandler"
+ "_suppressedGestureObserver"
+ "_suppressedGesturesEnabled"
+ "_takeBackDeviceCalledForActiveClientID"
+ "_triggerDisplayTimeout"
+ "_willStopStreaming"
+ "activeDeviceClients"
+ "attentionForFaceIDReadinessRequired"
+ "boxedMetadataSBuf != ((void*)0)"
+ "bwfcd_handleFigCaptureDeviceNotification"
+ "cameracaptured-idleSleepPreventionForBWGraph(ClientPID:%d)"
+ "captureSession_cancelMemoryPoolPrewarmingLocked"
+ "clientID: %d, pid: %d, clientApplicationID: %@, clientDescription: %@, clientPriority: %@, canStealFromClientsWithSamePriority: %d, deviceSharingWithOtherClientsAllowed: %d, clientType: %@, handler: %p"
+ "com.apple.coremedia.capture.device-lock-state-notification"
+ "com.apple.private.avfoundation.capture.camera-stolen-interruptor.allow"
+ "controlledStreamsForDevice:"
+ "deferredSetupStartCondition != ((void*)0)"
+ "depthDataSourceDimensions"
+ "depthDataSourceDimensionsHeight"
+ "depthDataSourceDimensionsWidth"
+ "depthDataTargetDimensions"
+ "depthDataTargetDimensionsHeight"
+ "depthDataTargetDimensionsWidth"
+ "description=CameraCapture-587.101.4"
+ "didChangeSuppressedGesturesEnabled:"
+ "faceIDReadiness"
+ "faceIDReadinessAttentionRequired"
+ "faceIDReadinessEnabled"
+ "faceIDReadinessOutput"
+ "faceIDReadinessPeriocularEnabled"
+ "faceOcclusionDetectionEnabled"
+ "faceTrackingMaxNumTrackedFaces"
+ "frameworkVersionDict != ((void*)0)"
+ "gestureCount"
+ "hallEvent != ((void*)0)"
+ "hitPortraitInPhotoPreviewThermalPressure"
+ "i52@0:8i16@20i28B32B36i40@?44"
+ "i60@0:8i16@20@28i36B40B44i48@?52"
+ "imageControlModeString != ((void*)0)"
+ "imageQueueSinkNodeDidDisplayFirstFrame:timedOut:"
+ "imageYBasePtr != ((void*)0)"
+ "inNotificationPayload == ((void*)0)"
+ "initWithDevice:figCaptureDevice:"
+ "initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:"
+ "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:"
+ "inputPixelBuffer != ((void*)0)"
+ "inputSampleBuffer != ((void*)0)"
+ "invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:"
+ "isHardCut"
+ "ispHallDataMutableArray != ((void*)0)"
+ "ispMetadataDictionary != ((void*)0)"
+ "localQueueOut != ((void*)0)"
+ "longestContinuousPortraitInPhotoPreviewInMS"
+ "motionToWake"
+ "motionToWakeEnabled"
+ "motionToWakeOutput"
+ "motionToWakeTargetFrameRate"
+ "newSbuf != ((void*)0)"
+ "newSynchronizedSlaveSbuf != ((void*)0)"
+ "obj != ((void*)0)"
+ "objOut != ((void*)0)"
+ "op->opIOSurface.surface == ((void*)0)"
+ "op->opIOSurface.thumbnailSurface == ((void*)0)"
+ "originalPixelBuffer != ((void*)0)"
+ "outSetupData != ((void*)0)"
+ "periocularForFaceIDReadinessEnabled"
+ "pixelBuffer != ((void*)0)"
+ "points != ((void*)0)"
+ "pool != ((void*)0)"
+ "poolOut != ((void*)0)"
+ "portVal != ((void*)0)"
+ "ptsAdjustedSampleBuffer != ((void*)0)"
+ "region != ((void*)0)"
+ "regionObj != ((void*)0)"
+ "regionOut != ((void*)0)"
+ "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:"
+ "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:clientType:deviceAvailabilityChangedHandler:"
+ "resultSampleBuffer != ((void*)0)"
+ "sampleBufferToEmit != ((void*)0)"
+ "sbuf != ((void*)0)"
+ "secureMetadataEnabled"
+ "senderOut != ((void*)0)"
+ "setAttentionForFaceIDReadinessRequired:"
+ "setDepthDataSourceDimensions:"
+ "setDepthDataTargetDimensions:"
+ "setFaceIDReadinessAttentionRequired:"
+ "setFaceIDReadinessEnabled:"
+ "setFaceIDReadinessPeriocularEnabled:"
+ "setFaceOcclusionDetectionEnabled:"
+ "setFaceTrackingMaxNumTrackedFaces:"
+ "setHitPortraitInPhotoPreviewThermalPressure:"
+ "setIsHardCut:"
+ "setLongestContinuousPortraitInPhotoPreviewInMS:"
+ "setMotionToWakeEnabled:"
+ "setMotionToWakeTargetFrameRate:"
+ "setMotionToWakeTargetFrameRate:forSessionID:"
+ "setPeriocularForFaceIDReadinessEnabled:"
+ "setSecureMetadataEnabled:"
+ "setSuppressGestureTriggeredReactions:"
+ "setSuppressedGestureHandler:"
+ "setSuppressedGesturesEnabled:"
+ "setTakeBackDeviceCalledForActiveClientID:"
+ "setupDataDict != ((void*)0)"
+ "storage->CoreMotionDelegate != ((void*)0)"
+ "storage->frameRing.sampleBuffers != ((void*)0)"
+ "storage->ispGravityRing.gravityVectors != ((void*)0)"
+ "storage->ispHallDataRingBuffer[i] != ((void*)0)"
+ "storage->ispMotionDataRingBuffer != ((void*)0)"
+ "storage->rawGravities != ((void*)0)"
+ "storage->rawHallPositions != ((void*)0)"
+ "storage->rawQuaternions != ((void*)0)"
+ "suppressGestureTriggeredReactions"
+ "suppressedGestureHandler"
+ "suppressedGesturesEnabled"
+ "systemVersionDict != ((void*)0)"
+ "systemVersionPropertyList != ((void*)0)"
+ "systemVersionURL != ((void*)0)"
+ "takeBackDeviceCalledForActiveClientID"
+ "targetFormatDescription != ((void*)0)"
+ "v28@0:8@\"BWImageQueueSinkNode\"16B24"
+ "v28@?0i8B12i16@\"NSString\"20"
+ "yyyy-MM-dd HH:mm:ss.SSS"
- "!( ((void *)0) == pixelBuffer || xStart < 0 || yStart < 0 || xStart >= width || yStart >= height || xSize < 1 || ySize < 1 )"
- "( AFIsLocked != ((void *)0) ) && ( AEIsLocked != ((void *)0) ) && ( AWBIsLocked != ((void *)0) ) && ( dynamicToneCurveIsLocked != ((void *)0) ) && ( LTMLocked != ((void *)0) )"
- "((void *)0) != atomWrappedSetupData"
- "((void *)0) != setupDataData"
- "-[BWFigCaptureDevice copyStreamForFigCaptureStream:error:]"
- "-[BWFigCaptureDevice copySyncGroupForFigCaptureSynchronizedStreamsGroup:error:]"
- "-[BWFigCaptureDevice invalidate]"
- "-[BWFigCaptureDeviceVendor _createDevice:reason:clientPID:]"
- "-[BWFigCaptureDeviceVendor _invalidateAndReleaseDevice:]"
- "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/b92a986a-ce8f-11ef-9e52-d285688f7a47/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
- "<<<< BWFigCaptureDevice >>>> %s: %{public}@: could not find BWFigCaptureStream for FigCaptureStreamRef %{public}@"
- "<<<< BWFigCaptureDevice >>>> %s: %{public}@: could not find BWFigCaptureSynchronizedStreamsGroup for FigCaptureSynchronizedStreamsGroupRef %{public}@"
- "<<<< BWFigVideoCaptureStream >>>> %s: ISP posted '%{public}@' %{public}@"
- "<<<< BWFigVideoCaptureStream >>>> %s: No still image capture in progress. Ignoring '%@'"
- "<<<< BWImageQueueSinkNode >>>> %s: %{public}@: Did display first frame (timeout) (numFramesReceived: %ld)"
- "@32@0:8^{OpaqueFigCaptureStream=}16^i24"
- "@32@0:8^{OpaqueFigCaptureSynchronizedStreamsGroup=}16@24"
- "@32@0:8^{OpaqueFigCaptureSynchronizedStreamsGroup=}16^i24"
- "@64@0:8i16@20@28i36B40B44B48B52@?56"
- "Allocator"
- "AudioMaxSampleRate"
- "AudioMinSampleRate"
- "AutoAENow"
- "AutoFocusNow"
- "BatteryLevelChanged"
- "BatteryStateChanged"
- "Boolean"
- "BufferQueue"
- "CGImageMetadataSetTagWithPath( auxiliaryImageProperties, ((void *)0), (CFStringRef)path, tag )"
- "CMIOBackgroundBlurAperture"
- "CMIOBackgroundBlurEnabled"
- "CMIOBackgroundReplacementEnabled"
- "CMIOBackgroundReplacementPixelBuffer"
- "CMIOCenterStageFramingMode"
- "CMIOCenterStageFramingModeChanged"
- "CMIOCenterStageRectOfInterest"
- "CMIOCenterStageRectOfInterestChanged"
- "CMIOCinematicFramingEnabled"
- "CMIOCompanionDeskViewDeviceUUID"
- "CMIOCompressedFormat"
- "CMIOExtensionDeviceID"
- "CMIOExtensionPropertyArray"
- "CMIOExtensionPropertyChanged"
- "CMIOFlashMode"
- "CMIOFlashSupported"
- "CMIOGesturesEnabled"
- "CMIOHighResolutionPhotoEnabled"
- "CMIOLocation"
- "CMIOManualFramingSupported"
- "CMIOMaxPhotoDimensionsHeight"
- "CMIOMaxPhotoDimensionsWidth"
- "CMIOQualityPrioritization"
- "CMIOReactionEffectsEnabled"
- "CMIOStillImageMaxQualityPrioritization"
- "CMIOStudioLightingEnabled"
- "CMIOStudioLightingIntensity"
- "CMIOVideoZoomFactor"
- "CMIOVideoZoomFactorChanged"
- "Camera activity without camera indicator light. Please file a radar."
- "ClientPriority"
- "Collection"
- "CompressedStillImageCaptureSupported"
- "Could not open manifest"
- "Could not update URL for tag %@"
- "DefaultFormatIndexDisabled"
- "DefaultProcessingParameters"
- "DeferAdditionOfAttachments"
- "DeviceNoLongerAvailable"
- "DeviceTrackingActiveChanged"
- "Discontinuity"
- "Enumeration"
- "EventTimeStamp"
- "EyeReliefSupported"
- "FigCaptureISPProcessingSession"
- "FigCaptureStream"
- "FigCaptureSynchronizedStreamsGroup"
- "FigRemoteQueueReceiverGetContext( recver ) == ((void *)0)"
- "FigSharedMemPoolSharedRegionGetOwner(region) == ((void *)0)"
- "FormatIndex"
- "HiddenStateChanged"
- "InputCropRect"
- "InputPixelBufferAttributes"
- "IntermediateTap"
- "Invalid intermediates"
- "Invalid still image capture settings"
- "Invalid still image settings"
- "IsFaceScene"
- "IsPeopleAndMotionScene"
- "J717"
- "J718"
- "J720"
- "J721"
- "LastShownInvalidFrameTTRPromptBuildVersion"
- "LastShownInvalidFrameTTRPromptDate"
- "Localizable-CMIOExtension-Seed"
- "MaximumAllowedFrameRate"
- "MaximumFrameRate"
- "MetadataDictionary"
- "MetadataGroup-Face"
- "MetadataGroup-Histogram"
- "MetadataGroup-OfflineVIS"
- "MetadataGroup-SceneClassification"
- "MetadataGroup-SecureEyeRelief"
- "MetadataGroup-TextRegion"
- "MinimumFrameRate"
- "Number"
- "ObjectsDetectionSupportedConfigurationKeys"
- "ObjectsDetectionSupportedMetadataKeys"
- "OutputHandler"
- "OutputParameters"
- "OutputPixelBufferAttributes"
- "OverflowDetected"
- "PixelBuffer"
- "PrimaryScaler"
- "PrimaryScalerLowRes"
- "PropertyType"
- "ReadOnly"
- "ReadWrite"
- "ReadWriteStatus"
- "ReadyToUnhideChanged"
- "Received black frames because the camera indicator light was off"
- "ResumedByUser"
- "SecondaryScaler"
- "SecondsSinceLastFaceDetected"
- "SelectedAttachmentKeys"
- "SensorAccessRevoked"
- "SessionType"
- "SessionTypeSpecificParameters"
- "ShouldBeSerialized"
- "StillImageBufferQueue"
- "StreamArray"
- "StreamArrayChanged"
- "StreamInterruption_InterruptionEnded"
- "StreamInterruption_StopNow"
- "StreamStarted"
- "StreamStopped"
- "String"
- "SupportedFormatsArray"
- "SupportedOutputs"
- "SupportedPropertiesDictionary"
- "TB,R,N,V_clientIsShareableFlashlight"
- "TB,R,N,V_deviceSharingWithFlashlightAllowed"
- "T^{OpaqueFigCaptureDevice=},R"
- "T^{OpaqueFigCaptureStream=},R"
- "UnrecoverableError"
- "Unused"
- "Value"
- "VideoBinningFactorHorizontal"
- "VideoBinningFactorVertical"
- "VideoIsBinned"
- "VideoMinFrameRate"
- "VideoPreviewHistogram"
- "VideoScaleFactor"
- "WriteOnly"
- "[FigCaptureDevice %p]"
- "[FigCaptureISPProcessingSession %p]"
- "[FigCaptureStream %p]"
- "[FigCaptureSynchronizedStreamsGroup %p]"
- "[parentPipeline addNode:visNode error:((void *)0)]"
- "^{OpaqueFigCaptureStream=}16@0:8"
- "^{OpaqueFigCaptureSynchronizedStreamsGroup=}16@0:8"
- "_audioCompressionSBP != ((void *)0)"
- "_audioCompressionSBP == ((void *)0)"
- "_autofocusProcessor == ((void *)0)"
- "_bypassPipelineStage"
- "_clientIsShareableFlashlight"
- "_createAutofocusSampleBufferProcessorFunction != ((void *)0)"
- "_createSampleBufferProcessorFunction != ((void *)0)"
- "_deviceSharingWithFlashlightAllowed"
- "_sensorIDDictionaryByPortType != ((void *)0)"
- "_stillImageCaptureDelegateDispatchGroup"
- "_streamNotificationDispatchQueue"
- "_streamingSessionAnalyticsAudioMixWithOthersEnabled"
- "boxedMetadataSBuf != ((void *)0)"
- "captureRequestIdentifierIsValid"
- "captureSession_cancelMemoryPoolPrewarming"
- "clientID: %d, pid: %d, clientApplicationID: %@, clientDescription: %@, clientPriority: %@, canStealFromClientsWithSamePriority: %d, deviceSharingWithOtherClientsAllowed: %d, deviceSharingWithFlashlightAllowed: %d, clientIsShareableFlashlight: %d, handler: %p"
- "clientIsShareableFlashlight"
- "copyStreamForFigCaptureStream:error:"
- "copySyncGroupForFigCaptureSynchronizedStreamsGroup:error:"
- "deferredSetupStartCondition != ((void *)0)"
- "description=CameraCapture-587.81.10"
- "deviceSharingWithFlashlightAllowed"
- "figCaptureStream"
- "figCaptureSynchronizedStreamsGroup"
- "frameworkVersionDict != ((void *)0)"
- "hallEvent != ((void *)0)"
- "i56@0:8i16@20i28B32B36B40B44@?48"
- "i64@0:8i16@20@28i36B40B44B48B52@?56"
- "imageControlModeString != ((void *)0)"
- "imageQueueSinkNodeDidDisplayFirstFrame:"
- "imageYBasePtr != ((void *)0)"
- "inNotificationPayload == ((void *)0)"
- "initWithDevice:"
- "initWithFigCaptureSynchronizedStreamsGroup:captureDevice:"
- "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
- "inputPixelBuffer != ((void *)0)"
- "inputSampleBuffer != ((void *)0)"
- "intermediatesAreValid"
- "ispHallDataMutableArray != ((void *)0)"
- "ispMetadataDictionary != ((void *)0)"
- "localQueueOut != ((void *)0)"
- "newSbuf != ((void *)0)"
- "newSynchronizedSlaveSbuf != ((void *)0)"
- "obj != ((void *)0)"
- "objOut != ((void *)0)"
- "op->opIOSurface.surface == ((void *)0)"
- "op->opIOSurface.thumbnailSurface == ((void *)0)"
- "originalPixelBuffer != ((void *)0)"
- "outSetupData != ((void *)0)"
- "photoDescriptorsAreValid"
- "pixelBuffer != ((void *)0)"
- "points != ((void *)0)"
- "pool != ((void *)0)"
- "poolOut != ((void *)0)"
- "portVal != ((void *)0)"
- "ptsAdjustedSampleBuffer != ((void *)0)"
- "regionObj != ((void *)0)"
- "regionOut != ((void *)0)"
- "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
- "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithFlashlightAllowed:clientIsShareableFlashlight:deviceAvailabilityChangedHandler:"
- "resultSampleBuffer != ((void *)0)"
- "sampleBufferToEmit != ((void *)0)"
- "sbuf != ((void *)0)"
- "senderOut != ((void *)0)"
- "setupDataDict != ((void *)0)"
- "stillImageCaptureSettingsIsValid"
- "stillImageSettingsIsValid"
- "storage->CoreMotionDelegate != ((void *)0)"
- "storage->frameRing.sampleBuffers != ((void *)0)"
- "storage->ispGravityRing.gravityVectors != ((void *)0)"
- "storage->ispHallDataRingBuffer[i] != ((void *)0)"
- "storage->ispMotionDataRingBuffer != ((void *)0)"
- "storage->rawGravities != ((void *)0)"
- "storage->rawHallPositions != ((void *)0)"
- "storage->rawQuaternions != ((void *)0)"
- "systemVersionDict != ((void *)0)"
- "systemVersionPropertyList != ((void *)0)"
- "systemVersionURL != ((void *)0)"
- "targetFormatDescription != ((void *)0)"
- "v20@?0i8B12i16"
- "v24@0:8@\"BWImageQueueSinkNode\"16"

```
