## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0x833a6c
+664.40.15.122.3
+  __TEXT.__text: 0x836760
   __TEXT.__auth_stubs: 0x5430
-  __TEXT.__objc_methlist: 0x340b0
-  __TEXT.__const: 0x1511d0
-  __TEXT.__cstring: 0xe3ca1
-  __TEXT.__oslogstring: 0x139319
+  __TEXT.__objc_methlist: 0x341d0
+  __TEXT.__const: 0x1511e0
+  __TEXT.__cstring: 0xe4174
+  __TEXT.__oslogstring: 0x139b86
   __TEXT.__gcc_except_tab: 0x3cec
   __TEXT.__dlopen_cstrs: 0x6af
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xf440
+  __TEXT.__unwind_info: 0xf478
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x8435
-  __TEXT.__objc_methname: 0xa73b6
-  __TEXT.__objc_methtype: 0x16327
-  __TEXT.__objc_stubs: 0x48a20
-  __DATA_CONST.__got: 0x6908
-  __DATA_CONST.__const: 0xfab0
+  __TEXT.__objc_methname: 0xa79f9
+  __TEXT.__objc_methtype: 0x16334
+  __TEXT.__objc_stubs: 0x48c60
+  __DATA_CONST.__got: 0x6910
+  __DATA_CONST.__const: 0xfab8
   __DATA_CONST.__objc_classlist: 0x1bd0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14b18
+  __DATA_CONST.__objc_selrefs: 0x14bb0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1a30
-  __DATA_CONST.__objc_arraydata: 0x3858
+  __DATA_CONST.__objc_arraydata: 0x3878
   __AUTH_CONST.__auth_got: 0x2a28
   __AUTH_CONST.__const: 0x4700
-  __AUTH_CONST.__cfstring: 0x4fac0
-  __AUTH_CONST.__objc_const: 0x94a40
-  __AUTH_CONST.__objc_intobj: 0x5bc8
-  __AUTH_CONST.__objc_arrayobj: 0x28b0
+  __AUTH_CONST.__cfstring: 0x4fce0
+  __AUTH_CONST.__objc_const: 0x94d40
+  __AUTH_CONST.__objc_intobj: 0x5c10
+  __AUTH_CONST.__objc_arrayobj: 0x2910
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa90
   __AUTH.__objc_data: 0x32f0
-  __DATA.__objc_ivar: 0xa914
+  __DATA.__objc_ivar: 0xa95c
   __DATA.__data: 0x54c0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1ae0
-  __DATA.__bss: 0x2810
+  __DATA.__bss: 0x27f8
   __DATA_DIRTY.__objc_data: 0xe330
   __DATA_DIRTY.__data: 0x1088
-  __DATA_DIRTY.__common: 0xd10
-  __DATA_DIRTY.__bss: 0xc10
+  __DATA_DIRTY.__common: 0xd20
+  __DATA_DIRTY.__bss: 0xc20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 2071A139-6C0D-3D87-8CB7-D55D20004A36
-  Functions: 34071
-  Symbols:   114039
-  CStrings:  69909
+  UUID: BD4CBEC8-FCF6-3783-B674-979D9DDD65DC
+  Functions: 34123
+  Symbols:   114208
+  CStrings:  70009
 
