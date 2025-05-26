## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-475.31.1.0.0
-  __TEXT.__text: 0x45a794
+477.8.0.0.0
+  __TEXT.__text: 0x460314
   __TEXT.__auth_stubs: 0x4a30
-  __TEXT.__objc_methlist: 0x25e6c
+  __TEXT.__objc_methlist: 0x261f4
   __TEXT.__const: 0x1501a8
-  __TEXT.__cstring: 0x63d47
-  __TEXT.__oslogstring: 0x19f99
+  __TEXT.__cstring: 0x64308
+  __TEXT.__oslogstring: 0x1a140
   __TEXT.__gcc_except_tab: 0x1ed0
   __TEXT.__dlopen_cstrs: 0x588
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xa1b4
-  __TEXT.__objc_classname: 0x6b35
-  __TEXT.__objc_methname: 0x7f371
-  __TEXT.__objc_methtype: 0x11739
-  __TEXT.__objc_stubs: 0x37fa0
-  __DATA_CONST.__got: 0x4640
-  __DATA_CONST.__const: 0x8840
-  __DATA_CONST.__objc_classlist: 0x16d0
+  __TEXT.__unwind_info: 0xa95c
+  __TEXT.__objc_classname: 0x6c8a
+  __TEXT.__objc_methname: 0x7fcff
+  __TEXT.__objc_methtype: 0x118f8
+  __TEXT.__objc_stubs: 0x383c0
+  __DATA_CONST.__got: 0x4690
+  __DATA_CONST.__const: 0x8950
+  __DATA_CONST.__objc_classlist: 0x16f0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x460
+  __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x64b98
-  __DATA_CONST.__objc_selrefs: 0x10050
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_classrefs: 0x1970
-  __DATA_CONST.__objc_superrefs: 0x1570
-  __DATA_CONST.__objc_arraydata: 0x3208
-  __AUTH_CONST.__objc_const: 0x318
-  __AUTH_CONST.__cfstring: 0x30c60
-  __AUTH_CONST.__objc_intobj: 0x4368
-  __AUTH_CONST.__objc_arrayobj: 0x22b0
-  __AUTH_CONST.__const: 0xfa8
+  __DATA_CONST.__objc_const: 0x657b0
+  __DATA_CONST.__objc_selrefs: 0x10158
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_classrefs: 0x1990
+  __DATA_CONST.__objc_superrefs: 0x1588
+  __DATA_CONST.__objc_arraydata: 0x3288
+  __AUTH_CONST.__objc_const: 0x480
+  __AUTH_CONST.__cfstring: 0x311c0
+  __AUTH_CONST.__objc_intobj: 0x4380
+  __AUTH_CONST.__objc_arrayobj: 0x2358
+  __AUTH_CONST.__const: 0xfe8
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0x960
   __AUTH_CONST.__auth_got: 0x2528
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x844c
-  __DATA.__data: 0x4d78
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0x84fc
+  __DATA.__data: 0x4d90
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x220
-  __DATA.__bss: 0xf10
-  __DATA_DIRTY.__const: 0x2548
+  __DATA.__common: 0x1a0
+  __DATA.__bss: 0xe88
+  __DATA_DIRTY.__const: 0x2508
   __DATA_DIRTY.__objc_const: 0x13b70
-  __DATA_DIRTY.__objc_data: 0xe1a0
-  __DATA_DIRTY.__data: 0xde0
-  __DATA_DIRTY.__common: 0x5a0
-  __DATA_DIRTY.__bss: 0x978
+  __DATA_DIRTY.__objc_data: 0xe1f0
+  __DATA_DIRTY.__data: 0xe00
+  __DATA_DIRTY.__common: 0x720
+  __DATA_DIRTY.__bss: 0xa50
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 18473
-  Symbols:   66172
-  CStrings:  32110
+  Functions: 18573
+  Symbols:   66521
+  CStrings:  32254
 
