## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-664.0.0.0.2
-  __TEXT.__text: 0x579f80
-  __TEXT.__auth_stubs: 0x5080
-  __TEXT.__objc_methlist: 0x323d0
-  __TEXT.__const: 0x150840
-  __TEXT.__cstring: 0x8be9f
-  __TEXT.__oslogstring: 0x39095
-  __TEXT.__gcc_except_tab: 0x2a7c
+664.2.5.0.0
+  __TEXT.__text: 0x57bf24
+  __TEXT.__auth_stubs: 0x5090
+  __TEXT.__objc_methlist: 0x32448
+  __TEXT.__const: 0x150850
+  __TEXT.__cstring: 0x8c31c
+  __TEXT.__oslogstring: 0x396b0
+  __TEXT.__gcc_except_tab: 0x2a6c
   __TEXT.__dlopen_cstrs: 0x65d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xdfb8
+  __TEXT.__unwind_info: 0xdfe8
   __TEXT.__eh_frame: 0x68
   __TEXT.__objc_classname: 0x812f
-  __TEXT.__objc_methname: 0x9fe5c
-  __TEXT.__objc_methtype: 0x15834
-  __TEXT.__objc_stubs: 0x44fc0
-  __DATA_CONST.__got: 0x6628
-  __DATA_CONST.__const: 0xdca0
+  __TEXT.__objc_methname: 0xa00b5
+  __TEXT.__objc_methtype: 0x15875
+  __TEXT.__objc_stubs: 0x45080
+  __DATA_CONST.__got: 0x6640
+  __DATA_CONST.__const: 0xdc78
   __DATA_CONST.__objc_classlist: 0x1b30
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x5a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d90
+  __DATA_CONST.__objc_selrefs: 0x13dd0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1998
   __DATA_CONST.__objc_arraydata: 0x3660
-  __AUTH_CONST.__auth_got: 0x2850
-  __AUTH_CONST.__const: 0x4008
-  __AUTH_CONST.__cfstring: 0x41e20
-  __AUTH_CONST.__objc_const: 0x8f228
-  __AUTH_CONST.__objc_intobj: 0x5550
+  __AUTH_CONST.__auth_got: 0x2858
+  __AUTH_CONST.__const: 0x4048
+  __AUTH_CONST.__cfstring: 0x41f60
+  __AUTH_CONST.__objc_const: 0x8f2b8
+  __AUTH_CONST.__objc_intobj: 0x5568
   __AUTH_CONST.__objc_arrayobj: 0x26e8
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa70
   __AUTH.__objc_data: 0x2da0
-  __DATA.__objc_ivar: 0xa184
+  __DATA.__objc_ivar: 0xa190
   __DATA.__data: 0x5228
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xa60
-  __DATA.__bss: 0x20b0
+  __DATA.__bss: 0x20c0
   __DATA_DIRTY.__objc_data: 0xe240
   __DATA_DIRTY.__data: 0x1060
   __DATA_DIRTY.__common: 0x780
-  __DATA_DIRTY.__bss: 0xc50
+  __DATA_DIRTY.__bss: 0xc60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 8D31699A-51D5-3A44-A1D1-C27779A298C1
-  Functions: 30070
-  Symbols:   98602
-  CStrings:  49661
+  UUID: 08EEAC6D-F228-305D-8C09-A0190443E1A5
+  Functions: 30098
+  Symbols:   98707
+  CStrings:  49720
 
