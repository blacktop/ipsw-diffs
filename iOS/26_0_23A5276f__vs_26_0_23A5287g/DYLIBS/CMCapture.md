## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x7d4e58
-  __TEXT.__auth_stubs: 0x50f0
-  __TEXT.__objc_methlist: 0x324e0
-  __TEXT.__const: 0x1508c0
-  __TEXT.__cstring: 0xdab92
-  __TEXT.__oslogstring: 0x127655
-  __TEXT.__gcc_except_tab: 0x3bfc
+659.0.0.0.4
+  __TEXT.__text: 0x7d6728
+  __TEXT.__auth_stubs: 0x5110
+  __TEXT.__objc_methlist: 0x325b8
+  __TEXT.__const: 0x1508b0
+  __TEXT.__cstring: 0xdaa57
+  __TEXT.__oslogstring: 0x128229
+  __TEXT.__gcc_except_tab: 0x3bc4
   __TEXT.__dlopen_cstrs: 0x6af
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xea30
+  __TEXT.__unwind_info: 0xecb0
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x813d
-  __TEXT.__objc_methname: 0xa08b8
-  __TEXT.__objc_methtype: 0x15574
-  __TEXT.__objc_stubs: 0x45bc0
-  __DATA_CONST.__got: 0x6638
-  __DATA_CONST.__const: 0xee10
-  __DATA_CONST.__objc_classlist: 0x1b38
+  __TEXT.__objc_classname: 0x8164
+  __TEXT.__objc_methname: 0xa0b00
+  __TEXT.__objc_methtype: 0x156a0
+  __TEXT.__objc_stubs: 0x45d00
+  __DATA_CONST.__got: 0x6648
+  __DATA_CONST.__const: 0xede8
+  __DATA_CONST.__objc_classlist: 0x1b40
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x5a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f98
+  __DATA_CONST.__objc_selrefs: 0x13ff8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x19a0
-  __DATA_CONST.__objc_arraydata: 0x36f0
-  __AUTH_CONST.__auth_got: 0x2888
-  __AUTH_CONST.__const: 0x4390
-  __AUTH_CONST.__cfstring: 0x4c7a0
-  __AUTH_CONST.__objc_const: 0x8f978
-  __AUTH_CONST.__objc_intobj: 0x5658
-  __AUTH_CONST.__objc_arrayobj: 0x2760
+  __DATA_CONST.__objc_superrefs: 0x19a8
+  __DATA_CONST.__objc_arraydata: 0x36e0
+  __AUTH_CONST.__auth_got: 0x2898
+  __AUTH_CONST.__const: 0x43b0
+  __AUTH_CONST.__cfstring: 0x4c8c0
+  __AUTH_CONST.__objc_const: 0x8fb48
+  __AUTH_CONST.__objc_intobj: 0x5640
+  __AUTH_CONST.__objc_arrayobj: 0x2748
   __AUTH_CONST.__objc_floatobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa70
-  __AUTH.__objc_data: 0x2cb0
-  __DATA.__objc_ivar: 0xa248
+  __AUTH.__objc_data: 0x2d00
+  __DATA.__objc_ivar: 0xa25c
   __DATA.__data: 0x52f0
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x1920
-  __DATA.__bss: 0x21c8
+  __DATA.__common: 0x1960
+  __DATA.__bss: 0x21d8
   __DATA_DIRTY.__objc_data: 0xe380
   __DATA_DIRTY.__data: 0xf98
   __DATA_DIRTY.__common: 0xd00
-  __DATA_DIRTY.__bss: 0xc00
+  __DATA_DIRTY.__bss: 0xbe0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 40EAA089-919E-3082-9528-1CE76330342E
-  Functions: 32890
-  Symbols:   109980
-  CStrings:  67058
+  UUID: C8081709-2EA5-3310-8405-5DDB13D6FC76
+  Functions: 32933
+  Symbols:   110130
+  CStrings:  67135
 
