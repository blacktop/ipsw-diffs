## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

 664.2.10.0.0
-  __TEXT.__text: 0x10455c
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xdee4
-  __TEXT.__const: 0x918
-  __TEXT.__gcc_except_tab: 0x24e0
-  __TEXT.__cstring: 0x1d07b
-  __TEXT.__oslogstring: 0x6c0b
-  __TEXT.__dlopen_cstrs: 0x178
+  __TEXT.__text: 0x1197d4
+  __TEXT.__auth_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0xef04
+  __TEXT.__const: 0x980
+  __TEXT.__gcc_except_tab: 0x2740
+  __TEXT.__cstring: 0x1fabb
+  __TEXT.__oslogstring: 0x7fe1
+  __TEXT.__dlopen_cstrs: 0x1d0
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x4608
-  __TEXT.__objc_classname: 0x17d3
-  __TEXT.__objc_methname: 0x26d58
-  __TEXT.__objc_methtype: 0x3c78
-  __TEXT.__objc_stubs: 0x16a40
-  __DATA_CONST.__got: 0x27a8
-  __DATA_CONST.__const: 0x6fc8
-  __DATA_CONST.__objc_classlist: 0x580
+  __TEXT.__unwind_info: 0x4b10
+  __TEXT.__objc_classname: 0x1996
+  __TEXT.__objc_methname: 0x2a375
+  __TEXT.__objc_methtype: 0x4042
+  __TEXT.__objc_stubs: 0x18800
+  __DATA_CONST.__got: 0x2978
+  __DATA_CONST.__const: 0x7a38
+  __DATA_CONST.__objc_classlist: 0x5d8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71b0
+  __DATA_CONST.__objc_selrefs: 0x7a50
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x4c0
-  __DATA_CONST.__objc_arraydata: 0x428
-  __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x13280
-  __AUTH_CONST.__objc_const: 0x16850
-  __AUTH_CONST.__objc_intobj: 0x9f0
+  __DATA_CONST.__objc_superrefs: 0x510
+  __DATA_CONST.__objc_arraydata: 0x450
+  __AUTH_CONST.__auth_got: 0xea0
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x141e0
+  __AUTH_CONST.__objc_const: 0x184d8
+  __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x17dc
-  __DATA.__data: 0xc08
-  __DATA.__bss: 0x6f0
-  __DATA.__common: 0x80
+  __AUTH.__objc_data: 0xaa0
+  __DATA.__objc_ivar: 0x19d8
+  __DATA.__data: 0xcc0
+  __DATA.__bss: 0x7a0
+  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0x2fd0
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x1c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D57F4D4-C18F-309B-877B-2C9255171757
-  Functions: 5851
-  Symbols:   20760
-  CStrings:  11638
+  UUID: 95121CE8-5577-3237-8EA7-FAE3CD461C05
+  Functions: 6312
+  Symbols:   22326
+  CStrings:  12520
 
