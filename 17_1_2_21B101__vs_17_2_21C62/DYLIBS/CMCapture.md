## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-465.15.2.0.0
-  __TEXT.__text: 0x4463d8
-  __TEXT.__auth_stubs: 0x4970
-  __TEXT.__objc_methlist: 0x2536c
-  __TEXT.__const: 0x150098
-  __TEXT.__cstring: 0x618bb
-  __TEXT.__oslogstring: 0x18189
-  __TEXT.__gcc_except_tab: 0x1e38
+470.16.1.0.0
+  __TEXT.__text: 0x44f100
+  __TEXT.__auth_stubs: 0x49c0
+  __TEXT.__objc_methlist: 0x25934
+  __TEXT.__const: 0x1500b8
+  __TEXT.__cstring: 0x62be7
+  __TEXT.__oslogstring: 0x1856b
+  __TEXT.__gcc_except_tab: 0x1e50
   __TEXT.__dlopen_cstrs: 0x53f
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x9fd0
-  __TEXT.__objc_classname: 0x6a4a
-  __TEXT.__objc_methname: 0x7cde7
-  __TEXT.__objc_methtype: 0x1161a
-  __TEXT.__objc_stubs: 0x37320
-  __DATA_CONST.__got: 0x4508
-  __DATA_CONST.__const: 0x8670
-  __DATA_CONST.__objc_classlist: 0x1698
+  __TEXT.__unwind_info: 0xa0b4
+  __TEXT.__objc_classname: 0x6aef
+  __TEXT.__objc_methname: 0x7e227
+  __TEXT.__objc_methtype: 0x116a6
+  __TEXT.__objc_stubs: 0x379c0
+  __DATA_CONST.__got: 0x45b8
+  __DATA_CONST.__const: 0x8748
+  __DATA_CONST.__objc_classlist: 0x16c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x62dd8
-  __DATA_CONST.__objc_selrefs: 0xfc10
-  __DATA_CONST.__objc_arraydata: 0x3208
-  __AUTH_CONST.__objc_const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x2fba0
-  __AUTH_CONST.__objc_intobj: 0x4350
-  __AUTH_CONST.__objc_arrayobj: 0x22b0
-  __AUTH_CONST.__const: 0x1170
-  __AUTH_CONST.__auth_ptr: 0xc0
+  __DATA_CONST.__objc_const: 0x63cc8
+  __DATA_CONST.__objc_selrefs: 0xfe20
+  __DATA_CONST.__objc_arraydata: 0x3218
+  __AUTH_CONST.__objc_const: 0x8b8
+  __AUTH_CONST.__cfstring: 0x304a0
+  __AUTH_CONST.__objc_intobj: 0x4368
+  __AUTH_CONST.__objc_arrayobj: 0x22c8
+  __AUTH_CONST.__const: 0x11f0
+  __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0x960
-  __AUTH_CONST.__auth_got: 0x24c8
-  __AUTH.__objc_data: 0x550
+  __AUTH_CONST.__auth_got: 0x24f0
+  __AUTH.__objc_data: 0x6e0
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1940
-  __DATA.__objc_superrefs: 0x1538
-  __DATA.__objc_ivar: 0x81c4
+  __DATA.__objc_classrefs: 0x1960
+  __DATA.__objc_superrefs: 0x1560
+  __DATA.__objc_ivar: 0x8318
   __DATA.__data: 0x4a10
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x2c0
-  __DATA.__bss: 0x1008
+  __DATA.__common: 0x2e0
+  __DATA.__bss: 0x1028
   __DATA_DIRTY.__const: 0x22c0
   __DATA_DIRTY.__objc_const: 0x134f8
   __DATA_DIRTY.__objc_data: 0xdca0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 18155
-  Symbols:   65107
-  CStrings:  31457
+  Functions: 18309
+  Symbols:   65640
+  CStrings:  31759
 