Symbols:
+ +[BWAudioSourceNode audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:outErr:]
+ +[BWInferenceAttachedMediaCropDescriptor attachedMediaCropDescriptorWithName:attachedMediaKey:cropRectKey:targetDimensions:extendCropRect:]
+ +[BWInferenceAttachedMediaCropDescriptor initialize]
+ -[BWAudioSourceNode _initWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:outErr:]
+ -[BWFigCaptureDeviceVendor streamsControlledByOtherClientsForDevice:]
+ -[BWInferenceAttachedMediaCropDescriptor applicableToSampleBuffer:forMediaKey:]
+ -[BWInferenceAttachedMediaCropDescriptor copyWithZone:]
+ -[BWInferenceAttachedMediaCropDescriptor dealloc]
+ -[BWInferenceAttachedMediaCropDescriptor description]
+ -[BWInferenceAttachedMediaCropDescriptor identifier]
+ -[BWInferenceAttachedMediaCropDescriptor initWithNameAndAttachedMediaKey:attachedMediaKey:cropRectKey:targetDimensions:extendCropRect:]
+ -[BWInferenceAttachedMediaCropDescriptor maxCropForDimensions:]
+ -[BWInferenceAttachedMediaCropDescriptor rectForSampleBuffer:]
+ -[BWInferenceAttachedMediaCropDescriptor rectForSampleBuffer:].cold.1
+ -[BWInferenceEngine preparedWorkloadDescription]
+ -[BWNRFAdaptiveBracketingParameters stopped]
+ -[BWOpticalFlowInferenceConfiguration attachedMediaCropRectKey]
+ -[BWOpticalFlowInferenceConfiguration colorInputCropMode]
+ -[BWOpticalFlowInferenceConfiguration colorInputFlipHorizontal]
+ -[BWOpticalFlowInferenceConfiguration setAttachedMediaCropRectKey:]
+ -[BWOpticalFlowInferenceConfiguration setColorInputCropMode:]
+ -[BWOpticalFlowInferenceConfiguration setColorInputFlipHorizontal:]
+ -[BWPhotonicEngineNode _emitOrEnqueueDisparityReferenceFrameIfNeededForSampleBuffer:]
+ -[BWPreviewStitcherNode _coreImageMetalLibraryURL]
+ -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:]
+ -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:].cold.1
+ -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:].cold.2
+ -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:].cold.3
+ -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:].cold.4
+ -[BWStillImageCaptureStreamSettings currentExpectedAdaptiveBracketedFrameCount]
+ -[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedTimeMachineFrameCountUsingGroup:]
+ -[BWStillImageProcessingSettings cannotProcessDepthPhotos]
+ -[BWStillImageSampleBufferSinkNode .cxx_destruct]
+ -[BWUBAdaptiveBracketingParameters stopped]
+ -[BWUBNRFAdaptiveBracketingParameters stopped]
+ -[CMCaptureLocalSessionVideoConfiguration description]
+ -[FigCaptureMicSourcePipeline _buildMicSourcePipelineWithConfiguration:graph:audioSession:cmSession:isAppAudioSession:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:numberOfCinematicStereoAudioOutputs:numberOfCinematicFOAAudioOutputs:renderDelegate:].cold.12
+ -[FigCaptureMicSourcePipeline _buildMicSourcePipelineWithConfiguration:graph:audioSession:cmSession:isAppAudioSession:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:numberOfCinematicStereoAudioOutputs:numberOfCinematicFOAAudioOutputs:renderDelegate:].cold.13
+ -[FigCaptureMicSourcePipeline initWithConfiguration:graph:name:audioSession:cmSession:isAppAudioSession:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:numberOfCinematicStereoAudioOutputs:numberOfCinematicFOAAudioOutputs:renderDelegate:outErr:]
+ GCC_except_table122
+ GCC_except_table174
+ GCC_except_table186
+ GCC_except_table192
+ GCC_except_table62
+ GCC_except_table74
+ _.compoundliteral.36
+ _.compoundliteral.49
+ _.compoundliteral.52
+ _.compoundliteral.53
+ _.compoundliteral.56
+ _.compoundliteral.57
+ _.compoundliteral.58
+ _.compoundliteral.59
+ _.compoundliteral.60
+ _.compoundliteral.62
+ _.compoundliteral.63
+ _.compoundliteral.64
+ _.compoundliteral.65
+ _.compoundliteral.75
+ _.compoundliteral.78
+ _BWCreateSushiRawDNGDictionary.cold.16
+ _BWIsStillImageSampleBuffer
+ _BWPortTypeIsColorCamera
+ _CMIDenormalizeCropRect
+ _CMINormalizeCropRect
+ _FigCaptureFrontDepthDataToRGBRotationAngle
+ _FigCaptureMetadataUtilitiesExtendRectToAspectRatioOfTargetDimensions
+ _FigCaptureMetadataUtilitiesGetValidBufferRectForProcessedRaw
+ _FigCaptureMetadataUtilitiesGreenGhostDetectedInFrame
+ _FigCaptureMetadataUtilitiesGreenGhostDetectedInMovie
+ _FigCaptureMetadataUtilitiesRectByExtendingRectToAspectRatio
+ _FigCapturePixelFormatHasRegroupedLayoutDownscale
+ _OBJC_CLASS_$_BWInferenceAttachedMediaCropDescriptor
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_IVAR_$_BWBackgroundBlurNode._asyncInitQueue
+ _OBJC_IVAR_$_BWBackgroundBlurNode._asyncProcessingQueue
+ _OBJC_IVAR_$_BWInferenceAttachedMediaCropDescriptor._attachedMediaKey
+ _OBJC_IVAR_$_BWInferenceAttachedMediaCropDescriptor._cropRectKey
+ _OBJC_IVAR_$_BWInferenceAttachedMediaCropDescriptor._extendCropRect
+ _OBJC_IVAR_$_BWInferenceAttachedMediaCropDescriptor._name
+ _OBJC_IVAR_$_BWInferenceAttachedMediaCropDescriptor._targetDimensions
+ _OBJC_IVAR_$_BWInferenceEngine._preparedWorkloadDescription
+ _OBJC_IVAR_$_BWNRFAdaptiveBracketingParameters._stopped
+ _OBJC_IVAR_$_BWOpticalFlowInferenceConfiguration._attachedMediaCropRectKey
+ _OBJC_IVAR_$_BWOpticalFlowInferenceConfiguration._colorInputCropMode
+ _OBJC_IVAR_$_BWOpticalFlowInferenceConfiguration._colorInputFlipHorizontal
+ _OBJC_IVAR_$_BWPreviewStitcherNode._coreImageMetalLibraryURL
+ _OBJC_IVAR_$_BWStillImageSampleBufferSinkNode._frameCoordinatorNode
+ _OBJC_IVAR_$_BWUBAdaptiveBracketingParameters._stopped
+ _OBJC_IVAR_$_BWUBNRFAdaptiveBracketingParameters._stopped
+ _OBJC_IVAR_$_BWVISNode._greenGhostOfflineParameters
+ _OBJC_IVAR_$_BWVISNode._greenGhostStatus
+ _OBJC_METACLASS_$_BWInferenceAttachedMediaCropDescriptor
+ _OUTLINED_FUNCTION_574
+ _OUTLINED_FUNCTION_575
+ __OBJC_$_CLASS_METHODS_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_$_INSTANCE_METHODS_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_$_PROP_LIST_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_CLASS_RO_$_BWInferenceAttachedMediaCropDescriptor
+ __OBJC_METACLASS_RO_$_BWInferenceAttachedMediaCropDescriptor
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.786
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.786.cold.1
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.787
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.796
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.100
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.149
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.726
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.726.cold.1
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.752
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.752.cold.1
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.752.cold.2
+ ___26-[BWAudioSourceNode stop:]_block_invoke.42
+ ___27-[BWAudioSourceNode start:]_block_invoke.36
+ ___27-[BWAudioSourceNode start:]_block_invoke.37
+ ___46-[FigCaptureStillImageSettings initWithCoder:]_block_invoke
+ ___47-[BWPhotonicEngineNode _ubInferenceInputRouter]_block_invoke.884
+ ___58-[BWCompressedShotBufferNode renderSampleBuffer:forInput:]_block_invoke.30
+ ___58-[BWCompressedShotBufferNode renderSampleBuffer:forInput:]_block_invoke.31
+ ___59-[BWStillImageCoordinatorNode renderSampleBuffer:forInput:]_block_invoke.83
+ ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.583
+ ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.586
+ ___66-[BWSmartStyleLearningNode processVideoSampleBuffer:frameEmitted:]_block_invoke.104
+ ___68-[BWFigVideoCaptureDevice _suspendTimeMachineWithCompletionHandler:]_block_invoke.550
+ ___69-[BWFigCaptureDeviceVendor streamsControlledByOtherClientsForDevice:]_block_invoke
+ ___70-[BWSmartStyleLearningNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.81
+ ___73-[BWStillImageCoordinatorNode commitStillImageMomentCaptureWithSettings:]_block_invoke.72
+ ___73-[BWStillImageCoordinatorNode didReachEndOfDataForConfigurationID:input:]_block_invoke.61
+ ___80-[BWFigVideoCaptureDevice _sendInitialValuesToPortraitEffectPropertiesDelegate:]_block_invoke.1054
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.175
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.178
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.181
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.184
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.187
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.190
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.193
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.196
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.199
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.202
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.205
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.208
+ ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.211
+ ___82-[BWBackgroundBlurNode _updateActiveReactions:currentRenderPTS:requestedTriggers:]_block_invoke.66
+ ___82-[BWBackgroundBlurNode _updateActiveReactions:currentRenderPTS:requestedTriggers:]_block_invoke.71
+ ___85-[BWPhotonicEngineNode _emitOrEnqueueDisparityReferenceFrameIfNeededForSampleBuffer:]_block_invoke
+ ___85-[BWPhotonicEngineNode _emitOrEnqueueDisparityReferenceFrameIfNeededForSampleBuffer:]_block_invoke_2
+ ___87-[BWStillImageCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:]_block_invoke.59
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.646
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.646.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.647
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.647.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.647.cold.2
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.638
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.638.cold.1
+ ___94-[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedTimeMachineFrameCountUsingGroup:]_block_invoke
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.689
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.689.cold.1
+ ___block_descriptor_40_e8_32o_e68_"BWInferenceVideoRequirement"36?0i8i12I16"NSString"20"NSArray"28ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_56_e8_32r40w48w_e43_v24?0"SCSensitivityAnalysis"8"NSError"16lr32l8w40l8w48l8
+ ___block_literal_global.1250
+ ___block_literal_global.1279
+ ___block_literal_global.1325
+ ___block_literal_global.1328
+ ___block_literal_global.1351
+ ___block_literal_global.1367
+ ___block_literal_global.1393
+ ___block_literal_global.1405
+ ___block_literal_global.1410
+ ___block_literal_global.1415
+ ___block_literal_global.1458
+ ___block_literal_global.177
+ ___block_literal_global.18
+ ___block_literal_global.180
+ ___block_literal_global.183
+ ___block_literal_global.189
+ ___block_literal_global.192
+ ___block_literal_global.195
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.207
+ ___block_literal_global.210
+ ___block_literal_global.262
+ ___block_literal_global.2793
+ ___block_literal_global.2817
+ ___block_literal_global.305
+ ___block_literal_global.315
+ ___block_literal_global.418
+ ___block_literal_global.576
+ ___block_literal_global.578
+ ___block_literal_global.580
+ ___block_literal_global.582
+ ___block_literal_global.585
+ ___block_literal_global.589
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.619
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.625
+ ___block_literal_global.627
+ ___block_literal_global.629
+ ___block_literal_global.632
+ ___block_literal_global.680
+ ___block_literal_global.685
+ ___block_literal_global.713
+ ___block_literal_global.718
+ ___block_literal_global.720
+ ___block_literal_global.722
+ ___block_literal_global.724
+ ___block_literal_global.726
+ ___block_literal_global.728
+ ___block_literal_global.730
+ ___block_literal_global.733
+ ___block_literal_global.751
+ ___block_literal_global.754
+ ___block_literal_global.756
+ ___block_literal_global.758
+ ___block_literal_global.760
+ ___block_literal_global.762
+ ___block_literal_global.764
+ ___block_literal_global.766
+ ___block_literal_global.768
+ ___block_literal_global.770
+ ___block_literal_global.773
+ ___block_literal_global.812
+ ___block_literal_global.975
+ ___captureSession_Invalidate_block_invoke.1335
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1455
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1453
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1448
+ ___captureSession_IrisStillImageSinkEndMomentCapture_block_invoke.1456
+ ___captureSession_SetConfiguration_block_invoke.1390
+ ___captureSession_SetSectionProperty_block_invoke.1358
+ ___captureSession_SetSectionProperty_block_invoke.1359
+ ___captureSession_SetSectionProperty_block_invoke.1365
+ ___captureSession_startDeferredGraphSetupOnWorkerQueueAfter_block_invoke.1260
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1202
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1203
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1173
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke.944
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.945
+ ___captureSession_updateRunningCondition_block_invoke.713
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1297
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1307
+ ___cmclsc_handleCaptureSessionDidStopRunningNotification_block_invoke
+ ___nrfp_createStateMachine_block_invoke.714
+ ___nrfp_createStateMachine_block_invoke.752
+ ___ubp_createStateMachine_block_invoke.613
+ _captureSession_SetSectionProperty.onceToken.1360
+ _cmclsc_handleCaptureSessionDidStopRunningNotification
+ _gBWInferenceAttachedMediaCropDescriptorTrace
+ _initWithCoder:.onceToken
+ _kFigCaptureSampleBufferAttachmentKey_InputCropRectWithinExtendedCropRect
+ _kFigCaptureStreamTimeMachineSuspendNowKey_AutoResume
+ _multiStreamCameraSourceNode_outputSampleBuffer.cold.12
+ _objc_msgSend$_cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:
+ _objc_msgSend$analyzePixelBuffer:orientation:
+ _objc_msgSend$attachedMediaCropDescriptorWithName:attachedMediaKey:cropRectKey:targetDimensions:extendCropRect:
+ _objc_msgSend$attachedMediaCropRectKey
+ _objc_msgSend$audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:outErr:
+ _objc_msgSend$blitPixelBuffer:inputValidBufferRect:toPixelBuffer:
+ _objc_msgSend$cachedKernelWithFunctionName:fromMetalLibrary:error:
+ _objc_msgSend$colorInputCropMode
+ _objc_msgSend$colorInputFlipHorizontal
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$cropAndScalePixelBuffer:inputValidBufferRect:toPixelBuffer:
+ _objc_msgSend$currentExpectedAdaptiveBracketedFrameCount
+ _objc_msgSend$expectedAdaptiveBracketedTimeMachineFrameCountUsingGroup:
+ _objc_msgSend$newlineCharacterSet
+ _objc_msgSend$preparedWorkloadDescription
+ _objc_msgSend$referenceFrameCandidatesCount
+ _objc_msgSend$setAsyncInitQueue:
+ _objc_msgSend$setAsyncProcessingQueue:
+ _objc_msgSend$setAttachedMediaCropRectKey:
+ _objc_msgSend$setColorInputCropMode:
+ _objc_msgSend$setColorInputFlipHorizontal:
+ _objc_msgSend$setOutColorROI:
+ _objc_msgSend$setReferenceFrameCandidatesCount:
+ _objc_msgSend$stopped
+ _objc_msgSend$undistortPixelBuffer:inputValidBufferRect:inputMetadata:cameraInfo:toPixelBuffer:
+ _psn_attachNormalisedInputCropRectToSampleBuffer
+ _setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:fencePortSendRight:.trueVideoTransitionExitObservedForSignpost
- +[BWAudioSourceNode audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:]
- -[BWAudioSourceNode _audioSessionMXBooleanPropertyIsTrue:]
- -[BWAudioSourceNode _initWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:]
- -[BWCompressedShotBufferNode renderSampleBuffer:forInput:].cold.1
- -[BWCompressedShotBufferNode renderSampleBuffer:forInput:].cold.2
- -[BWOpticalFlowInferenceConfiguration cropColorInputToFinalCropRect]
- -[BWOpticalFlowInferenceConfiguration cropColorInputToPrimaryCaptureRect]
- -[BWOpticalFlowInferenceConfiguration setCropColorInputToFinalCropRect:]
- -[BWOpticalFlowInferenceConfiguration setCropColorInputToPrimaryCaptureRect:]
- -[BWPhotonicEngineNode _emitOrEnqueueFusionReferenceFrameIfNeededForSampleBuffer:]
- -[BWPixelTransferNode setSkipProcessingWhenDepthDisabled:]
- -[BWPixelTransferNode skipProcessingWhenDepthDisabled]
- -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:]
- -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:].cold.1
- -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:].cold.2
- -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:].cold.3
- -[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:].cold.4
- -[BWSmartStyleLearningNode _cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:]
- -[BWSmartStyleLearningNode _cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:].cold.1
- -[BWSmartStyleLearningNode _cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:].cold.2
- -[BWSmartStyleLearningNode _cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:].cold.3
- -[BWSmartStyleLearningNode didSelectFormat:forInput:forAttachedMediaKey:].cold.13
- -[CMCaptureLocalSessionController _registerForFrameReceiveTimeoutNotification:]
- -[FigCaptureMicSourcePipeline initWithConfiguration:graph:name:audioSession:cmSession:isAppAudioSession:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:numberOfCinematicStereoAudioOutputs:numberOfCinematicFOAAudioOutputs:renderDelegate:]
- GCC_except_table119
- GCC_except_table176
- GCC_except_table188
- GCC_except_table52
- _.compoundliteral.34
- _.compoundliteral.35
- _.compoundliteral.38
- _.compoundliteral.72
- _.compoundliteral.73
- _.compoundliteral.81
- _.compoundliteral.84
- _.compoundliteral.85
- _.compoundliteral.86
- _.compoundliteral.87
- _.compoundliteral.88
- _.compoundliteral.89
- _.compoundliteral.90
- _.compoundliteral.91
- _.compoundliteral.94
- _FigCaptureSourceGetPortType
- _FigCapureFrontDepthDataToRGBRotationAngle
- _OBJC_IVAR_$_BWNRFAdaptiveBracketingParameters._stopAdaptiveBracketing
- _OBJC_IVAR_$_BWOpticalFlowInferenceConfiguration._cropColorInputToFinalCropRect
- _OBJC_IVAR_$_BWOpticalFlowInferenceConfiguration._cropColorInputToPrimaryCaptureRect
- _OBJC_IVAR_$_BWPixelTransferNode._skipProcessingWhenDepthDisabled
- _OBJC_IVAR_$_BWSmartStyleLearningNode._networkOutputMaskVideoFormat
- _OBJC_IVAR_$_BWUBAdaptiveBracketingParameters._stopAdaptiveBracketing
- _OBJC_IVAR_$_BWUBNRFAdaptiveBracketingParameters._stopAdaptiveBracketing
- _OBJC_IVAR_$_BWVISNode._detectedGreenGhostFrameCount
- _OBJC_IVAR_$_BWVISNode._greenGhostSampleBufferMetadataDetected
- _OBJC_IVAR_$_BWVISNode._offlineClippedSmall
- _OBJC_IVAR_$_BWVISNode._offlineExposureHigh
- _OBJC_IVAR_$_BWVISNode._offlineLuxLow
- _OBJC_IVAR_$_BWVISNode._offlineLuxSuperLow
- ___101-[BWPreviewStitcherNode _applyBrightnessCompensationToImage:referenceImage:bounds:compensationLevel:]_block_invoke
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.783
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.783.cold.1
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.784
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.793
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.107
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.156
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.723
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.723.cold.1
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749.cold.1
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749.cold.2
- ___26-[BWAudioSourceNode stop:]_block_invoke.36
- ___27-[BWAudioSourceNode start:]_block_invoke.30
- ___27-[BWAudioSourceNode start:]_block_invoke.31
- ___47-[BWPhotonicEngineNode _ubInferenceInputRouter]_block_invoke.881
- ___58-[BWCompressedShotBufferNode renderSampleBuffer:forInput:]_block_invoke_2
- ___58-[BWCompressedShotBufferNode renderSampleBuffer:forInput:]_block_invoke_3
- ___59-[BWStillImageCoordinatorNode renderSampleBuffer:forInput:]_block_invoke.85
- ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.584
- ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.587
- ___66-[BWSmartStyleLearningNode processVideoSampleBuffer:frameEmitted:]_block_invoke.107
- ___68-[BWFigVideoCaptureDevice _suspendTimeMachineWithCompletionHandler:]_block_invoke.551
- ___70-[BWSmartStyleLearningNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.84
- ___73-[BWStillImageCoordinatorNode commitStillImageMomentCaptureWithSettings:]_block_invoke.73
- ___73-[BWStillImageCoordinatorNode didReachEndOfDataForConfigurationID:input:]_block_invoke.62
- ___79-[CMCaptureLocalSessionController _registerForFrameReceiveTimeoutNotification:]_block_invoke
- ___79-[CMCaptureLocalSessionController _registerForFrameReceiveTimeoutNotification:]_block_invoke.104
- ___80-[BWFigVideoCaptureDevice _sendInitialValuesToPortraitEffectPropertiesDelegate:]_block_invoke.1055
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.176
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.179
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.182
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.185
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.188
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.191
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.194
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.197
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.200
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.203
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.206
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.209
- ___80-[BWStillImageCoordinatorNode _setupStateMachineWithAllStateTransitionsHandler:]_block_invoke.212
- ___82-[BWBackgroundBlurNode _updateActiveReactions:currentRenderPTS:requestedTriggers:]_block_invoke.64
- ___82-[BWBackgroundBlurNode _updateActiveReactions:currentRenderPTS:requestedTriggers:]_block_invoke.69
- ___82-[BWPhotonicEngineNode _emitOrEnqueueFusionReferenceFrameIfNeededForSampleBuffer:]_block_invoke
- ___82-[BWPhotonicEngineNode _emitOrEnqueueFusionReferenceFrameIfNeededForSampleBuffer:]_block_invoke_2
- ___87-[BWStillImageCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:]_block_invoke.60
- ___87-[BWStillImageCoordinatorNode configurationWithID:updatedFormat:didBecomeLiveForInput:]_block_invoke.61
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.643
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.643.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644.cold.2
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.635
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.635.cold.1
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.686
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.686.cold.1
- ___FigCaptureSourceGetPortType_block_invoke
- ___block_descriptor_40_e8_32o_e71_"BWInferenceVideoRequirement"40?0i8i12i16I20"NSString"24"NSArray"32ls32l8
- ___block_descriptor_48_e8_32o40w_e24_v16?0"NSNotification"8lw40l8s32l8
- ___block_descriptor_53_e8_32o40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_56_e8_32o40r48w_e43_v24?0"SCSensitivityAnalysis"8"NSError"16lr40l8w48l8s32l8
- ___block_literal_global.1246
- ___block_literal_global.1275
- ___block_literal_global.1321
- ___block_literal_global.1324
- ___block_literal_global.133
- ___block_literal_global.1347
- ___block_literal_global.1359
- ___block_literal_global.1389
- ___block_literal_global.1401
- ___block_literal_global.1406
- ___block_literal_global.1411
- ___block_literal_global.1454
- ___block_literal_global.178
- ___block_literal_global.181
- ___block_literal_global.184
- ___block_literal_global.187
- ___block_literal_global.190
- ___block_literal_global.193
- ___block_literal_global.196
- ___block_literal_global.199
- ___block_literal_global.202
- ___block_literal_global.205
- ___block_literal_global.208
- ___block_literal_global.211
- ___block_literal_global.215
- ___block_literal_global.258
- ___block_literal_global.2794
- ___block_literal_global.2818
- ___block_literal_global.288
- ___block_literal_global.301
- ___block_literal_global.419
- ___block_literal_global.577
- ___block_literal_global.581
- ___block_literal_global.583
- ___block_literal_global.586
- ___block_literal_global.590
- ___block_literal_global.614
- ___block_literal_global.616
- ___block_literal_global.618
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.628
- ___block_literal_global.631
- ___block_literal_global.677
- ___block_literal_global.682
- ___block_literal_global.712
- ___block_literal_global.715
- ___block_literal_global.717
- ___block_literal_global.721
- ___block_literal_global.725
- ___block_literal_global.727
- ___block_literal_global.729
- ___block_literal_global.732
- ___block_literal_global.75
- ___block_literal_global.750
- ___block_literal_global.753
- ___block_literal_global.755
- ___block_literal_global.757
- ___block_literal_global.759
- ___block_literal_global.761
- ___block_literal_global.763
- ___block_literal_global.765
- ___block_literal_global.767
- ___block_literal_global.769
- ___block_literal_global.772
- ___block_literal_global.805
- ___block_literal_global.971
- ___captureSession_Invalidate_block_invoke.1331
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1451
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1449
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1444
- ___captureSession_IrisStillImageSinkEndMomentCapture_block_invoke.1452
- ___captureSession_SetConfiguration_block_invoke.1386
- ___captureSession_SetSectionProperty_block_invoke.1354
- ___captureSession_SetSectionProperty_block_invoke.1355
- ___captureSession_SetSectionProperty_block_invoke.1357
- ___captureSession_startDeferredGraphSetupOnWorkerQueueAfter_block_invoke.1256
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1198
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1199
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1165
- ___captureSession_startObservingForAudiomxdDeath_block_invoke.940
- ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.941
- ___captureSession_updateRunningCondition_block_invoke.707
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1293
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1303
- ___nrfp_createStateMachine_block_invoke.713
- ___nrfp_createStateMachine_block_invoke.751
- ___ubp_createStateMachine_block_invoke.612
- _captureSession_SetSectionProperty.onceToken.1356
- _captureSession_buildGraphWithConfiguration.cold.30
- _kMXSessionProperty_IsActive
- _objc_msgSend$_cropAndScaleMasks:unstyledSampleBuffer:currentPTS:
- _objc_msgSend$_cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:
- _objc_msgSend$_registerForFrameReceiveTimeoutNotification:
- _objc_msgSend$analyzePixelBuffer:
- _objc_msgSend$audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:
- _objc_msgSend$cropAndScale:inputValidBufferRect:toPixelBuffer:
- _objc_msgSend$cropColorInputToFinalCropRect
- _objc_msgSend$expectedAdaptiveBracketedTimeMachineFrameCaptureCountUsingGroup:
- _objc_msgSend$finalCropRectDescriptorWithName:attachedMediaKey:
- _objc_msgSend$initWithInputMediaType:sinkID:
- _objc_msgSend$kernelWithString:
- _objc_msgSend$maximumNumberOfReferenceFrameCandidatesToHoldForProcessing
- _objc_msgSend$setCropColorInputToFinalCropRect:
- _objc_msgSend$setSkipProcessingWhenDepthDisabled:
- _objc_msgSend$undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:
CStrings:
+ "-[BWAudioSourceNode _initWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:outErr:]"
+ "-[BWCameraStreamingMonitor setStreaming:deviceType:maxFrameRate:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]"
+ "-[BWCompressedShotBufferNode renderSampleBuffer:forInput:]_block_invoke"
+ "-[BWFigVideoCaptureStream updateClientAuditToken:]"
+ "-[BWInferenceAttachedMediaCropDescriptor rectForSampleBuffer:]"
+ "-[BWInferenceSharedE5ANEMemoryProvider dealloc]"
+ "-[BWPhotonicEngineNode _attemptDisparityReferenceFrameResolutionForSettings:portType:]"
+ "-[BWPhotonicEngineNode _emitOrEnqueueDisparityReferenceFrameIfNeededForSampleBuffer:]"
+ "-[BWPhotonicEngineNode _emitOrEnqueueDisparityReferenceFrameIfNeededForSampleBuffer:]_block_invoke_2"
+ "-[BWPreviewStitcherNode _applyBrightnessCompensationToImage:referenceImage:bounds:compensationLevel:]"
+ "-[BWPreviewStitcherNode _coreImageMetalLibraryURL]"
+ "-[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
+ "23:28:16"
+ "4c8026313c8deb46069197fa963180c366d4c374"
+ "<%@ %p> - fmt:%c%c%c%c, w:%d, h:%d, scs:%d, cs:%d, csroi:(%.2f, %.2f, %.2f, %.2f), csfm: %d, mfpx: %.2f, mfpy: %.2f, mfzm: %.2f"
+ "<<<< BWAudioSourceNode >>>> %s: Setting kMXSessionProperty_PrefersBluetoothHighQualityContentCapture to %d failed with err: %d"
+ "<<<< BWAudioSourceNode >>>> %s: failed to deactivate audio before setting clientAudioClockDeviceUID. wasActive: %@, res: (%d), err : (%d)"
+ "<<<< BWAudioSourceNode >>>> %s: failed to set audio clock device. err: (%d)"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Camera is in use by %@"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Ignoring streaming %@ for metadata camera %@ from client PID %d"
+ "<<<< BWCameraStreamingMonitor >>>> %s: clientsActiveStreamUniqueIDs removing pid %d"
+ "<<<< BWCompressedShotBufferNode >>>> %s: (captureID:%lld) Emitting a node error: %@"
+ "<<<< BWCompressedShotBufferNode >>>> %s: (captureID:%lld) Failed to produce output sample buffer, will emit a node error"
+ "<<<< BWCompressedShotBufferNode >>>> %s: Failed to compress input sample buffer: %@"
+ "<<<< BWCompressedShotBufferNode >>>> %s: Failed to resolve outputSampleBuffer from inputSampleBuffer: %@ (passthroughInputBuffer:%d)"
+ "<<<< BWDeviceMotionActivityDetector >>>> %s: Unexpected motion data in device motion detection"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Update ClientAuditToken from PID %d to %d with streaming %u"
+ "<<<< BWFigVideoCaptureStream >>>> %s: [%@] Nondisruptive switching format set to %@ with ID:%d, previous %d, minFrameRate %d, maxFrameRate %d, maximumAllowedFrameRate %d, isSecondary %d"
+ "<<<< BWInferenceAttachedMediaCropDescriptor >>>> %s: Crop rectangle not available"
+ "<<<< BWInferenceAttachedMediaCropDescriptor >>>> %s: [%@] Providing %@ %@ from %@ for %@ image size width %zu, height %zu"
+ "<<<< BWInferenceAttachedMediaCropDescriptor >>>> Fig"
+ "<<<< BWInferenceNode >>>> %s: [%@] %@"
+ "<<<< BWInferenceNode >>>> %s: [%@] Releasing all resources -- the node cannot be used after this. Inference workload attempting to be released:"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: Destructing E5RT memory provider with active network dependents: %@"
+ "<<<< BWInferenceSharedResourceManager >>>> %s: %{public}@ took %.2fms"
+ "<<<< BWNRFProcessorController >>>> %s: Error occured while adding error recovery frame. Skipping processing for '%@' (err=%d)"
+ "<<<< BWNRFProcessorController >>>> %s: Error occured while adding frames. Skipping processing for '%@' (err=%d)"
+ "<<<< BWNRFProcessorController >>>> %s: Setting 'referenceFrameCandidatesCount' to '%d' (ZSL:%d)"
+ "<<<< BWPreviewStitcherNode >>>> %s: Failed finding the Metal library for BWPreviewStitcherNode.ci"
+ "<<<< BWPreviewStitcherNode >>>> %s: Failed to load CIColorKernel AdjustGamma with error %@"
+ "<<<< BWPreviewStitcherNode >>>> %s: Failed to load CIColorKernel ComputeGamma with error %@"
+ "<<<< BWPreviewStitcherNode >>>> %s: Failed to load CIColorKernel TwoY with error %@"
+ "<<<< BWSensitiveContentAnalyzerSinkNode >>>> %s: Ignoring analysis changed because self is nil."
+ "<<<< BWSensitiveContentAnalyzerSinkNode >>>> %s: upright orientation %d"
+ "<<<< BWSensitiveContentAnalyzerSinkNode >>>> %s: upright orientation unknown, assuming kFigExifOrientation_0RowTop0ColLeft (%d)"
+ "<<<< BWSmartStyleLearningNode >>>> %s: %@: Dropping sample buffer due to style rendering queue overload %lf, deltaFrameTimeInSeconds=%f"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Could not allocate outputSkyMaskPixelBuffer from the pool"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Could not create sample buffer from finalRefinedHairMaskPixelBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Could not crop scale and undistort mask: %d"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Could not get pixel buffer from outputRefinedHairMaskPixelBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Could not transfer inputSkyMaskPixelBuffer to outputSkyMaskPixelBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Error occured in mask refinement!"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to blit refined masks to output pool"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to copy metadata from inputHairMaskSampleBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to crop and scale mask for %@"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to crop and scale mask: %d"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to crop, scale and undistort masks"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Failed to get pixel buffer pool to crop and scale attached media %@ ( useIntermediatePool : %d )"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Style Learning is ready to learn but learning already in process. Giving some time for queue to clear. Delaying kicking off learning by one frame, deltaFrameTimeInSeconds=%f"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Time until next learning = %f, Ready to learn ? %@"
+ "<<<< BWSmartStyleLearningNode >>>> %s: deltaFrameTimeInSeconds = %f"
+ "<<<< BWStillImageProcessingNode >>>> %s: For port type: %@, received EVZero: %@, EVMinus: %@, unable to successfully spoof SynchronizedStreamsCaptureIDs."
+ "<<<< BWSynchronizerNode >>>> %s: quantization retimed: %lld/%d to %lld/%d"
+ "<<<< CMCaptureLocalSessionController >>>> %s: %{public}@ received DidStopRunning notification for sesison %@, error status %d"
+ "<<<< FigCaptureMicSourcePipeline >>>> %s: audio playing to the built-in speaker but the application does not allow the mic node to change the audio session's cinematic configuration to mono"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Failed to build the mic source pipeline with err(%d), ret(%d)"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Setting previewPipelinesReadyForPropertySetting to NO"
+ "<<<< FigCaptureSession >>>> %s: Detect %u number of graph start fail in a loop within %.3fsec. Last failed to build mic source pipeline (%d)."
+ "<<<< FigRemoteQueue >>>> %s: Registering surface id %d to %{public}s timed out from %s, signalling with %d"
+ "<<<< FigRemoteQueue >>>> %s: Releasing surface id %d to %{public}s timed out from %s (ignored)"
+ "<<<< FigRemoteQueue >>>> %s: mach_msg() returned 0x%x for sending surface id %d to %{public}s, signalling with %d"
+ "<<<< FigRemoteQueue >>>> %s: mach_msg() returned 0x%x while releasing surface id %x to %{public}s (ignored)"
+ "@\"BWInferenceVideoRequirement\"36@?0i8i12I16@\"NSString\"20@\"NSArray\"28"
+ "@\"BWStillImageFrameCoordinatorNode\""
+ "@168@0:8@16@24^{OpaqueCMClock=}32B40B44B48@52B60B64B68B72{?=[8I]}76Q108B116@120@128@136B144B148@152^i160"
+ "@52@0:8@16@24@32{?=ii}40B48"
+ "@64@0:8@16^{opaqueCMSampleBuffer=}24{?=qiIq}32B56B60"
+ "AdjustGamma"
+ "BWInferenceAttachedMediaCropDescriptor"
+ "BWInferenceAttachedMediaCropDescriptor.m"
+ "BWPreviewStitcherNode.ci"
+ "CMGQFrontFacingCameraDeferredPrewarmingDisabled"
+ "CameraCaptureTrueVideoExitAnimationDelay"
+ "ComputeGamma"
+ "Detect %u number of graph start fail in a loop within %.3fsec. Last failed to build mic source pipeline (%d)."
+ "Jun 30 2025"
+ "LastShownBuild:BWAudioSourceNode.m:1146"
+ "LastShownBuild:BWAudioSourceNode.m:482"
+ "LastShownBuild:BWDeviceMotionActivityDetector.m:532"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:2831"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:2882"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3466"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3476"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10165"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10200"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10389"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10398"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10410"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10417"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10444"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10504"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10646"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11518"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:14593"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17224"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1740"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17611"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18252"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18533"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18535"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21434"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21466"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21605"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22440"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22764"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:5285"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7795"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7796"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8018"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8820"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9263"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9714"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1157"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1695"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:730"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:12479"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2475"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3900"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3907"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3914"
+ "LastShownBuild:BWNRFProcessorController.m:1599"
+ "LastShownBuild:BWNRFProcessorController.m:1600"
+ "LastShownBuild:BWNRFProcessorController.m:4451"
+ "LastShownBuild:BWPhotoEncoderController.m:1019"
+ "LastShownBuild:BWPhotoEncoderController.m:1022"
+ "LastShownBuild:BWPhotoEncoderController.m:1386"
+ "LastShownBuild:BWPhotoEncoderController.m:1391"
+ "LastShownBuild:BWPhotoEncoderController.m:1618"
+ "LastShownBuild:BWPhotoEncoderController.m:1739"
+ "LastShownBuild:BWPhotoEncoderController.m:1755"
+ "LastShownBuild:BWPhotoEncoderController.m:3380"
+ "LastShownBuild:BWPhotoEncoderController.m:4062"
+ "LastShownBuild:BWPhotoEncoderController.m:5419"
+ "LastShownBuild:BWPhotonicEngineNode.m:4448"
+ "LastShownBuild:BWPhotonicEngineNode.m:5144"
+ "LastShownBuild:BWPhotonicEngineNode.m:5162"
+ "LastShownBuild:BWPhotonicEngineNode.m:7098"
+ "LastShownBuild:BWPhotonicEngineNode.m:8539"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2360"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3835"
+ "LastShownBuild:BWSensitiveContentAnalyzerSinkNode.m:104"
+ "LastShownBuild:BWSmartStyleRenderingProcessorController.m:815"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2025"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3395"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:462"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:465"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:468"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:471"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:581"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:600"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1000"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1266"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1272"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1290"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1969"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1999"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:771"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:943"
+ "LastShownBuild:BWStillImageScalerNode.m:1096"
+ "LastShownBuild:BWUBNRFProcessorController.m:1353"
+ "LastShownBuild:BWUBNRFProcessorController.m:1354"
+ "LastShownBuild:BWUBProcessorController.m:1151"
+ "LastShownBuild:BWUBProcessorController.m:1152"
+ "LastShownBuild:BWUBProcessorController.m:1153"
+ "LastShownBuild:BWVISNode.m:2275"
+ "LastShownBuild:BWVISNode.m:2293"
+ "LastShownBuild:BWVISNode.m:419"
+ "LastShownBuild:CMCaptureLocalSessionController.m:752"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1288"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:5523"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1439"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1445"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1446"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1450"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1566"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1572"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1736"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2714"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2800"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2801"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2973"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2976"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3147"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3150"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3195"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4107"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4113"
+ "LastShownBuild:FigCaptureSession.m:10727"
+ "LastShownBuild:FigCaptureSession.m:17144"
+ "LastShownBuild:FigCaptureSession.m:17147"
+ "LastShownBuild:FigCaptureSession.m:17981"
+ "LastShownBuild:FigCaptureSession.m:21351"
+ "LastShownBuild:FigCaptureSession.m:21386"
+ "LastShownBuild:FigCaptureSession.m:23580"
+ "LastShownBuild:FigCaptureSession.m:4140"
+ "LastShownBuild:FigCaptureSession.m:8052"
+ "LastShownBuild:FigCaptureSession.m:8058"
+ "LastShownBuild:FigCaptureSession.m:8061"
+ "LastShownBuild:FigCaptureSession.m:8072"
+ "LastShownBuild:FigCaptureSession.m:8075"
+ "LastShownBuild:FigCaptureSession.m:8085"
+ "LastShownBuild:FigCaptureSession.m:8103"
+ "LastShownBuild:FigCaptureSession.m:8117"
+ "LastShownBuild:FigCaptureSession.m:8130"
+ "LastShownBuild:FigCaptureSession.m:8134"
+ "LastShownBuild:FigCaptureSession.m:8137"
+ "LastShownBuild:FigCaptureSession.m:8231"
+ "LastShownBuild:FigCaptureSession.m:8236"
+ "LastShownBuild:FigCaptureSession.m:8244"
+ "LastShownBuild:FigCaptureSession.m:8248"
+ "LastShownBuild:FigCaptureSession.m:8659"
+ "LastShownBuild:FigCaptureSession.m:8926"
+ "LastShownBuild:FigCaptureSession.m:9752"
+ "LastShownBuild:FigCaptureSession.m:9907"
+ "LastShownBuild:FigCaptureSessionObserver.m:614"
+ "LastShownBuild:FigCaptureSourceServer.m:1973"
+ "LastShownBuild:FigRemoteQueue.m:1088"
+ "LastShownDate:BWAudioSourceNode.m:1146"
+ "LastShownDate:BWAudioSourceNode.m:482"
+ "LastShownDate:BWDeviceMotionActivityDetector.m:532"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:2831"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:2882"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3466"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3476"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10165"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10200"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10389"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10398"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10410"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10417"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10444"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10504"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10646"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11518"
+ "LastShownDate:BWFigVideoCaptureDevice.m:14593"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17224"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1740"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17611"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18252"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18533"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18535"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21434"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21466"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21605"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22440"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22764"
+ "LastShownDate:BWFigVideoCaptureDevice.m:5285"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7795"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7796"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8018"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8820"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9263"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9714"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1157"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1695"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:730"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:12479"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2475"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3900"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3907"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3914"
+ "LastShownDate:BWNRFProcessorController.m:1599"
+ "LastShownDate:BWNRFProcessorController.m:1600"
+ "LastShownDate:BWNRFProcessorController.m:4451"
+ "LastShownDate:BWPhotoEncoderController.m:1019"
+ "LastShownDate:BWPhotoEncoderController.m:1022"
+ "LastShownDate:BWPhotoEncoderController.m:1386"
+ "LastShownDate:BWPhotoEncoderController.m:1391"
+ "LastShownDate:BWPhotoEncoderController.m:1618"
+ "LastShownDate:BWPhotoEncoderController.m:1739"
+ "LastShownDate:BWPhotoEncoderController.m:1755"
+ "LastShownDate:BWPhotoEncoderController.m:3380"
+ "LastShownDate:BWPhotoEncoderController.m:4062"
+ "LastShownDate:BWPhotoEncoderController.m:5419"
+ "LastShownDate:BWPhotonicEngineNode.m:4448"
+ "LastShownDate:BWPhotonicEngineNode.m:5144"
+ "LastShownDate:BWPhotonicEngineNode.m:5162"
+ "LastShownDate:BWPhotonicEngineNode.m:7098"
+ "LastShownDate:BWPhotonicEngineNode.m:8539"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2360"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3835"
+ "LastShownDate:BWSensitiveContentAnalyzerSinkNode.m:104"
+ "LastShownDate:BWSmartStyleRenderingProcessorController.m:815"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2025"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3395"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:462"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:465"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:468"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:471"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:581"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:600"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1000"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1266"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1272"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1290"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1969"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1999"
+ "LastShownDate:BWStillImageMetadataUtilities.m:771"
+ "LastShownDate:BWStillImageMetadataUtilities.m:943"
+ "LastShownDate:BWStillImageScalerNode.m:1096"
+ "LastShownDate:BWUBNRFProcessorController.m:1353"
+ "LastShownDate:BWUBNRFProcessorController.m:1354"
+ "LastShownDate:BWUBProcessorController.m:1151"
+ "LastShownDate:BWUBProcessorController.m:1152"
+ "LastShownDate:BWUBProcessorController.m:1153"
+ "LastShownDate:BWVISNode.m:2275"
+ "LastShownDate:BWVISNode.m:2293"
+ "LastShownDate:BWVISNode.m:419"
+ "LastShownDate:CMCaptureLocalSessionController.m:752"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1288"
+ "LastShownDate:FigCaptureMetadataUtilities.m:5523"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1439"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1445"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1446"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1450"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1566"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1572"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1736"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2714"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2800"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2801"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2973"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2976"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3147"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3150"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3195"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4107"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4113"
+ "LastShownDate:FigCaptureSession.m:10727"
+ "LastShownDate:FigCaptureSession.m:17144"
+ "LastShownDate:FigCaptureSession.m:17147"
+ "LastShownDate:FigCaptureSession.m:17981"
+ "LastShownDate:FigCaptureSession.m:21351"
+ "LastShownDate:FigCaptureSession.m:21386"
+ "LastShownDate:FigCaptureSession.m:23580"
+ "LastShownDate:FigCaptureSession.m:4140"
+ "LastShownDate:FigCaptureSession.m:8052"
+ "LastShownDate:FigCaptureSession.m:8058"
+ "LastShownDate:FigCaptureSession.m:8061"
+ "LastShownDate:FigCaptureSession.m:8072"
+ "LastShownDate:FigCaptureSession.m:8075"
+ "LastShownDate:FigCaptureSession.m:8085"
+ "LastShownDate:FigCaptureSession.m:8103"
+ "LastShownDate:FigCaptureSession.m:8117"
+ "LastShownDate:FigCaptureSession.m:8130"
+ "LastShownDate:FigCaptureSession.m:8134"
+ "LastShownDate:FigCaptureSession.m:8137"
+ "LastShownDate:FigCaptureSession.m:8231"
+ "LastShownDate:FigCaptureSession.m:8236"
+ "LastShownDate:FigCaptureSession.m:8244"
+ "LastShownDate:FigCaptureSession.m:8248"
+ "LastShownDate:FigCaptureSession.m:8659"
+ "LastShownDate:FigCaptureSession.m:8926"
+ "LastShownDate:FigCaptureSession.m:9752"
+ "LastShownDate:FigCaptureSession.m:9907"
+ "LastShownDate:FigCaptureSessionObserver.m:614"
+ "LastShownDate:FigCaptureSourceServer.m:1973"
+ "LastShownDate:FigRemoteQueue.m:1088"
+ "Missing attachedMediaCropRectKey"
+ "MovieThresholdInSecond"
+ "Purge Inference Shared Resources"
+ "T@\"NSString\",N,V_attachedMediaCropRectKey"
+ "T@\"NSString\",R,N,V_preparedWorkloadDescription"
+ "TB,N,V_colorInputFlipHorizontal"
+ "Tc,N,V_colorInputCropMode"
+ "TwoY"
+ "Unexpected motion data in device motion detection"
+ "Unknown port type %@"
+ "_asyncInitQueue"
+ "_asyncProcessingQueue"
+ "_attachedMediaCropRectKey"
+ "_colorInputCropMode"
+ "_colorInputFlipHorizontal"
+ "_coreImageMetalLibraryURL"
+ "_cropAndScaleMasks:unstyledSampleBuffer:currentPTS:applyGDC:useIntermediatePool:"
+ "_cropRectKey"
+ "_extendCropRect"
+ "_frameCoordinatorNode"
+ "_greenGhostOfflineParameters"
+ "_greenGhostStatus"
+ "_preparedWorkloadDescription"
+ "_targetDimensions"
+ "analyzePixelBuffer:orientation:"
+ "attachedMediaCropDescriptorWithName:attachedMediaKey:cropRectKey:targetDimensions:extendCropRect:"
+ "attachedMediaCropRectKey"
+ "audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:outErr:"
+ "blitPixelBuffer:inputValidBufferRect:toPixelBuffer:"
+ "bwinferenceattachedmediacropdescriptor_trace"
+ "cachedKernelWithFunctionName:fromMetalLibrary:error:"
+ "cmclsc_handleCaptureSessionDidStopRunningNotification"
+ "cmclsc_handleCaptureSessionDidStopRunningNotification_block_invoke"
+ "colorCropRectDict"
+ "colorInputCropMode"
+ "colorInputFlipHorizontal"
+ "com.apple.bwgraph.backgroundblur.pteffect_init"
+ "com.apple.bwgraph.backgroundblur.pteffect_process"
+ "componentsSeparatedByCharactersInSet:"
+ "cropAndScalePixelBuffer:inputValidBufferRect:toPixelBuffer:"
+ "currentExpectedAdaptiveBracketedFrameCount"
+ "description=CameraCapture-659.0.0.0.4"
+ "expectedAdaptiveBracketedTimeMachineFrameCountUsingGroup:"
+ "f3c6df0ed1237d0ae3b3838a3c7e44324c1d2259"
+ "fac008f625af086ac6557daf39b162a9c9e5432a"
+ "metallib"
+ "micNodeConfiguresAppAudioSession"
+ "newlineCharacterSet"
+ "opticalFlowInferenceConfiguration.attachedMediaCropRectKey"
+ "outputRefinedHairMaskPixelBuffer"
+ "outputSkyMaskPixelBuffer"
+ "preparedWorkloadDescription"
+ "referenceFrameCandidatesCount"
+ "refinedMasks && ( refinedMasks.count == unrefinedMasks.count )"
+ "setAsyncInitQueue:"
+ "setAsyncProcessingQueue:"
+ "setAttachedMediaCropRectKey:"
+ "setColorInputCropMode:"
+ "setColorInputFlipHorizontal:"
+ "setOutColorROI:"
+ "setReferenceFrameCandidatesCount:"
+ "stopped"
+ "streamsControlledByOtherClientsForDevice:"
+ "undistortPixelBuffer:inputValidBufferRect:inputMetadata:cameraInfo:toPixelBuffer:"
+ "v20@0:8c16"
+ "{FigCaptureGreenGhostOfflineParams=\"luxSuperLow\"i\"luxLow\"i\"exposureHigh\"f\"clippedSmall\"i\"movieThresholdInSecond\"f}"
+ "{FigCaptureGreenGhostStatus=\"detectedGreenGhostFrameCount\"i\"greenGhostSampleBufferMetadataDetected\"B}"
- "( ( ! opticalFlowInferenceConfiguration.cropColorInputToFinalCropRect ) || ( ! opticalFlowInferenceConfiguration.cropColorInputToPrimaryCaptureRect ) )"
- "-[BWAudioSourceNode _audioSessionMXBooleanPropertyIsTrue:]"
- "-[BWAudioSourceNode _initWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:]"
- "-[BWPhotonicEngineNode _emitOrEnqueueFusionReferenceFrameIfNeededForSampleBuffer:]"
- "-[BWPhotonicEngineNode _emitOrEnqueueFusionReferenceFrameIfNeededForSampleBuffer:]_block_invoke_2"
- "-[BWSmartStyleLearningNode _cropAndScaleMasks:unstyledSampleBuffer:currentPTS:]"
- "-[BWSmartStyleLearningNode _cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:]"
- "-[CMCaptureLocalSessionController _registerForFrameReceiveTimeoutNotification:]"
- "-[CMCaptureLocalSessionController _registerForFrameReceiveTimeoutNotification:]_block_invoke"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (1)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthSynchronizerNode.m"
- "0b375d5ed4492d4d99ab68a3739d0791bdbe51b3"
- "23:44:01"
- "24995aa5493516159e61853986ebe7769210ed10"
- "<<<< BWAudioSourceNode >>>> %s: Setting kMXSessionProperty_PrefersBluetoothHighQualityContentCapture to true failed with err: %d"
- "<<<< BWAudioSourceNode >>>> %s: _audioSessionBooleanPropertyIsTrue(%@) failed (%@)"
- "<<<< BWFigVideoCaptureStream >>>> %s: [%@] Nondisruptive switching format set to %@ with ID:%d, previous %d, isSecondary %d"
- "<<<< BWInferenceNode >>>> %s: [%@] Releasing all resources -- the node cannot be used after this"
- "<<<< BWNRFProcessorController >>>> %s: Error occured while adding frames. Skipping Deep Fusion processing for '%@' (err=%d)"
- "<<<< BWNRFProcessorController >>>> %s: Setting 'maximumNumberOfReferenceFrameCandidatesToHoldForProcessing' to '%d' (ZSL:%d)"
- "<<<< BWSmartStyleLearningNode >>>> %s: %@: Dropping sample buffer due to style rendering queue overload %lf"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not allocate %@ output pixel buffer from the pool"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not allocate finalSkyMaskPixelBuffer from the pool"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not transfer inputMaskPixelBuffer to outputMaskPixelBuffer for %@"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not transfer inputSkyMaskSampleBuffer to finalSkyMaskPixelBuffer"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not undistort %@ pixel buffer"
- "<<<< BWSmartStyleLearningNode >>>> %s: Could not undistort inputWeightSegmentMapPixelBuffer"
- "<<<< BWSmartStyleLearningNode >>>> %s: Ready to learn ? %@"
- "<<<< BWSmartStyleLearningNode >>>> %s: Style Learning is ready to learn but learning already in process. Giving some time for queue to clear. Delaying kicking off learning by one frame."
- "<<<< BWSmartStyleLearningNode >>>> %s: networkOutputMaskFormatRequirements is nil"
- "<<<< BWSmartStyleLearningNode >>>> %s: pixelBufferPoolTouse is nil"
- "<<<< BWStillImageProcessingNode >>>> %s: For portType: %@, received EVZero: %@, EVMinus: %@, unable to successfully spoof SynchronizedStreamsCaptureIDs."
- "<<<< BWSynchronizerNode >>>> %s: quantization sourceInMasterClockToPreviousDeltaScaleConverted: %lld/%d"
- "<<<< BWVisionInferenceProvider >>>> %s: Vision was sent an invalid face rect for request:(%@) captureID:%lld"
- "<<<< CMCaptureLocalSessionController >>>> %s: %@ frame timeout registration underflow!"
- "<<<< CMCaptureLocalSessionController >>>> %s: Register:%d"
- "<<<< CMCaptureLocalSessionController >>>> %s: isAvailable :%d availabilityChangedReason:%d"
- "<<<< FigCaptureMicSourcePipeline >>>> %s: warning: audio playing to the built-in speaker but the application does not allow the mic node to change the audio session's cinematic configuration to mono"
- "<<<< FigRemoteQueue >>>> %s: Registering surface id %d timed out from %s, signalling with %d"
- "<<<< FigRemoteQueue >>>> %s: Releasing surface id %d timed out"
- "<<<< FigRemoteQueue >>>> %s: mach_msg() returned 0x%x while releasing surface id %x"
- "<<<< FigRemoteQueue >>>> %s: mach_msg() returned 0x%x, signalling with %d"
- "@\"BWInferenceVideoRequirement\"40@?0i8i12i16I20@\"NSString\"24@\"NSArray\"32"
- "@160@0:8@16@24^{OpaqueCMClock=}32B40B44B48@52B60B64B68B72{?=[8I]}76Q108B116@120@128@136B144B148@152"
- "@60@0:8@16^{opaqueCMSampleBuffer=}24{?=qiIq}32B56"
- "Both cropColorInputToPrimaryCaptureRect and cropColorInputToFinalCropRect can NOT be set to YES in the same configuration"
- "Failed to build the mic source pipeline"
- "Jun 18 2025"
- "LastShownBuild:BWAudioSourceNode.m:1018"
- "LastShownBuild:BWAudioSourceNode.m:393"
- "LastShownBuild:BWDepthSynchronizerNode.m:307"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:2817"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:2868"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3452"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3462"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10173"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10208"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10397"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10406"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10418"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10425"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10452"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10512"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10654"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11526"
- "LastShownBuild:BWFigVideoCaptureDevice.m:14601"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17232"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1741"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17619"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18260"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18541"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18543"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21437"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21469"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21608"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22438"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22762"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5286"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7803"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7804"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8026"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8828"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9271"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9722"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1152"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1659"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:725"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:12482"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2474"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3899"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3906"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3913"
- "LastShownBuild:BWNRFProcessorController.m:1588"
- "LastShownBuild:BWNRFProcessorController.m:1589"
- "LastShownBuild:BWNRFProcessorController.m:4425"
- "LastShownBuild:BWPhotoEncoderController.m:1017"
- "LastShownBuild:BWPhotoEncoderController.m:1020"
- "LastShownBuild:BWPhotoEncoderController.m:1384"
- "LastShownBuild:BWPhotoEncoderController.m:1389"
- "LastShownBuild:BWPhotoEncoderController.m:1616"
- "LastShownBuild:BWPhotoEncoderController.m:1737"
- "LastShownBuild:BWPhotoEncoderController.m:1753"
- "LastShownBuild:BWPhotoEncoderController.m:3368"
- "LastShownBuild:BWPhotoEncoderController.m:4050"
- "LastShownBuild:BWPhotoEncoderController.m:5407"
- "LastShownBuild:BWPhotonicEngineNode.m:4446"
- "LastShownBuild:BWPhotonicEngineNode.m:5142"
- "LastShownBuild:BWPhotonicEngineNode.m:5160"
- "LastShownBuild:BWPhotonicEngineNode.m:7094"
- "LastShownBuild:BWPhotonicEngineNode.m:8537"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2359"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3834"
- "LastShownBuild:BWSensitiveContentAnalyzerSinkNode.m:103"
- "LastShownBuild:BWSmartStyleRenderingProcessorController.m:826"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2019"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3389"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:447"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:450"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:453"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:456"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:566"
- "LastShownBuild:BWStillImageFrameCoordinatorNode.m:585"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1246"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1253"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1277"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1956"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1986"
- "LastShownBuild:BWStillImageMetadataUtilities.m:758"
- "LastShownBuild:BWStillImageMetadataUtilities.m:930"
- "LastShownBuild:BWStillImageMetadataUtilities.m:987"
- "LastShownBuild:BWStillImageScalerNode.m:1091"
- "LastShownBuild:BWUBNRFProcessorController.m:1343"
- "LastShownBuild:BWUBNRFProcessorController.m:1344"
- "LastShownBuild:BWUBProcessorController.m:1140"
- "LastShownBuild:BWUBProcessorController.m:1141"
- "LastShownBuild:BWUBProcessorController.m:1142"
- "LastShownBuild:BWVISNode.m:2291"
- "LastShownBuild:BWVISNode.m:2309"
- "LastShownBuild:BWVISNode.m:434"
- "LastShownBuild:BWVisionInferenceProvider.m:433"
- "LastShownBuild:CMCaptureLocalSessionController.m:746"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1287"
- "LastShownBuild:FigCaptureMetadataUtilities.m:5462"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1442"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1448"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1449"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1453"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1569"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1578"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1739"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2716"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2802"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2803"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2975"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2978"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3149"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3152"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3197"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4104"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4110"
- "LastShownBuild:FigCaptureSession.m:10660"
- "LastShownBuild:FigCaptureSession.m:17041"
- "LastShownBuild:FigCaptureSession.m:17874"
- "LastShownBuild:FigCaptureSession.m:21239"
- "LastShownBuild:FigCaptureSession.m:21274"
- "LastShownBuild:FigCaptureSession.m:23468"
- "LastShownBuild:FigCaptureSession.m:4090"
- "LastShownBuild:FigCaptureSession.m:7985"
- "LastShownBuild:FigCaptureSession.m:7991"
- "LastShownBuild:FigCaptureSession.m:7994"
- "LastShownBuild:FigCaptureSession.m:8005"
- "LastShownBuild:FigCaptureSession.m:8008"
- "LastShownBuild:FigCaptureSession.m:8018"
- "LastShownBuild:FigCaptureSession.m:8036"
- "LastShownBuild:FigCaptureSession.m:8050"
- "LastShownBuild:FigCaptureSession.m:8063"
- "LastShownBuild:FigCaptureSession.m:8067"
- "LastShownBuild:FigCaptureSession.m:8070"
- "LastShownBuild:FigCaptureSession.m:8164"
- "LastShownBuild:FigCaptureSession.m:8169"
- "LastShownBuild:FigCaptureSession.m:8177"
- "LastShownBuild:FigCaptureSession.m:8181"
- "LastShownBuild:FigCaptureSession.m:8592"
- "LastShownBuild:FigCaptureSession.m:8859"
- "LastShownBuild:FigCaptureSession.m:9685"
- "LastShownBuild:FigCaptureSession.m:9840"
- "LastShownBuild:FigCaptureSessionObserver.m:609"
- "LastShownBuild:FigCaptureSourceServer.m:1947"
- "LastShownBuild:FigRemoteQueue.m:1079"
- "LastShownDate:BWAudioSourceNode.m:1018"
- "LastShownDate:BWAudioSourceNode.m:393"
- "LastShownDate:BWDepthSynchronizerNode.m:307"
- "LastShownDate:BWFigCaptureDeviceVendor.m:2817"
- "LastShownDate:BWFigCaptureDeviceVendor.m:2868"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3452"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3462"
- "LastShownDate:BWFigVideoCaptureDevice.m:10173"
- "LastShownDate:BWFigVideoCaptureDevice.m:10208"
- "LastShownDate:BWFigVideoCaptureDevice.m:10397"
- "LastShownDate:BWFigVideoCaptureDevice.m:10406"
- "LastShownDate:BWFigVideoCaptureDevice.m:10418"
- "LastShownDate:BWFigVideoCaptureDevice.m:10425"
- "LastShownDate:BWFigVideoCaptureDevice.m:10452"
- "LastShownDate:BWFigVideoCaptureDevice.m:10512"
- "LastShownDate:BWFigVideoCaptureDevice.m:10654"
- "LastShownDate:BWFigVideoCaptureDevice.m:11526"
- "LastShownDate:BWFigVideoCaptureDevice.m:14601"
- "LastShownDate:BWFigVideoCaptureDevice.m:17232"
- "LastShownDate:BWFigVideoCaptureDevice.m:1741"
- "LastShownDate:BWFigVideoCaptureDevice.m:17619"
- "LastShownDate:BWFigVideoCaptureDevice.m:18260"
- "LastShownDate:BWFigVideoCaptureDevice.m:18541"
- "LastShownDate:BWFigVideoCaptureDevice.m:18543"
- "LastShownDate:BWFigVideoCaptureDevice.m:21437"
- "LastShownDate:BWFigVideoCaptureDevice.m:21469"
- "LastShownDate:BWFigVideoCaptureDevice.m:21608"
- "LastShownDate:BWFigVideoCaptureDevice.m:22438"
- "LastShownDate:BWFigVideoCaptureDevice.m:22762"
- "LastShownDate:BWFigVideoCaptureDevice.m:5286"
- "LastShownDate:BWFigVideoCaptureDevice.m:7803"
- "LastShownDate:BWFigVideoCaptureDevice.m:7804"
- "LastShownDate:BWFigVideoCaptureDevice.m:8026"
- "LastShownDate:BWFigVideoCaptureDevice.m:8828"
- "LastShownDate:BWFigVideoCaptureDevice.m:9271"
- "LastShownDate:BWFigVideoCaptureDevice.m:9722"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1152"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1659"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:725"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:12482"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2474"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3899"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3906"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3913"
- "LastShownDate:BWNRFProcessorController.m:1588"
- "LastShownDate:BWNRFProcessorController.m:1589"
- "LastShownDate:BWNRFProcessorController.m:4425"
- "LastShownDate:BWPhotoEncoderController.m:1017"
- "LastShownDate:BWPhotoEncoderController.m:1020"
- "LastShownDate:BWPhotoEncoderController.m:1384"
- "LastShownDate:BWPhotoEncoderController.m:1389"
- "LastShownDate:BWPhotoEncoderController.m:1616"
- "LastShownDate:BWPhotoEncoderController.m:1737"
- "LastShownDate:BWPhotoEncoderController.m:1753"
- "LastShownDate:BWPhotoEncoderController.m:3368"
- "LastShownDate:BWPhotoEncoderController.m:4050"
- "LastShownDate:BWPhotoEncoderController.m:5407"
- "LastShownDate:BWPhotonicEngineNode.m:4446"
- "LastShownDate:BWPhotonicEngineNode.m:5142"
- "LastShownDate:BWPhotonicEngineNode.m:5160"
- "LastShownDate:BWPhotonicEngineNode.m:7094"
- "LastShownDate:BWPhotonicEngineNode.m:8537"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2359"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3834"
- "LastShownDate:BWSensitiveContentAnalyzerSinkNode.m:103"
- "LastShownDate:BWSmartStyleRenderingProcessorController.m:826"
- "LastShownDate:BWStillImageCoordinatorNode.m:2019"
- "LastShownDate:BWStillImageCoordinatorNode.m:3389"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:447"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:450"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:453"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:456"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:566"
- "LastShownDate:BWStillImageFrameCoordinatorNode.m:585"
- "LastShownDate:BWStillImageMetadataUtilities.m:1246"
- "LastShownDate:BWStillImageMetadataUtilities.m:1253"
- "LastShownDate:BWStillImageMetadataUtilities.m:1277"
- "LastShownDate:BWStillImageMetadataUtilities.m:1956"
- "LastShownDate:BWStillImageMetadataUtilities.m:1986"
- "LastShownDate:BWStillImageMetadataUtilities.m:758"
- "LastShownDate:BWStillImageMetadataUtilities.m:930"
- "LastShownDate:BWStillImageMetadataUtilities.m:987"
- "LastShownDate:BWStillImageScalerNode.m:1091"
- "LastShownDate:BWUBNRFProcessorController.m:1343"
- "LastShownDate:BWUBNRFProcessorController.m:1344"
- "LastShownDate:BWUBProcessorController.m:1140"
- "LastShownDate:BWUBProcessorController.m:1141"
- "LastShownDate:BWUBProcessorController.m:1142"
- "LastShownDate:BWVISNode.m:2291"
- "LastShownDate:BWVISNode.m:2309"
- "LastShownDate:BWVISNode.m:434"
- "LastShownDate:BWVisionInferenceProvider.m:433"
- "LastShownDate:CMCaptureLocalSessionController.m:746"
- "LastShownDate:FigCaptureMetadataUtilities.m:1287"
- "LastShownDate:FigCaptureMetadataUtilities.m:5462"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1442"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1448"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1449"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1453"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1569"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1578"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1739"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2716"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2802"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2803"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2975"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2978"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3149"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3152"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3197"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4104"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4110"
- "LastShownDate:FigCaptureSession.m:10660"
- "LastShownDate:FigCaptureSession.m:17041"
- "LastShownDate:FigCaptureSession.m:17874"
- "LastShownDate:FigCaptureSession.m:21239"
- "LastShownDate:FigCaptureSession.m:21274"
- "LastShownDate:FigCaptureSession.m:23468"
- "LastShownDate:FigCaptureSession.m:4090"
- "LastShownDate:FigCaptureSession.m:7985"
- "LastShownDate:FigCaptureSession.m:7991"
- "LastShownDate:FigCaptureSession.m:7994"
- "LastShownDate:FigCaptureSession.m:8005"
- "LastShownDate:FigCaptureSession.m:8008"
- "LastShownDate:FigCaptureSession.m:8018"
- "LastShownDate:FigCaptureSession.m:8036"
- "LastShownDate:FigCaptureSession.m:8050"
- "LastShownDate:FigCaptureSession.m:8063"
- "LastShownDate:FigCaptureSession.m:8067"
- "LastShownDate:FigCaptureSession.m:8070"
- "LastShownDate:FigCaptureSession.m:8164"
- "LastShownDate:FigCaptureSession.m:8169"
- "LastShownDate:FigCaptureSession.m:8177"
- "LastShownDate:FigCaptureSession.m:8181"
- "LastShownDate:FigCaptureSession.m:8592"
- "LastShownDate:FigCaptureSession.m:8859"
- "LastShownDate:FigCaptureSession.m:9685"
- "LastShownDate:FigCaptureSession.m:9840"
- "LastShownDate:FigCaptureSessionObserver.m:609"
- "LastShownDate:FigCaptureSourceServer.m:1947"
- "LastShownDate:FigRemoteQueue.m:1079"
- "Refined masks not present!"
- "TB,N,V_cropColorInputToFinalCropRect"
- "Unable to get input sky mask sample buffer timing info"
- "Vision was sent an invalid face rect for request:(%@) captureID:%lld"
- "[%@] Received an out of order frame with CID:%d (PTS:%0.3f) after %d (PTS:%0.3f) from %@. Dropping the out of order buffer."
- "_cropAndScaleMasks:unstyledSampleBuffer:currentPTS:"
- "_cropAndUndistortMasks:unstyledSampleBuffer:currentPTS:useIntermediatePools:"
- "_cropColorInputToFinalCropRect"
- "_detectedGreenGhostFrameCount"
- "_networkOutputMaskVideoFormat"
- "_offlineClippedSmall"
- "_offlineExposureHigh"
- "_offlineLuxLow"
- "_offlineLuxSuperLow"
- "_registerForFrameReceiveTimeoutNotification:"
- "_skipProcessingWhenDepthDisabled"
- "_stopAdaptiveBracketing"
- "analyzePixelBuffer:"
- "audioSourceNodeWithAttributes:sessionPreset:clock:doConfigureAudio:doMixWithOthers:doAllowHQBluetoothRecording:audioSession:isAppAudioSession:doEndInterruption:audioSessionIsProxy:audioIsPlayingToBuiltinSpeaker:clientAuditToken:clientSDKVersionToken:clientOSVersionSupportsDecoupledIO:clientAudioClockDeviceUID:preferredIOBufferDuration:audioCaptureConnectionConfigurations:isConfiguredForContinuityCapture:isAudioOnlyRecordingSession:remoteIOOutputFormat:"
- "cropAndScale:inputValidBufferRect:toPixelBuffer:"
- "cropColorInputToFinalCropRect"
- "description=CameraCapture-655.0.0.122.4"
- "ed6240ee295d09fa1ebcb64acd38b914cbb5013c"
- "finalMaskPixelBuffer"
- "finalSkyMaskPixelBuffer"
- "initWithInputMediaType:sinkID:"
- "kernel vec4 AdjustGamma ( __sample a, __sample gamma, float adjPerc ) { \n   float adjGamma = 1.0 + ( gamma.x - 1.0 ) * adjPerc; \n   a.rgb = sign( a.rgb ) * pow( abs( a.rgb ), vec3( adjGamma ) ); \n   return a; }"
- "kernel vec4 ComputeGamma ( __sample twoY, float edgeRatio ) __attribute__((outputFormat(kCIFormatRh))) { \n   float avX = twoY.x * edgeRatio; \n   float avY = twoY.y * edgeRatio; \n   float gamma = log( avY ) / log( avX ); \n   return vec4(gamma, 0.0, 0.0, 1.0); }"
- "kernel vec4 TwoY ( __sample a, __sample b, float width, float height, float xOffset, float yOffset, float widthInset, float heightInset ) __attribute__((outputFormat(kCIFormatRGh))) { \n   vec2 dc = destCoord(); \n   dc.x -= xOffset; \n   dc.y -= yOffset; \n   if ( ( dc.x > widthInset ) && ( dc.x < ( width - widthInset - 1.0 ) ) && ( dc.y > heightInset ) && ( dc.y < ( height - heightInset - 1.0 ) ) ) return vec4( 0.0 ); \n   vec3 Y = vec3( 0.299, 0.587, 0.114 ); \n\t return vec4( dot( a.rgb, Y ), dot( b.rgb, Y ), 0.0, ( a.a * b.a ) ); }"
- "kernelWithString:"
- "maximumNumberOfReferenceFrameCandidatesToHoldForProcessing"
- "networkOutputMaskFormatRequirements"
- "pen_ensureSpoofingOfEVMReferenceFrameSynchronizedStreamCaptureIDs"
- "refinedMasks"
- "setCropColorInputToFinalCropRect:"
- "setSkipProcessingWhenDepthDisabled:"
- "skipProcessingWhenDepthDisabled"
- "undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:"

```
