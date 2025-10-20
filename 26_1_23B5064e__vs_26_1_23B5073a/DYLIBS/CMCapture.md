## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-664.40.18.0.0
-  __TEXT.__text: 0x5b3134
-  __TEXT.__auth_stubs: 0x52b0
-  __TEXT.__objc_methlist: 0x33ba0
+664.42.7.0.1
+  __TEXT.__text: 0x5bc838
+  __TEXT.__auth_stubs: 0x52c0
+  __TEXT.__objc_methlist: 0x33da0
   __TEXT.__const: 0x151150
-  __TEXT.__cstring: 0x913a8
-  __TEXT.__oslogstring: 0x3cec3
-  __TEXT.__gcc_except_tab: 0x2aec
+  __TEXT.__cstring: 0x91d99
+  __TEXT.__oslogstring: 0x3df35
+  __TEXT.__gcc_except_tab: 0x2b50
   __TEXT.__dlopen_cstrs: 0x65d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xe598
+  __TEXT.__unwind_info: 0xe6c0
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x83fd
-  __TEXT.__objc_methname: 0xa6013
-  __TEXT.__objc_methtype: 0x161cf
-  __TEXT.__objc_stubs: 0x47940
-  __DATA_CONST.__got: 0x68a0
-  __DATA_CONST.__const: 0xe868
-  __DATA_CONST.__objc_classlist: 0x1bb8
+  __TEXT.__objc_classname: 0x8425
+  __TEXT.__objc_methname: 0xa69d2
+  __TEXT.__objc_methtype: 0x1626a
+  __TEXT.__objc_stubs: 0x47ee0
+  __DATA_CONST.__got: 0x68a8
+  __DATA_CONST.__const: 0xeb20
+  __DATA_CONST.__objc_classlist: 0x1bc0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x147d8
+  __DATA_CONST.__objc_selrefs: 0x14908
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1a18
-  __DATA_CONST.__objc_arraydata: 0x37d0
-  __AUTH_CONST.__auth_got: 0x2968
+  __DATA_CONST.__objc_superrefs: 0x1a20
+  __DATA_CONST.__objc_arraydata: 0x37d8
+  __AUTH_CONST.__auth_got: 0x2970
   __AUTH_CONST.__const: 0x4200
-  __AUTH_CONST.__cfstring: 0x442a0
-  __AUTH_CONST.__objc_const: 0x938f8
-  __AUTH_CONST.__objc_intobj: 0x5b20
-  __AUTH_CONST.__objc_arrayobj: 0x2880
+  __AUTH_CONST.__cfstring: 0x44640
+  __AUTH_CONST.__objc_const: 0x93e00
+  __AUTH_CONST.__objc_intobj: 0x5b38
+  __AUTH_CONST.__objc_arrayobj: 0x2898
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa90
-  __AUTH.__objc_data: 0x32f0
-  __DATA.__objc_ivar: 0xa774
+  __AUTH.__objc_data: 0x3340
+  __DATA.__objc_ivar: 0xa7fc
   __DATA.__data: 0x54c0
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xb20
+  __DATA.__common: 0xb40
   __DATA.__bss: 0x2630
   __DATA_DIRTY.__objc_data: 0xe240
   __DATA_DIRTY.__data: 0x1088

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 68A7C3AD-45B2-36D8-AABE-855956BFEED6
-  Functions: 31029
-  Symbols:   101821
-  CStrings:  51448
+  UUID: FA632AB9-52BB-3F4E-8B2C-4FBE246F81E0
+  Functions: 31144
+  Symbols:   102192
+  CStrings:  51646
 