Symbols:
+ +[BWMultiCamConfiguration configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:stereoVideoCaptureEnabled:]
+ +[BWNodeError newError:sourceNode:stillImageSettings:metadata:]
+ +[BWStereoVideoCaptureSceneMonitor initialize]
+ +[BWStereoVideoMetadataNode initialize]
+ -[BWCameraAppLaunchAnalyticsPayload ispStartDuration]
+ -[BWCameraAppLaunchAnalyticsPayload numberOfGraphStartsDuringLaunch]
+ -[BWCameraAppLaunchAnalyticsPayload setIspStartDuration:]
+ -[BWCameraAppLaunchAnalyticsPayload setNumberOfGraphStartsDuringLaunch:]
+ -[BWDeepFusionProcessorInput beginProcessingCachedBuffersIfWaiting]
+ -[BWFigCaptureDeviceVendor _logISPStartupTimeToCoreAnalytics]
+ -[BWFigCaptureDeviceVendor createDeviceTime]
+ -[BWFigVideoCaptureDevice _depthDataDeliveryConfigureActiveSlaveStreamForMasterStream:]
+ -[BWFigVideoCaptureDevice _serviceStereoVideoCaptureSceneMonitoringWithFrameStatisticsByPortType:]
+ -[BWFigVideoCaptureDevice _updateSceneMonitorFocusStateForAutofocusProperty:propertyValue:]
+ -[BWFigVideoCaptureDevice _updateStereoVideoCaptureStatus:]
+ -[BWFigVideoCaptureDevice setStereoVideoCaptureEnabled:]
+ -[BWFigVideoCaptureDevice stereoVideoCaptureEnabled]
+ -[BWFigVideoCaptureDevice stereoVideoCaptureStatus]
+ -[BWIrisMovieInfo irisSequenceAdjusterRecipeIdentifier]
+ -[BWIrisMovieInfo maxSystemPressureLevel]
+ -[BWIrisMovieInfo numberOfFramesDropped]
+ -[BWIrisMovieInfo setIrisSequenceAdjusterRecipeIdentifier:]
+ -[BWIrisMovieInfo setMaxSystemPressureLevel:]
+ -[BWIrisMovieInfo setNumberOfFramesDropped:]
+ -[BWIrisMovieInfo setStillImageCaptureLuxLevel:]
+ -[BWIrisMovieInfo setTargetFrameRate:]
+ -[BWIrisMovieInfo setVideoFrameDurationStats:]
+ -[BWIrisMovieInfo stillImageCaptureLuxLevel]
+ -[BWIrisMovieInfo targetFrameRate]
+ -[BWIrisMovieInfo videoFrameDurationStats]
+ -[BWIrisSequenceAdjuster previewFrameDuration]
+ -[BWLivePhotoMovieAnalyticsPayload averageVideoFrameDurationInMilliseconds]
+ -[BWLivePhotoMovieAnalyticsPayload maxSystemPressureLevel]
+ -[BWLivePhotoMovieAnalyticsPayload maxVideoFrameDurationInMilliseconds]
+ -[BWLivePhotoMovieAnalyticsPayload medianVideoFrameDurationInMilliseconds]
+ -[BWLivePhotoMovieAnalyticsPayload minVideoFrameDurationInMilliseconds]
+ -[BWLivePhotoMovieAnalyticsPayload numberOfFramesDropped]
+ -[BWLivePhotoMovieAnalyticsPayload retimingRecipeIdentifier]
+ -[BWLivePhotoMovieAnalyticsPayload setAverageVideoFrameDurationInMilliseconds:]
+ -[BWLivePhotoMovieAnalyticsPayload setMaxSystemPressureLevel:]
+ -[BWLivePhotoMovieAnalyticsPayload setMaxVideoFrameDurationInMilliseconds:]
+ -[BWLivePhotoMovieAnalyticsPayload setMedianVideoFrameDurationInMilliseconds:]
+ -[BWLivePhotoMovieAnalyticsPayload setMinVideoFrameDurationInMilliseconds:]
+ -[BWLivePhotoMovieAnalyticsPayload setNumberOfFramesDropped:]
+ -[BWLivePhotoMovieAnalyticsPayload setRetimingRecipeIdentifier:]
+ -[BWLivePhotoMovieAnalyticsPayload setStillCaptureLuxLevel:]
+ -[BWLivePhotoMovieAnalyticsPayload setStillCapturePortType:]
+ -[BWLivePhotoMovieAnalyticsPayload setStillCaptureResolutionFlavor:]
+ -[BWLivePhotoMovieAnalyticsPayload setStillCaptureType:]
+ -[BWLivePhotoMovieAnalyticsPayload setTargetFrameRate:]
+ -[BWLivePhotoMovieAnalyticsPayload setVideoFrameDurationStandardDeviationInMilliseconds:]
+ -[BWLivePhotoMovieAnalyticsPayload stillCaptureLuxLevel]
+ -[BWLivePhotoMovieAnalyticsPayload stillCapturePortType]
+ -[BWLivePhotoMovieAnalyticsPayload stillCaptureResolutionFlavor]
+ -[BWLivePhotoMovieAnalyticsPayload stillCaptureType]
+ -[BWLivePhotoMovieAnalyticsPayload targetFrameRate]
+ -[BWLivePhotoMovieAnalyticsPayload videoFrameDurationStandardDeviationInMilliseconds]
+ -[BWMovieFileOutputAnalyticsPayload setStereoVideoCaptureEnabled:]
+ -[BWMovieFileOutputAnalyticsPayload setStereoVideoCaptureStatus:]
+ -[BWMovieFileOutputAnalyticsPayload stereoVideoCaptureEnabled]
+ -[BWMovieFileOutputAnalyticsPayload stereoVideoCaptureStatus]
+ -[BWMultiCamConfiguration _initWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:withCaptureDevice:readCurrentStateFromCaptureDevice:stereoVideoCaptureEnabled:]
+ -[BWMultiCamConfiguration sortedStreamsForTNRFeatureBasedRegistration:prioritizePrimaryStream:]
+ -[BWNodeError _initWithError:sourceNode:stillImageSettings:recordingSettings:metadata:]
+ -[BWNodeError metadata]
+ -[BWPhotonicEngineNode _emitError:stillImageSettings:metadata:description:]
+ -[BWPortraitAutoSuggest perFrameObjectValidity:originalFrameWidth:originalFrameHeight:frameWidth:frameHeight:finalCropRect:]
+ -[BWPortraitAutoSuggest processSbuf:]
+ -[BWPortraitAutoSuggest runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:]
+ -[BWQuickTimeMovieFileSinkNode _addStereoMovieLevelMetadataToSettingsMovieLevelMetadata:]
+ -[BWQuickTimeMovieFileSinkNode _handleSpatialAggressorsSeenMarkerBuffer:]
+ -[BWQuickTimeMovieFileSinkNode _initAnalyticsDataInIrisMovieInfo:]
+ -[BWQuickTimeMovieFileSinkNode setStereoVideoCaptureEnabled:]
+ -[BWQuickTimeMovieFileSinkNode stereoVideoCaptureEnabled]
+ -[BWStats initWithMedianCalculationEnabled:maxNumberOfSamplesForMedianCalculation:]
+ -[BWStats median]
+ -[BWStats nextDataPointIndex]
+ -[BWStats setNextDataPointIndex:]
+ -[BWStereoFusionNode _handleError:forSampleBuffer:input:metadata:]
+ -[BWStereoVideoCaptureAnalyticsPayload cameraPosture]
+ -[BWStereoVideoCaptureAnalyticsPayload eventDictionary]
+ -[BWStereoVideoCaptureAnalyticsPayload eventName]
+ -[BWStereoVideoCaptureAnalyticsPayload init]
+ -[BWStereoVideoCaptureAnalyticsPayload percentageOfFramesWithAggressiveFocusDistance]
+ -[BWStereoVideoCaptureAnalyticsPayload percentageOfFramesWithAggressiveLuxLevel]
+ -[BWStereoVideoCaptureAnalyticsPayload reset]
+ -[BWStereoVideoCaptureAnalyticsPayload setCameraPosture:]
+ -[BWStereoVideoCaptureAnalyticsPayload setPercentageOfFramesWithAggressiveFocusDistance:]
+ -[BWStereoVideoCaptureAnalyticsPayload setPercentageOfFramesWithAggressiveLuxLevel:]
+ -[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureDuration:]
+ -[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureEnabled:]
+ -[BWStereoVideoCaptureAnalyticsPayload setStereoVideoCaptureStatus:]
+ -[BWStereoVideoCaptureAnalyticsPayload setVideoOrientation:]
+ -[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureDuration]
+ -[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureEnabled]
+ -[BWStereoVideoCaptureAnalyticsPayload stereoVideoCaptureStatus]
+ -[BWStereoVideoCaptureAnalyticsPayload videoOrientation]
+ -[BWStereoVideoCaptureSceneMonitor dealloc]
+ -[BWStereoVideoCaptureSceneMonitor focusScanDidComplete]
+ -[BWStereoVideoCaptureSceneMonitor initWithTuningParametersByPortType:attachDebugFrameStatistics:]
+ -[BWStereoVideoCaptureSceneMonitor resolveStereoVideoCaptureStatusWithFrameStatistics:stereoVideoCaptureStatusOut:]
+ -[BWStereoVideoCaptureSceneMonitor setAutoFocusInProgress:focusLocked:oneShotFocusScanInProgress:]
+ -[BWStereoVideoMetadataNode _sendSpatialAggressorsSeenMarkerBufferForPTS:measuredDuration:]
+ -[BWStereoVideoMetadataNode dealloc]
+ -[BWStereoVideoMetadataNode didReachEndOfDataForInput:]
+ -[BWStereoVideoMetadataNode didSelectFormat:forInput:]
+ -[BWStereoVideoMetadataNode initWithPorts:secondaryPort:cameraInfoByPortType:]
+ -[BWStereoVideoMetadataNode nodeSubType]
+ -[BWStereoVideoMetadataNode nodeType]
+ -[BWStereoVideoMetadataNode renderSampleBuffer:forInput:]
+ -[BWStillImageAnalyticsPayloadCommon SNR]
+ -[BWStillImageAnalyticsPayloadCommon accelStandardDeviation]
+ -[BWStillImageAnalyticsPayloadCommon activeDeviceMask]
+ -[BWStillImageAnalyticsPayloadCommon afDriverShortOccurred]
+ -[BWStillImageAnalyticsPayloadCommon afPowerConsumption]
+ -[BWStillImageAnalyticsPayloadCommon alsLuxLevel]
+ -[BWStillImageAnalyticsPayloadCommon alsRearLuxLevel]
+ -[BWStillImageAnalyticsPayloadCommon apsMode]
+ -[BWStillImageAnalyticsPayloadCommon apsSubjectDistance]
+ -[BWStillImageAnalyticsPayloadCommon binned]
+ -[BWStillImageAnalyticsPayloadCommon burst]
+ -[BWStillImageAnalyticsPayloadCommon cameraPosture]
+ -[BWStillImageAnalyticsPayloadCommon captureFlags]
+ -[BWStillImageAnalyticsPayloadCommon captureType]
+ -[BWStillImageAnalyticsPayloadCommon clientApplicationID]
+ -[BWStillImageAnalyticsPayloadCommon clientRequestedQualityPrioritization]
+ -[BWStillImageAnalyticsPayloadCommon constituentImageDeliveryDeviceTypes]
+ -[BWStillImageAnalyticsPayloadCommon dealloc]
+ -[BWStillImageAnalyticsPayloadCommon deferred]
+ -[BWStillImageAnalyticsPayloadCommon deliverAsCameraAppSpecificEvent]
+ -[BWStillImageAnalyticsPayloadCommon deliveredDimensionHeight]
+ -[BWStillImageAnalyticsPayloadCommon deliveredDimensionWidth]
+ -[BWStillImageAnalyticsPayloadCommon depthDataDeliveryEnabled]
+ -[BWStillImageAnalyticsPayloadCommon depthEnabled]
+ -[BWStillImageAnalyticsPayloadCommon devicePosition]
+ -[BWStillImageAnalyticsPayloadCommon effectiveIntegrationTime]
+ -[BWStillImageAnalyticsPayloadCommon eventDictionary]
+ -[BWStillImageAnalyticsPayloadCommon eventName]
+ -[BWStillImageAnalyticsPayloadCommon exposureDuration]
+ -[BWStillImageAnalyticsPayloadCommon fastCapturePrioritizationEnabled]
+ -[BWStillImageAnalyticsPayloadCommon flashBrightnessRatio]
+ -[BWStillImageAnalyticsPayloadCommon focusingMethod]
+ -[BWStillImageAnalyticsPayloadCommon formatDimensionHeight]
+ -[BWStillImageAnalyticsPayloadCommon formatDimensionWidth]
+ -[BWStillImageAnalyticsPayloadCommon formatMaxFrameRate]
+ -[BWStillImageAnalyticsPayloadCommon geometricDistortionCorrectionEnabled]
+ -[BWStillImageAnalyticsPayloadCommon geometricDistortionCorrectionSource]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationBrightLightIsBrightScene]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationBrightLightROIIsComputed]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationLowLightExceedsMaxMaskAverage]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationLowLightMaskAverage]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationLowLightSkipRepair]
+ -[BWStillImageAnalyticsPayloadCommon greenGhostMitigationLowLightTripodMode]
+ -[BWStillImageAnalyticsPayloadCommon gyroStandardDeviation]
+ -[BWStillImageAnalyticsPayloadCommon highQualityPhotoWithVideoFormatSupported]
+ -[BWStillImageAnalyticsPayloadCommon imageExifOrientation]
+ -[BWStillImageAnalyticsPayloadCommon init]
+ -[BWStillImageAnalyticsPayloadCommon iso]
+ -[BWStillImageAnalyticsPayloadCommon leaderFollowerAutoFocusData]
+ -[BWStillImageAnalyticsPayloadCommon lensPosition]
+ -[BWStillImageAnalyticsPayloadCommon livePhotoEnabled]
+ -[BWStillImageAnalyticsPayloadCommon luxLevel]
+ -[BWStillImageAnalyticsPayloadCommon maxAFTrackingError]
+ -[BWStillImageAnalyticsPayloadCommon maxSphereTrackingError]
+ -[BWStillImageAnalyticsPayloadCommon minDistanceFromSphereEndStop]
+ -[BWStillImageAnalyticsPayloadCommon normalizedSNR]
+ -[BWStillImageAnalyticsPayloadCommon numberOfFaces]
+ -[BWStillImageAnalyticsPayloadCommon outputFileType]
+ -[BWStillImageAnalyticsPayloadCommon photoFormat]
+ -[BWStillImageAnalyticsPayloadCommon pixelFormat]
+ -[BWStillImageAnalyticsPayloadCommon portType]
+ -[BWStillImageAnalyticsPayloadCommon portraitEffectStatus]
+ -[BWStillImageAnalyticsPayloadCommon portraitRequested]
+ -[BWStillImageAnalyticsPayloadCommon practicalFocalLength]
+ -[BWStillImageAnalyticsPayloadCommon processingDuration]
+ -[BWStillImageAnalyticsPayloadCommon qualityPrioritization]
+ -[BWStillImageAnalyticsPayloadCommon redEyeReductionStatus]
+ -[BWStillImageAnalyticsPayloadCommon reset]
+ -[BWStillImageAnalyticsPayloadCommon resolutionFlavor]
+ -[BWStillImageAnalyticsPayloadCommon sceneFlags]
+ -[BWStillImageAnalyticsPayloadCommon semanticSceneType]
+ -[BWStillImageAnalyticsPayloadCommon semanticStyleRenderingSupported]
+ -[BWStillImageAnalyticsPayloadCommon semanticStyleToneBias]
+ -[BWStillImageAnalyticsPayloadCommon semanticStyleWarmthBias]
+ -[BWStillImageAnalyticsPayloadCommon sensorTemperature]
+ -[BWStillImageAnalyticsPayloadCommon setAccelStandardDeviation:]
+ -[BWStillImageAnalyticsPayloadCommon setActiveDeviceMask:]
+ -[BWStillImageAnalyticsPayloadCommon setAfDriverShortOccurred:]
+ -[BWStillImageAnalyticsPayloadCommon setAfPowerConsumption:]
+ -[BWStillImageAnalyticsPayloadCommon setAlsLuxLevel:]
+ -[BWStillImageAnalyticsPayloadCommon setAlsRearLuxLevel:]
+ -[BWStillImageAnalyticsPayloadCommon setApsMode:]
+ -[BWStillImageAnalyticsPayloadCommon setApsSubjectDistance:]
+ -[BWStillImageAnalyticsPayloadCommon setBinned:]
+ -[BWStillImageAnalyticsPayloadCommon setBurst:]
+ -[BWStillImageAnalyticsPayloadCommon setCameraPosture:]
+ -[BWStillImageAnalyticsPayloadCommon setCaptureFlags:]
+ -[BWStillImageAnalyticsPayloadCommon setCaptureType:]
+ -[BWStillImageAnalyticsPayloadCommon setClientApplicationID:]
+ -[BWStillImageAnalyticsPayloadCommon setClientRequestedQualityPrioritization:]
+ -[BWStillImageAnalyticsPayloadCommon setConstituentImageDeliveryDeviceTypes:]
+ -[BWStillImageAnalyticsPayloadCommon setDeferred:]
+ -[BWStillImageAnalyticsPayloadCommon setDeliverAsCameraAppSpecificEvent:]
+ -[BWStillImageAnalyticsPayloadCommon setDeliveredDimensionHeight:]
+ -[BWStillImageAnalyticsPayloadCommon setDeliveredDimensionWidth:]
+ -[BWStillImageAnalyticsPayloadCommon setDepthDataDeliveryEnabled:]
+ -[BWStillImageAnalyticsPayloadCommon setDepthEnabled:]
+ -[BWStillImageAnalyticsPayloadCommon setDevicePosition:]
+ -[BWStillImageAnalyticsPayloadCommon setEffectiveIntegrationTime:]
+ -[BWStillImageAnalyticsPayloadCommon setExposureDuration:]
+ -[BWStillImageAnalyticsPayloadCommon setFastCapturePrioritizationEnabled:]
+ -[BWStillImageAnalyticsPayloadCommon setFlashBrightnessRatio:]
+ -[BWStillImageAnalyticsPayloadCommon setFocusingMethod:]
+ -[BWStillImageAnalyticsPayloadCommon setFormatDimensionHeight:]
+ -[BWStillImageAnalyticsPayloadCommon setFormatDimensionWidth:]
+ -[BWStillImageAnalyticsPayloadCommon setFormatMaxFrameRate:]
+ -[BWStillImageAnalyticsPayloadCommon setGeometricDistortionCorrectionEnabled:]
+ -[BWStillImageAnalyticsPayloadCommon setGeometricDistortionCorrectionSource:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationBrightLightIsBrightScene:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationBrightLightROIIsComputed:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationLowLightExceedsMaxMaskAverage:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationLowLightMaskAverage:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationLowLightSkipRepair:]
+ -[BWStillImageAnalyticsPayloadCommon setGreenGhostMitigationLowLightTripodMode:]
+ -[BWStillImageAnalyticsPayloadCommon setGyroStandardDeviation:]
+ -[BWStillImageAnalyticsPayloadCommon setHighQualityPhotoWithVideoFormatSupported:]
+ -[BWStillImageAnalyticsPayloadCommon setImageExifOrientation:]
+ -[BWStillImageAnalyticsPayloadCommon setIso:]
+ -[BWStillImageAnalyticsPayloadCommon setLeaderFollowerAutoFocusData:]
+ -[BWStillImageAnalyticsPayloadCommon setLensPosition:]
+ -[BWStillImageAnalyticsPayloadCommon setLivePhotoEnabled:]
+ -[BWStillImageAnalyticsPayloadCommon setLuxLevel:]
+ -[BWStillImageAnalyticsPayloadCommon setMaxAFTrackingError:]
+ -[BWStillImageAnalyticsPayloadCommon setMaxSphereTrackingError:]
+ -[BWStillImageAnalyticsPayloadCommon setMinDistanceFromSphereEndStop:]
+ -[BWStillImageAnalyticsPayloadCommon setNormalizedSNR:]
+ -[BWStillImageAnalyticsPayloadCommon setNumberOfFaces:]
+ -[BWStillImageAnalyticsPayloadCommon setOutputFileType:]
+ -[BWStillImageAnalyticsPayloadCommon setPhotoFormat:]
+ -[BWStillImageAnalyticsPayloadCommon setPixelFormat:]
+ -[BWStillImageAnalyticsPayloadCommon setPortType:]
+ -[BWStillImageAnalyticsPayloadCommon setPortraitEffectStatus:]
+ -[BWStillImageAnalyticsPayloadCommon setPortraitRequested:]
+ -[BWStillImageAnalyticsPayloadCommon setPracticalFocalLength:]
+ -[BWStillImageAnalyticsPayloadCommon setProcessingDuration:]
+ -[BWStillImageAnalyticsPayloadCommon setQualityPrioritization:]
+ -[BWStillImageAnalyticsPayloadCommon setRedEyeReductionStatus:]
+ -[BWStillImageAnalyticsPayloadCommon setResolutionFlavor:]
+ -[BWStillImageAnalyticsPayloadCommon setSNR:]
+ -[BWStillImageAnalyticsPayloadCommon setSceneFlags:]
+ -[BWStillImageAnalyticsPayloadCommon setSemanticSceneType:]
+ -[BWStillImageAnalyticsPayloadCommon setSemanticStyleRenderingSupported:]
+ -[BWStillImageAnalyticsPayloadCommon setSemanticStyleToneBias:]
+ -[BWStillImageAnalyticsPayloadCommon setSemanticStyleWarmthBias:]
+ -[BWStillImageAnalyticsPayloadCommon setSensorTemperature:]
+ -[BWStillImageAnalyticsPayloadCommon setSphereMode:]
+ -[BWStillImageAnalyticsPayloadCommon setSpherePowerConsumption:]
+ -[BWStillImageAnalyticsPayloadCommon setStdAFTrackingError:]
+ -[BWStillImageAnalyticsPayloadCommon setStdSphereTrackingError:]
+ -[BWStillImageAnalyticsPayloadCommon setStfStillAnalyticsVersion:]
+ -[BWStillImageAnalyticsPayloadCommon setStfStillApplied:]
+ -[BWStillImageAnalyticsPayloadCommon setStfStillCorrectionStrength:]
+ -[BWStillImageAnalyticsPayloadCommon setStfStillSupported:]
+ -[BWStillImageAnalyticsPayloadCommon setStreamingTime:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrAnalyticsVersion:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrApplied:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrBackgroundCorrectionDirection:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrBackgroundCorrectionStrength:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrForegroundCorrectionDirection:]
+ -[BWStillImageAnalyticsPayloadCommon setSwfrForegroundCorrectionStrength:]
+ -[BWStillImageAnalyticsPayloadCommon setTimeLapse:]
+ -[BWStillImageAnalyticsPayloadCommon setTimeOfFlightAssistedAutoFocusEstimatorData:]
+ -[BWStillImageAnalyticsPayloadCommon setTimeOfFlightFlickerDetectionData:]
+ -[BWStillImageAnalyticsPayloadCommon setTimeSinceLastCaptureInSession:]
+ -[BWStillImageAnalyticsPayloadCommon sphereMode]
+ -[BWStillImageAnalyticsPayloadCommon spherePowerConsumption]
+ -[BWStillImageAnalyticsPayloadCommon stdAFTrackingError]
+ -[BWStillImageAnalyticsPayloadCommon stdSphereTrackingError]
+ -[BWStillImageAnalyticsPayloadCommon stfStillAnalyticsVersion]
+ -[BWStillImageAnalyticsPayloadCommon stfStillApplied]
+ -[BWStillImageAnalyticsPayloadCommon stfStillCorrectionStrength]
+ -[BWStillImageAnalyticsPayloadCommon stfStillSupported]
+ -[BWStillImageAnalyticsPayloadCommon streamingTime]
+ -[BWStillImageAnalyticsPayloadCommon swfrAnalyticsVersion]
+ -[BWStillImageAnalyticsPayloadCommon swfrApplied]
+ -[BWStillImageAnalyticsPayloadCommon swfrBackgroundCorrectionDirection]
+ -[BWStillImageAnalyticsPayloadCommon swfrBackgroundCorrectionStrength]
+ -[BWStillImageAnalyticsPayloadCommon swfrForegroundCorrectionDirection]
+ -[BWStillImageAnalyticsPayloadCommon swfrForegroundCorrectionStrength]
+ -[BWStillImageAnalyticsPayloadCommon timeLapse]
+ -[BWStillImageAnalyticsPayloadCommon timeOfFlightAssistedAutoFocusEstimatorData]
+ -[BWStillImageAnalyticsPayloadCommon timeOfFlightFlickerDetectionData]
+ -[BWStillImageAnalyticsPayloadCommon timeSinceLastCaptureInSession]
+ -[BWStillImageBravoDisparityNode _handleError:duringProcessingOfSampleBuffer:fromInput:]
+ -[BWStillImageCaptureAnalyticsPayload fusionMode]
+ -[BWStillImageCaptureAnalyticsPayload setFusionMode:]
+ -[BWStillImageErrorAnalyticsPayload digitalZoomRatioFromSource]
+ -[BWStillImageErrorAnalyticsPayload error]
+ -[BWStillImageErrorAnalyticsPayload eventDictionary]
+ -[BWStillImageErrorAnalyticsPayload eventName]
+ -[BWStillImageErrorAnalyticsPayload init]
+ -[BWStillImageErrorAnalyticsPayload reset]
+ -[BWStillImageErrorAnalyticsPayload setDigitalZoomRatioFromSource:]
+ -[BWStillImageErrorAnalyticsPayload setError:]
+ -[BWStillImageFilterNode _emitNodeErrorForErrorStatus:numberOfNodeErrors:stillImageSettings:metadata:]
+ -[BWStillImageSampleBufferSinkNode _coreAnalyticsPayloadWithSampleBuffer:error:stillImageSettings:metadata:]
+ -[BWStillImageSampleBufferSinkNode _reportCoreAnalyticsForNodeError:]
+ -[BWStillImageSampleBufferSinkNode _sendCoreAnalyticsPayloadAndResetReportingStateWithPayload:settingsID:processingFlags:]
+ -[BWStillImageSampleBufferSinkNode deferredPhotoProcessorEnabled]
+ -[BWStillImageSampleBufferSinkNode setDeferredPhotoProcessorEnabled:]
+ -[BWStillImageScalerNode _outputDimensionsForAttachedMediaKey:primaryMediaWidth:primaryMediaHeight:requestedWidth:requestedHeight:zoomWithoutUpscalingEnabled:normalizedZoomRect:optimizedEnhancedResolutionDepthCapture:]
+ -[BWUBNode _emitError:processorInput:metadata:description:]
+ -[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:]
+ -[BWVISProcessorControllerConfiguration attachStabilizedOutputCameraTrajectory]
+ -[BWVISProcessorControllerConfiguration disableTransformLimitsForPredeterminedTrajectory]
+ -[BWVISProcessorControllerConfiguration motionBlurShimmerMitigationMethod]
+ -[BWVISProcessorControllerConfiguration setAttachStabilizedOutputCameraTrajectory:]
+ -[BWVISProcessorControllerConfiguration setDisableTransformLimitsForPredeterminedTrajectory:]
+ -[BWVISProcessorControllerConfiguration setMotionBlurShimmerMitigationMethod:]
+ -[BWVideoCompressorNode _addStereoCompressionPropertiesToCompressionSettings:videoOrientation:]
+ -[BWVideoCompressorNode initWithCompressionSettings:overCaptureEnabled:stereoVideoCompressionEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:]
+ -[FigCaptureCameraParameters stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:]
+ -[FigCaptureCameraSourcePipeline _stereoVideoAddSlaveFrameSynchronizerNode:input1:input2:mediaType:name:outErr:]
+ -[FigCaptureCameraSourcePipelineConfiguration setStereoVideoCaptureEnabled:]
+ -[FigCaptureCameraSourcePipelineConfiguration stereoVideoCaptureEnabled]
+ -[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:applicationID:]
+ -[FigCaptureMovieFileSinkPipeline stereoVideoCaptureEnabled]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration depthWithDeepFusionSupported]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setDepthWithDeepFusionSupported:]
+ -[FigCaptureSourceCompanionFormat stereoVideoAEMaxGain]
+ -[FigCaptureSourceVideoFormat isStereoVideoCaptureSupported]
+ -[FigCaptureSourceVideoFormat stereoVideoAEMaxGain]
+ -[FigCaptureSourceVideoFormat stereoVideoCompanionFormat]
+ -[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
+ -[FigCaptureVISPipeline _newVISNodeWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:pipelineStage:captureDevice:outputDimensions:irisVISCleanOutputRectOut:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
+ -[FigCaptureVISPipeline initWithUpstreamOutput:graph:name:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
+ -[FigVideoCaptureConnectionConfiguration setStereoVideoCaptureEnabled:]
+ -[FigVideoCaptureConnectionConfiguration stereoVideoCaptureEnabled]
+ GCC_except_table135
+ GCC_except_table172
+ GCC_except_table177
+ GCC_except_table200
+ GCC_except_table218
+ GCC_except_table233
+ GCC_except_table257
+ GCC_except_table292
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table327
+ GCC_except_table50
+ GCC_except_table56
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table90
+ GCC_except_table98
+ _.compoundliteral.24
+ _.compoundliteral.25
+ _.compoundliteral.45
+ _.compoundliteral.56
+ _.compoundliteral.57
+ _.compoundliteral.58
+ _.compoundliteral.59
+ _.compoundliteral.63
+ _.compoundliteral.64
+ _.compoundliteral.65
+ _.compoundliteral.66
+ _.compoundliteral.68
+ _.compoundliteral.69
+ _.compoundliteral.74
+ _.compoundliteral.79
+ _.compoundliteral.80
+ _.compoundliteral.81
+ _.compoundliteral.82
+ _.compoundliteral.83
+ _.compoundliteral.84
+ _BWFigVideoCaptureDeviceStereoVideoCaptureStatusChangedNotification
+ _BWNodeSubTypeRealTimeStereoVideo
+ _BWStereoUtilitiesComputeCenterShiftForPrimaryStream
+ _BWStereoUtilitiesComputeRectificationQuaternion
+ _CMTagCollectionCreate
+ _CMTagMakeWithSInt64Value
+ _CMTaggedBufferGroupCreate
+ _FigCaptureIsRunningInVirtualization
+ _FigCaptureIsRunningInVirtualization.onceToken
+ _FigCaptureIsRunningInVirtualization.result
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithSpatialAggressorsSeenMetadata
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithSpatialVersionMetadata
+ _FigCaptureMetadataUtilitiesNormalizePoint
+ _FigCaptureOSVariantHasInternalUI
+ _FigCapturePlatformChipRevisionIdentifierString
+ _FigCaptureSourceFormatKey_StereoVideoAEMaxGain
+ _FigCaptureSourceFormatKey_StereoVideoCaptureSupported
+ _FigCaptureSourceFormatKey_StereoVideoCompanionFormat
+ _OBJC_CLASS_$_BWStereoVideoCaptureAnalyticsPayload
+ _OBJC_CLASS_$_BWStereoVideoCaptureSceneMonitor
+ _OBJC_CLASS_$_BWStereoVideoMetadataNode
+ _OBJC_CLASS_$_BWStillImageAnalyticsPayloadCommon
+ _OBJC_CLASS_$_BWStillImageErrorAnalyticsPayload
+ _OBJC_IVAR_$_BWBackgroundBlurNode._pendingPTEffectReactions
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._ispStartDuration
+ _OBJC_IVAR_$_BWCameraAppLaunchAnalyticsPayload._numberOfGraphStartsDuringLaunch
+ _OBJC_IVAR_$_BWFigCaptureDeviceVendor._createDeviceTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stereoVideoCaptureSceneMonitor
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stereoVideoCaptureSceneMonitorLock
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stereoVideoCaptureSceneMonitoringEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_BWIrisMovieInfo._irisSequenceAdjusterRecipeIdentifier
+ _OBJC_IVAR_$_BWIrisMovieInfo._maxSystemPressureLevel
+ _OBJC_IVAR_$_BWIrisMovieInfo._numberOfFramesDropped
+ _OBJC_IVAR_$_BWIrisMovieInfo._stillImageCaptureLuxLevel
+ _OBJC_IVAR_$_BWIrisMovieInfo._targetFrameRate
+ _OBJC_IVAR_$_BWIrisMovieInfo._videoFrameDurationStats
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._averageVideoFrameDurationInMilliseconds
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._maxSystemPressureLevel
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._maxVideoFrameDurationInMilliseconds
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._medianVideoFrameDurationInMilliseconds
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._minVideoFrameDurationInMilliseconds
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._numberOfFramesDropped
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._retimingRecipeIdentifier
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._stillCaptureLuxLevel
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._stillCapturePortType
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._stillCaptureResolutionFlavor
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._stillCaptureType
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._targetFrameRate
+ _OBJC_IVAR_$_BWLivePhotoMovieAnalyticsPayload._videoFrameDurationStandardDeviationInMilliseconds
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_BWMultiCamConfiguration._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_BWNodeError._metadata
+ _OBJC_IVAR_$_BWPreviewStitcherNode._narrowerCameraFoVFillsOverCapture
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._irisRetimingRecipeIdentifier
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._irisVideoFrameDurationStats
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCaptureAnalyticsPayload
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCaptureDuration
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCapturePercentageOfFramesWithAggressiveFocusDistance
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCapturePercentageOfFramesWithAggressiveLuxLevel
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_BWStats._maxNumberOfSamplesForMedianCalculation
+ _OBJC_IVAR_$_BWStats._medianCalculationEnabled
+ _OBJC_IVAR_$_BWStats._nextDataPointIndex
+ _OBJC_IVAR_$_BWStats._samples
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._cameraPosture
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._percentageOfFramesWithAggressiveFocusDistance
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._percentageOfFramesWithAggressiveLuxLevel
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._stereoVideoCaptureDuration
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_BWStereoVideoCaptureAnalyticsPayload._videoOrientation
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._focusDistanceThreshold
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._lastSuperWideFocusDistance
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._lastWideFocusDistance
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._luxLevelThreshold
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._oneShotFocusScanInProgress
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._sceneIsTooDark
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._sceneTooDarkMonitoringEnabled
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._subjectIsTooClose
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._subjectTooCloseMonitoringEnabled
+ _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._wideMiniumValidFocusDistance
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._aggregateStereoVideoCaptureStatus
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._consecutiveSpatiallyAggressiveFramesThreshold
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._numberOfConsecutiveFocusDistanceAggressiveFrames
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._numberOfConsecutiveLuxLevelAggressiveFrames
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._numberOfFocusDistanceAggressiveFrames
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._numberOfFramesEvaluatedForAggressiveStatus
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._numberOfLuxLevelAggressiveFrames
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._serializedRectificationQuaternion
+ _OBJC_IVAR_$_BWStereoVideoMetadataNode._startingPTS
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._SNR
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._accelStandardDeviation
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._activeDeviceMask
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._afDriverShortOccurred
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._afPowerConsumption
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._alsLuxLevel
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._alsRearLuxLevel
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._apsMode
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._apsSubjectDistance
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._binned
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._burst
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._cameraPosture
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._captureFlags
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._captureType
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._clientApplicationID
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._clientRequestedQualityPrioritization
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._constituentImageDeliveryDeviceTypes
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._deferred
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._deliverAsCameraAppSpecificEvent
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._deliveredDimensionHeight
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._deliveredDimensionWidth
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._depthDataDeliveryEnabled
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._depthEnabled
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._devicePosition
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._effectiveIntegrationTime
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._exposureDuration
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._fastCapturePrioritizationEnabled
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._flashBrightnessRatio
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._focusingMethod
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._formatDimensionHeight
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._formatDimensionWidth
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._formatMaxFrameRate
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._geometricDistortionCorrectionEnabled
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._geometricDistortionCorrectionSource
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationBrightLightIsBrightScene
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationBrightLightROIIsComputed
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationLowLightExceedsMaxMaskAverage
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationLowLightMaskAverage
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationLowLightSkipRepair
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._greenGhostMitigationLowLightTripodMode
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._gyroStandardDeviation
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._highQualityPhotoWithVideoFormatSupported
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._imageExifOrientation
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._iso
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._leaderFollowerAutoFocusData
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._lensPosition
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._livePhotoEnabled
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._luxLevel
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._maxAFTrackingError
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._maxSphereTrackingError
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._minDistanceFromSphereEndStop
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._normalizedSNR
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._numberOfFaces
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._outputFileType
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._photoFormat
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._pixelFormat
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._portType
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._portraitEffectStatus
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._portraitRequested
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._practicalFocalLength
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._processingDuration
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._qualityPrioritization
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._redEyeReductionStatus
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._resolutionFlavor
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._sceneFlags
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._semanticSceneType
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._semanticStyleRenderingSupported
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._semanticStyleToneBias
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._semanticStyleWarmthBias
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._sensorTemperature
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._sphereMode
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._spherePowerConsumption
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stdAFTrackingError
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stdSphereTrackingError
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stfStillAnalyticsVersion
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stfStillApplied
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stfStillCorrectionStrength
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._stfStillSupported
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._streamingTime
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrAnalyticsVersion
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrApplied
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrBackgroundCorrectionDirection
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrBackgroundCorrectionStrength
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrForegroundCorrectionDirection
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._swfrForegroundCorrectionStrength
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._timeLapse
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._timeOfFlightAssistedAutoFocusEstimatorData
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._timeOfFlightFlickerDetectionData
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._timeSinceLastCaptureInSession
+ _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._fusionMode
+ _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stillImageFusionMode
+ _OBJC_IVAR_$_BWStillImageErrorAnalyticsPayload._digitalZoomRatioFromSource
+ _OBJC_IVAR_$_BWStillImageErrorAnalyticsPayload._error
+ _OBJC_IVAR_$_BWStillImageSampleBufferSinkNode._deferredPhotoProcessorEnabled
+ _OBJC_IVAR_$_BWVISNode._stereoMode
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._attachStabilizedOutputCameraTrajectory
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._disableTransformLimitsForPredeterminedTrajectory
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._motionBlurShimmerMitigationMethod
+ _OBJC_IVAR_$_BWVideoCompressorNode._previousFrameOriginalPTS
+ _OBJC_IVAR_$_BWVideoCompressorNode._stereoTaggedCollections
+ _OBJC_IVAR_$_BWVideoCompressorNode._stereoVideoCompressionEnabled
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_FigCaptureDeferredProcessingEngine._currentDepthDataDeliveryEnabled
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkPipeline._stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkTailPipeline._stereoVideoCompanionVISPipeline
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._depthWithDeepFusionSupported
+ _OBJC_IVAR_$_FigCaptureSourceCompanionFormat._stereoVideoAEMaxGain
+ _OBJC_IVAR_$_FigCaptureSourceVideoFormat._stereoVideoCompanionFormat
+ _OBJC_IVAR_$_FigVideoCaptureConnectionConfiguration._stereoVideoCaptureEnabled
+ _OBJC_METACLASS_$_BWStereoVideoCaptureAnalyticsPayload
+ _OBJC_METACLASS_$_BWStereoVideoCaptureSceneMonitor
+ _OBJC_METACLASS_$_BWStereoVideoMetadataNode
+ _OBJC_METACLASS_$_BWStillImageAnalyticsPayloadCommon
+ _OBJC_METACLASS_$_BWStillImageErrorAnalyticsPayload
+ _VTCompressionSessionEncodeMultiImageFrame
+ _VTIsStereoMVHEVCEncodeSupported
+ __OBJC_$_CLASS_METHODS_BWStereoVideoCaptureSceneMonitor
+ __OBJC_$_CLASS_METHODS_BWStereoVideoMetadataNode
+ __OBJC_$_INSTANCE_METHODS_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_$_INSTANCE_METHODS_BWStereoVideoCaptureSceneMonitor
+ __OBJC_$_INSTANCE_METHODS_BWStereoVideoMetadataNode
+ __OBJC_$_INSTANCE_METHODS_BWStillImageAnalyticsPayloadCommon
+ __OBJC_$_INSTANCE_METHODS_BWStillImageErrorAnalyticsPayload
+ __OBJC_$_INSTANCE_VARIABLES_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_$_INSTANCE_VARIABLES_BWStereoVideoCaptureSceneMonitor
+ __OBJC_$_INSTANCE_VARIABLES_BWStereoVideoMetadataNode
+ __OBJC_$_INSTANCE_VARIABLES_BWStillImageAnalyticsPayloadCommon
+ __OBJC_$_INSTANCE_VARIABLES_BWStillImageErrorAnalyticsPayload
+ __OBJC_$_PROP_LIST_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_$_PROP_LIST_BWStillImageAnalyticsPayloadCommon
+ __OBJC_$_PROP_LIST_BWStillImageErrorAnalyticsPayload
+ __OBJC_CLASS_PROTOCOLS_$_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_CLASS_PROTOCOLS_$_BWStillImageAnalyticsPayloadCommon
+ __OBJC_CLASS_RO_$_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_CLASS_RO_$_BWStereoVideoCaptureSceneMonitor
+ __OBJC_CLASS_RO_$_BWStereoVideoMetadataNode
+ __OBJC_CLASS_RO_$_BWStillImageAnalyticsPayloadCommon
+ __OBJC_CLASS_RO_$_BWStillImageErrorAnalyticsPayload
+ __OBJC_METACLASS_RO_$_BWStereoVideoCaptureAnalyticsPayload
+ __OBJC_METACLASS_RO_$_BWStereoVideoCaptureSceneMonitor
+ __OBJC_METACLASS_RO_$_BWStereoVideoMetadataNode
+ __OBJC_METACLASS_RO_$_BWStillImageAnalyticsPayloadCommon
+ __OBJC_METACLASS_RO_$_BWStillImageErrorAnalyticsPayload
+ ___102-[BWStillImageFilterNode _emitNodeErrorForErrorStatus:numberOfNodeErrors:stillImageSettings:metadata:]_block_invoke
+ ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.287
+ ___177-[BWVideoCompressorNode initWithCompressionSettings:overCaptureEnabled:stereoVideoCompressionEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:]_block_invoke
+ ___196-[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:applicationID:]_block_invoke
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.536
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.854
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.262
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.265
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.240
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.243
+ ___53-[BWVideoCompressorNode renderSampleBuffer:forInput:]_block_invoke.60
+ ___59-[BWUBNode _emitError:processorInput:metadata:description:]_block_invoke
+ ___75-[BWPhotonicEngineNode _emitError:stillImageSettings:metadata:description:]_block_invoke
+ ___95-[BWMultiCamConfiguration sortedStreamsForTNRFeatureBasedRegistration:prioritizePrimaryStream:]_block_invoke
+ ___FigCaptureIsRunningInVirtualization_block_invoke
+ ___FigCaptureSessionServerStart_block_invoke_3
+ ___block_descriptor_32_e31_B16?0^{opaqueCMSampleBuffer=}8l
+ ___block_descriptor_49_e8_32o40o_e51_q24?0"BWFigCaptureStream"8"BWFigCaptureStream"16ls32l8s40l8
+ ___block_descriptor_80_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_literal_global.105
+ ___block_literal_global.183
+ ___block_literal_global.20
+ ___block_literal_global.23
+ ___block_literal_global.230
+ ___block_literal_global.233
+ ___block_literal_global.248
+ ___block_literal_global.26
+ ___block_literal_global.264
+ ___block_literal_global.269
+ ___block_literal_global.282
+ ___block_literal_global.367
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.486
+ ___block_literal_global.488
+ ___block_literal_global.490
+ ___block_literal_global.492
+ ___block_literal_global.494
+ ___block_literal_global.553
+ ___block_literal_global.658
+ ___block_literal_global.678
+ ___block_literal_global.681
+ ___block_literal_global.683
+ ___block_literal_global.684
+ ___block_literal_global.710
+ ___block_literal_global.770
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.754
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.752
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.748
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke.539
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.540
+ ___captureSession_updateRunningCondition_block_invoke.374
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.668
+ ___dfp_createStateMachine_block_invoke.484
+ ___getPTEffectDescriptorClass_block_invoke
+ ___getPTEffectDescriptorClass_block_invoke.cold.1
+ __unnamed_array_storage.110
+ __unnamed_array_storage.130
+ __unnamed_array_storage.154
+ __unnamed_array_storage.159
+ __unnamed_array_storage.160
+ __unnamed_array_storage.237
+ __unnamed_array_storage.306
+ __unnamed_array_storage.352
+ __unnamed_array_storage.365
+ __unnamed_array_storage.368
+ __unnamed_array_storage.376
+ __unnamed_array_storage.382
+ __unnamed_array_storage.449
+ __unnamed_array_storage.480
+ _captureSession_resetCameraAppSessionStartupTelemetry
+ _cs_addObjectToStreamsAttributes
+ _gStereoVideoMetadataNodeTrace
+ _getPTEffectDescriptorClass
+ _getPTEffectDescriptorClass.softClass
+ _kBWFileWriterAction_SpatialAggressorsSeen
+ _kBWFileWriterAction_StereoVideoCaptureDuration
+ _kBWFileWriterAction_StereoVideoCaptureStatus
+ _kBWFileWriterAction_StereoVideoCaptureStatusPercentageOfFramesWithAggressiveFocusDistance
+ _kBWFileWriterAction_StereoVideoCaptureStatusPercentageOfFramesWithAggressiveLuxLevel
+ _kCMINotification_GPUError
+ _kCMMetadataBaseDataType_UTF8
+ _kFigAppleMakerNote_FusionMode
+ _kFigCaptureDepthDataDeliveryConfigurationsKey_DeepFusionSupported
+ _kFigCaptureDeviceMultiCamConfigurationKey_TNRFeatureBasedRegistrationPriority
+ _kFigCaptureSampleBufferMetadata_FusionMode
+ _kFigCaptureSampleBufferProcessorOption_StereoVideoCaptureEnabled
+ _kFigCaptureSourceNotification_StereoVideoCaptureStatusChanged
+ _kFigCaptureStreamFocusTuningPreset_StereoVideo
+ _kFigCaptureStreamMetadata_PreviousFrameDurationInSec
+ _kFigCaptureSynchronizedStreamsGroupProperty_AEMatchIntegrationTimes
+ _kFigFormatDescriptionProjectionKind_Rectilinear
+ _kFigQuicktimeMetadataKey_SpatialAggressorsSeen
+ _kFigQuicktimeMetadataKey_SpatialFormatVersion
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputBiasRotationQuaternion
+ _kFigVideoStabilizationSampleBufferAttachmentKey_StabilizedOutputCameraGeometry
+ _kStereoVideoCaptureMetadataKey_StereoVideoCaptureStatus
+ _kVTCompressionPropertyKey_HasLeftStereoEyeView
+ _kVTCompressionPropertyKey_HasRightStereoEyeView
+ _kVTCompressionPropertyKey_HorizontalDisparityAdjustment
+ _kVTCompressionPropertyKey_HorizontalFieldOfView
+ _kVTCompressionPropertyKey_MVHEVCLeftAndRightViewIDs
+ _kVTCompressionPropertyKey_MVHEVCVideoLayerIDs
+ _kVTCompressionPropertyKey_MVHEVCViewIDs
+ _kVTCompressionPropertyKey_ProjectionKind
+ _kVTCompressionPropertyKey_StereoCameraBaseline
+ _objc_msgSend$attachStabilizedOutputCameraTrajectory
+ _objc_msgSend$beginProcessingCachedBuffersIfWaiting
+ _objc_msgSend$cameraPosture
+ _objc_msgSend$configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:stereoVideoCaptureEnabled:
+ _objc_msgSend$createDeviceTime
+ _objc_msgSend$deferred
+ _objc_msgSend$deliverAsCameraAppSpecificEvent
+ _objc_msgSend$depthWithDeepFusionSupported
+ _objc_msgSend$disableTransformLimitsForPredeterminedTrajectory
+ _objc_msgSend$initWithCompressionSettings:overCaptureEnabled:stereoVideoCompressionEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:
+ _objc_msgSend$initWithMedianCalculationEnabled:maxNumberOfSamplesForMedianCalculation:
+ _objc_msgSend$initWithPorts:secondaryPort:cameraInfoByPortType:
+ _objc_msgSend$initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:
+ _objc_msgSend$initWithTuningParametersByPortType:attachDebugFrameStatistics:
+ _objc_msgSend$irisSequenceAdjusterRecipeIdentifier
+ _objc_msgSend$isRenderRequiredForRequest:
+ _objc_msgSend$maxSystemPressureLevel
+ _objc_msgSend$median
+ _objc_msgSend$motionBlurShimmerMitigationMethod
+ _objc_msgSend$newError:sourceNode:stillImageSettings:metadata:
+ _objc_msgSend$numberOfFaces
+ _objc_msgSend$numberOfFramesDropped
+ _objc_msgSend$outColorBufferWriteSkipped
+ _objc_msgSend$previewFrameDuration
+ _objc_msgSend$resolveStereoVideoCaptureStatusWithFrameStatistics:stereoVideoCaptureStatusOut:
+ _objc_msgSend$runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:
+ _objc_msgSend$setActiveEffectType:
+ _objc_msgSend$setAllowSkipOutColorBufferWrite:
+ _objc_msgSend$setAttachStabilizedOutputCameraTrajectory:
+ _objc_msgSend$setAvailableEffectTypes:
+ _objc_msgSend$setAverageVideoFrameDurationInMilliseconds:
+ _objc_msgSend$setColorSize:
+ _objc_msgSend$setDepthWithDeepFusionSupported:
+ _objc_msgSend$setDigitalZoomRatioFromSource:
+ _objc_msgSend$setDisableTransformLimitsForPredeterminedTrajectory:
+ _objc_msgSend$setExternalDisparitySize:
+ _objc_msgSend$setIrisSequenceAdjusterRecipeIdentifier:
+ _objc_msgSend$setIspStartDuration:
+ _objc_msgSend$setMaxVideoFrameDurationInMilliseconds:
+ _objc_msgSend$setMedianVideoFrameDurationInMilliseconds:
+ _objc_msgSend$setMinVideoFrameDurationInMilliseconds:
+ _objc_msgSend$setMotionBlurShimmerMitigationMethod:
+ _objc_msgSend$setNumberOfGraphStartsDuringLaunch:
+ _objc_msgSend$setPercentageOfFramesWithAggressiveFocusDistance:
+ _objc_msgSend$setPercentageOfFramesWithAggressiveLuxLevel:
+ _objc_msgSend$setRetimingRecipeIdentifier:
+ _objc_msgSend$setStereoVideoCaptureDuration:
+ _objc_msgSend$setStereoVideoCaptureEnabled:
+ _objc_msgSend$setStereoVideoCaptureStatus:
+ _objc_msgSend$setStillCaptureLuxLevel:
+ _objc_msgSend$setStillCapturePortType:
+ _objc_msgSend$setStillCaptureResolutionFlavor:
+ _objc_msgSend$setStillCaptureType:
+ _objc_msgSend$setStillImageCaptureLuxLevel:
+ _objc_msgSend$setTargetFrameRate:
+ _objc_msgSend$setVideoFrameDurationStandardDeviationInMilliseconds:
+ _objc_msgSend$setVideoFrameDurationStats:
+ _objc_msgSend$stereoVideoAEMaxGain
+ _objc_msgSend$stereoVideoCaptureEnabled
+ _objc_msgSend$stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:
+ _objc_msgSend$stereoVideoCaptureStatus
+ _objc_msgSend$stereoVideoCompanionFormat
+ _objc_msgSend$stillImageCaptureLuxLevel
+ _objc_msgSend$targetFrameRate
+ _objc_msgSend$videoFrameDurationStats
+ _sGPUErrorNotificationToken
+ _su_computeRectificationRotation
+ _su_getViewMatrixInCameraCoordinates
- +[BWMultiCamConfiguration configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:]
- +[BWNodeError newError:sourceNode:stillImageSettings:]
- -[BWDeepFusionProcessorInput beginProcessingCachedBuffers]
- -[BWFigCaptureDeviceVendor _logISPStartupTimeToCoreAnalytics:]
- -[BWFigVideoCaptureDevice _updateSDOFFocusStateForAutofocusProperty:propertyValue:]
- -[BWFigVideoCaptureDevice _zeroShutterLagWithDepthConfigureActiveSlaveStreamForMasterStream:]
- -[BWMultiCamConfiguration _initWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:withCaptureDevice:readCurrentStateFromCaptureDevice:]
- -[BWNodeError _initWithError:sourceNode:stillImageSettings:recordingSettings:]
- -[BWPhotonicEngineNode _emitError:stillImageSettings:description:]
- -[BWPortraitAutoSuggest perFrameObjectValidity:originalFrameWidth:originalFrameHeight:frameWidth:frameHeight:finalCropRect:zoomFactor:]
- -[BWPortraitAutoSuggest processSbuf:zoomFactor:]
- -[BWPortraitAutoSuggest runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:zoomFactor:]
- -[BWStereoFusionNode _handleError:forSampleBuffer:input:]
- -[BWStillImageCaptureAnalyticsPayload SNR]
- -[BWStillImageCaptureAnalyticsPayload accelStandardDeviation]
- -[BWStillImageCaptureAnalyticsPayload activeDeviceMask]
- -[BWStillImageCaptureAnalyticsPayload afDriverShortOccurred]
- -[BWStillImageCaptureAnalyticsPayload afPowerConsumption]
- -[BWStillImageCaptureAnalyticsPayload alsLuxLevel]
- -[BWStillImageCaptureAnalyticsPayload alsRearLuxLevel]
- -[BWStillImageCaptureAnalyticsPayload apsMode]
- -[BWStillImageCaptureAnalyticsPayload apsSubjectDistance]
- -[BWStillImageCaptureAnalyticsPayload binned]
- -[BWStillImageCaptureAnalyticsPayload burst]
- -[BWStillImageCaptureAnalyticsPayload cameraPosture]
- -[BWStillImageCaptureAnalyticsPayload captureFlags]
- -[BWStillImageCaptureAnalyticsPayload captureType]
- -[BWStillImageCaptureAnalyticsPayload clientApplicationID]
- -[BWStillImageCaptureAnalyticsPayload clientRequestedQualityPrioritization]
- -[BWStillImageCaptureAnalyticsPayload constituentImageDeliveryDeviceTypes]
- -[BWStillImageCaptureAnalyticsPayload deferred]
- -[BWStillImageCaptureAnalyticsPayload deliverAsCameraAppSpecificEvent]
- -[BWStillImageCaptureAnalyticsPayload deliveredDimensionHeight]
- -[BWStillImageCaptureAnalyticsPayload deliveredDimensionWidth]
- -[BWStillImageCaptureAnalyticsPayload depthDataDeliveryEnabled]
- -[BWStillImageCaptureAnalyticsPayload depthEnabled]
- -[BWStillImageCaptureAnalyticsPayload devicePosition]
- -[BWStillImageCaptureAnalyticsPayload effectiveIntegrationTime]
- -[BWStillImageCaptureAnalyticsPayload exposureDuration]
- -[BWStillImageCaptureAnalyticsPayload fastCapturePrioritizationEnabled]
- -[BWStillImageCaptureAnalyticsPayload flashBrightnessRatio]
- -[BWStillImageCaptureAnalyticsPayload focusingMethod]
- -[BWStillImageCaptureAnalyticsPayload formatDimensionHeight]
- -[BWStillImageCaptureAnalyticsPayload formatDimensionWidth]
- -[BWStillImageCaptureAnalyticsPayload formatMaxFrameRate]
- -[BWStillImageCaptureAnalyticsPayload geometricDistortionCorrectionEnabled]
- -[BWStillImageCaptureAnalyticsPayload geometricDistortionCorrectionSource]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationBrightLightIsBrightScene]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationBrightLightROIIsComputed]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationLowLightExceedsMaxMaskAverage]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationLowLightMaskAverage]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationLowLightSkipRepair]
- -[BWStillImageCaptureAnalyticsPayload greenGhostMitigationLowLightTripodMode]
- -[BWStillImageCaptureAnalyticsPayload gyroStandardDeviation]
- -[BWStillImageCaptureAnalyticsPayload highQualityPhotoWithVideoFormatSupported]
- -[BWStillImageCaptureAnalyticsPayload imageExifOrientation]
- -[BWStillImageCaptureAnalyticsPayload iso]
- -[BWStillImageCaptureAnalyticsPayload leaderFollowerAutoFocusData]
- -[BWStillImageCaptureAnalyticsPayload lensPosition]
- -[BWStillImageCaptureAnalyticsPayload livePhotoEnabled]
- -[BWStillImageCaptureAnalyticsPayload luxLevel]
- -[BWStillImageCaptureAnalyticsPayload maxAFTrackingError]
- -[BWStillImageCaptureAnalyticsPayload maxSphereTrackingError]
- -[BWStillImageCaptureAnalyticsPayload minDistanceFromSphereEndStop]
- -[BWStillImageCaptureAnalyticsPayload normalizedSNR]
- -[BWStillImageCaptureAnalyticsPayload numberOfFaces]
- -[BWStillImageCaptureAnalyticsPayload outputFileType]
- -[BWStillImageCaptureAnalyticsPayload photoFormat]
- -[BWStillImageCaptureAnalyticsPayload pixelFormat]
- -[BWStillImageCaptureAnalyticsPayload portType]
- -[BWStillImageCaptureAnalyticsPayload portraitEffectStatus]
- -[BWStillImageCaptureAnalyticsPayload portraitRequested]
- -[BWStillImageCaptureAnalyticsPayload practicalFocalLength]
- -[BWStillImageCaptureAnalyticsPayload processingDuration]
- -[BWStillImageCaptureAnalyticsPayload qualityPrioritization]
- -[BWStillImageCaptureAnalyticsPayload redEyeReductionStatus]
- -[BWStillImageCaptureAnalyticsPayload resolutionFlavor]
- -[BWStillImageCaptureAnalyticsPayload sceneFlags]
- -[BWStillImageCaptureAnalyticsPayload semanticSceneType]
- -[BWStillImageCaptureAnalyticsPayload semanticStyleRenderingSupported]
- -[BWStillImageCaptureAnalyticsPayload semanticStyleToneBias]
- -[BWStillImageCaptureAnalyticsPayload semanticStyleWarmthBias]
- -[BWStillImageCaptureAnalyticsPayload sensorTemperature]
- -[BWStillImageCaptureAnalyticsPayload setAccelStandardDeviation:]
- -[BWStillImageCaptureAnalyticsPayload setActiveDeviceMask:]
- -[BWStillImageCaptureAnalyticsPayload setAfDriverShortOccurred:]
- -[BWStillImageCaptureAnalyticsPayload setAfPowerConsumption:]
- -[BWStillImageCaptureAnalyticsPayload setAlsLuxLevel:]
- -[BWStillImageCaptureAnalyticsPayload setAlsRearLuxLevel:]
- -[BWStillImageCaptureAnalyticsPayload setApsMode:]
- -[BWStillImageCaptureAnalyticsPayload setApsSubjectDistance:]
- -[BWStillImageCaptureAnalyticsPayload setBinned:]
- -[BWStillImageCaptureAnalyticsPayload setBurst:]
- -[BWStillImageCaptureAnalyticsPayload setCameraPosture:]
- -[BWStillImageCaptureAnalyticsPayload setCaptureFlags:]
- -[BWStillImageCaptureAnalyticsPayload setCaptureType:]
- -[BWStillImageCaptureAnalyticsPayload setClientApplicationID:]
- -[BWStillImageCaptureAnalyticsPayload setClientRequestedQualityPrioritization:]
- -[BWStillImageCaptureAnalyticsPayload setConstituentImageDeliveryDeviceTypes:]
- -[BWStillImageCaptureAnalyticsPayload setDeferred:]
- -[BWStillImageCaptureAnalyticsPayload setDeliverAsCameraAppSpecificEvent:]
- -[BWStillImageCaptureAnalyticsPayload setDeliveredDimensionHeight:]
- -[BWStillImageCaptureAnalyticsPayload setDeliveredDimensionWidth:]
- -[BWStillImageCaptureAnalyticsPayload setDepthDataDeliveryEnabled:]
- -[BWStillImageCaptureAnalyticsPayload setDepthEnabled:]
- -[BWStillImageCaptureAnalyticsPayload setDevicePosition:]
- -[BWStillImageCaptureAnalyticsPayload setEffectiveIntegrationTime:]
- -[BWStillImageCaptureAnalyticsPayload setExposureDuration:]
- -[BWStillImageCaptureAnalyticsPayload setFastCapturePrioritizationEnabled:]
- -[BWStillImageCaptureAnalyticsPayload setFlashBrightnessRatio:]
- -[BWStillImageCaptureAnalyticsPayload setFocusingMethod:]
- -[BWStillImageCaptureAnalyticsPayload setFormatDimensionHeight:]
- -[BWStillImageCaptureAnalyticsPayload setFormatDimensionWidth:]
- -[BWStillImageCaptureAnalyticsPayload setFormatMaxFrameRate:]
- -[BWStillImageCaptureAnalyticsPayload setGeometricDistortionCorrectionEnabled:]
- -[BWStillImageCaptureAnalyticsPayload setGeometricDistortionCorrectionSource:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationBrightLightIsBrightScene:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationBrightLightROIIsComputed:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationLowLightExceedsMaxMaskAverage:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationLowLightMaskAverage:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationLowLightSkipRepair:]
- -[BWStillImageCaptureAnalyticsPayload setGreenGhostMitigationLowLightTripodMode:]
- -[BWStillImageCaptureAnalyticsPayload setGyroStandardDeviation:]
- -[BWStillImageCaptureAnalyticsPayload setHighQualityPhotoWithVideoFormatSupported:]
- -[BWStillImageCaptureAnalyticsPayload setImageExifOrientation:]
- -[BWStillImageCaptureAnalyticsPayload setIso:]
- -[BWStillImageCaptureAnalyticsPayload setLeaderFollowerAutoFocusData:]
- -[BWStillImageCaptureAnalyticsPayload setLensPosition:]
- -[BWStillImageCaptureAnalyticsPayload setLivePhotoEnabled:]
- -[BWStillImageCaptureAnalyticsPayload setLuxLevel:]
- -[BWStillImageCaptureAnalyticsPayload setMaxAFTrackingError:]
- -[BWStillImageCaptureAnalyticsPayload setMaxSphereTrackingError:]
- -[BWStillImageCaptureAnalyticsPayload setMinDistanceFromSphereEndStop:]
- -[BWStillImageCaptureAnalyticsPayload setNormalizedSNR:]
- -[BWStillImageCaptureAnalyticsPayload setNumberOfFaces:]
- -[BWStillImageCaptureAnalyticsPayload setOutputFileType:]
- -[BWStillImageCaptureAnalyticsPayload setPhotoFormat:]
- -[BWStillImageCaptureAnalyticsPayload setPixelFormat:]
- -[BWStillImageCaptureAnalyticsPayload setPortType:]
- -[BWStillImageCaptureAnalyticsPayload setPortraitEffectStatus:]
- -[BWStillImageCaptureAnalyticsPayload setPortraitRequested:]
- -[BWStillImageCaptureAnalyticsPayload setPracticalFocalLength:]
- -[BWStillImageCaptureAnalyticsPayload setProcessingDuration:]
- -[BWStillImageCaptureAnalyticsPayload setQualityPrioritization:]
- -[BWStillImageCaptureAnalyticsPayload setRedEyeReductionStatus:]
- -[BWStillImageCaptureAnalyticsPayload setResolutionFlavor:]
- -[BWStillImageCaptureAnalyticsPayload setSNR:]
- -[BWStillImageCaptureAnalyticsPayload setSceneFlags:]
- -[BWStillImageCaptureAnalyticsPayload setSemanticSceneType:]
- -[BWStillImageCaptureAnalyticsPayload setSemanticStyleRenderingSupported:]
- -[BWStillImageCaptureAnalyticsPayload setSemanticStyleToneBias:]
- -[BWStillImageCaptureAnalyticsPayload setSemanticStyleWarmthBias:]
- -[BWStillImageCaptureAnalyticsPayload setSensorTemperature:]
- -[BWStillImageCaptureAnalyticsPayload setSphereMode:]
- -[BWStillImageCaptureAnalyticsPayload setSpherePowerConsumption:]
- -[BWStillImageCaptureAnalyticsPayload setStdAFTrackingError:]
- -[BWStillImageCaptureAnalyticsPayload setStdSphereTrackingError:]
- -[BWStillImageCaptureAnalyticsPayload setStfStillAnalyticsVersion:]
- -[BWStillImageCaptureAnalyticsPayload setStfStillApplied:]
- -[BWStillImageCaptureAnalyticsPayload setStfStillCorrectionStrength:]
- -[BWStillImageCaptureAnalyticsPayload setStfStillSupported:]
- -[BWStillImageCaptureAnalyticsPayload setStreamingTime:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrAnalyticsVersion:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrApplied:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrBackgroundCorrectionDirection:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrBackgroundCorrectionStrength:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrForegroundCorrectionDirection:]
- -[BWStillImageCaptureAnalyticsPayload setSwfrForegroundCorrectionStrength:]
- -[BWStillImageCaptureAnalyticsPayload setTimeLapse:]
- -[BWStillImageCaptureAnalyticsPayload setTimeOfFlightAssistedAutoFocusEstimatorData:]
- -[BWStillImageCaptureAnalyticsPayload setTimeOfFlightFlickerDetectionData:]
- -[BWStillImageCaptureAnalyticsPayload setTimeSinceLastCaptureInSession:]
- -[BWStillImageCaptureAnalyticsPayload sphereMode]
- -[BWStillImageCaptureAnalyticsPayload spherePowerConsumption]
- -[BWStillImageCaptureAnalyticsPayload stdAFTrackingError]
- -[BWStillImageCaptureAnalyticsPayload stdSphereTrackingError]
- -[BWStillImageCaptureAnalyticsPayload stfStillAnalyticsVersion]
- -[BWStillImageCaptureAnalyticsPayload stfStillApplied]
- -[BWStillImageCaptureAnalyticsPayload stfStillCorrectionStrength]
- -[BWStillImageCaptureAnalyticsPayload stfStillSupported]
- -[BWStillImageCaptureAnalyticsPayload streamingTime]
- -[BWStillImageCaptureAnalyticsPayload swfrAnalyticsVersion]
- -[BWStillImageCaptureAnalyticsPayload swfrApplied]
- -[BWStillImageCaptureAnalyticsPayload swfrBackgroundCorrectionDirection]
- -[BWStillImageCaptureAnalyticsPayload swfrBackgroundCorrectionStrength]
- -[BWStillImageCaptureAnalyticsPayload swfrForegroundCorrectionDirection]
- -[BWStillImageCaptureAnalyticsPayload swfrForegroundCorrectionStrength]
- -[BWStillImageCaptureAnalyticsPayload timeLapse]
- -[BWStillImageCaptureAnalyticsPayload timeOfFlightAssistedAutoFocusEstimatorData]
- -[BWStillImageCaptureAnalyticsPayload timeOfFlightFlickerDetectionData]
- -[BWStillImageCaptureAnalyticsPayload timeSinceLastCaptureInSession]
- -[BWStillImageFilterNode _emitNodeErrorForErrorStatus:numberOfNodeErrors:stillImageSettings:]
- -[BWStillImageSampleBufferSinkNode _coreAnalyticsPayloadWithSampleBuffer:stillImageSettings:]
- -[BWStillImageScalerNode _outputDimensionsForAttachedMediaKey:primaryMediaWidth:primaryMediaHeight:requestedWidth:requestedHeight:zoomWithoutUpscalingEnabled:normalizedZoomRect:]
- -[BWUBNode _emitError:processorInput:description:]
- -[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCenterQuaternion:]
- -[BWVISProcessorControllerConfiguration attachStabilizedOutputCenterQuaternion]
- -[BWVISProcessorControllerConfiguration disableTransformLimitsForPreComputedTrajectory]
- -[BWVISProcessorControllerConfiguration setAttachStabilizedOutputCenterQuaternion:]
- -[BWVISProcessorControllerConfiguration setDisableTransformLimitsForPreComputedTrajectory:]
- -[BWVideoCompressorNode initWithCompressionSettings:overCaptureEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:]
- -[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:]
- -[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
- -[FigCaptureVISPipeline _newVISNodeWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:pipelineStage:captureDevice:outputDimensions:irisVISCleanOutputRectOut:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
- -[FigCaptureVISPipeline initWithUpstreamOutput:graph:name:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]
- GCC_except_table100
- GCC_except_table134
- GCC_except_table171
- GCC_except_table176
- GCC_except_table217
- GCC_except_table231
- GCC_except_table256
- GCC_except_table305
- GCC_except_table307
- GCC_except_table321
- GCC_except_table52
- GCC_except_table69
- GCC_except_table79
- GCC_except_table82
- GCC_except_table97
- _.compoundliteral.28
- _.compoundliteral.29
- _.compoundliteral.30
- _.compoundliteral.31
- _.compoundliteral.32
- _.compoundliteral.33
- _.compoundliteral.36
- _.compoundliteral.37
- _.compoundliteral.38
- _.compoundliteral.39
- _.compoundliteral.41
- _.compoundliteral.42
- _.compoundliteral.47
- _.compoundliteral.72
- _.compoundliteral.87
- _.compoundliteral.88
- _.compoundliteral.89
- _.compoundliteral.90
- _.compoundliteral.91
- _.compoundliteral.92
- _OBJC_IVAR_$_BWBackgroundBlurNode._pendingReactions
- _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._reportErrorForFrameDrops
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._SNR
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._accelStandardDeviation
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._activeDeviceMask
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._afDriverShortOccurred
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._afPowerConsumption
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._alsLuxLevel
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._alsRearLuxLevel
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._apsMode
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._apsSubjectDistance
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._binned
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._burst
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._cameraPosture
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._captureFlags
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._captureType
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._clientApplicationID
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._clientRequestedQualityPrioritization
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._constituentImageDeliveryDeviceTypes
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._deferred
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._deliverAsCameraAppSpecificEvent
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._deliveredDimensionHeight
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._deliveredDimensionWidth
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._depthDataDeliveryEnabled
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._depthEnabled
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._devicePosition
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._effectiveIntegrationTime
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._exposureDuration
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._fastCapturePrioritizationEnabled
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._flashBrightnessRatio
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._focusingMethod
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._formatDimensionHeight
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._formatDimensionWidth
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._formatMaxFrameRate
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._geometricDistortionCorrectionEnabled
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._geometricDistortionCorrectionSource
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationBrightLightIsBrightScene
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationBrightLightROIIsComputed
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationLowLightExceedsMaxMaskAverage
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationLowLightMaskAverage
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationLowLightSkipRepair
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._greenGhostMitigationLowLightTripodMode
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._gyroStandardDeviation
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._highQualityPhotoWithVideoFormatSupported
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._imageExifOrientation
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._iso
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._leaderFollowerAutoFocusData
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._lensPosition
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._livePhotoEnabled
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._luxLevel
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._maxAFTrackingError
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._maxSphereTrackingError
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._minDistanceFromSphereEndStop
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._normalizedSNR
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._numberOfFaces
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._outputFileType
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._photoFormat
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._pixelFormat
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._portType
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._portraitEffectStatus
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._portraitRequested
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._practicalFocalLength
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._processingDuration
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._qualityPrioritization
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._redEyeReductionStatus
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._resolutionFlavor
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._sceneFlags
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._semanticSceneType
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._semanticStyleRenderingSupported
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._semanticStyleToneBias
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._semanticStyleWarmthBias
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._sensorTemperature
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._sphereMode
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._spherePowerConsumption
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stdAFTrackingError
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stdSphereTrackingError
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stfStillAnalyticsVersion
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stfStillApplied
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stfStillCorrectionStrength
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._stfStillSupported
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._streamingTime
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrAnalyticsVersion
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrApplied
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrBackgroundCorrectionDirection
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrBackgroundCorrectionStrength
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrForegroundCorrectionDirection
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._swfrForegroundCorrectionStrength
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._timeLapse
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._timeOfFlightAssistedAutoFocusEstimatorData
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._timeOfFlightFlickerDetectionData
- _OBJC_IVAR_$_BWStillImageCaptureAnalyticsPayload._timeSinceLastCaptureInSession
- _OBJC_IVAR_$_BWVISNode._sbufsBeingProcessed
- _OBJC_IVAR_$_BWVISNode._sbufsBeingProcessedLock
- _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._attachStabilizedOutputCenterQuaternion
- _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._disableTransformLimitsForPreComputedTrajectory
- __OBJC_CLASS_PROTOCOLS_$_BWStillImageCaptureAnalyticsPayload
- ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.284
- ___147-[BWVideoCompressorNode initWithCompressionSettings:overCaptureEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:]_block_invoke
- ___182-[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:]_block_invoke
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.528
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.256
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.259
- ___50-[BWUBNode _emitError:processorInput:description:]_block_invoke
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.239
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.242
- ___53-[BWVideoCompressorNode renderSampleBuffer:forInput:]_block_invoke.50
- ___66-[BWPhotonicEngineNode _emitError:stillImageSettings:description:]_block_invoke
- ___93-[BWStillImageFilterNode _emitNodeErrorForErrorStatus:numberOfNodeErrors:stillImageSettings:]_block_invoke
- ___block_literal_global.100
- ___block_literal_global.115
- ___block_literal_global.169
- ___block_literal_global.21
- ___block_literal_global.219
- ___block_literal_global.227
- ___block_literal_global.24
- ___block_literal_global.245
- ___block_literal_global.258
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.364
- ___block_literal_global.414
- ___block_literal_global.485
- ___block_literal_global.487
- ___block_literal_global.489
- ___block_literal_global.491
- ___block_literal_global.536
- ___block_literal_global.653
- ___block_literal_global.673
- ___block_literal_global.674
- ___block_literal_global.676
- ___block_literal_global.679
- ___block_literal_global.705
- ___block_literal_global.767
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.749
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.747
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.743
- ___captureSession_startObservingForAudiomxdDeath_block_invoke.534
- ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.535
- ___captureSession_updateRunningCondition_block_invoke.371
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.663
- __unnamed_array_storage.109
- __unnamed_array_storage.128
- __unnamed_array_storage.153
- __unnamed_array_storage.158
- __unnamed_array_storage.342
- __unnamed_array_storage.346
- __unnamed_array_storage.349
- __unnamed_array_storage.354
- __unnamed_array_storage.375
- __unnamed_array_storage.383
- __unnamed_array_storage.386
- __unnamed_array_storage.392
- __unnamed_array_storage.438
- __unnamed_array_storage.466
- __unnamed_array_storage.90
- _kFigCaptureSampleBufferMetadata_UBFusionMode
- _objc_msgSend$attachStabilizedOutputCenterQuaternion
- _objc_msgSend$beginProcessingCachedBuffers
- _objc_msgSend$configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:
- _objc_msgSend$disableTransformLimitsForPreComputedTrajectory
- _objc_msgSend$initWithCompressionSettings:overCaptureEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:
- _objc_msgSend$initWithFormat:metalCommandQueue:availableEffectTypes:activeEffectType:effectQuality:
- _objc_msgSend$initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCenterQuaternion:
- _objc_msgSend$newError:sourceNode:stillImageSettings:
- _objc_msgSend$runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:zoomFactor:
- _objc_msgSend$setAttachStabilizedOutputCenterQuaternion:
- _objc_msgSend$setDisableTransformLimitsForPreComputedTrajectory:
- _objc_msgSend$setPosition:
CStrings:
+ "! ( stereoVideoCaptureEnabled && cinematicVideoEnabled )"
+ "! stereoVideoCaptureEnabled || cameraConfiguration.videoStabilizationStrength == FigCaptureVideoStabilizationStrengthMedium"
+ "!spatialAggressorsSeenMarkerBuffer"
+ "( sbuf || ( error != noErr ) )"
+ ", dcProcessorVersion:%d"
+ ", deepZoomMode:%d"
+ ", deepZoomVersion:%d"
+ ", gdcEnabled:1"
+ ", generateInferencesForSemanticProcessingIfNeeded:1"
+ ", idcEnabled:1"
+ ", median: %lf%@"
+ ", noiseReductionAndFusionScheme:%d"
+ ", semanticRenderingVersion:%d"
+ "-[BWFigCaptureSession stillImageCoordinator:didCapturePhotoForSettings:]_block_invoke"
+ "-[BWInferenceSynchronizerNode renderSampleBuffer:forInput:]"
+ "-[BWPhotonicEngineNode _emitError:stillImageSettings:metadata:description:]"
+ "-[BWQuickTimeMovieFileSinkNode _handleSpatialAggressorsSeenMarkerBuffer:]"
+ "-[BWStereoVideoMetadataNode _sendSpatialAggressorsSeenMarkerBufferForPTS:measuredDuration:]"
+ "-[BWUBNode _emitError:processorInput:metadata:description:]"
+ "-[BWVideoCompressorNode _createCompressionSession]"
+ "-[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:applicationID:]"
+ "1.0"
+ "1576982"
+ "863542"
+ "<%@ %p>: %@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "<<<< BWDeepFusionProcessorController >>>> %s: Request '%{private}@': %@ -> %@ (captureID:%{public}lld)"
+ "<<<< BWInferenceSynchronizerNode >>>> %s: Not synchronizing inferences (captureID:%{public}lld); %{public}@ frame: %{public}@"
+ "<<<< BWNRFProcessorController >>>> %s: Asynchronous GPU processing of type '%{public}@' %{public}@ for '%{public}@' (captureID:%lld): %{public}@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: %.4lf received spatial aggressor seen notice (capture status %d, duration %f, percentage aggressive lux level %f, percentage aggressive focus %f)"
+ "<<<< BWStereoUtilities >>>> Fig"
+ "<<<< BWStereoVideoMetadataNode >>>> %s: %@: attaching marker %@ as %.4lf"
+ "<<<< BWStereoVideoMetadataNode >>>> Fig"
+ "<<<< BWVideoCompressorNode >>>> %s: will be attaching Debug SEI metadata, and to both pixel buffers if stereo video capture is enabled"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration (continued):%{public}@%{public}@%{public}@%{public}@"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s New session created."
+ "<<<< FigCaptureSession >>>> %s: %{public}s New session created. Experiments are %@, SoC version: %@ %@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Request timed out for pending iris movie recording request without irisMovieInfo %@"
+ "@\"BWStereoVideoCaptureAnalyticsPayload\""
+ "@\"BWStereoVideoCaptureSceneMonitor\""
+ "@\"BWStillImageAnalyticsPayloadCommon\""
+ "@168@0:8@16i24i28@32f40f44i48I52i56B60B64i68f72i76B80B84B88i92{CGRect={CGPoint=dd}{CGSize=dd}}96@128f136@140@148f156B160B164"
+ "@28@0:8B16q20"
+ "@44@0:8@16B24B28f32B36i40"
+ "@44@0:8i16@20@28@36"
+ "A0"
+ "A1"
+ "B0"
+ "B1"
+ "B32@0:8@16^i24"
+ "B32@0:8^{opaqueCMSampleBuffer=}16^i24"
+ "BWStereoUtilities.m"
+ "BWStereoVideoCaptureAnalyticsPayload"
+ "BWStereoVideoCaptureSceneMonitor"
+ "BWStereoVideoMetadataNode"
+ "BWStereoVideoMetadataNode.m"
+ "BWStillImageAnalyticsPayloadCommon"
+ "BWStillImageErrorAnalyticsPayload"
+ "Back Wide S-Wide sync node"
+ "CameraCapture (New Bugs)"
+ "Capture GPU Algorithms"
+ "Class getPTEffectDescriptorClass(void)_block_invoke"
+ "DISABLED"
+ "DeferredPhotoError"
+ "Failed to compute rectification quaternion"
+ "Failed to create an ADJasperPointCloud from point cloud data buffer. This should not happen."
+ "GPU error during processing"
+ "LastShownGPUErrorTTRPromptBuildVersion"
+ "LastShownGPUErrorTTRPromptDate"
+ "MiniumValidFocusDistance"
+ "Must have exactly 2 video inputs"
+ "Narrower Camera FoV Fills Over Capture"
+ "No analyticsPayload available -- skipping CoreAnalytics logging for BWStillImageCaptureAnalyticsPayload or BWStillImageErrorAnalyticsPayload"
+ "No sample buffer or error -- skipping CoreAnalytics logging"
+ "No stillImageCaptureAnalyticsPayload available -- skipping CoreAnalytics logging for BWStillImageCaptureAnalyticsPayload"
+ "No stillImageErrorAnalyticsPayload available -- skipping CoreAnalytics logging for BWStillImageErrorAnalyticsPayload"
+ "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@ %@"
+ "PTEffectDescriptor"
+ "Photo processing error. Please file a radar."
+ "PhotoError"
+ "RealtimeStereoVideo"
+ "SpatialAggressorsSeen"
+ "Stereo Video Metadata Node"
+ "Stereo video compression requested on system that doesn't support it"
+ "StereoVideoAEMaxGain"
+ "StereoVideoCaptureDuration"
+ "StereoVideoCaptureSceneMonitoringParameters"
+ "StereoVideoCaptureStatus"
+ "StereoVideoCaptureStatusChanged"
+ "StereoVideoCaptureStatusPercentageOfFramesWithAggressiveFocusDistance"
+ "StereoVideoCaptureStatusPercentageOfFramesWithAggressiveLuxLevel"
+ "StereoVideoCaptureSupported"
+ "StereoVideoCompanionFormat"
+ "T@\"BWStats\",C,N,V_videoFrameDurationStats"
+ "T@\"NSDictionary\",R,V_metadata"
+ "T@\"NSNumber\",C,N,V_irisSequenceAdjusterRecipeIdentifier"
+ "T@\"NSNumber\",C,N,V_retimingRecipeIdentifier"
+ "T@\"NSString\",C,N,V_stillCapturePortType"
+ "TB,N,V_attachStabilizedOutputCameraTrajectory"
+ "TB,N,V_depthWithDeepFusionSupported"
+ "TB,N,V_disableTransformLimitsForPredeterminedTrajectory"
+ "TB,N,V_stereoVideoCaptureEnabled"
+ "TB,R,N,GisStereoVideoCaptureSupported"
+ "TI,N,V_numberOfFramesDropped"
+ "TI,N,V_stillCaptureLuxLevel"
+ "TQ,N"
+ "Tail %d stereo video companion VIS Pipeline"
+ "Td,N,V_averageVideoFrameDurationInMilliseconds"
+ "Td,N,V_maxVideoFrameDurationInMilliseconds"
+ "Td,N,V_medianVideoFrameDurationInMilliseconds"
+ "Td,N,V_minVideoFrameDurationInMilliseconds"
+ "Td,N,V_targetFrameRate"
+ "Td,N,V_videoFrameDurationStandardDeviationInMilliseconds"
+ "Tf,N,V_digitalZoomRatioFromSource"
+ "Tf,N,V_percentageOfFramesWithAggressiveFocusDistance"
+ "Tf,N,V_percentageOfFramesWithAggressiveLuxLevel"
+ "Tf,N,V_stereoVideoCaptureDuration"
+ "Tf,N,V_targetFrameRate"
+ "Tf,R,V_stereoVideoAEMaxGain"
+ "Ti,N,V_ispStartDuration"
+ "Ti,N,V_motionBlurShimmerMitigationMethod"
+ "Ti,N,V_numberOfGraphStartsDuringLaunch"
+ "Ti,N,V_stereoVideoCaptureStatus"
+ "Ti,N,V_stillCaptureResolutionFlavor"
+ "Ti,N,V_stillCaptureType"
+ "Ti,N,V_stillImageCaptureLuxLevel"
+ "Ti,R,N,V_createDeviceTime"
+ "Tq,N,V_nextDataPointIndex"
+ "T{?=qiIq},R,N,V_previewFrameDuration"
+ "Unable to allocate allDetectionsCopy"
+ "Unsupported configuration for stereo video capture"
+ "[StereoVideoCompanionFormat]"
+ "[graph connectOutput:input1 toInput:slaveFrameSynchronizer.inputs[0] pipelineStage:((void *)0)]"
+ "[graph connectOutput:input2 toInput:slaveFrameSynchronizer.inputs[1] pipelineStage:((void *)0)]"
+ "[graph connectOutput:previousVideoOutput toInput:stereoVideoMetadataNode.input pipelineStage:tailPipelineStage]"
+ "[graph connectOutput:previousVideoOutput toInput:swapPrimaryWithSynchronizedSlaveNode.input pipelineStage:tailStereoCompanionVISPipelineStage]"
+ "[graph connectOutput:previousVideoOutput toInput:unswapPrimaryWithSynchronizedSlaveNode.input pipelineStage:tailStereoCompanionVISPipelineStage]"
+ "[parentPipeline addNode:stereoVideoMetadataNode error:&error]"
+ "[portType isEqualToString:(id)primaryPortType]"
+ "[self addNode:slaveFrameSynchronizer error:&error]"
+ "^{__CFData=}"
+ "_aggregateStereoVideoCaptureStatus"
+ "_attachStabilizedOutputCameraTrajectory"
+ "_averageVideoFrameDurationInMilliseconds"
+ "_captureDevice.isBravoVariant && [outputsBySourceDeviceType objectForKey:@(BWCaptureDeviceTypeWideCamera)] && [outputsBySourceDeviceType objectForKey:@(BWCaptureDeviceTypeSuperWideCamera)] && outputsBySourceDeviceType.count == 2"
+ "_consecutiveSpatiallyAggressiveFramesThreshold"
+ "_createDeviceTime"
+ "_currentDepthDataDeliveryEnabled"
+ "_depthWithDeepFusionSupported"
+ "_digitalZoomRatioFromSource"
+ "_disableTransformLimitsForPredeterminedTrajectory"
+ "_focusDistanceThreshold"
+ "_irisRetimingRecipeIdentifier"
+ "_irisSequenceAdjusterRecipeIdentifier"
+ "_irisVideoFrameDurationStats"
+ "_ispStartDuration"
+ "_lastSuperWideFocusDistance"
+ "_lastWideFocusDistance"
+ "_maxNumberOfSamplesForMedianCalculation"
+ "_maxVideoFrameDurationInMilliseconds"
+ "_medianCalculationEnabled"
+ "_medianVideoFrameDurationInMilliseconds"
+ "_minVideoFrameDurationInMilliseconds"
+ "_motionBlurShimmerMitigationMethod"
+ "_narrowerCameraFoVFillsOverCapture"
+ "_nextDataPointIndex"
+ "_numberOfConsecutiveFocusDistanceAggressiveFrames"
+ "_numberOfConsecutiveLuxLevelAggressiveFrames"
+ "_numberOfFocusDistanceAggressiveFrames"
+ "_numberOfFramesEvaluatedForAggressiveStatus"
+ "_numberOfGraphStartsDuringLaunch"
+ "_numberOfLuxLevelAggressiveFrames"
+ "_pendingPTEffectReactions"
+ "_percentageOfFramesWithAggressiveFocusDistance"
+ "_percentageOfFramesWithAggressiveLuxLevel"
+ "_previousFrameOriginalPTS"
+ "_retimingRecipeIdentifier"
+ "_samples"
+ "_serializedRectificationQuaternion"
+ "_stereoMode"
+ "_stereoTaggedCollections"
+ "_stereoVideoAEMaxGain"
+ "_stereoVideoCaptureAnalyticsPayload"
+ "_stereoVideoCaptureDuration"
+ "_stereoVideoCaptureEnabled"
+ "_stereoVideoCapturePercentageOfFramesWithAggressiveFocusDistance"
+ "_stereoVideoCapturePercentageOfFramesWithAggressiveLuxLevel"
+ "_stereoVideoCaptureSceneMonitor"
+ "_stereoVideoCaptureSceneMonitorLock"
+ "_stereoVideoCaptureSceneMonitoringEnabled"
+ "_stereoVideoCaptureStatus"
+ "_stereoVideoCompanionFormat"
+ "_stereoVideoCompanionVISPipeline"
+ "_stereoVideoCompressionEnabled"
+ "_stillCaptureLuxLevel"
+ "_stillCapturePortType"
+ "_stillCaptureResolutionFlavor"
+ "_stillCaptureType"
+ "_stillImageCaptureLuxLevel"
+ "_stillImageFusionMode"
+ "_targetFrameRate"
+ "_videoFrameDurationStandardDeviationInMilliseconds"
+ "_videoFrameDurationStats"
+ "_wideMiniumValidFocusDistance"
+ "allDetectionsCopy"
+ "analyticsPayload"
+ "attachStabilizedOutputCameraTrajectory"
+ "averageVideoFrameDurationInMilliseconds"
+ "beginProcessingCachedBuffersIfWaiting"
+ "bwstereovideometadatanode_trace"
+ "cameraGeometry"
+ "centerProjection[2] > 0.0f"
+ "centerShift"
+ "com.apple.TVSystemUIService"
+ "com.apple.coremedia.camera.StereoVideoCapture"
+ "com.apple.coremedia.capture.moviefile.stereo.companion.vis.tail.%d"
+ "configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:stereoVideoCaptureEnabled:"
+ "could not create stereo tagged buffer group"
+ "createDeviceTime"
+ "data.length == (12) * sizeof ( float )"
+ "depthWithDeepFusionSupported"
+ "description=CameraCapture-470.16.1"
+ "dfp_createStateMachine_block_invoke"
+ "digitalZoomRatioFromSource"
+ "disableTransformLimitsForPredeterminedTrajectory"
+ "dropping"
+ "focalLengthMillimeters > 0.0"
+ "initWithCompressionSettings:overCaptureEnabled:stereoVideoCompressionEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:"
+ "initWithMedianCalculationEnabled:maxNumberOfSamplesForMedianCalculation:"
+ "initWithPorts:secondaryPort:cameraInfoByPortType:"
+ "initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:"
+ "initWithTuningParametersByPortType:attachDebugFrameStatistics:"
+ "input1 && input2"
+ "inputFocalLengthPosition"
+ "irisSequenceAdjusterRecipeIdentifier"
+ "isRenderRequiredForRequest:"
+ "isStereoVideoCaptureSupported"
+ "ispStartDuration"
+ "kern.hv_vmm_present"
+ "launchDurationExcludingISP"
+ "maxVideoFrameDurationInMilliseconds"
+ "median"
+ "medianVideoFrameDurationInMilliseconds"
+ "metadata.count > 0"
+ "minVideoFrameDurationInMilliseconds"
+ "motionBlurShimmerMitigationMethod"
+ "newError:sourceNode:stillImageSettings:metadata:"
+ "nextDataPointIndex"
+ "nrfVersion:%d"
+ "numberOfGraphStartsDuringLaunch"
+ "outColorBufferWriteSkipped"
+ "outputCameraGeometryData && outputCameraGeometryData.length == sizeof( StabilizedCameraGeometry )"
+ "overCapture.preview.narrowerCameraFoVFillsOverCapture"
+ "passing through"
+ "percentageOfFramesWithAggressiveFocusDistance"
+ "percentageOfFramesWithAggressiveLuxLevel"
+ "pixelSizeMicrons > 0.0"
+ "pointCloud2"
+ "previewFrameDuration"
+ "rectificationQuaternionOut != ((void *)0)"
+ "rectificationRotation != ((void *)0)"
+ "resolveStereoVideoCaptureStatusWithFrameStatistics:stereoVideoCaptureStatusOut:"
+ "retimingRecipeIdentifier"
+ "runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:"
+ "setActiveEffectType:"
+ "setAllowSkipOutColorBufferWrite:"
+ "setAttachStabilizedOutputCameraTrajectory:"
+ "setAvailableEffectTypes:"
+ "setAverageVideoFrameDurationInMilliseconds:"
+ "setColorSize:"
+ "setDepthWithDeepFusionSupported:"
+ "setDigitalZoomRatioFromSource:"
+ "setDisableTransformLimitsForPredeterminedTrajectory:"
+ "setExternalDisparitySize:"
+ "setIrisSequenceAdjusterRecipeIdentifier:"
+ "setIspStartDuration:"
+ "setMaxVideoFrameDurationInMilliseconds:"
+ "setMedianVideoFrameDurationInMilliseconds:"
+ "setMinVideoFrameDurationInMilliseconds:"
+ "setMotionBlurShimmerMitigationMethod:"
+ "setNextDataPointIndex:"
+ "setNumberOfGraphStartsDuringLaunch:"
+ "setPercentageOfFramesWithAggressiveFocusDistance:"
+ "setPercentageOfFramesWithAggressiveLuxLevel:"
+ "setRetimingRecipeIdentifier:"
+ "setStereoVideoCaptureDuration:"
+ "setStereoVideoCaptureEnabled:"
+ "setStereoVideoCaptureStatus:"
+ "setStillCaptureLuxLevel:"
+ "setStillCapturePortType:"
+ "setStillCaptureResolutionFlavor:"
+ "setStillCaptureType:"
+ "setStillImageCaptureLuxLevel:"
+ "setTargetFrameRate:"
+ "setVideoFrameDurationStandardDeviationInMilliseconds:"
+ "setVideoFrameDurationStats:"
+ "stereo"
+ "stereoVideoAEMaxGain"
+ "stereoVideoCaptureDuration"
+ "stereoVideoCaptureEnabled"
+ "stereoVideoCaptureSceneMonitoringParametersForPortType:sensorIDString:"
+ "stereoVideoCaptureStatus"
+ "stereoVideoCaptureSupported"
+ "stereoVideoCompanionFormat"
+ "stillCaptureLuxLevel"
+ "stillCapturePortType"
+ "stillCaptureResolutionFlavor"
+ "stillCaptureType"
+ "stillImageCaptureAnalyticsPayload"
+ "stillImageCaptureLuxLevel"
+ "stillImageErrorAnalyticsPayload"
+ "synchronizedSBuf"
+ "synchronizedSourcePixelBuffer"
+ "targetFrameRate"
+ "validBufferRect"
+ "videoFrameDurationAverageInMilliseconds"
+ "videoFrameDurationMaxInMilliseconds"
+ "videoFrameDurationMedianInMilliseconds"
+ "videoFrameDurationMinInMilliseconds"
+ "videoFrameDurationStandardDeviationInMilliseconds"
+ "videoFrameDurationStats"
+ "viewMatrixOut != ((void *)0)"
- "-[BWPhotonicEngineNode _emitError:stillImageSettings:description:]"
- "-[BWUBNode _emitError:processorInput:description:]"
- "-[FigCaptureDeferredProcessingEngine _ensureGraphForProcessingContainer:sensorRawPixelFormat:sensorRawDimensions:ultraHighResSensorRawDimensions:depthDataDimensions:photoIdentifier:]"
- "423945"
- "<%@ %p>: nrfVersion:%d, noiseReductionAndFusionScheme:%d,  distortionCorrectionVersion:%d, intelligentDistortionCorrectionEnabled:%d, geometricDistortionCorrectionEnabled:%d, deepZoomVersion:%d, deepZoomMode:%d, semanticRenderingVersion:%d generateInferencesForSemanticProcessingIfNeeded:%d%@%@%@%@%@"
- "<<<< BWNRFProcessorController >>>> %s: Asynchronous GPU processing of type '%@' %@ for '%{private}@' (captureID:%lld): %@"
- "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Still Image PhotonicEngine Pipeline Configuration:%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@%{public}@"
- "<<<< FigCaptureSession >>>> %s: %{public}s Experiments are%@ disabled"
- "@\"BWStillImageCaptureAnalyticsPayload\""
- "@164@0:8@16i24i28@32f40f44i48I52i56B60B64f68i72B76B80B84i88{CGRect={CGPoint=dd}{CGSize=dd}}92@124f132@136@144f152B156B160"
- "@40@0:8@16B24f28B32i36"
- "B36@0:8^{opaqueCMSampleBuffer=}16^i24f32"
- "CoreMedia Capture"
- "Number of samples: %lld, min: %lf%@, max: %lf%@, average: %lf%@, standard deviation: %lf%@"
- "TB,N,V_attachStabilizedOutputCenterQuaternion"
- "TB,N,V_disableTransformLimitsForPreComputedTrajectory"
- "TQ,N,V_activeBlurEffect"
- "_attachStabilizedOutputCenterQuaternion"
- "_disableTransformLimitsForPreComputedTrajectory"
- "_pendingReactions"
- "_reportErrorForFrameDrops"
- "_sbufsBeingProcessed"
- "_sbufsBeingProcessedLock"
- "attachStabilizedOutputCenterQuaternion"
- "beginProcessingCachedBuffers"
- "captureSourceStorage->attributes"
- "configurationWithUnsynchronizedActiveStreamsPortTypes:synchronizedActiveStreamsGroupsPortTypes:"
- "description=CameraCapture-465.15.2"
- "disableTransformLimitsForPreComputedTrajectory"
- "initWithCompressionSettings:overCaptureEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:"
- "initWithFormat:metalCommandQueue:availableEffectTypes:activeEffectType:effectQuality:"
- "initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCenterQuaternion:"
- "newError:sourceNode:stillImageSettings:"
- "runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:zoomFactor:"
- "sbuf is nil -- skipping CoreAnalytics logging"
- "setAttachStabilizedOutputCenterQuaternion:"
- "setDisableTransformLimitsForPreComputedTrajectory:"
- "setPosition:"

```
