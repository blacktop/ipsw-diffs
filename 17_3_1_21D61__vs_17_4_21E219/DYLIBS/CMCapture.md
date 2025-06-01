## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-472.1.2.0.0
-  __TEXT.__text: 0x44f170
-  __TEXT.__auth_stubs: 0x49c0
-  __TEXT.__objc_methlist: 0x25934
-  __TEXT.__const: 0x1500b8
-  __TEXT.__cstring: 0x62be6
-  __TEXT.__oslogstring: 0x1856b
-  __TEXT.__gcc_except_tab: 0x1e50
-  __TEXT.__dlopen_cstrs: 0x53f
+475.31.1.0.0
+  __TEXT.__text: 0x45a794
+  __TEXT.__auth_stubs: 0x4a30
+  __TEXT.__objc_methlist: 0x25e6c
+  __TEXT.__const: 0x1501a8
+  __TEXT.__cstring: 0x63d47
+  __TEXT.__oslogstring: 0x19f99
+  __TEXT.__gcc_except_tab: 0x1ed0
+  __TEXT.__dlopen_cstrs: 0x588
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xa0b4
-  __TEXT.__objc_classname: 0x6aef
-  __TEXT.__objc_methname: 0x7e227
-  __TEXT.__objc_methtype: 0x116a6
-  __TEXT.__objc_stubs: 0x379c0
-  __DATA_CONST.__got: 0x45b8
-  __DATA_CONST.__const: 0x8748
-  __DATA_CONST.__objc_classlist: 0x16c0
+  __TEXT.__unwind_info: 0xa1b4
+  __TEXT.__objc_classname: 0x6b35
+  __TEXT.__objc_methname: 0x7f371
+  __TEXT.__objc_methtype: 0x11739
+  __TEXT.__objc_stubs: 0x37fa0
+  __DATA_CONST.__got: 0x4640
+  __DATA_CONST.__const: 0x8840
+  __DATA_CONST.__objc_classlist: 0x16d0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x63cc8
-  __DATA_CONST.__objc_selrefs: 0xfe20
-  __DATA_CONST.__objc_arraydata: 0x3218
-  __AUTH_CONST.__objc_const: 0x8b8
-  __AUTH_CONST.__cfstring: 0x304a0
+  __DATA_CONST.__objc_const: 0x64b98
+  __DATA_CONST.__objc_selrefs: 0x10050
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x1970
+  __DATA_CONST.__objc_superrefs: 0x1570
+  __DATA_CONST.__objc_arraydata: 0x3208
+  __AUTH_CONST.__objc_const: 0x318
+  __AUTH_CONST.__cfstring: 0x30c60
   __AUTH_CONST.__objc_intobj: 0x4368
-  __AUTH_CONST.__objc_arrayobj: 0x22c8
-  __AUTH_CONST.__const: 0x11f0
+  __AUTH_CONST.__objc_arrayobj: 0x22b0
+  __AUTH_CONST.__const: 0xfa8
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0x960
-  __AUTH_CONST.__auth_got: 0x24f0
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1960
-  __DATA.__objc_superrefs: 0x1560
-  __DATA.__objc_ivar: 0x8318
-  __DATA.__data: 0x4a10
+  __AUTH_CONST.__auth_got: 0x2528
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x844c
+  __DATA.__data: 0x4d78
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x2e0
-  __DATA.__bss: 0x1028
-  __DATA_DIRTY.__const: 0x22c0
-  __DATA_DIRTY.__objc_const: 0x134f8
-  __DATA_DIRTY.__objc_data: 0xdca0
-  __DATA_DIRTY.__data: 0xd98
-  __DATA_DIRTY.__common: 0x640
-  __DATA_DIRTY.__bss: 0x9e8
+  __DATA.__common: 0x220
+  __DATA.__bss: 0xf10
+  __DATA_DIRTY.__const: 0x2548
+  __DATA_DIRTY.__objc_const: 0x13b70
+  __DATA_DIRTY.__objc_data: 0xe1a0
+  __DATA_DIRTY.__data: 0xde0
+  __DATA_DIRTY.__common: 0x5a0
+  __DATA_DIRTY.__bss: 0x978
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 25E93EC6-8196-34B9-96EE-7C497B1EC804
-  Functions: 18309
-  Symbols:   65640
-  CStrings:  37940
+  UUID: A5869713-026C-37D0-8B52-BDB7A59F126C
+  Functions: 18473
+  Symbols:   66172
+  CStrings:  38353
 