Symbols:
+ +[FigCaptureSessionAttachedSessionManager initialize]
+ -[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:sessionIsPrewarming:]
+ -[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:completionHandler:]
+ -[BWFaceDetectionNode updateMetadataIdentifiers:rectOfInterest:emitsEmptyObjectDetectionMetadata:]
+ -[BWFanOutNode activateExtendedOutput:]
+ -[BWFanOutNode addExtendedOutput]
+ -[BWFanOutNode removeExtendedOutput:]
+ -[BWFigVideoCaptureDevice setMaximumFrameRate:attachedSessionID:]
+ -[BWFigVideoCaptureStream setMaximumFrameRate:attachedSessionID:]
+ -[BWFunnelNode addExtendedInput]
+ -[BWGraph cancelLiveExtension:]
+ -[BWGraph commitLiveExtension:withError:]
+ -[BWGraph commitLiveExtension:withError:].cold.1
+ -[BWGraph createAndBeginLiveExtension]
+ -[BWGraph createAndBeginLiveExtension].cold.1
+ -[BWGraph prepareLiveExtensionToBecomeLive:]
+ -[BWMultiStreamCameraSourceNode activateSecureMetadataOutputConfiguration:forAttachedSesssion:]
+ -[BWMultiStreamCameraSourceNode deactivateSecureMetadataForAttachedSession:]
+ -[BWSecureMetadataOutputConfigurator registerAttachedSessionID:]
+ -[BWSecureMetadataOutputConfigurator resetAllConfigurations]
+ -[BWSecureMetadataOutputConfigurator setConfiguration:forAttachedSessionID:]
+ -[BWSecureMetadataOutputConfigurator setMaximumFrameRate:forAttachedSessionID:]
+ -[BWSecureMetadataOutputConfigurator unregisterAttachedSessionID:]
+ -[CMCaptureLocalSessionController _determineMetadataCameraConfiguration]
+ -[CMCaptureLocalSessionController _newMetadataCameraFigCaptureSessionConfiguration]
+ -[CMCaptureLocalSessionController _resolveMetadataCameraFigCaptureSessionConfigurationValuesFromLocalSessionConfigurationValues]
+ -[CMCaptureLocalSessionController _startSessionForMetadataCameraStream:outError:]
+ -[CMCaptureLocalSessionController _stopSessionForMetadataCameraStream:outError:]
+ -[CMCaptureLocalSessionController _updateSessionConfigurationForMetadataCameraStream]
+ -[CMCaptureLocalSessionController metadataCameraSourceAttributes]
+ -[CMCaptureLocalSessionOutputStream _copyMetadataOnlySampleBufferFromSampleBuffer:]
+ -[CMCaptureLocalSessionOutputStream faceTrackingAttributes]
+ -[CMCaptureLocalSessionOutputStream setFaceTrackingAttributes:]
+ -[FigCaptureCameraSourcePipeline activateSecureMetadataOutputConfigurationForSessionID:]
+ -[FigCaptureCameraSourcePipeline addMetadataOutputNetworksForSessionID:graph:]
+ -[FigCaptureCameraSourcePipeline createOutputNetworkForOutput:withFanOutCount:graph:sessionID:]
+ -[FigCaptureCameraSourcePipeline metadataCategoriesForConnectionConfiguration:]
+ -[FigCaptureCameraSourcePipeline metadataObjectConnectionConfigurationForSessionID:]
+ -[FigCaptureCameraSourcePipeline metadataOutputsByCategoryForSessionID:connectionConfiguration:]
+ -[FigCaptureCameraSourcePipeline registerAttachedSessionID:]
+ -[FigCaptureCameraSourcePipeline removeMetadataOutputNetworksForOutputs:graph:sessionID:]
+ -[FigCaptureCameraSourcePipeline removeMetadataOutputNetworksForSessionID:graph:]
+ -[FigCaptureCameraSourcePipeline setMetadataObjectConnectionConfiguration:forSessionID:]
+ -[FigCaptureMetadataSinkPipeline extendForNodeOutputs:withConnectionConfiguration:]
+ -[FigCaptureMetadataSinkPipeline removeNodeOutputs:withConnectionConfiguration:]
+ -[FigCaptureSessionAttachedSessionManager _generateStateLog]
+ -[FigCaptureSessionAttachedSessionManager _startNextSession]
+ -[FigCaptureSessionAttachedSessionManager _stopAttachedSessionsAndRemoveHostSession:]
+ -[FigCaptureSessionAttachedSessionManager attachToRunningSession:]
+ -[FigCaptureSessionAttachedSessionManager init]
+ -[FigCaptureSessionAttachedSessionManager sessionDidReconfigure:]
+ -[FigCaptureSessionAttachedSessionManager sessionDidStartRunning:sessionContainsVideoSource:sessionContainsCameraSource:]
+ -[FigCaptureSessionAttachedSessionManager sessionDidStopRunning:captureDeviceStolen:sessionIsEligibleToAttach:clientStartedSession:]
+ -[FigCaptureSessionAttachedSessionManager sessionInvalidated:]
+ -[FigCaptureSessionConfiguration eligibleToAttachToExistingCaptureSession]
+ -[FigCaptureSessionConfiguration supportsAttachingSessionConfiguration:]
+ -[FigCaptureSessionObservatory attachSessionToHostSession:]
+ -[FigCaptureSessionObservatory captureSessionInvalidated:]
+ -[FigCaptureSessionPipelines addCameraSourcePipeline:sessionID:]
+ -[FigCaptureSessionPipelines addMetadataSinkPipeline:sessionID:]
+ -[FigCaptureSessionPipelines cameraSourcePipelineWithSessionID:]
+ -[FigCaptureSessionPipelines metadataSinkPipelineWithSessionID:]
+ -[FigCaptureSessionPipelines removeCameraSourcePipelineWithSessionID:]
+ -[FigCaptureSessionPipelines removeMetadataSinkPipelineWithSessionID:]
+ -[FigCaptureSourceCommonSettings metadataCameraHostingSupported]
+ GCC_except_table128
+ GCC_except_table142
+ GCC_except_table170
+ GCC_except_table331
+ GCC_except_table338
+ GCC_except_table340
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table68
+ GCC_except_table71
+ _.compoundliteral.32
+ _.compoundliteral.33
+ _.compoundliteral.34
+ _.compoundliteral.35
+ _.compoundliteral.45
+ _.compoundliteral.46
+ _.compoundliteral.47
+ _.compoundliteral.48
+ _.compoundliteral.54
+ _.compoundliteral.55
+ _.compoundliteral.65
+ _.compoundliteral.66
+ _.compoundliteral.69
+ _.compoundliteral.70
+ _.compoundliteral.72
+ _.compoundliteral.73
+ _.compoundliteral.82
+ _BWMetadataCategoryToString
+ _BWStringFromPixelBufferWithOptions
+ _CAImageQueueSetNominalFrameRate
+ _CMCaptureLocalSessionSinkID_MetadataCameraMetadataObject
+ _CMIStringFromPixelBufferWithOptions
+ _FigCaptureSessionAttachSession
+ _FigCaptureSessionStartDetachedSession
+ _FigCaptureSessionStopAttachedSession
+ _FigCaptureSourceSetProperty
+ _FigVideoCaptureSourceActivateAttachedCaptureSource
+ _FigVideoCaptureSourceActivateAttachedCaptureSource.cold.1
+ _FigVideoCaptureSourceActivateAttachedCaptureSource.cold.2
+ _FigVideoCaptureSourceDeactivateAttachedCaptureSource
+ _J817_J818_J820_J821
+ _OBJC_CLASS_$_FigCaptureSessionAttachedSessionManager
+ _OBJC_IVAR_$_BWFanOutNode._extendedOutputs
+ _OBJC_IVAR_$_BWFanOutNode._extendedOutputsLock
+ _OBJC_IVAR_$_BWGraph._activeLiveExtension
+ _OBJC_IVAR_$_BWImageQueueSinkNode._imageQueueNominalFrameRate
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfigurator._maximumFrameRateByClientID
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfigurator._registeredAttachedSessionIDs
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfigurator._secondaryClientConfigurationsByClientID
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._activeMetadataCameraFaceTrackingAttributes
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._activeMetadataCameraMetadataIdentifiers
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraCaptureSession
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraCaptureSessionConfig
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraCaptureSessionRunning
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraCaptureSource
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraCaptureSourceAttributes
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataCameraSinkIDActive
+ _OBJC_IVAR_$_CMCaptureLocalSessionController._metadataDeviceFormat
+ _OBJC_IVAR_$_CMCaptureLocalSessionOutputStream._faceTrackingAttributes
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._hostingSupported
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._metadataConnectionConfigurationBySessionID
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._metadataFanOutNodeByMetadataCategory
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._metadataOutputsByCategoryForSessionIDAndSourceDeviceType
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._attachedSessions
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._changeSeed
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._currentPrimarySession
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._currentlyStartingSession
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._currentlyStartingSessionChangeSeed
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._detachingSessions
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._incompatibleSessions
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._queue
+ _OBJC_IVAR_$_FigCaptureSessionAttachedSessionManager._sessionsToStart
+ _OBJC_IVAR_$_FigCaptureSessionObservatory._attachedSessionManager
+ _OBJC_IVAR_$_FigCaptureSessionPipelines._cameraSourcePipelinesBySessionID
+ _OBJC_IVAR_$_FigCaptureSessionPipelines._metadataSinkPipelinesBySessionID
+ _OBJC_IVAR_$_FigCaptureSourceCommonSettings._metadataCameraHostingSupported
+ _OBJC_METACLASS_$_FigCaptureSessionAttachedSessionManager
+ __OBJC_$_CLASS_METHODS_FigCaptureSessionAttachedSessionManager
+ __OBJC_$_INSTANCE_METHODS_FigCaptureSessionAttachedSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_FigCaptureSessionAttachedSessionManager
+ __OBJC_CLASS_RO_$_FigCaptureSessionAttachedSessionManager
+ __OBJC_METACLASS_RO_$_FigCaptureSessionAttachedSessionManager
+ ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.116
+ ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.120
+ ___121-[FigCaptureSessionAttachedSessionManager sessionDidStartRunning:sessionContainsVideoSource:sessionContainsCameraSource:]_block_invoke
+ ___132-[FigCaptureSessionAttachedSessionManager sessionDidStopRunning:captureDeviceStolen:sessionIsEligibleToAttach:clientStartedSession:]_block_invoke
+ ___168-[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:completionHandler:]_block_invoke
+ ___62-[FigCaptureSessionAttachedSessionManager sessionInvalidated:]_block_invoke
+ ___65-[FigCaptureSessionAttachedSessionManager sessionDidReconfigure:]_block_invoke
+ ___65-[FigCaptureSessionAttachedSessionManager sessionDidReconfigure:]_block_invoke.cold.1
+ ___66-[FigCaptureSessionAttachedSessionManager attachToRunningSession:]_block_invoke
+ ___80-[CMCaptureLocalSessionController _stopSessionForMetadataCameraStream:outError:]_block_invoke
+ ___81-[CMCaptureLocalSessionController _startSessionForMetadataCameraStream:outError:]_block_invoke
+ ___85-[CMCaptureLocalSessionController _updateSessionConfigurationForMetadataCameraStream]_block_invoke
+ ___FigCaptureSessionAttachSession_block_invoke
+ ___FigCaptureSessionStartDetachedSession_block_invoke
+ ___FigCaptureSessionStopAttachedSession_block_invoke
+ ___block_descriptor_107_e8_32o40o48o56o64b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8l
+ ___block_descriptor_33_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8l
+ ___block_descriptor_40_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8l
+ ___block_descriptor_40_e8_32o_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8ls32l8
+ ___block_descriptor_40_e8_32r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8lr32l8
+ ___block_descriptor_42_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32o40r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8ls32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8lr32l8
+ ___block_descriptor_50_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40r48r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32o40r48w_e5_v8?0lw48l8s32l8r40l8
+ ___block_descriptor_56_e8_32o40r_e200_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB^{OpaqueFigCaptureSource}}8lr40l8s32l8
+ ___block_literal_global.1270
+ ___block_literal_global.1283
+ ___block_literal_global.1320
+ ___block_literal_global.1323
+ ___block_literal_global.1331
+ ___block_literal_global.1342
+ ___block_literal_global.1352
+ ___block_literal_global.1355
+ ___block_literal_global.1378
+ ___block_literal_global.1380
+ ___block_literal_global.148
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.231
+ ___block_literal_global.456
+ ___block_literal_global.582
+ ___block_literal_global.616
+ ___block_literal_global.635
+ ___block_literal_global.79
+ ___block_literal_global.81
+ ___block_literal_global.898
+ ___block_literal_global.91
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1418
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1416
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1412
+ ___captureSession_SetSectionProperty_block_invoke.1349
+ ___captureSession_commitInflightConfiguration_block_invoke
+ ___captureSession_commitInflightConfiguration_block_invoke.756
+ ___captureSession_commitInflightConfiguration_block_invoke.cold.1
+ ___captureSession_commitInflightConfiguration_block_invoke.cold.2
+ ___captureSession_commitInflightConfiguration_block_invoke.cold.3
+ ___captureSession_detachFromHostSession_block_invoke
+ ___captureSession_detachFromHostSession_block_invoke.cold.1
+ ___captureSession_showCinematicFramingAlertIfApplicable_block_invoke.1254
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1193
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1197
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke.971
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.972
+ ___captureSession_updateGraphConfiguration_block_invoke.776
+ ___captureSession_updateRunningCondition_block_invoke.722
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1301
+ ___captureSourceRegisterWithHostSource_block_invoke
+ ___captureSourceUnregisterWithHostSource_block_invoke
+ ___multiStreamCameraSourceNode_outputSampleBuffer_block_invoke.1515
+ _captureSession_SetSectionProperty.onceToken.1350
+ _captureSource_handleHostCaptureSourceNotification
+ _captureSource_setPropertyInternal.cold.60
+ _captureSource_setPropertyInternal.cold.61
+ _cs_notificationPayloadForAttachingSession
+ _gFigCaptureSessionAttachedSessionManagerTrace
+ _kFigCaptureSampleBufferAttachmentKey_SyntheticReferencePixelBuffer
+ _kFigCaptureSessionDidStopRunningNotificationPayloadKey_ClientStartedSession
+ _kFigCaptureSessionDidStopRunningNotificationPayloadKey_EligibleToAttach
+ _kFigCaptureSourceAttributeKey_MetadataCameraAttachingSupported
+ _kFigCaptureSourceAttributeKey_MetadataCameraHostingSupported
+ _kFigCaptureSourcePropertySetByAttachedSourceKey_AttachedSessionID
+ _kFigCaptureSourcePropertySetByAttachedSourceKey_PropertyKey
+ _kFigCaptureSourcePropertySetByAttachedSourceKey_PropertyValue
+ _kFigCaptureSourceProperty_PropertySetByAttachedSource
+ _kFigCaptureSourceProperty_SecondaryClientTargetFrameRate
+ _objc_msgSend$_copyMetadataOnlySampleBufferFromSampleBuffer:
+ _objc_msgSend$_determineMetadataCameraConfiguration
+ _objc_msgSend$_newMetadataCameraFigCaptureSessionConfiguration
+ _objc_msgSend$_resolveMetadataCameraFigCaptureSessionConfigurationValuesFromLocalSessionConfigurationValues
+ _objc_msgSend$_startSessionForMetadataCameraStream:outError:
+ _objc_msgSend$_stopSessionForMetadataCameraStream:outError:
+ _objc_msgSend$_updateSessionConfigurationForMetadataCameraStream
+ _objc_msgSend$activateExtendedOutput:
+ _objc_msgSend$activateSecureMetadataOutputConfiguration:forAttachedSesssion:
+ _objc_msgSend$addCameraSourcePipeline:sessionID:
+ _objc_msgSend$addExtendedInput
+ _objc_msgSend$addExtendedOutput
+ _objc_msgSend$addMetadataSinkPipeline:sessionID:
+ _objc_msgSend$addNode:
+ _objc_msgSend$attachSessionToHostSession:
+ _objc_msgSend$cameraSourcePipelineCompatibleWithCameraConfiguration:
+ _objc_msgSend$cameraSourcePipelineWithSessionID:
+ _objc_msgSend$cancelLiveExtension:
+ _objc_msgSend$captureSessionInvalidated:
+ _objc_msgSend$coalescedSecureMetadataOutputConfiguration
+ _objc_msgSend$commitLiveExtension:withError:
+ _objc_msgSend$committed
+ _objc_msgSend$createAndBeginLiveExtension
+ _objc_msgSend$deactivateSecureMetadataForAttachedSession:
+ _objc_msgSend$eligibleToAttachToExistingCaptureSession
+ _objc_msgSend$faceTrackingAttributes
+ _objc_msgSend$metadataCameraHostingSupported
+ _objc_msgSend$metadataSinkPipelineWithSessionID:
+ _objc_msgSend$prepareLiveExtensionToBecomeLive:
+ _objc_msgSend$registerAttachedSessionID:
+ _objc_msgSend$removeAllNodes
+ _objc_msgSend$removeCameraSourcePipelineWithSessionID:
+ _objc_msgSend$removeExtendedOutput:
+ _objc_msgSend$removeInput:
+ _objc_msgSend$removeMetadataSinkPipelineWithSessionID:
+ _objc_msgSend$removeOutput:
+ _objc_msgSend$resetAllConfigurations
+ _objc_msgSend$sampleBufferReceiver
+ _objc_msgSend$setCommitted:
+ _objc_msgSend$setConfiguration:forAttachedSessionID:
+ _objc_msgSend$setMaximumFrameRate:attachedSessionID:
+ _objc_msgSend$setMaximumFrameRate:forAttachedSessionID:
+ _objc_msgSend$setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:completionHandler:
+ _objc_msgSend$supportsAttachingSessionConfiguration:
+ _objc_msgSend$unregisterAttachedSessionID:
+ _objc_msgSend$updateMetadataIdentifiers:rectOfInterest:emitsEmptyObjectDetectionMetadata:
- -[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:]
- -[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]
- GCC_except_table122
- GCC_except_table281
- GCC_except_table321
- GCC_except_table328
- GCC_except_table330
- GCC_except_table365
- GCC_except_table366
- GCC_except_table64
- GCC_except_table74
- _.compoundliteral.25
- _.compoundliteral.26
- _.compoundliteral.27
- _.compoundliteral.28
- _.compoundliteral.38
- _.compoundliteral.39
- _.compoundliteral.40
- _.compoundliteral.41
- _.compoundliteral.52
- _.compoundliteral.53
- _.compoundliteral.63
- _.compoundliteral.64
- _.compoundliteral.76
- _.compoundliteral.77
- _.compoundliteral.84
- _.compoundliteral.85
- _.compoundliteral.94
- _CFLocaleCopyCurrent
- _OUTLINED_FUNCTION_377
- ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.103
- ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.107
- ___148-[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke
- ___block_descriptor_106_e8_32o40o48o56o64b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_32_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
- ___block_descriptor_33_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
- ___block_descriptor_40_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
- ___block_descriptor_40_e8_32o_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8ls32l8
- ___block_descriptor_40_e8_32r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8
- ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32o40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8ls32l8r40l8
- ___block_descriptor_48_e8_32r40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8r40l8
- ___block_descriptor_48_e8_32r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8
- ___block_descriptor_56_e8_32o40r48r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32o40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr40l8s32l8
- ___block_literal_global.1253
- ___block_literal_global.1266
- ___block_literal_global.1303
- ___block_literal_global.1306
- ___block_literal_global.1314
- ___block_literal_global.1325
- ___block_literal_global.1335
- ___block_literal_global.1338
- ___block_literal_global.1361
- ___block_literal_global.1363
- ___block_literal_global.137
- ___block_literal_global.227
- ___block_literal_global.449
- ___block_literal_global.552
- ___block_literal_global.631
- ___block_literal_global.656
- ___block_literal_global.75
- ___block_literal_global.80
- ___block_literal_global.885
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1401
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1399
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1395
- ___captureSession_SetSectionProperty_block_invoke.1332
- ___captureSession_showCinematicFramingAlertIfApplicable_block_invoke.1237
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1171
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1175
- ___captureSession_startObservingForAudiomxdDeath_block_invoke.948
- ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.949
- ___captureSession_updateGraphConfiguration_block_invoke.750
- ___captureSession_updateRunningCondition_block_invoke.699
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1284
- ___multiStreamCameraSourceNode_outputSampleBuffer_block_invoke.1513
- _captureSession_SetSectionProperty.onceToken.1333
- _captureSession_shouldUseSceneClassifierToGateMetadataDetection.cold.1
- _figVideoCaptureStream_blackenFrameIfNecessary.cold.1
- _figVideoCaptureStream_blackenFrameIfNecessary.cold.2
- _objc_msgSend$setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:
- _sActiveVideoCaptureSources
CStrings:
+ "%@ Metadata Sink Pipeline"
+ "-[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:completionHandler:]_block_invoke"
+ "-[BWDeferredProcessorController process]"
+ "-[CMCaptureLocalSessionController _newMetadataCameraFigCaptureSessionConfiguration]"
+ "-[CMCaptureLocalSessionController _startSessionForMetadataCameraStream:outError:]_block_invoke"
+ "-[CMCaptureLocalSessionController _stopSessionForMetadataCameraStream:outError:]_block_invoke"
+ "-[CMCaptureLocalSessionController _updateSessionConfigurationForMetadataCameraStream]_block_invoke"
+ "-[CMCaptureLocalSessionOutputStream _copyMetadataOnlySampleBufferFromSampleBuffer:]"
+ "-[FigCaptureSessionAttachedSessionManager _generateStateLog]"
+ "-[FigCaptureSessionAttachedSessionManager _startNextSession]"
+ "-[FigCaptureSessionAttachedSessionManager _stopAttachedSessionsAndRemoveHostSession:]"
+ "-[FigCaptureSessionAttachedSessionManager attachToRunningSession:]_block_invoke"
+ "-[FigCaptureSessionAttachedSessionManager init]"
+ "-[FigCaptureSessionAttachedSessionManager sessionDidReconfigure:]_block_invoke"
+ "-[FigCaptureSessionAttachedSessionManager sessionDidStartRunning:sessionContainsVideoSource:sessionContainsCameraSource:]_block_invoke"
+ "-[FigCaptureSessionAttachedSessionManager sessionDidStopRunning:captureDeviceStolen:sessionIsEligibleToAttach:clientStartedSession:]_block_invoke"
+ "-[FigCaptureSessionAttachedSessionManager sessionInvalidated:]_block_invoke"
+ "23:09:09"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening DepthData frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening FocusPixel frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening RawImage frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening SIFRRawImage frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening SashimiRaw frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening SushiRaw frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Error blackening main sample buffer frame: err:%{public}d (frame:%{public}@)"
+ "<<<< BWStillImageProcessing >>>> %s: Attached synthetic reference %{private}@ for captureID:%{public}lld"
+ "<<<< BWStillImageProcessing >>>> %s: Unable to fetch synthetic reference buffer (err:%d)"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %@ Force metadata camera session %@ start since device is available now"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %@ Force metadata camera session %@ stop since device is unavailable"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ FigCaptureSession for metadata %@ (source %@) error:%d"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Live config metadata session %@"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Metadata Session %@ config %@"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Reconfigure Metadata Session %@"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Restart Metadata Session %@"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Start Metadata Session %@"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ Stop Metadata Camera1 Session"
+ "<<<< CMCaptureLocalSessionOutputStream >>>> %s: Error creating metadata format description, %d"
+ "<<<< CMCaptureLocalSessionOutputStream >>>> %s: Error creating output metadata sample buffer, %d"
+ "<<<< FigCaptureSession >>>> %s: %@"
+ "<<<< FigCaptureSession >>>> %s: Updating graph extensions for sessionID %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s:  %@ cannot attach because there is nothing to attach to."
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Adding stopped session %@ to _sessionsToStart"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Attempting to attach %@ to a host session."
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Clearing currentlyStartingSession %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Currently starting session started, resetting _currentlyStartingSession"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: FigCaptureSessionAttachedSessionManager created."
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: New primary session: %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: New primary session: %@, replaces %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Primary session %@ stopped, resetting primary session"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Received DidReconfigure for %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Received DidStartRunning for %@. sessionContainsVideoSource: %i, sessionContainsCameraSource: %i"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Received DidStopRunning for %@. captureDeviceStolen: %i, sessionIsEligibleToAttach: %i, clientStartedSession: %i"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Removing attached session %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Session %@ attached to host %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Session %@ did not attach to host %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Session %@ incompatible with host %@. Incompatible sessions: %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Session invalidated: %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Starting next session: %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Stopping attached session: %@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: state:\tprimarySession: %@\tattachedSessions: %@\tdetachingSessions: %@\tsessionsToStart: %@\tincompatibleSessions: %@"
+ "@\"BWGraphLiveExtension\""
+ "@\"FigCaptureSessionAttachedSessionManager\""
+ "AttachedClientID"
+ "B24@0:8^{OpaqueFigCaptureSession=}16"
+ "CMCaptureLocalSessionSinkID_MetadataCameraMetadataObject"
+ "Can't begin a new extension when the existing extension hasn't been committed"
+ "Cannot attach because candidate host session configuration does not support our configuration."
+ "Cannot attach because candidate host session is an attached session."
+ "Cannot attach because candidate host session is not running."
+ "EligibleToAttach"
+ "Extension is not currently active, cannot commit"
+ "Extension is not currently active, nothing to cancel"
+ "FaceTrackingFailureFieldOfViewModifier"
+ "FaceTrackingMaxFaces"
+ "FaceTrackingNetworkFailureThresholdMultiplier"
+ "FigCaptureSessionAttachSession_block_invoke"
+ "FigCaptureSessionAttachedSessionManager"
+ "Graph extension has not been committed yet, call commitLiveExtensionWithError."
+ "J817"
+ "J817-J818-J820-J821"
+ "J818"
+ "J820"
+ "J821"
+ "LastShownBuild:BWDeferredProcessorController.m:886"
+ "LastShownBuild:BWDeferredProcessorController.m:930"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3279"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3690"
+ "LastShownBuild:BWNRFProcessorController.m:4545"
+ "LastShownBuild:BWPhotoEncoderController.m:1416"
+ "LastShownBuild:BWPhotoEncoderController.m:1421"
+ "LastShownBuild:BWPhotoEncoderController.m:1648"
+ "LastShownBuild:BWPhotoEncoderController.m:1769"
+ "LastShownBuild:BWPhotoEncoderController.m:1785"
+ "LastShownBuild:BWPhotoEncoderController.m:1795"
+ "LastShownBuild:BWPhotoEncoderController.m:3488"
+ "LastShownBuild:BWPhotoEncoderController.m:4178"
+ "LastShownBuild:BWPhotoEncoderController.m:5540"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2355"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3856"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1411"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:5713"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2734"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2820"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2821"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2993"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2996"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3167"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3170"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3215"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4170"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4176"
+ "LastShownBuild:FigCaptureSession.m:10399"
+ "LastShownBuild:FigCaptureSession.m:10554"
+ "LastShownBuild:FigCaptureSession.m:13649"
+ "LastShownBuild:FigCaptureSession.m:16585"
+ "LastShownBuild:FigCaptureSession.m:18068"
+ "LastShownBuild:FigCaptureSession.m:18071"
+ "LastShownBuild:FigCaptureSession.m:18924"
+ "LastShownBuild:FigCaptureSession.m:22409"
+ "LastShownBuild:FigCaptureSession.m:22444"
+ "LastShownBuild:FigCaptureSession.m:24696"
+ "LastShownBuild:FigCaptureSession.m:4222"
+ "LastShownBuild:FigCaptureSession.m:4782"
+ "LastShownBuild:FigCaptureSession.m:8576"
+ "LastShownBuild:FigCaptureSession.m:8591"
+ "LastShownBuild:FigCaptureSession.m:8605"
+ "LastShownBuild:FigCaptureSession.m:8613"
+ "LastShownBuild:FigCaptureSession.m:8631"
+ "LastShownBuild:FigCaptureSession.m:8676"
+ "LastShownBuild:FigCaptureSession.m:8680"
+ "LastShownBuild:FigCaptureSession.m:8704"
+ "LastShownBuild:FigCaptureSession.m:8719"
+ "LastShownBuild:FigCaptureSession.m:8726"
+ "LastShownBuild:FigCaptureSession.m:8841"
+ "LastShownBuild:FigCaptureSession.m:8847"
+ "LastShownBuild:FigCaptureSession.m:8875"
+ "LastShownBuild:FigCaptureSession.m:8889"
+ "LastShownBuild:FigCaptureSession.m:9305"
+ "LastShownBuild:FigCaptureSession.m:9572"
+ "LastShownDate:BWDeferredProcessorController.m:886"
+ "LastShownDate:BWDeferredProcessorController.m:930"
+ "LastShownDate:BWFigVideoCaptureStream.m:3279"
+ "LastShownDate:BWFigVideoCaptureStream.m:3690"
+ "LastShownDate:BWNRFProcessorController.m:4545"
+ "LastShownDate:BWPhotoEncoderController.m:1416"
+ "LastShownDate:BWPhotoEncoderController.m:1421"
+ "LastShownDate:BWPhotoEncoderController.m:1648"
+ "LastShownDate:BWPhotoEncoderController.m:1769"
+ "LastShownDate:BWPhotoEncoderController.m:1785"
+ "LastShownDate:BWPhotoEncoderController.m:1795"
+ "LastShownDate:BWPhotoEncoderController.m:3488"
+ "LastShownDate:BWPhotoEncoderController.m:4178"
+ "LastShownDate:BWPhotoEncoderController.m:5540"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2355"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3856"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1411"
+ "LastShownDate:FigCaptureMetadataUtilities.m:5713"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2734"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2820"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2821"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2993"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2996"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3167"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3170"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3215"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4170"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4176"
+ "LastShownDate:FigCaptureSession.m:10399"
+ "LastShownDate:FigCaptureSession.m:10554"
+ "LastShownDate:FigCaptureSession.m:13649"
+ "LastShownDate:FigCaptureSession.m:16585"
+ "LastShownDate:FigCaptureSession.m:18068"
+ "LastShownDate:FigCaptureSession.m:18071"
+ "LastShownDate:FigCaptureSession.m:18924"
+ "LastShownDate:FigCaptureSession.m:22409"
+ "LastShownDate:FigCaptureSession.m:22444"
+ "LastShownDate:FigCaptureSession.m:24696"
+ "LastShownDate:FigCaptureSession.m:4222"
+ "LastShownDate:FigCaptureSession.m:4782"
+ "LastShownDate:FigCaptureSession.m:8576"
+ "LastShownDate:FigCaptureSession.m:8591"
+ "LastShownDate:FigCaptureSession.m:8605"
+ "LastShownDate:FigCaptureSession.m:8613"
+ "LastShownDate:FigCaptureSession.m:8631"
+ "LastShownDate:FigCaptureSession.m:8676"
+ "LastShownDate:FigCaptureSession.m:8680"
+ "LastShownDate:FigCaptureSession.m:8704"
+ "LastShownDate:FigCaptureSession.m:8719"
+ "LastShownDate:FigCaptureSession.m:8726"
+ "LastShownDate:FigCaptureSession.m:8841"
+ "LastShownDate:FigCaptureSession.m:8847"
+ "LastShownDate:FigCaptureSession.m:8875"
+ "LastShownDate:FigCaptureSession.m:8889"
+ "LastShownDate:FigCaptureSession.m:9305"
+ "LastShownDate:FigCaptureSession.m:9572"
+ "MetadataCameraAttachingSupported"
+ "MetadataCameraHostingSupported"
+ "Oct 15 2025"
+ "PrimaryClientSession"
+ "PropertySetByAttachedSource"
+ "SecondaryClientTargetFrameRate"
+ "T@\"NSDictionary\",&,N,V_faceTrackingAttributes"
+ "TB,R,N,V_metadataCameraHostingSupported"
+ "_activeLiveExtension"
+ "_activeMetadataCameraFaceTrackingAttributes"
+ "_activeMetadataCameraMetadataIdentifiers"
+ "_attachedSessionManager"
+ "_attachedSessions"
+ "_cameraSourcePipelinesBySessionID"
+ "_changeSeed"
+ "_copyMetadataOnlySampleBufferFromSampleBuffer:"
+ "_currentPrimarySession"
+ "_currentlyStartingSession"
+ "_currentlyStartingSessionChangeSeed"
+ "_detachingSessions"
+ "_determineMetadataCameraConfiguration"
+ "_extendedOutputs"
+ "_extendedOutputsLock"
+ "_faceTrackingAttributes"
+ "_hostingSupported"
+ "_imageQueueNominalFrameRate"
+ "_incompatibleSessions"
+ "_maximumFrameRateByClientID"
+ "_metadataCameraCaptureSession"
+ "_metadataCameraCaptureSessionConfig"
+ "_metadataCameraCaptureSessionRunning"
+ "_metadataCameraCaptureSource"
+ "_metadataCameraCaptureSourceAttributes"
+ "_metadataCameraHostingSupported"
+ "_metadataCameraSinkIDActive"
+ "_metadataConnectionConfigurationBySessionID"
+ "_metadataDeviceFormat"
+ "_metadataFanOutNodeByMetadataCategory"
+ "_metadataOutputsByCategoryForSessionIDAndSourceDeviceType"
+ "_metadataSinkPipelinesBySessionID"
+ "_newMetadataCameraFigCaptureSessionConfiguration"
+ "_registeredAttachedSessionIDs"
+ "_resolveMetadataCameraFigCaptureSessionConfigurationValuesFromLocalSessionConfigurationValues"
+ "_secondaryClientConfigurationsByClientID"
+ "_sessionsToStart"
+ "_startSessionForMetadataCameraStream:outError:"
+ "_stopSessionForMetadataCameraStream:outError:"
+ "_updateSessionConfigurationForMetadataCameraStream"
+ "activateExtendedOutput:"
+ "activateSecureMetadataOutputConfiguration:forAttachedSesssion:"
+ "addCameraSourcePipeline:sessionID:"
+ "addExtendedInput"
+ "addExtendedOutput"
+ "addMetadataSinkPipeline:sessionID:"
+ "attach to existing session"
+ "attachSessionToHostSession:"
+ "attachedSource && hostSource"
+ "beingExtended"
+ "cameraSourcePipelineWithSessionID:"
+ "cancelLiveExtension:"
+ "captureSessionInvalidated:"
+ "capturesessionattachedsessionmanager_trace"
+ "com.apple.coremedia.capturesessionattachedsessionmanager"
+ "commitLiveExtension:withError:"
+ "createAndBeginLiveExtension"
+ "deactivateSecureMetadataForAttachedSession:"
+ "description=CameraCapture-664.42.7.0.1"
+ "eligibleToAttachToExistingCaptureSession"
+ "extensionCommitted"
+ "faceTrackingAttributes"
+ "i16@?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}@q^{__CFString}@i@@@@^{OpaqueFigCaptureSource}f@@@i^{OpaqueFigFlashlight}@iBBB^{OpaqueFigSimpleMutex}@BB^{OpaqueFigCaptureSource}@@}8"
+ "metadataCameraAttachingSupported"
+ "metadataCameraHostingSupported"
+ "metadataCameraSourceAttributes"
+ "metadataSinkPipelineWithSessionID:"
+ "prepareLiveExtensionToBecomeLive:"
+ "registerAttachedSessionID:"
+ "removeCameraSourcePipelineWithSessionID:"
+ "removeExtendedOutput:"
+ "removeMetadataSinkPipelineWithSessionID:"
+ "resetAllConfigurations"
+ "setConfiguration:forAttachedSessionID:"
+ "setFaceTrackingAttributes:"
+ "setMaximumFrameRate:attachedSessionID:"
+ "setMaximumFrameRate:forAttachedSessionID:"
+ "setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:completionHandler:"
+ "storage->attachedSessionIDs.count > 0"
+ "supportsAttachingSessionConfiguration:"
+ "unregisterAttachedSessionID:"
+ "updateMetadataIdentifiers:rectOfInterest:emitsEmptyObjectDetectionMetadata:"
+ "v60@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24B56"
+ "v92@0:8@16B24B28{?=[8I]}32@64@72B80@?84"
- "-[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke"
- "00:25:12"
- "LastShownBuild:BWDeferredProcessorController.m:862"
- "LastShownBuild:BWDeferredProcessorController.m:906"
- "LastShownBuild:BWFigVideoCaptureStream.m:3222"
- "LastShownBuild:BWFigVideoCaptureStream.m:3633"
- "LastShownBuild:BWNRFProcessorController.m:4530"
- "LastShownBuild:BWPhotoEncoderController.m:1409"
- "LastShownBuild:BWPhotoEncoderController.m:1414"
- "LastShownBuild:BWPhotoEncoderController.m:1641"
- "LastShownBuild:BWPhotoEncoderController.m:1762"
- "LastShownBuild:BWPhotoEncoderController.m:1778"
- "LastShownBuild:BWPhotoEncoderController.m:1788"
- "LastShownBuild:BWPhotoEncoderController.m:3476"
- "LastShownBuild:BWPhotoEncoderController.m:4166"
- "LastShownBuild:BWPhotoEncoderController.m:5528"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2360"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3857"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1405"
- "LastShownBuild:FigCaptureMetadataUtilities.m:5707"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2729"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2815"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2816"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2988"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2991"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3162"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3165"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3210"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4165"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4171"
- "LastShownBuild:FigCaptureSession.m:10395"
- "LastShownBuild:FigCaptureSession.m:10550"
- "LastShownBuild:FigCaptureSession.m:13645"
- "LastShownBuild:FigCaptureSession.m:16566"
- "LastShownBuild:FigCaptureSession.m:18049"
- "LastShownBuild:FigCaptureSession.m:18052"
- "LastShownBuild:FigCaptureSession.m:18905"
- "LastShownBuild:FigCaptureSession.m:22390"
- "LastShownBuild:FigCaptureSession.m:22425"
- "LastShownBuild:FigCaptureSession.m:24677"
- "LastShownBuild:FigCaptureSession.m:4220"
- "LastShownBuild:FigCaptureSession.m:4780"
- "LastShownBuild:FigCaptureSession.m:8573"
- "LastShownBuild:FigCaptureSession.m:8579"
- "LastShownBuild:FigCaptureSession.m:8599"
- "LastShownBuild:FigCaptureSession.m:8610"
- "LastShownBuild:FigCaptureSession.m:8628"
- "LastShownBuild:FigCaptureSession.m:8673"
- "LastShownBuild:FigCaptureSession.m:8677"
- "LastShownBuild:FigCaptureSession.m:8701"
- "LastShownBuild:FigCaptureSession.m:8716"
- "LastShownBuild:FigCaptureSession.m:8720"
- "LastShownBuild:FigCaptureSession.m:8838"
- "LastShownBuild:FigCaptureSession.m:8844"
- "LastShownBuild:FigCaptureSession.m:8872"
- "LastShownBuild:FigCaptureSession.m:8886"
- "LastShownBuild:FigCaptureSession.m:9301"
- "LastShownBuild:FigCaptureSession.m:9568"
- "LastShownDate:BWDeferredProcessorController.m:862"
- "LastShownDate:BWDeferredProcessorController.m:906"
- "LastShownDate:BWFigVideoCaptureStream.m:3222"
- "LastShownDate:BWFigVideoCaptureStream.m:3633"
- "LastShownDate:BWNRFProcessorController.m:4530"
- "LastShownDate:BWPhotoEncoderController.m:1409"
- "LastShownDate:BWPhotoEncoderController.m:1414"
- "LastShownDate:BWPhotoEncoderController.m:1641"
- "LastShownDate:BWPhotoEncoderController.m:1762"
- "LastShownDate:BWPhotoEncoderController.m:1778"
- "LastShownDate:BWPhotoEncoderController.m:1788"
- "LastShownDate:BWPhotoEncoderController.m:3476"
- "LastShownDate:BWPhotoEncoderController.m:4166"
- "LastShownDate:BWPhotoEncoderController.m:5528"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2360"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3857"
- "LastShownDate:FigCaptureMetadataUtilities.m:1405"
- "LastShownDate:FigCaptureMetadataUtilities.m:5707"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2729"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2815"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2816"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2988"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2991"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3162"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3165"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3210"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4165"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4171"
- "LastShownDate:FigCaptureSession.m:10395"
- "LastShownDate:FigCaptureSession.m:10550"
- "LastShownDate:FigCaptureSession.m:13645"
- "LastShownDate:FigCaptureSession.m:16566"
- "LastShownDate:FigCaptureSession.m:18049"
- "LastShownDate:FigCaptureSession.m:18052"
- "LastShownDate:FigCaptureSession.m:18905"
- "LastShownDate:FigCaptureSession.m:22390"
- "LastShownDate:FigCaptureSession.m:22425"
- "LastShownDate:FigCaptureSession.m:24677"
- "LastShownDate:FigCaptureSession.m:4220"
- "LastShownDate:FigCaptureSession.m:4780"
- "LastShownDate:FigCaptureSession.m:8573"
- "LastShownDate:FigCaptureSession.m:8579"
- "LastShownDate:FigCaptureSession.m:8599"
- "LastShownDate:FigCaptureSession.m:8610"
- "LastShownDate:FigCaptureSession.m:8628"
- "LastShownDate:FigCaptureSession.m:8673"
- "LastShownDate:FigCaptureSession.m:8677"
- "LastShownDate:FigCaptureSession.m:8701"
- "LastShownDate:FigCaptureSession.m:8716"
- "LastShownDate:FigCaptureSession.m:8720"
- "LastShownDate:FigCaptureSession.m:8838"
- "LastShownDate:FigCaptureSession.m:8844"
- "LastShownDate:FigCaptureSession.m:8872"
- "LastShownDate:FigCaptureSession.m:8886"
- "LastShownDate:FigCaptureSession.m:9301"
- "LastShownDate:FigCaptureSession.m:9568"
- "Oct  6 2025"
- "description=CameraCapture-664.40.18"
- "i16@?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}@q^{__CFString}@i@@@@^{OpaqueFigCaptureSource}f@@@i^{OpaqueFigFlashlight}@iBBB^{OpaqueFigSimpleMutex}@BB}8"
- "setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:"
- "v88@0:8@16B24B28{?=[8I]}32@64@72@?80"

```
