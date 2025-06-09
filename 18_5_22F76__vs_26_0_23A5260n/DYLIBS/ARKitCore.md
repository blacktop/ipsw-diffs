## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-631.102.1.0.0
-  __TEXT.__text: 0x188adc
-  __TEXT.__auth_stubs: 0x3c70
-  __TEXT.__objc_methlist: 0x1078c
-  __TEXT.__const: 0x2c0f4
-  __TEXT.__gcc_except_tab: 0x13b5c
-  __TEXT.__oslogstring: 0x1cf49
-  __TEXT.__cstring: 0x1d36f
-  __TEXT.__ustring: 0x140
-  __TEXT.__unwind_info: 0x6268
-  __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x1eac
-  __TEXT.__objc_methname: 0x287e5
-  __TEXT.__objc_methtype: 0xc1f4
-  __TEXT.__objc_stubs: 0x19c40
-  __DATA_CONST.__got: 0x1610
-  __DATA_CONST.__const: 0x35c8
-  __DATA_CONST.__objc_classlist: 0x820
-  __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x218
+735.0.1.0.0
+  __TEXT.__text: 0x1934cc
+  __TEXT.__auth_stubs: 0x3c80
+  __TEXT.__objc_methlist: 0x1109c
+  __TEXT.__const: 0x2c128
+  __TEXT.__gcc_except_tab: 0x13d08
+  __TEXT.__cstring: 0x1d8bb
+  __TEXT.__oslogstring: 0x1e3ef
+  __TEXT.__ustring: 0xe6
+  __TEXT.__unwind_info: 0x6530
+  __TEXT.__objc_classname: 0x2024
+  __TEXT.__objc_methname: 0x2a16b
+  __TEXT.__objc_methtype: 0xa62a
+  __TEXT.__objc_stubs: 0x1aba0
+  __DATA_CONST.__got: 0x1680
+  __DATA_CONST.__const: 0x3650
+  __DATA_CONST.__objc_classlist: 0x860
+  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7888
-  __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x758
-  __DATA_CONST.__objc_arraydata: 0x830
-  __AUTH_CONST.__auth_got: 0x1e50
-  __AUTH_CONST.__const: 0x3a98
-  __AUTH_CONST.__cfstring: 0xfea0
-  __AUTH_CONST.__objc_const: 0x3a7d8
-  __AUTH_CONST.__objc_intobj: 0x3180
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __DATA_CONST.__objc_selrefs: 0x7d50
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_superrefs: 0x790
+  __DATA_CONST.__objc_arraydata: 0x870
+  __AUTH_CONST.__auth_got: 0x1e58
+  __AUTH_CONST.__const: 0x3c98
+  __AUTH_CONST.__cfstring: 0x10440
+  __AUTH_CONST.__objc_const: 0x3cd70
+  __AUTH_CONST.__objc_intobj: 0x3210
+  __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x3390
+  __AUTH.__objc_data: 0x3660
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1e84
-  __DATA.__data: 0x19f8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1d18
+  __DATA.__objc_ivar: 0x1fe4
+  __DATA.__data: 0x1ca0
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x1dd8
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1db0
-  __DATA_DIRTY.__bss: 0x480
+  __DATA_DIRTY.__objc_data: 0x1d60
+  __DATA_DIRTY.__bss: 0x4b0
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
   - /System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit
   - /System/Library/PrivateFrameworks/AppC3D.framework/AppC3D

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 31F849F4-D249-3EFF-A584-BE597053F413
-  Functions: 7501
-  Symbols:   29060
-  CStrings:  13911
+  UUID: 04CA4B53-93D4-37D5-A19D-BCB580FF92AD
+  Functions: 7754
+  Symbols:   30022
+  CStrings:  14392
 