Symbols:
+ -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:]
+ -[BWDeskCamNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:downStreamRequires10BitPixelFormat:]
+ -[BWPhotoEncoderController _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:exifExtraRotationDegrees:]
+ -[BWPhotoEncoderController _newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:exifExtraRotationDegrees:]
+ -[BWPhotoEncoderController legacySensorOrientationRotationDegreesForCapture]
+ -[BWPhotoEncoderControllerConfiguration clientIsCameraOrDerivative]
+ -[BWPhotoEncoderControllerConfiguration setClientIsCameraOrDerivative:]
+ -[BWPhotonicEngineNode _propagatedErrorRecoveryMetadataIfNeededForSampleBuffer:]
+ -[BWPocketDetectionNode didReachEndOfDataForConfigurationID:input:]
+ -[BWPocketDetectionNode hasNonLiveConfigurationChanges]
+ -[BWSmartCropNode _updateDetectedFacesArray:]
+ -[BWStillImageAnalyticsPayloadCommon recoveredFromError]
+ -[BWStillImageAnalyticsPayloadCommon setRecoveredFromError:]
+ -[BWStillImageCaptureMetadata processingError]
+ -[BWStillImageCaptureMetadata proxyProcessingError]
+ -[BWStillImageCaptureMetadata setProcessingError:]
+ -[BWStillImageCaptureMetadata setProxyProcessingError:]
+ -[BWStillImageProcessingSettings optimizedProcessingWithCropAndDownscaleEnabled]
+ -[BWStillImageProcessingSettings setOptimizedProcessingWithCropAndDownscaleEnabled:]
+ -[BWSynchronizerNode _newRetimedVideoSampleBuffer:updatePTSSyncHistory:].cold.5
+ -[BWSynchronizerNode _newRetimedVideoSampleBuffer:updatePTSSyncHistory:].cold.6
+ -[BWSynchronizerNode _newRetimedVideoSampleBuffer:updatePTSSyncHistory:].cold.7
+ -[BWTemporalFilterNode initWithMaxLossyCompression:filterSessionConfiguration:lowLightBandingMitigationEnabled:]
+ -[BWVISProcessorControllerConfiguration faceStabilizationSigmaModulationExponent]
+ -[BWVISProcessorControllerConfiguration faceStabilizationSigmaModulationSmoothTransitionMultiplier]
+ -[BWVISProcessorControllerConfiguration setFaceStabilizationSigmaModulationExponent:]
+ -[BWVISProcessorControllerConfiguration setFaceStabilizationSigmaModulationSmoothTransitionMultiplier:]
+ -[CMCaptureLocalSessionVideoConfiguration setTemporalFilterLowLightBandingMitigationEnabled:]
+ -[CMCaptureLocalSessionVideoConfiguration temporalFilterLowLightBandingMitigationEnabled]
+ -[FigCaptureCameraParameters nrfProcessingDimensionsForOptimizedLearnedFusionForSuperwide]
+ -[FigCaptureCameraParameters softISPCropDimensionsForOptimizedLearnedFusionForSuperwide]
+ -[FigCaptureStillImageSettings orientationMetadataExplicitlySet]
+ -[FigCaptureVideoDataSinkConfiguration setTemporalFilterLowLightBandingMitigationEnabled:]
+ -[FigCaptureVideoDataSinkConfiguration temporalFilterLowLightBandingMitigationEnabled]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setTemporalFilterLowLightBandingMitigationEnabled:]
+ GCC_except_table183
+ GCC_except_table277
+ GCC_except_table307
+ GCC_except_table329
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table374
+ _.compoundliteral.60
+ _.compoundliteral.61
+ _.compoundliteral.63
+ _.compoundliteral.70
+ _.compoundliteral.73
+ _.compoundliteral.74
+ _.compoundliteral.75
+ _.compoundliteral.80
+ _.compoundliteral.87
+ _.compoundliteral.88
+ _BWCameraSensorOrientationCompensationDegreesCWForRequestedSettings
+ _BWDroppedSampleReasonTimeSyncMSGClockNotReady
+ _FigCaptureIsCMClockFromTimeSyncMSGClock
+ _FigCaptureMetadataUtilitiesStillImageExifOrientationFromRotationDegreesAndMirrored
+ _FigCaptureMetadataUtilitiesStillImageExifOrientationFromRotationDegreesAndMirrored.cold.1
+ _FigCaptureNormalizePoint
+ _OBJC_IVAR_$_BWCinematicFramingNode._downstreamRequires10BitPixelFormat
+ _OBJC_IVAR_$_BWDeskCamNode._downstreamRequires10BitPixelFormat
+ _OBJC_IVAR_$_BWFrameRateGovernorNode._invalidFrameCount
+ _OBJC_IVAR_$_BWPhotoEncoderControllerConfiguration._clientIsCameraOrDerivative
+ _OBJC_IVAR_$_BWStillImageAnalyticsPayloadCommon._recoveredFromError
+ _OBJC_IVAR_$_BWStillImageCaptureMetadata._processingError
+ _OBJC_IVAR_$_BWStillImageCaptureMetadata._proxyProcessingError
+ _OBJC_IVAR_$_BWStillImageProcessingSettings._optimizedProcessingWithCropAndDownscaleEnabled
+ _OBJC_IVAR_$_BWSynchronizerNode._maxFramesToDropWhileTimeSyncClockStarts
+ _OBJC_IVAR_$_BWSynchronizerNode._timeSyncMSGClockConversionFailureCount
+ _OBJC_IVAR_$_BWTemporalFilterNode._lowLightBandingMitigationEnabled
+ _OBJC_IVAR_$_BWVISNode._faceStabilizationSigmaModulationExponent
+ _OBJC_IVAR_$_BWVISNode._faceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._faceStabilizationSigmaModulationExponent
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._faceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _OBJC_IVAR_$_CMCaptureLocalSessionVideoConfiguration._temporalFilterLowLightBandingMitigationEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkConfiguration._temporalFilterLowLightBandingMitigationEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._temporalFilterLowLightBandingMitigationEnabled
+ __PromotedConst.265
+ __PromotedConst.266
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.268
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.280
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.284
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.300
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.327
+ ___45-[BWSmartCropNode _updateDetectedFacesArray:]_block_invoke
+ ___66-[BWPhotonicEngineNodeResourceCoordinator liveReconfigureIfNeeded]_block_invoke.262
+ ___67-[BWPocketDetectionNode didReachEndOfDataForConfigurationID:input:]_block_invoke
+ ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.233
+ ___block_literal_global.183
+ ___block_literal_global.297
+ ___block_literal_global.411
+ ___block_literal_global.571
+ ___block_literal_global.594
+ ___block_literal_global.635
+ ___block_literal_global.698
+ ___block_literal_global.727
+ ___block_literal_global.736
+ ___block_literal_global.745
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1344
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1345
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1314
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1318
+ ___captureSession_updateRunningCondition_block_invoke.741
+ _captureSession_clientIsVisualIntelligenceCamera
+ _captureSession_clientIsVisualIntelligenceCamera.cold.1
+ _captureSession_clientIsVisualIntelligenceCamera.cold.2
+ _kFigCaptureStreamMetadata_ProResRawSensorRawValidBufferRect
+ _objc_msgSend$_addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:exifExtraRotationDegrees:
+ _objc_msgSend$_newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:exifExtraRotationDegrees:
+ _objc_msgSend$_updateDetectedFacesArray:
+ _objc_msgSend$faceStabilizationSigmaModulationExponent
+ _objc_msgSend$faceStabilizationSigmaModulationSmoothTransitionMultiplier
+ _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:
+ _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:downStreamRequires10BitPixelFormat:
+ _objc_msgSend$legacySensorOrientationRotationDegreesForCapture
+ _objc_msgSend$nrfProcessingDimensionsForOptimizedLearnedFusionForSuperwide
+ _objc_msgSend$optimizedProcessingWithCropAndDownscaleEnabled
+ _objc_msgSend$orientationMetadataExplicitlySet
+ _objc_msgSend$processingError
+ _objc_msgSend$proxyProcessingError
+ _objc_msgSend$setFaceStabilizationSigmaModulationExponent:
+ _objc_msgSend$setFaceStabilizationSigmaModulationSmoothTransitionMultiplier:
+ _objc_msgSend$setOptimizedProcessingWithCropAndDownscaleEnabled:
+ _objc_msgSend$setProcessingError:
+ _objc_msgSend$setProxyProcessingError:
+ _objc_msgSend$setRecoveredFromError:
+ _objc_msgSend$setTemporalFilterLowLightBandingMitigationEnabled:
+ _objc_msgSend$softISPCropDimensionsForOptimizedLearnedFusionForSuperwide
+ _objc_msgSend$temporalFilterLowLightBandingMitigationEnabled
+ _sfsn_isSlaveFrameProcessingEnabledForMaster
- -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:]
- -[BWDeskCamNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:]
- -[BWPhotoEncoderController _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:]
- -[BWPhotoEncoderController _newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:]
- -[BWPocketDetectionNode didReachEndOfDataForInput:]
- -[BWTemporalFilterNode initWithMaxLossyCompression:filterSessionConfiguration:]
- GCC_except_table162
- GCC_except_table182
- GCC_except_table276
- GCC_except_table328
- GCC_except_table335
- GCC_except_table337
- GCC_except_table372
- GCC_except_table82
- GCC_except_table91
- _.compoundliteral.100
- _.compoundliteral.51
- _.compoundliteral.52
- _.compoundliteral.53
- _.compoundliteral.54
- _.compoundliteral.65
- _.compoundliteral.68
- _.compoundliteral.71
- _.compoundliteral.78
- _.compoundliteral.79
- __PromotedConst.259
- __PromotedConst.260
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.263
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.275
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.279
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.295
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.322
- ___51-[BWPocketDetectionNode didReachEndOfDataForInput:]_block_invoke
- ___66-[BWPhotonicEngineNodeResourceCoordinator liveReconfigureIfNeeded]_block_invoke.259
- ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.228
- ___block_literal_global.182
- ___block_literal_global.408
- ___block_literal_global.440
- ___block_literal_global.570
- ___block_literal_global.593
- ___block_literal_global.634
- ___block_literal_global.697
- ___block_literal_global.731
- ___block_literal_global.740
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1341
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1342
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1311
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1315
- ___captureSession_updateRunningCondition_block_invoke.740
- _captureSession_shouldUseSceneClassifierToGateMetadataDetection.cold.1
- _captureSession_shouldUseSceneClassifierToGateMetadataDetection.cold.2
- _objc_msgSend$_addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:
- _objc_msgSend$_newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:
- _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:
- _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:
CStrings:
+ "-[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:]"
+ "-[BWDeskCamNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:downStreamRequires10BitPixelFormat:]"
+ "-[BWPhotoEncoderController _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:exifExtraRotationDegrees:]"
+ "-[BWPhotoEncoderController _newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:exifExtraRotationDegrees:]"
+ "-[BWPhotonicEngineNode _propagatedErrorRecoveryMetadataIfNeededForSampleBuffer:]"
+ "-[BWPocketDetectionNode didReachEndOfDataForConfigurationID:input:]"
+ "-[BWSmartCropNode _updateDetectedFacesArray:]"
+ "-[BWTemporalFilterNode initWithMaxLossyCompression:filterSessionConfiguration:lowLightBandingMitigationEnabled:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
+ "21:30:10"
+ "<%@ %p> - fmt:%c%c%c%c, w:%d, h:%d, scs:%d, cs:%d, csroi:(%.2f, %.2f, %.2f, %.2f), csfm: %d, mfpx: %.2f, mfpy: %.2f, mfzm: %.2f, tfllbme: %d"
+ "<%@ %p>: idc:%d, demRaw:%d, optForZoomFOV:%d, optFusion:%d clientImageCount:%d, manifest:%@"
+ "<<<< BWFrameRateGovernorNode >>>> %s: True Video %s delayed due to no sensor access (reason: %@)"
+ "<<<< BWFrameRateGovernorNode >>>> %s: [%p] Frame with PTS '%.3f' is invalid due to no sensor access (reason: %@), discarding for True Video %s"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %@[%@]: Clipped validBufferRect %@ to %@ for softISP crop dimensions for optimized learned fusion"
+ "<<<< BWPhotonicEngineNodeUtilities >>>> %s: Preparing for inference processing with intermediateZoomSrcRect:%@, intermediateZoomDstRect:%@, inferenceInputDownscalingFactorMultiplier:%f"
+ "<<<< BWPhotonicEngineNodeUtilities >>>> %s: Updating inference input metadata for intermediate zoom: %@ %@ --> %@ %@"
+ "<<<< BWSlaveFrameSynchronizerNode >>>> %s: Setting _slaveStreamHasStarted to YES, sbufIsMaster: %d, masterInputIndexChanged: %d, slaveFrameProcessingEnabled: %d"
+ "<<<< BWSmartCropNode >>>> %s: Failed to create copy of detectedFacesArray to update"
+ "<<<< BWSmartFramingSceneMonitor >>>> %s: Passed in fieldsOfView is empty"
+ "<<<< BWStillImageProcessing >>>> %s: Creating metadata attachments for captureID:%lld encodingScheme:%@ processingFlags:[%@] exifExtraRotationDegrees:%d photoDescriptor:%@"
+ "<<<< BWStillImageProcessing >>>> %s: minimumValidBufferRectForGDC %{private}@ exceeds optimized processing with crop and downscale rect %{private}@"
+ "<<<< BWStillImageProcessingNode >>>> %s: Missing non-SIFR error recovery frame for replacing '%@' for '%@'"
+ "<<<< BWStillImageProcessingNode >>>> %s: Replacing '%@' of '%f' with '%f' for '%@'"
+ "<<<< BWSynchronizerNode >>>> %s: Dropping frame %d while waiting for TimeSync clock. sourcePTS: {%lld/%d}"
+ "<<<< BWSynchronizerNode >>>> %s: [Pro Video] CMSyncConvertTime failed while running LFD or Genlock"
+ "<<<< BWSynchronizerNode >>>> %s: [Pro Video] TimeSync MSG clock took too long"
+ "<<<< EGStillImageLearnedFusionNRFNode >>>> %s: [%{public}@] callback sent: %d which was handled by the error recovery path"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: ExternalSync enabled"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: ExternalSync went from enabled to disabled"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: LockedFrameDuration enabled"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: LockedFrameDuration went from enabled to disabled"
+ "<<<< FigCaptureSession >>>> %s: Other metadata keys in requested settings: %@"
+ "<<<< FigCaptureSession >>>> %s: The client explicitly requested Exif orientation %d via metadata for the capture"
+ "@172@0:8{?=ii}16@24i32i36B40B44@48i56@60{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff}68B148B152B156Q160B168"
+ "@44@0:8i16^{opaqueCMSampleBuffer=}20@28i36i40"
+ "@80@0:8{?=ii}16@24i32i36B40@44i52@56i64@68B76"
+ "Additional LearnedFusion SoftISP output on-demand allocator (%@, %@)"
+ "CMSyncConvertTime failed to convert time, _sounceClock: %@, _masterClock: %@\n"
+ "HDRProxyGenerationFailed"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10343"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10378"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10567"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10576"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10595"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10622"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10682"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10824"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11696"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:14810"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17446"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1770"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17833"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18469"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18762"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18764"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20353"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21668"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21700"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21839"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22679"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23003"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:5447"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7044"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7055"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7973"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7974"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8196"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8998"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9441"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9892"
+ "LastShownBuild:BWFrameRateGovernorNode.m:275"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:12576"
+ "LastShownBuild:BWNRFProcessorController.m:4530"
+ "LastShownBuild:BWPhotoEncoderController.m:1037"
+ "LastShownBuild:BWPhotoEncoderController.m:1040"
+ "LastShownBuild:BWPhotoEncoderController.m:1409"
+ "LastShownBuild:BWPhotoEncoderController.m:1414"
+ "LastShownBuild:BWPhotoEncoderController.m:1641"
+ "LastShownBuild:BWPhotoEncoderController.m:1762"
+ "LastShownBuild:BWPhotoEncoderController.m:1778"
+ "LastShownBuild:BWPhotoEncoderController.m:1788"
+ "LastShownBuild:BWPhotoEncoderController.m:3476"
+ "LastShownBuild:BWPhotoEncoderController.m:4166"
+ "LastShownBuild:BWPhotoEncoderNode.m:362"
+ "LastShownBuild:BWPhotoEncoderNode.m:364"
+ "LastShownBuild:BWPhotonicEngineNode.m:2603"
+ "LastShownBuild:BWPhotonicEngineNode.m:2606"
+ "LastShownBuild:BWPhotonicEngineNode.m:3291"
+ "LastShownBuild:BWPhotonicEngineNode.m:3306"
+ "LastShownBuild:BWPhotonicEngineNode.m:3417"
+ "LastShownBuild:BWPhotonicEngineNode.m:3441"
+ "LastShownBuild:BWPhotonicEngineNode.m:4479"
+ "LastShownBuild:BWPhotonicEngineNode.m:5175"
+ "LastShownBuild:BWPhotonicEngineNode.m:5193"
+ "LastShownBuild:BWPhotonicEngineNode.m:7129"
+ "LastShownBuild:BWPhotonicEngineNode.m:7131"
+ "LastShownBuild:BWPhotonicEngineNode.m:8576"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3857"
+ "LastShownBuild:BWPhotonicEngineNodeUtilities.m:1240"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1099"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1297"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1304"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1374"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1456"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2036"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3436"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:552"
+ "LastShownBuild:BWSynchronizerNode.m:594"
+ "LastShownBuild:BWSynchronizerNode.m:606"
+ "LastShownBuild:BWSynchronizerNode.m:628"
+ "LastShownBuild:BWVISNode.m:2306"
+ "LastShownBuild:BWVISNode.m:2324"
+ "LastShownBuild:BWVISNode.m:433"
+ "LastShownBuild:CMCaptureLocalSessionController.m:770"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1405"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:5707"
+ "LastShownBuild:FigCaptureSession.m:10395"
+ "LastShownBuild:FigCaptureSession.m:10550"
+ "LastShownBuild:FigCaptureSession.m:11381"
+ "LastShownBuild:FigCaptureSession.m:13645"
+ "LastShownBuild:FigCaptureSession.m:16566"
+ "LastShownBuild:FigCaptureSession.m:18049"
+ "LastShownBuild:FigCaptureSession.m:18052"
+ "LastShownBuild:FigCaptureSession.m:18905"
+ "LastShownBuild:FigCaptureSession.m:22390"
+ "LastShownBuild:FigCaptureSession.m:22425"
+ "LastShownBuild:FigCaptureSession.m:24677"
+ "LastShownBuild:FigCaptureSession.m:4220"
+ "LastShownBuild:FigCaptureSession.m:4780"
+ "LastShownBuild:FigCaptureSession.m:8573"
+ "LastShownBuild:FigCaptureSession.m:8579"
+ "LastShownBuild:FigCaptureSession.m:8582"
+ "LastShownBuild:FigCaptureSession.m:8585"
+ "LastShownBuild:FigCaptureSession.m:8588"
+ "LastShownBuild:FigCaptureSession.m:8599"
+ "LastShownBuild:FigCaptureSession.m:8602"
+ "LastShownBuild:FigCaptureSession.m:8610"
+ "LastShownBuild:FigCaptureSession.m:8628"
+ "LastShownBuild:FigCaptureSession.m:8673"
+ "LastShownBuild:FigCaptureSession.m:8677"
+ "LastShownBuild:FigCaptureSession.m:8701"
+ "LastShownBuild:FigCaptureSession.m:8716"
+ "LastShownBuild:FigCaptureSession.m:8720"
+ "LastShownBuild:FigCaptureSession.m:8723"
+ "LastShownBuild:FigCaptureSession.m:8838"
+ "LastShownBuild:FigCaptureSession.m:8844"
+ "LastShownBuild:FigCaptureSession.m:8872"
+ "LastShownBuild:FigCaptureSession.m:8886"
+ "LastShownBuild:FigCaptureSession.m:9301"
+ "LastShownBuild:FigCaptureSession.m:950"
+ "LastShownBuild:FigCaptureSession.m:9568"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10343"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10378"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10567"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10576"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10595"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10622"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10682"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10824"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11696"
+ "LastShownDate:BWFigVideoCaptureDevice.m:14810"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17446"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1770"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17833"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18469"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18762"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18764"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20353"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21668"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21700"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21839"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22679"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23003"
+ "LastShownDate:BWFigVideoCaptureDevice.m:5447"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7044"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7055"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7973"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7974"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8196"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8998"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9441"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9892"
+ "LastShownDate:BWFrameRateGovernorNode.m:275"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:12576"
+ "LastShownDate:BWNRFProcessorController.m:4530"
+ "LastShownDate:BWPhotoEncoderController.m:1037"
+ "LastShownDate:BWPhotoEncoderController.m:1040"
+ "LastShownDate:BWPhotoEncoderController.m:1409"
+ "LastShownDate:BWPhotoEncoderController.m:1414"
+ "LastShownDate:BWPhotoEncoderController.m:1641"
+ "LastShownDate:BWPhotoEncoderController.m:1762"
+ "LastShownDate:BWPhotoEncoderController.m:1778"
+ "LastShownDate:BWPhotoEncoderController.m:1788"
+ "LastShownDate:BWPhotoEncoderController.m:3476"
+ "LastShownDate:BWPhotoEncoderController.m:4166"
+ "LastShownDate:BWPhotoEncoderNode.m:362"
+ "LastShownDate:BWPhotoEncoderNode.m:364"
+ "LastShownDate:BWPhotonicEngineNode.m:2603"
+ "LastShownDate:BWPhotonicEngineNode.m:2606"
+ "LastShownDate:BWPhotonicEngineNode.m:3291"
+ "LastShownDate:BWPhotonicEngineNode.m:3306"
+ "LastShownDate:BWPhotonicEngineNode.m:3417"
+ "LastShownDate:BWPhotonicEngineNode.m:3441"
+ "LastShownDate:BWPhotonicEngineNode.m:4479"
+ "LastShownDate:BWPhotonicEngineNode.m:5175"
+ "LastShownDate:BWPhotonicEngineNode.m:5193"
+ "LastShownDate:BWPhotonicEngineNode.m:7129"
+ "LastShownDate:BWPhotonicEngineNode.m:7131"
+ "LastShownDate:BWPhotonicEngineNode.m:8576"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3857"
+ "LastShownDate:BWPhotonicEngineNodeUtilities.m:1240"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1099"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1297"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1304"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1374"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1456"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2036"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3436"
+ "LastShownDate:BWStillImageCoordinatorNode.m:552"
+ "LastShownDate:BWSynchronizerNode.m:594"
+ "LastShownDate:BWSynchronizerNode.m:606"
+ "LastShownDate:BWSynchronizerNode.m:628"
+ "LastShownDate:BWVISNode.m:2306"
+ "LastShownDate:BWVISNode.m:2324"
+ "LastShownDate:BWVISNode.m:433"
+ "LastShownDate:CMCaptureLocalSessionController.m:770"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1405"
+ "LastShownDate:FigCaptureMetadataUtilities.m:5707"
+ "LastShownDate:FigCaptureSession.m:10395"
+ "LastShownDate:FigCaptureSession.m:10550"
+ "LastShownDate:FigCaptureSession.m:11381"
+ "LastShownDate:FigCaptureSession.m:13645"
+ "LastShownDate:FigCaptureSession.m:16566"
+ "LastShownDate:FigCaptureSession.m:18049"
+ "LastShownDate:FigCaptureSession.m:18052"
+ "LastShownDate:FigCaptureSession.m:18905"
+ "LastShownDate:FigCaptureSession.m:22390"
+ "LastShownDate:FigCaptureSession.m:22425"
+ "LastShownDate:FigCaptureSession.m:24677"
+ "LastShownDate:FigCaptureSession.m:4220"
+ "LastShownDate:FigCaptureSession.m:4780"
+ "LastShownDate:FigCaptureSession.m:8573"
+ "LastShownDate:FigCaptureSession.m:8579"
+ "LastShownDate:FigCaptureSession.m:8582"
+ "LastShownDate:FigCaptureSession.m:8585"
+ "LastShownDate:FigCaptureSession.m:8588"
+ "LastShownDate:FigCaptureSession.m:8599"
+ "LastShownDate:FigCaptureSession.m:8602"
+ "LastShownDate:FigCaptureSession.m:8610"
+ "LastShownDate:FigCaptureSession.m:8628"
+ "LastShownDate:FigCaptureSession.m:8673"
+ "LastShownDate:FigCaptureSession.m:8677"
+ "LastShownDate:FigCaptureSession.m:8701"
+ "LastShownDate:FigCaptureSession.m:8716"
+ "LastShownDate:FigCaptureSession.m:8720"
+ "LastShownDate:FigCaptureSession.m:8723"
+ "LastShownDate:FigCaptureSession.m:8838"
+ "LastShownDate:FigCaptureSession.m:8844"
+ "LastShownDate:FigCaptureSession.m:8872"
+ "LastShownDate:FigCaptureSession.m:8886"
+ "LastShownDate:FigCaptureSession.m:9301"
+ "LastShownDate:FigCaptureSession.m:950"
+ "LastShownDate:FigCaptureSession.m:9568"
+ "LearnedNRSIFRFailure"
+ "OptimizedFusionProcessing-OnDemand-%@-%@-%@-%@"
+ "OptimizedProcessing-OnDemand-%@-%@-%@-%@"
+ "Sep 29 2025"
+ "TB,N,V_optimizedProcessingWithCropAndDownscaleEnabled"
+ "TB,N,V_temporalFilterLowLightBandingMitigationEnabled"
+ "Tf,N,V_faceStabilizationSigmaModulationExponent"
+ "Tf,N,V_faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "Ti,N,V_processingError"
+ "Ti,N,V_proxyProcessingError"
+ "Ti,N,V_recoveredFromError"
+ "TimeSync clock backed by MSG took too long to create, CMSyncConvertTime is not converting time.\n_sounceClock: %@\n_masterClock: %@\n"
+ "TimeSyncMSGClockNotReady"
+ "True Video %s delayed due to no sensor access (reason: %@)"
+ "[Pro Video] CMSyncConvertTime failed while running LFD or Genlock"
+ "[Pro Video] TimeSync MSG clock took too long"
+ "[smartFramingFieldOfViewRects count] <= 4"
+ "_addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:exifExtraRotationDegrees:"
+ "_downstreamRequires10BitPixelFormat"
+ "_faceStabilizationSigmaModulationExponent"
+ "_faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "_invalidFrameCount"
+ "_lowLightBandingMitigationEnabled"
+ "_maxFramesToDropWhileTimeSyncClockStarts"
+ "_newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:exifExtraRotationDegrees:"
+ "_optimizedProcessingWithCropAndDownscaleEnabled"
+ "_processingError"
+ "_proxyProcessingError"
+ "_recoveredFromError"
+ "_temporalFilterLowLightBandingMitigationEnabled"
+ "_timeSyncMSGClockConversionFailureCount"
+ "_updateDetectedFacesArray:"
+ "description=CameraCapture-664.40.15.122.3"
+ "faceStabilizationSigmaModulationExponent"
+ "faceStabilizationSigmaModulationSmoothTransitionMultiplier"
+ "i52@0:8i16^{opaqueCMSampleBuffer=}20@28i36q40i48"
+ "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:"
+ "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:downStreamRequires10BitPixelFormat:"
+ "legacySensorOrientationRotationDegreesForCapture"
+ "nrfProcessingDimensionsForOptimizedLearnedFusionForSuperwide"
+ "optimizedProcessingWithCropAndDownscaleEnabled"
+ "orientationMetadataExplicitlySet"
+ "preview"
+ "processingError"
+ "proxyProcessingError"
+ "recoveredFromError"
+ "setFaceStabilizationSigmaModulationExponent:"
+ "setFaceStabilizationSigmaModulationSmoothTransitionMultiplier:"
+ "setOptimizedProcessingWithCropAndDownscaleEnabled:"
+ "setProcessingError:"
+ "setProxyProcessingError:"
+ "setRecoveredFromError:"
+ "setTemporalFilterLowLightBandingMitigationEnabled:"
+ "softISPCropDimensionsForOptimizedLearnedFusionForSuperwide"
+ "temporalFilterLowLightBandingMitigationEnabled"
+ "updatedDetectedFacesArray"
- "( [smartFramingFieldOfViewRects count] >= 2 ) && ( [smartFramingFieldOfViewRects count] <= 4 )"
- "-[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:]"
- "-[BWDeskCamNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:]"
- "-[BWPhotoEncoderController _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:]"
- "-[BWPhotoEncoderController _newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:]"
- "-[BWPocketDetectionNode didReachEndOfDataForInput:]"
- "-[BWTemporalFilterNode initWithMaxLossyCompression:filterSessionConfiguration:]"
- "23:22:02"
- "<%@ %p> - fmt:%c%c%c%c, w:%d, h:%d, scs:%d, cs:%d, csroi:(%.2f, %.2f, %.2f, %.2f), csfm: %d, mfpx: %.2f, mfpy: %.2f, mfzm: %.2f"
- "<%@ %p>: idc:%d, demRaw:%d, optForZoomFOV:%d clientImageCount:%d, manifest:%@"
- "<<<< BWPhotonicEngineNodeUtilities >>>> %s: Updating inference input metadata for intermediate zoom: %dx%d %@ --> %dx%d %@"
- "<<<< BWStillImageProcessing >>>> %s: Creating metadata attachments for captureID:%lld processingFlags:[%@] photoDescriptor:%@"
- "<<<< FigCaptureCameraSourcePipeline >>>> %s: ExternalSyncRate does not match (current=%@, new=%@)"
- "<<<< FigCaptureCameraSourcePipeline >>>> %s: LockedFrameRate does not match (current=%@, new=%@)"
- "@168@0:8{?=ii}16@24i32i36B40B44@48i56@60{?=BBB{CGRect={CGPoint=dd}{CGSize=dd}}ifffdfff}68B148B152B156Q160"
- "@40@0:8i16^{opaqueCMSampleBuffer=}20@28i36"
- "@76@0:8{?=ii}16@24i32i36B40@44i52@56i64@68"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10336"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10371"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10560"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10569"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10581"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10615"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10675"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10817"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11689"
- "LastShownBuild:BWFigVideoCaptureDevice.m:14803"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17439"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1763"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17826"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18462"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18755"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18757"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20346"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21661"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21693"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21832"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22672"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22996"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5440"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7037"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7048"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7966"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7967"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8189"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8991"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9434"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9885"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:12575"
- "LastShownBuild:BWNRFProcessorController.m:4478"
- "LastShownBuild:BWPhotoEncoderController.m:1035"
- "LastShownBuild:BWPhotoEncoderController.m:1038"
- "LastShownBuild:BWPhotoEncoderController.m:1407"
- "LastShownBuild:BWPhotoEncoderController.m:1412"
- "LastShownBuild:BWPhotoEncoderController.m:1639"
- "LastShownBuild:BWPhotoEncoderController.m:1760"
- "LastShownBuild:BWPhotoEncoderController.m:1776"
- "LastShownBuild:BWPhotoEncoderController.m:1786"
- "LastShownBuild:BWPhotoEncoderController.m:3477"
- "LastShownBuild:BWPhotoEncoderController.m:4167"
- "LastShownBuild:BWPhotoEncoderNode.m:361"
- "LastShownBuild:BWPhotoEncoderNode.m:363"
- "LastShownBuild:BWPhotonicEngineNode.m:2560"
- "LastShownBuild:BWPhotonicEngineNode.m:2584"
- "LastShownBuild:BWPhotonicEngineNode.m:3263"
- "LastShownBuild:BWPhotonicEngineNode.m:3278"
- "LastShownBuild:BWPhotonicEngineNode.m:3389"
- "LastShownBuild:BWPhotonicEngineNode.m:3413"
- "LastShownBuild:BWPhotonicEngineNode.m:4451"
- "LastShownBuild:BWPhotonicEngineNode.m:5147"
- "LastShownBuild:BWPhotonicEngineNode.m:5165"
- "LastShownBuild:BWPhotonicEngineNode.m:7101"
- "LastShownBuild:BWPhotonicEngineNode.m:7103"
- "LastShownBuild:BWPhotonicEngineNode.m:8548"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3820"
- "LastShownBuild:BWPhotonicEngineNodeUtilities.m:1231"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1096"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1294"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1301"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1371"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1453"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2033"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3427"
- "LastShownBuild:BWStillImageCoordinatorNode.m:549"
- "LastShownBuild:BWSynchronizerNode.m:558"
- "LastShownBuild:BWVISNode.m:2297"
- "LastShownBuild:BWVISNode.m:2315"
- "LastShownBuild:BWVISNode.m:424"
- "LastShownBuild:CMCaptureLocalSessionController.m:764"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1391"
- "LastShownBuild:FigCaptureMetadataUtilities.m:5689"
- "LastShownBuild:FigCaptureSession.m:10379"
- "LastShownBuild:FigCaptureSession.m:10534"
- "LastShownBuild:FigCaptureSession.m:11364"
- "LastShownBuild:FigCaptureSession.m:13628"
- "LastShownBuild:FigCaptureSession.m:16549"
- "LastShownBuild:FigCaptureSession.m:18032"
- "LastShownBuild:FigCaptureSession.m:18035"
- "LastShownBuild:FigCaptureSession.m:18888"
- "LastShownBuild:FigCaptureSession.m:22371"
- "LastShownBuild:FigCaptureSession.m:22406"
- "LastShownBuild:FigCaptureSession.m:24654"
- "LastShownBuild:FigCaptureSession.m:4218"
- "LastShownBuild:FigCaptureSession.m:4778"
- "LastShownBuild:FigCaptureSession.m:8557"
- "LastShownBuild:FigCaptureSession.m:8563"
- "LastShownBuild:FigCaptureSession.m:8566"
- "LastShownBuild:FigCaptureSession.m:8569"
- "LastShownBuild:FigCaptureSession.m:8572"
- "LastShownBuild:FigCaptureSession.m:8583"
- "LastShownBuild:FigCaptureSession.m:8586"
- "LastShownBuild:FigCaptureSession.m:8594"
- "LastShownBuild:FigCaptureSession.m:8612"
- "LastShownBuild:FigCaptureSession.m:8657"
- "LastShownBuild:FigCaptureSession.m:8661"
- "LastShownBuild:FigCaptureSession.m:8685"
- "LastShownBuild:FigCaptureSession.m:8700"
- "LastShownBuild:FigCaptureSession.m:8704"
- "LastShownBuild:FigCaptureSession.m:8707"
- "LastShownBuild:FigCaptureSession.m:8822"
- "LastShownBuild:FigCaptureSession.m:8828"
- "LastShownBuild:FigCaptureSession.m:8856"
- "LastShownBuild:FigCaptureSession.m:8870"
- "LastShownBuild:FigCaptureSession.m:9285"
- "LastShownBuild:FigCaptureSession.m:948"
- "LastShownBuild:FigCaptureSession.m:9552"
- "LastShownDate:BWFigVideoCaptureDevice.m:10336"
- "LastShownDate:BWFigVideoCaptureDevice.m:10371"
- "LastShownDate:BWFigVideoCaptureDevice.m:10560"
- "LastShownDate:BWFigVideoCaptureDevice.m:10569"
- "LastShownDate:BWFigVideoCaptureDevice.m:10581"
- "LastShownDate:BWFigVideoCaptureDevice.m:10615"
- "LastShownDate:BWFigVideoCaptureDevice.m:10675"
- "LastShownDate:BWFigVideoCaptureDevice.m:10817"
- "LastShownDate:BWFigVideoCaptureDevice.m:11689"
- "LastShownDate:BWFigVideoCaptureDevice.m:14803"
- "LastShownDate:BWFigVideoCaptureDevice.m:17439"
- "LastShownDate:BWFigVideoCaptureDevice.m:1763"
- "LastShownDate:BWFigVideoCaptureDevice.m:17826"
- "LastShownDate:BWFigVideoCaptureDevice.m:18462"
- "LastShownDate:BWFigVideoCaptureDevice.m:18755"
- "LastShownDate:BWFigVideoCaptureDevice.m:18757"
- "LastShownDate:BWFigVideoCaptureDevice.m:20346"
- "LastShownDate:BWFigVideoCaptureDevice.m:21661"
- "LastShownDate:BWFigVideoCaptureDevice.m:21693"
- "LastShownDate:BWFigVideoCaptureDevice.m:21832"
- "LastShownDate:BWFigVideoCaptureDevice.m:22672"
- "LastShownDate:BWFigVideoCaptureDevice.m:22996"
- "LastShownDate:BWFigVideoCaptureDevice.m:5440"
- "LastShownDate:BWFigVideoCaptureDevice.m:7037"
- "LastShownDate:BWFigVideoCaptureDevice.m:7048"
- "LastShownDate:BWFigVideoCaptureDevice.m:7966"
- "LastShownDate:BWFigVideoCaptureDevice.m:7967"
- "LastShownDate:BWFigVideoCaptureDevice.m:8189"
- "LastShownDate:BWFigVideoCaptureDevice.m:8991"
- "LastShownDate:BWFigVideoCaptureDevice.m:9434"
- "LastShownDate:BWFigVideoCaptureDevice.m:9885"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:12575"
- "LastShownDate:BWNRFProcessorController.m:4478"
- "LastShownDate:BWPhotoEncoderController.m:1035"
- "LastShownDate:BWPhotoEncoderController.m:1038"
- "LastShownDate:BWPhotoEncoderController.m:1407"
- "LastShownDate:BWPhotoEncoderController.m:1412"
- "LastShownDate:BWPhotoEncoderController.m:1639"
- "LastShownDate:BWPhotoEncoderController.m:1760"
- "LastShownDate:BWPhotoEncoderController.m:1776"
- "LastShownDate:BWPhotoEncoderController.m:1786"
- "LastShownDate:BWPhotoEncoderController.m:3477"
- "LastShownDate:BWPhotoEncoderController.m:4167"
- "LastShownDate:BWPhotoEncoderNode.m:361"
- "LastShownDate:BWPhotoEncoderNode.m:363"
- "LastShownDate:BWPhotonicEngineNode.m:2560"
- "LastShownDate:BWPhotonicEngineNode.m:2584"
- "LastShownDate:BWPhotonicEngineNode.m:3263"
- "LastShownDate:BWPhotonicEngineNode.m:3278"
- "LastShownDate:BWPhotonicEngineNode.m:3389"
- "LastShownDate:BWPhotonicEngineNode.m:3413"
- "LastShownDate:BWPhotonicEngineNode.m:4451"
- "LastShownDate:BWPhotonicEngineNode.m:5147"
- "LastShownDate:BWPhotonicEngineNode.m:5165"
- "LastShownDate:BWPhotonicEngineNode.m:7101"
- "LastShownDate:BWPhotonicEngineNode.m:7103"
- "LastShownDate:BWPhotonicEngineNode.m:8548"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3820"
- "LastShownDate:BWPhotonicEngineNodeUtilities.m:1231"
- "LastShownDate:BWStillImageCoordinatorNode.m:1096"
- "LastShownDate:BWStillImageCoordinatorNode.m:1294"
- "LastShownDate:BWStillImageCoordinatorNode.m:1301"
- "LastShownDate:BWStillImageCoordinatorNode.m:1371"
- "LastShownDate:BWStillImageCoordinatorNode.m:1453"
- "LastShownDate:BWStillImageCoordinatorNode.m:2033"
- "LastShownDate:BWStillImageCoordinatorNode.m:3427"
- "LastShownDate:BWStillImageCoordinatorNode.m:549"
- "LastShownDate:BWSynchronizerNode.m:558"
- "LastShownDate:BWVISNode.m:2297"
- "LastShownDate:BWVISNode.m:2315"
- "LastShownDate:BWVISNode.m:424"
- "LastShownDate:CMCaptureLocalSessionController.m:764"
- "LastShownDate:FigCaptureMetadataUtilities.m:1391"
- "LastShownDate:FigCaptureMetadataUtilities.m:5689"
- "LastShownDate:FigCaptureSession.m:10379"
- "LastShownDate:FigCaptureSession.m:10534"
- "LastShownDate:FigCaptureSession.m:11364"
- "LastShownDate:FigCaptureSession.m:13628"
- "LastShownDate:FigCaptureSession.m:16549"
- "LastShownDate:FigCaptureSession.m:18032"
- "LastShownDate:FigCaptureSession.m:18035"
- "LastShownDate:FigCaptureSession.m:18888"
- "LastShownDate:FigCaptureSession.m:22371"
- "LastShownDate:FigCaptureSession.m:22406"
- "LastShownDate:FigCaptureSession.m:24654"
- "LastShownDate:FigCaptureSession.m:4218"
- "LastShownDate:FigCaptureSession.m:4778"
- "LastShownDate:FigCaptureSession.m:8557"
- "LastShownDate:FigCaptureSession.m:8563"
- "LastShownDate:FigCaptureSession.m:8566"
- "LastShownDate:FigCaptureSession.m:8569"
- "LastShownDate:FigCaptureSession.m:8572"
- "LastShownDate:FigCaptureSession.m:8583"
- "LastShownDate:FigCaptureSession.m:8586"
- "LastShownDate:FigCaptureSession.m:8594"
- "LastShownDate:FigCaptureSession.m:8612"
- "LastShownDate:FigCaptureSession.m:8657"
- "LastShownDate:FigCaptureSession.m:8661"
- "LastShownDate:FigCaptureSession.m:8685"
- "LastShownDate:FigCaptureSession.m:8700"
- "LastShownDate:FigCaptureSession.m:8704"
- "LastShownDate:FigCaptureSession.m:8707"
- "LastShownDate:FigCaptureSession.m:8822"
- "LastShownDate:FigCaptureSession.m:8828"
- "LastShownDate:FigCaptureSession.m:8856"
- "LastShownDate:FigCaptureSession.m:8870"
- "LastShownDate:FigCaptureSession.m:9285"
- "LastShownDate:FigCaptureSession.m:948"
- "LastShownDate:FigCaptureSession.m:9552"
- "LearnedHRSIFRFailure"
- "Sep 16 2025"
- "_addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:"
- "_newMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:"
- "description=CameraCapture-664.40.10.122.3"
- "i48@0:8i16^{opaqueCMSampleBuffer=}20@28i36q40"
- "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:"
- "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portType:overheadCameraMode:captureDevice:"

```