Symbols:
+ +[BWColorConstancyProcessorController usesCustomProcessingFlow]
+ -[BWColorConstancyProcessorController _addFrame:type:]
+ -[BWColorConstancyProcessorController _loadSetupAndPrepareProcessor]
+ -[BWColorConstancyProcessorController _newOutputSampleBufferFromSampleBuffer:pixelBuffer:confidenceMap:metadata:processingFlags:formatDescriptionInOut:]
+ -[BWColorConstancyProcessorController dealloc]
+ -[BWColorConstancyProcessorController initWithConfiguration:]
+ -[BWColorConstancyProcessorController input:addAmbientFrame:]
+ -[BWColorConstancyProcessorController input:addFlashFrame:]
+ -[BWColorConstancyProcessorController inputAddFrameFailed:]
+ -[BWColorConstancyProcessorController metalImageBufferProcessor]
+ -[BWColorConstancyProcessorController outputPixelFormat]
+ -[BWColorConstancyProcessorController prepare]
+ -[BWColorConstancyProcessorController process]
+ -[BWColorConstancyProcessorController requestForInput:delegate:errOut:]
+ -[BWColorConstancyProcessorController reset]
+ -[BWColorConstancyProcessorControllerConfiguration clippingRecoveryEnabled]
+ -[BWColorConstancyProcessorControllerConfiguration dealloc]
+ -[BWColorConstancyProcessorControllerConfiguration lossyCompressionLevel]
+ -[BWColorConstancyProcessorControllerConfiguration saturationBoostEnabled]
+ -[BWColorConstancyProcessorControllerConfiguration setClippingRecoveryEnabled:]
+ -[BWColorConstancyProcessorControllerConfiguration setLossyCompressionLevel:]
+ -[BWColorConstancyProcessorControllerConfiguration setSaturationBoostEnabled:]
+ -[BWColorConstancyProcessorControllerConfiguration setVersion:]
+ -[BWColorConstancyProcessorControllerConfiguration version]
+ -[BWColorConstancyProcessorControllerInput addFrame:]
+ -[BWColorConstancyProcessorControllerInput addFrameFailed]
+ -[BWColorConstancyProcessorControllerInput ambientFrame]
+ -[BWColorConstancyProcessorControllerInput dealloc]
+ -[BWColorConstancyProcessorControllerInput flashFrame]
+ -[BWColorConstancyProcessorControllerRequest demosaicedRawErr]
+ -[BWColorConstancyProcessorControllerRequest readyForProcessing]
+ -[BWColorConstancyProcessorControllerRequest setDemosaicedRawErr:]
+ -[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:]
+ -[BWFigVideoCaptureDevice constantColorEnabled]
+ -[BWFigVideoCaptureDevice setConstantColorEnabled:]
+ -[BWFigVideoCaptureStream resignStreamStartStopDelegate]
+ -[BWFigVideoCaptureStream sourceNodeDidStopStreaming:]
+ -[BWIntelligentDistortionCorrectionProcessorControllerConfiguration baseDepthRotationDegrees]
+ -[BWIntelligentDistortionCorrectionProcessorControllerConfiguration setDepthDataCorrectionEnabled:primaryFormat:depthFormat:baseDepthRotationDegrees:]
+ -[BWMultiStreamCameraSourceNode eyeReliefStatusOutput]
+ -[BWMultiStreamCameraSourceNode trackedFacesOutput]
+ -[BWMultiStreamCameraSourceNodeConfiguration attentionDetectionEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration eyeReliefStatusOutputEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration secureMetadataEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration setAttentionDetectionEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setEyeReliefStatusOutputEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setSecureMetadataEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setTrackedFacesOutputEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration trackedFacesOutputEnabled]
+ -[BWPhotoEncoderNode _addConstantColorConfidenceMapForEncodingScheme:sampleBuffer:]
+ -[BWPhotoEncoderNode _handlePrewarmForConstantColorConfidenceMapForEncodingScheme:requestedStillImageCaptureSettings:confidenceMapDimensions:]
+ -[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]
+ -[BWPhotonicEngineNodeConfiguration constantColorClippingRecoveryEnabled]
+ -[BWPhotonicEngineNodeConfiguration constantColorSaturationBoostEnabled]
+ -[BWPhotonicEngineNodeConfiguration constantColorVersion]
+ -[BWPhotonicEngineNodeConfiguration sensorCenterOffset]
+ -[BWPhotonicEngineNodeConfiguration setConstantColorClippingRecoveryEnabled:]
+ -[BWPhotonicEngineNodeConfiguration setConstantColorSaturationBoostEnabled:]
+ -[BWPhotonicEngineNodeConfiguration setConstantColorVersion:]
+ -[BWPhotonicEngineNodeConfiguration setSensorCenterOffset:]
+ -[BWPointCloudDensificationNodeConfiguration initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:timeOfFlightCameraType:]
+ -[BWSoftISPProcessorControllerConfiguration sensorCenterOffset]
+ -[BWSoftISPProcessorControllerConfiguration setSensorCenterOffset:]
+ -[BWStillImageNodeConfiguration constantColorConfidenceMapDimensions]
+ -[BWStillImageNodeConfiguration setConstantColorConfidenceMapDimensions:]
+ -[BWUBCaptureParameters autoFlashColorConstancyNormalizedSNRThreshold]
+ -[BWVideoDepthInferenceConfiguration setSourceIsNuri:]
+ -[BWVideoDepthInferenceConfiguration sourceIsNuri]
+ -[FigCameraViewfinderLocal captureSessionDidStartWithVideoSource:captureSessionProxy:]
+ -[FigCameraViewfinderLocal captureSessionWillStartWithVideoSource:]
+ -[FigCaptureCameraSourcePipeline eyeReliefStatusOutputForSourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline trackedFacesOutputForSourceDeviceType:]
+ -[FigCaptureIrisSinkConfiguration constantColorClippingRecoveryEnabled]
+ -[FigCaptureIrisSinkConfiguration constantColorEnabled]
+ -[FigCaptureIrisSinkConfiguration constantColorSaturationBoostEnabled]
+ -[FigCaptureIrisSinkConfiguration setConstantColorClippingRecoveryEnabled:]
+ -[FigCaptureIrisSinkConfiguration setConstantColorEnabled:]
+ -[FigCaptureIrisSinkConfiguration setConstantColorSaturationBoostEnabled:]
+ -[FigCaptureLiDARDepthPipeline _buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:timeOfFlightCameraType:]
+ -[FigCaptureMetadataSinkPipeline _buildMetadataSinkPipeline:graph:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
+ -[FigCaptureMetadataSinkPipeline initWithConfiguration:graph:name:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:eyeReliefStatusSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
+ -[FigCapturePhotonicEngineSinkPipeline _addScalerNodeWithName:nodeConfiguration:bravoConstituentPhotoDeliveryEnabled:mainImageDownscalingFactorByAttachedMediaKey:depthDataDimensions:constantColorConfidenceMapDimensions:filterRenderingEnabled:enforcesZoomingForPortraitCaptures:backPressureDrivenPipelining:scalerNodeInputOut:scalerNodeOutputOut:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration constantColorClippingRecoveryEnabled]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration constantColorConfidenceMapDimensions]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration constantColorSaturationBoostEnabled]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration constantColorVersion]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration sensorCenterOffset]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setConstantColorClippingRecoveryEnabled:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setConstantColorConfidenceMapDimensions:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setConstantColorSaturationBoostEnabled:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setConstantColorVersion:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setSensorCenterOffset:]
+ -[FigCaptureSessionObservatory _willStartRunningForCaptureSession:sessionContainsVideoSource:]
+ -[FigCaptureSourceVideoFormat constantColorVersion]
+ -[FigCaptureSourceVideoFormat isConstantColorSupported]
+ -[FigCaptureStillImageSettings constantColorEnabled]
+ -[FigCaptureStillImageSettings constantColorFallbackPhotoDeliveryEnabled]
+ -[FigCaptureStillImageSettings setConstantColorEnabled:]
+ -[FigCaptureStillImageSettings setConstantColorFallbackPhotoDeliveryEnabled:]
+ -[FigMetadataObjectCaptureConnectionConfiguration attentionDetectionEnabled]
+ -[FigMetadataObjectCaptureConnectionConfiguration setAttentionDetectionEnabled:]
+ GCC_except_table200
+ GCC_except_table242
+ GCC_except_table302
+ GCC_except_table356
+ GCC_except_table431
+ GCC_except_table432
+ _.compoundliteral.23
+ _.compoundliteral.24
+ _.compoundliteral.33
+ _.compoundliteral.34
+ _.compoundliteral.35
+ _.compoundliteral.36
+ _.compoundliteral.46
+ _.compoundliteral.47
+ _.compoundliteral.48
+ _.compoundliteral.57
+ _.compoundliteral.73
+ _.compoundliteral.74
+ _.compoundliteral.75
+ _.compoundliteral.76
+ _.compoundliteral.78
+ _.compoundliteral.79
+ _.compoundliteral.80
+ _.compoundliteral.81
+ _BWAttachedMediaKey_ConstantColorConfidenceMap
+ _BWCreateSampleBufferWithDetectedObjectsInfo
+ _BWCreateSampleBufferWithEyeReliefResultDictionary
+ _BWIsConstantColorPrimaryFrame
+ _BWPhotonicEngineCreateColorConstancyProcessorControllerConfiguration
+ _FigCaptureMetadataObjectConfigurationRequiresEyeReliefStatus
+ _FigCaptureMetadataUtilitiesCreateDetectedObjectsInfoForCropRect
+ _FigCaptureMetadataUtilitiesCreateFacesArrayForCropRect
+ _FigCaptureMetadataUtilitiesRoundRectToMultipleOf
+ _FigCaptureMetadataUtilitiesUpdateDetectedObjectsInfoAndFacesArrayWithCropRect
+ _FigCapturePlatformSupportsExclaves
+ _FigCaptureSourceFormatKey_ColorConstancyVersion
+ _OBJC_CLASS_$_BWColorConstancyProcessorController
+ _OBJC_CLASS_$_BWColorConstancyProcessorControllerConfiguration
+ _OBJC_CLASS_$_BWColorConstancyProcessorControllerInput
+ _OBJC_CLASS_$_BWColorConstancyProcessorControllerRequest
+ _OBJC_IVAR_$_BWColorConstancyProcessorController._confidenceMapFormatDescription
+ _OBJC_IVAR_$_BWColorConstancyProcessorController._outputFormatDescription
+ _OBJC_IVAR_$_BWColorConstancyProcessorController._outputPixelFormat
+ _OBJC_IVAR_$_BWColorConstancyProcessorController._processor
+ _OBJC_IVAR_$_BWColorConstancyProcessorController._version
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerConfiguration._clippingRecoveryEnabled
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerConfiguration._lossyCompressionLevel
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerConfiguration._saturationBoostEnabled
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerConfiguration._version
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerConfiguration.version
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerInput._addFrameFailed
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerInput._ambientFrame
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerInput._flashFrame
+ _OBJC_IVAR_$_BWColorConstancyProcessorControllerRequest._demosaicedRawErr
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._constantColorEnabled
+ _OBJC_IVAR_$_BWIntelligentDistortionCorrectionProcessorControllerConfiguration._baseDepthRotationDegrees
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._eyeReliefStatusOutput
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._trackedFacesOutput
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._attentionDetectionEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._eyeReliefStatusOutputEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._secureMetadataEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._trackedFacesOutputEnabled
+ _OBJC_IVAR_$_BWPhotonicEngineNode._colorConstancyProcessorControllerConfiguration
+ _OBJC_IVAR_$_BWPhotonicEngineNode._colorConstancyProcessorControllerInputByPortType
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._constantColorClippingRecoveryEnabled
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._constantColorSaturationBoostEnabled
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._constantColorVersion
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._sensorCenterOffset
+ _OBJC_IVAR_$_BWSoftISPProcessorControllerConfiguration._sensorCenterOffset
+ _OBJC_IVAR_$_BWStillImageNodeConfiguration._constantColorConfidenceMapDimensions
+ _OBJC_IVAR_$_BWUBCaptureParameters._autoFlashColorConstancyNormalizedSNRThreshold
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._sourceIsNuri
+ _OBJC_IVAR_$_BWVideoDepthNode._sourceIsNuri
+ _OBJC_IVAR_$_FigCameraViewfinderLocal._sessionContainsVideoSource
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._eyeReliefStatusOutputsBySourceDeviceType
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._trackedFacesOutputsBySourceDeviceType
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._constantColorClippingRecoveryEnabled
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._constantColorEnabled
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._constantColorSaturationBoostEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._constantColorClippingRecoveryEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._constantColorConfidenceMapDimensions
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._constantColorSaturationBoostEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._constantColorVersion
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._sensorCenterOffset
+ _OBJC_IVAR_$_FigCaptureStillImageSettings._constantColorEnabled
+ _OBJC_IVAR_$_FigCaptureStillImageSettings._constantColorFallbackPhotoDeliveryEnabled
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._attentionDetectionEnabled
+ _OBJC_METACLASS_$_BWColorConstancyProcessorController
+ _OBJC_METACLASS_$_BWColorConstancyProcessorControllerConfiguration
+ _OBJC_METACLASS_$_BWColorConstancyProcessorControllerInput
+ _OBJC_METACLASS_$_BWColorConstancyProcessorControllerRequest
+ __OBJC_$_CLASS_METHODS_BWColorConstancyProcessorController
+ __OBJC_$_INSTANCE_METHODS_BWColorConstancyProcessorController
+ __OBJC_$_INSTANCE_METHODS_BWColorConstancyProcessorControllerConfiguration
+ __OBJC_$_INSTANCE_METHODS_BWColorConstancyProcessorControllerInput
+ __OBJC_$_INSTANCE_METHODS_BWColorConstancyProcessorControllerRequest
+ __OBJC_$_INSTANCE_VARIABLES_BWColorConstancyProcessorController
+ __OBJC_$_INSTANCE_VARIABLES_BWColorConstancyProcessorControllerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BWColorConstancyProcessorControllerInput
+ __OBJC_$_INSTANCE_VARIABLES_BWColorConstancyProcessorControllerRequest
+ __OBJC_$_PROP_LIST_BWColorConstancyProcessorController
+ __OBJC_$_PROP_LIST_BWColorConstancyProcessorControllerConfiguration
+ __OBJC_$_PROP_LIST_BWColorConstancyProcessorControllerInput
+ __OBJC_$_PROP_LIST_BWColorConstancyProcessorControllerRequest
+ __OBJC_$_PROP_LIST_CMIColourConstancyProcessorProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWColorConstancyProcessorControllerInputUpdatesDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMIColourConstancyProcessorProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWColorConstancyProcessorControllerInputUpdatesDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMIColourConstancyProcessorProtocol
+ __OBJC_$_PROTOCOL_REFS_BWColorConstancyProcessorControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_BWColorConstancyProcessorControllerInputUpdatesDelegate
+ __OBJC_$_PROTOCOL_REFS_CMIColourConstancyProcessorDelegate
+ __OBJC_$_PROTOCOL_REFS_CMIColourConstancyProcessorProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BWColorConstancyProcessorController
+ __OBJC_CLASS_RO_$_BWColorConstancyProcessorController
+ __OBJC_CLASS_RO_$_BWColorConstancyProcessorControllerConfiguration
+ __OBJC_CLASS_RO_$_BWColorConstancyProcessorControllerInput
+ __OBJC_CLASS_RO_$_BWColorConstancyProcessorControllerRequest
+ __OBJC_LABEL_PROTOCOL_$_BWColorConstancyProcessorControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_BWColorConstancyProcessorControllerInputUpdatesDelegate
+ __OBJC_LABEL_PROTOCOL_$_CMIColourConstancyProcessorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CMIColourConstancyProcessorProtocol
+ __OBJC_METACLASS_RO_$_BWColorConstancyProcessorController
+ __OBJC_METACLASS_RO_$_BWColorConstancyProcessorControllerConfiguration
+ __OBJC_METACLASS_RO_$_BWColorConstancyProcessorControllerInput
+ __OBJC_METACLASS_RO_$_BWColorConstancyProcessorControllerRequest
+ __OBJC_PROTOCOL_$_BWColorConstancyProcessorControllerDelegate
+ __OBJC_PROTOCOL_$_BWColorConstancyProcessorControllerInputUpdatesDelegate
+ __OBJC_PROTOCOL_$_CMIColourConstancyProcessorDelegate
+ __OBJC_PROTOCOL_$_CMIColourConstancyProcessorProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CMIColourConstancyProcessorProtocol
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.112
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.120
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.124
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke_2.125
+ ___101-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:stillImageSettings:portType:]_block_invoke.162
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.312
+ ___126-[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:]_block_invoke
+ ___128-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:queueProvidingInput:processingPlan:]_block_invoke.302
+ ___159-[BWPhotonicEngineNode _setupProcessingStateForIntelligentDistortionCorrectionIfNeededWithSettings:sequenceNumber:portType:queueProvidingInput:processingPlan:]_block_invoke.291
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.593
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.911
+ ___44-[BWPhotonicEngineNode _nrfOutputSbufRouter]_block_invoke.378
+ ___65-[BWPhotonicEngineNode _standardNROutputRouterWithExpectedQueue:]_block_invoke.380
+ ___67-[FigCameraViewfinderLocal captureSessionWillStartWithVideoSource:]_block_invoke
+ ___68-[BWColorConstancyProcessorController _loadSetupAndPrepareProcessor]_block_invoke
+ ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.92
+ ___86-[BWPhotonicEngineNode _setupProcessingStateForDeepFusionWithSettings:processingPlan:]_block_invoke.265
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.270
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.271
+ ___94-[FigCaptureSessionObservatory _willStartRunningForCaptureSession:sessionContainsVideoSource:]_block_invoke
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.286
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke_2
+ ___97-[BWPhotonicEngineNode _setupSoftISPOutputRoutingForFusionCaptureTypeIfNeededWithProcessingPlan:]_block_invoke.239
+ ___block_descriptor_68_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_78_e8_32o40o48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_literal_global.124
+ ___block_literal_global.129
+ ___block_literal_global.196
+ ___block_literal_global.223
+ ___block_literal_global.252
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.373
+ ___block_literal_global.384
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.72
+ ___block_literal_global.776
+ ___block_literal_global.827
+ ___block_literal_global.865
+ __unnamed_array_storage.199
+ __unnamed_array_storage.210
+ __unnamed_array_storage.237
+ __unnamed_array_storage.253
+ __unnamed_array_storage.257
+ __unnamed_array_storage.288
+ __unnamed_array_storage.310
+ __unnamed_array_storage.326
+ __unnamed_array_storage.344
+ __unnamed_array_storage.351
+ __unnamed_array_storage.366
+ __unnamed_array_storage.369
+ __unnamed_array_storage.375
+ __unnamed_array_storage.389
+ __unnamed_array_storage.408
+ __unnamed_array_storage.422
+ __unnamed_array_storage.456
+ __unnamed_array_storage.463
+ __unnamed_array_storage.472
+ __unnamed_array_storage.549
+ __unnamed_array_storage.578
+ __unnamed_array_storage.58
+ __unnamed_array_storage.589
+ __unnamed_array_storage.922
+ _csp_gdcExpandsImageDimensions
+ _kCMPhotoCompressionOption_AllowExperimentalCodecs
+ _kCMPhotoDecompressionOption_AllowExperimentalCodecs
+ _kFigCaptureDeviceNotification_SensorAccessRevoked
+ _kFigCaptureSampleBufferAttachmentKey_EyeReliefResult
+ _kFigCaptureSessionNotificationPayloadKey_ConstantColorConfidenceMapSurface
+ _kFigCaptureSessionNotificationPayloadKey_ConstantColorConfidenceMapSurface_Serialized
+ _kFigCaptureSessionNotificationPayloadKey_ConstantColorMetadata
+ _kFigCaptureSessionWillStartRunningNotificationPayloadKey_ContainsVideoSource
+ _kFigCaptureSourceAVHEVCSettingsKey_MSTFBand0ModulationOnlyWhenRequired
+ _kFigCaptureSourceAttributeKey_AttentionDetectionSupported
+ _kFigCaptureSourceAttributeKey_EyeReliefSupported
+ _kFigCaptureSourceAttributeKey_SecureMetadataSupported
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureEyeReliefStatusDetectionEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceDetectionConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceDetectionEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureDetectedFaces
+ _kFigCaptureStreamMetadataOutputKey_SecureEyeReliefResult
+ _kFigCaptureStreamMetadata_InvalidDueToNoSensorAccess
+ _kFigCaptureStreamProperty_ExclusivelyForSecureProcessing
+ _kFigCaptureStreamSecureFaceDetectionConfigurationKey_AttentionDetectionEnabled
+ _kFigConstantColorMetadataAttachmentKey_CenterWeightedMeanConfidenceLevel
+ _kFigMetadataIdentifier_QuickTimeMetadataEyeReliefStatus
+ _kFigSampleBufferAttachmentKey_ConstantColorMetadata
+ _mscsnu_createSampleBufferWithPTS
+ _multiStreamCameraSourceNode_secureDetectedFacesServiceQueueCallback
+ _multiStreamCameraSourceNode_secureEyeReliefStatusServiceQueueCallback
+ _objc_msgSend$_buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:timeOfFlightCameraType:
+ _objc_msgSend$attentionDetectionEnabled
+ _objc_msgSend$autoFlashColorConstancyNormalizedSNRThreshold
+ _objc_msgSend$baseDepthRotationDegrees
+ _objc_msgSend$captureSessionDidStartWithVideoSource:captureSessionProxy:
+ _objc_msgSend$captureSessionWillStartWithVideoSource:
+ _objc_msgSend$clippingRecoveryEnabled
+ _objc_msgSend$constantColorClippingRecoveryEnabled
+ _objc_msgSend$constantColorConfidenceMapDimensions
+ _objc_msgSend$constantColorEnabled
+ _objc_msgSend$constantColorFallbackPhotoDeliveryEnabled
+ _objc_msgSend$constantColorSaturationBoostEnabled
+ _objc_msgSend$constantColorVersion
+ _objc_msgSend$eyeReliefStatusOutput
+ _objc_msgSend$eyeReliefStatusOutputEnabled
+ _objc_msgSend$initWithDimensions:propagationMode:
+ _objc_msgSend$initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:timeOfFlightCameraType:
+ _objc_msgSend$outputCenterWeightedMeanColourAccuracyConfidenceLevel
+ _objc_msgSend$outputColourAccuracyConfidenceImagePixelBuffer
+ _objc_msgSend$resignStreamStartStopDelegate
+ _objc_msgSend$saturationBoostEnabled
+ _objc_msgSend$secureMetadataEnabled
+ _objc_msgSend$setAttentionDetectionEnabled:
+ _objc_msgSend$setClippingRecoveryEnabled:
+ _objc_msgSend$setConstantColorClippingRecoveryEnabled:
+ _objc_msgSend$setConstantColorConfidenceMapDimensions:
+ _objc_msgSend$setConstantColorEnabled:
+ _objc_msgSend$setConstantColorFallbackPhotoDeliveryEnabled:
+ _objc_msgSend$setConstantColorSaturationBoostEnabled:
+ _objc_msgSend$setConstantColorVersion:
+ _objc_msgSend$setDepthDataCorrectionEnabled:primaryFormat:depthFormat:baseDepthRotationDegrees:
+ _objc_msgSend$setEyeReliefStatusOutputEnabled:
+ _objc_msgSend$setFrontCameraHas180DegreesRotation:
+ _objc_msgSend$setOutputColourAccuracyConfidenceImagePixelBuffer:
+ _objc_msgSend$setSaturationBoostEnabled:
+ _objc_msgSend$setSecureMetadataEnabled:
+ _objc_msgSend$setSourceIsNuri:
+ _objc_msgSend$setTrackedFacesOutputEnabled:
+ _objc_msgSend$sourceIsNuri
+ _objc_msgSend$sourceNodeDidStopStreaming:
+ _objc_msgSend$takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:
+ _objc_msgSend$trackedFacesOutput
+ _objc_msgSend$trackedFacesOutputEnabled
+ _sPendingPowerEventsCount
- -[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:]
- -[BWFigVideoCaptureStream sourceNodeDidStopStreaming]
- -[BWIntelligentDistortionCorrectionProcessorControllerConfiguration setDepthDataCorrectionEnabled:primaryFormat:depthFormat:]
- -[BWPhotonicEngineNodeConfiguration geometricDistortionCorrectionInputCropOffset]
- -[BWPhotonicEngineNodeConfiguration setGeometricDistortionCorrectionInputCropOffset:]
- -[BWPointCloudDensificationNodeConfiguration initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:videoInputDimensions:timeOfFlightCameraType:]
- -[BWPointCloudDensificationNodeConfiguration videoInputDimensions]
- -[FigCameraViewfinderLocal captureSessionDidStart:]
- -[FigCameraViewfinderLocal captureSessionWillStart]
- -[FigCaptureLiDARDepthPipeline _buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:videoInputDimensions:timeOfFlightCameraType:]
- -[FigCaptureMetadataSinkPipeline _buildMetadataSinkPipeline:graph:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
- -[FigCaptureMetadataSinkPipeline initWithConfiguration:graph:name:videoPreviewOutput:offlineVISMotionDataSourceOutput:objectDetectionSourceOutput:faceTrackingSourceOutput:captureDevice:faceTrackingPipelineStage:clientAuditToken:inferenceScheduler:delegate:]
- -[FigCapturePhotonicEngineSinkPipeline _addScalerNodeWithName:nodeConfiguration:bravoConstituentPhotoDeliveryEnabled:mainImageDownscalingFactorByAttachedMediaKey:depthDataDimensions:filterRenderingEnabled:enforcesZoomingForPortraitCaptures:backPressureDrivenPipelining:scalerNodeInputOut:scalerNodeOutputOut:]
- -[FigCapturePhotonicEngineSinkPipelineConfiguration gdcInDCProcessorInputCropOffset]
- -[FigCapturePhotonicEngineSinkPipelineConfiguration setGdcInDCProcessorInputCropOffset:]
- -[FigCaptureSessionObservatory _willStartRunningForCaptureSession:]
- GCC_except_table198
- GCC_except_table238
- GCC_except_table294
- GCC_except_table347
- GCC_except_table422
- GCC_except_table423
- _.compoundliteral.39
- _.compoundliteral.40
- _.compoundliteral.41
- _.compoundliteral.42
- _.compoundliteral.50
- _.compoundliteral.51
- _.compoundliteral.52
- _.compoundliteral.53
- _.compoundliteral.54
- _.compoundliteral.55
- _.compoundliteral.60
- _.compoundliteral.61
- _.compoundliteral.63
- _.compoundliteral.64
- _.compoundliteral.65
- _.compoundliteral.66
- _.compoundliteral.67
- _.compoundliteral.68
- _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._geometricDistortionCorrectionInputCropOffset
- _OBJC_IVAR_$_BWPointCloudDensificationNodeConfiguration._videoInputDimensions
- _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._gdcInDCProcessorInputCropOffset
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.109
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.117
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.121
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke_2.122
- ___101-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:stillImageSettings:portType:]_block_invoke.159
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.304
- ___128-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:queueProvidingInput:processingPlan:]_block_invoke.294
- ___159-[BWPhotonicEngineNode _setupProcessingStateForIntelligentDistortionCorrectionIfNeededWithSettings:sequenceNumber:portType:queueProvidingInput:processingPlan:]_block_invoke.283
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.558
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.876
- ___44-[BWPhotonicEngineNode _nrfOutputSbufRouter]_block_invoke.370
- ___51-[FigCameraViewfinderLocal captureSessionWillStart]_block_invoke
- ___62-[BWMultiStreamCameraSourceNode _registerStreamOutputHandlers]_block_invoke_11
- ___65-[BWPhotonicEngineNode _standardNROutputRouterWithExpectedQueue:]_block_invoke.372
- ___67-[FigCaptureSessionObservatory _willStartRunningForCaptureSession:]_block_invoke
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.89
- ___86-[BWPhotonicEngineNode _setupProcessingStateForDeepFusionWithSettings:processingPlan:]_block_invoke.262
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.267
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.268
- ___90-[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:]_block_invoke
- ___97-[BWPhotonicEngineNode _setupSoftISPOutputRoutingForFusionCaptureTypeIfNeededWithProcessingPlan:]_block_invoke.236
- ___block_descriptor_77_e8_32o40o48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
- ___block_literal_global.121
- ___block_literal_global.145
- ___block_literal_global.194
- ___block_literal_global.237
- ___block_literal_global.249
- ___block_literal_global.325
- ___block_literal_global.330
- ___block_literal_global.364
- ___block_literal_global.375
- ___block_literal_global.426
- ___block_literal_global.428
- ___block_literal_global.67
- ___block_literal_global.773
- ___block_literal_global.798
- ___block_literal_global.836
- ___block_literal_global.88
- ___block_literal_global.93
- ___block_literal_global.98
- __unnamed_array_storage.157
- __unnamed_array_storage.205
- __unnamed_array_storage.234
- __unnamed_array_storage.241
- __unnamed_array_storage.254
- __unnamed_array_storage.265
- __unnamed_array_storage.271
- __unnamed_array_storage.302
- __unnamed_array_storage.309
- __unnamed_array_storage.318
- __unnamed_array_storage.321
- __unnamed_array_storage.343
- __unnamed_array_storage.350
- __unnamed_array_storage.361
- __unnamed_array_storage.367
- __unnamed_array_storage.381
- __unnamed_array_storage.400
- __unnamed_array_storage.414
- __unnamed_array_storage.448
- __unnamed_array_storage.464
- __unnamed_array_storage.546
- __unnamed_array_storage.554
- __unnamed_array_storage.826
- __unnamed_array_storage.888
- _dfrb_createCorrectedFacesArrayForTotalSensorCropRect
- _doirb_createCorrectedDetectedObjectsInfoForTotalSensorCropRect
- _kFigCaptureDeviceNotification_PixelsInvalidated
- _kFigCaptureStreamMetadataOutputKey_EyeOrientationSupport
- _kFigCaptureStreamMetadataOutputKey_StreamingDetectedFaces
- _kFigCaptureStreamMetadata_InvalidPixels
- _kFigCaptureStreamVideoOutputID_ProResRaw
- _multiStreamCameraSourceNode_proresRawServiceQueueCallback
- _objc_msgSend$_buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:videoInputDimensions:timeOfFlightCameraType:
- _objc_msgSend$captureSessionDidStart:
- _objc_msgSend$captureSessionWillStart
- _objc_msgSend$gdcInDCProcessorInputCropOffset
- _objc_msgSend$initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:videoInputDimensions:timeOfFlightCameraType:
- _objc_msgSend$setDepthDataCorrectionEnabled:primaryFormat:depthFormat:
- _objc_msgSend$setGdcInDCProcessorInputCropOffset:
- _objc_msgSend$sourceNodeDidStopStreaming
- _objc_msgSend$takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:
- _objc_msgSend$videoInputDimensions
CStrings:
+ " ConstantColor:1%@"
+ " constantColorConfidenceMap:%d"
+ "! err && infraredRequiredFormat"
+ "! err && requiredFormat"
+ "! err && underlyingFormat"
+ "(clippingRecovery ON)"
+ "(fallback:1)"
+ "(saturationBoost ON)"
+ ", (constantColor ON %@%@)"
+ ", attentionDetection:%d"
+ "-[BWColorConstancyProcessorController process]"
+ "-[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:]_block_invoke"
+ "-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke"
+ "-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke_2"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Missing optical center calibrated for narrower FOV - proceeding without (err: %d)"
+ "<<<< BWStillImageProcessing >>>> %s: Processed Color Constancy: captureID:%lld err:%d"
+ "<<<< BWStillImageProcessingNode >>>> %s: Routing sample buffer '%@' for '%@' (err=%d) into Color Constancy"
+ "<<<< BWStillImageProcessingNode >>>> %s: Routing sample buffer '%@' for '%@' (err=%d) into NRF (Constant Color Ambient fallback)"
+ "<<<< FigCapturePowerLog >>>> %s: Skipping check because there are %ld pending power events"
+ "@\"<CMIColourConstancyProcessorDelegate>\"16@0:8"
+ "@\"<CMIColourConstancyProcessorProtocol>\""
+ "@\"BWColorConstancyProcessorControllerConfiguration\""
+ "@60@0:8@16@24i32i36B40I44{?=ii}48i56"
+ "AVMetadataObjectTypeEyeReliefStatus"
+ "AttentionDetectionSupported"
+ "AutoFlashColorConstancyNormalizedSNRThreshold"
+ "BWColorConstancyProcessorController"
+ "BWColorConstancyProcessorControllerConfiguration"
+ "BWColorConstancyProcessorControllerDelegate"
+ "BWColorConstancyProcessorControllerInput"
+ "BWColorConstancyProcessorControllerInputUpdatesDelegate"
+ "BWColorConstancyProcessorControllerRequest"
+ "CMIColourConstancyFrameParamsV%d"
+ "CMIColourConstancyProcessorDelegate"
+ "CMIColourConstancyProcessorProtocol"
+ "ColorConstancyVersion"
+ "ColourConstancy"
+ "ConstantColorConfidenceMap"
+ "ConstantColorConfidenceMapSurface"
+ "ConstantColorConfidenceMapSurface_Serialized"
+ "ConstantColorMetadata"
+ "ContainsVideoSource"
+ "EyeReliefStatus"
+ "EyeReliefSupported"
+ "J507"
+ "J508"
+ "J537"
+ "J538"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "MSTFBand0ModulationOnlyWhenRequired"
+ "Metadata output is enabled, but no secure metadata features are enabled."
+ "MetadataGroup-SecureMetadata"
+ "NoiseReductionAccuracy"
+ "SecureDetectedObjects"
+ "SecureEyeReliefStatus"
+ "SecureMetadataCameraSupported"
+ "SecureMetadataSupported"
+ "SensorAccessRevoked"
+ "T@\"<BWFigCaptureStreamStartStopDelegate>\",N"
+ "T@\"<CMIColourConstancyProcessorDelegate>\",W,N"
+ "T@\"BWNodeOutput\",R,V_eyeReliefStatusOutput"
+ "T@\"BWNodeOutput\",R,V_trackedFacesOutput"
+ "TB,N,V_attentionDetectionEnabled"
+ "TB,N,V_clippingRecoveryEnabled"
+ "TB,N,V_constantColorClippingRecoveryEnabled"
+ "TB,N,V_constantColorEnabled"
+ "TB,N,V_constantColorFallbackPhotoDeliveryEnabled"
+ "TB,N,V_constantColorSaturationBoostEnabled"
+ "TB,N,V_eyeReliefStatusOutputEnabled"
+ "TB,N,V_saturationBoostEnabled"
+ "TB,N,V_secureMetadataEnabled"
+ "TB,N,V_sourceIsNuri"
+ "TB,N,V_trackedFacesOutputEnabled"
+ "TB,R,GisConstantColorSupported"
+ "Td,R,N,V_autoFlashColorConstancyNormalizedSNRThreshold"
+ "Ti,N,V_constantColorVersion"
+ "Ti,R,N,V_baseDepthRotationDegrees"
+ "T{?=ii},N,V_constantColorConfidenceMapDimensions"
+ "_attentionDetectionEnabled"
+ "_autoFlashColorConstancyNormalizedSNRThreshold"
+ "_baseDepthRotationDegrees"
+ "_buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:timeOfFlightCameraType:"
+ "_clippingRecoveryEnabled"
+ "_colorConstancyProcessorControllerConfiguration"
+ "_colorConstancyProcessorControllerInputByPortType"
+ "_confidenceMapFormatDescription"
+ "_constantColorClippingRecoveryEnabled"
+ "_constantColorConfidenceMapDimensions"
+ "_constantColorEnabled"
+ "_constantColorFallbackPhotoDeliveryEnabled"
+ "_constantColorSaturationBoostEnabled"
+ "_constantColorVersion"
+ "_eyeReliefStatusOutput"
+ "_eyeReliefStatusOutputEnabled"
+ "_eyeReliefStatusOutputsBySourceDeviceType"
+ "_saturationBoostEnabled"
+ "_secureMetadataEnabled"
+ "_sessionContainsVideoSource"
+ "_sourceIsNuri"
+ "_trackedFacesOutput"
+ "_trackedFacesOutputEnabled"
+ "_trackedFacesOutputsBySourceDeviceType"
+ "attentionDetectionEnabled"
+ "autoFlashColorConstancyNormalizedSNRThreshold"
+ "baseDepthRotationDegrees"
+ "captureSessionDidStartWithVideoSource:captureSessionProxy:"
+ "captureSessionWillStartWithVideoSource:"
+ "clippingRecoveryEnabled"
+ "constantColorClippingRecoveryEnabled"
+ "constantColorConfidenceMapDimensions"
+ "constantColorConfidenceMapDimensionsHeight"
+ "constantColorConfidenceMapDimensionsWidth"
+ "constantColorEnabled"
+ "constantColorFallbackPhotoDeliveryEnabled"
+ "constantColorSaturationBoostEnabled"
+ "constantColorSupported"
+ "constantColorVersion"
+ "description=CameraCapture-477.8"
+ "detectedObjectsInfo"
+ "detectedObjectsInfo is nil"
+ "eyeReliefStatusOutput"
+ "eyeReliefStatusOutputEnabled"
+ "i44@0:8@16@24@32i40"
+ "i44@0:8^{__CVBuffer=}16@\"NSDictionary\"24I32@\"<CMIColourConstancyFrameParams>\"36"
+ "initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:timeOfFlightCameraType:"
+ "isConstantColorSupported"
+ "outputCenterWeightedMeanColourAccuracyConfidenceLevel"
+ "outputColourAccuracyConfidenceImagePixelBuffer"
+ "resignStreamStartStopDelegate"
+ "saturationBoostEnabled"
+ "secureDetectedFacesSupported"
+ "secureEyeReliefSupported"
+ "secureMetadataEnabled"
+ "sensorCenterOffsetX"
+ "sensorCenterOffsetY"
+ "setAttentionDetectionEnabled:"
+ "setClippingRecoveryEnabled:"
+ "setConstantColorClippingRecoveryEnabled:"
+ "setConstantColorConfidenceMapDimensions:"
+ "setConstantColorEnabled:"
+ "setConstantColorFallbackPhotoDeliveryEnabled:"
+ "setConstantColorSaturationBoostEnabled:"
+ "setConstantColorVersion:"
+ "setDepthDataCorrectionEnabled:primaryFormat:depthFormat:baseDepthRotationDegrees:"
+ "setEyeReliefStatusOutputEnabled:"
+ "setFrontCameraHas180DegreesRotation:"
+ "setOutputCenterWeightedMeanColourAccuracyConfidenceLevel:"
+ "setOutputColourAccuracyConfidenceImagePixelBuffer:"
+ "setSaturationBoostEnabled:"
+ "setSecureMetadataEnabled:"
+ "setSourceIsNuri:"
+ "setTrackedFacesOutputEnabled:"
+ "sourceIsNuri"
+ "sourceNodeDidStopStreaming:"
+ "tag:apple.com,2023:photo:aux:constantcolorconfidencemap"
+ "takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:prefersDeviceInvalidatedImmediately:"
+ "trackedFacesOutput"
+ "trackedFacesOutputEnabled"
+ "v24@0:8@\"<CMIColourConstancyProcessorDelegate>\"16"
+ "v24@0:8@\"BWColorConstancyProcessorControllerInput\"16"
+ "v28@0:8B16@\"FigCaptureSessionProxy\"20"
+ "v32@0:8@\"BWColorConstancyProcessorControllerInput\"16^{opaqueCMSampleBuffer=}24"
+ "v36@0:8@16i24B28B32"
+ "v40@0:8B16@20@28i36"
- "-[BWFigCaptureDeviceVendor takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:]_block_invoke"
- "<<<< BWFigVideoCaptureStream >>>> %s: Missing optical center calibrated for narrower FOV - proceeding without"
- "@68@0:8@16@24i32i36B40I44{?=ii}48{?=ii}56i64"
- "PixelsInvalidated"
- "T@\"<BWFigCaptureStreamStartStopDelegate>\",N,V_startStopDelegate"
- "T{?=ii},R,N,V_videoInputDimensions"
- "T{CGPoint=dd},N,V_gdcInDCProcessorInputCropOffset"
- "_buildLiDARDepthPipelineWithVideoSourceCaptureOutput:pointCloudOutput:graph:videoInputDimensions:timeOfFlightCameraType:"
- "_gdcInDCProcessorInputCropOffset"
- "_videoInputDimensions"
- "captureSessionDidStart:"
- "captureSessionWillStart"
- "description=CameraCapture-475.31.1"
- "gdcInDCProcessorInputCropOffset"
- "gdcInDCProcessorInputCropOffsetX"
- "gdcInDCProcessorInputCropOffsetY"
- "i52@0:8@16@24@32{?=ii}40i48"
- "infraredCaptureSource"
- "infraredRequiredFormat"
- "initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:videoInputDimensions:timeOfFlightCameraType:"
- "pointCloudTimeMachineConnectionConfiguration"
- "setDepthDataCorrectionEnabled:primaryFormat:depthFormat:"
- "setGdcInDCProcessorInputCropOffset:"
- "sourceNodeDidStopStreaming"
- "takeBackDevice:forClient:informClientWhenDeviceAvailableAgain:"
- "timeOfFlightCaptureSource"
- "underlyingFormat"
- "v36@0:8B16@20@28"
- "videoInputDimensions"

```