Symbols:
+ +[ARDepthTechnique sceneDepthTechniqueForPrioritization:temporalSmoothing:]
+ +[ARKitUserDefaults resolutionForKey:resultingDimensions:]
+ +[ARParentTechnique techniqueInArray:passingTest:]
+ +[ARPlaneData transformAnchorToPlaneAnchorConvention:]
+ +[ARReferenceImage referenceImageUUIDForPixelBuffer:]
+ +[ARSceneDepthTechnique isSupported]
+ +[ARSystemTimeSnapshot timeSinceSnapshot:]
+ +[ARTechnique techniqueConformsToProtocol:inArray:]
+ +[ARUserProfile defaultProfile]
+ +[ARUserProfile isGuestProfileEnabled]
+ +[ARVideoFormat _supportedVideoFormatsForDevicePosition:deviceType:resolutions:frameRatesByPowerUsage:videoBinned:pixelFormat:needsHDRSupport:]
+ +[ARVideoFormat photoQualityPrioritizationOverride]
+ +[ARVideoFormat photoQualityPrioritizationOverride].cold.1
+ +[ARWorldTrackingConfiguration _querySupportedVideoFormats].cold.1
+ +[ARWorldTrackingConfiguration supportedVideoFormats].cold.1
+ +[NSDictionary(ARAdditions) diff:against:]
+ -[ADMutableCameraCalibration(ARAdditions) scaleAllowStretch:]
+ -[AR2DSkeletonDetectionPostProcessingTechnique init]
+ -[ARAnchorChangeSet .cxx_destruct]
+ -[ARAnchorChangeSet addedAnchors]
+ -[ARAnchorChangeSet externalAnchors]
+ -[ARAnchorChangeSet initWithAddedAnchors:updatedAnchors:removedAnchors:externalAnchors:]
+ -[ARAnchorChangeSet removedAnchors]
+ -[ARAnchorChangeSet updatedAnchors]
+ -[ARArchive removeDataWithFilename:extension:]
+ -[ARArchive removeDataWithPath:]
+ -[ARBKSAccelerometer _pollRawOrientation]
+ -[ARBKSAccelerometer accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:]
+ -[ARBKSAccelerometer accelerometer:didChangeDeviceOrientation:]
+ -[ARBKSAccelerometer isPassive]
+ -[ARBKSAccelerometer setPassive:]
+ -[ARCAMediaTimeProvider currentTime]
+ -[ARCamera initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:]
+ -[ARCircularArray removeObject:]
+ -[ARCollaborationData recipientIdentifiers]
+ -[ARCollaborationData setRecipientIdentifiers:]
+ -[ARConfiguration _createTechniques:forStillImage:]
+ -[ARConfiguration initPrivate].cold.1
+ -[ARConfiguration techniquesForStillImageGraph]
+ -[ARDaemonReplayBlockDelegate .cxx_destruct]
+ -[ARDaemonReplayBlockDelegate replayDidFailWithError:]
+ -[ARDaemonReplayBlockDelegate replayDidStartWithReplayTime:]
+ -[ARDaemonReplayBlockDelegate replayDidStop]
+ -[ARDaemonReplayBlockDelegate replayDidUpdateResourceWithKey:atTime:]
+ -[ARDaemonReplayBlockDelegate replayFailedBlock]
+ -[ARDaemonReplayBlockDelegate replayStartedBlock]
+ -[ARDaemonReplayBlockDelegate replayStoppedBlock]
+ -[ARDaemonReplayBlockDelegate replayUpdatedBlock]
+ -[ARDaemonReplayBlockDelegate setReplayFailedBlock:]
+ -[ARDaemonReplayBlockDelegate setReplayStartedBlock:]
+ -[ARDaemonReplayBlockDelegate setReplayStoppedBlock:]
+ -[ARDaemonReplayBlockDelegate setReplayUpdatedBlock:]
+ -[ARDepthSensor internalDepthSettings]
+ -[ARDeviceOrientationSensor initWithMotionManager:alignment:].cold.1
+ -[ARDispatchSourceExecutor .cxx_destruct]
+ -[ARDispatchSourceExecutor executeWithInterval:initialDelay:block:]
+ -[ARDispatchSourceExecutor init]
+ -[ARDispatchSourceExecutor isRunning]
+ -[ARDispatchSourceExecutor stop]
+ -[ARDisplayLink currentFramesPerSecond]
+ -[AREnvironmentProbeAnchor updateTransformToCoordinateSpace:withTimestamp:]
+ -[ARFrame anchorChangeSet]
+ -[ARFrame scheduledTimestamp]
+ -[ARFrame setAnchorChangeSet:]
+ -[ARFrame setScheduledTimestamp:]
+ -[ARFrameContextHandler numberOfInFlightContexts]
+ -[ARFrameUpdateTimer .cxx_destruct]
+ -[ARFrameUpdateTimer _frameDuration]
+ -[ARFrameUpdateTimer _frameUpdateTick]
+ -[ARFrameUpdateTimer _isBeforeFirstTimerTick]
+ -[ARFrameUpdateTimer _latencyIsTooHighForFrame:]
+ -[ARFrameUpdateTimer _latencyIsTooLowForFrame:]
+ -[ARFrameUpdateTimer _startExecutorWithFrameRate:initialDelay:]
+ -[ARFrameUpdateTimer _storeNewFrame:]
+ -[ARFrameUpdateTimer _timeSinceFrameWasScheduled:]
+ -[ARFrameUpdateTimer _timeTillNextTimerTick]
+ -[ARFrameUpdateTimer _unvendedFramesCount]
+ -[ARFrameUpdateTimer _updateExecutorForFrameRate:]
+ -[ARFrameUpdateTimer _vendFrame:withReason:]
+ -[ARFrameUpdateTimer _vendFrameIfAtLastTickNoFrameWasVended]
+ -[ARFrameUpdateTimer _vendFramesIfTooManyFramesAreQueued]
+ -[ARFrameUpdateTimer _vendFramesThatExceedTheMaximumLatency]
+ -[ARFrameUpdateTimer delegate]
+ -[ARFrameUpdateTimer initWithTimeProvider:executor:]
+ -[ARFrameUpdateTimer init]
+ -[ARFrameUpdateTimer isActive]
+ -[ARFrameUpdateTimer maxDesiredLatency]
+ -[ARFrameUpdateTimer minLatency]
+ -[ARFrameUpdateTimer resetState]
+ -[ARFrameUpdateTimer scheduleFrame:captureFramesPerSecond:]
+ -[ARFrameUpdateTimer setActive:]
+ -[ARFrameUpdateTimer setDelegate:]
+ -[ARFrameUpdateTimer setMaxDesiredLatency:]
+ -[ARFrameUpdateTimer setMinLatency:]
+ -[ARFrameUpdateTimer stop]
+ -[ARFrameUpdateTimer timeoutForNextFrameUpdateWithNumberOfInFlightContexts:]
+ -[ARGPUCubemapProjector init].cold.4
+ -[ARGPUCubemapProjector init].cold.5
+ -[ARGPUCubemapProjector init].cold.6
+ -[ARImageData isBackUltraWide]
+ -[ARImageSensor internalSettings]
+ -[ARImageSensor setPowerUsage:].cold.1
+ -[ARInFrameAnchorVisualizer .cxx_destruct]
+ -[ARInFrameAnchorVisualizer drawOriginAndAnchorsOnFrame:]
+ -[ARInFrameAnchorVisualizer init]
+ -[ARLocationSensor _start]
+ -[ARMLImageDownScalingResultData isDroppedData]
+ -[ARMLImageDownScalingResultData setIsDroppedData:]
+ -[ARMLImageMattingMetadataTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]
+ -[ARMLImageProcessingTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]
+ -[ARMotionSensor initWithMotionManager:].cold.1
+ -[ARNonSynchronousData arMLDepthResult]
+ -[ARNonSynchronousData segmentationResultWithDataSource:]
+ -[ARNonSynchronousData setStillRequiresPostProcessing:]
+ -[ARNonSynchronousData stillRequiresPostProcessing]
+ -[ARParentImageSensorSettings internalSettings]
+ -[ARParentTechnique _logTechniqueState:state:data:]
+ -[ARParentTechnique prepareWasCalled]
+ -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:]
+ -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:].cold.1
+ -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:].cold.2
+ -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:].cold.3
+ -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:].cold.4
+ -[ARParentTechnique requestResultDataAtTimestamp:context:withTimeout:]
+ -[ARParentTechnique submitResultsForTimestamp:context:]
+ -[ARParentTechnique techniqueConformsToProtocol:]
+ -[ARParentTechnique toJSONWithRootName:]
+ -[ARParentTechnique(DotGraph) dotGraphWithLines:rootName:]
+ -[ARPersonOcclusionParentTechnique submitResultsForTimestamp:context:]
+ -[ARPersonSegmentationTechnique _endLoadingMLModelSignpost]
+ -[ARPersonSegmentationTechnique _endMLCreateResultSignpostWithTimestamp:]
+ -[ARPersonSegmentationTechnique _endMLProcessingSignpostWithTimestamp:]
+ -[ARPersonSegmentationTechnique _endMLRunNetworkSignpostWithTimestamp:]
+ -[ARPersonSegmentationTechnique _startLoadingMLModelSignpost]
+ -[ARPersonSegmentationTechnique _startMLCreateResultSignpostWithTimestamp:orientation:outputSize:]
+ -[ARPersonSegmentationTechnique _startMLProcessingSignpostWithTimestamp:]
+ -[ARPersonSegmentationTechnique _startMLRunNetworkSignpostWithTimestamp:]
+ -[ARPersonSegmentationTechnique disableTemporalSegmentation]
+ -[ARPersonSegmentationTechnique setDisableTemporalSegmentation:]
+ -[ARPointCloudSensorData initWithPointCloudData:captureFramePerSecond:captureDevice:captureSession:].cold.2
+ -[ARProcessInfoThermalStateProvider thermalState]
+ -[ARRemoteGeoTrackingTechnique processData:]
+ -[ARRemoteService _startServiceSynchronous:]
+ -[ARRemoteService channel]
+ -[ARRemoteService createDispatchChannelWithRequest:completion:]
+ -[ARRemoteService createDispatchChannelWithRequest:completion:].cold.1
+ -[ARRemoteService createDispatchChannelWithRequest:completion:].cold.2
+ -[ARRemoteService createDispatchChannelWithRequest:completion:].cold.3
+ -[ARRemoteService createDispatchChannelWithRequest:completion:].cold.4
+ -[ARRemoteService createDispatchChannelWithRequest:completion:].cold.5
+ -[ARRemoteService createRTChannelWithRequest:completion:]
+ -[ARRemoteService createRTChannelWithRequest:completion:].cold.1
+ -[ARRemoteService dispatchChannelClosed]
+ -[ARRemoteService dispatchChannelQueue]
+ -[ARRemoteService dispatchChannel]
+ -[ARRemoteService handleDispatchChannelMessage:size:type:]
+ -[ARRemoteService initWithDaemon:deviceEndpoint:]
+ -[ARRemoteService initWithDaemon:fixedPriorityQueueForXPC:]
+ -[ARRemoteService initWithDaemon:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:]
+ -[ARRemoteService initWithDeviceEndpoint:]
+ -[ARRemoteService initWithDispatchChannelQueue:fixedPriorityQueueForXPC:]
+ -[ARRemoteService initWithEndpoint:deviceEndpoint:]
+ -[ARRemoteService initWithFixedPriorityQueueForXPC:]
+ -[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:fixedPriorityQueueForXPC:]
+ -[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:]
+ -[ARRemoteService isDataAccessAllowed]
+ -[ARRemoteService isWorldOriginSet]
+ -[ARRemoteService serverConnectionInterrupted]
+ -[ARRemoteService serviceDidConfigureBlock]
+ -[ARRemoteService serviceDidUpdateDataAccessBlock]
+ -[ARRemoteService setChannel:]
+ -[ARRemoteService setDataAccessAllowed:]
+ -[ARRemoteService setDispatchChannel:]
+ -[ARRemoteService setDispatchChannelQueue:]
+ -[ARRemoteService setIsWorldOriginSet:]
+ -[ARRemoteService setServiceDidConfigureBlock:]
+ -[ARRemoteService setServiceDidUpdateDataAccessBlock:]
+ -[ARRemoteService setupCompleteForRTChannel]
+ -[ARRemoteTechnique techniqueDidOutputResultData:timestamp:context:].cold.1
+ -[ARRenderSyncScheduler currentFramesPerSecond]
+ -[ARSLAMState isTravelMode]
+ -[ARSceneDepthTechnique .cxx_destruct]
+ -[ARSceneDepthTechnique _generateDepthForDownscaledImageData:error:]
+ -[ARSceneDepthTechnique _generateDepthForDownscaledImageData:error:].cold.1
+ -[ARSceneDepthTechnique _getCameraCalibration:rotation:inputDimensions:]
+ -[ARSceneDepthTechnique _prepareOnDimensionsChange:outputRotation:error:]
+ -[ARSceneDepthTechnique _prepareOnce]
+ -[ARSceneDepthTechnique _prepareOnce].cold.1
+ -[ARSceneDepthTechnique _rotatedPixelBufferImageData:rotationAngle:]
+ -[ARSceneDepthTechnique _safeProcessData:]
+ -[ARSceneDepthTechnique _safeProcessData:].cold.1
+ -[ARSceneDepthTechnique _safeProcessData:].cold.2
+ -[ARSceneDepthTechnique captureBehavior]
+ -[ARSceneDepthTechnique dealloc]
+ -[ARSceneDepthTechnique depthDataSource]
+ -[ARSceneDepthTechnique initWithPrioritization:temporalSmoothing:]
+ -[ARSceneDepthTechnique init]
+ -[ARSceneDepthTechnique isBusy]
+ -[ARSceneDepthTechnique isEqual:]
+ -[ARSceneDepthTechnique pipelineParameters]
+ -[ARSceneDepthTechnique prepare:]
+ -[ARSceneDepthTechnique prioritization]
+ -[ARSceneDepthTechnique processData:]
+ -[ARSceneDepthTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]
+ -[ARSceneDepthTechnique requiredSensorDataTypes]
+ -[ARSceneDepthTechnique requiredTimeInterval]
+ -[ARSceneDepthTechnique resultDataClasses]
+ -[ARSceneDepthTechnique waitForProcessingCompleteInDeterministicMode]
+ -[ARSession _geoTrackingPublicStatusChangedFromLastVendedFrameToFrame:]
+ -[ARSession _logTechniqueGraphForDebugging]
+ -[ARSession _populateRawSceneUnderstandingDataForFrame:fromResultData:]
+ -[ARSession _preferredRenderFrameRateForCaptureFrameRate:isNominalPower:]
+ -[ARSession _preferredRenderSyncFrameRateForCaptureFrameRate:]
+ -[ARSession _setInternalConfiguration:]
+ -[ARSession _setPrimaryTechnique:secondaryTechnique:stillImageRootTechnique:]
+ -[ARSession _setThermalStateProvider:]
+ -[ARSession _startSensorsWithDataTypes:]
+ -[ARSession _startSensorsWithDataTypes:].cold.1
+ -[ARSession _trackingStateChangedFromLastVendedFrameToFrame:]
+ -[ARSession _updateAnchorsForFrame:resultDatas:context:]
+ -[ARSession _updateAnchorsForFrame:resultDatas:context:].cold.1
+ -[ARSession _updateThermalStateFromCurrentProcessInfo]
+ -[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]
+ -[ARSession configurationForPublicGetter]
+ -[ARSession currentRenderSyncFramesPerSecond]
+ -[ARSession setConfigurationForPublicGetter:]
+ -[ARSession setStillImageRootTechnique:]
+ -[ARSession setUseFrameUpdateTimer:]
+ -[ARSession stillImageRootTechnique]
+ -[ARSession timerDidVendFrame:]
+ -[ARSession useFrameUpdateTimer]
+ -[ARSkeletonDefinition .cxx_construct]
+ -[ARSystemTimeSnapshot description]
+ -[ARSystemTimeSnapshot initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:]
+ -[ARSystemTimeSnapshot init]
+ -[ARSystemTimeSnapshot timeSinceSnapshot:]
+ -[ARSystemTimeSnapshot upTimeIncludingSleepAndDriftCorrection]
+ -[ARSystemTimeSnapshot upTimeIncludingSleep]
+ -[ARSystemTimeSnapshot upTime]
+ -[ARTechnique techniqueConformsToProtocol:]
+ -[ARTechnique techniqueLevel]
+ -[ARTechnique toJSONWithRootName:]
+ -[ARTechnique(DotGraph) dotGraphWithLines:rootName:]
+ -[ARTechniqueGatherContext gatheredDataWasAlreadyCaptured]
+ -[ARTechniqueParallelGatherContext clearPreviousContext]
+ -[ARTechniqueParallelGatherContext isComplete]
+ -[ARUserProfile .cxx_destruct]
+ -[ARUserProfile description]
+ -[ARUserProfile identifier]
+ -[ARUserProfile initWithIdentifier:type:]
+ -[ARUserProfile isEqual:]
+ -[ARUserProfile type]
+ -[ARVideoFormat defaultColorSpace]
+ -[ARVideoFormat defaultPhotoSettings]
+ -[ARVideoFormat maxPhotoDimensions]
+ -[ARVideoFormat maxPhotoDimensions].cold.1
+ -[ARWorldAlignmentTechnique requiredSensorDataTypes]
+ -[ARWorldTrackingTechnique _compensationMatrixForBravoSession]
+ -[ARWorldTrackingTechnique _compensationMatrixForTrackingCameraID:]
+ -[ARWorldTrackingTechnique _compensationMatrixForWidePlusUWSessionAndTrackingCameraID:]
+ -[ARWorldTrackingTechnique _postProcessNonSynchronousDataForSceneUnderstanding:]
+ -[ARWorldTrackingTechnique _saveExtrinsicsForBravoCamSessionFromImage:]
+ -[ARWorldTrackingTechnique _saveExtrinsicsForWidePlusUWSessionFromImage:]
+ -[ARWorldTrackingTechnique _saveExtrinsicsFromImage:]
+ -[ARWorldTrackingTechnique _sessionType]
+ -[ARWorldTrackingTechnique setIsMultiSessionMode:]
+ -[DrawData color]
+ -[DrawData initWithPosition:size:color:]
+ -[DrawData position]
+ -[DrawData size]
+ -[NSUUID(ARAdditions) ar_tinyUUIDString]
+ -[PixelBufferConverter convertPixelBuffer:toFormat:]
+ -[PixelBufferConverter convertPixelBuffer:toFormat:].cold.1
+ -[PixelBufferConverter convertPixelBuffer:toFormat:].cold.2
+ -[PixelBufferConverter convertPixelBuffer:toFormat:].cold.3
+ -[PixelBufferConverter dealloc]
+ -[PixelBufferConverter init]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table148
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table75
+ OBJC_IVAR_$_ARTechniqueGatherContext._gatherLock
+ OBJC_IVAR_$_ARTechniqueGatherContext._resultsCaptured
+ _ARAbortWithError
+ _ARAppleDepthUseLegacyDepthTechnique
+ _ARAuditTokenForCurrentProcess
+ _ARAuditTokenForCurrentProcess.cold.1
+ _ARBackWidePhotoQualityPrioritizationOverride
+ _ARBackWidePhotoQualityPrioritizationOverride.cold.1
+ _ARBackWidePhotoQualityPrioritizationOverride.onceToken
+ _ARBackWidePhotoQualityPrioritizationOverride.override
+ _ARCallerName
+ _ARCreateCVPixelBufferFromPoolWithMaxAllocation
+ _ARCreateCVPixelBufferFromPoolWithZeroCopyOption.cold.3
+ _ARCreateFixedPriorityDispatchQueueWithPriority
+ _ARDeviceEqualsType
+ _AREntitlementIsPresentForCurrentProcess
+ _AREntitlementIsPresentForCurrentProcess.cold.1
+ _ARGeoTrackingDisableLocationAuthorizationCheckForReplayDefaultsKey
+ _ARImmersiveDeviceStreamingSupported
+ _ARInFrameAnchorVisualizationEnabledDefaultsKey
+ _ARInstrumentsValueFromFrameVendReason
+ _ARInstrumentsValueFromFrameVendReason.cold.1
+ _ARInstrumentsValueFromFrameVendReason.latencyTooHigh
+ _ARInstrumentsValueFromFrameVendReason.noFrameOnLastTick
+ _ARInstrumentsValueFromFrameVendReason.onceToken
+ _ARInstrumentsValueFromFrameVendReason.queueFull
+ _ARInstrumentsValueFromFrameVendReason.timerDisabled
+ _ARInstrumentsValueFromFrameVendReason.timerTick
+ _ARIsBravoCamera
+ _ARIsIntelMac
+ _ARIsIntelMac.cachedReturn
+ _ARIsIntelMac.cold.1
+ _ARIsIntelMac.onceToken
+ _ARIsKnownVirtualDevice
+ _ARKitDaemonBundle
+ _ARKitDaemonBundle.arkitDaemonBundle
+ _ARKitDaemonBundle.cold.1
+ _ARKitDaemonBundle.onceToken
+ _ARLinkedOnOrAfterConstellationE
+ _ARLinkedOnOrAfterConstellationE.cachedReturn
+ _ARLinkedOnOrAfterConstellationE.cold.1
+ _ARLinkedOnOrAfterConstellationE.onceToken
+ _ARLinkedOnOrAfterDawn
+ _ARLinkedOnOrAfterDawn.cachedReturn
+ _ARLinkedOnOrAfterDawn.cold.1
+ _ARLinkedOnOrAfterDawn.onceToken
+ _ARLinkedOnOrAfterLuck
+ _ARLinkedOnOrAfterLuck.cachedReturn
+ _ARLinkedOnOrAfterLuck.cold.1
+ _ARLinkedOnOrAfterLuck.onceToken
+ _ARLinkedOnOrAfterVisionOS_3_0
+ _ARLinkedOnOrAfterVisionOS_3_0.cachedReturn
+ _ARLinkedOnOrAfterVisionOS_3_0.cold.1
+ _ARLinkedOnOrAfterVisionOS_3_0.onceToken
+ _AROSAllowsInternalSecurityPolicies
+ _AROSAllowsInternalSecurityPolicies.cold.1
+ _AROSAllowsInternalSecurityPolicies.onceToken
+ _AROSAllowsInternalSecurityPolicies.s_isDevFused
+ _AROSHasInternalUI
+ _AROSHasInternalUI.cold.1
+ _AROSHasInternalUI.onceToken
+ _AROSHasInternalUI.s_hasInternalUI
+ _ARParentTechniqueEnableLowLatencyDefaultsKey
+ _ARPointCloudDataOutputDeferredStartEnabled
+ _ARSaveIOSurfaceRAW
+ _ARSaveIOSurfaceRAW.cold.1
+ _ARSaveIOSurfaceRAW.cold.2
+ _ARSaveIOSurfaceRAW.cold.3
+ _ARSaveIOSurfaceRAW.cold.4
+ _ARSessionDisableRenderSyncSchedulingDefaultsKey
+ _ARSubclassOverridesInstanceSelector
+ _ARTimerFramesPerSecond
+ _ARVector2Description
+ _ARWrapTo2Pi
+ _ARWrapToPi
+ _AVCaptureDeviceTypeBuiltInTelephotoCamera
+ _CAFrameRateRangeMake
+ _CA_EVENT_VIDEOFORMAT_FIELD_COLORSPACE_INT
+ _CV3DSLAMCalibrationCameraVideoModeIsSupported
+ _CV3DSLAMStateIsGravityUpdated
+ _CVPixelBufferPoolCreatePixelBufferWithAuxAttributes
+ _ComputeExtrinsicsMap
+ _CreateDrawDatasFromFrame
+ _DrawOntoPixelBufferBGRA
+ _DrawRectOfSize
+ _GetPosition
+ _IOHIDEventGetIntegerValue
+ _OBJC_CLASS_$_ADJasperColorExecutor
+ _OBJC_CLASS_$_ADLogManager
+ _OBJC_CLASS_$_ARAnchorChangeSet
+ _OBJC_CLASS_$_ARCAMediaTimeProvider
+ _OBJC_CLASS_$_ARDaemonReplayBlockDelegate
+ _OBJC_CLASS_$_ARDispatchSourceExecutor
+ _OBJC_CLASS_$_ARFrameUpdateTimer
+ _OBJC_CLASS_$_ARInFrameAnchorVisualizer
+ _OBJC_CLASS_$_ARProcessInfoThermalStateProvider
+ _OBJC_CLASS_$_ARSceneDepthTechnique
+ _OBJC_CLASS_$_ARSystemTimeSnapshot
+ _OBJC_CLASS_$_ARUserProfile
+ _OBJC_CLASS_$_DrawData
+ _OBJC_CLASS_$_PixelBufferConverter
+ _OBJC_IVAR_$_AR2DSkeletonDetectionPostProcessingTechnique._previous3DSkeletonLock
+ _OBJC_IVAR_$_ARAnchorChangeSet._addedAnchors
+ _OBJC_IVAR_$_ARAnchorChangeSet._externalAnchors
+ _OBJC_IVAR_$_ARAnchorChangeSet._removedAnchors
+ _OBJC_IVAR_$_ARAnchorChangeSet._updatedAnchors
+ _OBJC_IVAR_$_ARBKSAccelerometer._lastRawOrientation
+ _OBJC_IVAR_$_ARBKSAccelerometer._passive
+ _OBJC_IVAR_$_ARCollaborationData._recipientIdentifiers
+ _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayFailedBlock
+ _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayStartedBlock
+ _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayStoppedBlock
+ _OBJC_IVAR_$_ARDaemonReplayBlockDelegate._replayUpdatedBlock
+ _OBJC_IVAR_$_ARDepthTechnique._adLogger
+ _OBJC_IVAR_$_ARDispatchSourceExecutor._timer
+ _OBJC_IVAR_$_ARDispatchSourceExecutor._timerLock
+ _OBJC_IVAR_$_ARDispatchSourceExecutor._timerQueue
+ _OBJC_IVAR_$_ARDisplayLink._currentFramesPerSecond
+ _OBJC_IVAR_$_ARFaceTrackingImageSensor._usePreviousImageDataUponDataDrop
+ _OBJC_IVAR_$_ARFrame._anchorChangeSet
+ _OBJC_IVAR_$_ARFrame._scheduledTimestamp
+ _OBJC_IVAR_$_ARFrameUpdateTimer._active
+ _OBJC_IVAR_$_ARFrameUpdateTimer._delegate
+ _OBJC_IVAR_$_ARFrameUpdateTimer._executor
+ _OBJC_IVAR_$_ARFrameUpdateTimer._frameRate
+ _OBJC_IVAR_$_ARFrameUpdateTimer._frameWasVendedAtLastTimerTick
+ _OBJC_IVAR_$_ARFrameUpdateTimer._lastFrameVendReason
+ _OBJC_IVAR_$_ARFrameUpdateTimer._lastFrameVendTimestamp
+ _OBJC_IVAR_$_ARFrameUpdateTimer._lastTimerTick
+ _OBJC_IVAR_$_ARFrameUpdateTimer._maxDesiredLatency
+ _OBJC_IVAR_$_ARFrameUpdateTimer._minLatency
+ _OBJC_IVAR_$_ARFrameUpdateTimer._timeProvider
+ _OBJC_IVAR_$_ARFrameUpdateTimer._timerQueue
+ _OBJC_IVAR_$_ARFrameUpdateTimer._unvendedFrames
+ _OBJC_IVAR_$_ARFrameUpdateTimer._unvendedFramesLock
+ _OBJC_IVAR_$_ARInFrameAnchorVisualizer._bgraToInputFormatConverter
+ _OBJC_IVAR_$_ARInFrameAnchorVisualizer._inputFormatToBGRAConverter
+ _OBJC_IVAR_$_ARInFrameAnchorVisualizer._lock
+ _OBJC_IVAR_$_ARLocationSensor._isRunning
+ _OBJC_IVAR_$_ARLocationSensor._startTimestamp
+ _OBJC_IVAR_$_ARMLImageDownScalingResultData._isDroppedData
+ _OBJC_IVAR_$_ARMLImageDownScalingTechnique._prepared
+ _OBJC_IVAR_$_ARNonSynchronousData._stillRequiresPostProcessing
+ _OBJC_IVAR_$_ARNormalTechnique._kernelSize
+ _OBJC_IVAR_$_ARParentTechnique._isDeterministicMode
+ _OBJC_IVAR_$_ARParentTechnique._prepareWasCalled
+ _OBJC_IVAR_$_ARParentTechnique._useLowLatencyPath
+ _OBJC_IVAR_$_ARPersonSegmentationTechnique._disableTemporalSegmentation
+ _OBJC_IVAR_$_ARRemoteService._channel
+ _OBJC_IVAR_$_ARRemoteService._dataAccessAllowed
+ _OBJC_IVAR_$_ARRemoteService._deviceEndpoint
+ _OBJC_IVAR_$_ARRemoteService._dispatchChannel
+ _OBJC_IVAR_$_ARRemoteService._dispatchChannelClosed
+ _OBJC_IVAR_$_ARRemoteService._dispatchChannelQueue
+ _OBJC_IVAR_$_ARRemoteService._isWorldOriginSet
+ _OBJC_IVAR_$_ARRemoteService._serviceDidConfigureBlock
+ _OBJC_IVAR_$_ARRemoteService._serviceDidUpdateDataAccessBlock
+ _OBJC_IVAR_$_ARSceneDepthTechnique._busySemaphore
+ _OBJC_IVAR_$_ARSceneDepthTechnique._computeNormals
+ _OBJC_IVAR_$_ARSceneDepthTechnique._depthProcessingQueue
+ _OBJC_IVAR_$_ARSceneDepthTechnique._deterministic
+ _OBJC_IVAR_$_ARSceneDepthTechnique._executor
+ _OBJC_IVAR_$_ARSceneDepthTechnique._float32RotationTechnique
+ _OBJC_IVAR_$_ARSceneDepthTechnique._inputDimensions
+ _OBJC_IVAR_$_ARSceneDepthTechnique._normalsHelperBuffer
+ _OBJC_IVAR_$_ARSceneDepthTechnique._oneComponent8RotationTechnique
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputConfidenceMapPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputConfidencePixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputDepthPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputDimensionsInOriginalImageRotation
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputNormalsInOriginalImageRotationPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputRotation
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputScaledConfidenceMapPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputScaledConfidencePixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputScaledDepthPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputScaledSingleFrameConfidencePixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputScaledSingleFrameDepthPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputSingleFrameConfidencePixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._outputSingleFrameDepthPixelBufferPool
+ _OBJC_IVAR_$_ARSceneDepthTechnique._prepLock
+ _OBJC_IVAR_$_ARSceneDepthTechnique._prepared
+ _OBJC_IVAR_$_ARSceneDepthTechnique._prioritization
+ _OBJC_IVAR_$_ARSceneDepthTechnique._startedPrepare
+ _OBJC_IVAR_$_ARSceneDepthTechnique._temporalConsistencyMethod
+ _OBJC_IVAR_$_ARSession._configurationForPublicGetter
+ _OBJC_IVAR_$_ARSession._frameUpdateTimer
+ _OBJC_IVAR_$_ARSession._inFrameAnchorVisualizer
+ _OBJC_IVAR_$_ARSession._lastVendedFrame
+ _OBJC_IVAR_$_ARSession._lastVendedFrameSemaphore
+ _OBJC_IVAR_$_ARSession._resultDataPredictionQueue
+ _OBJC_IVAR_$_ARSession._stillImageProcessingQueue
+ _OBJC_IVAR_$_ARSession._stillImageRootTechnique
+ _OBJC_IVAR_$_ARSession._thermalStateProvider
+ _OBJC_IVAR_$_ARSession._useFrameUpdateTimer
+ _OBJC_IVAR_$_ARSkeletonDefinition._jointname_to_index
+ _OBJC_IVAR_$_ARSystemTimeSnapshot._upTime
+ _OBJC_IVAR_$_ARSystemTimeSnapshot._upTimeIncludingSleep
+ _OBJC_IVAR_$_ARSystemTimeSnapshot._upTimeIncludingSleepAndDriftCorrection
+ _OBJC_IVAR_$_ARUserProfile._identifier
+ _OBJC_IVAR_$_ARUserProfile._type
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._enableMLCMRelocalization
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._extrinsicsFromUWToWide
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._extrinsicsFromWideToTele
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._extrinsicsFromWideToUW
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._isMultiSessionMode
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._pendingRawSceneUnderstandingResults
+ _OBJC_IVAR_$_ARWorldTrackingTechnique._pendingRawSceneUnderstandingResultsLock
+ _OBJC_IVAR_$_DrawData._color
+ _OBJC_IVAR_$_DrawData._position
+ _OBJC_IVAR_$_DrawData._size
+ _OBJC_IVAR_$_PixelBufferConverter._pixelBufferPool
+ _OBJC_IVAR_$_PixelBufferConverter._pixelTransferSession
+ _OBJC_METACLASS_$_ARAnchorChangeSet
+ _OBJC_METACLASS_$_ARCAMediaTimeProvider
+ _OBJC_METACLASS_$_ARDaemonReplayBlockDelegate
+ _OBJC_METACLASS_$_ARDispatchSourceExecutor
+ _OBJC_METACLASS_$_ARFrameUpdateTimer
+ _OBJC_METACLASS_$_ARInFrameAnchorVisualizer
+ _OBJC_METACLASS_$_ARProcessInfoThermalStateProvider
+ _OBJC_METACLASS_$_ARSceneDepthTechnique
+ _OBJC_METACLASS_$_ARSystemTimeSnapshot
+ _OBJC_METACLASS_$_ARUserProfile
+ _OBJC_METACLASS_$_DrawData
+ _OBJC_METACLASS_$_PixelBufferConverter
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _SignedDistance
+ _TrackingStateDifferent
+ __ARAddScalingTechniquesToTechniques
+ __ARParentTechniqueForDepthTechnique
+ __OBJC_$_CATEGORY_ADMutableCameraCalibration_$_ARAdditions
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_ARAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ADMutableCameraCalibration_$_ARAdditions
+ __OBJC_$_CATEGORY_NSDictionary_$_ARAdditions
+ __OBJC_$_CLASS_METHODS_ARDepthTechnique
+ __OBJC_$_CLASS_METHODS_ARSceneDepthTechnique
+ __OBJC_$_CLASS_METHODS_ARSystemTimeSnapshot
+ __OBJC_$_CLASS_METHODS_ARUserProfile
+ __OBJC_$_INSTANCE_METHODS_ARAnchorChangeSet
+ __OBJC_$_INSTANCE_METHODS_ARCAMediaTimeProvider
+ __OBJC_$_INSTANCE_METHODS_ARDaemonReplayBlockDelegate
+ __OBJC_$_INSTANCE_METHODS_ARDispatchSourceExecutor
+ __OBJC_$_INSTANCE_METHODS_ARFrameUpdateTimer
+ __OBJC_$_INSTANCE_METHODS_ARInFrameAnchorVisualizer
+ __OBJC_$_INSTANCE_METHODS_ARProcessInfoThermalStateProvider
+ __OBJC_$_INSTANCE_METHODS_ARSceneDepthTechnique
+ __OBJC_$_INSTANCE_METHODS_ARSystemTimeSnapshot
+ __OBJC_$_INSTANCE_METHODS_ARUserProfile
+ __OBJC_$_INSTANCE_METHODS_DrawData
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(ARAdditions|ARPersonDetectionData)
+ __OBJC_$_INSTANCE_METHODS_PixelBufferConverter
+ __OBJC_$_INSTANCE_VARIABLES_ARAnchorChangeSet
+ __OBJC_$_INSTANCE_VARIABLES_ARDaemonReplayBlockDelegate
+ __OBJC_$_INSTANCE_VARIABLES_ARDispatchSourceExecutor
+ __OBJC_$_INSTANCE_VARIABLES_ARFrameUpdateTimer
+ __OBJC_$_INSTANCE_VARIABLES_ARInFrameAnchorVisualizer
+ __OBJC_$_INSTANCE_VARIABLES_ARSceneDepthTechnique
+ __OBJC_$_INSTANCE_VARIABLES_ARSystemTimeSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_ARUserProfile
+ __OBJC_$_INSTANCE_VARIABLES_DrawData
+ __OBJC_$_INSTANCE_VARIABLES_PixelBufferConverter
+ __OBJC_$_PROP_LIST_ARAnchorChangeSet
+ __OBJC_$_PROP_LIST_ARBKSAccelerometer
+ __OBJC_$_PROP_LIST_ARCAMediaTimeProvider
+ __OBJC_$_PROP_LIST_ARDaemonReplayBlockDelegate
+ __OBJC_$_PROP_LIST_ARDepthTechniqueProtocol
+ __OBJC_$_PROP_LIST_ARFrameUpdateTimer
+ __OBJC_$_PROP_LIST_ARProcessInfoThermalStateProvider
+ __OBJC_$_PROP_LIST_ARSceneDepthTechnique
+ __OBJC_$_PROP_LIST_ARSystemTimeSnapshot
+ __OBJC_$_PROP_LIST_ARThermalStateProvider
+ __OBJC_$_PROP_LIST_ARUserProfile
+ __OBJC_$_PROP_LIST_DrawData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARDaemonReplayDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARDepthTechniqueProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARFrameUpdateTimerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARRepetitiveExecutor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARSupportsAsyncEmptyResultEmission
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARThermalStateProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARTimeProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BKSAccelerometerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKSAccelerometerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARDaemonReplayDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARDepthTechniqueProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARFrameUpdateTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARRepetitiveExecutor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARSupportsAsyncEmptyResultEmission
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARThermalStateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ARTimeProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKSAccelerometerDelegate
+ __OBJC_$_PROTOCOL_REFS_ARDaemonReplayDelegate
+ __OBJC_$_PROTOCOL_REFS_ARDepthTechniqueProtocol
+ __OBJC_$_PROTOCOL_REFS_ARFrameUpdateTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_ARSupportsAsyncEmptyResultEmission
+ __OBJC_$_PROTOCOL_REFS_ARTimeProviding
+ __OBJC_$_PROTOCOL_REFS_BKSAccelerometerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ARBKSAccelerometer
+ __OBJC_CLASS_PROTOCOLS_$_ARCAMediaTimeProvider
+ __OBJC_CLASS_PROTOCOLS_$_ARDaemonReplayBlockDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ARDispatchSourceExecutor
+ __OBJC_CLASS_PROTOCOLS_$_ARMLImageMattingMetadataTechnique
+ __OBJC_CLASS_PROTOCOLS_$_ARProcessInfoThermalStateProvider
+ __OBJC_CLASS_PROTOCOLS_$_ARSceneDepthTechnique
+ __OBJC_CLASS_RO_$_ARAnchorChangeSet
+ __OBJC_CLASS_RO_$_ARCAMediaTimeProvider
+ __OBJC_CLASS_RO_$_ARDaemonReplayBlockDelegate
+ __OBJC_CLASS_RO_$_ARDispatchSourceExecutor
+ __OBJC_CLASS_RO_$_ARFrameUpdateTimer
+ __OBJC_CLASS_RO_$_ARInFrameAnchorVisualizer
+ __OBJC_CLASS_RO_$_ARProcessInfoThermalStateProvider
+ __OBJC_CLASS_RO_$_ARSceneDepthTechnique
+ __OBJC_CLASS_RO_$_ARSystemTimeSnapshot
+ __OBJC_CLASS_RO_$_ARUserProfile
+ __OBJC_CLASS_RO_$_DrawData
+ __OBJC_CLASS_RO_$_PixelBufferConverter
+ __OBJC_LABEL_PROTOCOL_$_ARDaemonReplayDelegate
+ __OBJC_LABEL_PROTOCOL_$_ARDepthTechniqueProtocol
+ __OBJC_LABEL_PROTOCOL_$_ARFrameUpdateTimerDelegate
+ __OBJC_LABEL_PROTOCOL_$_ARRepetitiveExecutor
+ __OBJC_LABEL_PROTOCOL_$_ARSupportsAsyncEmptyResultEmission
+ __OBJC_LABEL_PROTOCOL_$_ARThermalStateProvider
+ __OBJC_LABEL_PROTOCOL_$_ARTimeProviding
+ __OBJC_LABEL_PROTOCOL_$_BKSAccelerometerDelegate
+ __OBJC_METACLASS_RO_$_ARAnchorChangeSet
+ __OBJC_METACLASS_RO_$_ARCAMediaTimeProvider
+ __OBJC_METACLASS_RO_$_ARDaemonReplayBlockDelegate
+ __OBJC_METACLASS_RO_$_ARDispatchSourceExecutor
+ __OBJC_METACLASS_RO_$_ARFrameUpdateTimer
+ __OBJC_METACLASS_RO_$_ARInFrameAnchorVisualizer
+ __OBJC_METACLASS_RO_$_ARProcessInfoThermalStateProvider
+ __OBJC_METACLASS_RO_$_ARSceneDepthTechnique
+ __OBJC_METACLASS_RO_$_ARSystemTimeSnapshot
+ __OBJC_METACLASS_RO_$_ARUserProfile
+ __OBJC_METACLASS_RO_$_DrawData
+ __OBJC_METACLASS_RO_$_PixelBufferConverter
+ __OBJC_PROTOCOL_$_ARDaemonReplayDelegate
+ __OBJC_PROTOCOL_$_ARDepthTechniqueProtocol
+ __OBJC_PROTOCOL_$_ARFrameUpdateTimerDelegate
+ __OBJC_PROTOCOL_$_ARRepetitiveExecutor
+ __OBJC_PROTOCOL_$_ARSupportsAsyncEmptyResultEmission
+ __OBJC_PROTOCOL_$_ARThermalStateProvider
+ __OBJC_PROTOCOL_$_ARTimeProviding
+ __OBJC_PROTOCOL_$_BKSAccelerometerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_ARDepthTechniqueProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ARSupportsAsyncEmptyResultEmission
+ __PromotedConst.322
+ __PromotedConst.323
+ __PromotedConst.592
+ __PromotedConst.64
+ __PromotedConst.65
+ __PromotedConst.66
+ __Z26GetCV3DSLAMCameraModelTypev
+ __Z26GetCV3DSLAMCameraModelTypev.cold.1
+ __Z27IsCV3DVIOVideoModeSupported23CV3DSLAMCameraVideoMode
+ __Z27IsCV3DVIOVideoModeSupported23CV3DSLAMCameraVideoMode.cold.1
+ __ZL12setSemanticsP13ARPlaneAnchorbPK23CV3DPlaneDetectionPlane
+ __ZN12ARNoiseModelD2Ev
+ __ZN12_GLOBAL__N_124populateJointnameToIndexEP7NSArrayIP8NSStringERNSt3__113unordered_mapINS5_17basic_string_viewIcNS5_11char_traitsIcEEEEmNS5_4hashISA_EENS5_8equal_toISA_EENS5_9allocatorINS5_4pairIKSA_mEEEEEE
+ __ZN3cva3SVDINS_6MatrixIfLj0ELj0ELb0EEELb1EED2Ev
+ __ZN5arkit16BoundingBoxGroup6appendERKNS_7IntRectE
+ __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne200100Ev
+ __ZNKSt3__114default_deleteIN5arkit16FaceTrackingDataEEclB8ne200100EPS2_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ne200100Ev
+ __ZNKSt3__118__string_view_hashIcEclB8ne200100ENS_17basic_string_viewIcNS_11char_traitsIcEEEE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8ne200100EPKvm
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN5arkit16BoundingBoxGroupEEEPS3_EclB8ne200100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_EclB8ne200100Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIxNS1_IxEEEEEEPS4_EclB8ne200100Ev
+ __ZNKSt9type_infoeqB8ne200100ERKS_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110shared_ptrIN5arkit16FaceTrackingDataEEC2B8ne200100IS2_Li0EEEPT_
+ __ZNSt3__110shared_ptrIN5arkit19PrecomputedFaceDataEEC2B8ne200100IS2_Li0EEEPT_
+ __ZNSt3__110unique_ptrIN5arkit19PrecomputedFaceDataENS_14default_deleteIS2_EEED1B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100IN5arkit15RobustExpFilterIfEELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEmEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEmEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS5_JRKNS_21piecewise_construct_tENS_5tupleIJOS5_EEENSM_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEmEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIS5_EENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEmEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_17basic_string_viewIcNS_11char_traitsIcEEEEmEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__rotate_gcdB8ne200100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN5arkit7IntRectEEEEET0_S7_S7_S7_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1INS_17basic_string_viewIcS2_EELi0EEERKT_RKS4_
+ __ZNSt3__112construct_atB8ne200100IN5arkit15RobustExpFilterIfEEJddddddddEPS3_EEPT_S6_DpOT0_
+ __ZNSt3__113__fill_n_boolB8ne200100ILb0ENS_6vectorIbNS_9allocatorIbEEEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS6_vE9size_typeE
+ __ZNSt3__113__fill_n_boolB8ne200100ILb1ENS_6vectorIbNS_9allocatorIbEEEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS_29__size_difference_type_traitsIS6_vE9size_typeE
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferIN5arkit16BoundingBoxGroupERNS_9allocatorIS2_EEE17__destruct_at_endB8ne200100EPS2_
+ __ZNSt3__114__split_bufferINS_10shared_ptrIK20CV3DSLAMStateContextEERNS_9allocatorIS4_EEE5clearB8ne200100Ev
+ __ZNSt3__114__split_bufferINS_6vectorINS1_IfNS_9allocatorIfEEEENS2_IS4_EEEERNS2_IS6_EEE5clearB8ne200100Ev
+ __ZNSt3__114__split_bufferINS_6vectorIfNS_9allocatorIfEEEERNS2_IS4_EEE17__destruct_at_endB8ne200100EPS4_
+ __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS6_EEE12emplace_backIJRS6_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS6_EEE12emplace_backIJS6_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS6_EEE13emplace_frontIJS6_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEERNS_9allocatorIS6_EEE12emplace_backIJS6_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEERNS_9allocatorIS6_EEE13emplace_frontIJRS6_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIiiEENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIiiEENS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIiiEENS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIiiEERNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPNS_4pairIiiEERNS_9allocatorIS3_EEE13emplace_frontIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE13emplace_frontIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPKvRNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPKvRNS_9allocatorIS3_EEE12emplace_backIJS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIfRNS_9allocatorIfEEE12emplace_backIJfEEEvDpOT_
+ __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__115allocate_sharedB8ne200100I14RaycastSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRU8__strongU13block_pointerFvPK20CV3DRaycastResultMapEbELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I21PlaneDetectionSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100I21PlaneDetectionSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListERU8__strongU13block_pointerFvPK37CV3DPlaneDetectionSingleShotPlaneListEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN5arkit12KeyMapBufferIPKvNS_6vectorIhNS_9allocatorIhEEEEEENS6_IS9_EEJiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN5arkit15RobustExpFilterIfEENS_9allocatorIS3_EEJddddddddELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN5arkit3btr15ScaleCorrection4ImplENS_9allocatorIS4_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne200100IN5arkit3btr15ScaleCorrectionENS_9allocatorIS3_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocator_destroyB8ne200100INS_9allocatorI15ARTexturedPlaneEENS_16reverse_iteratorIPS2_EES6_EEvRT_T0_T1_
+ __ZNSt3__119__allocator_destroyB8ne200100INS_9allocatorI15ARTexturedPlaneEEPS2_S4_EEvRT_T0_T1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ERKNS_12basic_stringIcS2_S4_EEj
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__120__optional_copy_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne200100ERKS8_
+ __ZNSt3__120__optional_copy_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne200100ERKS8_.cold.1
+ __ZNSt3__120__shared_ptr_emplaceI14RaycastSessionNS_9allocatorIS1_EEEC2B8ne200100IJRP15CV3DSLAMSessionRU8__strongU13block_pointerFvPK20CV3DRaycastResultMapEbES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PlaneDetectionSessionNS_9allocatorIS1_EEEC2B8ne200100IJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI21PlaneDetectionSessionNS_9allocatorIS1_EEEC2B8ne200100IJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListERU8__strongU13block_pointerFvPK37CV3DPlaneDetectionSingleShotPlaneListEES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN5arkit12KeyMapBufferIPKvNS_6vectorIhNS_9allocatorIhEEEEEENS6_IS9_EEEC2B8ne200100IJiESA_Li0EEESA_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN5arkit15RobustExpFilterIfEENS_9allocatorIS3_EEEC2B8ne200100IJddddddddES5_Li0EEES5_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN5arkit3btr15ScaleCorrectionENS_9allocatorIS3_EEEC2B8ne200100IJES5_Li0EEES5_DpOT_
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8ne200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8ne200100EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB8ne200100EPSB_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_5arrayIhLm16EEE15ARTexturedPlaneEEPvEEEEEclB8ne200100EPS9_
+ __ZNSt3__123__optional_storage_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EE16__construct_fromB8ne200100IRKNS_20__optional_copy_baseIS7_Lb0EEEEEvOT_
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__throw_bad_optional_accessB8ne200100Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI15ARTexturedPlaneEEPS3_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN5arkit16BoundingBoxGroupEEEPS4_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIxNS2_IxEEEEEEPS5_EEED2B8ne200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorI15ARTexturedPlaneEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN3cva6MatrixIfLj1ELj0ELb0EEEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorIN5arkit16BoundingBoxGroupEEEPS3_EEvRT_T0_S8_S8_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne200100INS_9allocatorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEEEEPS6_EEvRT_T0_SB_SB_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorIxNS1_IxEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__13mapINS_5arrayIhLm16EEE15ARTexturedPlaneNS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEE6insertB8ne200100INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS2_S3_EEPNS_11__tree_nodeISG_PvEElEEEEEEvT_SN_
+ __ZNSt3__13mapINS_5arrayIhLm16EEE15ARTexturedPlaneNS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEEC2B8ne200100ERKSB_
+ __ZNSt3__13setINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEE6insertB8ne200100INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEEvT_SF_
+ __ZNSt3__13setINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEEC2B8ne200100ERKS7_
+ __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEE6insertB8ne200100INS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEEEEvT_SD_
+ __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEEC2B8ne200100ERKS5_
+ __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne200100IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_
+ __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne200100IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_.cold.1
+ __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne200100IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_.cold.2
+ __ZNSt3__14pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEC2B8ne200100IfNS1_9MatrixRefIfLj1ELj0ELb0EEELi0EEEONS0_IT_T0_EE
+ __ZNSt3__15dequeINS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS5_EEE26__maybe_remove_front_spareB8ne200100Eb
+ __ZNSt3__15dequeINS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS5_EEED2B8ne200100Ev
+ __ZNSt3__15dequeINS_4pairIiiEENS_9allocatorIS2_EEED2B8ne200100Ev
+ __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEE25__maybe_remove_back_spareB8ne200100Eb
+ __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEED2B8ne200100Ev
+ __ZNSt3__16__treeINS_12__value_typeINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_19__map_value_compareIS3_S5_NS_4lessIS3_EELb1EEENS_9allocatorIS5_EEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__16__treeINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEE18_DetachedTreeCacheD2B8ne200100Ev
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI11AlignedPoseNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEED1B8ne200100Ev
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE22__base_destruct_at_endB8ne200100EPS1_
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE22__construct_one_at_endB8ne200100IJRKS1_EEEvDpOT_
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorI17espresso_buffer_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorI18__ARC3DShapeVertexNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEED1B8ne200100Ev
+ __ZNSt3__16vectorI5edge3IxENS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI5edge3IxENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI5edge3IxENS_9allocatorIS2_EEEC2B8ne200100Em
+ __ZNSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE9push_backB8ne200100EOS1_
+ __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPKS1_S7_EEvT_T0_m
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE18__assign_with_sizeB8ne200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE9push_backB8ne200100EOS1_
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEEC2B8ne200100Em
+ __ZNSt3__16vectorIDv4_hNS_9allocatorIS1_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorIDv4_hNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv4_tNS_9allocatorIS1_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
+ __ZNSt3__16vectorIDv4_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIfLj1ELj0ELb0EEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIfLj1ELj0ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroup7ElementENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIN5arkit7IntRectENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE9push_backB8ne200100EOS5_
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEEC2B8ne200100EmRKS3_
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE22__construct_one_at_endB8ne200100IJRKS3_EEEvDpOT_
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE9push_backB8ne200100EOS3_
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEEC2B8ne200100EmRKS3_
+ __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE9push_backB8ne200100ERKS4_
+ __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne200100Em
+ __ZNSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEEC2B8ne200100Em
+ __ZNSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE24__emplace_back_slow_pathIJS5_EEEPS5_DpOT_
+ __ZNSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP19__CVPixelBufferPoolNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPKS2_S8_EEvT_T0_m
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEED1B8ne200100Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne200100IPdS5_EEvT_T0_m
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB8ne200100EOd
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne200100EmRKd
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPKfS6_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100EOf
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE9push_backB8ne200100ERKf
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPhS5_EEvT_T0_m
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB8ne200100IPhS5_EEvT_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPhEES7_EES7_NS5_IPKhEET_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE9push_backB8ne200100EOh
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne200100IPiS5_EEvT_T0_m
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100ERKi
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne200100EmRKi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8ne200100IPmS5_EEvT_T0_l
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B8ne200100Em
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE16__init_with_sizeB8ne200100IPKsS6_EEvT_T0_m
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE18__assign_with_sizeB8ne200100IPKsS6_EEvT_T0_l
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE9push_backB8ne200100EOs
+ __ZNSt3__16vectorIsNS_9allocatorIsEEEC2B8ne200100Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne200100IPxS5_EEvT_T0_m
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE18__assign_with_sizeB8ne200100IPxS5_EEvT_T0_l
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B8ne200100Em
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne200100IPyS5_EEvT_T0_m
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100EOy
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100ERKy
+ __ZNSt3__16vectorIyNS_9allocatorIyEEEC2B8ne200100Em
+ __ZNSt3__17getlineB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
+ __ZNSt3__18__rotateB8ne200100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN5arkit7IntRectEEES6_EENS_4pairIT0_S8_EES8_S8_T1_
+ __ZNSt3__18optionalIN3cva6MatrixIfLj9ELj1ELb0EEEEaSB8ne200100INS1_16MatrixBinaryExprINS1_16MatrixScalarExprIS3_NS1_6detail5MulOpEEESA_NS8_5AddOpEEEvEERS4_OT_
+ __ZNSt3__19allocatorI11AlignedPoseE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI13simd_float4x4E17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI15ARTexturedPlaneE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI17espresso_buffer_tE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI18CV3DHitTestPoint3DE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI18__ARC3DShapeVertexE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI23CV3DHitTestCovariance3DE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI27CV3DSurfaceDetectionPoint3DE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI5ARSRTE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI5edge3IxEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorI7ARPatchE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIDv2_fE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIDv3_fE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIDv4_hE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIDv4_tE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN3cva6MatrixIfLj1ELj0ELb0EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN3cva6MatrixIfLj2ELj1ELb0EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN3cva6MatrixIfLj3ELj1ELb0EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN3cva6MatrixIjLj2ELj1ELb0EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN3cva6MatrixIjLj3ELj1ELb0EEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN5arkit16BoundingBoxGroup7ElementEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN5arkit16BoundingBoxGroupEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN5arkit7IntRectEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIN5arkit8LandmarkEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_10shared_ptrIK20CV3DSLAMStateContextEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4listI4edgeIxENS0_IS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4listI5edge0IxENS0_IS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4listI5edge1IxENS0_IS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4listI5edge2IxENS0_IS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4pairI7Pos4DofS2_EEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_6vectorINS1_IfNS0_IfEEEENS0_IS3_EEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_6vectorIdNS0_IdEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_6vectorIfNS0_IfEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorINS_6vectorIxNS0_IxEEEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP10__CVBufferE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIP19__CVPixelBufferPoolE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPKcE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPNS_4pairIiiEEE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIPPKvE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIdE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIfE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIiE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorImE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIsE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIxE17allocate_at_leastB8ne200100Em
+ __ZNSt3__19allocatorIyE17allocate_at_leastB8ne200100Em
+ __ZNSt3__1rsB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZZ26GetCV3DSLAMCameraModelTypevE15cameraModelType
+ __ZZ26GetCV3DSLAMCameraModelTypevE9onceToken
+ ___121-[ARPersonSegmentationTechnique runNeuralNetworkWithImageData:originalImageData:regionOfInterest:rotationOfResultTensor:]_block_invoke.26
+ ___143+[ARVideoFormat _supportedVideoFormatsForDevicePosition:deviceType:resolutions:frameRatesByPowerUsage:videoBinned:pixelFormat:needsHDRSupport:]_block_invoke
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.38
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.39
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.42
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.59
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.63
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.67
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.71
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.83
+ ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke_2.43
+ ___169-[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:]_block_invoke
+ ___169-[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:]_block_invoke_2
+ ___18-[ARQATracer stop]_block_invoke.84
+ ___28-[ARRemoteService reconnect]_block_invoke.76
+ ___37-[ARFrameUpdateTimer _storeNewFrame:]_block_invoke
+ ___37-[ARSceneDepthTechnique processData:]_block_invoke
+ ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke.465
+ ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_2.469
+ ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_3.470
+ ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_4.475
+ ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_5.476
+ ___39+[ARWorldTrackingTechnique isSupported]_block_invoke.cold.1
+ ___39-[ARNonSynchronousData arMLDepthResult]_block_invoke
+ ___40-[ARSession sensor:didOutputSensorData:]_block_invoke_3
+ ___40-[ARSession sensor:didOutputSensorData:]_block_invoke_4
+ ___40-[ARWorldTrackingTechnique processData:]_block_invoke.124
+ ___40-[ARWorldTrackingTechnique processData:]_block_invoke_2
+ ___42-[ARSession runWithConfiguration:options:]_block_invoke.43
+ ___44-[ARRemoteService _startServiceSynchronous:]_block_invoke
+ ___44-[ARRemoteService _startServiceSynchronous:]_block_invoke.67
+ ___44-[ARRemoteService _startServiceSynchronous:]_block_invoke.cold.1
+ ___44-[ARRemoteService _startServiceSynchronous:]_block_invoke.cold.2
+ ___44-[ARSessionMetrics _processFrameProperties:]_block_invoke.449
+ ___45+[ARSession _applySessionOverrides:outError:]_block_invoke.462
+ ___46-[ARRemoteService serviceConfiguredWithError:]_block_invoke.84
+ ___46-[ARRemoteService serviceConfiguredWithError:]_block_invoke.84.cold.1
+ ___48-[ARSession _sessionShouldAttemptRelocalization]_block_invoke.508
+ ___51+[ARTechnique techniqueConformsToProtocol:inArray:]_block_invoke
+ ___51+[ARVideoFormat photoQualityPrioritizationOverride]_block_invoke
+ ___54-[ARSession getGeoLocationForPoint:completionHandler:]_block_invoke.237
+ ___56-[ARSession _updateAnchorsForFrame:resultDatas:context:]_block_invoke
+ ___57-[ARInFrameAnchorVisualizer drawOriginAndAnchorsOnFrame:]_block_invoke
+ ___57-[ARInFrameAnchorVisualizer drawOriginAndAnchorsOnFrame:]_block_invoke_2
+ ___57-[ARNonSynchronousData segmentationResultWithDataSource:]_block_invoke
+ ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.308
+ ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.309
+ ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.196
+ ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.197
+ ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.199
+ ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.203
+ ___63-[ARFrameUpdateTimer _startExecutorWithFrameRate:initialDelay:]_block_invoke
+ ___63-[ARRemoteService createDispatchChannelWithRequest:completion:]_block_invoke
+ ___63-[ARRemoteService createDispatchChannelWithRequest:completion:]_block_invoke.96
+ ___63-[ARRemoteService createDispatchChannelWithRequest:completion:]_block_invoke.cold.1
+ ___63-[ARWorldTrackingTechnique didReceiveKeyframesUpdatedCallback:]_block_invoke.172
+ ___67-[ARDispatchSourceExecutor executeWithInterval:initialDelay:block:]_block_invoke
+ ___68-[ARSceneDepthTechnique _generateDepthForDownscaledImageData:error:]_block_invoke
+ ___68-[ARSceneDepthTechnique _generateDepthForDownscaledImageData:error:]_block_invoke.32
+ ___68-[ARSceneDepthTechnique _generateDepthForDownscaledImageData:error:]_block_invoke_2
+ ___69-[ARSceneDepthTechnique waitForProcessingCompleteInDeterministicMode]_block_invoke
+ ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke
+ ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke.466
+ ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke_2
+ ___69-[ARSession captureHighResolutionFrameUsingPhotoSettings:completion:]_block_invoke_3
+ ___70-[ARParentImageSensor captureDeviceTypeToExtrinsicsMapForImageSensor:]_block_invoke
+ ___70-[ARParentImageSensor captureDeviceTypeToExtrinsicsMapForImageSensor:]_block_invoke_2
+ ___71-[ARSession _populateRawSceneUnderstandingDataForFrame:fromResultData:]_block_invoke
+ ___71-[ARSession _populateRawSceneUnderstandingDataForFrame:fromResultData:]_block_invoke_2
+ ___71-[ARSession _populateRawSceneUnderstandingDataForFrame:fromResultData:]_block_invoke_3
+ ___72-[ARSceneDepthTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]_block_invoke
+ ___77-[ARSession _setPrimaryTechnique:secondaryTechnique:stillImageRootTechnique:]_block_invoke
+ ___77-[ARWorldTrackingTechnique _updatePoseData:forTimeStamp:updateTrackingState:]_block_invoke.219
+ ___79-[ARMLImageProcessingTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]_block_invoke
+ ___80-[ARWorldTrackingTechnique _postProcessNonSynchronousDataForSceneUnderstanding:]_block_invoke
+ ___80-[ARWorldTrackingTechnique _postProcessNonSynchronousDataForSceneUnderstanding:]_block_invoke_2
+ ___80-[ARWorldTrackingTechnique _postProcessNonSynchronousDataForSceneUnderstanding:]_block_invoke_3
+ ___80-[ARWorldTrackingTechnique _postProcessNonSynchronousDataForSceneUnderstanding:]_block_invoke_4
+ ___83-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:]_block_invoke
+ ___83-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:]_block_invoke_2
+ ___83-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:]_block_invoke_3
+ ___83-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:withTimeout:]_block_invoke_4
+ ___84-[ARMLImageMattingMetadataTechnique pushEmptyResultOnAsynchronousQueueForTimestamp:]_block_invoke
+ ___ARBackWidePhotoQualityPrioritizationOverride_block_invoke
+ ___ARCreateCVPixelBufferFromPoolWithZeroCopyOption_block_invoke
+ ___ARDeviceSupported_block_invoke.cold.1
+ ___ARInstrumentsValueFromFrameVendReason_block_invoke
+ ___ARIsIntelMac_block_invoke
+ ___ARKitDaemonBundle_block_invoke
+ ___ARLinkedOnOrAfterConstellationE_block_invoke
+ ___ARLinkedOnOrAfterDawn_block_invoke
+ ___ARLinkedOnOrAfterLuck_block_invoke
+ ___ARLinkedOnOrAfterVisionOS_3_0_block_invoke
+ ___AROSAllowsInternalSecurityPolicies_block_invoke
+ ___AROSHasInternalUI_block_invoke
+ ___DrawOntoPixelBufferBGRA_block_invoke
+ ____Z26GetCV3DSLAMCameraModelTypev_block_invoke
+ ___block_descriptor_32_e23_16?0"ARImageSensor"8l
+ ___block_descriptor_32_e29_q24?0"ARFrame"8"ARFrame"16l
+ ___block_descriptor_32_e29_q24?0"NSArray"8"NSArray"16l
+ ___block_descriptor_32_e32_B32?0"AVCaptureDevice"8Q16^B24l
+ ___block_descriptor_40_e35_B32?0"ARSegmentationData"8Q16^B24l
+ ___block_descriptor_40_e8_32w_e15_v28?0^v8Q16I24lw32l8
+ ___block_descriptor_48_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_ea8_32w_e5_v8?0lw32l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_72_e8_32r40r48r56r64r_e5_v8?0lr32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_96_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.103
+ ___block_literal_global.105
+ ___block_literal_global.113
+ ___block_literal_global.124
+ ___block_literal_global.134
+ ___block_literal_global.136
+ ___block_literal_global.140
+ ___block_literal_global.144
+ ___block_literal_global.148
+ ___block_literal_global.152
+ ___block_literal_global.157
+ ___block_literal_global.167
+ ___block_literal_global.168
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.208
+ ___block_literal_global.212
+ ___block_literal_global.215
+ ___block_literal_global.229
+ ___block_literal_global.237
+ ___block_literal_global.240
+ ___block_literal_global.252
+ ___block_literal_global.255
+ ___block_literal_global.258
+ ___block_literal_global.262
+ ___block_literal_global.277
+ ___block_literal_global.284
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.296
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.313
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.378
+ ___block_literal_global.384
+ ___block_literal_global.388
+ ___block_literal_global.390
+ ___block_literal_global.393
+ ___block_literal_global.395
+ ___block_literal_global.416
+ ___block_literal_global.420
+ ___block_literal_global.422
+ ___block_literal_global.425
+ ___block_literal_global.450
+ ___block_literal_global.454
+ ___block_literal_global.456
+ ___block_literal_global.474
+ ___block_literal_global.476
+ ___block_literal_global.478
+ ___block_literal_global.484
+ ___block_literal_global.512
+ ___block_literal_global.513
+ ___block_literal_global.516
+ ___block_literal_global.518
+ ___block_literal_global.533
+ ___block_literal_global.576
+ ___block_literal_global.579
+ ___block_literal_global.582
+ ___block_literal_global.586
+ ___block_literal_global.611
+ ___block_literal_global.625
+ ___block_literal_global.633
+ ___block_literal_global.81
+ ___block_literal_global.85
+ ___block_literal_global.928
+ ___block_literal_global.932
+ ___block_literal_global.934
+ ___block_literal_global.937
+ ___block_literal_global.97
+ __createADError
+ __createAllocationError
+ __createPoolAllocationError
+ __createResamplingError
+ __isPointCloudBlackened
+ _abort_with_reason
+ _backtrace
+ _channel_dispatch_activate
+ _channel_dispatch_create_from_request
+ _channel_dispatch_set_cancel_handler
+ _channel_dispatch_set_message_handler
+ _channel_rt_create_from_request
+ _dispatch_workloop_set_scheduler_priority
+ _dladdr
+ _kCGColorSpaceSRGB
+ _kCV3DSLAMAnchorAddedResultGroupNotAuthorized
+ _kCV3DSLAMAnchorAddedResultMaxNRAreasReached
+ _kCV3DSLAMAnchorAddedResultNRAnchorNotPermitted
+ _kCV3DSLAMCMDataValueTypeMLFrameSet
+ _kCV3DSLAMCMDataValueTypeSubmapsStatsInfo
+ _kCVPixelBufferPoolAllocationThresholdKey
+ _objc_msgSend$_changePowerUsage:
+ _objc_msgSend$_compensationMatrixForBravoSession
+ _objc_msgSend$_compensationMatrixForTrackingCameraID:
+ _objc_msgSend$_compensationMatrixForWidePlusUWSessionAndTrackingCameraID:
+ _objc_msgSend$_createTechniques:forStillImage:
+ _objc_msgSend$_frameDuration
+ _objc_msgSend$_frameUpdateTick
+ _objc_msgSend$_generateDepthForDownscaledImageData:error:
+ _objc_msgSend$_geoTrackingPublicStatusChangedFromLastVendedFrameToFrame:
+ _objc_msgSend$_getCameraCalibration:rotation:inputDimensions:
+ _objc_msgSend$_isBeforeFirstTimerTick
+ _objc_msgSend$_latencyIsTooHighForFrame:
+ _objc_msgSend$_latencyIsTooLowForFrame:
+ _objc_msgSend$_logTechniqueGraphForDebugging
+ _objc_msgSend$_logTechniqueState:state:data:
+ _objc_msgSend$_pollRawOrientation
+ _objc_msgSend$_populateRawSceneUnderstandingDataForFrame:fromResultData:
+ _objc_msgSend$_postProcessNonSynchronousDataForSceneUnderstanding:
+ _objc_msgSend$_preferredRenderFrameRateForCaptureFrameRate:isNominalPower:
+ _objc_msgSend$_preferredRenderSyncFrameRateForCaptureFrameRate:
+ _objc_msgSend$_prepareOnDimensionsChange:outputRotation:error:
+ _objc_msgSend$_prepareOnce
+ _objc_msgSend$_rotatedPixelBufferImageData:rotationAngle:
+ _objc_msgSend$_safeProcessData:
+ _objc_msgSend$_saveExtrinsicsForBravoCamSessionFromImage:
+ _objc_msgSend$_saveExtrinsicsForWidePlusUWSessionFromImage:
+ _objc_msgSend$_saveExtrinsicsFromImage:
+ _objc_msgSend$_sessionType
+ _objc_msgSend$_setInternalConfiguration:
+ _objc_msgSend$_setPrimaryTechnique:secondaryTechnique:stillImageRootTechnique:
+ _objc_msgSend$_start
+ _objc_msgSend$_startExecutorWithFrameRate:initialDelay:
+ _objc_msgSend$_startSensorsWithDataTypes:
+ _objc_msgSend$_startServiceSynchronous:
+ _objc_msgSend$_storeNewFrame:
+ _objc_msgSend$_supportedVideoFormatsForDevicePosition:deviceType:resolutions:frameRatesByPowerUsage:videoBinned:pixelFormat:needsHDRSupport:
+ _objc_msgSend$_timeSinceFrameWasScheduled:
+ _objc_msgSend$_timeTillNextTimerTick
+ _objc_msgSend$_trackingStateChangedFromLastVendedFrameToFrame:
+ _objc_msgSend$_unvendedFramesCount
+ _objc_msgSend$_updateAnchorsForFrame:resultDatas:context:
+ _objc_msgSend$_updateExecutorForFrameRate:
+ _objc_msgSend$_updateThermalStateFromCurrentProcessInfo
+ _objc_msgSend$_vendFrame:withReason:
+ _objc_msgSend$_vendFrameIfAtLastTickNoFrameWasVended
+ _objc_msgSend$_vendFramesIfTooManyFramesAreQueued
+ _objc_msgSend$_vendFramesThatExceedTheMaximumLatency
+ _objc_msgSend$anchorChangeSet
+ _objc_msgSend$arMLDepthResult
+ _objc_msgSend$baseAddress
+ _objc_msgSend$bytesPerElement
+ _objc_msgSend$bytesPerRow
+ _objc_msgSend$captureHighResolutionFrameUsingPhotoSettings:completion:
+ _objc_msgSend$channel
+ _objc_msgSend$clearPreviousContext
+ _objc_msgSend$color
+ _objc_msgSend$configurationForPublicGetter
+ _objc_msgSend$constituentDevices
+ _objc_msgSend$convertPixelBuffer:toFormat:
+ _objc_msgSend$currentFramesPerSecond
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$defaultColorSpace
+ _objc_msgSend$defaultLoggerWithName:
+ _objc_msgSend$defaultPhotoSettings
+ _objc_msgSend$disableTemporalSegmentation
+ _objc_msgSend$dispatchChannelQueue
+ _objc_msgSend$dotGraphWithLines:rootName:
+ _objc_msgSend$drawOriginAndAnchorsOnFrame:
+ _objc_msgSend$elementHeight
+ _objc_msgSend$elementWidth
+ _objc_msgSend$executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:
+ _objc_msgSend$executeWithInterval:initialDelay:block:
+ _objc_msgSend$executorParameters
+ _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:
+ _objc_msgSend$gatheredDataWasAlreadyCaptured
+ _objc_msgSend$handleDispatchChannelMessage:size:type:
+ _objc_msgSend$imageWithCVPixelBuffer:
+ _objc_msgSend$initWithAddedAnchors:updatedAnchors:removedAnchors:externalAnchors:
+ _objc_msgSend$initWithDaemon:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:
+ _objc_msgSend$initWithDispatchChannelQueue:fixedPriorityQueueForXPC:
+ _objc_msgSend$initWithIdentifier:type:
+ _objc_msgSend$initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:
+ _objc_msgSend$initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:fixedPriorityQueueForXPC:
+ _objc_msgSend$initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:
+ _objc_msgSend$initWithPosition:size:color:
+ _objc_msgSend$initWithTimeProvider:executor:
+ _objc_msgSend$initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:
+ _objc_msgSend$instanceMethodForSelector:
+ _objc_msgSend$internalDepthSettings
+ _objc_msgSend$internalSettings
+ _objc_msgSend$isActive
+ _objc_msgSend$isBackUltraWide
+ _objc_msgSend$isComplete
+ _objc_msgSend$isDeferredStartEnabled
+ _objc_msgSend$isDeferredStartSupported
+ _objc_msgSend$isDroppedData
+ _objc_msgSend$lockWithOptions:seed:
+ _objc_msgSend$logPixelBuffer:name:timestamp:
+ _objc_msgSend$logger
+ _objc_msgSend$minLatency
+ _objc_msgSend$numberOfInFlightContexts
+ _objc_msgSend$pipeline
+ _objc_msgSend$planeCount
+ _objc_msgSend$pointCount
+ _objc_msgSend$prepareForEngineType:roi:exifOrientation:rotationPreference:
+ _objc_msgSend$prepareWasCalled
+ _objc_msgSend$pushEmptyResultOnAsynchronousQueueForTimestamp:
+ _objc_msgSend$recipientIdentifiers
+ _objc_msgSend$referenceImageUUIDForPixelBuffer:
+ _objc_msgSend$removeDataWithPath:
+ _objc_msgSend$replayFailedBlock
+ _objc_msgSend$replayStartedBlock
+ _objc_msgSend$replayStoppedBlock
+ _objc_msgSend$replayUpdatedBlock
+ _objc_msgSend$requestResultDataAtTimestamp:context:onTechniques:withTimeout:
+ _objc_msgSend$requestResultDataAtTimestamp:context:withTimeout:
+ _objc_msgSend$resolutionForKey:resultingDimensions:
+ _objc_msgSend$scaleAllowStretch:
+ _objc_msgSend$sceneDepthTechniqueForPrioritization:temporalSmoothing:
+ _objc_msgSend$scheduleFrame:captureFramesPerSecond:
+ _objc_msgSend$scheduledTimestamp
+ _objc_msgSend$segmentationResultWithDataSource:
+ _objc_msgSend$serviceDidConfigureBlock
+ _objc_msgSend$setAnchorChangeSet:
+ _objc_msgSend$setBufferCopyPolicy:
+ _objc_msgSend$setChannel:
+ _objc_msgSend$setConfigurationForPublicGetter:
+ _objc_msgSend$setDeferredStartEnabled:
+ _objc_msgSend$setDisableTemporalSegmentation:
+ _objc_msgSend$setDispatchChannelQueue:
+ _objc_msgSend$setIgnoreDistortionInDepthReprojection:
+ _objc_msgSend$setIntrinsicMatrix:
+ _objc_msgSend$setIsDroppedData:
+ _objc_msgSend$setIsMultiSessionMode:
+ _objc_msgSend$setMovieFragmentInterval:
+ _objc_msgSend$setPassive:
+ _objc_msgSend$setPixelSize:
+ _objc_msgSend$setPreferredFrameRateRange:
+ _objc_msgSend$setReferenceDimensions:
+ _objc_msgSend$setScheduledTimestamp:
+ _objc_msgSend$setServiceDidConfigureBlock:
+ _objc_msgSend$setServiceDidUpdateDataAccessBlock:
+ _objc_msgSend$setStillImageRootTechnique:
+ _objc_msgSend$setStillRequiresPostProcessing:
+ _objc_msgSend$setTemporalConsistencyMethod:
+ _objc_msgSend$setupCompleteForRTChannel
+ _objc_msgSend$sortDescriptorWithKey:ascending:comparator:
+ _objc_msgSend$sortedArrayUsingDescriptors:
+ _objc_msgSend$spotIdentifiers
+ _objc_msgSend$stillImageRootTechnique
+ _objc_msgSend$stillRequiresPostProcessing
+ _objc_msgSend$submitResultsForTimestamp:context:
+ _objc_msgSend$supportedColorSpaces
+ _objc_msgSend$targetTimestamp
+ _objc_msgSend$techniqueConformsToProtocol:
+ _objc_msgSend$techniqueConformsToProtocol:inArray:
+ _objc_msgSend$techniqueInArray:passingTest:
+ _objc_msgSend$techniqueLevel
+ _objc_msgSend$techniquesForStillImageGraph
+ _objc_msgSend$timeSinceSnapshot:
+ _objc_msgSend$timeoutForNextFrameUpdateWithNumberOfInFlightContexts:
+ _objc_msgSend$timerDidVendFrame:
+ _objc_msgSend$toJSONWithRootName:
+ _objc_msgSend$transformAnchorToPlaneAnchorConvention:
+ _objc_msgSend$unlockWithOptions:seed:
+ _objc_msgSend$upTime
+ _objc_msgSend$upTimeIncludingSleep
+ _objc_msgSend$upTimeIncludingSleepAndDriftCorrection
+ _objc_msgSend$useFrameUpdateTimer
+ _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingPoseDelta:previousCalibration:currentCalibration:
+ _objc_msgSend$wrapperWithDictionary:
+ _objc_msgSend$writeToFile:atomically:
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_ui
+ _photoQualityPrioritizationOverride.onceToken
+ _photoQualityPrioritizationOverride.override
+ _uname
+ _usleep
+ _vImageOverwriteChannelsWithScalar_ARGB8888
+ _xpc_dictionary_create
+ _xpc_dictionary_get_uint64
- +[ARAreaLight supportsSecureCoding]
- +[ARImageSensor maxPhotoDimensionsForVideoFormat:maximumHeight:]
- +[ARImageSensor maxPhotoDimensionsForVideoFormat:maximumHeight:].cold.1
- +[ARKitUserDefaults resolutionDictionaryForKey:]
- +[ARObjectTrackingRemoteControl serviceName]
- +[ARParametricLights supportsSecureCoding]
- +[ARParentTechnique techinqueInArray:passingTest:]
- +[ARPlaneWorld findMergedPlanes::]
- +[ARPositionalTrackingConfiguration _querySupportedVideoFormats].cold.2
- -[ARAreaLight angularSize]
- -[ARAreaLight color]
- -[ARAreaLight direction]
- -[ARAreaLight encodeWithCoder:]
- -[ARAreaLight initWithCoder:]
- -[ARAreaLight initWithDirection:angularSize:color:]
- -[ARCamera initWithIntrinsics:imageResolution:devicePosition:lensType:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:]
- -[ARCamera lensType]
- -[ARCamera setLensType:]
- -[ARDepthMapData depthMap]
- -[ARDepthMapData setDepthMap:]
- -[ARDepthSensor mutableDepthSettings]
- -[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:].cold.15
- -[AREnvironmentProbeAnchor parametricLights]
- -[AREnvironmentProbeAnchor setParametricLights:]
- -[ARFrame depthMap]
- -[ARFrame estimatedLuminance]
- -[ARFrame setDepthMap:]
- -[ARFrame setEstimatedLuminance:]
- -[ARImageData lensType]
- -[ARImageData setLensType:]
- -[ARImageSensor _defaultPhotoSettings]
- -[ARImageSensor forceUpdatePowerUsage:]
- -[ARImageSensor forceUpdatePowerUsage:].cold.1
- -[ARImageSensor mutableSettings]
- -[ARMLImageDownScalingTechnique requestResultDataAtTimestamp:context:]
- -[ARMLImageDownScalingTechnique setShouldOperateOnHighResolutionImages:]
- -[ARMLImageDownScalingTechnique shouldOperateOnHighResolutionImages]
- -[ARMLImageMattingMetadataTechnique isEqual:]
- -[ARMLImageMattingMetadataTechnique requestResultDataAtTimestamp:context:]
- -[ARMLImageMattingMetadataTechnique setShouldOperateOnHighResolutionImages:]
- -[ARMLImageMattingMetadataTechnique shouldOperateOnHighResolutionImages]
- -[ARParametricLights .cxx_destruct]
- -[ARParametricLights ambientColor]
- -[ARParametricLights areaLights]
- -[ARParametricLights encodeWithCoder:]
- -[ARParametricLights initWithAmbientColor:areaLights:]
- -[ARParametricLights initWithCoder:]
- -[ARParentImageSensor forceUpdatePowerUsage:]
- -[ARParentTechnique _submitResultsForTimestamp:context:]
- -[ARParentTechnique optionalSensorDataTypes]
- -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:].cold.1
- -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:].cold.2
- -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:].cold.3
- -[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:].cold.4
- -[ARParentTechnique(DotGraph) dotGraphWithLines:]
- -[ARPersonSegmentationTechnique _prepareOnce:].cold.3
- -[ARPersonSegmentationTechnique processData:]
- -[ARPersonSegmentationTechnique requestResultDataAtTimestamp:context:]
- -[ARPersonSegmentationTechnique setShouldOperateOnHighResolutionImages:]
- -[ARPersonSegmentationTechnique shouldOperateOnHighResolutionImages]
- -[ARRemoteService _serverConnectionInterrupted]
- -[ARRemoteService didSetWorldOrigin]
- -[ARRemoteService initWithDaemon:startConnection:dispatchChannelQueue:]
- -[ARRemoteService initWithDispatchChannelQueue:]
- -[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:]
- -[ARSISemanticSegmentationTechnique _prepareOnce:].cold.5
- -[ARSISemanticSegmentationTechnique _prepareOnce:].cold.6
- -[ARSession _changePowerUsage:forced:]
- -[ARSession _exposeInternalDepthData]
- -[ARSession _exposeInternalDepthData].cold.1
- -[ARSession _setPrimaryTechnique:secondaryTechnique:]
- -[ARSession _startSensorsWithRequiredDataTypes:optionalDataTypes:]
- -[ARSession _startSensorsWithRequiredDataTypes:optionalDataTypes:].cold.1
- -[ARSession _updateAnchorsForFrame:resultDatas:context:addedAnchors:updatedAnchors:removedAnchors:externalAnchors:]
- -[ARSession _updateAnchorsForFrame:resultDatas:context:addedAnchors:updatedAnchors:removedAnchors:externalAnchors:].cold.1
- -[ARSession _updatePowerUsageForced:]
- -[ARSession _updateThermalState:]
- -[ARTechnique optionalSensorDataTypes]
- -[ARTechnique(DotGraph) dotGraphWithLines:]
- -[ARTechniqueSequentialGatherContext mergeResultsOfContext:resultFilterBlock:]
- -[ARWorldAlignmentTechnique optionalSensorDataTypes]
- -[ARWorldTrackingTechnique _isBravoCamOtherThanWideUsed]
- -[ARWorldTrackingTechnique extrinsicsToWideSensor]
- -[ARWorldTrackingTechnique setExtrinsicsToWideSensor:]
- GCC_except_table104
- GCC_except_table109
- GCC_except_table110
- GCC_except_table112
- GCC_except_table123
- GCC_except_table128
- GCC_except_table130
- GCC_except_table133
- GCC_except_table142
- GCC_except_table145
- GCC_except_table146
- GCC_except_table149
- GCC_except_table150
- GCC_except_table154
- GCC_except_table158
- GCC_except_table161
- GCC_except_table167
- GCC_except_table169
- GCC_except_table76
- _ARAVCaptureDevicePositionToString
- _ARAddScalingTechniquesToTechniques
- _ARAnchorsFromCV3DAnchorsArray.cold.5
- _ARConfigurationShouldProvideNonBinnedVideoFormatsUserDefaultsKey
- _ARCreateTemporaryDirectory
- _ARCreateTransactionForService
- _ARDepthSPIApprovedBundleIDPrefix
- _ARDeviceRequiresFrameTrendControllerWorkaround
- _ARDeviceSupportsSceneLuminanceEstimation
- _AREstimatedSceneLuminanceForCamera
- _ARFileDescriptorIsTTY
- _ARFileDescriptorIsTTY.cold.1
- _ARFileDescriptorIsTTY.isSSHTTY
- _ARFileDescriptorIsTTY.onceToken
- _ARGeoTrackingUseCMFusionUserDefaultsKey
- _ARGetLensTypeFromCalibrationDictionary
- _ARGetLensTypeFromCalibrationDictionary.cold.1
- _ARIsAirPlaneModeEnabled
- _ARLinkedOnOrAfterCrystal
- _ARLinkedOnOrAfterCrystal.cachedReturn
- _ARLinkedOnOrAfterCrystal.cold.1
- _ARLinkedOnOrAfterCrystal.onceToken
- _ARLinkedOnOrAfterPeaceE
- _ARLinkedOnOrAfterPeaceE.cachedReturn
- _ARLinkedOnOrAfterPeaceE.cold.1
- _ARLinkedOnOrAfterPeaceE.onceToken
- _ARLoadExternalBundleByName
- _ARMLModelPath
- _ARObjectTrackingInternalErrorCodeIsTransientError
- _ARObjectTrackingInternalErrorCodeShouldStopProvider
- _ARPlaneEstimationAnchorRotationKey
- _ARPrintColorBlue
- _ARPrintColorBold
- _ARPrintColorBoldRed
- _ARPrintColorBoldUnderlineBlue
- _ARPrintColorGreen
- _ARPrintColorNormal
- _ARPrintColorPurple
- _ARPrintColorRed
- _ARPrintColorYellow
- _ARPrintEscapeDisableAlternativeBuffer
- _ARPrintEscapeEnableAlternativeBuffer
- _ARPrintEscapeEraseScreen
- _ARPrintEscapeMoveToLocation
- _ARPrintToiTerm
- _ARPrintUsageStrings
- _ARReflectedLightMeterCalibrationConstantForDevice
- _ARRequestIDsFromSLAMAnchorUpdate
- _ARSandboxContains
- _ARSandboxDirectories
- _ARTrackingSystemPresentationStyleModal
- _ARTrackingSystemPresentationStyleStatus
- _ARTrackingSystemSymbolRenderingModeMonochrome
- _ARTrackingSystemSymbolRenderingModeMulticolor
- _CV3DPlaneDetectionPlaneCreateTriangulatedPolygons
- _CV3DPlaneDetectionPlaneExtentPolygons
- _CV3DPlaneDetectionPolygonAtIndex
- _CV3DPlaneDetectionPolygonListLength
- _CV3DPlaneDetectionPolygonPointsNum
- _CV3DPlaneDetectionPolygonPointsRawPtr
- _CV3DReconMeshGetFacesRawPtr
- _CV3DVIOIsVideoModeSupported
- _NSErrorFromARObjectTrackingInternalErrorCode
- _NSErrorFromARObjectTrackingInternalErrorCodeAndUserInfo
- _NSErrorFromARObjectTrackingODTError
- _OBJC_CLASS_$_ARAreaLight
- _OBJC_CLASS_$_ARDepthMapData
- _OBJC_CLASS_$_ARObjectTrackingRemoteControl
- _OBJC_CLASS_$_ARParametricLights
- _OBJC_IVAR_$_AR2DSkeletonDetectionPostProcessingTechnique._previous3DSkeletonSemaphore
- _OBJC_IVAR_$_ARAreaLight._angularSize
- _OBJC_IVAR_$_ARAreaLight._color
- _OBJC_IVAR_$_ARAreaLight._direction
- _OBJC_IVAR_$_ARCamera._lensType
- _OBJC_IVAR_$_ARDepthMapData._depthMap
- _OBJC_IVAR_$_ARDepthTechnique._alphamapAvailable
- _OBJC_IVAR_$_ARDepthTechnique._outputAlphaPixelBufferPool
- _OBJC_IVAR_$_ARDepthTechnique._pipelineParameters
- _OBJC_IVAR_$_AREnvironmentProbeAnchor._parametricLights
- _OBJC_IVAR_$_ARFrame._depthMap
- _OBJC_IVAR_$_ARFrame._estimatedLuminance
- _OBJC_IVAR_$_ARImageData._lensType
- _OBJC_IVAR_$_ARLocationSensor._isStopped
- _OBJC_IVAR_$_ARMLImageDownScalingTechnique._shouldOperateOnHighResolutionImages
- _OBJC_IVAR_$_ARMLImageMattingMetadataTechnique._shouldOperateOnHighResolutionImages
- _OBJC_IVAR_$_ARParametricLights._ambientColor
- _OBJC_IVAR_$_ARParametricLights._areaLights
- _OBJC_IVAR_$_ARPersonSegmentationTechnique._shouldOperateOnHighResolutionImages
- _OBJC_IVAR_$_ARPlaneData._applyPivotRotation
- _OBJC_IVAR_$_ARRemoteService._originFromWorld
- _OBJC_IVAR_$_ARRemoteService._worldFromOrigin
- _OBJC_IVAR_$_ARTechniqueParallelGatherContext._gatherLock
- _OBJC_IVAR_$_ARTechniqueParallelGatherContext._resultsCaptured
- _OBJC_IVAR_$_ARWorldTrackingTechnique._extrinsicsToWideSensor
- _OBJC_METACLASS_$_ARAreaLight
- _OBJC_METACLASS_$_ARDepthMapData
- _OBJC_METACLASS_$_ARObjectTrackingRemoteControl
- _OBJC_METACLASS_$_ARParametricLights
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ARPersonDetectionData
- __OBJC_$_CATEGORY_NSDictionary_$_ARPersonDetectionData
- __OBJC_$_CLASS_METHODS_ARAreaLight
- __OBJC_$_CLASS_METHODS_ARObjectTrackingRemoteControl
- __OBJC_$_CLASS_METHODS_ARParametricLights
- __OBJC_$_CLASS_METHODS_ARPlaneWorld
- __OBJC_$_CLASS_PROP_LIST_ARAreaLight
- __OBJC_$_CLASS_PROP_LIST_ARParametricLights
- __OBJC_$_INSTANCE_METHODS_ARAreaLight
- __OBJC_$_INSTANCE_METHODS_ARDepthMapData
- __OBJC_$_INSTANCE_METHODS_ARParametricLights
- __OBJC_$_INSTANCE_VARIABLES_ARAreaLight
- __OBJC_$_INSTANCE_VARIABLES_ARDepthMapData
- __OBJC_$_INSTANCE_VARIABLES_ARParametricLights
- __OBJC_$_PROP_LIST_ARAreaLight
- __OBJC_$_PROP_LIST_ARDepthMapData
- __OBJC_$_PROP_LIST_ARImageSensorData
- __OBJC_$_PROP_LIST_ARParametricLights
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ARImageSensorData
- __OBJC_$_PROTOCOL_METHOD_TYPES_ARImageSensorData
- __OBJC_$_PROTOCOL_REFS_ARImageSensorData
- __OBJC_CLASS_PROTOCOLS_$_ARAreaLight
- __OBJC_CLASS_PROTOCOLS_$_ARDepthMapData
- __OBJC_CLASS_PROTOCOLS_$_ARParametricLights
- __OBJC_CLASS_RO_$_ARAreaLight
- __OBJC_CLASS_RO_$_ARDepthMapData
- __OBJC_CLASS_RO_$_ARObjectTrackingRemoteControl
- __OBJC_CLASS_RO_$_ARParametricLights
- __OBJC_LABEL_PROTOCOL_$_ARImageSensorData
- __OBJC_METACLASS_RO_$_ARAreaLight
- __OBJC_METACLASS_RO_$_ARDepthMapData
- __OBJC_METACLASS_RO_$_ARObjectTrackingRemoteControl
- __OBJC_METACLASS_RO_$_ARParametricLights
- __OBJC_PROTOCOL_$_ARImageSensorData
- __PromotedConst.327
- __PromotedConst.328
- __PromotedConst.58
- __PromotedConst.584
- __PromotedConst.59
- __PromotedConst.60
- __ZL22semanticsLabelForPlanePK23CV3DPlaneDetectionPlaneP14NSMutableArrayIP8NSNumberE
- __ZN12ARNoiseModelD1Ev
- __ZN3cva3SVDINS_6MatrixIfLj0ELj0ELb0EEELb1EED1Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__114default_deleteIKN5arkit14RTFSPContainerEEclB8ne190102EPS3_
- __ZNKSt3__114default_deleteIN5arkit16FaceTrackingDataEEclB8ne190102EPS2_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorIN5arkit16BoundingBoxGroupEEEPS3_EclB8ne190102Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_EclB8ne190102Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIxNS1_IxEEEEEEPS4_EclB8ne190102Ev
- __ZNKSt3__16vectorI11AlignedPoseNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI17espresso_buffer_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI18__ARC3DShapeVertexNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI5edge3IxENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv2_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv4_hNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv4_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN3cva6MatrixIfLj1ELj0ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5arkit16BoundingBoxGroup7ElementENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5arkit7IntRectENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP10__CVBufferNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP19__CVPixelBufferPoolNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt9type_infoeqB8ne190102ERKS_
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110shared_ptrIN5arkit16FaceTrackingDataEEC2B8ne190102IS2_Li0EEEPT_
- __ZNSt3__110shared_ptrIN5arkit19PrecomputedFaceDataEEC2B8ne190102IS2_Li0EEEPT_
- __ZNSt3__110unique_ptrIN5arkit19PrecomputedFaceDataENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
- __ZNSt3__112__rotate_gcdB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN5arkit7IntRectEEEEET0_S7_S7_S7_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__113__fill_n_boolB8ne190102ILb0ENS_6vectorIbNS_9allocatorIbEEEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS6_9size_typeE
- __ZNSt3__113__fill_n_boolB8ne190102ILb1ENS_6vectorIbNS_9allocatorIbEEEEEEvNS_14__bit_iteratorIT0_Lb0EXLi0EEEENS6_9size_typeE
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferI15ARTexturedPlaneRNS_9allocatorIS1_EEE17__destruct_at_endB8ne190102EPS1_
- __ZNSt3__114__split_bufferIN5arkit16BoundingBoxGroupERNS_9allocatorIS2_EEE17__destruct_at_endB8ne190102EPS2_
- __ZNSt3__114__split_bufferINS_10shared_ptrIK20CV3DSLAMStateContextEERNS_9allocatorIS4_EEE5clearB8ne190102Ev
- __ZNSt3__114__split_bufferINS_6vectorINS1_IfNS_9allocatorIfEEEENS2_IS4_EEEERNS2_IS6_EEE5clearB8ne190102Ev
- __ZNSt3__114__split_bufferINS_6vectorIfNS_9allocatorIfEEEERNS2_IS4_EEE17__destruct_at_endB8ne190102EPS4_
- __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS6_EEE10push_frontEOS6_
- __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS6_EEE9push_backEOS6_
- __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEERNS_9allocatorIS6_EEE10push_frontERKS6_
- __ZNSt3__114__split_bufferIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEERNS_9allocatorIS6_EEE9push_backEOS6_
- __ZNSt3__114__split_bufferIPNS_4pairIiiEENS_9allocatorIS3_EEE10push_frontEOS3_
- __ZNSt3__114__split_bufferIPNS_4pairIiiEENS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__114__split_bufferIPNS_4pairIiiEERNS_9allocatorIS3_EEE10push_frontERKS3_
- __ZNSt3__114__split_bufferIPNS_4pairIiiEERNS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE10push_frontEOS3_
- __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE10push_frontERKS3_
- __ZNSt3__114__split_bufferIPPKvNS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__114__split_bufferIPPKvRNS_9allocatorIS3_EEE9push_backEOS3_
- __ZNSt3__114__split_bufferIfRNS_9allocatorIfEEE9push_backEOf
- __ZNSt3__114basic_ifstreamIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__115allocate_sharedB8ne190102I14RaycastSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRU8__strongU13block_pointerFvPK20CV3DRaycastResultMapEbELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I21PlaneDetectionSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102I21PlaneDetectionSessionNS_9allocatorIS1_EEJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListERU8__strongU13block_pointerFvPK37CV3DPlaneDetectionSingleShotPlaneListEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN5arkit12KeyMapBufferIPKvNS_6vectorIhNS_9allocatorIhEEEEEENS6_IS9_EEJiELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN5arkit15RobustExpFilterIfEENS_9allocatorIS3_EEJddddddddELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN5arkit3btr15ScaleCorrection4ImplENS_9allocatorIS4_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne190102IN5arkit3btr15ScaleCorrectionENS_9allocatorIS3_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne190102Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11AlignedPoseEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI13simd_float4x4EEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI15ARTexturedPlaneEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI17espresso_buffer_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI18CV3DHitTestPoint3DEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI18__ARC3DShapeVertexEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI23CV3DHitTestCovariance3DEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI27CV3DSurfaceDetectionPoint3DEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI5ARSRTEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI5edge3IxEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI7ARPatchEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDv2_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDv3_fEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDv4_hEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIDv4_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3cva6MatrixIfLj1ELj0ELb0EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3cva6MatrixIfLj2ELj1ELb0EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3cva6MatrixIfLj3ELj1ELb0EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3cva6MatrixIjLj2ELj1ELb0EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN3cva6MatrixIjLj3ELj1ELb0EEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5arkit16BoundingBoxGroup7ElementEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5arkit16BoundingBoxGroupEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5arkit7IntRectEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN5arkit8LandmarkEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrIK20CV3DSLAMStateContextEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4listI4edgeIxENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4listI5edge0IxENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4listI5edge1IxENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4listI5edge2IxENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairI7Pos4DofS3_EEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIdNS1_IdEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_6vectorIxNS1_IxEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP10__CVBufferEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP19__CVPixelBufferPoolEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKcEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_4pairIiiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocator_destroyB8ne190102INS_9allocatorI15ARTexturedPlaneEENS_16reverse_iteratorIPS2_EES6_EEvRT_T0_T1_
- __ZNSt3__119__allocator_destroyB8ne190102INS_9allocatorI15ARTexturedPlaneEEPS2_S4_EEvRT_T0_T1_
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102ERKNS_12basic_stringIcS2_S4_EEj
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__120__optional_copy_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne190102ERKS8_
- __ZNSt3__120__optional_copy_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EEC2B8ne190102ERKS8_.cold.1
- __ZNSt3__120__shared_ptr_emplaceI14RaycastSessionNS_9allocatorIS1_EEEC2B8ne190102IJRP15CV3DSLAMSessionRU8__strongU13block_pointerFvPK20CV3DRaycastResultMapEbES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI21PlaneDetectionSessionNS_9allocatorIS1_EEEC2B8ne190102IJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListEES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI21PlaneDetectionSessionNS_9allocatorIS1_EEEC2B8ne190102IJRP15CV3DSLAMSessionRK27PlaneDetectionConfigurationRU8__strongU13block_pointerFvPK27CV3DPlaneDetectionPlaneListERU8__strongU13block_pointerFvPK37CV3DPlaneDetectionSingleShotPlaneListEES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN5arkit12KeyMapBufferIPKvNS_6vectorIhNS_9allocatorIhEEEEEENS6_IS9_EEEC2B8ne190102IJiESA_Li0EEESA_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN5arkit15RobustExpFilterIfEENS_9allocatorIS3_EEEC2B8ne190102IJddddddddES5_Li0EEES5_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN5arkit3btr15ScaleCorrectionENS_9allocatorIS3_EEEC2B8ne190102IJES5_Li0EEES5_DpOT_
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__120back_insert_iteratorINS_6vectorIdNS_9allocatorIdEEEEEaSB8ne190102EOd
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIPKvNS_6vectorIhNS1_IhEEEEEEPvEEEEEclB8ne190102EPSB_
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_5arrayIhLm16EEE15ARTexturedPlaneEEPvEEEEEclB8ne190102EPS9_
- __ZNSt3__123__optional_storage_baseIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEELb0EE16__construct_fromB8ne190102IRKNS_20__optional_copy_baseIS7_Lb0EEEEEvOT_
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__throw_bad_optional_accessB8ne190102Ev
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI15ARTexturedPlaneEEPS3_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorIN5arkit16BoundingBoxGroupEEEPS4_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIxNS2_IxEEEEEEPS5_EEED2B8ne190102Ev
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI15ARTexturedPlaneEES2_EEvRT_PT0_S7_S7_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN3cva6MatrixIfLj1ELj0ELb0EEEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorIN5arkit16BoundingBoxGroupEEES3_EEvRT_PT0_S8_S8_
- __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEEEES6_EEvRT_PT0_SB_SB_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIxNS1_IxEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__13mapINS_5arrayIhLm16EEE15ARTexturedPlaneNS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEE6insertB8ne190102INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS2_S3_EEPNS_11__tree_nodeISG_PvEElEEEEEEvT_SN_
- __ZNSt3__13mapINS_5arrayIhLm16EEE15ARTexturedPlaneNS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEEC2B8ne190102ERKSB_
- __ZNSt3__13setINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEE6insertB8ne190102INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEEvT_SF_
- __ZNSt3__13setINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEEC2B8ne190102ERKS7_
- __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEE6insertB8ne190102INS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEEEEvT_SD_
- __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEEC2B8ne190102ERKS5_
- __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne190102IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_
- __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne190102IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_.cold.1
- __ZNSt3__14pairIN3cva6MatrixIfLj9ELj1ELb0EEEfEC2B8ne190102IRNS2_IfLj0ELj1ELb0EEERKfLi0EEEOT_OT0_.cold.2
- __ZNSt3__14pairIRNS_5arrayIhLm16EEER15ARTexturedPlaneEaSB8ne190102IKS2_S4_Li0EEERS6_RKNS0_IT_T0_EE
- __ZNSt3__14pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEC2B8ne190102IfNS1_9MatrixRefIfLj1ELj0ELb0EEELi0EEEONS0_IT_T0_EE
- __ZNSt3__15dequeINS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS5_EEE26__maybe_remove_front_spareB8ne190102Eb
- __ZNSt3__15dequeINS_4pairINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_9allocatorIS5_EEED2B8ne190102Ev
- __ZNSt3__15dequeINS_4pairIiiEENS_9allocatorIS2_EEED2B8ne190102Ev
- __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEE25__maybe_remove_back_spareB8ne190102Eb
- __ZNSt3__15dequeIPKvNS_9allocatorIS2_EEED2B8ne190102Ev
- __ZNSt3__16__treeINS_12__value_typeINS_5arrayIhLm16EEE15ARTexturedPlaneEENS_19__map_value_compareIS3_S5_NS_4lessIS3_EELb1EEENS_9allocatorIS5_EEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__16__treeINS_5arrayIhLm16EEENS_4lessIS2_EENS_9allocatorIS2_EEE18_DetachedTreeCacheD2B8ne190102Ev
- __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPKS1_S7_EEvT_T0_m
- __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEEC1B8ne190102ESt16initializer_listIS1_E
- __ZNSt3__16vectorI13simd_float4x4NS_9allocatorIS1_EEED1B8ne190102Ev
- __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE21__push_back_slow_pathIRKS1_EEPS1_OT_
- __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE22__base_destruct_at_endB8ne190102EPS1_
- __ZNSt3__16vectorI15ARTexturedPlaneNS_9allocatorIS1_EEE22__construct_one_at_endB8ne190102IJRKS1_EEEvDpOT_
- __ZNSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI18CV3DHitTestPoint3DNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI23CV3DHitTestCovariance3DNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI27CV3DSurfaceDetectionPoint3DNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPKS1_S7_EEvT_T0_m
- __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEEC1B8ne190102ESt16initializer_listIS1_E
- __ZNSt3__16vectorI5ARSRTNS_9allocatorIS1_EEED1B8ne190102Ev
- __ZNSt3__16vectorI5edge3IxENS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI5edge3IxENS_9allocatorIS2_EEEC2B8ne190102Em
- __ZNSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorI7ARPatchNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPKS1_S7_EEvT_T0_m
- __ZNSt3__16vectorIDv2_fNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPKS1_S7_EEvT_T0_m
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE18__assign_with_sizeB8ne190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEEC2B8ne190102Em
- __ZNSt3__16vectorIDv4_hNS_9allocatorIS1_EEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorIDv4_tNS_9allocatorIS1_EEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPS1_EES8_EES8_NS6_IPKS1_EET_T0_l
- __ZNSt3__16vectorIN3cva6MatrixIfLj1ELj0ELb0EEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN3cva6MatrixIfLj2ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN3cva6MatrixIfLj3ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN3cva6MatrixIjLj2ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN3cva6MatrixIjLj3ELj1ELb0EEENS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN5arkit16BoundingBoxGroup7ElementENS_9allocatorIS3_EEE12emplace_backIJRKNS1_7IntRectEEEERS3_DpOT_
- __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEPS2_OT_
- __ZNSt3__16vectorIN5arkit16BoundingBoxGroupENS_9allocatorIS2_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIN5arkit8LandmarkENS_9allocatorIS2_EEE21__push_back_slow_pathIRKS2_EEPS2_OT_
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS0_IdNS_9allocatorIdEEEENS1_IS3_EEEC2B8ne190102EmRKS3_
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE21__push_back_slow_pathIRKS3_EEPS3_OT_
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS0_IxNS_9allocatorIxEEEENS1_IS3_EEEC2B8ne190102EmRKS3_
- __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_10shared_ptrIK20CV3DSLAMStateContextEENS_9allocatorIS4_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4listI4edgeIxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4listI5edge0IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4listI5edge1IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4listI5edge2IxENS_9allocatorIS3_EEEENS4_IS6_EEEC2B8ne190102Em
- __ZNSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS_4pairI7Pos4DofS2_EENS_9allocatorIS3_EEEC2B8ne190102Em
- __ZNSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS_4pairIfN3cva6MatrixIfLj1ELj0ELb0EEEEENS_9allocatorIS5_EEE21__push_back_slow_pathIS5_EEPS5_OT_
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEEC1B8ne190102ESt16initializer_listIS2_E
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEED1B8ne190102Ev
- __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne190102IPdS5_EEvT_T0_m
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102EmRKd
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPKfS6_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC1B8ne190102ESt16initializer_listIfE
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB8ne190102IPhS5_EEvT_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne190102INS_11__wrap_iterIPhEES7_EES7_NS5_IPKhEET_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEE16__init_with_sizeB8ne190102IPiS5_EEvT_T0_m
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102Em
- __ZNSt3__16vectorIiNS_9allocatorIiEEEC2B8ne190102EmRKi
- __ZNSt3__16vectorIjNS_9allocatorIjEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIjNS_9allocatorIjEEEC2B8ne190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8ne190102IPmS5_EEvT_T0_l
- __ZNSt3__16vectorImNS_9allocatorImEEEC2B8ne190102Em
- __ZNSt3__16vectorIsNS_9allocatorIsEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIsNS_9allocatorIsEEE16__init_with_sizeB8ne190102IPKsS6_EEvT_T0_m
- __ZNSt3__16vectorIsNS_9allocatorIsEEE18__assign_with_sizeB8ne190102IPKsS6_EEvT_T0_l
- __ZNSt3__16vectorIsNS_9allocatorIsEEEC2B8ne190102Em
- __ZNSt3__16vectorIxNS_9allocatorIxEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
- __ZNSt3__16vectorIxNS_9allocatorIxEEE18__assign_with_sizeB8ne190102IPxS5_EEvT_T0_l
- __ZNSt3__16vectorIxNS_9allocatorIxEEEC2B8ne190102Em
- __ZNSt3__16vectorIyNS_9allocatorIyEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIyNS_9allocatorIyEEE16__init_with_sizeB8ne190102IPyS5_EEvT_T0_m
- __ZNSt3__16vectorIyNS_9allocatorIyEEEC2B8ne190102Em
- __ZNSt3__17getlineB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EES6_
- __ZNSt3__18__rotateB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPN5arkit7IntRectEEES6_EENS_4pairIT0_S8_EES8_S8_T1_
- __ZNSt3__18optionalIN3cva6MatrixIfLj9ELj1ELb0EEEEaSB8ne190102INS1_16MatrixBinaryExprINS1_16MatrixScalarExprIS3_NS1_6detail5MulOpEEESA_NS8_5AddOpEEEvEERS4_OT_
- __ZNSt3__19allocatorIN5arkit15RobustExpFilterIfEEE7destroyB8ne190102EPS3_
- __ZNSt3__19allocatorIN5arkit15RobustExpFilterIfEEE9constructB8ne190102IS3_JddddddddEEEvPT_DpOT0_
- __ZNSt3__1rsB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEERNS_13basic_istreamIT_T0_EES9_RNS_12basic_stringIS6_S7_T1_EE
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___115-[ARSession _updateAnchorsForFrame:resultDatas:context:addedAnchors:updatedAnchors:removedAnchors:externalAnchors:]_block_invoke
- ___121-[ARPersonSegmentationTechnique runNeuralNetworkWithImageData:originalImageData:regionOfInterest:rotationOfResultTensor:]_block_invoke.33
- ___129-[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:]_block_invoke
- ___129-[ARRemoteService initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:]_block_invoke_2
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.32
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.33
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.34
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.54
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.58
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.62
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.66
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke.70
- ___143-[ARDepthTechnique createResultDataFromTensors:numberOfOutputTensors:imageDataForNeuralNetwork:inputImageData:rotationNeeded:regionOfInterest:]_block_invoke_2.35
- ___18-[ARQATracer stop]_block_invoke.83
- ___28-[ARRemoteService reconnect]_block_invoke.67
- ___32-[ARRemoteService _startService]_block_invoke
- ___32-[ARRemoteService _startService]_block_invoke.58
- ___32-[ARRemoteService _startService]_block_invoke.cold.1
- ___32-[ARRemoteService _startService]_block_invoke.cold.2
- ___37-[ARSession _exposeInternalDepthData]_block_invoke
- ___37-[ARSession _exposeInternalDepthData]_block_invoke_2
- ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke.462
- ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_2.466
- ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_3.467
- ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_4.472
- ___37-[ARSessionMetrics _recordSessionEnd]_block_invoke_5.473
- ___42-[ARSession runWithConfiguration:options:]_block_invoke.39
- ___44-[ARSessionMetrics _processFrameProperties:]_block_invoke.446
- ___45+[ARSession _applySessionOverrides:outError:]_block_invoke.447
- ___46-[ARRemoteService serviceConfiguredWithError:]_block_invoke.78
- ___46-[ARRemoteService serviceConfiguredWithError:]_block_invoke.78.cold.1
- ___48-[ARSession _sessionShouldAttemptRelocalization]_block_invoke.492
- ___53-[ARSession _setPrimaryTechnique:secondaryTechnique:]_block_invoke
- ___54-[ARSession getGeoLocationForPoint:completionHandler:]_block_invoke.174
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.245
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.261
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke.262
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke_2.249
- ___61-[ARSession technique:didOutputResultData:timestamp:context:]_block_invoke_3.253
- ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.202
- ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.204
- ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.206
- ___61-[ARWorldTrackingTechnique _initializeSLAMAndPredictorHandle]_block_invoke.208
- ___63-[ARWorldTrackingTechnique didReceiveKeyframesUpdatedCallback:]_block_invoke.177
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_2
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_3
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_4
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_5
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_6
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_7
- ___65-[ARWorldTrackingTechnique requestResultDataAtTimestamp:context:]_block_invoke_8
- ___68-[ARRemoteTechnique techniqueDidOutputResultData:timestamp:context:]_block_invoke
- ___68-[ARSession captureHighResolutionFrameWithPhotoSettings:completion:]_block_invoke
- ___68-[ARSession captureHighResolutionFrameWithPhotoSettings:completion:]_block_invoke_2
- ___68-[ARSession captureHighResolutionFrameWithPhotoSettings:completion:]_block_invoke_3
- ___71-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:]_block_invoke
- ___71-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:]_block_invoke_2
- ___71-[ARParentTechnique requestResultDataAtTimestamp:context:onTechniques:]_block_invoke_3
- ___77-[ARWorldTrackingTechnique _updatePoseData:forTimeStamp:updateTrackingState:]_block_invoke.224
- ___78-[ARTechniqueSequentialGatherContext mergeResultsOfContext:resultFilterBlock:]_block_invoke
- ___ARFileDescriptorIsTTY_block_invoke
- ___ARLinkedOnOrAfterCrystal_block_invoke
- ___ARLinkedOnOrAfterPeaceE_block_invoke
- ___block_descriptor_32_e35_B32?0"ARSegmentationData"8Q16^B24l
- ___block_descriptor_40_e8_32bs_e24_B16?0"<ARResultData>"8ls32l8
- ___block_descriptor_40_e8_32s_e25_B32?0"NSString"8Q16^B24ls32l8
- ___block_descriptor_72_ea8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.101
- ___block_literal_global.117
- ___block_literal_global.121
- ___block_literal_global.123
- ___block_literal_global.127
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.146
- ___block_literal_global.147
- ___block_literal_global.151
- ___block_literal_global.170
- ___block_literal_global.175
- ___block_literal_global.179
- ___block_literal_global.183
- ___block_literal_global.199
- ___block_literal_global.214
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.226
- ___block_literal_global.238
- ___block_literal_global.241
- ___block_literal_global.244
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.264
- ___block_literal_global.280
- ___block_literal_global.282
- ___block_literal_global.289
- ___block_literal_global.290
- ___block_literal_global.295
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.329
- ___block_literal_global.366
- ___block_literal_global.370
- ___block_literal_global.371
- ___block_literal_global.372
- ___block_literal_global.375
- ___block_literal_global.380
- ___block_literal_global.405
- ___block_literal_global.441
- ___block_literal_global.451
- ___block_literal_global.457
- ___block_literal_global.460
- ___block_literal_global.471
- ___block_literal_global.475
- ___block_literal_global.479
- ___block_literal_global.520
- ___block_literal_global.524
- ___block_literal_global.526
- ___block_literal_global.557
- ___block_literal_global.568
- ___block_literal_global.572
- ___block_literal_global.574
- ___block_literal_global.578
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.64
- ___block_literal_global.69
- ___block_literal_global.71
- ___block_literal_global.8
- ___block_literal_global.82
- ___block_literal_global.869
- ___block_literal_global.873
- ___block_literal_global.875
- ___block_literal_global.878
- ___realtime_assert_rtn
- ___stderrp
- ___stdoutp
- __exposeInternalDepthData.exposeInternalDepthData
- __exposeInternalDepthData.onceToken
- __printColoredMessage
- __printError
- __printFormat
- __printInfo
- __printMessage
- __printMessageWithColor
- __printWarning
- _ar_rt_frame_time_estimator_add_frame_time
- _ar_rt_frame_time_estimator_estimate_frame_time
- _ar_rt_frame_time_estimator_init
- _ar_rt_frame_time_estimator_reset
- _ar_rt_ring_buffer_add_element
- _ar_rt_ring_buffer_add_element.cold.1
- _ar_rt_ring_buffer_decrement_index
- _ar_rt_ring_buffer_decrement_index.cold.1
- _ar_rt_ring_buffer_empty
- _ar_rt_ring_buffer_empty.cold.1
- _ar_rt_ring_buffer_filled
- _ar_rt_ring_buffer_filled.cold.1
- _ar_rt_ring_buffer_increment_index
- _ar_rt_ring_buffer_increment_index.cold.1
- _ar_rt_ring_buffer_init
- _ar_rt_ring_buffer_init.cold.1
- _ar_rt_ring_buffer_reset
- _ar_rt_ring_buffer_reset.cold.1
- _fflush
- _fileno
- _fprintf
- _fputs
- _isatty
- _kARSFBSUserNotificationIconSystemNameKey
- _kARSFBSUserNotificationNoticeDefaultTimeout
- _kARSFBSUserNotificationPresentationStyleKey
- _kARSFBSUserNotificationSymbolForegroundStyleKey
- _kARSFBSUserNotificationSymbolRenderingModeKey
- _kCGColorSpaceGenericRGBLinear
- _kCIImageColorSpace
- _kCV3DVIO_LensType
- _kCVPixelBufferIOSurfacePurgeableKey
- _malloc_type_calloc
- _objc_msgSend$_changePowerUsage:forced:
- _objc_msgSend$_defaultPhotoSettings
- _objc_msgSend$_exposeInternalDepthData
- _objc_msgSend$_isBravoCamOtherThanWideUsed
- _objc_msgSend$_serverConnectionInterrupted
- _objc_msgSend$_setPrimaryTechnique:secondaryTechnique:
- _objc_msgSend$_startSensorsWithRequiredDataTypes:optionalDataTypes:
- _objc_msgSend$_submitResultsForTimestamp:context:
- _objc_msgSend$_updateAnchorsForFrame:resultDatas:context:addedAnchors:updatedAnchors:removedAnchors:externalAnchors:
- _objc_msgSend$_updatePowerUsageForced:
- _objc_msgSend$_updateThermalState:
- _objc_msgSend$alphaMapOutput
- _objc_msgSend$bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:
- _objc_msgSend$captureHighResolutionFrameWithPhotoSettings:completion:
- _objc_msgSend$clientBundleIdentifier
- _objc_msgSend$depthMap
- _objc_msgSend$dotGraphWithLines:
- _objc_msgSend$fileExistsAtPath:isDirectory:
- _objc_msgSend$findMergedPlanes::
- _objc_msgSend$forceUpdatePowerUsage:
- _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:
- _objc_msgSend$imageWithCVPixelBuffer:options:
- _objc_msgSend$initWithAmbientColor:areaLights:
- _objc_msgSend$initWithDaemon:startConnection:dispatchChannelQueue:
- _objc_msgSend$initWithDirection:angularSize:color:
- _objc_msgSend$initWithDispatchChannelQueue:
- _objc_msgSend$initWithEndpoint:startConnection:dispatchChannelQueue:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithFormat:arguments:
- _objc_msgSend$initWithIntrinsics:imageResolution:devicePosition:lensType:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:
- _objc_msgSend$initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:
- _objc_msgSend$lensType
- _objc_msgSend$listForKey:
- _objc_msgSend$maxPhotoDimensionsForVideoFormat:maximumHeight:
- _objc_msgSend$maxPhotoQualityPrioritization
- _objc_msgSend$mergeResultsOfContext:resultFilterBlock:
- _objc_msgSend$mutableSettings
- _objc_msgSend$optionalSensorDataTypes
- _objc_msgSend$parametricLights
- _objc_msgSend$pathForResource:ofType:inDirectory:
- _objc_msgSend$resolutionDictionaryForKey:
- _objc_msgSend$setDepthMap:
- _objc_msgSend$setLensType:
- _objc_msgSend$setShouldOperateOnHighResolutionImages:
- _objc_msgSend$shouldOperateOnHighResolutionImages
- _objc_msgSend$stringByStandardizingPath
- _objc_msgSend$techinqueInArray:passingTest:
- _objc_msgSend$uppercaseString
- _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:previousNormals:intoCurrentNormals:usingPoseDelta:previousCalibration:currentCalibration:
- _objc_setProperty_nonatomic
- _os_transaction_create
- _printColoredMessage
- _printError
- _printInfo
- _printMessage
- _printVector3
- _printWarning
- _printf
- _puts
CStrings:
+ " gravityUpdated=%@"
+ " recipients=%@"
+ "\"(%p)\"[label=\"{%@ %@|(%p)"
+ "\"3"
+ "$"
+ "%@ Stopped location updates"
+ "%@(%p): Unable to create pixel buffer with aux attributes for %@: %i"
+ "%p"
+ "%{public}@ <%p>: %@ Configuring photo output for max. photo quality prioritization: %ld"
+ "%{public}@ <%p>: %@ deferred start supported: %u, enabled: %u."
+ "%{public}@ <%p>: %@ dispatch channel with queue: %@"
+ "%{public}@ <%p>: %@ frame update timer"
+ "%{public}@ <%p>: %@: No video frame received. Dropping frame! Reason: %@"
+ "%{public}@ <%p>: %@: Video frame received without camera calibration data. Dropping frame! Reason: %@"
+ "%{public}@ <%p>: %@: Video frame received without vision data. Reason: %@"
+ "%{public}@ <%p>: ARPositionalTrackingConfiguration frame rate set to %f by user defaults"
+ "%{public}@ <%p>: ARWorldTrackingConfiguration is not supported"
+ "%{public}@ <%p>: Aborted generating data because the point cloud is blackened."
+ "%{public}@ <%p>: Connection set to custom fixed priority queue: %@"
+ "%{public}@ <%p>: Could not convert pixel buffer"
+ "%{public}@ <%p>: Could not create pixel buffer from pool."
+ "%{public}@ <%p>: Creating a dispatch channel with dispatchChannelDataSize equal to 0."
+ "%{public}@ <%p>: Dropped a pointCloudDataOutput because data is nil: %@"
+ "%{public}@ <%p>: Dropped frame. Techniques that did not get the image: %@"
+ "%{public}@ <%p>: Enabling scheduling for ResultRequestSchedulers"
+ "%{public}@ <%p>: Encountered ARCaptureLensUnknown in Bravo cam session."
+ "%{public}@ <%p>: Error setting cancel handler for Dispatch Channel"
+ "%{public}@ <%p>: Error setting message handler for Dispatch Channel"
+ "%{public}@ <%p>: Failed generating depth: missing point cloud"
+ "%{public}@ <%p>: Failed preparing scene depth: %@"
+ "%{public}@ <%p>: Failed running scene depth frame: %@"
+ "%{public}@ <%p>: Failed to create RT channel from request using channel_rt_create_from_request"
+ "%{public}@ <%p>: Failed to create dispatch channel from request"
+ "%{public}@ <%p>: Holding back frame because we're under the minimum latency."
+ "%{public}@ <%p>: Ignoring location update for stopped sensor"
+ "%{public}@ <%p>: Location manager created: %{private}@"
+ "%{public}@ <%p>: No in flight context found for %f"
+ "%{public}@ <%p>: No new unvended frame ready to publish at timer tick. Will attempt to push shortly."
+ "%{public}@ <%p>: Preparing still image techniques"
+ "%{public}@ <%p>: Re-using existing still image techniques if possible."
+ "%{public}@ <%p>: Replacing highRes session technique %p with %p"
+ "%{public}@ <%p>: Result of querying supportedVideoFormats is empty."
+ "%{public}@ <%p>: Started location updates"
+ "%{public}@ <%p>: Starting ARDispatchSourceExecutor with frame rate %lu and initialDelay %f"
+ "%{public}@ <%p>: Unable to initialize ARDeviceOrientationSensor: Device motion from CMMotionManager not available."
+ "%{public}@ <%p>: Unable to initialize ARMotionSensor: accelerometer and/or gyroscope from CMMotionManager not available."
+ "%{public}@ <%p>: Using all new high-res techniques."
+ "%{public}@ <%p>: Vending frame outside of timer tick because %lu frames are already queued."
+ "%{public}@ <%p>: Vending frame outside of timer tick because maximum latency of %f s is reached."
+ "%{public}@ <%p>: Vending frame outside of timer tick."
+ "%{public}@ <%p>: _startService%@"
+ "%{public}@ <%p>: dispatchDataSize changed on _messageBuffer. _messageBuffer is being resized."
+ "%{public}@ <%p>: first location update received after %f seconds"
+ "%{public}@ <%p>: preparing AppleDepth executor on orientation change: (%.0f,%.0f) -> (%.0f,%.0f)"
+ "%{public}@ <%p>: startedSensorDataTypes: %@  VS.  requiredDataTypes: %@"
+ "%{public}@ <%p>: video format is nil, supportedVideoFormats is empty"
+ "%{public}@: Cancelled dispatch channel"
+ "%{public}@: message_size doesn't match dispatchChannelDataSize."
+ "(%f %f)"
+ "-[ARRemoteService handleDispatchChannelMessage:size:type:]"
+ ".dispatchChannelQueue"
+ ".xpc"
+ "0x%016lX"
+ "1#"
+ ": synchronous"
+ "<%@: %p upTime=%f upTimeIncludingSleep=%f upTimeIncludingSleepAndDriftCorrection=%f>"
+ "<%@: %p: Identifier:%@, type:%@>"
+ "<Unknown>"
+ "@\"<ARFrameUpdateTimerDelegate>\""
+ "@\"<ARRepetitiveExecutor>\""
+ "@\"<ARThermalStateProvider>\""
+ "@\"<ARTimeProviding>\""
+ "@\"ADJasperColorExecutor\""
+ "@\"ADJasperColorPipelineParameters\"16@0:8"
+ "@\"ADLogManager\""
+ "@\"ARAnchorChangeSet\""
+ "@\"ARFrameUpdateTimer\""
+ "@\"ARInFrameAnchorVisualizer\""
+ "@\"ARTechnique\"24@0:8@\"Protocol\"16"
+ "@\"ARTechnique\"32@0:8@\"Protocol\"16@\"NSArray\"24"
+ "@\"NSObject<OS_channel_dispatch>\""
+ "@\"NSObject<OS_channel_rt>\""
+ "@\"NSObject<OS_nw_endpoint>\""
+ "@\"PixelBufferConverter\""
+ "@104@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^^}16{vector<short, std::allocator<short>>=^s^s^s}40Q647288"
+ "@168@0:8{?=[3]}16{CGSize=dd}64q8088120d136@144@152Q160"
+ "@16@?0@\"ARImageSensor\"8"
+ "@216@0:8{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v^v}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}}}16@192d200d208"
+ "@248@0:8@16{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}@}24"
+ "@32@0:8^{__CVBuffer=}16q24"
+ "@39@0:816f32{Color=CCC}36"
+ "@40@0:8d16d24d32"
+ "@40@0:8{set<unsigned long long, std::less<unsigned long long>, std::allocator<unsigned long long>>={__tree<unsigned long long, std::less<unsigned long long>, std::allocator<unsigned long long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16"
+ "@44@0:8{vector<ARPatch, std::allocator<ARPatch>>=^{?}^{?}^{?}}16f40"
+ "@48@0:8@16B24@28B36@40"
+ "@52@0:8@16@24@32@40B48"
+ "@60@0:8q16@24@32@40B48I52B56"
+ "@64@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^^}16{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q^Q}40"
+ "@72@0:8@16@24@32@40B48@52B60@64"
+ "@72@0:8d16{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}^{ARTexturedPlane}^{ARTexturedPlane}}24@48@56@64"
+ "@88@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^^}16{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q^Q}40{vector<float, std::allocator<float>>=^f^f^f}64"
+ "ARAnchorChangeSet"
+ "ARCAMediaTimeProvider"
+ "ARCrashCustomerVisible: %@"
+ "ARDaemonReplayDelegate"
+ "ARDepthTechniqueProtocol"
+ "ARDispatchSourceExecutor"
+ "ARFrameUpdateTimer"
+ "ARFrameUpdateTimerDelegate"
+ "ARInFrameAnchorVisualizer"
+ "ARKit is not supported on this device (via MobileGestalt)."
+ "ARProcessInfoThermalStateProvider"
+ "ARRepetitiveExecutor"
+ "ARSaveIOSurfaceRAW: Only planar surface are supported."
+ "ARSaveIOSurfaceRAW: Only surface with elementWidth == 1 supported."
+ "ARSaveIOSurfaceRAW: Only surface with elementWidth == elementHeight supported."
+ "ARSaveIOSurfaceRAW: validBytesPerRow (%zu) must be <  paddedBytesPerRow (%zu)."
+ "ARSceneDepthTechnique"
+ "ARSupportsAsyncEmptyResultEmission"
+ "ARSystemTimeSnapshot"
+ "ARThermalStateProvider"
+ "ARTimeProviding"
+ "ARUserProfile"
+ "ARWorldTracking is not supported on this device. VIO is video mode supported returned false."
+ "AnchorGroupNotAuthorized"
+ "B32@0:8@16^{?=ii}24"
+ "B32@?0@\"AVCaptureDevice\"8Q16^B24"
+ "BKSAccelerometerDelegate"
+ "Confidence Map Output"
+ "Confidence Output"
+ "Creating"
+ "Default"
+ "Disabling"
+ "DrawData"
+ "Enabling"
+ "Enrolled"
+ "Error getting vertices count"
+ "Error retrieving entitlement %@: %@"
+ "Error: %@(%p): Unable to create pixel buffer with aux attributes for %@: %i"
+ "Error: %{public}@ <%p>: %@: No video frame received. Dropping frame! Reason: %@"
+ "Error: %{public}@ <%p>: %@: Video frame received without camera calibration data. Dropping frame! Reason: %@"
+ "Error: %{public}@ <%p>: %@: Video frame received without vision data. Reason: %@"
+ "Error: %{public}@ <%p>: ARWorldTrackingConfiguration is not supported"
+ "Error: %{public}@ <%p>: Aborted generating data because the point cloud is blackened."
+ "Error: %{public}@ <%p>: Could not convert pixel buffer"
+ "Error: %{public}@ <%p>: Could not create pixel buffer from pool."
+ "Error: %{public}@ <%p>: Could not create pixel buffer pool."
+ "Error: %{public}@ <%p>: Creating a dispatch channel with dispatchChannelDataSize equal to 0."
+ "Error: %{public}@ <%p>: Error setting cancel handler for Dispatch Channel"
+ "Error: %{public}@ <%p>: Error setting message handler for Dispatch Channel"
+ "Error: %{public}@ <%p>: Failed generating depth: missing point cloud"
+ "Error: %{public}@ <%p>: Failed preparing scene depth: %@"
+ "Error: %{public}@ <%p>: Failed running scene depth frame: %@"
+ "Error: %{public}@ <%p>: Failed to create RT channel from request using channel_rt_create_from_request"
+ "Error: %{public}@ <%p>: Failed to create dispatch channel from request"
+ "Error: %{public}@ <%p>: No in flight context found for %f"
+ "Error: %{public}@ <%p>: Result of querying supportedVideoFormats is empty."
+ "Error: %{public}@ <%p>: Unable to initialize ARDeviceOrientationSensor: Device motion from CMMotionManager not available."
+ "Error: %{public}@ <%p>: Unable to initialize ARMotionSensor: accelerometer and/or gyroscope from CMMotionManager not available."
+ "Error: %{public}@ <%p>: dispatchDataSize changed on _messageBuffer. _messageBuffer is being resized."
+ "Error: %{public}@ <%p>: video format is nil, supportedVideoFormats is empty"
+ "Error: %{public}@: message_size doesn't match dispatchChannelDataSize."
+ "Error: ARKit is not supported on this device (via MobileGestalt)."
+ "Error: ARSaveIOSurfaceRAW: Only planar surface are supported."
+ "Error: ARSaveIOSurfaceRAW: Only surface with elementWidth == 1 supported."
+ "Error: ARSaveIOSurfaceRAW: Only surface with elementWidth == elementHeight supported."
+ "Error: ARSaveIOSurfaceRAW: validBytesPerRow (%zu) must be <  paddedBytesPerRow (%zu)."
+ "Error: ARWorldTracking is not supported on this device. VIO is video mode supported returned false."
+ "Error: Error retrieving entitlement %@: %@"
+ "Error: Unable to fetch audit token for current process with statusCode: %i"
+ "Failed generating depth with AD error %li"
+ "Failed preparing AppleDepth executor AD error %li"
+ "Failed to allocate buffer for scene depth"
+ "Failed to allocate buffer pool for scene depth with error %li"
+ "Failed to resample scene depth output buffer with error %li"
+ "Guest"
+ "HighRes"
+ "Is Complete: %@\r"
+ "LatencyTooHigh"
+ "Localizable"
+ "MLFrameSet"
+ "MaxNRAreasReached"
+ "NRAnchorNotPermitted"
+ "NoFrameOnLastTick"
+ "PersistGuest"
+ "PixelBufferConverter"
+ "Primary"
+ "PrivateFrameworks/ARKitDaemon.framework"
+ "QueueFull"
+ "Reusing"
+ "S"
+ "Scaled Confidence Map Output"
+ "Scaled Depth Output"
+ "Scaled single frame Confidence Output"
+ "Scaled single frame Depth Output"
+ "Split"
+ "Stopped location updates"
+ "Subclass needs to override %@ and not call super"
+ "SubmapsStatsInfo"
+ "T,R,V_position"
+ "T@\"<ARFrameUpdateTimerDelegate>\",W,N,V_delegate"
+ "T@\"ADJasperColorPipelineParameters\",R,N"
+ "T@\"ARAnchorChangeSet\",&,N,V_anchorChangeSet"
+ "T@\"ARConfiguration\",&,V_configurationForPublicGetter"
+ "T@\"ARParentTechnique\",&,V_stillImageRootTechnique"
+ "T@\"AVCapturePhotoSettings\",R,N"
+ "T@\"NSArray\",R,C,N,V_addedAnchors"
+ "T@\"NSArray\",R,C,N,V_externalAnchors"
+ "T@\"NSArray\",R,C,N,V_removedAnchors"
+ "T@\"NSArray\",R,C,N,V_updatedAnchors"
+ "T@\"NSObject<OS_channel_dispatch>\",&,N,V_dispatchChannel"
+ "T@\"NSObject<OS_channel_rt>\",&,N,V_channel"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchChannelQueue"
+ "T@\"NSSet\",&,N,V_recipientIdentifiers"
+ "T@\"NSString\",R,N,V_identifier"
+ "T@?,C,N,V_replayFailedBlock"
+ "T@?,C,N,V_replayStartedBlock"
+ "T@?,C,N,V_replayStoppedBlock"
+ "T@?,C,N,V_replayUpdatedBlock"
+ "T@?,C,N,V_serviceDidConfigureBlock"
+ "T@?,C,N,V_serviceDidUpdateDataAccessBlock"
+ "TB,GisDataAccessAllowed,V_dataAccessAllowed"
+ "TB,N,GisActive,V_active"
+ "TB,N,GisPassive"
+ "TB,N,V_disableTemporalSegmentation"
+ "TB,N,V_isMultiSessionMode"
+ "TB,N,V_useFrameUpdateTimer"
+ "TB,R,V_prepareWasCalled"
+ "TB,V_isDroppedData"
+ "TB,V_isWorldOriginSet"
+ "TB,V_stillRequiresPostProcessing"
+ "Td,N,V_maxDesiredLatency"
+ "Td,N,V_minLatency"
+ "Td,N,V_scheduledTimestamp"
+ "Td,R"
+ "Td,R,N,V_upTime"
+ "Td,R,N,V_upTimeIncludingSleep"
+ "Td,R,N,V_upTimeIncludingSleepAndDriftCorrection"
+ "Tf,R,V_size"
+ "TimerDisabled"
+ "TimerTick"
+ "Tq,R,N,V_type"
+ "T{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v^v}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}}},N,V_chunkMesh"
+ "T{Color=CCC},R,V_color"
+ "T{vector<unsigned char, std::allocator<unsigned char>>=***},N,V_semanticsVector"
+ "Unable to fetch audit token for current process with statusCode: %i"
+ "Unable to generate normal map: %li"
+ "Unknown (%d)"
+ "^{__CVBuffer=}28@0:8^{__CVBuffer=}16I24"
+ "_active"
+ "_adLogger"
+ "_anchorChangeSet"
+ "_bgraToInputFormatConverter"
+ "_busySemaphore"
+ "_channel"
+ "_compensationMatrixForBravoSession"
+ "_compensationMatrixForTrackingCameraID:"
+ "_compensationMatrixForWidePlusUWSessionAndTrackingCameraID:"
+ "_configurationForPublicGetter"
+ "_createTechniques:forStillImage:"
+ "_currentFramesPerSecond"
+ "_dataAccessAllowed"
+ "_depthProcessingQueue"
+ "_deviceEndpoint"
+ "_disableTemporalSegmentation"
+ "_dispatchChannel"
+ "_dispatchChannelClosed"
+ "_dispatchChannelQueue"
+ "_enableMLCMRelocalization"
+ "_executor"
+ "_extrinsicsFromUWToWide"
+ "_extrinsicsFromWideToTele"
+ "_extrinsicsFromWideToUW"
+ "_frameDuration"
+ "_frameUpdateTick"
+ "_frameUpdateTimer"
+ "_frameWasVendedAtLastTimerTick"
+ "_generateDepthForDownscaledImageData:error:"
+ "_geoTrackingPublicStatusChangedFromLastVendedFrameToFrame:"
+ "_getCameraCalibration:rotation:inputDimensions:"
+ "_inFrameAnchorVisualizer"
+ "_inputDimensions"
+ "_inputFormatToBGRAConverter"
+ "_isBeforeFirstTimerTick"
+ "_isDeterministicMode"
+ "_isDroppedData"
+ "_isMultiSessionMode"
+ "_isRunning"
+ "_isWorldOriginSet"
+ "_jointname_to_index"
+ "_kernelSize"
+ "_lastFrameVendReason"
+ "_lastFrameVendTimestamp"
+ "_lastRawOrientation"
+ "_lastTimerTick"
+ "_lastVendedFrame"
+ "_lastVendedFrameSemaphore"
+ "_latencyIsTooHighForFrame:"
+ "_latencyIsTooLowForFrame:"
+ "_logTechniqueGraphForDebugging"
+ "_logTechniqueState:state:data:"
+ "_maxDesiredLatency"
+ "_minLatency"
+ "_outputDimensionsInOriginalImageRotation"
+ "_outputNormalsInOriginalImageRotationPixelBufferPool"
+ "_outputRotation"
+ "_outputScaledConfidenceMapPixelBufferPool"
+ "_outputScaledConfidencePixelBufferPool"
+ "_outputScaledDepthPixelBufferPool"
+ "_outputScaledSingleFrameConfidencePixelBufferPool"
+ "_outputScaledSingleFrameDepthPixelBufferPool"
+ "_outputSingleFrameConfidencePixelBufferPool"
+ "_outputSingleFrameDepthPixelBufferPool"
+ "_passive"
+ "_pendingRawSceneUnderstandingResults"
+ "_pendingRawSceneUnderstandingResultsLock"
+ "_pixelTransferSession"
+ "_pollRawOrientation"
+ "_populateRawSceneUnderstandingDataForFrame:fromResultData:"
+ "_postProcessNonSynchronousDataForSceneUnderstanding:"
+ "_preferredRenderFrameRateForCaptureFrameRate:isNominalPower:"
+ "_preferredRenderSyncFrameRateForCaptureFrameRate:"
+ "_prepareOnDimensionsChange:outputRotation:error:"
+ "_prepareOnce"
+ "_prepareWasCalled"
+ "_prepared"
+ "_previous3DSkeletonLock"
+ "_recipientIdentifiers"
+ "_replayFailedBlock"
+ "_replayStartedBlock"
+ "_replayStoppedBlock"
+ "_replayUpdatedBlock"
+ "_resultDataPredictionQueue"
+ "_rotatedPixelBufferImageData:rotationAngle:"
+ "_safeProcessData:"
+ "_saveExtrinsicsForBravoCamSessionFromImage:"
+ "_saveExtrinsicsForWidePlusUWSessionFromImage:"
+ "_saveExtrinsicsFromImage:"
+ "_scheduledTimestamp"
+ "_serviceDidConfigureBlock"
+ "_serviceDidUpdateDataAccessBlock"
+ "_sessionType"
+ "_setInternalConfiguration:"
+ "_setPrimaryTechnique:secondaryTechnique:stillImageRootTechnique:"
+ "_setThermalStateProvider:"
+ "_start"
+ "_startExecutorWithFrameRate:initialDelay:"
+ "_startSensorsWithDataTypes:"
+ "_startServiceSynchronous:"
+ "_startTimestamp"
+ "_startedPrepare"
+ "_stillImageProcessingQueue"
+ "_stillImageRootTechnique"
+ "_stillRequiresPostProcessing"
+ "_storeNewFrame:"
+ "_supportedVideoFormatsForDevicePosition:deviceType:resolutions:frameRatesByPowerUsage:videoBinned:pixelFormat:needsHDRSupport:"
+ "_thermalStateProvider"
+ "_timeProvider"
+ "_timeSinceFrameWasScheduled:"
+ "_timeTillNextTimerTick"
+ "_timerLock"
+ "_timerQueue"
+ "_trackingStateChangedFromLastVendedFrameToFrame:"
+ "_unvendedFrames"
+ "_unvendedFramesCount"
+ "_unvendedFramesLock"
+ "_upTime"
+ "_upTimeIncludingSleep"
+ "_upTimeIncludingSleepAndDriftCorrection"
+ "_updateAnchorsForFrame:resultDatas:context:"
+ "_updateExecutorForFrameRate:"
+ "_updateThermalStateFromCurrentProcessInfo"
+ "_useFrameUpdateTimer"
+ "_useLowLatencyPath"
+ "_usePreviousImageDataUponDataDrop"
+ "_vendFrame:withReason:"
+ "_vendFrameIfAtLastTickNoFrameWasVended"
+ "_vendFramesIfTooManyFramesAreQueued"
+ "_vendFramesThatExceedTheMaximumLatency"
+ "accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:"
+ "accelerometer:didChangeDeviceOrientation:"
+ "added"
+ "anchorChangeSet"
+ "arMLDepthResult"
+ "ar_tinyUUIDString"
+ "arkitdepth"
+ "baseAddress"
+ "bytesPerElement"
+ "bytesPerRow"
+ "callingProcessData"
+ "captureHighResolutionFrameUsingPhotoSettings:completion:"
+ "channel"
+ "children"
+ "clearPreviousContext"
+ "colorSpace"
+ "com.apple.ARKitDaemon"
+ "com.apple.arkit"
+ "com.apple.arkit.appleDepth.useLegacyDepthTechnique"
+ "com.apple.arkit.geotracking.disableLocationAuthorizationCheckForReplay"
+ "com.apple.arkit.inFrameAnchorVisualization"
+ "com.apple.arkit.parenttechnique.enableLowLatencyPath"
+ "com.apple.arkit.pointCloudDataOutput.deferredStartEnabled"
+ "com.apple.arkit.resultDataPredictionQueue"
+ "com.apple.arkit.scenedepthtechnique"
+ "com.apple.arkit.session.disableRenderSyncScheduling"
+ "com.apple.arkit.technique.stillimages"
+ "com.apple.arkit.timerSerialQueue"
+ "confidenceLevels"
+ "confidenceOutProcessed"
+ "confidenceOutRaw"
+ "configurationForPublicGetter"
+ "constituentDevices"
+ "convertPixelBuffer:toFormat:"
+ "createDispatchChannelWithRequest:completion:"
+ "createRTChannelWithRequest:completion:"
+ "currentFramesPerSecond"
+ "currentRenderSyncFramesPerSecond"
+ "d24@0:8Q16"
+ "dataAccessAllowed"
+ "dataWithLength:"
+ "defaultColorSpace"
+ "defaultLoggerWithName:"
+ "defaultPhotoSettings"
+ "defaultProfile"
+ "depthOutProcessed"
+ "depthOutRaw"
+ "diff:against:"
+ "disableTemporalSegmentation"
+ "dispatchChannel"
+ "dispatchChannelClosed"
+ "dispatchChannelQueue"
+ "dotGraphWithLines:rootName:"
+ "drawOriginAndAnchorsOnFrame:"
+ "elementHeight"
+ "elementWidth"
+ "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:"
+ "executeWithInterval:initialDelay:block:"
+ "executorParameters"
+ "fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:"
+ "gatheredDataWasAlreadyCaptured"
+ "gravityUpdated"
+ "handleDispatchChannelMessage:size:type:"
+ "id"
+ "imageWithCVPixelBuffer:"
+ "initWithAddedAnchors:updatedAnchors:removedAnchors:externalAnchors:"
+ "initWithDaemon:deviceEndpoint:"
+ "initWithDaemon:fixedPriorityQueueForXPC:"
+ "initWithDaemon:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:"
+ "initWithDeviceEndpoint:"
+ "initWithDispatchChannelQueue:fixedPriorityQueueForXPC:"
+ "initWithEndpoint:deviceEndpoint:"
+ "initWithFixedPriorityQueueForXPC:"
+ "initWithIdentifier:type:"
+ "initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:"
+ "initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:fixedPriorityQueueForXPC:"
+ "initWithMachServiceName:exportedInterface:remoteObjectInterface:endpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:deviceEndpoint:"
+ "initWithPosition:size:color:"
+ "initWithTimeProvider:executor:"
+ "initWithUpTime:upTimeIncludingSleep:upTimeIncludingSleepAndDriftCorrection:"
+ "instanceMethodForSelector:"
+ "internalDepthSettings"
+ "internalSettings"
+ "isBackUltraWide"
+ "isComplete"
+ "isDataAccessAllowed"
+ "isDeferredStartEnabled"
+ "isDeferredStartSupported"
+ "isDroppedData"
+ "isGuestProfileEnabled"
+ "isPassive"
+ "isTravelMode"
+ "isWorldOriginSet"
+ "lockWithOptions:seed:"
+ "logPixelBuffer:name:timestamp:"
+ "logger"
+ "maxDesiredLatency"
+ "minLatency"
+ "modified"
+ "normalsOutProcessed"
+ "numberOfInFlightContexts"
+ "old"
+ "parallelTechniqueTimeout"
+ "passive"
+ "photoQualityPrioritizationOverride"
+ "pipeline"
+ "planeCount"
+ "pointCount"
+ "prepareForEngineType:roi:exifOrientation:rotationPreference:"
+ "prepareWasCalled"
+ "processedColor"
+ "processedJasper"
+ "pushEmptyResultOnAsynchronousQueueForTimestamp:"
+ "q24@?0@\"ARFrame\"8@\"ARFrame\"16"
+ "q24@?0@\"NSArray\"8@\"NSArray\"16"
+ "q28@0:8q16B24"
+ "receivedResultData"
+ "recipientIdentifiers"
+ "referenceImageUUIDForPixelBuffer:"
+ "removeDataWithFilename:extension:"
+ "removeDataWithPath:"
+ "removed"
+ "replayDidFailWithError:"
+ "replayDidStartWithReplayTime:"
+ "replayDidStop"
+ "replayDidUpdateResourceWithKey:atTime:"
+ "replayFailedBlock"
+ "replayStartedBlock"
+ "replayStoppedBlock"
+ "replayUpdatedBlock"
+ "requestResultDataAtTimestamp:context:onTechniques:withTimeout:"
+ "requestResultDataAtTimestamp:context:withTimeout:"
+ "requestingResultDataParallel"
+ "requestingResultDataSerial"
+ "resolutionForKey:resultingDimensions:"
+ "same"
+ "scaleAllowStretch:"
+ "sceneDepthTechniqueForPrioritization:temporalSmoothing:"
+ "scheduleFrame:captureFramesPerSecond:"
+ "scheduledTimestamp"
+ "segmentationResultWithDataSource:"
+ "sequentialTechniqueTimeout"
+ "serviceDidConfigureBlock"
+ "serviceDidUpdateDataAccessBlock"
+ "setAnchorChangeSet:"
+ "setBufferCopyPolicy:"
+ "setChannel:"
+ "setConfigurationForPublicGetter:"
+ "setDataAccessAllowed:"
+ "setDeferredStartEnabled:"
+ "setDisableTemporalSegmentation:"
+ "setDispatchChannel:"
+ "setDispatchChannelQueue:"
+ "setIgnoreDistortionInDepthReprojection:"
+ "setIntrinsicMatrix:"
+ "setIsDroppedData:"
+ "setIsMultiSessionMode:"
+ "setIsWorldOriginSet:"
+ "setMaxDesiredLatency:"
+ "setMinLatency:"
+ "setMovieFragmentInterval:"
+ "setPassive:"
+ "setPixelSize:"
+ "setPreferredFrameRateRange:"
+ "setRecipientIdentifiers:"
+ "setReferenceDimensions:"
+ "setReplayFailedBlock:"
+ "setReplayStartedBlock:"
+ "setReplayStoppedBlock:"
+ "setReplayUpdatedBlock:"
+ "setScheduledTimestamp:"
+ "setServiceDidConfigureBlock:"
+ "setServiceDidUpdateDataAccessBlock:"
+ "setStillImageRootTechnique:"
+ "setStillRequiresPostProcessing:"
+ "setTemporalConsistencyMethod:"
+ "setUseFrameUpdateTimer:"
+ "setupCompleteForRTChannel"
+ "single frame Confidence Output"
+ "single frame Depth Output"
+ "sortDescriptorWithKey:ascending:comparator:"
+ "sortedArrayUsingDescriptors:"
+ "spotIdentifiers"
+ "stillImageRootTechnique"
+ "stillRequiresPostProcessing"
+ "submitResultsForTimestamp:context:"
+ "submittedResultData"
+ "supportedColorSpaces"
+ "targetTimestamp"
+ "techniqueConformsToProtocol:"
+ "techniqueConformsToProtocol:inArray:"
+ "techniqueInArray:passingTest:"
+ "techniqueLevel"
+ "techniquesForStillImageGraph"
+ "timeSinceSnapshot:"
+ "timeoutForNextFrameUpdateWithNumberOfInFlightContexts:"
+ "timerDidVendFrame:"
+ "toJSONWithRootName:"
+ "transformAnchorToPlaneAnchorConvention:"
+ "unlockWithOptions:seed:"
+ "upTime"
+ "upTimeIncludingSleep"
+ "upTimeIncludingSleepAndDriftCorrection"
+ "useFrameUpdateTimer"
+ "v192@0:8{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v^v}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}}}16"
+ "v24@0:8@\"ARFrame\"16"
+ "v28@?0^v8Q16I24"
+ "v32@0:8@\"ARXPCDictionaryWrapper\"16@?<v@?@\"ARXPCDictionaryWrapper\">24"
+ "v32@0:8@\"BKSAccelerometer\"16q24"
+ "v32@0:8@\"NSMutableArray\"16@\"NSString\"24"
+ "v32@0:8@\"NSObject<OS_xpc_object>\"16@?<v@?@\"NSObject<OS_xpc_object>\">24"
+ "v32@0:8@\"NSString\"16d24"
+ "v32@0:8Q16d24"
+ "v36@0:8^v16Q24I32"
+ "v376@0:8^{__CVBuffer=}16f24{?=[3]}28{?=[4]}76{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}@}140Q364B372"
+ "v40@0:8d16@24d32"
+ "v40@0:8d16d24@?32"
+ "v40@0:8d16d24@?<v@?>32"
+ "v40@0:8{vector<unsigned char, std::allocator<unsigned char>>=***}16"
+ "v476@0:8{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}@}16{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}@}240Q464B472"
+ "v48@0:8@\"BKSAccelerometer\"16d24f32f36f40i44"
+ "v48@0:8@16d24f32f36f40i44"
+ "v48@0:8d16@24@32d40"
+ "v48@0:8{CGSize=dd}16q32^@40"
+ "warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingPoseDelta:previousCalibration:currentCalibration:"
+ "writeToFile:atomically:"
+ "x86_64"
+ "{?=[4]}20@0:8I16"
+ "{?=[4]}80@0:8{?=[4]}16"
+ "{?=ii}16@0:8"
+ "{ARPlaneUpdateQueue=\"queue\"{queue<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>, std::deque<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"c\"{deque<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__map_\"{__split_buffer<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> *, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"__cap_\"^^v}\"__start_\"Q\"__size_\"Q}}\"elements\"{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=\"__tree_\"{__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}}"
+ "{ChunkMesh=\"chunk_position\"{Matrix<short, 3U, 1U, false>=\"m_data\"[3s]}\"mesh\"{TriMesh<float, unsigned int>=\"vertices\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"colors\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"normals\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"faces\"{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"edges\"{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"tex_coords\"{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}\"tex_faces\"{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}}}"
+ "{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v^v}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v^v}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v^v}}}16@0:8"
+ "{Color=\"red\"C\"green\"C\"blue\"C}"
+ "{Color=CCC}16@0:8"
+ "{FacialLightEstimation=\"m_validSampleIntensities\"{Matrix<float, 0U, 1U, false>=\"m_data\"^f\"m_capacity\"Q\"m_rows\"I}\"m_validChromaSampleIDS\"{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__cap_\"^i}\"m_sampleIndices_all\"{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__cap_\"^i}\"m_validRtfs\"{Matrix<float, 0U, 0U, false>=\"m_data\"^f\"m_capacity\"Q\"m_rows\"I\"m_cols\"I}\"m_precomputedFaceData\"{shared_ptr<arkit::PrecomputedFaceData>=\"__ptr_\"^{PrecomputedFaceData}\"__cntrl_\"^{__shared_weak_count}}\"m_smoother\"{ExponentialSmoother<cva::Matrix<float, 9, 1>>=\"state\"{optional<cva::Matrix<float, 9, 1>>=\"\"(?=\"__null_state_\"c\"__val_\"{Matrix<float, 9U, 1U, false>=\"m_data\"[9f]})\"__engaged_\"B}}\"m_inliers\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
+ "{map<long, double, std::less<long>, std::allocator<std::pair<const long, double>>>=\"__tree_\"{__tree<std::__value_type<long, double>, std::__map_value_compare<long, std::__value_type<long, double>, std::less<long>>, std::allocator<std::__value_type<long, double>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::array<unsigned char, 16>, ARTexturedPlane, std::less<std::array<unsigned char, 16>>, std::allocator<std::pair<const std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__tree_\"{__tree<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>, std::allocator<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::array<unsigned char, 16>, ARTexturedPlane, std::less<std::array<unsigned char, 16>>, std::allocator<std::pair<const std::array<unsigned char, 16>, ARTexturedPlane>>>={__tree<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>, std::allocator<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}36@0:8r^v16r^v24B32"
+ "{optional<(anonymous namespace)::Undistorter>=\"\"(?=\"__null_state_\"c\"__val_\"{Undistorter=\"m_unrotatedImageWidth\"Q\"m_unrotatedImageHeight\"Q\"m_mappingU\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}\"m_mappingV\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}})\"__engaged_\"B}"
+ "{unordered_map<std::string_view, unsigned long, std::hash<basic_string_view<char, char_traits<char>>>, std::equal_to<std::string_view>, std::allocator<std::pair<const std::string_view, unsigned long>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string_view, unsigned long>, std::__unordered_map_hasher<std::string_view, std::__hash_value_type<std::string_view, unsigned long>, std::hash<basic_string_view<char, char_traits<char>>>, std::equal_to<std::string_view>>, std::__unordered_map_equal<std::string_view, std::__hash_value_type<std::string_view, unsigned long>, std::equal_to<std::string_view>, std::hash<basic_string_view<char, char_traits<char>>>>, std::allocator<std::__hash_value_type<std::string_view, unsigned long>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, unsigned long>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, unsigned long>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, unsigned long>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string_view, unsigned long>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<ARPatch, std::allocator<ARPatch>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<ARSRT, std::allocator<ARSRT>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=\"__begin_\"^{ARTexturedPlane}\"__end_\"^{ARTexturedPlane}\"__cap_\"^{ARTexturedPlane}}"
+ "{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}^{ARTexturedPlane}^{ARTexturedPlane}}16@0:8"
+ "{vector<__CVPixelBufferPool *, std::allocator<__CVPixelBufferPool *>>=\"__begin_\"^^{__CVPixelBufferPool}\"__end_\"^^{__CVPixelBufferPool}\"__cap_\"^^{__CVPixelBufferPool}}"
+ "{vector<espresso_buffer_t, std::allocator<espresso_buffer_t>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
+ "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
+ "{vector<short, std::allocator<short>>=\"__begin_\"^s\"__end_\"^s\"__cap_\"^s}"
+ "{vector<simd_float4x4, std::allocator<simd_float4x4>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<std::shared_ptr<const CV3DSLAMStateContext>, std::allocator<std::shared_ptr<const CV3DSLAMStateContext>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<unsigned char __attribute__((ext_vector_type(4))), std::allocator<unsigned char __attribute__((ext_vector_type(4)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
+ "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__cap_\"*}"
+ "{vector<unsigned char, std::allocator<unsigned char>>=***}16@0:8"
+ "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
+ "{vector<unsigned short __attribute__((ext_vector_type(4))), std::allocator<unsigned short __attribute__((ext_vector_type(4)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
+ "\xb2"
+ "\xf0\xf0Q"
+ "\xf0\xf0\xf0\xf0!"
- "\x1b[0m"
- "\x1b[1;31m"
- "\x1b[1;32m"
- "\x1b[1;33m"
- "\x1b[1;34m"
- "\x1b[1;35m"
- "\x1b[1;4;34m"
- "\x1b[1m"
- " arkitctl <COMMAND> [help]\n"
- "\"(%p)\"[label=\"{%@|(%p)"
- "%@ stopped location manager."
- "%@:%@"
- "%s: (%f, %f, %f)"
- "%{public}@"
- "%{public}@ <%p>: %@ Could not set all properties for defaultPhotoSettings because photo output has not been created yet."
- "%{public}@ <%p>: %@ Using photo quality prioritization: %ld"
- "%{public}@ <%p>: %@: No video frame received. Dropping frame! Reason: %ld"
- "%{public}@ <%p>: %@: Video frame received without camera calibration data. Dropping frame! Reason: %ld"
- "%{public}@ <%p>: %@: Video frame received without vision data. Reason: %ld"
- "%{public}@ <%p>: CM fusion is enabled."
- "%{public}@ <%p>: Disregarding location update for stopped sensor"
- "%{public}@ <%p>: Dropped a pointCloudDataOutput: %@"
- "%{public}@ <%p>: Unable to create alpha buffer for generating optical flow result pixelbuffer"
- "%{public}@ <%p>: _startService"
- "%{public}@ <%p>: started location updates."
- "%{public}@ <%p>: startedSensorDataTypes: %@  VS.  requiredDataTypes: %@ optionalDataTypes: %@"
- "%{public}s: ARLensType not configured in calibration directory"
- "1\""
- "9!\x0f\xfe "
- "@\"ADJasperColorPipelineParameters\""
- "@\"ARParametricLights\""
- "@104@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^}}16{vector<short, std::allocator<short>>=^s^s{__compressed_pair<short *, std::allocator<short>>=^s}}40Q647288"
- "@176@0:8{?=[3]}16{CGSize=dd}64q80Q8896128d144@152@160Q168"
- "@216@0:8{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 2, 1> *, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v}}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 2, 1> *, std::allocator<cva::Matrix<float, 2, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}}}16@192d200d208"
- "@248@0:8@16{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::array<unsigned char, 16>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<std::array<unsigned char, 16>>>=Q}}}@}24"
- "@40@0:816@32"
- "@40@0:8{set<unsigned long long, std::less<unsigned long long>, std::allocator<unsigned long long>>={__tree<unsigned long long, std::less<unsigned long long>, std::allocator<unsigned long long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long long>>=Q}}}16"
- "@44@0:8{vector<ARPatch, std::allocator<ARPatch>>=^{?}^{?}{__compressed_pair<ARPatch *, std::allocator<ARPatch>>=^{?}}}16f40"
- "@52@0:816f3236"
- "@64@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^}}16{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q{__compressed_pair<unsigned long long *, std::allocator<unsigned long long>>=^Q}}40"
- "@72@0:8d16{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}^{ARTexturedPlane}{__compressed_pair<ARTexturedPlane *, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}}}24@48@56@64"
- "@88@0:8{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^^{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=^}}16{vector<unsigned long long, std::allocator<unsigned long long>>=^Q^Q{__compressed_pair<unsigned long long *, std::allocator<unsigned long long>>=^Q}}40{vector<float, std::allocator<float>>=^f^f{__compressed_pair<float *, std::allocator<float>>=^f}}64"
- "A!"
- "ARAreaLight"
- "ARDepthMapData"
- "ARImageSensorData"
- "ARLensType ARGetLensTypeFromCalibrationDictionary(NSDictionary *__strong _Nonnull)"
- "ARObjectTrackingRemoteControl"
- "ARParametricLights"
- "ARRTRingBuffer.c"
- "AirplaneMode"
- "Alpha Ouput"
- "Error: %{public}@ <%p>: %@: No video frame received. Dropping frame! Reason: %ld"
- "Error: %{public}@ <%p>: %@: Video frame received without camera calibration data. Dropping frame! Reason: %ld"
- "Error: %{public}@ <%p>: %@: Video frame received without vision data. Reason: %ld"
- "Error: %{public}@ <%p>: Unable to create alpha buffer for generating optical flow result pixelbuffer"
- "Error: %{public}s: ARLensType not configured in calibration directory"
- "L' "
- "Localizable_iOS"
- "MLModels/%@"
- "MLModels/Debug"
- "MLModels/NonPrecompiled"
- "SFBSIconSystemName"
- "SFBSPresentationStyle"
- "SFBSSymbolForegroundStyle"
- "SFBSSymbolRenderingMode"
- "SSH_TTY"
- "T,N"
- "T,R,N,V_ambientColor"
- "T,R,N,V_color"
- "T@\"ADJasperColorPipelineParameters\",R,N,V_pipelineParameters"
- "T@\"ARParametricLights\",&,N,V_parametricLights"
- "T@\"NSArray\",R,N,V_areaLights"
- "TB,N,V_shouldOperateOnHighResolutionImages"
- "TQ,N"
- "TQ,N,V_lensType"
- "T^{CGImage=},&,N,V_depthMap"
- "T^{CGImage=},N,V_depthMap"
- "Td,N,V_estimatedLuminance"
- "Tf,N"
- "Tf,R,N,V_angularSize"
- "Tq,R,N,V_prioritization"
- "T{?=[3]},N"
- "T{?=[4]},R,N,V_originFromWorld"
- "T{?=[4]},R,N,V_worldFromOrigin"
- "T{?=[4]},V_extrinsicsToWideSensor"
- "T{CGSize=dd},N"
- "T{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 2, 1> *, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v}}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 2, 1> *, std::allocator<cva::Matrix<float, 2, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}}},N,V_chunkMesh"
- "T{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}},N,V_semanticsVector"
- "Usage:"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "_"
- "_alphamapAvailable"
- "_ambientColor"
- "_angularSize"
- "_applyPivotRotation"
- "_areaLights"
- "_changePowerUsage:forced:"
- "_defaultPhotoSettings"
- "_depthMap"
- "_estimatedLuminance"
- "_exposeInternalDepthData"
- "_isBravoCamOtherThanWideUsed"
- "_isStopped"
- "_lensType"
- "_originFromWorld"
- "_outputAlphaPixelBufferPool"
- "_parametricLights"
- "_pipelineParameters"
- "_previous3DSkeletonSemaphore"
- "_serverConnectionInterrupted"
- "_setPrimaryTechnique:secondaryTechnique:"
- "_shouldOperateOnHighResolutionImages"
- "_startSensorsWithRequiredDataTypes:optionalDataTypes:"
- "_submitResultsForTimestamp:context:"
- "_updateAnchorsForFrame:resultDatas:context:addedAnchors:updatedAnchors:removedAnchors:externalAnchors:"
- "_updatePowerUsageForced:"
- "_updateThermalState:"
- "_worldFromOrigin"
- "alphaMapOutput"
- "ambientColor"
- "angularSize"
- "ar_rt_ring_buffer_add_element"
- "ar_rt_ring_buffer_decrement_index"
- "ar_rt_ring_buffer_empty"
- "ar_rt_ring_buffer_filled"
- "ar_rt_ring_buffer_increment_index"
- "ar_rt_ring_buffer_init"
- "ar_rt_ring_buffer_reset"
- "areaLights"
- "clientBundleIdentifier"
- "com.apple."
- "com.apple.arkit.appleDepthSPI.bundleID.approvedList"
- "com.apple.arkit.configuration.shouldProvideNonBinnedVideoFormats"
- "com.apple.arkit.geotracking.usecmfusion"
- "com.apple.arkit.planeEstimation.anchorRotation"
- "depthMap"
- "didSetWorldOrigin"
- "dotGraphWithLines:"
- "estimatedLuminance"
- "fileExistsAtPath:isDirectory:"
- "findMergedPlanes::"
- "forceUpdatePowerUsage:"
- "fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:"
- "imageWithCVPixelBuffer:options:"
- "initWithAmbientColor:areaLights:"
- "initWithDaemon:startConnection:dispatchChannelQueue:"
- "initWithDirection:angularSize:color:"
- "initWithDispatchChannelQueue:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithIntrinsics:imageResolution:devicePosition:lensType:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:"
- "initWithMachServiceName:exportedInterface:remoteObjectInterface:dispatchChannelQueue:"
- "lensType"
- "maxPhotoDimensionsForVideoFormat:maximumHeight:"
- "maxPhotoQualityPrioritization"
- "mergeResultsOfContext:resultFilterBlock:"
- "mutableDepthSettings"
- "mutableSettings"
- "optionalSensorDataTypes"
- "parametricLights"
- "pathForResource:ofType:inDirectory:"
- "resolutionDictionaryForKey:"
- "ring_buffer"
- "setDepthMap:"
- "setEstimatedLuminance:"
- "setLensType:"
- "setParametricLights:"
- "setShouldOperateOnHighResolutionImages:"
- "shouldOperateOnHighResolutionImages"
- "size >= 0"
- "stringByStandardizingPath"
- "techinqueInArray:passingTest:"
- "uppercaseString"
- "v192@0:8{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 2, 1> *, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v}}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 2, 1> *, std::allocator<cva::Matrix<float, 2, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}}}16"
- "v24@0:8@\"NSMutableArray\"16"
- "v24@0:8^{CGImage=}16"
- "v28@0:8Q16B24"
- "v376@0:8^{__CVBuffer=}16f24{?=[3]}28{?=[4]}76{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::array<unsigned char, 16>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<std::array<unsigned char, 16>>>=Q}}}@}140Q364B372"
- "v40@0:8{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}16"
- "v476@0:8{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::array<unsigned char, 16>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<std::array<unsigned char, 16>>>=Q}}}@}16{ARTexturedPlane={array<unsigned char, 16UL>=[16C]}Q{?=[4]}{array<float __attribute__((ext_vector_type(3))), 4UL>=[4]}{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>={__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::array<unsigned char, 16>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<std::array<unsigned char, 16>>>=Q}}}@}240Q464B472"
- "v72@0:8@16@24@32@40@48@56@64"
- "warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:previousNormals:intoCurrentNormals:usingPoseDelta:previousCalibration:currentCalibration:"
- "{?=ii}28@0:8@16i24"
- "{ARPlaneUpdateQueue=\"queue\"{queue<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>, std::deque<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"c\"{deque<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__map_\"{__split_buffer<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> *, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"__end_cap_\"{__compressed_pair<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> **, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane> *>>=\"__value_\"^^v}}\"__start_\"Q\"__size_\"{__compressed_pair<unsigned long, std::allocator<std::pair<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__value_\"Q}}}\"elements\"{set<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=\"__tree_\"{__tree<std::array<unsigned char, 16>, std::less<std::array<unsigned char, 16>>, std::allocator<std::array<unsigned char, 16>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::array<unsigned char, 16>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<std::array<unsigned char, 16>>>=\"__value_\"Q}}}}"
- "{ChunkMesh=\"chunk_position\"{Matrix<short, 3U, 1U, false>=\"m_data\"[3s]}\"mesh\"{TriMesh<float, unsigned int>=\"vertices\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=\"__value_\"^v}}\"colors\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=\"__value_\"^v}}\"normals\"{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=\"__value_\"^v}}\"faces\"{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__value_\"^v}}\"edges\"{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<unsigned int, 2, 1> *, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=\"__value_\"^v}}\"tex_coords\"{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<float, 2, 1> *, std::allocator<cva::Matrix<float, 2, 1>>>=\"__value_\"^v}}\"tex_faces\"{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=\"__value_\"^v}}}}"
- "{ChunkMesh={Matrix<short, 3U, 1U, false>=[3s]}{TriMesh<float, unsigned int>={vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<float, 3, 1>, std::allocator<cva::Matrix<float, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 3, 1> *, std::allocator<cva::Matrix<float, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 2, 1>, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 2, 1> *, std::allocator<cva::Matrix<unsigned int, 2, 1>>>=^v}}{vector<cva::Matrix<float, 2, 1>, std::allocator<cva::Matrix<float, 2, 1>>>=^v^v{__compressed_pair<cva::Matrix<float, 2, 1> *, std::allocator<cva::Matrix<float, 2, 1>>>=^v}}{vector<cva::Matrix<unsigned int, 3, 1>, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v^v{__compressed_pair<cva::Matrix<unsigned int, 3, 1> *, std::allocator<cva::Matrix<unsigned int, 3, 1>>>=^v}}}}16@0:8"
- "{FacialLightEstimation=\"m_validSampleIntensities\"{Matrix<float, 0U, 1U, false>=\"m_data\"^f\"m_capacity\"Q\"m_rows\"I}\"m_validChromaSampleIDS\"{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__end_cap_\"{__compressed_pair<int *, std::allocator<int>>=\"__value_\"^i}}\"m_sampleIndices_all\"{vector<int, std::allocator<int>>=\"__begin_\"^i\"__end_\"^i\"__end_cap_\"{__compressed_pair<int *, std::allocator<int>>=\"__value_\"^i}}\"m_validRtfs\"{Matrix<float, 0U, 0U, false>=\"m_data\"^f\"m_capacity\"Q\"m_rows\"I\"m_cols\"I}\"m_precomputedFaceData\"{shared_ptr<arkit::PrecomputedFaceData>=\"__ptr_\"^{PrecomputedFaceData}\"__cntrl_\"^{__shared_weak_count}}\"m_smoother\"{ExponentialSmoother<cva::Matrix<float, 9, 1>>=\"state\"{optional<cva::Matrix<float, 9, 1>>=\"\"(?=\"__null_state_\"c\"__val_\"{Matrix<float, 9U, 1U, false>=\"m_data\"[9f]})\"__engaged_\"B}}\"m_inliers\"{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{map<long, double, std::less<long>, std::allocator<std::pair<const long, double>>>=\"__tree_\"{__tree<std::__value_type<long, double>, std::__map_value_compare<long, std::__value_type<long, double>, std::less<long>>, std::allocator<std::__value_type<long, double>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<long, double>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<long, std::__value_type<long, double>, std::less<long>>>=\"__value_\"Q}}}"
- "{map<std::array<unsigned char, 16>, ARTexturedPlane, std::less<std::array<unsigned char, 16>>, std::allocator<std::pair<const std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__tree_\"{__tree<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>, std::allocator<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>>=\"__value_\"Q}}}"
- "{map<std::array<unsigned char, 16>, ARTexturedPlane, std::less<std::array<unsigned char, 16>>, std::allocator<std::pair<const std::array<unsigned char, 16>, ARTexturedPlane>>>={__tree<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>, std::allocator<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, ARTexturedPlane>, std::less<std::array<unsigned char, 16>>>>=Q}}}36@0:8r^v16r^v24B32"
- "{map<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>, std::less<std::array<unsigned char, 16>>, std::allocator<std::pair<const std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>>>={__tree<std::__value_type<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>, std::less<std::array<unsigned char, 16>>>, std::allocator<std::__value_type<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::array<unsigned char, 16>, std::__value_type<std::array<unsigned char, 16>, std::set<std::array<unsigned char, 16>>>, std::less<std::array<unsigned char, 16>>>>=Q}}}32@0:8r^v16r^v24"
- "{optional<(anonymous namespace)::Undistorter>=\"\"(?=\"__null_state_\"c\"__val_\"{Undistorter=\"m_unrotatedImageWidth\"Q\"m_unrotatedImageHeight\"Q\"m_mappingU\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}\"m_mappingV\"{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}})\"__engaged_\"B}"
- "{vector<ARPatch, std::allocator<ARPatch>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<ARPatch *, std::allocator<ARPatch>>=\"__value_\"^{?}}}"
- "{vector<ARSRT, std::allocator<ARSRT>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<ARSRT *, std::allocator<ARSRT>>=\"__value_\"^{?}}}"
- "{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=\"__begin_\"^{ARTexturedPlane}\"__end_\"^{ARTexturedPlane}\"__end_cap_\"{__compressed_pair<ARTexturedPlane *, std::allocator<ARTexturedPlane>>=\"__value_\"^{ARTexturedPlane}}}"
- "{vector<ARTexturedPlane, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}^{ARTexturedPlane}{__compressed_pair<ARTexturedPlane *, std::allocator<ARTexturedPlane>>=^{ARTexturedPlane}}}16@0:8"
- "{vector<__CVPixelBufferPool *, std::allocator<__CVPixelBufferPool *>>=\"__begin_\"^^{__CVPixelBufferPool}\"__end_\"^^{__CVPixelBufferPool}\"__end_cap_\"{__compressed_pair<__CVPixelBufferPool **, std::allocator<__CVPixelBufferPool *>>=\"__value_\"^^{__CVPixelBufferPool}}}"
- "{vector<espresso_buffer_t, std::allocator<espresso_buffer_t>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<espresso_buffer_t *, std::allocator<espresso_buffer_t>>=\"__value_\"^{?}}}"
- "{vector<float __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(2))), std::allocator<float __attribute__((ext_vector_type(2)))>>=\"__value_\"^}}"
- "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__value_\"^}}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "{vector<short, std::allocator<short>>=\"__begin_\"^s\"__end_\"^s\"__end_cap_\"{__compressed_pair<short *, std::allocator<short>>=\"__value_\"^s}}"
- "{vector<simd_float4x4, std::allocator<simd_float4x4>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<simd_float4x4 *, std::allocator<simd_float4x4>>=\"__value_\"^{?}}}"
- "{vector<std::shared_ptr<const CV3DSLAMStateContext>, std::allocator<std::shared_ptr<const CV3DSLAMStateContext>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::shared_ptr<const CV3DSLAMStateContext> *, std::allocator<std::shared_ptr<const CV3DSLAMStateContext>>>=\"__value_\"^v}}"
- "{vector<unsigned char __attribute__((ext_vector_type(4))), std::allocator<unsigned char __attribute__((ext_vector_type(4)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<unsigned char * __attribute__((ext_vector_type(4))), std::allocator<unsigned char __attribute__((ext_vector_type(4)))>>=\"__value_\"^}}"
- "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__end_cap_\"{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=\"__value_\"*}}"
- "{vector<unsigned char, std::allocator<unsigned char>>=**{__compressed_pair<unsigned char *, std::allocator<unsigned char>>=*}}16@0:8"
- "{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long long *, std::allocator<unsigned long long>>=\"__value_\"^Q}}"
- "{vector<unsigned short __attribute__((ext_vector_type(4))), std::allocator<unsigned short __attribute__((ext_vector_type(4)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<unsigned short * __attribute__((ext_vector_type(4))), std::allocator<unsigned short __attribute__((ext_vector_type(4)))>>=\"__value_\"^}}"
- "|HighResOnly"
- "\xa0&\x0f\xfe "
- "\xa2"
- "\xf0\xf01"
- "\xf0\xf0\xf0\xa1"

```