Symbols:
+ +[AVCaptureDeviceDynamicAspectRatioRequest dynamicAspectRatioRequestWithCompletionBlock:requestID:]
+ +[AVCaptureExternalDisplayConfigurator initialize]
+ +[AVCaptureExternalDisplayConfigurator isBypassingColorSpaceConversionSupported]
+ +[AVCaptureExternalDisplayConfigurator isMatchingFrameRateSupported]
+ +[AVCaptureExternalDisplayConfigurator isPreferredResolutionSupported]
+ +[AVCaptureExternalDisplayConfigurator isSupported]
+ +[AVCaptureExternalDisplayConfigurator registerConfigurator:withDisplayIdentifier:]
+ +[AVCaptureExternalDisplayConfigurator registerConfigurator:withDisplayIdentifier:].cold.1
+ +[AVCaptureFraming framingWithAspectRatio:zoomFactor:]
+ +[AVCaptureFraming initialize]
+ +[AVCaptureOutput supportedProResRawCodecTypes]
+ +[AVCaptureSmartFraming initialize]
+ +[AVCaptureSmartFraming smartFramingWithAspectRatio:zoomFactor:]
+ +[AVCaptureSmartFramingMonitor initialize]
+ +[AVCaptureTimecodeGenerator frameCountSource]
+ +[AVCaptureTimecodeGenerator realTimeClockSource]
+ +[AVExternalSyncDevice initialize]
+ +[AVExternalSyncDeviceDiscoverySession initialize]
+ +[AVExternalSyncDeviceDiscoverySession isSupported]
+ +[AVExternalSyncDeviceDiscoverySession isSupported].cold.1
+ +[AVExternalSyncDeviceDiscoverySession sharedSession]
+ +[AVExternalSyncDeviceDiscoverySession sharedSession].cold.1
+ -[AVCaptureDevice isFollowingExternalSyncDevice]
+ -[AVCaptureDevice isVideoFrameDurationLocked]
+ -[AVCaptureDevice minSupportedExternalSyncFrameDuration]
+ -[AVCaptureDevice minSupportedLockedVideoFrameDuration]
+ -[AVCaptureDevice resetActiveLockedVideoFrameDurationForOwner:]
+ -[AVCaptureDevice setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:]
+ -[AVCaptureDevice setActiveLockedVideoFrameDuration:forOwner:]
+ -[AVCaptureDevice setActiveSyncDevice:]
+ -[AVCaptureDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:]
+ -[AVCaptureDevice(DockKit) isDockedTrackingActive]
+ -[AVCaptureDevice(DynamicAspectRatio) dynamicAspectRatioAndDynamicAspectRatioRequestID]
+ -[AVCaptureDevice(DynamicAspectRatio) dynamicAspectRatioRequestID]
+ -[AVCaptureDevice(DynamicAspectRatio) dynamicAspectRatio]
+ -[AVCaptureDevice(DynamicAspectRatio) dynamicDimensions]
+ -[AVCaptureDevice(DynamicAspectRatio) setDynamicAspectRatio:completionHandler:]
+ -[AVCaptureDevice(OutputAspectRatio_SPI) outputAspectRatio]
+ -[AVCaptureDevice(OutputAspectRatio_SPI) outputDimensions]
+ -[AVCaptureDevice(OutputAspectRatio_SPI) setOutputAspectRatio:completionHandler:]
+ -[AVCaptureDevice(SmartFramingMonitoringInternal) isSmartFramingMonitoringSupported]
+ -[AVCaptureDevice(SmartFramingMonitoringInternal) smartFramingMonitor]
+ -[AVCaptureDeviceDynamicAspectRatioRequest _initWithCompletionBlock:requestID:]
+ -[AVCaptureDeviceDynamicAspectRatioRequest dealloc]
+ -[AVCaptureDeviceDynamicAspectRatioRequest dynamicAspectRatioCompletionBlock]
+ -[AVCaptureDeviceFormat geometricDistortionCorrectedVideoFieldOfViewForAspectRatio:]
+ -[AVCaptureDeviceFormat isMountedInPortraitOrientation]
+ -[AVCaptureDeviceFormat isSmartCropSupported]
+ -[AVCaptureDeviceFormat isSmartFramingSupported]
+ -[AVCaptureDeviceFormat supportedDynamicAspectRatios]
+ -[AVCaptureDeviceFormat supportedOutputAspectRatios]
+ -[AVCaptureDeviceFormat videoFieldOfViewForAspectRatio:]
+ -[AVCaptureDeviceFormat videoFieldOfViewForAspectRatio:geometricDistortionCorrected:]
+ -[AVCaptureDeviceInput _applyActiveExternalSyncVideoFrameDuration]
+ -[AVCaptureDeviceInput _applyActiveLockedVideoFrameDuration]
+ -[AVCaptureDeviceInput _resetActiveLockedVideoFrameDurationWithFormatChanged:]
+ -[AVCaptureDeviceInput _setGenlockSignalCompensationDelay:]
+ -[AVCaptureDeviceInput _updateExternalSyncSupported]
+ -[AVCaptureDeviceInput _updateLockedVideoFrameDurationSupported]
+ -[AVCaptureDeviceInput activeExternalSyncVideoFrameDuration]
+ -[AVCaptureDeviceInput activeLockedVideoFrameDuration]
+ -[AVCaptureDeviceInput externalSyncDevice]
+ -[AVCaptureDeviceInput followExternalSyncDevice:videoFrameDuration:delegate:]
+ -[AVCaptureDeviceInput isExternalSyncSupported]
+ -[AVCaptureDeviceInput isLockedVideoFrameDurationSupported]
+ -[AVCaptureDeviceInput setActiveLockedVideoFrameDuration:]
+ -[AVCaptureDeviceInput unfollowExternalSyncDevice]
+ -[AVCaptureExternalDisplayConfiguration bypassColorSpaceConversion]
+ -[AVCaptureExternalDisplayConfiguration description]
+ -[AVCaptureExternalDisplayConfiguration preferredResolution]
+ -[AVCaptureExternalDisplayConfiguration setBypassColorSpaceConversion:]
+ -[AVCaptureExternalDisplayConfiguration setPreferredResolution:]
+ -[AVCaptureExternalDisplayConfiguration setShouldMatchFrameRate:]
+ -[AVCaptureExternalDisplayConfiguration shouldMatchFrameRate]
+ -[AVCaptureExternalDisplayConfigurator _configureExternalDisplayColorspace]
+ -[AVCaptureExternalDisplayConfigurator _configureExternalDisplayFrameRate]
+ -[AVCaptureExternalDisplayConfigurator _configureExternalDisplay]
+ -[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorConfigure]
+ -[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorTeardown]
+ -[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorConfigure]
+ -[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorTeardown]
+ -[AVCaptureExternalDisplayConfigurator _dispatchConfiguration]
+ -[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorConfigure]
+ -[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorTeardown]
+ -[AVCaptureExternalDisplayConfigurator _externalDisplayConfigurationChangedHandler]
+ -[AVCaptureExternalDisplayConfigurator _getConfigurationWithCompletion:]
+ -[AVCaptureExternalDisplayConfigurator _makeInActive]
+ -[AVCaptureExternalDisplayConfigurator _setup]
+ -[AVCaptureExternalDisplayConfigurator activeExternalDisplayFrameRate]
+ -[AVCaptureExternalDisplayConfigurator dealloc]
+ -[AVCaptureExternalDisplayConfigurator description]
+ -[AVCaptureExternalDisplayConfigurator device]
+ -[AVCaptureExternalDisplayConfigurator dispatchConfiguration]
+ -[AVCaptureExternalDisplayConfigurator externalDisplayAndCaptureDeviceSynchronized]
+ -[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:]
+ -[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:].cold.1
+ -[AVCaptureExternalDisplayConfigurator externalDisplayLayerObserver:visibiltyChanged:]
+ -[AVCaptureExternalDisplayConfigurator identifier]
+ -[AVCaptureExternalDisplayConfigurator initWithDevice:previewLayer:configuration:]
+ -[AVCaptureExternalDisplayConfigurator isActive]
+ -[AVCaptureExternalDisplayConfigurator observeValueForKeyPath:ofObject:change:context:]
+ -[AVCaptureExternalDisplayConfigurator observingDeviceColorspace]
+ -[AVCaptureExternalDisplayConfigurator observingDeviceFramerate]
+ -[AVCaptureExternalDisplayConfigurator previewLayer]
+ -[AVCaptureExternalDisplayConfigurator registerSelfForDisplay:]
+ -[AVCaptureExternalDisplayConfigurator registered]
+ -[AVCaptureExternalDisplayConfigurator retryConfiguration]
+ -[AVCaptureExternalDisplayConfigurator setActive:]
+ -[AVCaptureExternalDisplayConfigurator setActiveExternalDisplayFrameRate:]
+ -[AVCaptureExternalDisplayConfigurator setObservingDeviceColorspace:]
+ -[AVCaptureExternalDisplayConfigurator setObservingDeviceFramerate:]
+ -[AVCaptureExternalDisplayConfigurator setRegistered:]
+ -[AVCaptureExternalDisplayConfigurator setRetryConfiguration:]
+ -[AVCaptureExternalDisplayConfigurator stop]
+ -[AVCaptureFigVideoDevice _drainDynamicAspectRatioRequestQueue]
+ -[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]
+ -[AVCaptureFigVideoDevice _setEnabledSmartFramingFieldsOfView:]
+ -[AVCaptureFigVideoDevice _setSmartFramingMonitorRunning:]
+ -[AVCaptureFigVideoDevice _updateRectOfInterestSizeForSensorOrientationAndDynamicAspectRatio:]
+ -[AVCaptureFigVideoDevice activeExternalSyncVideoFrameDuration]
+ -[AVCaptureFigVideoDevice activeLockedVideoFrameDuration]
+ -[AVCaptureFigVideoDevice drainDynamicAspectRatioCompletionHandlers]
+ -[AVCaptureFigVideoDevice dynamicAspectRatioAndDynamicAspectRatioRequestID]
+ -[AVCaptureFigVideoDevice dynamicAspectRatioRequestID]
+ -[AVCaptureFigVideoDevice dynamicAspectRatio]
+ -[AVCaptureFigVideoDevice dynamicDimensions]
+ -[AVCaptureFigVideoDevice isDockedTrackingActive]
+ -[AVCaptureFigVideoDevice isFollowingExternalSyncDevice]
+ -[AVCaptureFigVideoDevice isSmartFramingMonitoringSupported]
+ -[AVCaptureFigVideoDevice isVideoFrameDurationLocked]
+ -[AVCaptureFigVideoDevice minSupportedExternalSyncFrameDuration]
+ -[AVCaptureFigVideoDevice minSupportedLockedVideoFrameDuration]
+ -[AVCaptureFigVideoDevice resetActiveLockedVideoFrameDurationForOwner:]
+ -[AVCaptureFigVideoDevice resetDeviceClockAndInputPortsToHostClock]
+ -[AVCaptureFigVideoDevice setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:]
+ -[AVCaptureFigVideoDevice setActiveLockedVideoFrameDuration:forOwner:]
+ -[AVCaptureFigVideoDevice setActiveSyncDevice:]
+ -[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:]
+ -[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]
+ -[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:].cold.1
+ -[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:].cold.2
+ -[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:]
+ -[AVCaptureFigVideoDevice smartFramingMonitor]
+ -[AVCaptureFraming _initWithAspectRatio:zoomFactor:]
+ -[AVCaptureFraming aspectRatio]
+ -[AVCaptureFraming copyWithZone:]
+ -[AVCaptureFraming dealloc]
+ -[AVCaptureFraming debugDescription]
+ -[AVCaptureFraming description]
+ -[AVCaptureFraming isEqual:]
+ -[AVCaptureFraming zoomFactor]
+ -[AVCaptureMovieFileOutput _invokeClientCompositingCallbackForSettingsID:compositingData:]
+ -[AVCaptureMovieFileOutput _isProResRawRecordingAndAWBIsNotLockedForWrapper:]
+ -[AVCaptureMovieFileOutput handleChangedMSGPulseDurationForDevice:]
+ -[AVCaptureMovieFileOutput isMultiCamClientCompositingEnabled]
+ -[AVCaptureMovieFileOutput isMultiCamClientCompositingSupported]
+ -[AVCaptureMovieFileOutput multiCamClientCompositingPrimaryConnection]
+ -[AVCaptureMovieFileOutput setMultiCamClientCompositingEnabled:]
+ -[AVCaptureMovieFileOutput setMultiCamClientCompositingPrimaryConnection:secondaryConnection:]
+ -[AVCaptureMultiCamClientCompositingData _imageForGainMapSampleBuffer:]
+ -[AVCaptureMultiCamClientCompositingData _imageForSampleBuffer:gainMapMetadata:]
+ -[AVCaptureMultiCamClientCompositingData _initWithPrimarySampleBuffer:primaryGainMapSampleBuffer:secondarySampleBuffer:secondaryGainMapSampleBuffer:outputSampleBuffer:outputGainMapSampleBuffer:]
+ -[AVCaptureMultiCamClientCompositingData compositingMetadata]
+ -[AVCaptureMultiCamClientCompositingData dealloc]
+ -[AVCaptureMultiCamClientCompositingData outputGainMapSampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData outputSampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData primaryGainMapImage]
+ -[AVCaptureMultiCamClientCompositingData primaryGainMapSampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData primaryImage]
+ -[AVCaptureMultiCamClientCompositingData primarySampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData secondaryGainMapImage]
+ -[AVCaptureMultiCamClientCompositingData secondaryGainMapSampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData secondaryImage]
+ -[AVCaptureMultiCamClientCompositingData secondarySampleBuffer]
+ -[AVCaptureMultiCamClientCompositingData setCompositingMetadata:]
+ -[AVCaptureOutput _invokeClientCompositingCallbackForSettingsID:compositingData:]
+ -[AVCaptureOutput handleChangedDynamicAspectRatio:forFormat:]
+ -[AVCaptureOutput updateMetadataTransformForSourceFormat:aspectRatio:]
+ -[AVCapturePhotoOutput _invokeClientCompositingCallbackForSettingsID:compositingData:]
+ -[AVCapturePhotoOutput _updateCameraSensorOrientationCompensationSupportedForDevice:]
+ -[AVCapturePhotoOutput isCameraSensorOrientationCompensationEnabled]
+ -[AVCapturePhotoOutput isCameraSensorOrientationCompensationSupported]
+ -[AVCapturePhotoOutput isMultiCamClientCompositingEnabled]
+ -[AVCapturePhotoOutput isMultiCamClientCompositingSupported]
+ -[AVCapturePhotoOutput multiCamClientCompositingPrimaryConnection]
+ -[AVCapturePhotoOutput setCameraSensorOrientationCompensationEnabled:]
+ -[AVCapturePhotoOutput setMultiCamClientCompositingEnabled:]
+ -[AVCapturePhotoOutput setMultiCamClientCompositingPrimaryConnection:secondaryConnection:]
+ -[AVCaptureSession _invokeClientCompositingCallbackForSinkID:settingsID:compositingData:]
+ -[AVCaptureSession _updateMultiCamClientCompositingCallback]
+ -[AVCaptureSmartFraming _initWithAspectRatio:zoomFactor:]
+ -[AVCaptureSmartFraming aspectRatio]
+ -[AVCaptureSmartFraming copyWithZone:]
+ -[AVCaptureSmartFraming dealloc]
+ -[AVCaptureSmartFraming debugDescription]
+ -[AVCaptureSmartFraming description]
+ -[AVCaptureSmartFraming isEqual:]
+ -[AVCaptureSmartFraming zoomFactor]
+ -[AVCaptureSmartFramingMonitor _handleChangedActiveFormat:]
+ -[AVCaptureSmartFramingMonitor _populatePhotoModeSmartFramingsAndFieldsOfViewFromZoomFactorsByFieldOfView:]
+ -[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForFramings:]
+ -[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForSmartFramings:]
+ -[AVCaptureSmartFramingMonitor dealloc]
+ -[AVCaptureSmartFramingMonitor debugDescription]
+ -[AVCaptureSmartFramingMonitor description]
+ -[AVCaptureSmartFramingMonitor device]
+ -[AVCaptureSmartFramingMonitor enabledFramings]
+ -[AVCaptureSmartFramingMonitor enabledSmartFramings]
+ -[AVCaptureSmartFramingMonitor initWithDevice:smartFramingZoomFactorsByFieldOfView:]
+ -[AVCaptureSmartFramingMonitor isMonitoring]
+ -[AVCaptureSmartFramingMonitor observeValueForKeyPath:ofObject:change:context:]
+ -[AVCaptureSmartFramingMonitor recommendedFraming]
+ -[AVCaptureSmartFramingMonitor recommendedSmartFraming]
+ -[AVCaptureSmartFramingMonitor setEnabledFramings:]
+ -[AVCaptureSmartFramingMonitor setEnabledSmartFramings:]
+ -[AVCaptureSmartFramingMonitor startMonitoring:]
+ -[AVCaptureSmartFramingMonitor startMonitoringWithError:]
+ -[AVCaptureSmartFramingMonitor stopMonitoring]
+ -[AVCaptureSmartFramingMonitor supportedFramings]
+ -[AVCaptureSmartFramingMonitor supportedSmartFramings]
+ -[AVCaptureSmartFramingMonitor updateRecommendedSmartFramingWithFieldOfView:]
+ -[AVCaptureStillImageOutput _updateCameraSensorOrientationCompensationSupportedForDevice:]
+ -[AVCaptureStillImageOutput isCameraSensorOrientationCompensationEnabled]
+ -[AVCaptureStillImageOutput isCameraSensorOrientationCompensationSupported]
+ -[AVCaptureStillImageOutput setCameraSensorOrientationCompensationEnabled:]
+ -[AVCaptureTimecodeGenerator _addTimecodeToRingBuffer:timestamp:]
+ -[AVCaptureTimecodeGenerator _isTimecodeRingBufferEmpty]
+ -[AVCaptureTimecodeGenerator _isTimecodeRingBufferStale]
+ -[AVCaptureTimecodeGenerator _newestTimecodeRingBufferEntry]
+ -[AVCaptureTimecodeGenerator _notifyDelegateOfSourceListUpdate:]
+ -[AVCaptureTimecodeGenerator _notifyDelegateOfSynchronizationStatusChange:filterRedundancy:]
+ -[AVCaptureTimecodeGenerator _notifyDelegateOfTimecodeUpdate:]
+ -[AVCaptureTimecodeGenerator _openMidiTimecodeDataStreamWithUUID:success:]
+ -[AVCaptureTimecodeGenerator _openMidiTimecodeDataStreamWithUUID:success:].cold.1
+ -[AVCaptureTimecodeGenerator _pollRingBufferStatus]
+ -[AVCaptureTimecodeGenerator _registerMidiEndpointAsSynchronizationSource:]
+ -[AVCaptureTimecodeGenerator _registerSynchronizationSource:]
+ -[AVCaptureTimecodeGenerator _removeMidiEndpointAsSynchronizationSource:]
+ -[AVCaptureTimecodeGenerator _removeSynchronizationSource:]
+ -[AVCaptureTimecodeGenerator _resetTimecodeRingBuffer]
+ -[AVCaptureTimecodeGenerator _scheduleTimecodeRingBufferPolling]
+ -[AVCaptureTimecodeGenerator _timeOfDay]
+ -[AVCaptureTimecodeGenerator _timecodeIsCoherent:]
+ -[AVCaptureTimecodeGenerator availableSources]
+ -[AVCaptureTimecodeGenerator callbackQueue]
+ -[AVCaptureTimecodeGenerator currentSource]
+ -[AVCaptureTimecodeGenerator dealloc]
+ -[AVCaptureTimecodeGenerator delegateCallbackQueue]
+ -[AVCaptureTimecodeGenerator delegate]
+ -[AVCaptureTimecodeGenerator generateInitialTimecode]
+ -[AVCaptureTimecodeGenerator init]
+ -[AVCaptureTimecodeGenerator setDelegate:queue:]
+ -[AVCaptureTimecodeGenerator setSynchronizationTimeout:]
+ -[AVCaptureTimecodeGenerator setTimecodeAlignmentOffset:]
+ -[AVCaptureTimecodeGenerator setTimecodeFrameDuration:]
+ -[AVCaptureTimecodeGenerator startExternalSourceObserver]
+ -[AVCaptureTimecodeGenerator startSynchronizationWithTimecodeSource:]
+ -[AVCaptureTimecodeGenerator synchronizationTimeout]
+ -[AVCaptureTimecodeGenerator timecodeAlignmentOffset]
+ -[AVCaptureTimecodeGenerator timecodeFrameDuration]
+ -[AVCaptureTimecodeSource copyWithZone:]
+ -[AVCaptureTimecodeSource dealloc]
+ -[AVCaptureTimecodeSource displayName]
+ -[AVCaptureTimecodeSource hash]
+ -[AVCaptureTimecodeSource initWithDisplayName:sourceType:uuid:]
+ -[AVCaptureTimecodeSource isEqual:]
+ -[AVCaptureTimecodeSource type]
+ -[AVCaptureTimecodeSource utilizesRingBufferSyncDiscipline]
+ -[AVCaptureTimecodeSource uuid]
+ -[AVCaptureVideoDataOutput recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:]
+ -[AVCaptureVideoDataOutput updateClientVideoSettingsForAspectRatio:]
+ -[AVCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:]
+ -[AVExternalSyncDevice _handleSourceDiedEvent]
+ -[AVExternalSyncDevice _handleUSBConnectionStateChange:]
+ -[AVExternalSyncDevice _handleUnfollow]
+ -[AVExternalSyncDevice _initWithIdentifier:pid:vid:]
+ -[AVExternalSyncDevice _notifyDelegateOfError:]
+ -[AVExternalSyncDevice _setClock:]
+ -[AVExternalSyncDevice _setDelegate:]
+ -[AVExternalSyncDevice _setupStateMachine]
+ -[AVExternalSyncDevice applyActiveExternalSyncVideoFrameDuration]
+ -[AVExternalSyncDevice clock]
+ -[AVExternalSyncDevice configurationTimeoutBlock]
+ -[AVExternalSyncDevice dealloc]
+ -[AVExternalSyncDevice handleClockReceived:]
+ -[AVExternalSyncDevice handleClockSetupFailedWithError:]
+ -[AVExternalSyncDevice handleFollowForDevice:withSessionRunning:]
+ -[AVExternalSyncDevice handleFollowTimeout]
+ -[AVExternalSyncDevice handleLockStateUpdateTriggerID:lockState:]
+ -[AVExternalSyncDevice handleSessionStateChange:]
+ -[AVExternalSyncDevice handleTSMSGOutOfBoundsTriggerID:error:]
+ -[AVExternalSyncDevice handleTSMSGSessionStoppedTriggerID:status:]
+ -[AVExternalSyncDevice handleTransitionToActiveSyncFromConfiguring]
+ -[AVExternalSyncDevice handleTransitionToActiveSync]
+ -[AVExternalSyncDevice handleTransitionToConfiguring]
+ -[AVExternalSyncDevice handleTransitionToIdle]
+ -[AVExternalSyncDevice handleTransitionToJamSync]
+ -[AVExternalSyncDevice handleTransitionToUnavailable]
+ -[AVExternalSyncDevice handleTriggerPresentTriggerID:isPresentState:]
+ -[AVExternalSyncDevice handleUnfollow]
+ -[AVExternalSyncDevice isLocked]
+ -[AVExternalSyncDevice isSessionRunning]
+ -[AVExternalSyncDevice isUsbConnected]
+ -[AVExternalSyncDevice notifyDelegateStatusChange]
+ -[AVExternalSyncDevice productID]
+ -[AVExternalSyncDevice queue]
+ -[AVExternalSyncDevice setConfigurationTimeoutBlock:]
+ -[AVExternalSyncDevice setLocked:]
+ -[AVExternalSyncDevice setSessionRunning:]
+ -[AVExternalSyncDevice setSignalCompensationDelay:]
+ -[AVExternalSyncDevice signalCompensationDelay]
+ -[AVExternalSyncDevice state]
+ -[AVExternalSyncDevice status]
+ -[AVExternalSyncDevice uniqueIdentifier]
+ -[AVExternalSyncDevice uuid]
+ -[AVExternalSyncDevice vendorID]
+ -[AVExternalSyncDeviceDiscoverySession _handleNotification:dict:]
+ -[AVExternalSyncDeviceDiscoverySession _updateDevicesEvent:]
+ -[AVExternalSyncDeviceDiscoverySession dealloc]
+ -[AVExternalSyncDeviceDiscoverySession devices]
+ -[AVExternalSyncDeviceDiscoverySession init]
+ -[AVExternalSyncDeviceDiscoverySession observeValueForKeyPath:ofObject:change:context:]
+ -[AVExternalSyncDeviceDiscoverySession setupNotifications]
+ -[AVExternalSyncDeviceDiscoverySession setupSource]
+ -[AVExternalSyncDeviceDiscoverySession teardownNotifications]
+ -[AVExternalSyncDeviceDiscoverySession teardownSource]
+ -[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:]
+ -[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:]
+ -[AVSpatialOverCaptureVideoPreviewLayer setPrimaryCaptureRectAspectRatio:centerPoint:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table124
+ GCC_except_table132
+ GCC_except_table147
+ GCC_except_table154
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table263
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table297
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table337
+ GCC_except_table358
+ GCC_except_table371
+ GCC_except_table373
+ GCC_except_table380
+ GCC_except_table394
+ GCC_except_table417
+ GCC_except_table427
+ GCC_except_table439
+ GCC_except_table454
+ GCC_except_table457
+ GCC_except_table484
+ GCC_except_table488
+ GCC_except_table499
+ GCC_except_table501
+ GCC_except_table520
+ GCC_except_table525
+ GCC_except_table532
+ GCC_except_table539
+ GCC_except_table549
+ GCC_except_table563
+ GCC_except_table586
+ GCC_except_table597
+ GCC_except_table607
+ GCC_except_table621
+ GCC_except_table637
+ GCC_except_table656
+ GCC_except_table677
+ GCC_except_table680
+ GCC_except_table708
+ GCC_except_table710
+ GCC_except_table712
+ GCC_except_table72
+ GCC_except_table736
+ GCC_except_table74
+ GCC_except_table748
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table758
+ GCC_except_table760
+ GCC_except_table78
+ GCC_except_table803
+ GCC_except_table807
+ GCC_except_table82
+ GCC_except_table862
+ GCC_except_table864
+ GCC_except_table866
+ GCC_except_table868
+ GCC_except_table914
+ GCC_except_table920
+ GCC_except_table928
+ GCC_except_table936
+ _AVAppleMakerNote_FrontAndBackCameraCompositionPictureInPictureRect
+ _AVCaptureAspectRatio16x9
+ _AVCaptureAspectRatio1x1
+ _AVCaptureAspectRatio3x4
+ _AVCaptureAspectRatio4x3
+ _AVCaptureAspectRatio9x16
+ _AVCaptureConvertDimensionsForAspectRatio
+ _AVCaptureCreateAVAssetWriterCompatibleMovieMetadata
+ _AVCaptureDeviceDynamicAspectRatioKey
+ _AVCaptureDeviceDynamicAspectRatioRequestIDKey
+ _AVCaptureDeviceInputActiveLockedVideoFrameDurationChangedContext
+ _AVCaptureDeviceInputactiveExternalSyncVideoFrameDurationChangedContext
+ _AVCaptureDeviceSmartFramingSuggestedFieldOfView
+ _AVCaptureDeviceSmartFramingSuggestedFieldOfViewChangedNotification
+ _AVCaptureDynamicAspectRatio16x9
+ _AVCaptureDynamicAspectRatio1x1
+ _AVCaptureDynamicAspectRatio3x4
+ _AVCaptureDynamicAspectRatio4x3
+ _AVCaptureDynamicAspectRatio9x16
+ _AVCaptureExternalPreviewLayerConfiguratorActiveColorSpaceChangedContext
+ _AVCaptureExternalPreviewLayerConfiguratorMinFrameDurationChangedContext
+ _AVCaptureFlippedDimensions
+ _AVCaptureIsSensorMountedInPortraitOrientation
+ _AVCaptureMultiCamClientCompositingMetadataCompositionPictureInPictureRectKey
+ _AVCaptureMultiCamClientCompositingMetadataCoreImageGainMapPropertiesKey
+ _AVCapturePhotoOutputDeviceDynamicAspectRatioChangedContext
+ _AVCaptureSessionInputActiveExternalSyncVideoFrameDurationChangedContext
+ _AVCaptureSessionInputActiveLockedVideoFrameDurationChangedContext
+ _AVCaptureSessionVideoInputDeviceDynamicAspectRatioChangedContext
+ _AVCaptureSmartFramingFieldOfViewLandscape
+ _AVCaptureSmartFramingFieldOfViewNone
+ _AVCaptureSmartFramingFieldOfViewPortrait
+ _AVCaptureSmartFramingFieldOfViewZoomedOutLandscape
+ _AVCaptureSmartFramingFieldOfViewZoomedOutPortrait
+ _AVCaptureSmartFramingMonitorActiveFormatChangedContext
+ _AVCaptureTimecodeAdvancedByFrames
+ _AVCaptureTimecodeAdvancedByFrames.cold.1
+ _AVCaptureTimecodeAdvancedByFrames.cold.10
+ _AVCaptureTimecodeAdvancedByFrames.cold.2
+ _AVCaptureTimecodeAdvancedByFrames.cold.3
+ _AVCaptureTimecodeAdvancedByFrames.cold.4
+ _AVCaptureTimecodeAdvancedByFrames.cold.5
+ _AVCaptureTimecodeAdvancedByFrames.cold.6
+ _AVCaptureTimecodeAdvancedByFrames.cold.7
+ _AVCaptureTimecodeAdvancedByFrames.cold.8
+ _AVCaptureTimecodeAdvancedByFrames.cold.9
+ _AVCaptureTimecodeCreateMetadataSampleBufferAssociatedWithPresentationTimeStamp
+ _AVCaptureTimecodeCreateMetadataSampleBufferForDuration
+ _AVCaptureTranslateAVCaptureAspectRatioToFig
+ _AVCaptureVideoCodecTypeIsProResRaw
+ _AVCaptureWhiteBalanceTemperatureAndTintValuesCloudy
+ _AVCaptureWhiteBalanceTemperatureAndTintValuesDaylight
+ _AVCaptureWhiteBalanceTemperatureAndTintValuesFluorescent
+ _AVCaptureWhiteBalanceTemperatureAndTintValuesShadow
+ _AVCaptureWhiteBalanceTemperatureAndTintValuesTungsten
+ _AVExternalSyncDeviceDiscoverySessionUsbConnectedChangedContext
+ _AVSmartStyleCastTypeBrightPop
+ _AVVideoCodecTypeAppleProResRAW
+ _AVVideoCodecTypeAppleProResRAWHQ
+ _CACurrentMediaTime
+ _CCCrypt
+ _CMBlockBufferReplaceDataBytes
+ _CMTimeCodeFormatDescriptionCreate
+ _CMVideoDimensionsAreEqual
+ _CMVideoFormatDescriptionCreate
+ _D23
+ _FigCaptureCreateCMClockFromTimeSyncMSGClock
+ _FigCaptureSessionRemoteSetClientCompositingSinkCallback
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource
+ _GestaltGetDeviceClass
+ _MIDIClientCreateWithBlock
+ _MIDIClientDispose
+ _MIDIEndpointGetEntity
+ _MIDIEntityGetDevice
+ _MIDIGetNumberOfSources
+ _MIDIGetSource
+ _MIDIInputPortCreateWithProtocol
+ _MIDIObjectGetIntegerProperty
+ _MIDIObjectGetStringProperty
+ _MIDIPortConnectSource
+ _MIDIPortDispose
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_AVCaptureDeviceDynamicAspectRatioRequest
+ _OBJC_CLASS_$_AVCaptureExternalDisplayConfiguration
+ _OBJC_CLASS_$_AVCaptureExternalDisplayConfigurator
+ _OBJC_CLASS_$_AVCaptureFraming
+ _OBJC_CLASS_$_AVCaptureMultiCamClientCompositingData
+ _OBJC_CLASS_$_AVCaptureSmartFraming
+ _OBJC_CLASS_$_AVCaptureSmartFramingMonitor
+ _OBJC_CLASS_$_AVCaptureTimecodeGenerator
+ _OBJC_CLASS_$_AVCaptureTimecodeSource
+ _OBJC_CLASS_$_AVExternalSyncDevice
+ _OBJC_CLASS_$_AVExternalSyncDeviceDiscoverySession
+ _OBJC_CLASS_$_FigStateMachine
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_IVAR_$_AVCaptureDevice._videoFrameDurationLocked
+ _OBJC_IVAR_$_AVCaptureDeviceDynamicAspectRatioRequest._dynamicAspectRatioCompletionBlock
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.dynamicAspectRatioSupported
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.mountedInPortraitOrientation
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.smartCropFeatureFlagEnabled
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.smartCropSupported
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.activeExternalSyncVideoFrameDuration
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.activeLockedVideoFrameDuration
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.activeVideoExternalSyncDevice
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.externalSyncSupported
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.lockedVideoFrameDurationSupported
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfiguration._bypassColorSpaceConversion
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfiguration._preferredResolution
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfiguration._shouldMatchFrameRate
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._active
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._activeExternalDisplayFrameRate
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._configuration
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._configurationBlock
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._configurationTimeoutBlock
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._configuratorWeakReference
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._deviceWeakReference
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._identifier
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._observationLayer
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._observingDeviceColorspace
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._observingDeviceFramerate
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._previewLayerWeakReference
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._queue
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._registered
+ _OBJC_IVAR_$_AVCaptureExternalDisplayConfigurator._retryConfiguration
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeExternalSyncDevice
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeExternalSyncVideoFrameDuration
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeExternalSyncVideoFrameDurationOwner
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeLockedVideoFrameDuration
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeLockedVideoFrameDurationOwner
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._dynamicAspectRatio
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._dynamicAspectRatioRequestID
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._dynamicAspectRatioRequestQueue
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._dynamicDimensions
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._smartFramingMonitor
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._smartFramingMonitoringSupported
+ _OBJC_IVAR_$_AVCaptureFraming._aspectRatio
+ _OBJC_IVAR_$_AVCaptureFraming._zoomFactor
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.multiCamClientCompositingPrimaryConnection
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._compositingMetadata
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._outputGainMapSampleBuffer
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._outputSampleBuffer
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._primaryGainMapImage
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._primaryGainMapSampleBuffer
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._primaryImage
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._primarySampleBuffer
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._secondaryGainMapImage
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._secondaryGainMapSampleBuffer
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._secondaryImage
+ _OBJC_IVAR_$_AVCaptureMultiCamClientCompositingData._secondarySampleBuffer
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.cameraSensorOrientationCompensationAutomaticallyEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.cameraSensorOrientationCompensationEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.cameraSensorOrientationCompensationSupported
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.multiCamClientCompositingPrimaryConnection
+ _OBJC_IVAR_$_AVCaptureSmartFraming._aspectRatio
+ _OBJC_IVAR_$_AVCaptureSmartFraming._zoomFactor
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._deviceWeakReference
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._enabledFramings
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._enabledSmartFramings
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._framingsLock
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._isMonitoring
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._isMonitoringLock
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._monitorWeakReference
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._photoModeFieldsOfView
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._photoModeFramings
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._photoModeSmartFramings
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._recommendedFraming
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._recommendedSmartFraming
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._supportedFramings
+ _OBJC_IVAR_$_AVCaptureSmartFramingMonitor._supportedSmartFramings
+ _OBJC_IVAR_$_AVCaptureStillImageOutputInternal.cameraSensorOrientationCompensationAutomaticallyEnabled
+ _OBJC_IVAR_$_AVCaptureStillImageOutputInternal.cameraSensorOrientationCompensationEnabled
+ _OBJC_IVAR_$_AVCaptureStillImageOutputInternal.cameraSensorOrientationCompensationSupported
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._currentSource
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._delegateCallbackQueue
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._delegateStorage
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._isTimecodeRingBufferFull
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._localGMTOffset
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._machTimebase
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._midiClient
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._midiInputPort
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._midiSourceDiscoveryClient
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._mutableSynchronizationSources
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._resourceLock
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._ringBufferStatusPollingQueue
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._statusNotificationSchedulingQueue
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._synchronizationStatus
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._synchronizationTimeout
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeAlignmentOffset
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeFrameDuration
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeRingBuffer
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeRingBufferCapacity
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeRingBufferHead
+ _OBJC_IVAR_$_AVCaptureTimecodeGenerator._timecodeRingBufferIngestTimeStamp
+ _OBJC_IVAR_$_AVCaptureTimecodeSource._displayName
+ _OBJC_IVAR_$_AVCaptureTimecodeSource._type
+ _OBJC_IVAR_$_AVCaptureTimecodeSource._uuid
+ _OBJC_IVAR_$_AVExternalSyncDevice._captureDeviceInput
+ _OBJC_IVAR_$_AVExternalSyncDevice._clock
+ _OBJC_IVAR_$_AVExternalSyncDevice._configurationTimeoutBlock
+ _OBJC_IVAR_$_AVExternalSyncDevice._delegate
+ _OBJC_IVAR_$_AVExternalSyncDevice._deviceWeakReference
+ _OBJC_IVAR_$_AVExternalSyncDevice._locked
+ _OBJC_IVAR_$_AVExternalSyncDevice._productID
+ _OBJC_IVAR_$_AVExternalSyncDevice._queue
+ _OBJC_IVAR_$_AVExternalSyncDevice._sessionRunning
+ _OBJC_IVAR_$_AVExternalSyncDevice._signalCompensationDelay
+ _OBJC_IVAR_$_AVExternalSyncDevice._stateMachine
+ _OBJC_IVAR_$_AVExternalSyncDevice._unfollowTimeoutBlock
+ _OBJC_IVAR_$_AVExternalSyncDevice._uniqueIdentifier
+ _OBJC_IVAR_$_AVExternalSyncDevice._usbConnected
+ _OBJC_IVAR_$_AVExternalSyncDevice._uuid
+ _OBJC_IVAR_$_AVExternalSyncDevice._vendorID
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._deviceLock
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._devices
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._fcs
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._serverDiedObserver
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._sourceLock
+ _OBJC_IVAR_$_AVExternalSyncDeviceDiscoverySession._weakReference
+ _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._primaryCaptureRectSmartFramingTransitionPercentComplete
+ _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._primaryCaptureRectSmartFramingTransitionTargetFieldOfView
+ _OBJC_METACLASS_$_AVCaptureDeviceDynamicAspectRatioRequest
+ _OBJC_METACLASS_$_AVCaptureExternalDisplayConfiguration
+ _OBJC_METACLASS_$_AVCaptureExternalDisplayConfigurator
+ _OBJC_METACLASS_$_AVCaptureFraming
+ _OBJC_METACLASS_$_AVCaptureMultiCamClientCompositingData
+ _OBJC_METACLASS_$_AVCaptureSmartFraming
+ _OBJC_METACLASS_$_AVCaptureSmartFramingMonitor
+ _OBJC_METACLASS_$_AVCaptureTimecodeGenerator
+ _OBJC_METACLASS_$_AVCaptureTimecodeSource
+ _OBJC_METACLASS_$_AVExternalSyncDevice
+ _OBJC_METACLASS_$_AVExternalSyncDeviceDiscoverySession
+ _SecRandomCopyBytes
+ _T2030
+ _V53_V54
+ _V57
+ __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal)
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_$_CLASS_METHODS_AVCaptureExternalDisplayConfigurator
+ __OBJC_$_CLASS_METHODS_AVCaptureFraming
+ __OBJC_$_CLASS_METHODS_AVCaptureSmartFraming
+ __OBJC_$_CLASS_METHODS_AVCaptureSmartFramingMonitor
+ __OBJC_$_CLASS_METHODS_AVCaptureTimecodeGenerator
+ __OBJC_$_CLASS_METHODS_AVExternalSyncDevice
+ __OBJC_$_CLASS_METHODS_AVExternalSyncDeviceDiscoverySession
+ __OBJC_$_CLASS_PROP_LIST_AVCaptureExternalDisplayConfigurator
+ __OBJC_$_CLASS_PROP_LIST_AVCaptureTimecodeGenerator
+ __OBJC_$_CLASS_PROP_LIST_AVExternalSyncDeviceDiscoverySession
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal)
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_$_INSTANCE_METHODS_AVCaptureExternalDisplayConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVCaptureExternalDisplayConfigurator
+ __OBJC_$_INSTANCE_METHODS_AVCaptureFraming
+ __OBJC_$_INSTANCE_METHODS_AVCaptureMultiCamClientCompositingData
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSmartFraming
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSmartFramingMonitor
+ __OBJC_$_INSTANCE_METHODS_AVCaptureTimecodeGenerator
+ __OBJC_$_INSTANCE_METHODS_AVCaptureTimecodeSource
+ __OBJC_$_INSTANCE_METHODS_AVExternalSyncDevice
+ __OBJC_$_INSTANCE_METHODS_AVExternalSyncDeviceDiscoverySession
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureExternalDisplayConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureExternalDisplayConfigurator
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureFraming
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureMultiCamClientCompositingData
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureSmartFraming
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureSmartFramingMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureTimecodeGenerator
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureTimecodeSource
+ __OBJC_$_INSTANCE_VARIABLES_AVExternalSyncDevice
+ __OBJC_$_INSTANCE_VARIABLES_AVExternalSyncDeviceDiscoverySession
+ __OBJC_$_PROP_LIST_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_$_PROP_LIST_AVCaptureExternalDisplayConfiguration
+ __OBJC_$_PROP_LIST_AVCaptureExternalDisplayConfigurator
+ __OBJC_$_PROP_LIST_AVCaptureFraming
+ __OBJC_$_PROP_LIST_AVCaptureMultiCamClientCompositingData
+ __OBJC_$_PROP_LIST_AVCaptureSmartFraming
+ __OBJC_$_PROP_LIST_AVCaptureSmartFramingMonitor
+ __OBJC_$_PROP_LIST_AVCaptureTimecodeGenerator
+ __OBJC_$_PROP_LIST_AVCaptureTimecodeSource
+ __OBJC_$_PROP_LIST_AVExternalSyncDevice
+ __OBJC_$_PROP_LIST_AVExternalSyncDeviceDiscoverySession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVExternalSyncDeviceDeviceNotificationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVExternalSyncDeviceDeviceNotificationDelegate
+ __OBJC_$_PROTOCOL_REFS_AVExternalSyncDeviceDeviceNotificationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureExternalDisplayConfigurator
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureTimecodeSource
+ __OBJC_CLASS_PROTOCOLS_$_AVExternalSyncDevice
+ __OBJC_CLASS_RO_$_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_CLASS_RO_$_AVCaptureExternalDisplayConfiguration
+ __OBJC_CLASS_RO_$_AVCaptureExternalDisplayConfigurator
+ __OBJC_CLASS_RO_$_AVCaptureFraming
+ __OBJC_CLASS_RO_$_AVCaptureMultiCamClientCompositingData
+ __OBJC_CLASS_RO_$_AVCaptureSmartFraming
+ __OBJC_CLASS_RO_$_AVCaptureSmartFramingMonitor
+ __OBJC_CLASS_RO_$_AVCaptureTimecodeGenerator
+ __OBJC_CLASS_RO_$_AVCaptureTimecodeSource
+ __OBJC_CLASS_RO_$_AVExternalSyncDevice
+ __OBJC_CLASS_RO_$_AVExternalSyncDeviceDiscoverySession
+ __OBJC_LABEL_PROTOCOL_$_AVExternalSyncDeviceDeviceNotificationDelegate
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceDynamicAspectRatioRequest
+ __OBJC_METACLASS_RO_$_AVCaptureExternalDisplayConfiguration
+ __OBJC_METACLASS_RO_$_AVCaptureExternalDisplayConfigurator
+ __OBJC_METACLASS_RO_$_AVCaptureFraming
+ __OBJC_METACLASS_RO_$_AVCaptureMultiCamClientCompositingData
+ __OBJC_METACLASS_RO_$_AVCaptureSmartFraming
+ __OBJC_METACLASS_RO_$_AVCaptureSmartFramingMonitor
+ __OBJC_METACLASS_RO_$_AVCaptureTimecodeGenerator
+ __OBJC_METACLASS_RO_$_AVCaptureTimecodeSource
+ __OBJC_METACLASS_RO_$_AVExternalSyncDevice
+ __OBJC_METACLASS_RO_$_AVExternalSyncDeviceDiscoverySession
+ __OBJC_PROTOCOL_$_AVExternalSyncDeviceDeviceNotificationDelegate
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_24
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_25
+ ___200-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:]_block_invoke
+ ___34-[AVCaptureTimecodeGenerator init]_block_invoke
+ ___38-[AVExternalSyncDevice handleUnfollow]_block_invoke
+ ___42-[AVExternalSyncDevice _setupStateMachine]_block_invoke
+ ___42-[AVExternalSyncDevice _setupStateMachine]_block_invoke_2
+ ___42-[AVExternalSyncDevice _setupStateMachine]_block_invoke_3
+ ___42-[AVExternalSyncDevice _setupStateMachine]_block_invoke_4
+ ___42-[AVExternalSyncDevice _setupStateMachine]_block_invoke_5
+ ___43-[AVExternalSyncDevice handleFollowTimeout]_block_invoke
+ ___44-[AVCaptureExternalDisplayConfigurator stop]_block_invoke
+ ___44-[AVCaptureFigVideoDevice dynamicDimensions]_block_invoke
+ ___44-[AVExternalSyncDevice handleClockReceived:]_block_invoke
+ ___45-[AVCaptureFigVideoDevice dynamicAspectRatio]_block_invoke
+ ___46-[AVCaptureExternalDisplayConfigurator _setup]_block_invoke
+ ___46-[AVExternalSyncDevice _handleSourceDiedEvent]_block_invoke
+ ___47-[AVCaptureFigVideoDevice setActiveSyncDevice:]_block_invoke
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.504
+ ___49-[AVCaptureFigVideoDevice isDockedTrackingActive]_block_invoke
+ ___49-[AVExternalSyncDevice handleSessionStateChange:]_block_invoke
+ ___51+[AVExternalSyncDeviceDiscoverySession isSupported]_block_invoke
+ ___53+[AVExternalSyncDeviceDiscoverySession sharedSession]_block_invoke
+ ___53-[AVExternalSyncDevice handleTransitionToConfiguring]_block_invoke
+ ___54-[AVCaptureFigVideoDevice dynamicAspectRatioRequestID]_block_invoke
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.745
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_44
+ ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.650
+ ___56-[AVExternalSyncDevice _handleUSBConnectionStateChange:]_block_invoke
+ ___56-[AVExternalSyncDevice handleClockSetupFailedWithError:]_block_invoke
+ ___57-[AVCaptureFigVideoDevice activeLockedVideoFrameDuration]_block_invoke
+ ___57-[AVCaptureTimecodeGenerator startExternalSourceObserver]_block_invoke
+ ___58-[AVExternalSyncDeviceDiscoverySession setupNotifications]_block_invoke
+ ___60-[AVCaptureSession _updateMultiCamClientCompositingCallback]_block_invoke
+ ___61-[AVCaptureExternalDisplayConfigurator dispatchConfiguration]_block_invoke
+ ___62-[AVCaptureExternalDisplayConfigurator _dispatchConfiguration]_block_invoke
+ ___62-[AVCaptureTimecodeGenerator _notifyDelegateOfTimecodeUpdate:]_block_invoke
+ ___62-[AVCaptureTimecodeGenerator _notifyDelegateOfTimecodeUpdate:]_block_invoke_2
+ ___62-[AVExternalSyncDevice handleTSMSGOutOfBoundsTriggerID:error:]_block_invoke
+ ___63-[AVCaptureExternalDisplayConfigurator registerSelfForDisplay:]_block_invoke
+ ___63-[AVCaptureFigVideoDevice activeExternalSyncVideoFrameDuration]_block_invoke
+ ___64-[AVCaptureTimecodeGenerator _notifyDelegateOfSourceListUpdate:]_block_invoke
+ ___64-[AVCaptureTimecodeGenerator _notifyDelegateOfSourceListUpdate:]_block_invoke_2
+ ___64-[AVCaptureTimecodeGenerator _scheduleTimecodeRingBufferPolling]_block_invoke
+ ___65-[AVCaptureExternalDisplayConfigurator _configureExternalDisplay]_block_invoke
+ ___65-[AVExternalSyncDevice handleFollowForDevice:withSessionRunning:]_block_invoke
+ ___65-[AVExternalSyncDevice handleLockStateUpdateTriggerID:lockState:]_block_invoke
+ ___66-[AVExternalSyncDevice handleTSMSGSessionStoppedTriggerID:status:]_block_invoke
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.342
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke_2
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke_3
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke_4
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke_5
+ ___68-[AVCaptureFigVideoDevice drainDynamicAspectRatioCompletionHandlers]_block_invoke
+ ___69-[AVExternalSyncDevice handleTriggerPresentTriggerID:isPresentState:]_block_invoke
+ ___70-[AVCaptureFigVideoDevice setActiveLockedVideoFrameDuration:forOwner:]_block_invoke
+ ___70-[AVCaptureFigVideoDevice setActiveLockedVideoFrameDuration:forOwner:]_block_invoke_2
+ ___70-[AVCaptureFigVideoDevice setActiveLockedVideoFrameDuration:forOwner:]_block_invoke_3
+ ___71-[AVCaptureFigVideoDevice resetActiveLockedVideoFrameDurationForOwner:]_block_invoke
+ ___72-[AVCaptureExternalDisplayConfigurator _getConfigurationWithCompletion:]_block_invoke
+ ___72-[AVCaptureExternalDisplayConfigurator _getConfigurationWithCompletion:]_block_invoke.cold.1
+ ___74-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayFrameRate]_block_invoke
+ ___74-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayFrameRate]_block_invoke.cold.1
+ ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.703
+ ___74-[AVCaptureTimecodeGenerator _openMidiTimecodeDataStreamWithUUID:success:]_block_invoke
+ ___74-[AVCaptureTimecodeGenerator _openMidiTimecodeDataStreamWithUUID:success:]_block_invoke_2
+ ___75-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayColorspace]_block_invoke
+ ___75-[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]_block_invoke
+ ___75-[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]_block_invoke_2
+ ___75-[AVCaptureFigVideoDevice dynamicAspectRatioAndDynamicAspectRatioRequestID]_block_invoke
+ ___79-[AVCaptureSmartFramingMonitor observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___82-[AVCaptureExternalDisplayConfigurator initWithDevice:previewLayer:configuration:]_block_invoke
+ ___83+[AVCaptureExternalDisplayConfigurator registerConfigurator:withDisplayIdentifier:]_block_invoke
+ ___86-[AVCaptureExternalDisplayConfigurator externalDisplayLayerObserver:visibiltyChanged:]_block_invoke
+ ___86-[AVCapturePhotoOutput _invokeClientCompositingCallbackForSettingsID:compositingData:]_block_invoke
+ ___87-[AVCaptureExternalDisplayConfigurator observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___88-[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:]_block_invoke
+ ___88-[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:]_block_invoke.75
+ ___90-[AVCaptureMovieFileOutput _invokeClientCompositingCallbackForSettingsID:compositingData:]_block_invoke
+ ___92-[AVCaptureTimecodeGenerator _notifyDelegateOfSynchronizationStatusChange:filterRedundancy:]_block_invoke
+ ___92-[AVCaptureTimecodeGenerator _notifyDelegateOfSynchronizationStatusChange:filterRedundancy:]_block_invoke_2
+ ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke.356
+ ___96-[AVCaptureVideoDataOutput recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:]_block_invoke
+ ___99-[AVCaptureFigVideoDevice setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:]_block_invoke
+ ___99-[AVCaptureFigVideoDevice setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:]_block_invoke_2
+ ___99-[AVCaptureFigVideoDevice setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:]_block_invoke_3
+ ___AVControlCenterModulesPrewarm_block_invoke.441
+ ____registerVideoDevicesOnce_block_invoke.1512
+ ___block_descriptor_104_e8_32o40o48o_e34_v16?0^{OpaqueFigCaptureSession=}8ls32l8s40l8s48l8
+ ___block_descriptor_112_e8_32o40o48o56o64o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e30_v16?0r^{MIDINotification=iI}8l
+ ___block_descriptor_32_e39_v28?0"AVExternalSyncDevice"8I16I20i24l
+ ___block_descriptor_40_e8_32o_e201_i80?0^{__CFString=}8q16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^{opaqueCMSampleBuffer=}64r^^{__CFDictionary}72ls32l8
+ ___block_descriptor_40_e8_32o_e30_v16?0r^{MIDINotification=iI}8ls32l8
+ ___block_descriptor_40_e8_32o_e33_v16?0"FBSDisplayConfiguration"8ls32l8
+ ___block_descriptor_40_e8_32o_e59_v24?0r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}8^v16ls32l8
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_481_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r448r456r464r472r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8r448l8r456l8r464l8r472l8
+ ___block_descriptor_48_e8_32o40o_e24_v16?0"NSNotification"8ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e34_v16?0^{OpaqueFigCaptureSession=}8ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32o40o48r56r64r_e5_v8?0lr48l8s32l8r56l8s40l8r64l8
+ ___block_descriptor_72_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32o40o48o56o64o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.149
+ ___block_literal_global.1504
+ ___block_literal_global.1511
+ ___block_literal_global.1514
+ ___block_literal_global.1661
+ ___block_literal_global.188
+ ___block_literal_global.215
+ ___block_literal_global.217
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.31
+ ___block_literal_global.324
+ ___block_literal_global.33
+ ___block_literal_global.37
+ ___block_literal_global.434
+ ___block_literal_global.444
+ ___block_literal_global.468
+ ___block_literal_global.526
+ ___block_literal_global.569
+ ___block_literal_global.626
+ ___block_literal_global.631
+ ___block_literal_global.634
+ ___block_literal_global.920
+ ___block_literal_global.923
+ ___block_literal_global.928
+ ___figCaptureSourceNotificationHandler_block_invoke
+ ___getFBSMutableDisplayConfigurationRequestClass_block_invoke
+ ___getFBSMutableDisplayConfigurationRequestClass_block_invoke.cold.1
+ ___getUISDisplayConfigurationChangedNotificationSymbolLoc_block_invoke
+ ___getUISDisplayConfigurationForContextIDSymbolLoc_block_invoke
+ ___getUISRequestDisplayConfigurationForContextIDSymbolLoc_block_invoke
+ ___getUISSDisplayConfigurationAffectedContextIDsKeySymbolLoc_block_invoke
+ __block_invoke.timecode
+ __block_invoke.userBits
+ _avcc_defaultVideoRetainedBufferCount
+ _avcs_updateAVCaptureConnectionForAspectRatio
+ _bzero
+ _dispatch_after
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _figCaptureSourceNotificationHandler
+ _fmod
+ _gAVCaptureExternalDisplayConfiguratorTrace
+ _gAVCaptureFramingTrace
+ _gAVCaptureSmartFramingMonitorTrace
+ _gAVExternalSyncDeviceTrace
+ _getFBSMutableDisplayConfigurationRequestClass.softClass
+ _getUISDisplayConfigurationChangedNotification
+ _getUISDisplayConfigurationChangedNotification.cold.1
+ _getUISDisplayConfigurationChangedNotificationSymbolLoc.ptr
+ _getUISDisplayConfigurationForContextIDSymbolLoc.ptr
+ _getUISRequestDisplayConfigurationForContextIDSymbolLoc.ptr
+ _getUISSDisplayConfigurationAffectedContextIDsKeySymbolLoc.ptr
+ _kCIImageCacheHint
+ _kCIImageColorSpace
+ _kCIImageProperties
+ _kCMVideoDimensionsZero
+ _kEncryptionIV
+ _kEncryptionKey
+ _kFigCaptureSampleBufferMetadata_FlexRangeImageProperties
+ _kFigCaptureSampleBufferMetadata_GainMapHeadroom
+ _kFigCaptureSampleBufferMetadata_MeteorPlusGainMapAverage
+ _kFigCaptureSessionPreviewSinkPrimaryCaptureRectKey_SmartFramingTransitionPercentComplete
+ _kFigCaptureSessionPreviewSinkPrimaryCaptureRectKey_SmartFramingTransitionTargetFieldOfView
+ _kFigCaptureSessionVideoDataSinkProperty_MovieLevelMetadata
+ _kFigCaptureSourceAttributeKey_CameraSensorOrientationCompensation
+ _kFigCaptureSourceAttributeKey_ExternalSyncMaxFrameRate
+ _kFigCaptureSourceAttributeKey_LockedFrameDurationMaxFrameRate
+ _kFigCaptureSourceAttributeKey_SmartFramingZoomFactorsByFieldOfView
+ _kFigCaptureSourceFrameDurationBoundsKey_FrameDurationMax
+ _kFigCaptureSourceFrameDurationBoundsKey_FrameDurationMin
+ _kFigCaptureSourceNotificationExternalSyncDeviceDiscoverySessionDevicesChangedPayloadKey_PID
+ _kFigCaptureSourceNotificationExternalSyncDeviceDiscoverySessionDevicesChangedPayloadKey_VID
+ _kFigCaptureSourceNotificationKey_DynamicAspectRatioRequestID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_ClockID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_Error
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_LockState
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_OutOfBounds
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_SessionStopped
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_State
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_Status
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_TriggerID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_TriggerPreset
+ _kFigCaptureSourceNotification_ExternalSyncDeviceDiscoverySessionDevicesChanged
+ _kFigCaptureSourceNotification_LiveReconfigurationForDynamicAspectRatioComplete
+ _kFigCaptureSourceNotification_PulseGeneratorStatusChanged
+ _kFigCaptureSourceNotification_SmartFramingSuggestedFieldOfViewChanged
+ _kFigCaptureSourceProperty_EnabledSmartFramingFieldsOfView
+ _kFigCaptureSourceProperty_FrameDurationBounds
+ _kFigCaptureSourceProperty_SmartFramingMonitorRunning
+ _kFigMetadataDataTypeNamespace_QuickTimeMetadata
+ _kFigMetadataItemProperty_DataType
+ _kFigMetadataItemProperty_Key
+ _kFigMetadataItemProperty_Keyspace
+ _kFigMetadataItemProperty_Value
+ _kMIDIPropertyName
+ _kMIDIPropertyUniqueID
+ _kSecRandomDefault
+ _mach_timebase_info
+ _modf
+ _objc_msgSend$_addTimecodeToRingBuffer:timestamp:
+ _objc_msgSend$_applyActiveLockedVideoFrameDuration
+ _objc_msgSend$_configureExternalDisplay
+ _objc_msgSend$_configureExternalDisplayColorspace
+ _objc_msgSend$_configureExternalDisplayFrameRate
+ _objc_msgSend$_deviceColorspaceChangeMonitorConfigure
+ _objc_msgSend$_deviceColorspaceChangeMonitorTeardown
+ _objc_msgSend$_deviceFramerateChangedMonitorConfigure
+ _objc_msgSend$_deviceFramerateChangedMonitorTeardown
+ _objc_msgSend$_dispatchConfiguration
+ _objc_msgSend$_displayConfigurationChangedMonitorConfigure
+ _objc_msgSend$_displayConfigurationChangedMonitorTeardown
+ _objc_msgSend$_drainDynamicAspectRatioRequestQueue
+ _objc_msgSend$_externalDisplayConfigurationChangedHandler
+ _objc_msgSend$_getConfigurationWithCompletion:
+ _objc_msgSend$_handleChangedActiveFormat:
+ _objc_msgSend$_handleLiveReconfigurationCompletionWithPayload:
+ _objc_msgSend$_handleNotification:dict:
+ _objc_msgSend$_handleSourceDiedEvent
+ _objc_msgSend$_handleUSBConnectionStateChange:
+ _objc_msgSend$_handleUnfollow
+ _objc_msgSend$_imageForGainMapSampleBuffer:
+ _objc_msgSend$_imageForSampleBuffer:gainMapMetadata:
+ _objc_msgSend$_initWithAspectRatio:zoomFactor:
+ _objc_msgSend$_initWithCompletionBlock:requestID:
+ _objc_msgSend$_initWithIdentifier:pid:vid:
+ _objc_msgSend$_initWithPrimarySampleBuffer:primaryGainMapSampleBuffer:secondarySampleBuffer:secondaryGainMapSampleBuffer:outputSampleBuffer:outputGainMapSampleBuffer:
+ _objc_msgSend$_invokeClientCompositingCallbackForSettingsID:compositingData:
+ _objc_msgSend$_invokeClientCompositingCallbackForSinkID:settingsID:compositingData:
+ _objc_msgSend$_isProResRawRecordingAndAWBIsNotLockedForWrapper:
+ _objc_msgSend$_isSpatialVideoCaptureEnabledOnMFO:
+ _objc_msgSend$_isTimecodeRingBufferEmpty
+ _objc_msgSend$_isTimecodeRingBufferStale
+ _objc_msgSend$_makeInActive
+ _objc_msgSend$_newestTimecodeRingBufferEntry
+ _objc_msgSend$_notifyDelegateOfError:
+ _objc_msgSend$_notifyDelegateOfSourceListUpdate:
+ _objc_msgSend$_notifyDelegateOfSynchronizationStatusChange:filterRedundancy:
+ _objc_msgSend$_notifyDelegateOfTimecodeUpdate:
+ _objc_msgSend$_openMidiTimecodeDataStreamWithUUID:success:
+ _objc_msgSend$_pollRingBufferStatus
+ _objc_msgSend$_populatePhotoModeSmartFramingsAndFieldsOfViewFromZoomFactorsByFieldOfView:
+ _objc_msgSend$_registerMidiEndpointAsSynchronizationSource:
+ _objc_msgSend$_registerSynchronizationSource:
+ _objc_msgSend$_removeMidiEndpointAsSynchronizationSource:
+ _objc_msgSend$_removeSynchronizationSource:
+ _objc_msgSend$_resetActiveLockedVideoFrameDurationWithFormatChanged:
+ _objc_msgSend$_resetTimecodeRingBuffer
+ _objc_msgSend$_scheduleTimecodeRingBufferPolling
+ _objc_msgSend$_setDelegate:
+ _objc_msgSend$_setEnabledSmartFramingFieldsOfView:
+ _objc_msgSend$_setGenlockSignalCompensationDelay:
+ _objc_msgSend$_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:
+ _objc_msgSend$_setSmartFramingMonitorRunning:
+ _objc_msgSend$_setup
+ _objc_msgSend$_setupStateMachine
+ _objc_msgSend$_timeOfDay
+ _objc_msgSend$_timecodeIsCoherent:
+ _objc_msgSend$_updateCameraSensorOrientationCompensationSupportedForDevice:
+ _objc_msgSend$_updateDevicesEvent:
+ _objc_msgSend$_updateExternalSyncSupported
+ _objc_msgSend$_updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForFramings:
+ _objc_msgSend$_updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForSmartFramings:
+ _objc_msgSend$_updateLockedVideoFrameDurationSupported
+ _objc_msgSend$_updateMultiCamClientCompositingCallback
+ _objc_msgSend$_updateRectOfInterestSizeForSensorOrientationAndDynamicAspectRatio:
+ _objc_msgSend$activeExternalDisplayFrameRate
+ _objc_msgSend$activeExternalSyncVideoFrameDuration
+ _objc_msgSend$activeLockedVideoFrameDuration
+ _objc_msgSend$addOperationWithBlock:
+ _objc_msgSend$applyActiveExternalSyncVideoFrameDuration
+ _objc_msgSend$aspectRatio
+ _objc_msgSend$availableSources
+ _objc_msgSend$bypassColorSpaceConversion
+ _objc_msgSend$cancelAllOperations
+ _objc_msgSend$captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:
+ _objc_msgSend$captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:
+ _objc_msgSend$captureOutput:readyForClientCompositingForOutputFileAtURL:primaryPixelBuffer:primaryPTS:secondaryPixelBuffer:secondaryPTS:outputPixelBuffer:compositeMetadata:
+ _objc_msgSend$captureOutput:readyForClientCompositingForResolvedSettings:compositingData:
+ _objc_msgSend$captureOutput:readyForClientCompositingForResolvedSettings:primaryPixelBuffer:primaryPTS:secondaryPixelBuffer:secondaryPTS:outputPixelBuffer:compositeMetadata:
+ _objc_msgSend$compositingMetadata
+ _objc_msgSend$connectionID
+ _objc_msgSend$dispatchConfiguration
+ _objc_msgSend$displayName
+ _objc_msgSend$drainDynamicAspectRatioCompletionHandlers
+ _objc_msgSend$dynamicAspectRatio
+ _objc_msgSend$dynamicAspectRatioAndDynamicAspectRatioRequestID
+ _objc_msgSend$dynamicAspectRatioCompletionBlock
+ _objc_msgSend$dynamicAspectRatioRequestWithCompletionBlock:requestID:
+ _objc_msgSend$dynamicDimensions
+ _objc_msgSend$enabledFramings
+ _objc_msgSend$enabledSmartFramings
+ _objc_msgSend$externalDisplayAndCaptureDeviceSynchronized
+ _objc_msgSend$externalSyncDevice:failedWithError:
+ _objc_msgSend$externalSyncDeviceStatusDidChange:
+ _objc_msgSend$figCaptureSourceAttributes
+ _objc_msgSend$frameCountSource
+ _objc_msgSend$framingWithAspectRatio:zoomFactor:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$handleChangedDynamicAspectRatio:forFormat:
+ _objc_msgSend$handleChangedMSGPulseDurationForDevice:
+ _objc_msgSend$handleClockReceived:
+ _objc_msgSend$handleClockSetupFailedWithError:
+ _objc_msgSend$handleFollowForDevice:withSessionRunning:
+ _objc_msgSend$handleFollowTimeout
+ _objc_msgSend$handleLockStateUpdateTriggerID:lockState:
+ _objc_msgSend$handleSessionStateChange:
+ _objc_msgSend$handleTSMSGOutOfBoundsTriggerID:error:
+ _objc_msgSend$handleTSMSGSessionStoppedTriggerID:status:
+ _objc_msgSend$handleTransitionToActiveSync
+ _objc_msgSend$handleTransitionToActiveSyncFromConfiguring
+ _objc_msgSend$handleTransitionToConfiguring
+ _objc_msgSend$handleTransitionToIdle
+ _objc_msgSend$handleTransitionToJamSync
+ _objc_msgSend$handleTransitionToUnavailable
+ _objc_msgSend$handleTriggerPresentTriggerID:isPresentState:
+ _objc_msgSend$handleUnfollow
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$hash
+ _objc_msgSend$horizontalFieldOfViewForAspectRatio:
+ _objc_msgSend$horizontalGeometricDistortionCorrectedFieldOfViewForAspectRatio:
+ _objc_msgSend$imageWithCVPixelBuffer:options:
+ _objc_msgSend$initWithDevice:smartFramingZoomFactorsByFieldOfView:
+ _objc_msgSend$initWithDisplayName:sourceType:uuid:
+ _objc_msgSend$initWithLabel:stateCount:initialState:owner:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$isBypassingColorSpaceConversionSupported
+ _objc_msgSend$isCameraSensorOrientationCompensationEnabled
+ _objc_msgSend$isCinematicFramingActive
+ _objc_msgSend$isDockedTrackingActive
+ _objc_msgSend$isDynamicAspectRatioSupported
+ _objc_msgSend$isExternalSyncSupported
+ _objc_msgSend$isFollowingExternalSyncDevice
+ _objc_msgSend$isLocked
+ _objc_msgSend$isLockedVideoFrameDurationSupported
+ _objc_msgSend$isMatchingFrameRateSupported
+ _objc_msgSend$isMonitoring
+ _objc_msgSend$isMountedInPortraitOrientation
+ _objc_msgSend$isMultiCamClientCompositingEnabled
+ _objc_msgSend$isMultiCamClientCompositingSupported
+ _objc_msgSend$isPreferredResolutionSupported
+ _objc_msgSend$isSessionRunning
+ _objc_msgSend$isSmartCropSupported
+ _objc_msgSend$isSmartFramingMonitoringSupported
+ _objc_msgSend$isSmartFramingSupported
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$isUsbConnected
+ _objc_msgSend$isVideoFrameDurationLocked
+ _objc_msgSend$maxUpscalingDimensions
+ _objc_msgSend$minSupportedExternalSyncFrameDuration
+ _objc_msgSend$minSupportedLockedVideoFrameDuration
+ _objc_msgSend$multiCamClientCompositingEnabled
+ _objc_msgSend$multiCamClientCompositingPrimaryConnection
+ _objc_msgSend$notifyDelegateStatusChange
+ _objc_msgSend$observingDeviceColorspace
+ _objc_msgSend$observingDeviceFramerate
+ _objc_msgSend$outputSampleBuffer
+ _objc_msgSend$preferredResolution
+ _objc_msgSend$primarySampleBuffer
+ _objc_msgSend$realTimeClockSource
+ _objc_msgSend$recommendedFraming
+ _objc_msgSend$recommendedSmartFraming
+ _objc_msgSend$refreshRate
+ _objc_msgSend$registerConfigurator:withDisplayIdentifier:
+ _objc_msgSend$registerSelfForDisplay:
+ _objc_msgSend$registered
+ _objc_msgSend$resetActiveLockedVideoFrameDurationForOwner:
+ _objc_msgSend$resetDeviceClockAndInputPortsToHostClock
+ _objc_msgSend$retryConfiguration
+ _objc_msgSend$secondarySampleBuffer
+ _objc_msgSend$secondsFromGMTForDate:
+ _objc_msgSend$sensorOrientation
+ _objc_msgSend$setActive:
+ _objc_msgSend$setActiveExternalDisplayFrameRate:
+ _objc_msgSend$setActiveExternalSyncSignalCompensationDelay:withExternalSyncDevice:
+ _objc_msgSend$setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:
+ _objc_msgSend$setActiveLockedVideoFrameDuration:forOwner:
+ _objc_msgSend$setActiveSyncDevice:
+ _objc_msgSend$setAllowsColorMatching:
+ _objc_msgSend$setCameraSensorOrientationCompensationEnabled:
+ _objc_msgSend$setCompositingMetadata:
+ _objc_msgSend$setDisableFrameDoubling:
+ _objc_msgSend$setDynamicAspectRatio:completionHandler:
+ _objc_msgSend$setExternalSyncFrameRate:
+ _objc_msgSend$setFocusMode:
+ _objc_msgSend$setLabel:forState:
+ _objc_msgSend$setLockedFrameRate:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setMultiCamClientCompositingEnabled:
+ _objc_msgSend$setMultiCamClientCompositingPrimaryConnectionID:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNativePixelSize:
+ _objc_msgSend$setObservingDeviceColorspace:
+ _objc_msgSend$setObservingDeviceFramerate:
+ _objc_msgSend$setOutputAspectRatio:
+ _objc_msgSend$setOutputAspectRatioRequestID:
+ _objc_msgSend$setOutputSettings:forConnection:
+ _objc_msgSend$setOverscanCompensation:
+ _objc_msgSend$setPerformsAtomicStateTransitions:
+ _objc_msgSend$setRefreshRate:
+ _objc_msgSend$setRegistered:
+ _objc_msgSend$setRetryConfiguration:
+ _objc_msgSend$setSessionRunning:
+ _objc_msgSend$setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:
+ _objc_msgSend$setupNotifications
+ _objc_msgSend$setupSource
+ _objc_msgSend$shouldMatchFrameRate
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$smartCropFormat
+ _objc_msgSend$smartFramingMonitor
+ _objc_msgSend$smartFramingWithAspectRatio:zoomFactor:
+ _objc_msgSend$startExternalSourceObserver
+ _objc_msgSend$state
+ _objc_msgSend$supportedDynamicAspectRatios
+ _objc_msgSend$supportedFramings
+ _objc_msgSend$supportedProResRawCodecTypes
+ _objc_msgSend$supportedSmartFramings
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$teardownNotifications
+ _objc_msgSend$teardownSource
+ _objc_msgSend$timecodeGenerator:didReceiveUpdate:fromSource:
+ _objc_msgSend$timecodeGenerator:didUpdateAvailableSources:
+ _objc_msgSend$timecodeGenerator:transitionedToSynchronizationStatus:forSource:
+ _objc_msgSend$transitionToState:
+ _objc_msgSend$transitionToState:fromState:
+ _objc_msgSend$unfollowExternalSyncDevice
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$updateClientVideoSettingsForAspectRatio:
+ _objc_msgSend$updateMetadataTransformForSourceFormat:aspectRatio:
+ _objc_msgSend$updateRecommendedSmartFramingWithFieldOfView:
+ _objc_msgSend$updateSupportedProperties
+ _objc_msgSend$utilizesRingBufferSyncDiscipline
+ _objc_msgSend$uuid
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$verticalFieldOfViewForAspectRatio:
+ _objc_msgSend$verticalGeometricDistortionCorrectedFieldOfViewForAspectRatio:
+ _objc_msgSend$videoFieldOfViewForAspectRatio:geometricDistortionCorrected:
+ _objc_msgSend$waitUntilAllOperationsAreFinished
+ _objc_msgSend$whenTransitioningToState:callHandler:
+ _objc_msgSend$whiteBalanceMode
+ _objc_msgSend$zoomFactor
+ _objc_opt_new
+ _os_unfair_lock_assert_owner
+ _registerConfigurator:withDisplayIdentifier:.configuratorRegistry
+ _registerConfigurator:withDisplayIdentifier:.onceToken
+ _sharedSession.sAVExternalSyncDeviceDiscoverySession
+ _tg_UUIDFromSInt32
+ _tg_UUIDFromSInt32.cold.1
+ _tg_calculateDropFramesPerEvent
+ _tg_calculateDropFramesPerEvent.cold.1
+ _tg_calculateDropFramesPerEvent.cold.2
+ _tg_packageTimecodeAsMetadataBuffer
+ _tg_packageTimecodeAsMetadataBuffer.cold.1
+ _tg_packageTimecodeAsMetadataBuffer.cold.2
+ _tg_packageTimecodeAsMetadataBuffer.cold.3
+ _tg_totalFramesFromTimecode
+ _tg_totalFramesFromTimecode.cold.1
+ _tg_totalFramesFromTimecode.cold.2
+ _tg_totalFramesFromTimecode.cold.3
+ _tg_totalFramesFromTimecode.cold.4
+ _tg_totalFramesFromTimecode.cold.5
+ _tg_totalFramesFromTimecode.cold.6
+ _uuidEncryptionParametersInitialized
- -[AVCaptureConnection figCaptureConnectionConfigurationForSessionPreset:allConnections:].cold.3
- -[AVCaptureOutput updateMetadataTransformForSourceFormat:]
- -[AVCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:]
- -[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]
- -[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:]
- GCC_except_table120
- GCC_except_table128
- GCC_except_table138
- GCC_except_table142
- GCC_except_table151
- GCC_except_table152
- GCC_except_table161
- GCC_except_table163
- GCC_except_table167
- GCC_except_table169
- GCC_except_table173
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table187
- GCC_except_table189
- GCC_except_table192
- GCC_except_table203
- GCC_except_table204
- GCC_except_table205
- GCC_except_table209
- GCC_except_table215
- GCC_except_table230
- GCC_except_table233
- GCC_except_table251
- GCC_except_table268
- GCC_except_table273
- GCC_except_table279
- GCC_except_table282
- GCC_except_table287
- GCC_except_table295
- GCC_except_table298
- GCC_except_table304
- GCC_except_table307
- GCC_except_table313
- GCC_except_table334
- GCC_except_table345
- GCC_except_table347
- GCC_except_table349
- GCC_except_table355
- GCC_except_table392
- GCC_except_table402
- GCC_except_table414
- GCC_except_table429
- GCC_except_table432
- GCC_except_table459
- GCC_except_table463
- GCC_except_table474
- GCC_except_table482
- GCC_except_table489
- GCC_except_table493
- GCC_except_table495
- GCC_except_table500
- GCC_except_table524
- GCC_except_table538
- GCC_except_table561
- GCC_except_table572
- GCC_except_table582
- GCC_except_table596
- GCC_except_table612
- GCC_except_table631
- GCC_except_table652
- GCC_except_table655
- GCC_except_table683
- GCC_except_table685
- GCC_except_table687
- GCC_except_table69
- GCC_except_table70
- GCC_except_table711
- GCC_except_table723
- GCC_except_table725
- GCC_except_table727
- GCC_except_table733
- GCC_except_table735
- GCC_except_table75
- GCC_except_table778
- GCC_except_table782
- GCC_except_table79
- GCC_except_table835
- GCC_except_table837
- GCC_except_table839
- GCC_except_table841
- GCC_except_table85
- GCC_except_table885
- GCC_except_table887
- GCC_except_table93
- GCC_except_table96
- __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|CameraLensSmudgeDetection)
- __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|CameraLensSmudgeDetection)
- ___122-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]_block_invoke
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.435
- ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.625
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.335
- ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.678
- ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke.346
- ___AVControlCenterModulesPrewarm_block_invoke.439
- ____registerVideoDevicesOnce_block_invoke.1393
- ___block_descriptor_457_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r448r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8r448l8
- ___block_descriptor_88_e8_32o40o_e34_v16?0^{OpaqueFigCaptureSession=}8ls32l8s40l8
- ___block_literal_global.103
- ___block_literal_global.1385
- ___block_literal_global.1392
- ___block_literal_global.1395
- ___block_literal_global.142
- ___block_literal_global.1583
- ___block_literal_global.181
- ___block_literal_global.186
- ___block_literal_global.220
- ___block_literal_global.257
- ___block_literal_global.432
- ___block_literal_global.442
- ___block_literal_global.457
- ___block_literal_global.466
- ___block_literal_global.500
- ___block_literal_global.557
- ___block_literal_global.562
- ___block_literal_global.565
- ___block_literal_global.902
- ___block_literal_global.905
- ___block_literal_global.910
- _objc_msgSend$_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:
- _objc_msgSend$captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:
- _objc_msgSend$updateMetadataTransformForSourceFormat:
CStrings:
+ "%@, %.2f"
+ "( timecode->frameDuration.value > 0 ) && ( timecode->frameDuration.timescale > 0 )"
+ "+[AVCaptureExternalDisplayConfigurator registerConfigurator:withDisplayIdentifier:]"
+ ", lowlatency"
+ ", supports Dynamic Aspect Ratio"
+ ", supports Smart Crop"
+ "-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayColorspace]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator _configureExternalDisplayFrameRate]"
+ "-[AVCaptureExternalDisplayConfigurator _configureExternalDisplay]"
+ "-[AVCaptureExternalDisplayConfigurator _configureExternalDisplay]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorConfigure]"
+ "-[AVCaptureExternalDisplayConfigurator _deviceColorspaceChangeMonitorTeardown]"
+ "-[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorConfigure]"
+ "-[AVCaptureExternalDisplayConfigurator _deviceFramerateChangedMonitorTeardown]"
+ "-[AVCaptureExternalDisplayConfigurator _dispatchConfiguration]"
+ "-[AVCaptureExternalDisplayConfigurator _dispatchConfiguration]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorConfigure]"
+ "-[AVCaptureExternalDisplayConfigurator _displayConfigurationChangedMonitorTeardown]"
+ "-[AVCaptureExternalDisplayConfigurator _externalDisplayConfigurationChangedHandler]"
+ "-[AVCaptureExternalDisplayConfigurator _getConfigurationWithCompletion:]"
+ "-[AVCaptureExternalDisplayConfigurator _makeInActive]"
+ "-[AVCaptureExternalDisplayConfigurator _setup]"
+ "-[AVCaptureExternalDisplayConfigurator _setup]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator dealloc]"
+ "-[AVCaptureExternalDisplayConfigurator dispatchConfiguration]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:]"
+ "-[AVCaptureExternalDisplayConfigurator externalDisplayConfigurationChangedNotification:]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator externalDisplayLayerObserver:visibiltyChanged:]"
+ "-[AVCaptureExternalDisplayConfigurator externalDisplayLayerObserver:visibiltyChanged:]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator initWithDevice:previewLayer:configuration:]"
+ "-[AVCaptureExternalDisplayConfigurator observeValueForKeyPath:ofObject:change:context:]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator registerSelfForDisplay:]"
+ "-[AVCaptureExternalDisplayConfigurator registerSelfForDisplay:]_block_invoke"
+ "-[AVCaptureExternalDisplayConfigurator stop]_block_invoke"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]"
+ "-[AVCaptureMovieFileOutput _startRecording:]"
+ "-[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForFramings:]"
+ "-[AVCaptureSmartFramingMonitor _updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForSmartFramings:]"
+ "-[AVCaptureSmartFramingMonitor startMonitoring:]"
+ "-[AVCaptureSmartFramingMonitor startMonitoringWithError:]"
+ "-[AVCaptureSmartFramingMonitor stopMonitoring]"
+ "-[AVCaptureSmartFramingMonitor updateRecommendedSmartFramingWithFieldOfView:]"
+ "-[AVExternalSyncDevice _handleSourceDiedEvent]"
+ "-[AVExternalSyncDevice _handleUSBConnectionStateChange:]"
+ "-[AVExternalSyncDevice handleClockReceived:]"
+ "-[AVExternalSyncDevice handleClockSetupFailedWithError:]"
+ "-[AVExternalSyncDevice handleFollowForDevice:withSessionRunning:]"
+ "-[AVExternalSyncDevice handleFollowTimeout]"
+ "-[AVExternalSyncDevice handleLockStateUpdateTriggerID:lockState:]"
+ "-[AVExternalSyncDevice handleSessionStateChange:]"
+ "-[AVExternalSyncDevice handleTSMSGOutOfBoundsTriggerID:error:]_block_invoke"
+ "-[AVExternalSyncDevice handleTSMSGSessionStoppedTriggerID:status:]"
+ "-[AVExternalSyncDevice handleTriggerPresentTriggerID:isPresentState:]"
+ "-[AVExternalSyncDevice handleUnfollow]"
+ "-[AVExternalSyncDevice notifyDelegateStatusChange]"
+ "2OOOD"
+ "93"
+ "<%@ %p shouldMatchFrameRate=%d, bypassColorSpaceConversion=%d>"
+ "<%@ %p>:"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Attempting to tear down colorspace monitoring observingDeviceColorspace:%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Attempting to tear down framerate monitoring observingDeviceFramerate:%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Cannnot Register for display %@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Destroy Configurator"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Disabling color matching on %{public}@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ DispatchConfiguration already scheduled so skipping configuration block=%@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Early exit since config was nil"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Error getting configuration for previewLayer"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ External configuration Synchronized=%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ External configuration applied retryConfiguration=%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Not active so skipping configuration active:%d registered: %d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Received UISDisplayConfigurationChangedNotification"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Received UISDisplayConfigurationChangedNotification that does not contain id:%u"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Recieved device configuration update for keyPath:%{public}@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Register for display %@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Setting up colorspace monitoring preserveCaptureColorSpaceOnOutput:%{public}d observingDeviceColorspace:%d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Setting up configurator"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Setting up display configuration monitoring"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Setting up framerate monitoring configureFrameDuration:%{public}d observingDeviceFramerate:%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Start Configurator with configuration %{public}@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Teardown display configuration monitoring"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ Updating config:%{public}@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ deviceAndDisplayInSync=%{public}d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ isVisible:%d"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ made config request:%@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ making inactive"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: %{public}@ scheduled _configurationBlock=%{public}@"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: Early exit since nil hardwareIdentifier"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: Early exit since self was released"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: ObserveValueForKeyPath early exit since self was released"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: called"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: configuration timed out"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: configurationTimeoutBlock early exit since self was released"
+ "<<<< AVCaptureExternalPreviewLayerConfigurator >>>> %s: early exit since self was released"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: <DockKit> iPhone is Docked to DockKit Mount. CenterStageEnabled: %d CenterStageActive: %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: Creating CMClock from TSClock failed: (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] dockedTrackingActive changed (newValue: %d)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: Auto white balance is not locked for ProRes Raw capture."
+ "<<<< AVCaptureSmartFramingMonitor >>>> %s: One of the the enabled framings \"%{public}@\" has no match in the internal supported store!"
+ "<<<< AVCaptureSmartFramingMonitor >>>> %s: Recommended framing field of view \"%{public}@\" has no match in the internal supported store! Ignoring."
+ "<<<< AVCaptureSmartFramingMonitor >>>> %s: isMonitoring %d -> %d"
+ "<<<< AVExternalSyncDevice >>>> %s: %@{public} Delegate has been released"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ device:%{public}@"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ isConnected: %d"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ isPresentState: %d"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ lockState: %d"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ sessionInStart:%d"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ status: %d"
+ "<<<< AVExternalSyncDevice >>>> %s: Received fatal error from MSG"
+ "@\"AVCaptureExternalDisplayConfiguration\""
+ "@\"AVCaptureFraming\""
+ "@\"AVCaptureSmartFraming\""
+ "@\"AVCaptureSmartFramingMonitor\""
+ "@\"AVCaptureTimecodeSource\""
+ "@\"AVExternalSyncDevice\""
+ "@\"CIImage\""
+ "@\"FigStateMachine\""
+ "@\"NSOperationQueue\""
+ "@28@0:8@16f24"
+ "@28@0:8@?16i24"
+ "@32@0:8@16I24I28"
+ "@40@0:8@16q24@32"
+ "@64@0:8^{opaqueCMSampleBuffer=}16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56"
+ "A monitor may not be instantiated for a device that doesn't support smart framing"
+ "AVCaptureAspectRatio16x9"
+ "AVCaptureAspectRatio1x1"
+ "AVCaptureAspectRatio3x4"
+ "AVCaptureAspectRatio4x3"
+ "AVCaptureAspectRatio9x16"
+ "AVCaptureDeviceDynamicAspectRatioKey"
+ "AVCaptureDeviceDynamicAspectRatioRequest"
+ "AVCaptureDeviceDynamicAspectRatioRequestIDKey"
+ "AVCaptureDeviceSmartFramingSuggestedFieldOfView"
+ "AVCaptureDeviceSmartFramingSuggestedFieldOfViewChangedNotification"
+ "AVCaptureExternalDisplayConfiguration"
+ "AVCaptureExternalDisplayConfigurator"
+ "AVCaptureExternalDisplayConfigurator.m"
+ "AVCaptureFraming"
+ "AVCaptureMultiCamClientCompositingData"
+ "AVCaptureSmartFraming"
+ "AVCaptureSmartFramingMonitor"
+ "AVCaptureSystemStylePickerUT6"
+ "AVCaptureTimecodeGenerator"
+ "AVCaptureTimecodeGenerator.m"
+ "AVCaptureTimecodeSource"
+ "AVCaptureVideoStabilizationModeLowLatency"
+ "AVExternalSyncDevice"
+ "AVExternalSyncDeviceDeviceNotificationDelegate"
+ "AVExternalSyncDeviceDiscoverySession"
+ "AVExternalSyncDeviceDiscoverySession not supported - use -isSupported"
+ "AVExternalSyncState%@ state machine"
+ "ActiveSync"
+ "B56@0:8{?=CCCCI{?=qiIq}q}16"
+ "BrightPop"
+ "Camera sensor orientation compensation is not supported in the current configuration"
+ "CameraCapture"
+ "Capturing ProRes Raw codec is supported only on external storage device."
+ "Class getFBSMutableDisplayConfigurationRequestClass(void)_block_invoke"
+ "CompositionPictureInPictureRect"
+ "Configuring"
+ "CoreImageGainMapProperties"
+ "D23"
+ "Device may not be nil"
+ "Dynamic Aspect Ratio not supported by this device"
+ "DynamicAspectRatio"
+ "F < framesPerSecond"
+ "FBSDisplayConfiguration *AVUISDisplayConfigurationForContextID(uint32_t)"
+ "FBSMutableDisplayConfigurationRequest"
+ "Failed to create clock."
+ "FieldOfViewLandscape"
+ "FieldOfViewNone"
+ "FieldOfViewPortrait"
+ "FieldOfViewZoomedOutLandscape"
+ "FieldOfViewZoomedOutPortrait"
+ "Frame Counter"
+ "H < 24"
+ "Idle"
+ "InputPort"
+ "Internal error."
+ "JamSync"
+ "M < kMinutesPerHour"
+ "MIDI Discovery Client"
+ "MIDIClient"
+ "MultiCam client compositing is not enabled on this output"
+ "NSString *getUISDisplayConfigurationChangedNotification(void)"
+ "NSString *getUISSDisplayConfigurationAffectedContextIDsKey(void)"
+ "Not supported - must use AVCaptureMultiCamSession with this receiver"
+ "Not supported - use isMultiCamClientCompositingSupported"
+ "Only one device can use activeExternalSyncVideoFrameDuration or activeLockedVideoFrameDuration"
+ "OutputAspectRatio_SPI"
+ "PreviewLayer may not be nil"
+ "Real Time Clock"
+ "S < kSecondsPerMinute"
+ "SMART_STYLE_BRIGHTPOP"
+ "SmartCrop"
+ "SmartFramingMonitoringInternal"
+ "Square crop must be NO when the active format supports dynamic aspect ratios"
+ "T2030"
+ "T@\"<AVCaptureTimecodeGeneratorDelegate>\",R,N"
+ "T@\"AVCaptureFraming\",R,N"
+ "T@\"AVCaptureTimecodeSource\",R,N"
+ "T@\"AVCaptureTimecodeSource\",R,N,V_currentSource"
+ "T@\"AVExternalSyncDevice\",R,N"
+ "T@\"AVExternalSyncDeviceDiscoverySession\",R"
+ "T@\"NSDictionary\",&,N,V_compositingMetadata"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_delegateCallbackQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSString\",R,C,N,V_displayName"
+ "T@\"NSString\",R,N,V_uniqueIdentifier"
+ "T@\"NSUUID\",R,C,N,V_uuid"
+ "T@\"NSUUID\",R,N,V_identifier"
+ "T@\"NSUUID\",R,N,V_uuid"
+ "T@?,C,N,V_configurationTimeoutBlock"
+ "T@?,R,C,N,V_dynamicAspectRatioCompletionBlock"
+ "TB,N,GisActive,V_active"
+ "TB,N,GisCameraSensorOrientationCompensationEnabled"
+ "TB,N,GisLocked,V_locked"
+ "TB,N,GisSessionRunning,V_sessionRunning"
+ "TB,N,V_bypassColorSpaceConversion"
+ "TB,N,V_observingDeviceColorspace"
+ "TB,N,V_observingDeviceFramerate"
+ "TB,N,V_registered"
+ "TB,N,V_retryConfiguration"
+ "TB,N,V_shouldMatchFrameRate"
+ "TB,R,GisBypassingColorSpaceConversionSupported"
+ "TB,R,GisMatchingFrameRateSupported"
+ "TB,R,GisPreferredResolutionSupported"
+ "TB,R,GisSmartFramingMonitoringSupported"
+ "TB,R,N,GisCameraSensorOrientationCompensationSupported"
+ "TB,R,N,GisExternalSyncSupported"
+ "TB,R,N,GisFollowingExternalSyncDevice"
+ "TB,R,N,GisLockedVideoFrameDurationSupported"
+ "TB,R,N,GisMonitoring"
+ "TB,R,N,GisUsbConnected,V_usbConnected"
+ "TB,R,N,GisVideoFrameDurationLocked,V_videoFrameDurationLocked"
+ "TI,R,N,V_productID"
+ "TI,R,N,V_vendorID"
+ "T^{OpaqueCMClock=},R,N,V_clock"
+ "T^{opaqueCMSampleBuffer=},R,N,V_outputGainMapSampleBuffer"
+ "T^{opaqueCMSampleBuffer=},R,N,V_outputSampleBuffer"
+ "T^{opaqueCMSampleBuffer=},R,N,V_primaryGainMapSampleBuffer"
+ "T^{opaqueCMSampleBuffer=},R,N,V_primarySampleBuffer"
+ "T^{opaqueCMSampleBuffer=},R,N,V_secondaryGainMapSampleBuffer"
+ "T^{opaqueCMSampleBuffer=},R,N,V_secondarySampleBuffer"
+ "Td,N,V_activeExternalDisplayFrameRate"
+ "Td,N,V_synchronizationTimeout"
+ "Td,N,V_timecodeAlignmentOffset"
+ "The primary connection has not been not added to this output"
+ "The primary connection must be a video connection"
+ "The secondary connection has not been added to this output"
+ "The secondary connection must be a video connection"
+ "Timed out syncing to external pulse."
+ "Tq,R,N,V_type"
+ "T{?=ii},N,V_preferredResolution"
+ "T{?=qiIq},N,V_signalCompensationDelay"
+ "T{?=qiIq},N,V_timecodeFrameDuration"
+ "UISDisplayConfigurationChangedNotification"
+ "UISDisplayConfigurationForContextID"
+ "UISRequestDisplayConfigurationForContextID"
+ "UISSDisplayConfigurationAffectedContextIDsKey"
+ "Unavailable"
+ "Unnamed MIDI Device"
+ "Unsupported operation - can't set activeVideoMaxFrameDuration when AVCaptureDeviceInput's activeLockedVideoFrameDuration is set."
+ "Unsupported operation - can't set activeVideoMinFrameDuration when AVCaptureDeviceInput's activeLockedVideoFrameDuration is set."
+ "V53"
+ "V53-V54"
+ "V54"
+ "V57"
+ "Video settings dimensions must match the source device's dynamic aspect ratio"
+ "^{?={?=CCCCI{?=qiIq}q}Q}"
+ "_active"
+ "_activeExternalDisplayFrameRate"
+ "_activeExternalSyncDevice"
+ "_activeExternalSyncVideoFrameDuration"
+ "_activeExternalSyncVideoFrameDurationOwner"
+ "_activeLockedVideoFrameDuration"
+ "_activeLockedVideoFrameDurationOwner"
+ "_addTimecodeToRingBuffer:timestamp:"
+ "_applyActiveExternalSyncVideoFrameDuration"
+ "_applyActiveLockedVideoFrameDuration"
+ "_aspectRatio"
+ "_bypassColorSpaceConversion"
+ "_captureDeviceInput"
+ "_clock"
+ "_compositingMetadata"
+ "_configuration"
+ "_configurationBlock"
+ "_configurationTimeoutBlock"
+ "_configuratorWeakReference"
+ "_configureExternalDisplay"
+ "_configureExternalDisplayColorspace"
+ "_configureExternalDisplayFrameRate"
+ "_currentSource"
+ "_delegateCallbackQueue"
+ "_deviceColorspaceChangeMonitorConfigure"
+ "_deviceColorspaceChangeMonitorTeardown"
+ "_deviceFramerateChangedMonitorConfigure"
+ "_deviceFramerateChangedMonitorTeardown"
+ "_deviceLock"
+ "_dispatchConfiguration"
+ "_displayConfigurationChangedMonitorConfigure"
+ "_displayConfigurationChangedMonitorTeardown"
+ "_drainDynamicAspectRatioRequestQueue"
+ "_dynamicAspectRatio"
+ "_dynamicAspectRatioCompletionBlock"
+ "_dynamicAspectRatioRequestID"
+ "_dynamicAspectRatioRequestQueue"
+ "_dynamicDimensions"
+ "_enabledFramings"
+ "_enabledSmartFramings"
+ "_externalDisplayConfigurationChangedHandler"
+ "_framingsLock"
+ "_getConfigurationWithCompletion:"
+ "_handleChangedActiveFormat:"
+ "_handleLiveReconfigurationCompletionWithPayload:"
+ "_handleNotification:dict:"
+ "_handleSourceDiedEvent"
+ "_handleUSBConnectionStateChange:"
+ "_handleUnfollow"
+ "_imageForGainMapSampleBuffer:"
+ "_imageForSampleBuffer:gainMapMetadata:"
+ "_initWithAspectRatio:zoomFactor:"
+ "_initWithCompletionBlock:requestID:"
+ "_initWithIdentifier:pid:vid:"
+ "_initWithPrimarySampleBuffer:primaryGainMapSampleBuffer:secondarySampleBuffer:secondaryGainMapSampleBuffer:outputSampleBuffer:outputGainMapSampleBuffer:"
+ "_invokeClientCompositingCallbackForSettingsID:compositingData:"
+ "_invokeClientCompositingCallbackForSinkID:settingsID:compositingData:"
+ "_isMonitoring"
+ "_isMonitoringLock"
+ "_isProResRawRecordingAndAWBIsNotLockedForWrapper:"
+ "_isTimecodeRingBufferEmpty"
+ "_isTimecodeRingBufferFull"
+ "_isTimecodeRingBufferStale"
+ "_localGMTOffset"
+ "_locked"
+ "_machTimebase"
+ "_makeInActive"
+ "_midiClient"
+ "_midiInputPort"
+ "_midiSourceDiscoveryClient"
+ "_monitorWeakReference"
+ "_mutableSynchronizationSources"
+ "_newestTimecodeRingBufferEntry"
+ "_notifyDelegateOfError:"
+ "_notifyDelegateOfSourceListUpdate:"
+ "_notifyDelegateOfSynchronizationStatusChange:filterRedundancy:"
+ "_notifyDelegateOfTimecodeUpdate:"
+ "_observationLayer"
+ "_observingDeviceColorspace"
+ "_observingDeviceFramerate"
+ "_openMidiTimecodeDataStreamWithUUID:success:"
+ "_outputGainMapSampleBuffer"
+ "_outputSampleBuffer"
+ "_photoModeFieldsOfView"
+ "_photoModeFramings"
+ "_photoModeSmartFramings"
+ "_pollRingBufferStatus"
+ "_populatePhotoModeSmartFramingsAndFieldsOfViewFromZoomFactorsByFieldOfView:"
+ "_preferredResolution"
+ "_primaryCaptureRectSmartFramingTransitionPercentComplete"
+ "_primaryCaptureRectSmartFramingTransitionTargetFieldOfView"
+ "_primaryGainMapImage"
+ "_primaryGainMapSampleBuffer"
+ "_primaryImage"
+ "_primarySampleBuffer"
+ "_productID"
+ "_recommendedFraming"
+ "_recommendedSmartFraming"
+ "_registerMidiEndpointAsSynchronizationSource:"
+ "_registerSynchronizationSource:"
+ "_registered"
+ "_removeMidiEndpointAsSynchronizationSource:"
+ "_removeSynchronizationSource:"
+ "_resetActiveLockedVideoFrameDurationWithFormatChanged:"
+ "_resetTimecodeRingBuffer"
+ "_resourceLock"
+ "_retryConfiguration"
+ "_ringBufferStatusPollingQueue"
+ "_scheduleTimecodeRingBufferPolling"
+ "_secondaryGainMapImage"
+ "_secondaryGainMapSampleBuffer"
+ "_secondaryImage"
+ "_secondarySampleBuffer"
+ "_serverDiedObserver"
+ "_sessionRunning"
+ "_setDelegate:"
+ "_setEnabledSmartFramingFieldsOfView:"
+ "_setGenlockSignalCompensationDelay:"
+ "_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:"
+ "_setSmartFramingMonitorRunning:"
+ "_setup"
+ "_setupStateMachine"
+ "_shouldMatchFrameRate"
+ "_signalCompensationDelay"
+ "_smartFramingMonitor"
+ "_smartFramingMonitoringSupported"
+ "_sourceLock"
+ "_stateMachine"
+ "_statusNotificationSchedulingQueue"
+ "_supportedFramings"
+ "_supportedSmartFramings"
+ "_synchronizationStatus"
+ "_synchronizationTimeout"
+ "_timeOfDay"
+ "_timecodeAlignmentOffset"
+ "_timecodeFrameDuration"
+ "_timecodeIsCoherent:"
+ "_timecodeRingBuffer"
+ "_timecodeRingBufferCapacity"
+ "_timecodeRingBufferHead"
+ "_timecodeRingBufferIngestTimeStamp"
+ "_unfollowTimeoutBlock"
+ "_updateCameraSensorOrientationCompensationSupportedForDevice:"
+ "_updateDevicesEvent:"
+ "_updateExternalSyncSupported"
+ "_updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForFramings:"
+ "_updateFigCaptureSourceEnabledSmartFramingFieldsOfViewForSmartFramings:"
+ "_updateLockedVideoFrameDurationSupported"
+ "_updateMultiCamClientCompositingCallback"
+ "_updateRectOfInterestSizeForSensorOrientationAndDynamicAspectRatio:"
+ "_usbConnected"
+ "_uuid"
+ "_vendorID"
+ "_videoFrameDurationLocked"
+ "_zoomFactor"
+ "activeExternalDisplayFrameRate"
+ "activeExternalSyncVideoFrameDuration"
+ "activeLockedVideoFrameDuration"
+ "activeLockedVideoFrameDuration can not be set while external sync is running. Stop the external sync with -unfollowExternalSyncDevice before setting the activeLockedVideoFrameDuration."
+ "activeLockedVideoFrameDuration is not supported on this device. Check the device minSupportedLockedVideoFrameDuration property."
+ "activeLockedVideoFrameDuration is not supported with this configuration - use -[AVCaptureDeviceInput isLockedVideoFrameDurationSupported] "
+ "activeLockedVideoFrameDuration must be less than the device minSupportedLockedVideoFrameDuration property."
+ "activeVideoExternalSyncDevice"
+ "addOperationWithBlock:"
+ "applyActiveExternalSyncVideoFrameDuration"
+ "aspectRatio"
+ "autoVideoFrameRateEnabled may not be set to true when isFollowingExternalSyncDevice is true."
+ "autoVideoFrameRateEnabled may not be set to true when isVideoFrameDurationLocked is true."
+ "availableSources"
+ "avcaptureexternaldisplayconfigurator_trace"
+ "avcaptureframing_trace"
+ "avcapturesmartframingmonitor_trace"
+ "avexternalsyncdevice_trace"
+ "bypassColorSpaceConversion"
+ "bypassColorSpaceConversion is not supported"
+ "callbackQueue"
+ "cameraSensorOrientationCompensationAutomaticallyEnabled"
+ "cameraSensorOrientationCompensationEnabled"
+ "cameraSensorOrientationCompensationSupported"
+ "cancelAllOperations"
+ "captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:"
+ "captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:"
+ "captureOutput:readyForClientCompositingForOutputFileAtURL:primaryPixelBuffer:primaryPTS:secondaryPixelBuffer:secondaryPTS:outputPixelBuffer:compositeMetadata:"
+ "captureOutput:readyForClientCompositingForResolvedSettings:compositingData:"
+ "captureOutput:readyForClientCompositingForResolvedSettings:primaryPixelBuffer:primaryPTS:secondaryPixelBuffer:secondaryPTS:outputPixelBuffer:compositeMetadata:"
+ "com.alibaba.dingtalklite"
+ "com.apple.avcaptureexternaldisplayconfigurator"
+ "com.apple.avcaptureexternalsyncdevice"
+ "com.apple.avfoundation.timecode.ringBufferStatusPollingQueue"
+ "com.apple.avfoundation.timecode.statusOperationSchedulingQueue"
+ "com.firespotter.UberConference"
+ "com.google.Tachyon"
+ "com.hammerandchisel.discord"
+ "com.iwilab.KakaoTalk"
+ "com.viber"
+ "compositingMetadata"
+ "configurationTimeoutBlock"
+ "currentSource"
+ "dispatchConfiguration"
+ "drainDynamicAspectRatioCompletionHandlers"
+ "dynamicAspectRatio"
+ "dynamicAspectRatioAndDynamicAspectRatioRequestID"
+ "dynamicAspectRatioCompletionBlock"
+ "dynamicAspectRatioRequestID"
+ "dynamicAspectRatioRequestWithCompletionBlock:requestID:"
+ "dynamicAspectRatioSupported"
+ "dynamicDimensions"
+ "enabledFramings"
+ "enabledFramings may not be nil"
+ "enabledFramings must only contain values present in supportedFramings"
+ "enabledSmartFramings"
+ "enabledSmartFramings may not be nil"
+ "enabledSmartFramings must only contain values present in supportedSmartFramings"
+ "externalDisplayAndCaptureDeviceSynchronized"
+ "externalDisplayConfigurationChangedNotification:"
+ "externalSyncDevice"
+ "externalSyncDevice:failedWithError:"
+ "externalSyncDeviceStatusDidChange:"
+ "externalSyncSupported"
+ "f28@0:8@16B24"
+ "followExternalSyncDevice:videoFrameDuration:delegate:"
+ "followExternalSyncDevice:videoFrameDuration:delegate: can not be called while syncDevice.status is not in AVExternalSyncDeviceStatusReady. Call unfollowExternalSyncDevice before setting external sync."
+ "followExternalSyncDevice:videoFrameDuration:delegate: is not supported by this device - use -[AVCaptureDeviceInput isExternalSyncSupported] "
+ "followExternalSyncDevice:videoFrameDuration:delegate: is not supported on this device. Check the device minSupportedExternalSyncFrameDuration property."
+ "followExternalSyncDevice:videoFrameDuration:delegate: with can not be called while lockedFrameDuration is running. Set activeLockedVideoFrameDuration = kCMTimeInvalid before setting external sync."
+ "followingExternalSyncDevice"
+ "frameCountSource"
+ "frameDuration must be less than the device minSupportedExternalSyncFrameDuration property."
+ "frameDuration.value != 0"
+ "frameQuanta >= 1"
+ "framesPerSecond != 0"
+ "framesToDrop < framesPerSecond"
+ "framingWithAspectRatio:zoomFactor:"
+ "generateInitialTimecode"
+ "geometricDistortionCorrectedVideoFieldOfViewForAspectRatio:"
+ "getUUIDBytes:"
+ "handleChangedDynamicAspectRatio:forFormat:"
+ "handleChangedMSGPulseDurationForDevice:"
+ "handleClockReceived:"
+ "handleClockSetupFailedWithError:"
+ "handleFollowForDevice:withSessionRunning:"
+ "handleFollowTimeout"
+ "handleLockStateUpdateTriggerID:lockState:"
+ "handleSessionStateChange:"
+ "handleTSMSGOutOfBoundsTriggerID:error:"
+ "handleTSMSGSessionStoppedTriggerID:status:"
+ "handleTransitionToActiveSync"
+ "handleTransitionToActiveSyncFromConfiguring"
+ "handleTransitionToConfiguring"
+ "handleTransitionToIdle"
+ "handleTransitionToJamSync"
+ "handleTransitionToUnavailable"
+ "handleTriggerPresentTriggerID:isPresentState:"
+ "handleUnfollow"
+ "hardwareIdentifier"
+ "horizontalFieldOfViewForAspectRatio:"
+ "horizontalGeometricDistortionCorrectedFieldOfViewForAspectRatio:"
+ "i32@0:8q16@24"
+ "i40@0:8@16q24@32"
+ "i80@?0^{__CFString=}8q16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^{opaqueCMSampleBuffer=}64r^^{__CFDictionary}72"
+ "iOS 26.0"
+ "imageWithCVPixelBuffer:options:"
+ "initWithDevice:previewLayer:configuration:"
+ "initWithDevice:smartFramingZoomFactorsByFieldOfView:"
+ "initWithDisplayName:sourceType:uuid:"
+ "initWithLabel:stateCount:initialState:owner:"
+ "initWithUUIDBytes:"
+ "isBypassingColorSpaceConversionSupported"
+ "isCameraSensorOrientationCompensationEnabled"
+ "isCameraSensorOrientationCompensationSupported"
+ "isDockedTrackingActive"
+ "isDynamicAspectRatioSupported"
+ "isExternalSyncSupported"
+ "isFollowingExternalSyncDevice"
+ "isLocked"
+ "isLockedVideoFrameDurationSupported"
+ "isMatchingFrameRateSupported"
+ "isMonitoring"
+ "isMountedInPortraitOrientation"
+ "isMultiCamClientCompositingEnabled"
+ "isMultiCamClientCompositingSupported"
+ "isPreferredResolutionSupported"
+ "isSessionRunning"
+ "isSmartCropSupported"
+ "isSmartFramingMonitoringSupported"
+ "isSmartFramingSupported"
+ "isSubsetOfSet:"
+ "isUsbConnected"
+ "isVideoFrameDurationLocked"
+ "isfinite( nominalFPS ) && nominalFPS > 0"
+ "isfinite(frameRate)"
+ "isfinite(nominalFPS) && nominalFPS > 0"
+ "jp.naver.line"
+ "keyStatus == errSecSuccess && ivStatus == errSecSuccess"
+ "locked"
+ "lockedVideoFrameDurationSupported"
+ "maxUpscalingDimensions"
+ "minSupportedExternalSyncFrameDuration"
+ "minSupportedLockedVideoFrameDuration"
+ "monitoring"
+ "mountedInPortraitOrientation"
+ "multiCamClientCompositingEnabled"
+ "multiCamClientCompositingPrimaryConnection"
+ "notifyDelegateStatusChange"
+ "observingDeviceColorspace"
+ "observingDeviceFramerate"
+ "org.whispersystems.signal"
+ "outputAspectRatio"
+ "outputGainMapSampleBuffer"
+ "outputSampleBuffer"
+ "ph.telegra.Telegraph"
+ "preferredResolution"
+ "preferredResolution cannot have negative width or height"
+ "preferredResolution is not supported"
+ "primaryGainMapImage"
+ "primaryGainMapSampleBuffer"
+ "primaryImage"
+ "primarySampleBuffer"
+ "productID"
+ "queue"
+ "realTimeClockSource"
+ "recommendedFraming"
+ "recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:"
+ "recommendedSmartFraming"
+ "refreshRate"
+ "registerConfigurator:withDisplayIdentifier:"
+ "registerSelfForDisplay:"
+ "registered"
+ "resetActiveLockedVideoFrameDurationForOwner:"
+ "resetDeviceClockAndInputPortsToHostClock"
+ "retryConfiguration"
+ "secondaryGainMapImage"
+ "secondaryGainMapSampleBuffer"
+ "secondaryImage"
+ "secondarySampleBuffer"
+ "seconds > 0.0"
+ "secondsFromGMTForDate:"
+ "sensorOrientation"
+ "sessionRunning"
+ "setActive:"
+ "setActiveExternalDisplayFrameRate:"
+ "setActiveExternalSyncSignalCompensationDelay:withExternalSyncDevice:"
+ "setActiveExternalSyncVideoFrameDuration:withExternalSyncDevice:forOwner:"
+ "setActiveLockedVideoFrameDuration:"
+ "setActiveLockedVideoFrameDuration:forOwner:"
+ "setActiveSyncDevice:"
+ "setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:"
+ "setAllowsColorMatching:"
+ "setBypassColorSpaceConversion:"
+ "setCameraSensorOrientationCompensationEnabled:"
+ "setCompositingMetadata:"
+ "setConfigurationTimeoutBlock:"
+ "setDisableFrameDoubling:"
+ "setDynamicAspectRatio:completionHandler:"
+ "setEnabledFramings:"
+ "setEnabledSmartFramings:"
+ "setExternalSyncFrameRate:"
+ "setLabel:forState:"
+ "setLocked:"
+ "setLockedFrameRate:"
+ "setMaxConcurrentOperationCount:"
+ "setMultiCamClientCompositingEnabled:"
+ "setMultiCamClientCompositingPrimaryConnection:secondaryConnection:"
+ "setMultiCamClientCompositingPrimaryConnectionID:"
+ "setName:"
+ "setNativePixelSize:"
+ "setObservingDeviceColorspace:"
+ "setObservingDeviceFramerate:"
+ "setOutputAspectRatio:"
+ "setOutputAspectRatio:completionHandler:"
+ "setOutputAspectRatioRequestID:"
+ "setOverscanCompensation:"
+ "setPerformsAtomicStateTransitions:"
+ "setPreferredResolution:"
+ "setPrimaryCaptureRectAspectRatio:centerPoint:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:"
+ "setRefreshRate:"
+ "setRegistered:"
+ "setRetryConfiguration:"
+ "setSessionRunning:"
+ "setShouldMatchFrameRate:"
+ "setSignalCompensationDelay:"
+ "setSynchronizationTimeout:"
+ "setTimecodeAlignmentOffset:"
+ "setTimecodeFrameDuration:"
+ "setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:"
+ "setupNotifications"
+ "setupSource"
+ "shouldMatchFrameRate"
+ "shouldMatchFrameRate is not supported"
+ "shouldMatchFrameRateSupported"
+ "signalCompensationDelay"
+ "sleepForTimeInterval:"
+ "smartCropFeatureFlagEnabled"
+ "smartCropFormat"
+ "smartCropSupported"
+ "smartFramingMonitor"
+ "smartFramingMonitoringSupported"
+ "smartFramingWithAspectRatio:zoomFactor:"
+ "startExternalSourceObserver"
+ "startMonitoring:"
+ "startMonitoringWithError:"
+ "startSynchronizationWithTimecodeSource:"
+ "state"
+ "stopMonitoring"
+ "supportedDynamicAspectRatios"
+ "supportedFramings"
+ "supportedOutputAspectRatios"
+ "supportedProResRawCodecTypes"
+ "supportedSmartFramings"
+ "supportsBypassingColorSpaceConversion"
+ "supportsPreferredResolution"
+ "synchronizationTimeout"
+ "systemTimeZone"
+ "teardownNotifications"
+ "teardownSource"
+ "tg_calculateDropFramesPerEvent"
+ "tg_createTimeCode32FormatDescription"
+ "tg_initializeUUIDEncryptionParametersIfNeeded"
+ "tg_packageTimecodeAsMetadataBuffer"
+ "tg_timecodeFromTotalFrames"
+ "tg_totalFramesFromTimecode"
+ "timecode != NULL"
+ "timecode->frameDuration.value != 0"
+ "timecode->frames < framesPerSecond"
+ "timecode->hours < 24"
+ "timecode->minutes < kSecondsPerMinute"
+ "timecode->seconds < kSecondsPerMinute"
+ "timecodeAlignmentOffset"
+ "timecodeFrameDuration"
+ "timecodeGenerator:didReceiveUpdate:fromSource:"
+ "timecodeGenerator:didUpdateAvailableSources:"
+ "timecodeGenerator:transitionedToSynchronizationStatus:forSource:"
+ "transitionToState:"
+ "transitionToState:fromState:"
+ "unfollowExternalSyncDevice"
+ "uniqueIdentifier"
+ "updateClientVideoSettingsForAspectRatio:"
+ "updateMetadataTransformForSourceFormat:aspectRatio:"
+ "updateRecommendedSmartFramingWithFieldOfView:"
+ "usbConnected"
+ "utilizesRingBufferSyncDiscipline"
+ "v16@?0@\"FBSDisplayConfiguration\"8"
+ "v16@?0r^{MIDINotification=iI}8"
+ "v24@0:8I16B20"
+ "v24@0:8I16I20"
+ "v24@?0r^{MIDIEventList=iI[1{MIDIEventPacket=QI[64I]}]}8^v16"
+ "v28@0:8@\"AVCaptureDeviceInput\"16B24"
+ "v28@?0@\"AVExternalSyncDevice\"8I16I20i24"
+ "v32@0:8@16^B24"
+ "v32@0:8{?=ff}16@?24"
+ "v56@0:8@16{?=qiIq}24@48"
+ "v56@0:8d16{CGPoint=dd}24d40@48"
+ "v56@0:8{?=CCCCI{?=qiIq}q}16"
+ "v56@0:8{?=qiIq}16@40@48"
+ "v64@0:8d16{CGPoint=dd}24d40d48@56"
+ "v64@0:8{?=CCCCI{?=qiIq}q}16Q56"
+ "v64@0:8{?=qiIq}16{?=qiIq}40"
+ "variableFrameRateVideoCaptureEnabled may not be set to true when activeExternalSyncVideoFrameDuration is set."
+ "variableFrameRateVideoCaptureEnabled may not be set to true when activeLockedVideoFrameDuration is set."
+ "vendorID"
+ "verticalFieldOfViewForAspectRatio:"
+ "verticalGeometricDistortionCorrectedFieldOfViewForAspectRatio:"
+ "videoFieldOfViewForAspectRatio:"
+ "videoFieldOfViewForAspectRatio:geometricDistortionCorrected:"
+ "videoFrameDurationLocked"
+ "void AVUISRequestDisplayConfigurationForContextID(uint32_t, FBSDisplayConfigurationRequest *)"
+ "waitUntilAllOperationsAreFinished"
+ "whenTransitioningToState:callHandler:"
+ "zoomFactor"
+ "{?=CCCCI{?=qiIq}q}16@0:8"
+ "{?={?=CCCCI{?=qiIq}q}Q}16@0:8"
+ "{CGAffineTransform=dddddd}60@0:8{CGSize=dd}16{CGSize=dd}32@48B56"
+ "{CGSize=dd}32@0:8{CGSize=dd}16"
+ "{mach_timebase_info=\"numer\"I\"denom\"I}"
- "2OOOA"
- "_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:"
- "captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:"
- "updateMetadataTransformForSourceFormat:"
- "{CGAffineTransform=dddddd}56@0:8{CGSize=dd}16{CGSize=dd}32@48"

```