Symbols:
+ -[BWAudioConverterNode expectsToRecordOnlyOnce]
+ -[BWAudioConverterNode setExpectsToRecordOnlyOnce:]
+ -[BWAudioRemixAnalysisMetadataNode expectsToRecordOnlyOnce]
+ -[BWAudioRemixAnalysisMetadataNode renderSampleBuffer:forInput:].cold.9
+ -[BWAudioRemixAnalysisMetadataNode setExpectsToRecordOnlyOnce:]
+ -[BWCaptureDeferredPhotoProcessor _runImageCorruptionDetectionForJob:onEncodedSurface:surfaceSize:]
+ -[BWInferenceScalingRequirement _processOrderedVideoRequirementsForLandscapeOriented:withPrototypeRequirement:]
+ -[BWPhotoEncoderController _addOrientationOptionsToDictionary:encodingScheme:metadata:allowSensorOrientationRotation:]
+ -[BWPhotoEncoderController _addOrientationOptionsToDictionary:encodingScheme:orientation:allowSensorOrientationRotation:]
+ -[BWPhotoEncoderController _desiredOrientationForOrientation:encodingScheme:]
+ -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:mainImageHandleInOut:]
+ -[BWPhotoEncoderController _exifExtraRotationDegreesForEncodingScheme:]
+ -[BWPhotoEncoderController _optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:containerOptionsOut:encodingOptionsOut:]
+ -[BWPhotoEncoderController inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:].cold.1
+ -[BWPhotoEncoderControllerConfiguration legacySensorOrientationRotationDegrees]
+ -[BWPhotoEncoderControllerConfiguration setLegacySensorOrientationRotationDegrees:]
+ -[BWPhotoEncoderNode initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:clientIsCameraOrDerivative:]
+ -[BWSoftISPProcessorController _inputBufferRectWithinSensorCropRectForFrame:]
+ -[BWStillImageNodeConfiguration documentScanningEnabled]
+ -[BWStillImageNodeConfiguration setDocumentScanningEnabled:]
+ -[BWStillImageProcessingSettings documentScanning]
+ -[BWStillImageProcessingSettings setDocumentScanning:]
+ GCC_except_table128
+ GCC_except_table261
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table308
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table58
+ GCC_except_table91
+ _.compoundliteral.37
+ _.compoundliteral.40
+ _.compoundliteral.41
+ _.compoundliteral.43
+ _.compoundliteral.44
+ _.compoundliteral.52
+ _.compoundliteral.55
+ _.compoundliteral.81
+ _.compoundliteral.82
+ _.compoundliteral.83
+ _.compoundliteral.84
+ _.compoundliteral.85
+ _.compoundliteral.86
+ _.compoundliteral.87
+ _.compoundliteral.88
+ _BWDeepZoomTransferFusionHighResolutionWithZoomedImageUpperThreshold
+ _CMPhotoDetectCorruptionForSource
+ _FigCaptureIsCarryDevice
+ _FigCaptureIsCarryDevice.cold.1
+ _FigCaptureIsCarryDevice.onceToken
+ _FigCaptureIsCarryDevice.sIsCarryDevice
+ _FigCaptureMetadataUtilitiesRotationDegreesAndMirroredFromExifOrientation
+ _FigCaptureMetadataUtilitiesRotationDegreesAndMirroredFromExifOrientation.cold.1
+ _FigCaptureMetadataUtilitiesUpdateISPSpatialMetadataForStillImageCrop
+ _OBJC_IVAR_$_BWAudioConverterNode._expectsToRecordOnlyOnce
+ _OBJC_IVAR_$_BWAudioRemixAnalysisMetadataNode._expectsToRecordOnlyOnce
+ _OBJC_IVAR_$_BWPhotoEncoderControllerConfiguration._legacySensorOrientationRotationDegrees
+ _OBJC_IVAR_$_BWStillImageNodeConfiguration._documentScanningEnabled
+ _OBJC_IVAR_$_BWStillImageProcessingSettings._documentScanning
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.268
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.268.cold.1
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.288
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.315
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke_2.272
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke_2.316
+ ___65-[BWCaptureDeferredPhotoProcessor job:completedWithSampleBuffer:]_block_invoke_2
+ ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.228
+ ___FigCaptureIsCarryDevice_block_invoke
+ ___block_literal_global.153
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.291
+ ___block_literal_global.606
+ ___block_literal_global.612
+ ___block_literal_global.74
+ ___captureDeferredPhotoProcessor_CancelAllPrewarming_block_invoke.205
+ ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.187
+ ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.189
+ ___captureDeferredPhotoProcessor_workloop_block_invoke.178
+ ___captureSession_suspendTrueVideoVISProcessing_block_invoke
+ _captureSession_resumeTrueVideoVISProcessingForSemaphore
+ _captureSession_suspendTrueVideoVISProcessing
+ _kCMPhotoCompressionOption_DesiredImageOrientation
+ _kFigCaptureSampleBufferMetadata_SensorRawBufferCropRect
+ _kFigCaptureStillImageProcessingMetadataKey_DocumentScanning
+ _objc_msgSend$_addOrientationOptionsToDictionary:encodingScheme:metadata:allowSensorOrientationRotation:
+ _objc_msgSend$_addOrientationOptionsToDictionary:encodingScheme:orientation:allowSensorOrientationRotation:
+ _objc_msgSend$_desiredOrientationForOrientation:encodingScheme:
+ _objc_msgSend$_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:mainImageHandleInOut:
+ _objc_msgSend$_exifExtraRotationDegreesForEncodingScheme:
+ _objc_msgSend$_optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:containerOptionsOut:encodingOptionsOut:
+ _objc_msgSend$documentScanning
+ _objc_msgSend$initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:clientIsCameraOrDerivative:
+ _objc_msgSend$legacySensorOrientationRotationDegrees
+ _objc_msgSend$setDocumentScanning:
+ _objc_msgSend$setExpectsToRecordOnlyOnce:
- -[BWPhotoEncoderController _addOrientationOptionsToDictionary:encodingScheme:metadata:]
- -[BWPhotoEncoderController _addOrientationOptionsToDictionary:encodingScheme:orientation:]
- -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:]
- -[BWPhotoEncoderController _optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:containerOptionsOut:encodingOptionsOut:]
- -[BWPhotoEncoderNode initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:]
- -[BWSoftISPProcessorControllerConfiguration documentScanningEnabled]
- -[BWSoftISPProcessorControllerConfiguration setDocumentScanningEnabled:]
- GCC_except_table127
- GCC_except_table297
- GCC_except_table303
- GCC_except_table305
- GCC_except_table340
- GCC_except_table341
- GCC_except_table76
- GCC_except_table82
- GCC_except_table89
- _.compoundliteral.28
- _.compoundliteral.29
- _.compoundliteral.31
- _.compoundliteral.34
- _.compoundliteral.35
- _.compoundliteral.36
- _.compoundliteral.39
- _.compoundliteral.50
- _.compoundliteral.51
- _.compoundliteral.57
- _.compoundliteral.58
- _.compoundliteral.61
- _.compoundliteral.62
- _.compoundliteral.63
- _.compoundliteral.64
- _OBJC_IVAR_$_BWMetadataSynchronizerNode._numEODMessagesReceived
- _OBJC_IVAR_$_BWSoftISPProcessorControllerConfiguration._documentScanningEnabled
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.263
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.263.cold.1
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.283
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.310
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke_2.267
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke_2.311
- ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.222
- ___block_descriptor_84_e8_32o40o48o56o64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.142
- ___block_literal_global.174
- ___block_literal_global.212
- ___block_literal_global.214
- ___block_literal_global.258
- ___block_literal_global.290
- ___block_literal_global.601
- ___block_literal_global.604
- ___captureDeferredPhotoProcessor_CancelAllPrewarming_block_invoke.197
- ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.179
- ___captureDeferredPhotoProcessor_ProcessPhoto_block_invoke.181
- ___captureDeferredPhotoProcessor_workloop_block_invoke.170
- _objc_msgSend$_addOrientationOptionsToDictionary:encodingScheme:metadata:
- _objc_msgSend$_addOrientationOptionsToDictionary:encodingScheme:orientation:
- _objc_msgSend$_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:
- _objc_msgSend$_optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:containerOptionsOut:encodingOptionsOut:
- _objc_msgSend$initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:
CStrings:
+ "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@%@%@%@%@"
+ "-[BWAudioConverterNode _handleUpdatedRecordingSettings:]"
+ "-[BWAudioRemixAnalysisMetadataNode renderSampleBuffer:forInput:]"
+ "-[BWCaptureDeferredPhotoProcessor _runImageCorruptionDetectionForJob:onEncodedSurface:surfaceSize:]"
+ "-[BWPhotoEncoderController _desiredOrientationForOrientation:encodingScheme:]"
+ "-[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:mainImageHandleInOut:]"
+ "-[BWPreviewStitcherNode _newStitchedSampleBufferFromWiderCamera:narrowerCamera:widerCameraRegionsShifts:teleShift:primaryCaptureRectOut:primaryCaptureRectBeforeCroppingOut:centerWiderCameraShiftOut:currentFrameRate:inputCropRectOut:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
+ "23:29:57"
+ "<%@ %p>: %@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "<<<< BWAudioConverterNode >>>> %s: %{public}@: nil _audioCompressionSBP while receiving recording settings with _expectsToRecordOnlyOnce is YES, creating _audioCompressionSBP now"
+ "<<<< BWAudioRemixAnalysisMetadataNode >>>> %s: %{public}@: _movieRemixSessionManager not ready when receiving start maker and _expectsToRecordOnlyOnce is YES, calling -startNewSessionBlocking now"
+ "<<<< BWFileCoordinatorNode >>>> %s: resuming from paused failed for captureID:%lld, telling file writer to resume and then we will stop"
+ "<<<< BWFileCoordinatorNode >>>> %s: telling delegate that we are stopping before starting"
+ "<<<< BWPixelTransferNode >>>> %s: %{public}@"
+ "<<<< BWPixelTransferNode >>>> %s: %{public}@%{public}@"
+ "<<<< BWPreviewStitcherNode >>>> %s: Dropping preview frame due to stitcher dynamic range mismatch"
+ "<<<< BWStillImageProcessing >>>> %s: Skip piecemeal encoding for attachedMediaKey %{public}@ as input is ready for processing"
+ "<<<< BWStillImageProcessing >>>> %s: called for {%{public}@} with captureID:%{public}lld sbuf:%{public}@ %{private}@"
+ "<<<< BWStillImageProcessing >>>> %s: orientation[%{public}d] -> desiredOrientation[%{public}d] for: mirrored:%{public}d, exifExtraRotationDegrees: %{public}dº, encodingScheme: %{public}@"
+ "<<<< BWSynchronizerNode >>>> %s: [Pro Video] Unexpected timescale"
+ "<<<< FigCaptureDeferredPhotoProcessor >>>> %s: %{public}@ took %.2fms"
+ "<<<< FigCaptureDeferredPhotoProcessor >>>> %s: Image corruption detected on identifier: %{public}@ for captureID:%lld"
+ "<<<< FigCaptureOSStateHandle >>>> %s: <%p[%{public}@]> %{public}@"
+ "<<<< FigCaptureOSStateHandle >>>> %s: <%p[%{public}@]> %{public}@%{public}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ %{public}@%{public}@"
+ "<<<< FigCaptureSession >>>> %s: Releasing visProcessingSemaphore (didn't wait)"
+ "<<<< FigCaptureSession >>>> %s: Signalling and releasing visProcessingSemaphore"
+ "<<<< FigCaptureSession >>>> %s: Waiting on visProcessingSemaphore"
+ "@60@0:8@16@24i32@36B44i48B52B56"
+ "Aug  5 2025"
+ "Detecting image corruption"
+ "ExperimentGroup"
+ "FigCaptureVideoDimensionsAreValid( sourceDimensions )"
+ "InputBufferRectWithinSensorCropRect"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:12539"
+ "LastShownBuild:BWPhotoEncoderController.m:1035"
+ "LastShownBuild:BWPhotoEncoderController.m:1038"
+ "LastShownBuild:BWPhotoEncoderController.m:1407"
+ "LastShownBuild:BWPhotoEncoderController.m:1412"
+ "LastShownBuild:BWPhotoEncoderController.m:1639"
+ "LastShownBuild:BWPhotoEncoderController.m:1760"
+ "LastShownBuild:BWPhotoEncoderController.m:1776"
+ "LastShownBuild:BWPhotoEncoderController.m:1786"
+ "LastShownBuild:BWPhotoEncoderController.m:3477"
+ "LastShownBuild:BWPhotoEncoderController.m:4167"
+ "LastShownBuild:BWPhotoEncoderController.m:5528"
+ "LastShownBuild:BWPhotoEncoderNode.m:361"
+ "LastShownBuild:BWPhotoEncoderNode.m:363"
+ "LastShownBuild:BWPhotonicEngineNode.m:3262"
+ "LastShownBuild:BWPhotonicEngineNode.m:3277"
+ "LastShownBuild:BWPhotonicEngineNode.m:3388"
+ "LastShownBuild:BWPhotonicEngineNode.m:3412"
+ "LastShownBuild:BWPhotonicEngineNode.m:4450"
+ "LastShownBuild:BWPhotonicEngineNode.m:5146"
+ "LastShownBuild:BWPhotonicEngineNode.m:5164"
+ "LastShownBuild:BWPhotonicEngineNode.m:7102"
+ "LastShownBuild:BWPhotonicEngineNode.m:8547"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3405"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1004"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1263"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1270"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1276"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1294"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1971"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2001"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:634"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:775"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:947"
+ "LastShownBuild:BWSynchronizerNode.m:558"
+ "LastShownBuild:BWVISNode.m:2275"
+ "LastShownBuild:BWVISNode.m:2293"
+ "LastShownBuild:BWVISNode.m:423"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1359"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:5652"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1454"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1460"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1461"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1465"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1581"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1587"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1590"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1751"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2729"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2815"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2816"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2988"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2991"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3162"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3165"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3210"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4165"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4171"
+ "LastShownBuild:FigCaptureSession.m:10343"
+ "LastShownBuild:FigCaptureSession.m:10498"
+ "LastShownBuild:FigCaptureSession.m:17953"
+ "LastShownBuild:FigCaptureSession.m:17956"
+ "LastShownBuild:FigCaptureSession.m:18795"
+ "LastShownBuild:FigCaptureSession.m:22276"
+ "LastShownBuild:FigCaptureSession.m:22311"
+ "LastShownBuild:FigCaptureSession.m:24559"
+ "LastShownBuild:FigCaptureSession.m:4195"
+ "LastShownBuild:FigCaptureSession.m:8521"
+ "LastShownBuild:FigCaptureSession.m:8527"
+ "LastShownBuild:FigCaptureSession.m:8530"
+ "LastShownBuild:FigCaptureSession.m:8533"
+ "LastShownBuild:FigCaptureSession.m:8536"
+ "LastShownBuild:FigCaptureSession.m:8547"
+ "LastShownBuild:FigCaptureSession.m:8550"
+ "LastShownBuild:FigCaptureSession.m:8558"
+ "LastShownBuild:FigCaptureSession.m:8576"
+ "LastShownBuild:FigCaptureSession.m:8621"
+ "LastShownBuild:FigCaptureSession.m:8625"
+ "LastShownBuild:FigCaptureSession.m:8649"
+ "LastShownBuild:FigCaptureSession.m:8664"
+ "LastShownBuild:FigCaptureSession.m:8668"
+ "LastShownBuild:FigCaptureSession.m:8671"
+ "LastShownBuild:FigCaptureSession.m:8786"
+ "LastShownBuild:FigCaptureSession.m:8792"
+ "LastShownBuild:FigCaptureSession.m:8820"
+ "LastShownBuild:FigCaptureSession.m:8834"
+ "LastShownBuild:FigCaptureSession.m:9249"
+ "LastShownBuild:FigCaptureSession.m:9516"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:12539"
+ "LastShownDate:BWPhotoEncoderController.m:1035"
+ "LastShownDate:BWPhotoEncoderController.m:1038"
+ "LastShownDate:BWPhotoEncoderController.m:1407"
+ "LastShownDate:BWPhotoEncoderController.m:1412"
+ "LastShownDate:BWPhotoEncoderController.m:1639"
+ "LastShownDate:BWPhotoEncoderController.m:1760"
+ "LastShownDate:BWPhotoEncoderController.m:1776"
+ "LastShownDate:BWPhotoEncoderController.m:1786"
+ "LastShownDate:BWPhotoEncoderController.m:3477"
+ "LastShownDate:BWPhotoEncoderController.m:4167"
+ "LastShownDate:BWPhotoEncoderController.m:5528"
+ "LastShownDate:BWPhotoEncoderNode.m:361"
+ "LastShownDate:BWPhotoEncoderNode.m:363"
+ "LastShownDate:BWPhotonicEngineNode.m:3262"
+ "LastShownDate:BWPhotonicEngineNode.m:3277"
+ "LastShownDate:BWPhotonicEngineNode.m:3388"
+ "LastShownDate:BWPhotonicEngineNode.m:3412"
+ "LastShownDate:BWPhotonicEngineNode.m:4450"
+ "LastShownDate:BWPhotonicEngineNode.m:5146"
+ "LastShownDate:BWPhotonicEngineNode.m:5164"
+ "LastShownDate:BWPhotonicEngineNode.m:7102"
+ "LastShownDate:BWPhotonicEngineNode.m:8547"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3405"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1004"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1263"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1270"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1276"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1294"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1971"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2001"
+ "LastShownDate:BWStillImageMetadataUtilities.m:634"
+ "LastShownDate:BWStillImageMetadataUtilities.m:775"
+ "LastShownDate:BWStillImageMetadataUtilities.m:947"
+ "LastShownDate:BWSynchronizerNode.m:558"
+ "LastShownDate:BWVISNode.m:2275"
+ "LastShownDate:BWVISNode.m:2293"
+ "LastShownDate:BWVISNode.m:423"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1359"
+ "LastShownDate:FigCaptureMetadataUtilities.m:5652"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1454"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1460"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1461"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1465"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1581"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1587"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1590"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1751"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2729"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2815"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2816"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2988"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2991"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3162"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3165"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3210"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4165"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4171"
+ "LastShownDate:FigCaptureSession.m:10343"
+ "LastShownDate:FigCaptureSession.m:10498"
+ "LastShownDate:FigCaptureSession.m:17953"
+ "LastShownDate:FigCaptureSession.m:17956"
+ "LastShownDate:FigCaptureSession.m:18795"
+ "LastShownDate:FigCaptureSession.m:22276"
+ "LastShownDate:FigCaptureSession.m:22311"
+ "LastShownDate:FigCaptureSession.m:24559"
+ "LastShownDate:FigCaptureSession.m:4195"
+ "LastShownDate:FigCaptureSession.m:8521"
+ "LastShownDate:FigCaptureSession.m:8527"
+ "LastShownDate:FigCaptureSession.m:8530"
+ "LastShownDate:FigCaptureSession.m:8533"
+ "LastShownDate:FigCaptureSession.m:8536"
+ "LastShownDate:FigCaptureSession.m:8547"
+ "LastShownDate:FigCaptureSession.m:8550"
+ "LastShownDate:FigCaptureSession.m:8558"
+ "LastShownDate:FigCaptureSession.m:8576"
+ "LastShownDate:FigCaptureSession.m:8621"
+ "LastShownDate:FigCaptureSession.m:8625"
+ "LastShownDate:FigCaptureSession.m:8649"
+ "LastShownDate:FigCaptureSession.m:8664"
+ "LastShownDate:FigCaptureSession.m:8668"
+ "LastShownDate:FigCaptureSession.m:8671"
+ "LastShownDate:FigCaptureSession.m:8786"
+ "LastShownDate:FigCaptureSession.m:8792"
+ "LastShownDate:FigCaptureSession.m:8820"
+ "LastShownDate:FigCaptureSession.m:8834"
+ "LastShownDate:FigCaptureSession.m:9249"
+ "LastShownDate:FigCaptureSession.m:9516"
+ "TB,N,V_documentScanning"
+ "TB,N,V_expectsToRecordOnlyOnce"
+ "Ti,N,V_legacySensorOrientationRotationDegrees"
+ "[Pro Video] Unexpected timescale"
+ "_addOrientationOptionsToDictionary:encodingScheme:metadata:allowSensorOrientationRotation:"
+ "_addOrientationOptionsToDictionary:encodingScheme:orientation:allowSensorOrientationRotation:"
+ "_desiredOrientationForOrientation:encodingScheme:"
+ "_documentScanning"
+ "_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:mainImageHandleInOut:"
+ "_exifExtraRotationDegreesForEncodingScheme:"
+ "_expectsToRecordOnlyOnce"
+ "_legacySensorOrientationRotationDegrees"
+ "_optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:allowSensorOrientationRotation:containerOptionsOut:encodingOptionsOut:"
+ "c:%d, r:%d, h:%d, sh:%d auo:%d m:%d, x:%d, a:%d, apr:%d, l:%d, lh:%d, s:%d, g:%d, v:%d, t:%d, aux:%@ isr:%@, osr:%@, asr:%@"
+ "captureSession_resumeTrueVideoVISProcessingForSemaphore"
+ "captureSession_suspendTrueVideoVISProcessing"
+ "carry"
+ "com.apple.MailCompositionService"
+ "com.apple.da"
+ "description=CameraCapture-664.2.5"
+ "documentScanning"
+ "expectsToRecordOnlyOnce"
+ "history {%lld/%d} and _quantizationFrameDuration {%lld/%d} don't have matching timescale"
+ "i120@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104B108^q112"
+ "i128@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104B108^@112^@120"
+ "i24@0:8i16i20"
+ "initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:clientIsCameraOrDerivative:"
+ "legacySensorOrientationRotationDegrees"
+ "setDocumentScanning:"
+ "setExpectsToRecordOnlyOnce:"
+ "setLegacySensorOrientationRotationDegrees:"
+ "v36@0:8@16i24i28B32"
+ "v40@0:8@16i24@28B36"
- "%@ movies:%d, suspended:%d, preserveSuspended:%d, movieDur:%.2fs, trim:%d, %lldfps, preparedID:%lld%@%@%@%@%@%@ maxQuality:%d%@%@%@%@%@%@%@%@%@%@"
- "-[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:]"
- "19:06:32"
- "<%@ %p>: %@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "<<<< BWPixelTransferNode >>>> %s: %@"
- "<<<< BWPixelTransferNode >>>> %s: %@%@"
- "<<<< BWStillImageProcessing >>>> %s: called for {%{private}@} captureID:%{public}lld %{private}@"
- "<<<< FigCaptureOSStateHandle >>>> %s: <%p[%{public}@]> %@"
- "<<<< FigCaptureOSStateHandle >>>> %s: <%p[%{public}@]> %@%@"
- "<<<< FigCaptureSession >>>> %s: %{public}@ %@"
- "<<<< FigCaptureSession >>>> %s: %{public}@ %@%@"
- "@56@0:8@16@24i32@36B44i48B52"
- "Jul 26 2025"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:12507"
- "LastShownBuild:BWPhotoEncoderController.m:1021"
- "LastShownBuild:BWPhotoEncoderController.m:1024"
- "LastShownBuild:BWPhotoEncoderController.m:1393"
- "LastShownBuild:BWPhotoEncoderController.m:1398"
- "LastShownBuild:BWPhotoEncoderController.m:1625"
- "LastShownBuild:BWPhotoEncoderController.m:1746"
- "LastShownBuild:BWPhotoEncoderController.m:1762"
- "LastShownBuild:BWPhotoEncoderController.m:1772"
- "LastShownBuild:BWPhotoEncoderController.m:3410"
- "LastShownBuild:BWPhotoEncoderController.m:4092"
- "LastShownBuild:BWPhotoEncoderController.m:5450"
- "LastShownBuild:BWPhotoEncoderNode.m:355"
- "LastShownBuild:BWPhotoEncoderNode.m:357"
- "LastShownBuild:BWPhotonicEngineNode.m:3260"
- "LastShownBuild:BWPhotonicEngineNode.m:3275"
- "LastShownBuild:BWPhotonicEngineNode.m:3386"
- "LastShownBuild:BWPhotonicEngineNode.m:3410"
- "LastShownBuild:BWPhotonicEngineNode.m:4448"
- "LastShownBuild:BWPhotonicEngineNode.m:5144"
- "LastShownBuild:BWPhotonicEngineNode.m:5162"
- "LastShownBuild:BWPhotonicEngineNode.m:7098"
- "LastShownBuild:BWPhotonicEngineNode.m:8541"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3403"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1000"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1259"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1266"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1272"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1290"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1967"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1997"
- "LastShownBuild:BWStillImageMetadataUtilities.m:630"
- "LastShownBuild:BWStillImageMetadataUtilities.m:771"
- "LastShownBuild:BWStillImageMetadataUtilities.m:943"
- "LastShownBuild:BWVISNode.m:2273"
- "LastShownBuild:BWVISNode.m:2291"
- "LastShownBuild:BWVISNode.m:422"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1358"
- "LastShownBuild:FigCaptureMetadataUtilities.m:5613"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1441"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1447"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1448"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1452"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1568"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1574"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1577"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1738"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2716"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2802"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2803"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2975"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2978"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3149"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3152"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3197"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4151"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4157"
- "LastShownBuild:FigCaptureSession.m:10038"
- "LastShownBuild:FigCaptureSession.m:17420"
- "LastShownBuild:FigCaptureSession.m:17423"
- "LastShownBuild:FigCaptureSession.m:18263"
- "LastShownBuild:FigCaptureSession.m:21704"
- "LastShownBuild:FigCaptureSession.m:21739"
- "LastShownBuild:FigCaptureSession.m:23967"
- "LastShownBuild:FigCaptureSession.m:4186"
- "LastShownBuild:FigCaptureSession.m:8118"
- "LastShownBuild:FigCaptureSession.m:8124"
- "LastShownBuild:FigCaptureSession.m:8127"
- "LastShownBuild:FigCaptureSession.m:8130"
- "LastShownBuild:FigCaptureSession.m:8133"
- "LastShownBuild:FigCaptureSession.m:8144"
- "LastShownBuild:FigCaptureSession.m:8147"
- "LastShownBuild:FigCaptureSession.m:8155"
- "LastShownBuild:FigCaptureSession.m:8173"
- "LastShownBuild:FigCaptureSession.m:8218"
- "LastShownBuild:FigCaptureSession.m:8222"
- "LastShownBuild:FigCaptureSession.m:8246"
- "LastShownBuild:FigCaptureSession.m:8261"
- "LastShownBuild:FigCaptureSession.m:8265"
- "LastShownBuild:FigCaptureSession.m:8268"
- "LastShownBuild:FigCaptureSession.m:8362"
- "LastShownBuild:FigCaptureSession.m:8367"
- "LastShownBuild:FigCaptureSession.m:8375"
- "LastShownBuild:FigCaptureSession.m:8379"
- "LastShownBuild:FigCaptureSession.m:8790"
- "LastShownBuild:FigCaptureSession.m:9057"
- "LastShownBuild:FigCaptureSession.m:9883"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:12507"
- "LastShownDate:BWPhotoEncoderController.m:1021"
- "LastShownDate:BWPhotoEncoderController.m:1024"
- "LastShownDate:BWPhotoEncoderController.m:1393"
- "LastShownDate:BWPhotoEncoderController.m:1398"
- "LastShownDate:BWPhotoEncoderController.m:1625"
- "LastShownDate:BWPhotoEncoderController.m:1746"
- "LastShownDate:BWPhotoEncoderController.m:1762"
- "LastShownDate:BWPhotoEncoderController.m:1772"
- "LastShownDate:BWPhotoEncoderController.m:3410"
- "LastShownDate:BWPhotoEncoderController.m:4092"
- "LastShownDate:BWPhotoEncoderController.m:5450"
- "LastShownDate:BWPhotoEncoderNode.m:355"
- "LastShownDate:BWPhotoEncoderNode.m:357"
- "LastShownDate:BWPhotonicEngineNode.m:3260"
- "LastShownDate:BWPhotonicEngineNode.m:3275"
- "LastShownDate:BWPhotonicEngineNode.m:3386"
- "LastShownDate:BWPhotonicEngineNode.m:3410"
- "LastShownDate:BWPhotonicEngineNode.m:4448"
- "LastShownDate:BWPhotonicEngineNode.m:5144"
- "LastShownDate:BWPhotonicEngineNode.m:5162"
- "LastShownDate:BWPhotonicEngineNode.m:7098"
- "LastShownDate:BWPhotonicEngineNode.m:8541"
- "LastShownDate:BWStillImageCoordinatorNode.m:3403"
- "LastShownDate:BWStillImageMetadataUtilities.m:1000"
- "LastShownDate:BWStillImageMetadataUtilities.m:1259"
- "LastShownDate:BWStillImageMetadataUtilities.m:1266"
- "LastShownDate:BWStillImageMetadataUtilities.m:1272"
- "LastShownDate:BWStillImageMetadataUtilities.m:1290"
- "LastShownDate:BWStillImageMetadataUtilities.m:1967"
- "LastShownDate:BWStillImageMetadataUtilities.m:1997"
- "LastShownDate:BWStillImageMetadataUtilities.m:630"
- "LastShownDate:BWStillImageMetadataUtilities.m:771"
- "LastShownDate:BWStillImageMetadataUtilities.m:943"
- "LastShownDate:BWVISNode.m:2273"
- "LastShownDate:BWVISNode.m:2291"
- "LastShownDate:BWVISNode.m:422"
- "LastShownDate:FigCaptureMetadataUtilities.m:1358"
- "LastShownDate:FigCaptureMetadataUtilities.m:5613"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1441"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1447"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1448"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1452"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1568"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1574"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1577"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1738"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2716"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2802"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2803"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2975"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2978"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3149"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3152"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3197"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4151"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4157"
- "LastShownDate:FigCaptureSession.m:10038"
- "LastShownDate:FigCaptureSession.m:17420"
- "LastShownDate:FigCaptureSession.m:17423"
- "LastShownDate:FigCaptureSession.m:18263"
- "LastShownDate:FigCaptureSession.m:21704"
- "LastShownDate:FigCaptureSession.m:21739"
- "LastShownDate:FigCaptureSession.m:23967"
- "LastShownDate:FigCaptureSession.m:4186"
- "LastShownDate:FigCaptureSession.m:8118"
- "LastShownDate:FigCaptureSession.m:8124"
- "LastShownDate:FigCaptureSession.m:8127"
- "LastShownDate:FigCaptureSession.m:8130"
- "LastShownDate:FigCaptureSession.m:8133"
- "LastShownDate:FigCaptureSession.m:8144"
- "LastShownDate:FigCaptureSession.m:8147"
- "LastShownDate:FigCaptureSession.m:8155"
- "LastShownDate:FigCaptureSession.m:8173"
- "LastShownDate:FigCaptureSession.m:8218"
- "LastShownDate:FigCaptureSession.m:8222"
- "LastShownDate:FigCaptureSession.m:8246"
- "LastShownDate:FigCaptureSession.m:8261"
- "LastShownDate:FigCaptureSession.m:8265"
- "LastShownDate:FigCaptureSession.m:8268"
- "LastShownDate:FigCaptureSession.m:8362"
- "LastShownDate:FigCaptureSession.m:8367"
- "LastShownDate:FigCaptureSession.m:8375"
- "LastShownDate:FigCaptureSession.m:8379"
- "LastShownDate:FigCaptureSession.m:8790"
- "LastShownDate:FigCaptureSession.m:9057"
- "LastShownDate:FigCaptureSession.m:9883"
- "_addOrientationOptionsToDictionary:encodingScheme:metadata:"
- "_addOrientationOptionsToDictionary:encodingScheme:orientation:"
- "_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:"
- "_optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:containerOptionsOut:encodingOptionsOut:"
- "c:%d, r:%d, h:%d, sh:%d auo:%d m:%d, x:%d, a:%d, apr:%d, l:%d, lh:%d, s:%d, g:%d, v:%d, t:%d, aux:%@ osr:%@, asr:%@"
- "description=CameraCapture-664.0.0.0.2"
- "i116@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104^q108"
- "i124@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104^@108^@116"
- "initWithNodeConfiguration:sensorConfigurationsByPortType:semanticDevelopmentVersion:inferenceScheduler:alwaysAwaitInference:portraitRenderQuality:deferredPhotoProcessorEnabled:"

```