Symbols:
+ +[BWTemporalFilterNode initialize]
+ -[BWAttachedMediaSplitNode emitsDroppedSampleForMissingAttachedMedia]
+ -[BWAttachedMediaSplitNode setEmitsDroppedSampleForMissingAttachedMedia:]
+ -[BWCMPhotoCompressionSession addCustomMetadataContents:URI:name:]
+ -[BWCameraAppLaunchAnalyticsPayload deviceIsLocked]
+ -[BWCameraAppLaunchAnalyticsPayload deviceStolenCondition]
+ -[BWCameraAppLaunchAnalyticsPayload deviceStolenDuration]
+ -[BWCameraAppLaunchAnalyticsPayload isColdLaunch]
+ -[BWCameraAppLaunchAnalyticsPayload setDeviceIsLocked:]
+ -[BWCameraAppLaunchAnalyticsPayload setDeviceStolenCondition:]
+ -[BWCameraAppLaunchAnalyticsPayload setDeviceStolenDuration:]
+ -[BWCameraAppLaunchAnalyticsPayload setIsColdLaunch:]
+ -[BWCameraStreamingMonitor _informInternalFrameworksFromSetStreaming:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:]
+ -[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:mediaEnvironment:]
+ -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]
+ -[BWCameraStreamingMonitor setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]
+ -[BWCinematicFramingNode _getDeviceToCameraSpaceTransform:]
+ -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:pipelineType:]
+ -[BWCinematicFramingNode regionOfInterestForCameraControlsChangedHandler]
+ -[BWCinematicFramingNode regionOfInterestForCameraControls]
+ -[BWCinematicFramingNode setRegionOfInterestForCameraControlsChangedHandler:]
+ -[BWDNGCompressionSession addCustomMetadataContents:URI:name:]
+ -[BWDeepFusionProcessorController _propagateZoomAndLtmRelatedMetadataIfNeeded]
+ -[BWDeferredPipelineParameters setStillImageGDCSourceMode:]
+ -[BWDeferredPipelineParameters stillImageGDCSourceMode]
+ -[BWDeviceOrientationMonitor currentOrientation]
+ -[BWFanOutNode setDiscardsSampleBuffer:forOutputIndex:]
+ -[BWFigCaptureDeviceVendor hasActiveForClientAssertion]
+ -[BWFigVideoCaptureDevice _createBWFigVideoCaptureStreamsForCaptureStreams:attributeDictionaries:cameraParameters:synchronizedStreamsGroup:clientAuditToken:tccIdentity:mediaEnvironment:]
+ -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:]
+ -[BWFigVideoCaptureDevice _updateOrientationTotalTimes:]
+ -[BWFigVideoCaptureDevice initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:]
+ -[BWFigVideoCaptureDevice sceneClassificationConfidences]
+ -[BWFigVideoCaptureDevice setStreamingSessionAnalyticsHighlightRecoveryEnabled:]
+ -[BWFigVideoCaptureDevice setStreamingSessionAnalyticsPixelFormat:]
+ -[BWFigVideoCaptureDevice setStreamingSessionAnalyticsVideoDimensions:]
+ -[BWFigVideoCaptureDevice streamingSessionAnalyticsHighlightRecoveryEnabled]
+ -[BWFigVideoCaptureDevice streamingSessionAnalyticsPixelFormat]
+ -[BWFigVideoCaptureDevice streamingSessionAnalyticsVideoDimensions]
+ -[BWFigVideoCaptureStream completedNondisruptiveSwitchingCommandID]
+ -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:]
+ -[BWFigVideoCaptureStream mediaEnvironment]
+ -[BWFigVideoCaptureStream setCompletedNondisruptiveSwitchingCommandID:]
+ -[BWGraph _timedOutWaitingForOperationToCompleteWithDescription:]
+ -[BWInferenceProviderStorage inputSampleBufferAttachments]
+ -[BWInferenceProviderStorage setInputSampleBufferAttachments:]
+ -[BWInferenceSchedulerScaler allowsAsyncPropagation]
+ -[BWInferenceSimpleStorage inputSampleBufferAttachments]
+ -[BWInferenceSimpleStorage setInputSampleBufferAttachments:]
+ -[BWIntelligentDistortionCorrectionProcessorControllerConfiguration geometricDistortionCorrectionInputCropOffset]
+ -[BWIntelligentDistortionCorrectionProcessorControllerConfiguration setGeometricDistortionCorrectionInputCropOffset:]
+ -[BWMultiStreamCameraSourceNodeConfiguration faceTrackingNetworkFailureThresholdMultiplier]
+ -[BWMultiStreamCameraSourceNodeConfiguration faceTrackingNumTrackedFaces]
+ -[BWMultiStreamCameraSourceNodeConfiguration faceTrackingUseRecognition]
+ -[BWMultiStreamCameraSourceNodeConfiguration sensorCenterOffset]
+ -[BWMultiStreamCameraSourceNodeConfiguration setFaceTrackingNetworkFailureThresholdMultiplier:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setFaceTrackingNumTrackedFaces:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setFaceTrackingUseRecognition:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setSensorCenterOffset:]
+ -[BWPhotoEncoderNode _addGainMapForEncodingScheme:sampleBuffer:outputWidth:outputHeight:primaryOutputAspectRatio:processingFlags:parentImageHandle:]
+ -[BWPhotoEncoderNode _cropRectForRequestedSettings:inputDimensions:metadata:processingFlags:]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration description]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration dimensions]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration initWithDimensions:propagationMode:]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration initWithMainImageDownscalingFactor:propagationMode:]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration propagationMode]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration requiresEncoding]
+ -[BWPhotoEncoderNodeAttachedMediaConfiguration setPropagationMode:]
+ -[BWPhotonicEngineNodeConfiguration geometricDistortionCorrectionInputCropOffset]
+ -[BWPhotonicEngineNodeConfiguration setGeometricDistortionCorrectionInputCropOffset:]
+ -[BWPhotonicEngineNodeConfiguration setStillImageGDCSourceMode:]
+ -[BWPhotonicEngineNodeConfiguration stillImageGDCSourceMode]
+ -[BWStillImageAnalyticsPayloadCommon awbStable]
+ -[BWStillImageAnalyticsPayloadCommon depthAFStatus]
+ -[BWStillImageAnalyticsPayloadCommon lensTemperature]
+ -[BWStillImageAnalyticsPayloadCommon setAwbStable:]
+ -[BWStillImageAnalyticsPayloadCommon setDepthAFStatus:]
+ -[BWStillImageAnalyticsPayloadCommon setLensTemperature:]
+ -[BWStillImageCaptureMetadata setStreamingTime:]
+ -[BWStillImageCaptureMetadata streamingTime]
+ -[BWStreamingSessionAnalyticsPayload binned]
+ -[BWStreamingSessionAnalyticsPayload colorSpace]
+ -[BWStreamingSessionAnalyticsPayload fieldOfView]
+ -[BWStreamingSessionAnalyticsPayload highlightRecoveryEnabled]
+ -[BWStreamingSessionAnalyticsPayload maximumFrameRate]
+ -[BWStreamingSessionAnalyticsPayload maximumSupportedFrameRate]
+ -[BWStreamingSessionAnalyticsPayload minimumFrameRate]
+ -[BWStreamingSessionAnalyticsPayload minimumSupportedFrameRate]
+ -[BWStreamingSessionAnalyticsPayload orientationFaceDownTime]
+ -[BWStreamingSessionAnalyticsPayload orientationFaceUpTime]
+ -[BWStreamingSessionAnalyticsPayload pixelFormat]
+ -[BWStreamingSessionAnalyticsPayload setBinned:]
+ -[BWStreamingSessionAnalyticsPayload setColorSpace:]
+ -[BWStreamingSessionAnalyticsPayload setFieldOfView:]
+ -[BWStreamingSessionAnalyticsPayload setHighlightRecoveryEnabled:]
+ -[BWStreamingSessionAnalyticsPayload setMaximumFrameRate:]
+ -[BWStreamingSessionAnalyticsPayload setMaximumSupportedFrameRate:]
+ -[BWStreamingSessionAnalyticsPayload setMinimumFrameRate:]
+ -[BWStreamingSessionAnalyticsPayload setMinimumSupportedFrameRate:]
+ -[BWStreamingSessionAnalyticsPayload setOrientationFaceDownTime:]
+ -[BWStreamingSessionAnalyticsPayload setOrientationFaceUpTime:]
+ -[BWStreamingSessionAnalyticsPayload setPixelFormat:]
+ -[BWStreamingSessionAnalyticsPayload setVideoDimensions:]
+ -[BWStreamingSessionAnalyticsPayload videoDimensions]
+ -[BWTemporalFilterNode _dropInputSampleBuffer:]
+ -[BWTemporalFilterNode _invalidateFilterSession]
+ -[BWTemporalFilterNode _supportedOutputPixelFormats]
+ -[BWTemporalFilterNode _updateOutputRequirements]
+ -[BWTemporalFilterNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
+ -[BWTemporalFilterNode dealloc]
+ -[BWTemporalFilterNode didReachEndOfDataForInput:]
+ -[BWTemporalFilterNode didSelectFormat:forInput:]
+ -[BWTemporalFilterNode nodeSubType]
+ -[BWTemporalFilterNode nodeType]
+ -[BWTemporalFilterNode prepareForCurrentConfigurationToBecomeLive]
+ -[BWTemporalFilterNode renderSampleBuffer:forInput:]
+ -[FigCaptureCameraSourcePipeline updateForChangesInVideoDataConnectionConfigurations:]
+ -[FigCaptureCinematographyPipeline _buildCinematographyPipeline:videoSourceCaptureOutput:sourceSemanticMasksOutput:previewOutput:auxiliaryOutput:sourceID:graph:captureDevice:inferenceScheduler:]
+ -[FigCaptureCinematographyPipeline initWithConfiguration:videoSourceCaptureOutput:sourceSemanticMasksOutput:previewOutput:auxiliaryOutput:graph:name:sourceID:captureDevice:inferenceScheduler:errorOut:]
+ -[FigCaptureClientApplicationStateMonitor _handleLayout:]
+ -[FigCaptureClientApplicationStateMonitor _handleMediaEndowmentUpdate:]
+ -[FigCaptureClientApplicationStateMonitor _updateMediaEnvironmentWithEndowmentInfos:evaluateLayout:]
+ -[FigCaptureClientApplicationStateMonitor initWithClientAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:]
+ -[FigCaptureClientApplicationStateMonitor mediaEnvironmentTCCIdentity]
+ -[FigCaptureClientApplicationStateMonitor mediaEnvironment]
+ -[FigCaptureClientApplicationStateMonitorClient initWithAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:]
+ -[FigCaptureClientApplicationStateMonitorClient mediaEnvironmentBundleID]
+ -[FigCaptureClientApplicationStateMonitorClient mediaEnvironmentTCCIdentity]
+ -[FigCaptureClientApplicationStateMonitorClient mediaEnvironment]
+ -[FigCaptureClientApplicationStateMonitorClient setMediaEnvironmentBundleID:]
+ -[FigCaptureClientApplicationStateMonitorClient setMediaEnvironmentTCCIdentity:]
+ -[FigCaptureDeviceLockStateMonitor deviceIsLocked]
+ -[FigCaptureDisplayLayout isPaymentServiceVisible]
+ -[FigCaptureDisplayLayout setPaymentServiceVisible:]
+ -[FigCaptureDisplayLayoutMonitor currentLayout]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration gdcInDCProcessorInputCropOffset]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setGdcInDCProcessorInputCropOffset:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setStillImageGDCSourceMode:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration stillImageGDCSourceMode]
+ -[FigCapturePowerLogMissingCameraStopEventObserver _cameraAppIsForegroundInLayout:]
+ -[FigCapturePowerLogMissingCameraStopEventObserver _cancelCameraAppStreamingTimer]
+ -[FigCapturePowerLogMissingCameraStopEventObserver _checkCameraAppPowerEventsForAnyStreamingCameras]
+ -[FigCapturePowerLogMissingCameraStopEventObserver _showTTRPromptIfNecessary]
+ -[FigCapturePowerLogMissingCameraStopEventObserver _startCameraAppStreamingTimer]
+ -[FigCapturePowerLogMissingCameraStopEventObserver dealloc]
+ -[FigCapturePowerLogMissingCameraStopEventObserver initWithQueue:]
+ -[FigCapturePowerLogMissingCameraStopEventObserver layoutMonitor:didUpdateLayout:]
+ -[FigCapturePreviewSinkPipeline _appendFilteredPreviewPipeline:desiredPipelineStage:desiredStreamingFilterPipelineStage:previewSinkPipelineConfiguration:videoPreviewSinkConnectionConfiguration:graph:inferenceScheduler:captureDevice:focusBlurMapForDepthFiltersEnabled:depthFromMonocularNetworkEnabled:maxLossyCompressionLevel:metalCommandQueue:zoomBeforeDepthFilterRenderingEnabled:portriatAutoSuggestEnabled:]
+ -[FigCapturePreviewSinkPipeline _buildVideoPreviewSinkPipeline:sourcePreviewOutput:graph:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:]
+ -[FigCapturePreviewSinkPipeline initWithConfiguration:sourcePreviewOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:]
+ -[FigCaptureSourceCompanionFormat sensorCenterOffset]
+ -[FigCaptureSourceVideoFormat sensorCenterOffset]
+ -[FigCaptureVideoDataSinkConfiguration active]
+ -[FigCaptureVideoDataSinkConfiguration setActive:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration cinematicFramingEnabled]
+ -[FigCaptureVideoDataSinkPipelineConfiguration deskCamEnabled]
+ -[FigCaptureVideoDataSinkPipelineConfiguration manualCinematicFramingEnabled]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setCenterStageFramingMode:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setGazeSelectionEnabled:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setOverheadCameraMode:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setSubjectSelectionEnabled:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setTemporalFilterEnabled:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration subjectSelectionEnabled]
+ GCC_except_table103
+ GCC_except_table174
+ GCC_except_table202
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table294
+ GCC_except_table347
+ GCC_except_table422
+ GCC_except_table423
+ _.compoundliteral.43
+ _.compoundliteral.44
+ _.compoundliteral.46
+ _.compoundliteral.47
+ _.compoundliteral.49
+ _.compoundliteral.54
+ _.compoundliteral.62
+ _.compoundliteral.65
+ _.compoundliteral.66
+ _.compoundliteral.69
+ _.compoundliteral.70
+ _.compoundliteral.77
+ _.compoundliteral.78
+ _.compoundliteral.79
+ _.compoundliteral.80
+ _.compoundliteral.81
+ _.compoundliteral.82
+ _BWDroppedSampleReasonAttachedMediaNotFound
+ _BWDroppedSampleReasonTemporalFilterSessionFailure
+ _BWFigVideoCaptureDevicePropertySceneClassificationConfidences
+ _BWFigVideoCaptureDeviceSceneClassificationConfidencesChangedNotification
+ _BWFigVideoCaptureDeviceSmartCameraEnabledChangedNotification
+ _BWPixelBufferColorSpace
+ _BWPixelBufferIsHDR
+ _CGRectIsInfinite
+ _CMPhotoCompressionSessionAddCustomMetadata
+ _CMSimpleQueueReset
+ _CVImageBufferCreateColorSpaceFromAttachments
+ _FigCaptureCameraRequires180DegreesRotation
+ _FigCaptureClientApplicationIdentifierMusic
+ _FigCaptureClientApplicationIdentifierProximityReaderSceneUI
+ _FigCaptureClientIsWebBrowserRenderingExtension
+ _FigCaptureDeferredPhotoProcessorIsAllowedToPrewarm
+ _FigCaptureMediaEndowmentNamespace
+ _FigCaptureSourceFormatKey_SensorCenterOffsetX
+ _FigCaptureSourceFormatKey_SensorCenterOffsetY
+ _FigCaptureSourceGetSourceDeviceType
+ _OBJC_CLASS_$_BWTemporalFilterNode
+ _OBJC_CLASS_$_FigCapturePowerLogMissingCameraStopEventObserver
+ _OBJC_IVAR_$_BWAttachedMediaSplitNode._emitsDroppedSampleForMissingAttachedMedia
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._deviceIsLocked
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._deviceStolenCondition
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._deviceStolenDuration
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._isColdLaunch
+ _OBJC_IVAR_$_BWCinematicFramingNode._pipelineType
+ _OBJC_IVAR_$_BWCinematicFramingNode._regionOfInterestForCameraControls
+ _OBJC_IVAR_$_BWCinematicFramingNode._regionOfInterestForCameraControlsChangedHandler
+ _OBJC_IVAR_$_BWDeferredPipelineParameters._stillImageGDCSourceMode
+ _OBJC_IVAR_$_BWFanOutNode._outputsDiscardsSampleBuffer
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._colorSpace
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationFaceDownTotalTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationFaceUpTotalTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stillImageCaptureNowBusyCount
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._streamingSessionAnalyticsHighlightRecoveryEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._streamingSessionAnalyticsPixelFormat
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._streamingSessionAnalyticsVideoDimensions
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._completedNondisruptiveSwitchingCommandID
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._firstValidFrameSeen
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._mediaEnvironment
+ _OBJC_IVAR_$_BWInferenceProviderStorage._inputSampleBufferAttachments
+ _OBJC_IVAR_$_BWInferenceSchedulerScaler._allowsAsyncPropagation
+ _OBJC_IVAR_$_BWInferenceSimpleStorage._inputSampleBufferAttachments
+ _OBJC_IVAR_$_BWIntelligentDistortionCorrectionProcessorControllerConfiguration._geometricDistortionCorrectionInputCropOffset
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._faceTrackingNetworkFailureThresholdMultiplier
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._faceTrackingNumTrackedFaces
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._faceTrackingUseRecognition
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._sensorCenterOffset
+ _OBJC_IVAR_$_BWPhotoEncoderNodeAttachedMediaConfiguration._dimensions
+ _OBJC_IVAR_$_BWPhotoEncoderNodeAttachedMediaConfiguration._propagationMode
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._geometricDistortionCorrectionInputCropOffset
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._stillImageGDCSourceMode
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._awbStable
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._depthAFStatus
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._lensTemperature
+ _OBJC_IVAR_$_BWStillImageCaptureMetadata._streamingTime
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._binned
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._colorSpace
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._fieldOfView
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._highlightRecoveryEnabled
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._maximumFrameRate
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._maximumSupportedFrameRate
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._minimumFrameRate
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._minimumSupportedFrameRate
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._orientationFaceDownTime
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._orientationFaceUpTime
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._pixelFormat
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._videoDimensions
+ _OBJC_IVAR_$_BWTemporalFilterNode._dumpInputVideo
+ _OBJC_IVAR_$_BWTemporalFilterNode._dumpOutputVideo
+ _OBJC_IVAR_$_BWTemporalFilterNode._inputSampleBufferQueue
+ _OBJC_IVAR_$_BWTemporalFilterNode._inputSampleBufferQueueLock
+ _OBJC_IVAR_$_BWTemporalFilterNode._maxLossyCompressionLevel
+ _OBJC_IVAR_$_BWTemporalFilterNode._mctfSession
+ _OBJC_IVAR_$_BWTemporalFilterNode._videoInput
+ _OBJC_IVAR_$_BWTemporalFilterNode._videoOutput
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._videoCaptureSplitterNode
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._ispFaceTrackingNetworkFailureThresholdMultiplier
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._ispFaceTrackingNumTrackedFaces
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._ispFaceTrackingUseRecognition
+ _OBJC_IVAR_$_FigCaptureClientApplicationStateMonitor._mediaEndowmentMonitor
+ _OBJC_IVAR_$_FigCaptureClientApplicationStateMonitorClient._mediaEnvironment
+ _OBJC_IVAR_$_FigCaptureClientApplicationStateMonitorClient._mediaEnvironmentBundleID
+ _OBJC_IVAR_$_FigCaptureClientApplicationStateMonitorClient._mediaEnvironmentTCCIdentity
+ _OBJC_IVAR_$_FigCaptureDisplayLayout._paymentServiceVisible
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._gdcInDCProcessorInputCropOffset
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._stillImageGDCSourceMode
+ _OBJC_IVAR_$_FigCapturePowerLogMissingCameraStopEventObserver._cameraAppStreamingTimer
+ _OBJC_IVAR_$_FigCapturePowerLogMissingCameraStopEventObserver._eventDateFormatter
+ _OBJC_IVAR_$_FigCapturePowerLogMissingCameraStopEventObserver._layoutMonitor
+ _OBJC_IVAR_$_FigCapturePowerLogMissingCameraStopEventObserver._observerQueue
+ _OBJC_IVAR_$_FigCapturePowerLogMissingCameraStopEventObserver._previousLayoutHasForegroundCameraApp
+ _OBJC_IVAR_$_FigCaptureSourceCompanionFormat._sensorCenterOffset
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkConfiguration._active
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._centerStageFramingMode
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._cinematicFramingEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._deskCamEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._gazeSelectionEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._manualCinematicFramingEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._overheadCameraMode
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._subjectSelectionEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._temporalFilterEnabled
+ _OBJC_METACLASS_$_BWTemporalFilterNode
+ _OBJC_METACLASS_$_FigCapturePowerLogMissingCameraStopEventObserver
+ _ReplayKitLibraryCore
+ _ReplayKitLibraryCore.frameworkLibrary
+ _VTTemporalFilterSessionCompleteFrames
+ _VTTemporalFilterSessionCreate
+ _VTTemporalFilterSessionInvalidate
+ _VTTemporalFilterSessionProcessFrame
+ __OBJC_$_CLASS_METHODS_BWTemporalFilterNode
+ __OBJC_$_CLASS_PROP_LIST_FigCaptureStillImageSinkPipeline.345
+ __OBJC_$_INSTANCE_METHODS_BWTemporalFilterNode
+ __OBJC_$_INSTANCE_METHODS_FigCapturePowerLogMissingCameraStopEventObserver
+ __OBJC_$_INSTANCE_VARIABLES_BWTemporalFilterNode
+ __OBJC_$_INSTANCE_VARIABLES_FigCapturePowerLogMissingCameraStopEventObserver
+ __OBJC_$_PROP_LIST_BWFigVideoCaptureDeviceCenterStageDelegate
+ __OBJC_$_PROP_LIST_FigCapturePowerLogMissingCameraStopEventObserver
+ __OBJC_$_PROP_LIST_FigCaptureStillImageSinkPipeline.363
+ __OBJC_CLASS_PROTOCOLS_$_FigCapturePowerLogMissingCameraStopEventObserver
+ __OBJC_CLASS_RO_$_BWTemporalFilterNode
+ __OBJC_CLASS_RO_$_FigCapturePowerLogMissingCameraStopEventObserver
+ __OBJC_METACLASS_RO_$_BWTemporalFilterNode
+ __OBJC_METACLASS_RO_$_FigCapturePowerLogMissingCameraStopEventObserver
+ __PromotedConst.220
+ __PromotedConst.221
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.101
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.142
+ ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.315
+ ___119-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke
+ ___131-[BWCameraStreamingMonitor setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke
+ ___17-[BWGraph start:]_block_invoke.54
+ ___17-[BWGraph start:]_block_invoke.62
+ ___280-[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:]_block_invoke
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.558
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.876
+ ___50-[BWFigVideoCaptureDevice setCenterStageDelegate:]_block_invoke
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke.206
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_2.207
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_3.208
+ ___50-[FigCaptureDeviceLockStateMonitor deviceIsLocked]_block_invoke
+ ___52-[BWTemporalFilterNode _supportedOutputPixelFormats]_block_invoke
+ ___55-[BWFigCaptureDeviceVendor hasActiveForClientAssertion]_block_invoke
+ ___59-[FigCaptureClientApplicationStateMonitor _initWithClient:]_block_invoke
+ ___59-[FigCaptureClientApplicationStateMonitor _initWithClient:]_block_invoke_2
+ ___61-[BWFigVideoCaptureDevice setManualCinematicFramingDelegate:]_block_invoke
+ ___62-[BWMultiStreamCameraSourceNode _registerStreamOutputHandlers]_block_invoke_11
+ ___64-[BWPhotoEncoderNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.186
+ ___78-[BWDeepFusionProcessorController _propagateZoomAndLtmRelatedMetadataIfNeeded]_block_invoke
+ ___78-[BWDeepFusionProcessorController _propagateZoomAndLtmRelatedMetadataIfNeeded]_block_invoke_2
+ ___81-[FigCapturePowerLogMissingCameraStopEventObserver _startCameraAppStreamingTimer]_block_invoke
+ ___82-[FigCapturePowerLogMissingCameraStopEventObserver layoutMonitor:didUpdateLayout:]_block_invoke
+ ___97-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:mediaEnvironment:]_block_invoke
+ ___97-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:mediaEnvironment:]_block_invoke.29
+ ___FigCaptureCameraStreamingPowerLogInitialize_block_invoke_2
+ ___ReplayKitLibraryCore_block_invoke
+ ___block_descriptor_109_e8_32o40o48o56o64b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8l
+ ___block_descriptor_40_e8_32o_e40_v16?0"<RBSProcessMonitorConfiguring>"8ls32l8
+ ___block_descriptor_40_e8_32o_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0i8lw32l8
+ ___block_descriptor_76_e8_32o_e40_v16?0"STMutableMediaStatusDomainData"8ls32l8
+ ___block_literal_global.102
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.121
+ ___block_literal_global.127
+ ___block_literal_global.145
+ ___block_literal_global.147
+ ___block_literal_global.176
+ ___block_literal_global.189
+ ___block_literal_global.202
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.219
+ ___block_literal_global.225
+ ___block_literal_global.227
+ ___block_literal_global.229
+ ___block_literal_global.239
+ ___block_literal_global.249
+ ___block_literal_global.251
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.270
+ ___block_literal_global.274
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.325
+ ___block_literal_global.330
+ ___block_literal_global.364
+ ___block_literal_global.375
+ ___block_literal_global.426
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.485
+ ___block_literal_global.487
+ ___block_literal_global.489
+ ___block_literal_global.491
+ ___block_literal_global.493
+ ___block_literal_global.495
+ ___block_literal_global.598
+ ___block_literal_global.600
+ ___block_literal_global.602
+ ___block_literal_global.604
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
+ ___block_literal_global.666
+ ___block_literal_global.686
+ ___block_literal_global.689
+ ___block_literal_global.692
+ ___block_literal_global.714
+ ___block_literal_global.716
+ ___block_literal_global.718
+ ___block_literal_global.720
+ ___block_literal_global.722
+ ___block_literal_global.724
+ ___block_literal_global.726
+ ___block_literal_global.728
+ ___block_literal_global.773
+ ___block_literal_global.798
+ ___block_literal_global.836
+ ___block_literal_global.86
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___block_literal_global.97
+ ___block_literal_global.99
+ ___captureDeferredPhotoProcessor_CancelAllPrewarming_block_invoke.135
+ ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.125
+ ___captureDeferredPhotoProcessor_workloop_block_invoke.119
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.760
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.758
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.754
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke.547
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.548
+ ___captureSession_updateRunningCondition_block_invoke.379
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.676
+ ___dfp_createStateMachine_block_invoke.485
+ ___fcc_frontCameraOrientation_block_invoke
+ ___getSTAttributedEntityClass_block_invoke
+ ___getSTAttributedEntityClass_block_invoke.cold.1
+ ___getSTExecutableIdentityClass_block_invoke
+ ___getSTExecutableIdentityClass_block_invoke.cold.1
+ ___getshowReactionsTipSymbolLoc_block_invoke
+ ___getshowReactionsTipSymbolLoc_block_invoke.cold.1
+ __unnamed_array_storage.113
+ __unnamed_array_storage.118
+ __unnamed_array_storage.137
+ __unnamed_array_storage.144
+ __unnamed_array_storage.153
+ __unnamed_array_storage.190
+ __unnamed_array_storage.218
+ __unnamed_array_storage.226
+ __unnamed_array_storage.277
+ __unnamed_array_storage.381
+ __unnamed_array_storage.477
+ __unnamed_array_storage.546
+ __unnamed_array_storage.554
+ __unnamed_array_storage.826
+ __unnamed_array_storage.888
+ _audit_stringReplayKit
+ _btfn_temporalFilterSessionCallback
+ _captureSession_createDepthDataPipelineConfiguration
+ _captureSession_createVideoDataSinkPipeline
+ _captureSession_teardownImageQueueSinkNodesIfNeeded
+ _cs_sendNotificationOfNewTransientValue.cold.1
+ _dispatch_assert_queue$V2
+ _dispatch_block_wait
+ _fcc_frontCameraOrientation.onceToken
+ _fcc_frontCameraOrientation.sFrontCameraOrientation
+ _fvcd_handleRegionOfInterestChangedForCameraControlsFromFramingDelegates
+ _gBWTemporalFilterNodeTrace
+ _gFigCapturePowerLogTrace
+ _gFigCaptureUtilitiesTrace
+ _getSTAttributedEntityClass
+ _getSTAttributedEntityClass.softClass
+ _getSTExecutableIdentityClass
+ _getSTExecutableIdentityClass.softClass
+ _getshowReactionsTipSymbolLoc
+ _getshowReactionsTipSymbolLoc.ptr
+ _kCMPhotoCustomMetadata_Data
+ _kCMPhotoCustomMetadata_Name
+ _kCMPhotoCustomMetadata_URI
+ _kCVImageBufferCGColorSpaceKey
+ _kFigBarcodeScannerSampleBufferProcessorProperty_Prepare
+ _kFigCaptureDeviceRequestControlOfStreamsOptionsKey_ClientPriority
+ _kFigCaptureISPProcessingSessionOutputID_PrimaryScalerLowRes
+ _kFigCaptureSampleBufferAttachmentKey_DebugPixelData
+ _kFigCaptureSessionCreateMsgParam_MediaEnvironment
+ _kFigCaptureSourceProperty_SceneClassificationActive
+ _kFigCaptureSourceProperty_SceneClassificationConfidences
+ _kFigCaptureStreamAFStatusExtendedKey_DepthAFStatus
+ _kFigCaptureStreamMetadata_AFStatusExtended
+ _kFigCaptureStreamMetadata_LensTemperature
+ _kFigCaptureStreamProperty_ManualFramingDeviceType
+ _kFigCaptureStreamVideoOutputID_ProResRaw
+ _kFigCaptureVideoSourceUniqueID_FrontSuperWideMetadata
+ _kMXSystemControllerMediaEndowmentPayload_AuditToken
+ _kMXSystemControllerMediaEndowmentPayload_BundleID
+ _kMXSystemControllerMediaEndowmentPayload_RecordingWebsite
+ _kVTTemporalFilterClass_TemporalNoiseReduction
+ _kVTTemporalFilterPropertyKey_OutputPixelBufferPool
+ _kVTTemporalFilterSessionOptions_ClientPID
+ _kVTTemporalFilterSessionOptions_ShortName
+ _kVTTemporalFilterSpecification_TemporalFilterID
+ _multiStreamCameraSourceNode_proresRawServiceQueueCallback
+ _objc_msgSend$_initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:
+ _objc_msgSend$completedNondisruptiveSwitchingCommandID
+ _objc_msgSend$currentOrientation
+ _objc_msgSend$deviceIsLocked
+ _objc_msgSend$endowment
+ _objc_msgSend$endowmentInfoForHandle
+ _objc_msgSend$endowmentInfos
+ _objc_msgSend$endowmentNamespace
+ _objc_msgSend$environment
+ _objc_msgSend$gdcInDCProcessorInputCropOffset
+ _objc_msgSend$geometricDistortionCorrectionInputCropOffset
+ _objc_msgSend$initWithAttributedEntity:activeEntity:
+ _objc_msgSend$initWithAuditToken:
+ _objc_msgSend$initWithAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:
+ _objc_msgSend$initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:
+ _objc_msgSend$initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:
+ _objc_msgSend$initWithClientAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:
+ _objc_msgSend$initWithConfiguration:sourcePreviewOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:
+ _objc_msgSend$initWithExecutableIdentity:
+ _objc_msgSend$initWithExecutableIdentity:website:
+ _objc_msgSend$initWithMainImageDownscalingFactor:propagationMode:
+ _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:pipelineType:
+ _objc_msgSend$inputSampleBufferAttachments
+ _objc_msgSend$isPaymentServiceVisible
+ _objc_msgSend$mediaEnvironment
+ _objc_msgSend$mediaEnvironmentBundleID
+ _objc_msgSend$mediaEnvironmentTCCIdentity
+ _objc_msgSend$regionOfInterestForCameraControls
+ _objc_msgSend$requiresEncoding
+ _objc_msgSend$sceneClassificationConfidences
+ _objc_msgSend$sensorCenterOffset
+ _objc_msgSend$setAwbStable:
+ _objc_msgSend$setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:
+ _objc_msgSend$setCompletedNondisruptiveSwitchingCommandID:
+ _objc_msgSend$setDepthAFStatus:
+ _objc_msgSend$setDeviceIsLocked:
+ _objc_msgSend$setDeviceStolenCondition:
+ _objc_msgSend$setDeviceStolenDuration:
+ _objc_msgSend$setDeviceToCameraSpaceTransform:
+ _objc_msgSend$setFaceTrackingNumTrackedFaces:
+ _objc_msgSend$setFaceTrackingUseRecognition:
+ _objc_msgSend$setFieldOfView:
+ _objc_msgSend$setGdcInDCProcessorInputCropOffset:
+ _objc_msgSend$setGeometricDistortionCorrectionInputCropOffset:
+ _objc_msgSend$setInputSampleBufferAttachments:
+ _objc_msgSend$setIsColdLaunch:
+ _objc_msgSend$setLensTemperature:
+ _objc_msgSend$setMediaEnvironmentBundleID:
+ _objc_msgSend$setMediaEnvironmentTCCIdentity:
+ _objc_msgSend$setOrientationFaceDownTime:
+ _objc_msgSend$setOrientationFaceUpTime:
+ _objc_msgSend$setPaymentServiceVisible:
+ _objc_msgSend$setPropagationMode:
+ _objc_msgSend$setRegionOfInterestForCameraControlsChangedHandler:
+ _objc_msgSend$setSensorCenterOffset:
+ _objc_msgSend$setStillImageGDCSourceMode:
+ _objc_msgSend$setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:
+ _objc_msgSend$setStreamingSessionAnalyticsHighlightRecoveryEnabled:
+ _objc_msgSend$setStreamingSessionAnalyticsPixelFormat:
+ _objc_msgSend$setStreamingSessionAnalyticsVideoDimensions:
+ _objc_msgSend$setVideoDimensions:
+ _objc_msgSend$warpCGRect:fromCamera:toCamera:
+ _sCameraStreamingPowerEventsByPortType
+ _sMissingCameraStopEventObserver
+ _sOSStateHandle
+ _sTemporaryCameraHistoryItemsLock
- -[BWCameraStreamingMonitor _informInternalFrameworksFromSetStreaming:deviceType:clientAuditToken:tccIdentity:]
- -[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]
- -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:completionHandler:]
- -[BWCameraStreamingMonitor setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:completionHandler:]
- -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:]
- -[BWDeepFusionProcessorController _propagateZoomRelatedMetadataIfNeeded]
- -[BWFigCaptureStream _registerForNotificationBarrier]
- -[BWFigCaptureStream _unregisterForNotificationBarrier]
- -[BWFigCaptureStream waitForNotificationBarrier]
- -[BWFigVideoCaptureDevice _createBWFigVideoCaptureStreamsForCaptureStreams:attributeDictionaries:cameraParameters:synchronizedStreamsGroup:clientAuditToken:tccIdentity:]
- -[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:]
- -[BWFigVideoCaptureDevice initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:error:]
- -[BWFigVideoCaptureStream initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:error:]
- -[BWGraph _waitForSourceNodesToStart].cold.1
- -[BWPhotoEncoderNode _addGainMapForEncodingScheme:sampleBuffer:outputWidth:outputHeight:primaryOutputAspectRatio:processingFlags:parentImageHanlde:]
- -[BWPhotoEncoderNode _aspectRatioAdjustmentFactorForSbuf:]
- -[BWPhotoEncoderNode _cropRectForSampleBuffer:metadata:]
- -[BWPhotoEncoderNodeAttachedMediaConfiguration initWithMainImageDownscalingFactor:propagatesDownstream:]
- -[BWStillImageAnalyticsPayloadCommon deliverAsCameraAppSpecificEvent]
- -[BWStillImageAnalyticsPayloadCommon setDeliverAsCameraAppSpecificEvent:]
- -[FigCaptureCinematographyPipeline _buildCinematographyPipeline:videoSourceCaptureOutput:previewOutput:auxiliaryOutput:sourceID:graph:captureDevice:inferenceScheduler:]
- -[FigCaptureCinematographyPipeline initWithConfiguration:videoSourceCaptureOutput:previewOutput:auxiliaryOutput:graph:name:sourceID:captureDevice:inferenceScheduler:errorOut:]
- -[FigCaptureClientApplicationStateMonitor initWithClientAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:]
- -[FigCaptureClientApplicationStateMonitorClient initWithAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:]
- -[FigCaptureDisplayLayout isContactlessUIServiceVisible]
- -[FigCaptureDisplayLayout setContactlessUIServiceVisible:]
- -[FigCapturePreviewSinkPipeline _appendFilteredPreviewPipeline:desiredPipelineStage:desiredStreamingFilterPipelineStage:videoPreviewSinkConnectionConfiguration:graph:inferenceScheduler:captureDevice:focusBlurMapForDepthFiltersEnabled:depthFromMonocularNetworkEnabled:maxLossyCompressionLevel:zoomBeforeDepthFilterRenderingEnabled:portriatAutoSuggestEnabled:]
- -[FigCapturePreviewSinkPipeline _buildVideoPreviewSinkPipeline:sourcePreviewOutput:sourceSemanticMasksOutput:graph:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:]
- -[FigCapturePreviewSinkPipeline initWithConfiguration:sourcePreviewOutput:sourceSemanticMasksOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:]
- GCC_except_table172
- GCC_except_table200
- GCC_except_table232
- GCC_except_table233
- GCC_except_table286
- GCC_except_table338
- GCC_except_table413
- GCC_except_table414
- GCC_except_table57
- _.compoundliteral.30
- _.compoundliteral.31
- _.compoundliteral.32
- _.compoundliteral.33
- _.compoundliteral.35
- _.compoundliteral.36
- _.compoundliteral.58
- _.compoundliteral.67
- _.compoundliteral.72
- _.compoundliteral.75
- _.compoundliteral.76
- _.compoundliteral.85
- _.compoundliteral.86
- _.compoundliteral.87
- _.compoundliteral.88
- _.compoundliteral.89
- _.compoundliteral.90
- _BWDeviceModelIsD3yD8x
- _CMNotificationCenterBarrier
- _CMNotificationCenterRegisterForBarrierSupport
- _CMNotificationCenterUnregisterForBarrierSupport
- _OBJC_IVAR_$_BWFigVideoCaptureDevice._nonDisruptiveSwitchOverPreventingStillImageCaptureInProgress
- _OBJC_IVAR_$_BWFigVideoCaptureDevice._variableFrameRateMostRecentInferenceResult
- _OBJC_IVAR_$_BWPhotoEncoderNodeAttachedMediaConfiguration._propagatesDownstream
- _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._deliverAsCameraAppSpecificEvent
- _OBJC_IVAR_$_FigCaptureDisplayLayout._contactlessUIServiceVisible
- __OBJC_$_CLASS_PROP_LIST_FigCaptureStillImageSinkPipeline.344
- __OBJC_$_PROP_LIST_FigCaptureStillImageSinkPipeline.362
- ___102-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:completionHandler:]_block_invoke
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.100
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.141
- ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.287
- ___114-[BWCameraStreamingMonitor setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:completionHandler:]_block_invoke
- ___17-[BWGraph start:]_block_invoke.59
- ___17-[BWGraph start:]_block_invoke_2
- ___263-[BWFigVideoCaptureDevice _initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:]_block_invoke
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.536
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.854
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke.181
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_2.182
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_3.183
- ___64-[BWPhotoEncoderNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.157
- ___72-[BWDeepFusionProcessorController _propagateZoomRelatedMetadataIfNeeded]_block_invoke
- ___72-[BWDeepFusionProcessorController _propagateZoomRelatedMetadataIfNeeded]_block_invoke_2
- ___80-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]_block_invoke
- ___80-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]_block_invoke.28
- ___block_descriptor_64_e40_v16?0"STMutableMediaStatusDomainData"8l
- ___block_descriptor_93_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.105
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.120
- ___block_literal_global.125
- ___block_literal_global.134
- ___block_literal_global.137
- ___block_literal_global.141
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.183
- ___block_literal_global.193
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.209
- ___block_literal_global.215
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.220
- ___block_literal_global.224
- ___block_literal_global.226
- ___block_literal_global.228
- ___block_literal_global.233
- ___block_literal_global.248
- ___block_literal_global.250
- ___block_literal_global.253
- ___block_literal_global.255
- ___block_literal_global.257
- ___block_literal_global.269
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.322
- ___block_literal_global.327
- ___block_literal_global.361
- ___block_literal_global.367
- ___block_literal_global.416
- ___block_literal_global.483
- ___block_literal_global.486
- ___block_literal_global.488
- ___block_literal_global.490
- ___block_literal_global.492
- ___block_literal_global.494
- ___block_literal_global.56
- ___block_literal_global.597
- ___block_literal_global.599
- ___block_literal_global.601
- ___block_literal_global.603
- ___block_literal_global.605
- ___block_literal_global.607
- ___block_literal_global.609
- ___block_literal_global.658
- ___block_literal_global.678
- ___block_literal_global.681
- ___block_literal_global.683
- ___block_literal_global.684
- ___block_literal_global.710
- ___block_literal_global.713
- ___block_literal_global.715
- ___block_literal_global.719
- ___block_literal_global.721
- ___block_literal_global.723
- ___block_literal_global.725
- ___block_literal_global.727
- ___block_literal_global.770
- ___block_literal_global.775
- ___block_literal_global.81
- ___block_literal_global.813
- ___block_literal_global.85
- ___block_literal_global.87
- ___captureDeferredPhotoProcessor_CancelAllPrewarming_block_invoke.134
- ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.124
- ___captureDeferredPhotoProcessor_workloop_block_invoke.118
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.754
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.752
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.748
- ___captureSession_startObservingForAudiomxdDeath_block_invoke.539
- ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.540
- ___captureSession_updateRunningCondition_block_invoke.374
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.668
- ___dfp_createStateMachine_block_invoke.484
- __unnamed_array_storage.103
- __unnamed_array_storage.117
- __unnamed_array_storage.133
- __unnamed_array_storage.138
- __unnamed_array_storage.152
- __unnamed_array_storage.154
- __unnamed_array_storage.225
- __unnamed_array_storage.232
- __unnamed_array_storage.237
- __unnamed_array_storage.306
- __unnamed_array_storage.377
- __unnamed_array_storage.449
- __unnamed_array_storage.474
- __unnamed_array_storage.543
- __unnamed_array_storage.803
- __unnamed_array_storage.865
- __unnamed_array_storage.98
- _captureSession_resetCameraAppSessionStartupTelemetry
- _kFigCaptureStreamProperty_OptimizedForBaselineProcessing
- _objc_msgSend$_initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:
- _objc_msgSend$deliverAsCameraAppSpecificEvent
- _objc_msgSend$initWithAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:
- _objc_msgSend$initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:error:
- _objc_msgSend$initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:error:
- _objc_msgSend$initWithClientAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:
- _objc_msgSend$initWithConfiguration:sourcePreviewOutput:sourceSemanticMasksOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:
- _objc_msgSend$initWithMainImageDownscalingFactor:propagatesDownstream:
- _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:
- _objc_msgSend$isContactlessUIServiceVisible
- _objc_msgSend$setCameraAccess:deviceType:clientAuditToken:tccIdentity:completionHandler:
- _objc_msgSend$setContactlessUIServiceVisible:
- _objc_msgSend$setDeliverAsCameraAppSpecificEvent:
- _objc_msgSend$setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:completionHandler:
- _objc_msgSend$waitForNotificationBarrier
- _qtmfsn_pixelBufferIsHDR
- _rqsn_sampleBufferIsHDR
- _sCameraStreamingPowerEventsByCameraType
CStrings:
+ " enableTelemetry=YES "
+ "! stream->streaming"
+ "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d O:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@%@"
+ "%@: Camera Streaming Power Events: %@"
+ "%@: Metadata ID:%d, active ID:%d."
+ "( ! FigCFEqual( _captureStream.portType, kFigCapturePortType_FrontFacingInfraredCamera ) ) || ( _deviceType == BWCaptureDeviceTypeInfraredMetadataCamera )"
+ "( ! error && sampleBuffer )"
+ "( outputIndex > -1 ) && ( outputIndex < 16 )"
+ "((! deviceCheck ) || hasCaptureDevice)"
+ ", gdcSourceMode:%d"
+ ", mediaEnvironment: %@"
+ "-[BWCameraStreamingMonitor _informInternalFrameworksFromSetStreaming:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:]"
+ "-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:mediaEnvironment:]"
+ "-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:mediaEnvironment:]_block_invoke"
+ "-[BWDeferredCaptureControllerInput encounteredProcessingError:]"
+ "-[BWFigCaptureDeviceVendor _showISPLeftOnTapToRadarPromptIfNecessary:radarTitle:radarDescription:radarClassification:radarReproducibility:]"
+ "-[BWFigVideoCaptureStream setActiveNondisruptiveSwitchingFormatIndex:]"
+ "-[BWGraph _timedOutWaitingForOperationToCompleteWithDescription:]"
+ "-[BWGraph _waitForSourceNodesToStart]"
+ "-[BWGraph cancelDeferredNodePrepare]"
+ "-[BWGraph cancelDeferredSourceNodeStart]"
+ "-[BWGraph dealloc]"
+ "-[BWGraph enableDeferredStartForSourceNode:]"
+ "-[BWGraph initWithConfigurationQueuePriority:]"
+ "-[BWGraph startDeferredSourceNodesIfNeeded]"
+ "-[BWGraph waitForStartOrCommitToComplete]"
+ "-[BWTemporalFilterNode configurationWithID:updatedFormat:didBecomeLiveForInput:]"
+ "-[FigCaptureClientApplicationStateMonitor _handleMediaEndowmentUpdate:]"
+ "-[FigCaptureClientApplicationStateMonitor _updateMediaEnvironmentWithEndowmentInfos:evaluateLayout:]"
+ "-[FigCaptureDeferredProcessingEngine _shouldReuseGraphForContainer:]"
+ "-[FigCapturePowerLogMissingCameraStopEventObserver _checkCameraAppPowerEventsForAnyStreamingCameras]"
+ "-[FigCapturePowerLogMissingCameraStopEventObserver _showTTRPromptIfNecessary]"
+ "<%@ %p>: %@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "<%@ %p>: mainImageDownscalingFactor:%f, dimensions:%dx%d, mode:%@"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Media environment doesn't have audit token. Send camera streaming ON message to SystemStatus for %d"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming ON message to MediaSafetyNet for %d"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming ON message to SystemStatus for %d"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming ON message to SystemStatus for active identity %d, attributed identity %d, website: %{private}@"
+ "<<<< BWDeepFusionProcessorController >>>> %s: Skipping adding frame of type '%{public}@' for '%{private}@' (requestErr:%d)"
+ "<<<< BWDerectificationInferenceProvider >>>> Fig"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Not showing prompt because the build hasn't changed since the last time the prompt was shown."
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Not showing prompt because the date hasn't changed since the last time the prompt was shown"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Stale activity assertion found! %@"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Driver/firmware is busy, retrying (count:%d, err=%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Driver/firmware is busy, stopping retrying (count:%d, err=%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Nondisruptive switch-over complete (all:%d, stillImageCapturePending:%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Nondisruptive switch-over in-progress: %@"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: [%@] Inconsistent nondisruptive switching command ID, metadata ID %d is greater than active ID %d"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Failed to set kFigCaptureStreamProperty_NondisruptiveSwitchingFormatIndex to %@ (err=%d)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: ISP posted '%{public}@' %{public}@"
+ "<<<< BWFigVideoCaptureStream >>>> %s: [%@] Nondisruptive switching format set to %@ with ID:%d, previous %d, isSecondary %d"
+ "<<<< BWGraph >>>> %s: <%p> Called"
+ "<<<< BWGraph >>>> %s: <%p> Created with priority %d"
+ "<<<< BWGraph >>>> %s: <%p> Deallocating"
+ "<<<< BWGraph >>>> %s: <%p> Deferring start for <%p, %@, %{public}@>"
+ "<<<< BWGraph >>>> %s: <%p> Enabling for <%p, %@, %{public}@>"
+ "<<<< BWGraph >>>> %s: <%p> Starting"
+ "<<<< BWGraph >>>> %s: <%p> Starting. Experiments are %@"
+ "<<<< BWGraph >>>> %s: <%p> Stopping"
+ "<<<< BWGraph >>>> %s: <%p> Waiting for source nodes to start"
+ "<<<< BWGraph >>>> %s: <%p> Waiting for start/commit to complete"
+ "<<<< BWGraph >>>> %s: <%p> description: %{public}@"
+ "<<<< BWPhotoEncoderNode >>>> %s: Added aux images into %@ for captureID:%lld: %@ %@ %@%@%@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Frames dropped due to format writer queue being full (slow drive)."
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Setting early termination error code for dropped frame due to slow drive (%d)."
+ "<<<< BWStillImageProcessing >>>> %s: Removing deferred container for %{public}@ due to error %d"
+ "<<<< BWTemporalFilterNode >>>> %s: ConfigurationID %lld is now live for input %@"
+ "<<<< CMIOExtensionFigCaptureStream >>>> Fig"
+ "<<<< FigCaptureClientApplicationStateMonitor >>>> %s: %{public}@ Endowment infos: %@, evaluate layout: %d"
+ "<<<< FigCaptureClientApplicationStateMonitor >>>> %s: %{public}@ Update: %@"
+ "<<<< FigCaptureClientApplicationStateMonitor >>>> %s: %{public}@ mediaEnvironmentBundleID changing from %{public}@ to %{public}@"
+ "<<<< FigCaptureDeferredProcessingEngine >>>> %s: %@ graph: portTypesMatch:%d, pipelineParametersMatch:%d, captureTypesMatch:%d, deferredPhotoFinalDimensionsMatch:%d, containerAndGraphSourceNodeOutputDimensionsMatch:%d, demosaicedRawMatch:%d, demosaicRawRequiresGraphRebuild:%d, ultraHighResolutionCaptureRequiresGraphRebuild:%d, depthDataMatch:%d, portraitRenderingMatch:%d"
+ "<<<< FigCaptureDeferredProcessingEngine >>>> %s: Releasing resources at QoS %{public}@"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
+ "<<<< FigCapturePowerLog >>>> %s: %{public}@: %{public}@"
+ "<<<< FigCapturePowerLog >>>> %s: Camera Streaming Power Events:"
+ "<<<< FigCapturePowerLog >>>> %s: Event #%d: %{public}@"
+ "<<<< FigCapturePowerLog >>>> %s: Failed to serialize state: %@"
+ "<<<< FigCapturePowerLog >>>> %s: Not showing prompt because the build hasn't changed since the last time the prompt was shown."
+ "<<<< FigCapturePowerLog >>>> %s: Not showing prompt because the date hasn't changed since the last time the prompt was shown."
+ "<<<< FigCapturePowerLog >>>> %s: PID: %d, applicationID: %{private}@, uniqueID: %{public}@, streaming: %d, portType: %{public}@"
+ "<<<< FigCapturePowerLog >>>> %s: PLLogRegisteredEvent(camera, %{public}@, ...) (%d)"
+ "<<<< FigCapturePowerLog >>>> %s: Showing TTR prompt..."
+ "<<<< FigCapturePowerLog >>>> %s: sCameraStreamingPowerEventQueue is NULL.  Check FigCaptureCameraStreamingPowerEventInitialize"
+ "<<<< FigCapturePowerLog >>>> %s: sCameraStreamingPowerEventsByPortType is NULL.  Check FigCaptureCameraStreamingPowerEventInitialize"
+ "<<<< FigCaptureSession >>>> %s: %{public}s ClientStartedSession:%d Cam/Audio:%d/%d bg:%d prewarming:%d int:%d multitasking:%d pip:%d devStolen:%d pressured:%d active:%d shouldRun:%d (start:%d stop:%d)"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Configuration: Tearing down graph, capture sources %@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Encountered err (%d) during prewarming"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Error (%d) is fatal. Reset session running state (clientStartedSession, clientRequestedPrewarming, runningForPrewarmedHomeScreenIconResume, sessionShouldRun)"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Error (%d) is not fatal."
+ "<<<< FigCaptureSession >>>> %s: %{public}s Posting notification %{public}@ with payload %{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Stopped running, tearing down graph"
+ "<<<< FigCaptureSession >>>> %s: %{public}s building configuration: %{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s client wants session running %i, and status is %s, nothing to do"
+ "<<<< FigCaptureSession >>>> %s: %{public}s committing configuration: %{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s error (%d) building graph with configuration"
+ "<<<< FigCaptureSession >>>> %s: %{public}s error (%d) updating graph configuration"
+ "<<<< FigCaptureSession >>>> %s: %{public}s failed to commit configuration with error (%d)"
+ "<<<< FigCaptureSession >>>> %s: %{public}s failed to start graph with error (%d)"
+ "<<<< FigCaptureSession >>>> %s: %{public}s got an error (%i) applying configuration %{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s graph <%p> finished starting"
+ "<<<< FigCaptureSession >>>> %s: %{public}s no configuration to commit, we must have coalesced because new configurations came too fast"
+ "<<<< FigCaptureSession >>>> %s: %{public}s stopError: %d"
+ "<<<< FigCaptureSession >>>> %s: %{public}s translated error (%d) to (%d)"
+ "<<<< FigCaptureSession >>>> %s: (stopError: %d), sessionShouldRun: %d, sessionStatus: %s, sessionShouldStop: %d"
+ "<<<< FigCaptureSession >>>> %s: Creating session for PID %d"
+ "<<<< FigCaptureSession >>>> %s: Media environments may only be specified by processes with the com.apple.developer.web-browser-engine.rendering entitlement"
+ "<<<< FigCaptureSession >>>> %s: Media environments must be specified by processes with the com.apple.developer.web-browser-engine.rendering entitlement"
+ "<<<< FigCaptureSession >>>> %s: sessionShouldRun: %d, sessionStatus: %s, sessionShouldStart: %d, sessionInterruptionError: %d, startingSessionForPrewarming: %d"
+ "<<<< FigCaptureSource >>>> %s: Already gave gestures-disabled user guidance for %@"
+ "<<<< FigCaptureSource >>>> %s: Called (%p) position (%d)"
+ "<<<< FigCaptureSource >>>> %s: Could not locate record for %@: %@"
+ "<<<< FigCaptureSource >>>> %s: Registered %p for device notifications"
+ "<<<< FigCaptureSource >>>> %s: Unregistered %p from device notifications"
+ "<<<< FigCaptureSource >>>> %s: showReactionsTip indicates gestures-disabled user guidance %s given for %@ (name %@)"
+ "<<<< FigCaptureUtilities >>>> %s: Prompt opening Tap-to-Radar: %@"
+ "<<<< FigCaptureUtilities >>>> %s: Response Flags: %ld"
+ "@\"RBSProcessMonitor\""
+ "@116@0:8@16@24@32@40B48@52{?=[8I]}60@92@100^i108"
+ "@120@0:8@16@24@32@40@48@56{?=[8I]}64@96@104^i112"
+ "@140@0:8@16@24@32@40B48@52{?=[8I]}60@92@100@108^?116@124^i132"
+ "@156@0:8{?=ii}16@24i32i36B40B44@48i56@60@68{?=BB{CGRect={CGPoint=dd}{CGSize=dd}}ifffd}76B140B144Q148"
+ "@28@0:8f16q20"
+ "@32@0:8{?=ii}16q24"
+ "@68@0:8{?=[8I]}16@48B56@?60"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "AttachedMediaNotFound"
+ "BOOL soft_showReactionsTip(NSString *, NSString *)"
+ "BWTemporalFilterNode"
+ "CMIOExtensionFigCaptureStream.m"
+ "Camera Streaming Power Events"
+ "CaptureDeviceStolenDuringLaunch"
+ "Class getSTAttributedEntityClass(void)_block_invoke"
+ "Class getSTExecutableIdentityClass(void)_block_invoke"
+ "ClientPriority"
+ "Encode Only"
+ "FigCaptureLogCameraStreamingPowerEvent"
+ "FigCapturePowerLogMissingCameraStopEventObserver"
+ "FigCapturePromptOpenTapToRadar"
+ "FigCapturePromptOpenTapToRadar_block_invoke"
+ "FigCaptureSessionCreateMsgParam_MediaEnvironment"
+ "Front Ultra Wide Metadata Camera"
+ "FrontCameraRotationForISP"
+ "Internal inconsistency, scalerCropRect %@ is out of bounds {%d,%d}"
+ "LastShownMissingCameraStopPowerEventTTRPromptBuildVersion"
+ "LastShownMissingCameraStopPowerEventTTRPromptDate"
+ "MCTFMode"
+ "Missing camera stop power event!"
+ "Missing camera stop power event. Please file a radar."
+ "Not re-using"
+ "PrimaryScalerLowRes"
+ "Propagate And Encode"
+ "Propagate Only"
+ "Reusing"
+ "STAttributedEntity"
+ "STExecutableIdentity"
+ "SceneClassificationActive"
+ "SceneClassificationConfidences"
+ "SceneClassificationConfidencesChanged"
+ "SensorCenterOffsetX"
+ "SensorCenterOffsetY"
+ "SmartCameraEnabledChanged"
+ "SuperWideMetadata"
+ "T@\"CMIExternalMemoryResource\",?,&,N"
+ "T@\"FigCaptureDisplayLayout\",R,N"
+ "T@\"NSDictionary\",C,N,V_inputSampleBufferAttachments"
+ "T@\"NSObject<OS_tcc_identity>\",&,N,V_mediaEnvironmentTCCIdentity"
+ "T@\"NSObject<OS_tcc_identity>\",R,N"
+ "T@\"NSString\",&,N,V_mediaEnvironmentBundleID"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,&,N,V_mediaEnvironment"
+ "T@\"NSString\",R,N,V_mediaEnvironment"
+ "T@?,N"
+ "TB,?,R,N"
+ "TB,N,GisPaymentServiceVisible,V_paymentServiceVisible"
+ "TB,N,V_active"
+ "TB,N,V_awbStable"
+ "TB,N,V_deviceIsLocked"
+ "TB,N,V_faceTrackingUseRecognition"
+ "TB,N,V_isColdLaunch"
+ "TB,N,V_streamingSessionAnalyticsHighlightRecoveryEnabled"
+ "TB,R,N,V_allowsAsyncPropagation"
+ "TI,N,V_depthAFStatus"
+ "TI,N,V_orientationFaceDownTime"
+ "TI,N,V_orientationFaceUpTime"
+ "TI,N,V_streamingSessionAnalyticsPixelFormat"
+ "TemporalFilterSessionFailure"
+ "Tf,N,V_fieldOfView"
+ "Tf,N,V_lensTemperature"
+ "Tf,N,V_maximumFrameRate"
+ "Tf,N,V_minimumFrameRate"
+ "Ti,N,V_completedNondisruptiveSwitchingCommandID"
+ "Ti,N,V_deviceStolenCondition"
+ "Ti,N,V_deviceStolenDuration"
+ "Ti,N,V_faceTrackingNumTrackedFaces"
+ "Ti,N,V_stillImageGDCSourceMode"
+ "Ti,R,N,V_currentOrientation"
+ "Ti,R,N,V_mostRecentPortraitLandscapeOrientation"
+ "Tq,N,V_propagationMode"
+ "T{?=ii},N,V_streamingSessionAnalyticsVideoDimensions"
+ "T{?=ii},N,V_videoDimensions"
+ "T{?=ii},R,N,V_dimensions"
+ "T{CGPoint=dd},N,V_gdcInDCProcessorInputCropOffset"
+ "T{CGPoint=dd},N,V_geometricDistortionCorrectionInputCropOffset"
+ "T{CGPoint=dd},N,V_sensorCenterOffset"
+ "T{CGPoint=dd},R,V_sensorCenterOffset"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_regionOfInterestForCameraControls"
+ "[16{BWStreamOutputStorage=\"type\"i\"flags\"I\"ready\"B\"enabled\"B\"nodeOutput\"@\"BWNodeOutput\"\"simpleQueue\"^{opaqueCMSimpleQueue}\"bufferServicingQueue\"@\"NSObject<OS_dispatch_queue>\"\"bufferServicingQueueCallback\"^?\"cachedFormatDescription\"^{opaqueCMFormatDescription}\"lastEmittedPTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"retainedBufferCount\"i\"streamRetainedBufferCount\"i\"internalPixelBufferPool\"@\"BWPixelBufferPool\"\"bufferPoolOwnedByAnotherNode\"B\"bytesPerRowAlignmentRequirement\"i\"planeAlignmentRequirement\"i\"sensorInterfaceRawPixelFormat\"I\"sashimiRawPixelFormat\"I\"sushiRawPixelFormat\"I\"outputDimensions\"{?=\"width\"i\"height\"i}\"cropRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"lastISPAppliedZoomFactor\"f\"ioSurfaceCompressionRatioStats\"@\"BWStats\"\"pixelBufferCompressionType\"i\"totalCompressedDataSize\"Q\"totalUncompressedDataSize\"Q\"lumaCompressionHistogram\"[16Q]\"chromaCompressionHistogram\"[16Q]\"universalCompressionNumberOfSamples\"I\"lastUniversalCompressionSamplePTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"pixelFormatIsTenBit\"B\"pixelFormatIs420\"B\"pixelFormatIsLossyCompression\"B\"prefetchEnabled\"B}]"
+ "[21I]"
+ "[propertyValue isKindOfClass:[NSDictionary class]]"
+ "^{OpaqueVTTemporalFilterSession=}"
+ "_FigIsNotCurrentDispatchQueue( _monitorQueue )"
+ "_allowsAsyncPropagation"
+ "_cameraAppStreamingTimer"
+ "_completedNondisruptiveSwitchingCommandID"
+ "_depthAFStatus"
+ "_deviceStolenCondition"
+ "_deviceStolenDuration"
+ "_dumpInputVideo"
+ "_dumpOutputVideo"
+ "_emitsDroppedSampleForMissingAttachedMedia"
+ "_eventDateFormatter"
+ "_faceTrackingNumTrackedFaces"
+ "_faceTrackingUseRecognition"
+ "_fieldOfView"
+ "_firstValidFrameSeen"
+ "_gdcInDCProcessorInputCropOffset"
+ "_geometricDistortionCorrectionInputCropOffset"
+ "_initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:"
+ "_inputSampleBufferAttachments"
+ "_inputSampleBufferQueue"
+ "_inputSampleBufferQueueLock"
+ "_isColdLaunch"
+ "_ispFaceTrackingNetworkFailureThresholdMultiplier"
+ "_ispFaceTrackingNumTrackedFaces"
+ "_ispFaceTrackingUseRecognition"
+ "_lensTemperature"
+ "_mctfSession"
+ "_mediaEndowmentMonitor"
+ "_mediaEnvironment"
+ "_mediaEnvironmentBundleID"
+ "_mediaEnvironmentTCCIdentity"
+ "_observerQueue"
+ "_orientationFaceDownTime"
+ "_orientationFaceDownTotalTime"
+ "_orientationFaceUpTime"
+ "_orientationFaceUpTotalTime"
+ "_outputsDiscardsSampleBuffer"
+ "_paymentServiceVisible"
+ "_pipelineType"
+ "_previousLayoutHasForegroundCameraApp"
+ "_propagationMode"
+ "_regionOfInterestForCameraControlsChangedHandler"
+ "_sensorCenterOffset"
+ "_stillImageCaptureNowBusyCount"
+ "_stillImageGDCSourceMode"
+ "_streamingSessionAnalyticsHighlightRecoveryEnabled"
+ "_streamingSessionAnalyticsPixelFormat"
+ "_streamingSessionAnalyticsVideoDimensions"
+ "_subjectSelectionEnabled"
+ "_temporalFilterEnabled"
+ "_videoCaptureSplitterNode"
+ "active"
+ "addCustomMetadataContents:URI:name:"
+ "bwtemporalfilternode_trace"
+ "captureSession_beginDeferredGraphSetupAndWaitForCameraSourcesToStart"
+ "captureSession_buildGraphWithConfiguration"
+ "captureSession_didStopRunning"
+ "captureSession_postNotificationWithPayload_block_invoke"
+ "captureSession_resetSessionRunningStateOnFatalError"
+ "captureSession_startGraph"
+ "captureSession_stopGraph"
+ "captureSession_stopRunningInternal"
+ "captureSession_teardownGraph"
+ "captureSession_updateGraphConfiguration"
+ "captureSession_willStartRunning"
+ "captureSource_Finalize"
+ "captureSource_registerDeviceNotificationListeners"
+ "captureSource_unregisterDeviceNotificationListeners"
+ "capturepowerlog_trace"
+ "captureutilities_trace"
+ "com.apple.Music"
+ "com.apple.ProximityReaderSceneUI"
+ "com.apple.avfoundation.avcapturedevice.private.built-in_metadata:3"
+ "com.apple.coremedia.camera.DeferredPhotoCapture"
+ "com.apple.coremedia.camera.PhotoCapture"
+ "com.apple.developer.web-browser-engine.rendering"
+ "com.apple.mediaexperience.session-Media"
+ "com.apple.private.avfoundation.capture.temporary.no-media-environment.allow"
+ "com.apple.videotoolbox.temporalfilter.mctf"
+ "com.apple.web-browser-engine.gpu"
+ "com.apple.web-browser-engine.rendering"
+ "completedNondisruptiveSwitchingCommandID"
+ "cpls_logCameraStreamingPowerEvents"
+ "cpls_osStateData"
+ "cs_getBackingsForBuiltInAndExternalCameras"
+ "cs_handleRequestGesturesDefaultDisabledNotificationSignal"
+ "currentOrientation"
+ "depth:%d"
+ "depthAFStatus"
+ "description=CameraCapture-475.31.1"
+ "deviceIsLocked"
+ "deviceStolenCondition"
+ "deviceStolenDuration"
+ "emitsDroppedSampleForMissingAttachedMedia"
+ "endowment"
+ "endowmentInfoForHandle"
+ "endowmentInfos"
+ "endowmentNamespace"
+ "environment"
+ "faceTrackingNumTrackedFaces"
+ "faceTrackingUseRecognition"
+ "gainMap:%d"
+ "gdcInDCProcessorInputCropOffset"
+ "gdcInDCProcessorInputCropOffsetX"
+ "gdcInDCProcessorInputCropOffsetY"
+ "geometricDistortionCorrectionInputCropOffset"
+ "hasActiveForClientAssertion"
+ "i40@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32"
+ "initWithAttributedEntity:activeEntity:"
+ "initWithAuditToken:"
+ "initWithAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:"
+ "initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:"
+ "initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:mediaEnvironment:error:"
+ "initWithClientAuditToken:mediaEnvironment:forThirdPartyTorch:applicationAndLayoutStateHandler:"
+ "initWithConfiguration:sourcePreviewOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:"
+ "initWithDimensions:propagationMode:"
+ "initWithExecutableIdentity:"
+ "initWithExecutableIdentity:website:"
+ "initWithMainImageDownscalingFactor:propagationMode:"
+ "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:pipelineType:"
+ "inputSampleBufferAttachments"
+ "isColdLaunch"
+ "isPaymentServiceVisible"
+ "lensTemperature"
+ "mediaEnvironment"
+ "mediaEnvironmentBundleID"
+ "mediaEnvironmentTCCIdentity"
+ "metalPreviewDispatchQueue"
+ "netLaunchDuration"
+ "orientationFaceDownTime"
+ "orientationFaceUpTime"
+ "outputID"
+ "paymentService: 1"
+ "paymentServiceVisible"
+ "personMask:%d"
+ "propagationMode"
+ "regionOfInterestForCameraControls"
+ "regionOfInterestForCameraControlsChangedHandler"
+ "requiresEncoding"
+ "sceneClassificationConfidences"
+ "sensorCenterOffset"
+ "setActive:"
+ "setAwbStable:"
+ "setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:"
+ "setCompletedNondisruptiveSwitchingCommandID:"
+ "setDepthAFStatus:"
+ "setDeviceIsLocked:"
+ "setDeviceStolenCondition:"
+ "setDeviceStolenDuration:"
+ "setDeviceToCameraSpaceTransform:"
+ "setDiscardsSampleBuffer:forOutputIndex:"
+ "setEmitsDroppedSampleForMissingAttachedMedia:"
+ "setFaceTrackingNumTrackedFaces:"
+ "setFaceTrackingUseRecognition:"
+ "setFieldOfView:"
+ "setGdcInDCProcessorInputCropOffset:"
+ "setGeometricDistortionCorrectionInputCropOffset:"
+ "setInputSampleBufferAttachments:"
+ "setIsColdLaunch:"
+ "setLensTemperature:"
+ "setMediaEnvironmentBundleID:"
+ "setMediaEnvironmentTCCIdentity:"
+ "setOrientationFaceDownTime:"
+ "setOrientationFaceUpTime:"
+ "setPaymentServiceVisible:"
+ "setPropagationMode:"
+ "setRegionOfInterestForCameraControlsChangedHandler:"
+ "setSensorCenterOffset:"
+ "setStillImageGDCSourceMode:"
+ "setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:"
+ "setStreamingSessionAnalyticsHighlightRecoveryEnabled:"
+ "setStreamingSessionAnalyticsPixelFormat:"
+ "setStreamingSessionAnalyticsVideoDimensions:"
+ "setVideoDimensions:"
+ "showReactionsTip"
+ "signal/*/request-gestures-default-disabled-notification"
+ "softlink:r:path:/System/Library/Frameworks/ReplayKit.framework/ReplayKit"
+ "stream && configs"
+ "stream->stillImageConfig.enabled"
+ "stream->stillImageConfig.pixelBufferHandler"
+ "stream->streaming"
+ "streamingSessionAnalyticsHighlightRecoveryEnabled"
+ "streamingSessionAnalyticsPixelFormat"
+ "streamingSessionAnalyticsVideoDimensions"
+ "superwidemetadata"
+ "v80@0:8B16i20{?=[8I]}24@56@64@?72"
+ "v88@0:8B16i20@24{?=[8I]}32@64@72@?80"
+ "videoDimensions"
+ "videoDimensionsHeight"
+ "videoDimensionsWidth"
+ "videoeffects/%@/did-show-gestures-default-disabled-notification"
+ "void *ReplayKitLibrary(void)"
+ "warpCGRect:fromCamera:toCamera:"
+ "was"
+ "was not"
+ "with no payload"
+ "with payload %@"
- "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d O:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@"
- "( ! FigCFEqual( _captureStream.portType, kFigCapturePortType_FrontFacingInfraredCamera ) ) || _deviceType == BWCaptureDeviceTypeInfraredMetadataCamera"
- "( outputIndex > -1 ) && ( outputIndex < ( BWStreamOutputIndexSemanticMasks + 1 ) )"
- "((! deviceCheck ) || ( device && device == storage->capdev ))"
- "-[BWCameraStreamingMonitor _informInternalFrameworksFromSetStreaming:deviceType:clientAuditToken:tccIdentity:]"
- "-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]"
- "-[BWGraph start:]_block_invoke_2"
- "<%@ %p>: %@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming ON message to MediaSafetyNet"
- "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming ON message to SystemStatus"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Nondisruptive switch-over complete (all:%d, preventingStillImageCapture:%d, stillImageCapturePending:%d)"
- "<<<< BWFigVideoCaptureStream >>>> %s: ISP posted '%@' with payload '%@'"
- "<<<< BWGraph >>>> %s: Experiments are disabled"
- "<<<< BWPhotoEncoderNode >>>> %s: Added aux images into %@ for captureID:%lld: depth:%d personMask:%d gainMap:%d"
- "<<<< FigCaptureDeferredPhotoProcessor >>>> %s: SKIPPING PREWARMING -- unsupported by this platform or disabled by defaults write"
- "<<<< FigCaptureDeferredProcessingEngine >>>> %s: Releasing resources"
- "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
- "<<<< FigCaptureSession >>>> %s: %{public}s ClientStartedSession:%d Cam/Audio:%d/%d bg:%d prewarming:%d int:%d multitasking:%d pip:%d devStolen:%d pressured:%d active:%d shouldRun:%d start:%d stop:%d"
- "<<<< FigCaptureSession >>>> %s: %{public}s Encountered err %d during prewarming"
- "<<<< FigCaptureSession >>>> %s: %{public}s committing configuration %{public}@"
- "@108@0:8@16@24@32@40B48@52{?=[8I]}60@92^i100"
- "@112@0:8@16@24@32@40@48@56{?=[8I]}64@96^i104"
- "@132@0:8@16@24@32@40B48@52{?=[8I]}60@92@100^?108@116^i124"
- "@148@0:8{?=ii}16@24i32i36B40B44@48i56@60@68{?=BB{CGRect={CGPoint=dd}{CGSize=dd}}ifffd}76B140B144"
- "@24@0:8f16B20"
- "@60@0:8{?=[8I]}16B48@?52"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "DeferredPhotoCapture"
- "DeferredPhotoError"
- "Manifest exceeds allowed file size"
- "Manifest exceeds permitted size"
- "PhotoCapture"
- "PhotoError"
- "TB,N,GisContactlessUIServiceVisible,V_contactlessUIServiceVisible"
- "TB,N,V_deliverAsCameraAppSpecificEvent"
- "TB,N,V_smartCameraEnabled"
- "TB,R,N,V_propagatesDownstream"
- "TI,R,N,V_mostRecentPortraitLandscapeOrientation"
- "Ti,N,V_streamingTime"
- "Value of kFigCaptureStreamMetadata_AutoFocusRecommendedMasterPortType is not a constant"
- "[12{BWStreamOutputStorage=\"type\"i\"flags\"I\"ready\"B\"enabled\"B\"nodeOutput\"@\"BWNodeOutput\"\"simpleQueue\"^{opaqueCMSimpleQueue}\"bufferServicingQueue\"@\"NSObject<OS_dispatch_queue>\"\"bufferServicingQueueCallback\"^?\"cachedFormatDescription\"^{opaqueCMFormatDescription}\"lastEmittedPTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"retainedBufferCount\"i\"streamRetainedBufferCount\"i\"internalPixelBufferPool\"@\"BWPixelBufferPool\"\"bufferPoolOwnedByAnotherNode\"B\"bytesPerRowAlignmentRequirement\"i\"planeAlignmentRequirement\"i\"sensorInterfaceRawPixelFormat\"I\"sashimiRawPixelFormat\"I\"sushiRawPixelFormat\"I\"outputDimensions\"{?=\"width\"i\"height\"i}\"cropRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"lastISPAppliedZoomFactor\"f\"ioSurfaceCompressionRatioStats\"@\"BWStats\"\"pixelBufferCompressionType\"i\"totalCompressedDataSize\"Q\"totalUncompressedDataSize\"Q\"lumaCompressionHistogram\"[16Q]\"chromaCompressionHistogram\"[16Q]\"universalCompressionNumberOfSamples\"I\"lastUniversalCompressionSamplePTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"pixelFormatIsTenBit\"B\"pixelFormatIs420\"B\"pixelFormatIsLossyCompression\"B\"prefetchEnabled\"B}]"
- "[20I]"
- "[requestedSettingsObj isKindOfClass:[FigCaptureStillImageSettings class]]"
- "_contactlessUIServiceVisible"
- "_deliverAsCameraAppSpecificEvent"
- "_initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:deviceVendor:createAutofocusSampleBufferProcessorFunction:cameraParameters:error:"
- "_nonDisruptiveSwitchOverPreventingStillImageCaptureInProgress"
- "_propagatesDownstream"
- "_variableFrameRateMostRecentInferenceResult"
- "camera"
- "cameraApp"
- "com.apple.coremedia.%@.%@"
- "contactlessUI: 1"
- "contactlessUIServiceVisible"
- "csu_getBackings"
- "deliverAsCameraAppSpecificEvent"
- "description=CameraCapture-472.1.2"
- "initWithAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:"
- "initWithCaptureDevice:attributes:synchronizedStreamsAttributes:unsynchronizedStreamsAttributes:multiCamEnabled:applicationID:clientAuditToken:tccIdentity:error:"
- "initWithCaptureStream:parentDevice:attributes:sensorIDDictionary:synchronizedStreamsGroup:applicationID:clientAuditToken:tccIdentity:error:"
- "initWithClientAuditToken:forThirdPartyTorch:applicationAndLayoutStateHandler:"
- "initWithConfiguration:sourcePreviewOutput:sourceSemanticMasksOutput:imageQueueSinkNode:graph:name:inferenceScheduler:captureDevice:previewTapDelegate:zoomPIPOverlayDelegate:"
- "initWithMainImageDownscalingFactor:propagatesDownstream:"
- "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:deviceModelName:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:"
- "isContactlessUIServiceVisible"
- "manifestFileSize <= manifestFileSizeMax"
- "requestedSettingsObj"
- "setCameraAccess:deviceType:clientAuditToken:tccIdentity:completionHandler:"
- "setContactlessUIServiceVisible:"
- "setDeliverAsCameraAppSpecificEvent:"
- "setStreaming:deviceType:streamUniqueID:clientAuditToken:tccIdentity:completionHandler:"
- "v72@0:8B16i20{?=[8I]}24@56@?64"
- "v80@0:8B16i20@24{?=[8I]}32@64@?72"
- "waitForNotificationBarrier"

```
