## AppleDepth

> `/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth`

```diff

-137.3.0.0.0
-  __TEXT.__text: 0xa5ac4
-  __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x479c
-  __TEXT.__const: 0x11e0
-  __TEXT.__gcc_except_tab: 0xb808
-  __TEXT.__oslogstring: 0x532a
-  __TEXT.__cstring: 0x4524
-  __TEXT.__unwind_info: 0x25d0
-  __TEXT.__objc_classname: 0x8efe
-  __TEXT.__objc_methname: 0xdf94
-  __TEXT.__objc_methtype: 0x4199
-  __TEXT.__objc_stubs: 0x7160
-  __DATA_CONST.__got: 0x640
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x3b0
+148.0.0.0.0
+  __TEXT.__text: 0x1016b4
+  __TEXT.__auth_stubs: 0x1490
+  __TEXT.__objc_methlist: 0x6f34
+  __TEXT.__const: 0x14c0
+  __TEXT.__gcc_except_tab: 0x1223c
+  __TEXT.__oslogstring: 0x8f51
+  __TEXT.__cstring: 0x77b5
+  __TEXT.__unwind_info: 0x39b0
+  __TEXT.__objc_classname: 0x948d
+  __TEXT.__objc_methname: 0x1738a
+  __TEXT.__objc_methtype: 0x7c3d
+  __TEXT.__objc_stubs: 0xaa00
+  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__const: 0x320
+  __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c8
-  __DATA_CONST.__objc_superrefs: 0x320
-  __DATA_CONST.__objc_arraydata: 0x150
-  __AUTH_CONST.__auth_got: 0x9e0
-  __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x4660
-  __AUTH_CONST.__objc_const: 0xbff0
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xb70
-  __DATA.__data: 0xe83c8
-  __DATA.__bss: 0x161
+  __DATA_CONST.__objc_selrefs: 0x3738
+  __DATA_CONST.__objc_superrefs: 0x458
+  __DATA_CONST.__objc_arraydata: 0x180
+  __AUTH_CONST.__auth_got: 0xa58
+  __AUTH_CONST.__const: 0xa68
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x11e80
+  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__objc_floatobj: 0x30
+  __AUTH_CONST.__objc_doubleobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x115c
+  __DATA.__data: 0xe85f8
+  __DATA.__bss: 0x4d1
   __DATA_DIRTY.__objc_data: 0x2440
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D46CADCF-F054-3BB5-87D8-763C6FBBF745
-  Functions: 1877
-  Symbols:   7400
-  CStrings:  4298
+  UUID: 83E616E1-80F6-3740-9590-448D1DCF388E
+  Functions: 3067
+  Symbols:   11406
+  CStrings:  6438
 
Symbols:
+ +[ADBinocularDepthOutput outputWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:]
+ +[ADBinocularDepthWarperMesh rectifyCameraPairForLeftCalib:rightCalib:leftRectifiedCameraToPlatformTransform:rightRectifiedCameraToPlatformTransform:prioritization:]
+ +[ADBinocularDepthWarperMesh skew:]
+ +[ADBinocularDepthWarperMesh updateWarper:source:target:]
+ +[ADDeviceConfiguration getRealDeviceName]
+ +[ADDeviceConfiguration hasLidarToColorIncreasedBaseline:]
+ +[ADDeviceConfiguration preferencesWithDefaultValues:]
+ +[ADJasperColorExecutor defaults]
+ +[ADJasperColorInFieldCalibrationControllerParameters defaults]
+ +[ADJasperColorInFieldCalibrationExecutor defaults]
+ +[ADJasperColorInFieldCalibrationInterSessionData defaults]
+ +[ADJasperColorInFieldCalibrationPipelineParameters defaults]
+ +[ADJasperPearlInFieldCalibrationTelemetry reportTelemetry:firstTimeEvent:]
+ +[ADJasperPearlInFieldCalibrationTelemetry reportTriggeringTelemetry:]
+ +[ADLKTOpticalFlow highPerformanceConfig]
+ +[ADLKTOpticalFlow highQualityConfig]
+ +[ADLogManager defaults]
+ +[ADMetalUtils textureForSize:pixelFormat:mipmapped:metalDevice:]
+ +[ADMetricDepthExecutor defaults]
+ +[ADMetricDepthPipeline defaults]
+ +[ADMetricDepthPipelineParameters defaults]
+ +[ADNetworkProvider createRequestedLayoutsForDimensions:]
+ +[ADNetworkProvider createRequestedLayoutsForDimensions:function:]
+ +[ADNetworkProvider createRequestedLayoutsForDimensions:layout:function:]
+ +[ADNetworkProvider nonRunnableProviderForNetwork:]
+ +[ADNetworkProvider nonRunnableProviderForNetwork:espressoEngine:]
+ +[ADNetworkProvider nonRunnableProviderForNetwork:requestedLayouts:]
+ +[ADNetworkProvider providerForNetwork:requestedLayouts:espressoEngine:makeRunnable:]
+ +[ADNetworkProvider providerForNetwork:requestedLayouts:makeRunnable:]
+ +[ADPearlColorInFieldCalibrationInterSessionData defaults]
+ +[ADPearlColorInFieldCalibrationPipeline defaults]
+ +[ADPearlColorInFieldCalibrationPipelineParameters defaults]
+ +[ADUtils fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:alpha:confidenceUnits:]
+ +[ADUtils pixelBufferFromData:width:height:pixelFormat:]
+ +[ADUtils pixelBufferToData:]
+ +[ADUtils warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingOpticalFlow:]
+ +[ADVisualDepthBuffer inputWithImage:confidence:calibration:]
+ +[ADVisualDepthBuffer inputWithImage:confidence:calibration:uuid:]
+ +[ADVisualDepthBuffer inputWithImage:confidence:labels:normals:calibration:uuid:pose:timestamp:]
+ +[ADVisualDepthMeshChunk meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:]
+ +[ADVisualDepthMeshChunk meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:]
+ +[ADVisualDepthMeshChunk meshChunkWithVertices:faces:confidence:classification:uuid:timestamp:]
+ +[ADVisualDepthMeshChunk meshChunkWithVertices:faces:confidence:classification:uuid:timestamp:longRange:]
+ +[ADVisualDepthMeshChunk meshChunkWithVerticesBuffer:verticesCount:verticesOffset:verticesStride:facesBuffer:facesCount:facesOffset:facesStride:uuid:timestamp:]
+ +[ADVisualDepthMeshChunk removedMeshChunkWithUuid:timestamp:]
+ +[ADVisualDepthMeshChunk removedMeshChunkWithUuid:timestamp:longRange:]
+ +[ADVisualDepthOutput outputWithDepthForPrimaryPoV:depthForSecondaryPoV:]
+ +[ADVisualDepthOutput outputWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:]
+ +[ADVisualDepthPipeline defaults]
+ +[ADVisualDepthPipeline povcDimensions]
+ +[ADVisualDepthPipeline predictsDisparity]
+ -[ADBinocularDepthExecutor .cxx_destruct]
+ -[ADBinocularDepthExecutor allocateIntermediateBuffers]
+ -[ADBinocularDepthExecutor computeCropForRectifiedImage:calib:]
+ -[ADBinocularDepthExecutor dealloc]
+ -[ADBinocularDepthExecutor deallocateEspressoBuffers]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:auxOutputDepth:auxOutputConfidence:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:auxOutputDepth:auxOutputConfidence:timestamp:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputCalib:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputCalib:timestamp:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputSegmentation:auxOutputCalib:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputSegmentation:auxOutputCalib:timestamp:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:timestamp:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:refCalib:auxCalib:timestamp:]
+ -[ADBinocularDepthExecutor executeWithRefColor:auxColor:timestamp:]
+ -[ADBinocularDepthExecutor getIntermediates]
+ -[ADBinocularDepthExecutor getRectifiedColorInputSaturationRate]
+ -[ADBinocularDepthExecutor initForEspressoEngine:]
+ -[ADBinocularDepthExecutor initWithPrioritization:espressoEngine:]
+ -[ADBinocularDepthExecutor numberOfExecutionSteps]
+ -[ADBinocularDepthExecutor pipeline]
+ -[ADBinocularDepthExecutor prepareForInputRoi:]
+ -[ADBinocularDepthExecutor sendAnalyticsWithRefSaturationRate:auxSaturationRate:]
+ -[ADBinocularDepthExecutor setColorInput:calib:toNetworkBuffer:isRef:crop:]
+ -[ADBinocularDepthExecutorParameters .cxx_destruct]
+ -[ADBinocularDepthExecutorParameters coreAnalyticsEventInterval]
+ -[ADBinocularDepthExecutorParameters initForPipeline:]
+ -[ADBinocularDepthExecutorParameters pipelineParameters]
+ -[ADBinocularDepthExecutorParameters saturationCheckInterval]
+ -[ADBinocularDepthExecutorParameters saturationThreshold]
+ -[ADBinocularDepthExecutorParameters setCoreAnalyticsEventInterval:]
+ -[ADBinocularDepthExecutorParameters setSaturationCheckInterval:]
+ -[ADBinocularDepthExecutorParameters setSaturationThreshold:]
+ -[ADBinocularDepthFlow .cxx_destruct]
+ -[ADBinocularDepthFlow executor]
+ -[ADBinocularDepthFlow initWithExecutor:]
+ -[ADBinocularDepthFlow processIfMatch:]
+ -[ADBinocularDepthFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADBinocularDepthFlow pushSecondaryColor:pose:calibration:timestamp:]
+ -[ADBinocularDepthOutput .cxx_destruct]
+ -[ADBinocularDepthOutput auxConfidence]
+ -[ADBinocularDepthOutput auxDepth]
+ -[ADBinocularDepthOutput auxOutputCalibration]
+ -[ADBinocularDepthOutput auxSegmentation]
+ -[ADBinocularDepthOutput dealloc]
+ -[ADBinocularDepthOutput initWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:]
+ -[ADBinocularDepthPipeline .cxx_destruct]
+ -[ADBinocularDepthPipeline auxOutputCalib]
+ -[ADBinocularDepthPipeline auxRectifiedCalib]
+ -[ADBinocularDepthPipeline extractYChannelFromColorInput:toBuffer:]
+ -[ADBinocularDepthPipeline inferenceDescriptor]
+ -[ADBinocularDepthPipeline initForEspressoEngine:]
+ -[ADBinocularDepthPipeline initWithPrioritization:espressoEngine:]
+ -[ADBinocularDepthPipeline pipelineParameters]
+ -[ADBinocularDepthPipeline postProcessDisparity:outputDepth:]
+ -[ADBinocularDepthPipeline postProcessEspressoConfidence:outputConfidence:]
+ -[ADBinocularDepthPipeline postProcessEspressoConfidence:outputConfidence:confidenceUnits:]
+ -[ADBinocularDepthPipeline prepareStereoWarpMeshesWithRefCalib:auxCalib:]
+ -[ADBinocularDepthPipeline refRectifiedCalib]
+ -[ADBinocularDepthPipeline setPipelineParameters:]
+ -[ADBinocularDepthPipeline warpImage:processedImage:isRef:]
+ -[ADBinocularDepthPipelineParameters confidenceUnits]
+ -[ADBinocularDepthPipelineParameters init]
+ -[ADBinocularDepthPipelineParameters rectifiedCameraFieldOfViewHeight]
+ -[ADBinocularDepthPipelineParameters rectifiedCameraFieldOfViewWidth]
+ -[ADBinocularDepthPipelineParameters setConfidenceUnits:]
+ -[ADBinocularDepthPipelineParameters setRectifiedCameraFieldOfViewHeight:]
+ -[ADBinocularDepthPipelineParameters setRectifiedCameraFieldOfViewWidth:]
+ -[ADBinocularDepthWarperMesh deallocMemory]
+ -[ADBinocularDepthWarperMesh dealloc]
+ -[ADBinocularDepthWarperMesh init]
+ -[ADBinocularDepthWarperMesh undistortColorImage:undistortedImage:]
+ -[ADBinocularDepthWarperMesh updateWithSource:target:]
+ -[ADConfidenceLevelRanges description]
+ -[ADDensifiedLiDARFocusAssistExecutor colorRoi]
+ -[ADDensifiedLiDARFocusAssistExecutor executeWithColor:timestamp:pointClouds:lidarCalibration:colorMetadata:colorCameraCalibration:outputDepthMap:outputConfidenceMap:outputCalibration:]
+ -[ADDensifiedLiDARFocusAssistExecutor initWithParameters:]
+ -[ADDensifiedLiDARFocusAssistExecutor validDepthRect]
+ -[ADDensifiedLiDARFocusAssistExecutorParameters autoSetColorROI]
+ -[ADDensifiedLiDARFocusAssistExecutorParameters initWithPipelineParameters:]
+ -[ADDensifiedLiDARFocusAssistExecutorParameters init]
+ -[ADDensifiedLiDARFocusAssistExecutorParameters setAutoSetColorROI:]
+ -[ADDensifiedLiDARFocusAssistFlow .cxx_destruct]
+ -[ADDensifiedLiDARFocusAssistFlow delegate]
+ -[ADDensifiedLiDARFocusAssistFlow executor]
+ -[ADDensifiedLiDARFocusAssistFlow handleMatch:]
+ -[ADDensifiedLiDARFocusAssistFlow initWithExecutor:]
+ -[ADDensifiedLiDARFocusAssistFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADDensifiedLiDARFocusAssistFlow pushPointCloud:pose:calibration:timestamp:]
+ -[ADDensifiedLiDARFocusAssistFlow setDelegate:]
+ -[ADDensifiedLiDARFocusAssistPipeline expectedColorSensorROI]
+ -[ADDensifiedLiDARFocusAssistPipeline getTeleAfPlatformType]
+ -[ADDensifiedLiDARFocusAssistPipeline validDepthRect]
+ -[ADDensifiedLiDARFocusAssistPipelineParameters initForDevice:]
+ -[ADEspressoBinocularDepthInferenceDescriptor .cxx_destruct]
+ -[ADEspressoBinocularDepthInferenceDescriptor auxiliaryColorInput]
+ -[ADEspressoBinocularDepthInferenceDescriptor auxiliaryConfidenceOutput]
+ -[ADEspressoBinocularDepthInferenceDescriptor auxiliaryDisparityOutput]
+ -[ADEspressoBinocularDepthInferenceDescriptor auxiliarySegmentationOutput]
+ -[ADEspressoBinocularDepthInferenceDescriptor initWithNetworkProvider:prioritization:espressoEngine:]
+ -[ADEspressoBinocularDepthInferenceDescriptor referenceColorInput]
+ -[ADEspressoMetricDepthInferenceDescriptor .cxx_destruct]
+ -[ADEspressoMetricDepthInferenceDescriptor cameraEmbeddingInput]
+ -[ADEspressoMetricDepthInferenceDescriptor confidenceOutput]
+ -[ADEspressoMetricDepthInferenceDescriptor depthOutput]
+ -[ADEspressoMetricDepthInferenceDescriptor initWithNetworkProvider:espressoEngine:]
+ -[ADEspressoMetricDepthInferenceDescriptor jasperInput]
+ -[ADEspressoMetricDepthInferenceDescriptor normalsOutput]
+ -[ADEspressoMetricDepthInferenceDescriptor pearlInput]
+ -[ADEspressoMetricDepthInferenceDescriptor primaryColorInput]
+ -[ADEspressoMetricDepthInferenceDescriptor secondaryColorInput]
+ -[ADExecutorParameters setStepsToExecute:]
+ -[ADExecutorParameters stepsToExecute]
+ -[ADFusedDepthLoggerHandler name]
+ -[ADJasperColorExecutor copyConfidenceAllowPixelFormatChange:outputConfidence:]
+ -[ADJasperColorExecutor doesSupportBufferCopyPolicy:]
+ -[ADJasperColorExecutor executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointCloud:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:]
+ -[ADJasperColorExecutor executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:]
+ -[ADJasperColorExecutor executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:]
+ -[ADJasperColorExecutor rotateConfidenceAllowPixelFormatChange:rotation:outputConfidence:]
+ -[ADJasperColorExecutorParameters ignoreDistortionInDepthReprojection]
+ -[ADJasperColorExecutorParameters setIgnoreDistortionInDepthReprojection:]
+ -[ADJasperColorInFieldCalibrationPipeline resetSdfHistory]
+ -[ADJasperColorInFieldCalibrationPipelineParameters sdfHistorySize]
+ -[ADJasperColorInfieldCalibrationFlow initWithExecutor:andIntersessionData:andExtrinsicsFlowMode:]
+ -[ADJasperColorPipeline fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:]
+ -[ADJasperColorPipeline warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingOpticalFlow:]
+ -[ADJasperColorPipeline warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingPoseDelta:previousCalibration:currentCalibration:]
+ -[ADJasperPearlInFieldCalibrationExecutor .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationExecutor dealloc]
+ -[ADJasperPearlInFieldCalibrationExecutor executeWithInterSessionData:outResult:]
+ -[ADJasperPearlInFieldCalibrationExecutor executeWithInterSessionData:result:]
+ -[ADJasperPearlInFieldCalibrationExecutor executeWithJasperPearlInterSessionData:result:]
+ -[ADJasperPearlInFieldCalibrationExecutor extractIRSensorCalibFromLastSyncMatch]
+ -[ADJasperPearlInFieldCalibrationExecutor extractJasperToPearlCalibFromLastSyncMatch]
+ -[ADJasperPearlInFieldCalibrationExecutor extractPearlInputsFromLastSyncMatch]
+ -[ADJasperPearlInFieldCalibrationExecutor extractPearlPrevPoseFromLastSyncMatch]
+ -[ADJasperPearlInFieldCalibrationExecutor initWithParameters:pceCalib:]
+ -[ADJasperPearlInFieldCalibrationExecutor initWithPceCalib:]
+ -[ADJasperPearlInFieldCalibrationExecutor logJPCInputs:]
+ -[ADJasperPearlInFieldCalibrationExecutor logJasperAggPC:timestamp:]
+ -[ADJasperPearlInFieldCalibrationExecutor logPose:logMessagePrefix:]
+ -[ADJasperPearlInFieldCalibrationExecutor numberOfExecutionSteps]
+ -[ADJasperPearlInFieldCalibrationExecutor overrideCVCalIntrinsicsWithPCECalibIntrinsics:temperature:]
+ -[ADJasperPearlInFieldCalibrationExecutor pceCalib]
+ -[ADJasperPearlInFieldCalibrationExecutor pearlInfraredCameraCalibration]
+ -[ADJasperPearlInFieldCalibrationExecutor prepare]
+ -[ADJasperPearlInFieldCalibrationExecutor printOutResults:]
+ -[ADJasperPearlInFieldCalibrationExecutor pushJasperPointCloud:timestamp:pose:jasperToPearlOperationalTransform:]
+ -[ADJasperPearlInFieldCalibrationExecutor pushJasperPointCloud:timestamp:pose:jasperToPearlTransform:]
+ -[ADJasperPearlInFieldCalibrationExecutor pushPearlDepth:pearlDx:pearlDy:pearlScore:timestamp:metadata:pose:prevPose:]
+ -[ADJasperPearlInFieldCalibrationExecutor pushPearlDepth:pearlDx:pearlDy:pearlScore:timestamp:pose:pearlSensorCalibration:]
+ -[ADJasperPearlInFieldCalibrationExecutor pushPearlDepth:timestamp:pose:temperature:irSensorOperationalCalibration:]
+ -[ADJasperPearlInFieldCalibrationExecutor setPceCalib:]
+ -[ADJasperPearlInFieldCalibrationExecutor setPearlInfraredCameraCalibration:]
+ -[ADJasperPearlInFieldCalibrationExecutor shouldExecuteWithInterSessionDataRun:]
+ -[ADJasperPearlInFieldCalibrationExecutorParameters .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationExecutorParameters init]
+ -[ADJasperPearlInFieldCalibrationExecutorParameters pipelineParameters]
+ -[ADJasperPearlInFieldCalibrationInterSessionData .cxx_construct]
+ -[ADJasperPearlInFieldCalibrationInterSessionData .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationInterSessionData aggPointsWrapperObj]
+ -[ADJasperPearlInFieldCalibrationInterSessionData buildISFInputDictWithEFL:principalPointtX:principalPointtY:rotationMat:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData firstIFAFrameTimestampCurrentExecution]
+ -[ADJasperPearlInFieldCalibrationInterSessionData firstTimeEventFired]
+ -[ADJasperPearlInFieldCalibrationInterSessionData initDiagnosticPipelineLog]
+ -[ADJasperPearlInFieldCalibrationInterSessionData initIsf]
+ -[ADJasperPearlInFieldCalibrationInterSessionData initWithDictionaryRepresentation:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData initWithPCECalibData:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData init]
+ -[ADJasperPearlInFieldCalibrationInterSessionData insertEntryToDiagnosticPipelineLog:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData irCamFOVCoveragePercent]
+ -[ADJasperPearlInFieldCalibrationInterSessionData lastAlgoRadarTriggerTimestamp]
+ -[ADJasperPearlInFieldCalibrationInterSessionData lastIFAFrameTimestampCurrentExecution]
+ -[ADJasperPearlInFieldCalibrationInterSessionData lastPearlTemp]
+ -[ADJasperPearlInFieldCalibrationInterSessionData maxIRCamTemperatureCurrentExecution]
+ -[ADJasperPearlInFieldCalibrationInterSessionData minIRCamTemperatureCurrentExecution]
+ -[ADJasperPearlInFieldCalibrationInterSessionData numOfIFAFramesCurrentExecution]
+ -[ADJasperPearlInFieldCalibrationInterSessionData numOfUniqueTOFSpots]
+ -[ADJasperPearlInFieldCalibrationInterSessionData persistenceData]
+ -[ADJasperPearlInFieldCalibrationInterSessionData processJpcResult:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData resetIFAObjects]
+ -[ADJasperPearlInFieldCalibrationInterSessionData reset]
+ -[ADJasperPearlInFieldCalibrationInterSessionData rotArray]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setAggPointsWrapperObj:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setFirstIFAFrameTimestampCurrentExecution:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setFirstTimeEventFired:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setIrCamFOVCoveragePercent:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setLastAlgoRadarTriggerTimestamp:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setLastIFAFrameTimestampCurrentExecution:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setLastPearlTemp:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setMaxIRCamTemperatureCurrentExecution:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setMinIRCamTemperatureCurrentExecution:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setNumOfIFAFramesCurrentExecution:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setNumOfUniqueTOFSpots:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setRotArray:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData setTransArray:]
+ -[ADJasperPearlInFieldCalibrationInterSessionData transArray]
+ -[ADJasperPearlInFieldCalibrationJasperInput .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationJasperInput bankPointCloud]
+ -[ADJasperPearlInFieldCalibrationJasperInput jasperBankPose]
+ -[ADJasperPearlInFieldCalibrationJasperInput setBankPointCloud:]
+ -[ADJasperPearlInFieldCalibrationJasperInput setJasperBankPose:]
+ -[ADJasperPearlInFieldCalibrationJasperInput setTimestamp:]
+ -[ADJasperPearlInFieldCalibrationJasperInput timestamp]
+ -[ADJasperPearlInFieldCalibrationPearlInput depth]
+ -[ADJasperPearlInFieldCalibrationPearlInput dx]
+ -[ADJasperPearlInFieldCalibrationPearlInput dy]
+ -[ADJasperPearlInFieldCalibrationPearlInput getPearlDepthAttachments]
+ -[ADJasperPearlInFieldCalibrationPearlInput pose]
+ -[ADJasperPearlInFieldCalibrationPearlInput prevPose]
+ -[ADJasperPearlInFieldCalibrationPearlInput score]
+ -[ADJasperPearlInFieldCalibrationPearlInput setDepth:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setDx:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setDy:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setPose:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setPrevPose:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setScore:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setTemperature:]
+ -[ADJasperPearlInFieldCalibrationPearlInput setTimestamp:]
+ -[ADJasperPearlInFieldCalibrationPearlInput temperature]
+ -[ADJasperPearlInFieldCalibrationPearlInput timestamp]
+ -[ADJasperPearlInFieldCalibrationPipeline .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationPipeline buildJpcInputDataObjectWithPearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:outJpcInputs:]
+ -[ADJasperPearlInFieldCalibrationPipeline checkPrerequisitesForProcessWithPearlWithPearlInputs:]
+ -[ADJasperPearlInFieldCalibrationPipeline fillTelemetryData:jpcError:]
+ -[ADJasperPearlInFieldCalibrationPipeline fillTelemetryDataWithPreviousCalibration:pceCalib:]
+ -[ADJasperPearlInFieldCalibrationPipeline fixEFLTempCoeffInISFResult:eflTempCoeff:temperature:]
+ -[ADJasperPearlInFieldCalibrationPipeline getIRSensorCameraCalibFromPCECalib]
+ -[ADJasperPearlInFieldCalibrationPipeline getJpcObjectForRunMode:isValid:]
+ -[ADJasperPearlInFieldCalibrationPipeline getPCECalibStruct]
+ -[ADJasperPearlInFieldCalibrationPipeline initWithParameters:pceCalib:]
+ -[ADJasperPearlInFieldCalibrationPipeline init]
+ -[ADJasperPearlInFieldCalibrationPipeline logJpcInputData:]
+ -[ADJasperPearlInFieldCalibrationPipeline pceCalib]
+ -[ADJasperPearlInFieldCalibrationPipeline pipelineParameters]
+ -[ADJasperPearlInFieldCalibrationPipeline processJpcResultWithStatus:gmcjResult:glaResult:result:interSessionData:temperature:eflTempCoeff:]
+ -[ADJasperPearlInFieldCalibrationPipeline processWithPearl:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:]
+ -[ADJasperPearlInFieldCalibrationPipeline runWithJpc:runMode:pearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:]
+ -[ADJasperPearlInFieldCalibrationPipeline setGMCJResult:result:temperature:]
+ -[ADJasperPearlInFieldCalibrationPipeline setPceCalib:]
+ -[ADJasperPearlInFieldCalibrationPipeline setPipelineParameters:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters init]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters isReportTelemetry]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters logger]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters pointCloudAggregationParameters]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters pointCloudFilterParameters]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setIsReportTelemetry:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setLogger:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setPointCloudAggregationParameters:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setPointCloudFilterParameters:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setSkipISF:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters setStepsToExecute:]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters skipISF]
+ -[ADJasperPearlInFieldCalibrationPipelineParameters stepsToExecute]
+ -[ADJasperPearlInFieldCalibrationResult .cxx_destruct]
+ -[ADJasperPearlInFieldCalibrationResult efl]
+ -[ADJasperPearlInFieldCalibrationResult pceCalib]
+ -[ADJasperPearlInFieldCalibrationResult principalPointX]
+ -[ADJasperPearlInFieldCalibrationResult principalPointY]
+ -[ADJasperPearlInFieldCalibrationResult setEfl:]
+ -[ADJasperPearlInFieldCalibrationResult setPceCalib:]
+ -[ADJasperPearlInFieldCalibrationResult setPrincipalPointX:]
+ -[ADJasperPearlInFieldCalibrationResult setPrincipalPointY:]
+ -[ADJasperPearlInFieldCalibrationResult setTelemetryData:]
+ -[ADJasperPearlInFieldCalibrationResult setTemperature:]
+ -[ADJasperPearlInFieldCalibrationResult telemetryData]
+ -[ADJasperPearlInFieldCalibrationResult temperature]
+ -[ADJasperPearlTelemetryData .cxx_destruct]
+ -[ADJasperPearlTelemetryData depthDiffThresholdAboveMedian]
+ -[ADJasperPearlTelemetryData gmcjErrorCode]
+ -[ADJasperPearlTelemetryData gmcjOutputValidationErrorCode]
+ -[ADJasperPearlTelemetryData gmcjPPXChangeMicronFromPrev]
+ -[ADJasperPearlTelemetryData gmcjPPXChangeMicronFromT0]
+ -[ADJasperPearlTelemetryData gmcjPPYChangeMicronFromPrev]
+ -[ADJasperPearlTelemetryData gmcjPPYChangeMicronFromT0]
+ -[ADJasperPearlTelemetryData gmcjProjRotXChangeFromPrev]
+ -[ADJasperPearlTelemetryData gmcjProjRotXChangeFromT0]
+ -[ADJasperPearlTelemetryData gmcjProjRotYChangeFromPrev]
+ -[ADJasperPearlTelemetryData gmcjProjRotYChangeFromT0]
+ -[ADJasperPearlTelemetryData gmcjProjRotZChangeFromPrev]
+ -[ADJasperPearlTelemetryData gmcjProjRotZChangeFromT0]
+ -[ADJasperPearlTelemetryData gmcjScaleChangePercentFromPrev]
+ -[ADJasperPearlTelemetryData gmcjScaleChangePercentFromT0]
+ -[ADJasperPearlTelemetryData init]
+ -[ADJasperPearlTelemetryData intervalBetweenIFAFrames]
+ -[ADJasperPearlTelemetryData irCamFOVCoveragePercent]
+ -[ADJasperPearlTelemetryData isAssignedGMCJBlock]
+ -[ADJasperPearlTelemetryData isAssignedGMCJValidation]
+ -[ADJasperPearlTelemetryData isAssignedIFABlock]
+ -[ADJasperPearlTelemetryData isAssignedJasperReflectionsFrameFilter]
+ -[ADJasperPearlTelemetryData isAssignedPipelineCurrent]
+ -[ADJasperPearlTelemetryData isAssignedPipelinePrevious]
+ -[ADJasperPearlTelemetryData jasperMisalignmentAfter]
+ -[ADJasperPearlTelemetryData jasperMisalignmentBefore]
+ -[ADJasperPearlTelemetryData jpcErrorCode]
+ -[ADJasperPearlTelemetryData maxIRCamTemperature]
+ -[ADJasperPearlTelemetryData minIRCamTemperature]
+ -[ADJasperPearlTelemetryData motionBetweenFramesRotationX]
+ -[ADJasperPearlTelemetryData motionBetweenFramesRotationY]
+ -[ADJasperPearlTelemetryData motionBetweenFramesRotationZ]
+ -[ADJasperPearlTelemetryData motionBetweenFramesTranslationX]
+ -[ADJasperPearlTelemetryData motionBetweenFramesTranslationY]
+ -[ADJasperPearlTelemetryData motionBetweenFramesTranslationZ]
+ -[ADJasperPearlTelemetryData newEfl]
+ -[ADJasperPearlTelemetryData newPPX]
+ -[ADJasperPearlTelemetryData newPPY]
+ -[ADJasperPearlTelemetryData newRotX]
+ -[ADJasperPearlTelemetryData newRotY]
+ -[ADJasperPearlTelemetryData newRotZ]
+ -[ADJasperPearlTelemetryData numJasperSpotsFlaggedAsGlare]
+ -[ADJasperPearlTelemetryData numJasperSpotsFlaggedAsReflectiveSurface]
+ -[ADJasperPearlTelemetryData numOfAggregatedFrames]
+ -[ADJasperPearlTelemetryData numOfUniqueTOFSpots]
+ -[ADJasperPearlTelemetryData numPearlJasperCorrespondencesPostLocalDepthVarFilter]
+ -[ADJasperPearlTelemetryData numPearlJasperCorrespondencesPostPJDepthDiffFilter]
+ -[ADJasperPearlTelemetryData numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter]
+ -[ADJasperPearlTelemetryData numPearlJasperCorrespondencesPreIFA]
+ -[ADJasperPearlTelemetryData numPearlOnlyCorrespondencesPostSpatialCoverageFilter]
+ -[ADJasperPearlTelemetryData numPearlOnlyCorrespondencesPreIFA]
+ -[ADJasperPearlTelemetryData pceCalib]
+ -[ADJasperPearlTelemetryData pearlCalibSetSize]
+ -[ADJasperPearlTelemetryData pearlJapserCalibSetSize]
+ -[ADJasperPearlTelemetryData pearlTemperature]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankRotationX]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankRotationY]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankRotationZ]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankRotation]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankTranslationX]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankTranslationY]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankTranslationZ]
+ -[ADJasperPearlTelemetryData pearlToLastJasperBankTranslation]
+ -[ADJasperPearlTelemetryData prevEfl]
+ -[ADJasperPearlTelemetryData prevPPX]
+ -[ADJasperPearlTelemetryData prevPPY]
+ -[ADJasperPearlTelemetryData prevRotX]
+ -[ADJasperPearlTelemetryData prevRotY]
+ -[ADJasperPearlTelemetryData prevRotZ]
+ -[ADJasperPearlTelemetryData reprojectionErrorAfter]
+ -[ADJasperPearlTelemetryData reprojectionErrorBefore]
+ -[ADJasperPearlTelemetryData setDepthDiffThresholdAboveMedian:]
+ -[ADJasperPearlTelemetryData setGmcjErrorCode:]
+ -[ADJasperPearlTelemetryData setGmcjOutputValidationErrorCode:]
+ -[ADJasperPearlTelemetryData setGmcjPPXChangeMicronFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjPPXChangeMicronFromT0:]
+ -[ADJasperPearlTelemetryData setGmcjPPYChangeMicronFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjPPYChangeMicronFromT0:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotXChangeFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotXChangeFromT0:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotYChangeFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotYChangeFromT0:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotZChangeFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjProjRotZChangeFromT0:]
+ -[ADJasperPearlTelemetryData setGmcjScaleChangePercentFromPrev:]
+ -[ADJasperPearlTelemetryData setGmcjScaleChangePercentFromT0:]
+ -[ADJasperPearlTelemetryData setIntervalBetweenIFAFrames:]
+ -[ADJasperPearlTelemetryData setIrCamFOVCoveragePercent:]
+ -[ADJasperPearlTelemetryData setIsAssignedGMCJBlock:]
+ -[ADJasperPearlTelemetryData setIsAssignedGMCJValidation:]
+ -[ADJasperPearlTelemetryData setIsAssignedIFABlock:]
+ -[ADJasperPearlTelemetryData setIsAssignedJasperReflectionsFrameFilter:]
+ -[ADJasperPearlTelemetryData setIsAssignedPipelineCurrent:]
+ -[ADJasperPearlTelemetryData setIsAssignedPipelinePrevious:]
+ -[ADJasperPearlTelemetryData setJasperMisalignmentAfter:]
+ -[ADJasperPearlTelemetryData setJasperMisalignmentBefore:]
+ -[ADJasperPearlTelemetryData setJpcErrorCode:]
+ -[ADJasperPearlTelemetryData setMaxIRCamTemperature:]
+ -[ADJasperPearlTelemetryData setMinIRCamTemperature:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesRotationX:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesRotationY:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesRotationZ:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesTranslationX:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesTranslationY:]
+ -[ADJasperPearlTelemetryData setMotionBetweenFramesTranslationZ:]
+ -[ADJasperPearlTelemetryData setNewEfl:]
+ -[ADJasperPearlTelemetryData setNewPPX:]
+ -[ADJasperPearlTelemetryData setNewPPY:]
+ -[ADJasperPearlTelemetryData setNewRotX:]
+ -[ADJasperPearlTelemetryData setNewRotY:]
+ -[ADJasperPearlTelemetryData setNewRotZ:]
+ -[ADJasperPearlTelemetryData setNumJasperSpotsFlaggedAsGlare:]
+ -[ADJasperPearlTelemetryData setNumJasperSpotsFlaggedAsReflectiveSurface:]
+ -[ADJasperPearlTelemetryData setNumOfAggregatedFrames:]
+ -[ADJasperPearlTelemetryData setNumOfUniqueTOFSpots:]
+ -[ADJasperPearlTelemetryData setNumPearlJasperCorrespondencesPostLocalDepthVarFilter:]
+ -[ADJasperPearlTelemetryData setNumPearlJasperCorrespondencesPostPJDepthDiffFilter:]
+ -[ADJasperPearlTelemetryData setNumPearlJasperCorrespondencesPostPJWorkDistOverlapFilter:]
+ -[ADJasperPearlTelemetryData setNumPearlJasperCorrespondencesPreIFA:]
+ -[ADJasperPearlTelemetryData setNumPearlOnlyCorrespondencesPostSpatialCoverageFilter:]
+ -[ADJasperPearlTelemetryData setNumPearlOnlyCorrespondencesPreIFA:]
+ -[ADJasperPearlTelemetryData setPceCalib:]
+ -[ADJasperPearlTelemetryData setPearlCalibSetSize:]
+ -[ADJasperPearlTelemetryData setPearlJapserCalibSetSize:]
+ -[ADJasperPearlTelemetryData setPearlTemperature:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankRotation:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankRotationX:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankRotationY:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankRotationZ:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankTranslation:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankTranslationX:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankTranslationY:]
+ -[ADJasperPearlTelemetryData setPearlToLastJasperBankTranslationZ:]
+ -[ADJasperPearlTelemetryData setPrevEfl:]
+ -[ADJasperPearlTelemetryData setPrevPPX:]
+ -[ADJasperPearlTelemetryData setPrevPPY:]
+ -[ADJasperPearlTelemetryData setPrevRotX:]
+ -[ADJasperPearlTelemetryData setPrevRotY:]
+ -[ADJasperPearlTelemetryData setPrevRotZ:]
+ -[ADJasperPearlTelemetryData setReprojectionErrorAfter:]
+ -[ADJasperPearlTelemetryData setReprojectionErrorBefore:]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerEndReasonIsConvergence]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerEndReasonIsMaxFrameCount]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerEndReasonIsOutputValidationMetricIncreased]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerFirstFrameTemperature]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerFirstFrameTimestamp]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerFrameCount]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerLastFrameTemperature]
+ -[ADJasperPearlTriggeringTelemetryData caCurrentTriggerLastFrameTimestamp]
+ -[ADJasperPearlTriggeringTelemetryData caLastTriggerLastFrameTemperature]
+ -[ADJasperPearlTriggeringTelemetryData caLastTriggerLastFrameTimestamp]
+ -[ADJasperPearlTriggeringTelemetryData init]
+ -[ADJasperPearlTriggeringTelemetryData notifyNewFrameArrived:temperature:]
+ -[ADJasperPearlTriggeringTelemetryData notifyTriggeringSessionEnded]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerEndReasonIsConvergence:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerEndReasonIsMaxFrameCount:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerEndReasonIsOutputValidationMetricIncreased:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerFirstFrameTemperature:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerFirstFrameTimestamp:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerFrameCount:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerLastFrameTemperature:]
+ -[ADJasperPearlTriggeringTelemetryData setCaCurrentTriggerLastFrameTimestamp:]
+ -[ADJasperPearlTriggeringTelemetryData setCaLastTriggerLastFrameTemperature:]
+ -[ADJasperPearlTriggeringTelemetryData setCaLastTriggerLastFrameTimestamp:]
+ -[ADJasperPearlTriggeringTelemetryData setTriggeringEndReason:triggerEndReasonIsMaxFrameCount:triggerEndReasonIsValidationMetricIncreased:]
+ -[ADLKTConfidenceParameters checkFlowInFOV]
+ -[ADLKTConfidenceParameters conditionNumberMaxValue]
+ -[ADLKTConfidenceParameters conditionNumberMinValue]
+ -[ADLKTConfidenceParameters gradientNormMaxValue]
+ -[ADLKTConfidenceParameters gradientNormMinValue]
+ -[ADLKTConfidenceParameters init]
+ -[ADLKTConfidenceParameters scaleIdxForConfidenceComponents]
+ -[ADLKTConfidenceParameters setCheckFlowInFOV:]
+ -[ADLKTConfidenceParameters setConditionNumberMaxValue:]
+ -[ADLKTConfidenceParameters setConditionNumberMinValue:]
+ -[ADLKTConfidenceParameters setGradientNormMaxValue:]
+ -[ADLKTConfidenceParameters setGradientNormMinValue:]
+ -[ADLKTConfidenceParameters setScaleIdxForConfidenceComponents:]
+ -[ADLKTExecutor convertInputFormatIfNeeded:greyscaleInput:]
+ -[ADLKTExecutor createColorConvertingSession:]
+ -[ADLKTExecutor createConfidenceBuffer]
+ -[ADLKTExecutor createOpticalFlowBuffer]
+ -[ADLKTExecutor dealloc]
+ -[ADLKTExecutor downscaleImageAndGenerateMipmapsIfNeeded:inputTexture:]
+ -[ADLKTExecutor executeFromFrame:toFrame:outputOpticalFlow:outputConfidence:]
+ -[ADLKTExecutor executeFromFrame:toFrame:validBufferRect:outputOpticalFlow:outputConfidence:]
+ -[ADLKTExecutor executeFromFrameToPreviousFrame:outputOpticalFlow:outputConfidence:]
+ -[ADLKTExecutor initWithDescriptor:forLayout:executorParameters:]
+ -[ADLKTExecutor processFrame:validBufferRect:intoOpticalFlowBuffer:outputConfidence:]
+ -[ADLKTExecutorParameters .cxx_destruct]
+ -[ADLKTExecutorParameters confidenceParameters]
+ -[ADLKTExecutorParameters confidenceUnits]
+ -[ADLKTExecutorParameters init]
+ -[ADLKTExecutorParameters setConfidenceParameters:]
+ -[ADLKTExecutorParameters setConfidenceUnits:]
+ -[ADLKTFlow .cxx_destruct]
+ -[ADLKTFlow delegate]
+ -[ADLKTFlow executor]
+ -[ADLKTFlow initWithExecutor:forTemporalOpticalFlow:]
+ -[ADLKTFlow processMatch:]
+ -[ADLKTFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADLKTFlow pushSecondaryColor:pose:calibration:timestamp:]
+ -[ADLKTFlow setDelegate:]
+ -[ADLKTOpticalFlow _computeConfidence:shiftMap:outConfidceMap:cropSizeRatio:]
+ -[ADLKTOpticalFlow _computeFeaturesDerivativesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:]
+ -[ADLKTOpticalFlow _computeFeaturesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:]
+ -[ADLKTOpticalFlow _createImagePyramidWithCommandBuffer:cropSizeRatio:inOutPyramidsArray:error:]
+ -[ADLKTOpticalFlow _createImagePyramidWithCommandBuffer:in_tex:cropSizeRatio:outPyramidsArray:error:]
+ -[ADLKTOpticalFlow _doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:cropSizeRatio:]
+ -[ADLKTOpticalFlow _doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:in_uv_tex:out_uv_tex:out_w_tex:uniforms:cropSizeRatio:]
+ -[ADLKTOpticalFlow _downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:cropSizeRatio:]
+ -[ADLKTOpticalFlow _prepareLKTGPUUniforms:out_uv_tex:coeff:stride:computeConfidenceComponents:]
+ -[ADLKTOpticalFlow confidenceParameters]
+ -[ADLKTOpticalFlow dispatchCommandEncoder:pipeline:width:height:]
+ -[ADLKTOpticalFlow encodeOpticalFlowSolverToCommandBuffer:currentFeaturesArray:currentDerivitiveArray:previousFeaturesArray:previousDerivitiveArray:currentPyramidsArray:validBufferRect:outShiftMap:outConfidenceMap:]
+ -[ADLKTOpticalFlow encodePyramidFeaturesToCommandBuffer:grayscaleTexture:validBufferRect:outPyramidsArray:outFeaturesArray:outDerivitiveArray:]
+ -[ADLKTOpticalFlow initWithDevice:inputSize:config:confidenceParameters:]
+ -[ADLKTOpticalFlow setConfidenceParameters:]
+ -[ADLKTTexturesDescriptor confidenceDescriptor]
+ -[ADLKTTexturesDescriptor downscaledInputDescriptor]
+ -[ADLKTTexturesDescriptor downscaledInputSizeForLayout:]
+ -[ADLKTTexturesDescriptor initForSupportedSizes:prioritization:]
+ -[ADLKTTexturesDescriptor outputDescriptor]
+ -[ADLKTTexturesDescriptor outputSizeForLayout:]
+ -[ADLogManager forceCounterAsTimestamp]
+ -[ADLogManager setForceCounterAsTimestamp:]
+ -[ADLogManager updateTimestampWithOverride:]
+ -[ADMetricDepthExecutor .cxx_destruct]
+ -[ADMetricDepthExecutor allocateIntermediateBuffers]
+ -[ADMetricDepthExecutor deallocInferenceBuffers]
+ -[ADMetricDepthExecutor dealloc]
+ -[ADMetricDepthExecutor doesSupportBufferCopyPolicy:]
+ -[ADMetricDepthExecutor espressoRunner]
+ -[ADMetricDepthExecutor executeWithPrimaryColor:secondaryColor:pearl:pointClouds:primaryColorCalibration:secondaryColorCalibration:pearlCalibration:lidarCameraCalibration:primaryColorPose:secondaryColorPose:pearlPose:pointCloudPoses:timestamp:outputDepthMap:outputUncertaintyMap:outputConfidenceMap:outputConfidenceLevels:outputNormalsMap:outputActiveDepthMaskMap:outputDepthCalibration:]
+ -[ADMetricDepthExecutor getIntermediates]
+ -[ADMetricDepthExecutor initForEspressoEngine:]
+ -[ADMetricDepthExecutor init]
+ -[ADMetricDepthExecutor lastFrameStatistics]
+ -[ADMetricDepthExecutor numberOfExecutionSteps]
+ -[ADMetricDepthExecutor pipeline]
+ -[ADMetricDepthExecutor prepareForInputRoi:]
+ -[ADMetricDepthExecutor prepareForInputRoi:engineType:]
+ -[ADMetricDepthExecutor writeMetricDepthToJPEG:timestamp:preProcessedJasper:preProcessedPearl:preProcessedPrimaryColor:rawConfOut:rawDepthOut:]
+ -[ADMetricDepthExecutorParameters .cxx_destruct]
+ -[ADMetricDepthExecutorParameters initForPipeline:]
+ -[ADMetricDepthExecutorParameters pipelineParameters]
+ -[ADMetricDepthFlow .cxx_destruct]
+ -[ADMetricDepthFlow executor]
+ -[ADMetricDepthFlow initWithExecutor:]
+ -[ADMetricDepthFlow initWithExecutor:calculateConfidenceMap:calculateConfidenceLevels:]
+ -[ADMetricDepthFlow processIfMatch:]
+ -[ADMetricDepthFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADMetricDepthFlow pushPearlDepth:pose:depthCalibration:irToDepthTransform:timestamp:]
+ -[ADMetricDepthFlow pushPointCloud:pose:calibration:timestamp:]
+ -[ADMetricDepthFlow pushSecondaryColor:pose:calibration:timestamp:]
+ -[ADMetricDepthFrameStatistics allPosesValid]
+ -[ADMetricDepthFrameStatistics colorPoseRoll]
+ -[ADMetricDepthFrameStatistics depthSensorsIgnored]
+ -[ADMetricDepthFrameStatistics jasperInputSpotCount]
+ -[ADMetricDepthFrameStatistics jasperPoseDistance]
+ -[ADMetricDepthFrameStatistics jasperProjectedSpotCount]
+ -[ADMetricDepthFrameStatistics pearlProjectedPixelCount]
+ -[ADMetricDepthFrameStatistics pearlProjectedPixelPercentage]
+ -[ADMetricDepthFrameStatistics setAllPosesValid:]
+ -[ADMetricDepthFrameStatistics setColorPoseRoll:]
+ -[ADMetricDepthFrameStatistics setDepthSensorsIgnored:]
+ -[ADMetricDepthFrameStatistics setJasperInputSpotCount:]
+ -[ADMetricDepthFrameStatistics setJasperPoseDistance:]
+ -[ADMetricDepthFrameStatistics setJasperProjectedSpotCount:]
+ -[ADMetricDepthFrameStatistics setPearlProjectedPixelCount:]
+ -[ADMetricDepthFrameStatistics setPearlProjectedPixelPercentage:]
+ -[ADMetricDepthPipeline .cxx_construct]
+ -[ADMetricDepthPipeline .cxx_destruct]
+ -[ADMetricDepthPipeline createCameraEmbeddingsForRightCameraCalibration:leftCameraCalibration:rightCameraPose:leftCameraPose:outputBuffer:]
+ -[ADMetricDepthPipeline createJasperEmbeddings:cropTo:rotateBy:outputBuffer:outputBatchOffset:]
+ -[ADMetricDepthPipeline createJasperEmbeddingsForRightCameraPointCloud:leftCameraPointCloud:crop:rotation:outputBuffer:]
+ -[ADMetricDepthPipeline emulatePeridotFromJasper:jasperPoses:jasperTimestamps:jasperToPlatformTransform:pearlDepth:pearlPose:pearlCalibration:outPointCloud:outPose:outTimestamp:]
+ -[ADMetricDepthPipeline fillSensorsMask:]
+ -[ADMetricDepthPipeline filterJasperPointCloud:usingPearlInput:]
+ -[ADMetricDepthPipeline filterUncertainty:output:]
+ -[ADMetricDepthPipeline inferenceDescriptor]
+ -[ADMetricDepthPipeline initForEspressoEngine:]
+ -[ADMetricDepthPipeline initForEspressoEngine:pipelineParameters:]
+ -[ADMetricDepthPipeline init]
+ -[ADMetricDepthPipeline outputActiveDepthMaskDescriptor]
+ -[ADMetricDepthPipeline outputConfidenceDescriptor]
+ -[ADMetricDepthPipeline outputConfidenceLevelsDescriptor]
+ -[ADMetricDepthPipeline outputDepthDescriptor]
+ -[ADMetricDepthPipeline outputNormalsDescriptor]
+ -[ADMetricDepthPipeline pearlReprojector]
+ -[ADMetricDepthPipeline pipelineParameters]
+ -[ADMetricDepthPipeline postProcessEspressoConfidence:outputConfidence:confidenceUnits:]
+ -[ADMetricDepthPipeline postProcessEspressoDepth:espressoConfidence:espressoNormals:toOutputDepth:outputConfidence:outputNormals:]
+ -[ADMetricDepthPipeline postProcessEspressoDepth:espressoConfidence:toOutputDepth:outputConfidence:]
+ -[ADMetricDepthPipeline postProcessEspressoNormals:toOutputNormals:]
+ -[ADMetricDepthPipeline preprocessPearlDepth:pearlPose:pearlCalibration:colorPose:colorCalibration:outputBuffer:]
+ -[ADMetricDepthPipeline setPipelineParameters:]
+ -[ADMetricDepthPipelineParameters .cxx_destruct]
+ -[ADMetricDepthPipelineParameters aggregationParameters]
+ -[ADMetricDepthPipelineParameters confidenceBucketingHighThreshold]
+ -[ADMetricDepthPipelineParameters confidenceBucketingLowThreshold]
+ -[ADMetricDepthPipelineParameters confidenceLevelRanges]
+ -[ADMetricDepthPipelineParameters confidenceUnits]
+ -[ADMetricDepthPipelineParameters init]
+ -[ADMetricDepthPipelineParameters maxCenterResolution]
+ -[ADMetricDepthPipelineParameters maxJasperDepth]
+ -[ADMetricDepthPipelineParameters maxRaysResolution]
+ -[ADMetricDepthPipelineParameters numCenterBands]
+ -[ADMetricDepthPipelineParameters numJasperBands]
+ -[ADMetricDepthPipelineParameters numRaysBands]
+ -[ADMetricDepthPipelineParameters pearlJasperCoFilteringMaxAllowedDisagreement]
+ -[ADMetricDepthPipelineParameters pearlJasperCoFilteringMaxPearlDepth]
+ -[ADMetricDepthPipelineParameters pointCloudFilter]
+ -[ADMetricDepthPipelineParameters setAggregationParameters:]
+ -[ADMetricDepthPipelineParameters setConfidenceBucketingHighThreshold:]
+ -[ADMetricDepthPipelineParameters setConfidenceBucketingLowThreshold:]
+ -[ADMetricDepthPipelineParameters setConfidenceLevelRanges:]
+ -[ADMetricDepthPipelineParameters setConfidenceUnits:]
+ -[ADMetricDepthPipelineParameters setMaxCenterResolution:]
+ -[ADMetricDepthPipelineParameters setMaxJasperDepth:]
+ -[ADMetricDepthPipelineParameters setMaxRaysResolution:]
+ -[ADMetricDepthPipelineParameters setNumCenterBands:]
+ -[ADMetricDepthPipelineParameters setNumJasperBands:]
+ -[ADMetricDepthPipelineParameters setNumRaysBands:]
+ -[ADMetricDepthPipelineParameters setPearlJasperCoFilteringMaxAllowedDisagreement:]
+ -[ADMetricDepthPipelineParameters setPearlJasperCoFilteringMaxPearlDepth:]
+ -[ADMetricDepthPipelineParameters setPointCloudFilter:]
+ -[ADMonocularFlow .cxx_destruct]
+ -[ADMonocularFlow executor]
+ -[ADMonocularFlow initWithExecutor:]
+ -[ADMonocularFlow processColor:timestamp:]
+ -[ADMonocularFlow pushColor:pose:calibration:metadata:timestamp:]
+ -[ADMonocularFlow pushColor:timestamp:]
+ -[ADNetworkProvider bufferExists:isInput:]
+ -[ADNetworkProvider initWithNetwork:requestedLayouts:espressoEngine:makeRunnable:]
+ -[ADNetworkProvider readJsonMetadataFile:requestedLayouts:]
+ -[ADNetworkProvider supportedDimensionsForInput:expectedPixelFormat:]
+ -[ADPipelineParameters requestedDimensions]
+ -[ADPipelineParameters setRequestedDimensions:]
+ -[ADVisualDepthBuffer .cxx_destruct]
+ -[ADVisualDepthBuffer calibration]
+ -[ADVisualDepthBuffer confidence]
+ -[ADVisualDepthBuffer dealloc]
+ -[ADVisualDepthBuffer image]
+ -[ADVisualDepthBuffer initWithImage:confidence:labels:normals:calibration:uuid:pose:timestamp:]
+ -[ADVisualDepthBuffer labels]
+ -[ADVisualDepthBuffer normals]
+ -[ADVisualDepthBuffer pose]
+ -[ADVisualDepthBuffer setCalibration:]
+ -[ADVisualDepthBuffer setConfidence:]
+ -[ADVisualDepthBuffer setImage:]
+ -[ADVisualDepthBuffer setLabels:]
+ -[ADVisualDepthBuffer setNormals:]
+ -[ADVisualDepthBuffer setPose:]
+ -[ADVisualDepthBuffer setTimestamp:]
+ -[ADVisualDepthBuffer setUuid:]
+ -[ADVisualDepthBuffer timestamp]
+ -[ADVisualDepthBuffer uuid]
+ -[ADVisualDepthExecutor .cxx_destruct]
+ -[ADVisualDepthExecutor checkProjectionChanged:newCalib:]
+ -[ADVisualDepthExecutor dealloc]
+ -[ADVisualDepthExecutor deallocateVisualDepthBuffers]
+ -[ADVisualDepthExecutor executeForTimestamp:pose:]
+ -[ADVisualDepthExecutor executeForTimestamp:pose:output:]
+ -[ADVisualDepthExecutor executeWithOutput:]
+ -[ADVisualDepthExecutor execute]
+ -[ADVisualDepthExecutor getIntermediates]
+ -[ADVisualDepthExecutor initWithOutputDimensions:]
+ -[ADVisualDepthExecutor initWithWorkingSize:]
+ -[ADVisualDepthExecutor isReadyForExecution]
+ -[ADVisualDepthExecutor numberOfExecutionSteps]
+ -[ADVisualDepthExecutor pipeline]
+ -[ADVisualDepthExecutor prepareForInputRoi:]
+ -[ADVisualDepthExecutor primaryColorCameraCalibration]
+ -[ADVisualDepthExecutor primaryDisparityCalibration]
+ -[ADVisualDepthExecutor primaryTargetCameraCalibration]
+ -[ADVisualDepthExecutor pushKeyframes:]
+ -[ADVisualDepthExecutor pushMesh:]
+ -[ADVisualDepthExecutor pushPrimaryColorImage:timestamp:pose:]
+ -[ADVisualDepthExecutor pushSecondaryColorImage:timestamp:pose:]
+ -[ADVisualDepthExecutor secondaryColorCameraCalibration]
+ -[ADVisualDepthExecutor secondaryDisparityCalibration]
+ -[ADVisualDepthExecutor secondaryTargetCameraCalibration]
+ -[ADVisualDepthExecutor setPrimaryColorCameraCalibration:]
+ -[ADVisualDepthExecutor setPrimaryDisparityCalibration:]
+ -[ADVisualDepthExecutor setPrimaryTargetCameraCalibration:]
+ -[ADVisualDepthExecutor setSecondaryColorCameraCalibration:]
+ -[ADVisualDepthExecutor setSecondaryDisparityCalibration:]
+ -[ADVisualDepthExecutor setSecondaryTargetCameraCalibration:]
+ -[ADVisualDepthExecutor updatePixelBufferAllocationForImageDescriptor:pixelBuffer:]
+ -[ADVisualDepthExecutorParameters .cxx_destruct]
+ -[ADVisualDepthExecutorParameters initForPipeline:]
+ -[ADVisualDepthExecutorParameters pipelineParameters]
+ -[ADVisualDepthGeometry .cxx_destruct]
+ -[ADVisualDepthGeometry buffer]
+ -[ADVisualDepthGeometry count]
+ -[ADVisualDepthGeometry initWithBuffer:count:offset:stride:]
+ -[ADVisualDepthGeometry offset]
+ -[ADVisualDepthGeometry setBuffer:]
+ -[ADVisualDepthGeometry setCount:]
+ -[ADVisualDepthGeometry setOffset:]
+ -[ADVisualDepthGeometry setStride:]
+ -[ADVisualDepthGeometry stride]
+ -[ADVisualDepthKeyframeInput .cxx_destruct]
+ -[ADVisualDepthKeyframeInput addKeyframe:]
+ -[ADVisualDepthKeyframeInput clear]
+ -[ADVisualDepthKeyframeInput init]
+ -[ADVisualDepthKeyframeInput meshKeyframes]
+ -[ADVisualDepthKeyframeInput metricDepth]
+ -[ADVisualDepthKeyframeInput removeKeyframeWithUUID:]
+ -[ADVisualDepthKeyframeInput setMetricDepth:]
+ -[ADVisualDepthMeshChunk .cxx_destruct]
+ -[ADVisualDepthMeshChunk classification]
+ -[ADVisualDepthMeshChunk confidence]
+ -[ADVisualDepthMeshChunk faces]
+ -[ADVisualDepthMeshChunk initWithFile:]
+ -[ADVisualDepthMeshChunk initWithVertices:faces:confidence:classification:transform:uuid:timestamp:]
+ -[ADVisualDepthMeshChunk initWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:]
+ -[ADVisualDepthMeshChunk init]
+ -[ADVisualDepthMeshChunk longRange]
+ -[ADVisualDepthMeshChunk setClassification:]
+ -[ADVisualDepthMeshChunk setConfidence:]
+ -[ADVisualDepthMeshChunk setFaces:]
+ -[ADVisualDepthMeshChunk setLongRange:]
+ -[ADVisualDepthMeshChunk setTimestamp:]
+ -[ADVisualDepthMeshChunk setTransform:]
+ -[ADVisualDepthMeshChunk setUuid:]
+ -[ADVisualDepthMeshChunk setVertices:]
+ -[ADVisualDepthMeshChunk timestamp]
+ -[ADVisualDepthMeshChunk transform]
+ -[ADVisualDepthMeshChunk uuid]
+ -[ADVisualDepthMeshChunk vertices]
+ -[ADVisualDepthMeshChunk writeToFile:atomically:]
+ -[ADVisualDepthMeshInput .cxx_destruct]
+ -[ADVisualDepthMeshInput addChunk:]
+ -[ADVisualDepthMeshInput clear]
+ -[ADVisualDepthMeshInput init]
+ -[ADVisualDepthMeshInput meshChunks]
+ -[ADVisualDepthMeshInput removeChunkWithUUID:]
+ -[ADVisualDepthMetalDescriptor .cxx_destruct]
+ -[ADVisualDepthMetalDescriptor initWithColorInputSize:colorInputFormat:rasterizedMeshInputSize:occlusionSize:povcSize:predictsDisparity:]
+ -[ADVisualDepthMetalDescriptor primaryColorInput]
+ -[ADVisualDepthMetalDescriptor primaryOcclusionMapOutput]
+ -[ADVisualDepthMetalDescriptor primaryPredictionConfidenceOutput]
+ -[ADVisualDepthMetalDescriptor primaryPredictionOutput]
+ -[ADVisualDepthMetalDescriptor primaryRasterizedMeshInput]
+ -[ADVisualDepthMetalDescriptor secondaryColorInput]
+ -[ADVisualDepthMetalDescriptor secondaryOcclusionMapOutput]
+ -[ADVisualDepthMetalDescriptor secondaryPredictionConfidenceOutput]
+ -[ADVisualDepthMetalDescriptor secondaryPredictionOutput]
+ -[ADVisualDepthMetalDescriptor secondaryRasterizedMeshInput]
+ -[ADVisualDepthOutput .cxx_destruct]
+ -[ADVisualDepthOutput addPrimaryCalibration:secondaryCalibration:timestamp:]
+ -[ADVisualDepthOutput confidenceForPrimaryPoV]
+ -[ADVisualDepthOutput confidenceForSecondaryPoV]
+ -[ADVisualDepthOutput dealloc]
+ -[ADVisualDepthOutput depthForPrimaryPoV]
+ -[ADVisualDepthOutput depthForSecondaryPoV]
+ -[ADVisualDepthOutput initWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:]
+ -[ADVisualDepthOutput occlusionForPrimaryPoV]
+ -[ADVisualDepthOutput occlusionForSecondaryPoV]
+ -[ADVisualDepthOutput primaryPoVCameraCalibration]
+ -[ADVisualDepthOutput secondaryPoVCameraCalibration]
+ -[ADVisualDepthOutput timestamp]
+ -[ADVisualDepthPipeline .cxx_destruct]
+ -[ADVisualDepthPipeline addKeyframeInput:timestamp:]
+ -[ADVisualDepthPipeline addMeshInput:]
+ -[ADVisualDepthPipeline buildMetalPipelineWithQueue:lensDistortion:]
+ -[ADVisualDepthPipeline clearKeyframes:]
+ -[ADVisualDepthPipeline dealloc]
+ -[ADVisualDepthPipeline dropLastFrame:]
+ -[ADVisualDepthPipeline encodePredictionToCommandBuffer:primaryColorInput:secondaryColorInput:primaryPredictionOutput:secondaryPredictionOutput:primaryOcclusionOutput:secondaryOcclusionOutput:predictionTimestamp:predictionPose:poseSessionID:poseReinitCount:]
+ -[ADVisualDepthPipeline getMinDistanceForTimestamp:]
+ -[ADVisualDepthPipeline initWithMetalCommandQueue:dimensions:format:]
+ -[ADVisualDepthPipeline metalDescriptor]
+ -[ADVisualDepthPipeline numDynamicPixels]
+ -[ADVisualDepthPipeline pipelineParameters]
+ -[ADVisualDepthPipeline resetState]
+ -[ADVisualDepthPipeline setPipelineParameters:]
+ -[ADVisualDepthPipeline shouldExecuteForTimestamp:poseMillimeters:]
+ -[ADVisualDepthPipeline updateSceneMonitoringForTimestamp:]
+ -[ADVisualDepthPipelineParameters init]
+ -[AggregatedDataWrapper .cxx_construct]
+ -[AggregatedDataWrapper .cxx_destruct]
+ -[AggregatedDataWrapper aggData]
+ -[AggregatedDataWrapper init]
+ -[AggregatedDataWrapper setAggData:]
+ -[AggregatedDataWrapper setAggPoints:]
+ -[CVPixelBufferARCWrapper dealloc]
+ -[CVPixelBufferARCWrapper initWithPearlDepth:pearlDx:pearlDy:pearlScore:]
+ -[CVPixelBufferARCWrapper pearlDepth]
+ -[CVPixelBufferARCWrapper pearlDx]
+ -[CVPixelBufferARCWrapper pearlDy]
+ -[CVPixelBufferARCWrapper pearlScore]
+ -[CVPixelBufferARCWrapper setPearlDepth:]
+ -[CVPixelBufferARCWrapper setPearlDx:]
+ -[CVPixelBufferARCWrapper setPearlDy:]
+ -[CVPixelBufferARCWrapper setPearlScore:]
+ GCC_except_table1001
+ GCC_except_table1002
+ GCC_except_table1012
+ GCC_except_table1014
+ GCC_except_table1015
+ GCC_except_table1037
+ GCC_except_table1038
+ GCC_except_table1046
+ GCC_except_table1047
+ GCC_except_table1051
+ GCC_except_table1083
+ GCC_except_table1084
+ GCC_except_table1091
+ GCC_except_table1092
+ GCC_except_table1101
+ GCC_except_table1106
+ GCC_except_table1107
+ GCC_except_table1108
+ GCC_except_table1116
+ GCC_except_table1124
+ GCC_except_table1125
+ GCC_except_table1163
+ GCC_except_table1165
+ GCC_except_table1166
+ GCC_except_table1170
+ GCC_except_table1171
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1181
+ GCC_except_table1185
+ GCC_except_table1188
+ GCC_except_table1189
+ GCC_except_table1193
+ GCC_except_table1194
+ GCC_except_table1195
+ GCC_except_table1205
+ GCC_except_table1206
+ GCC_except_table1208
+ GCC_except_table1209
+ GCC_except_table1210
+ GCC_except_table1211
+ GCC_except_table1225
+ GCC_except_table1226
+ GCC_except_table1227
+ GCC_except_table1229
+ GCC_except_table1230
+ GCC_except_table1231
+ GCC_except_table1232
+ GCC_except_table1233
+ GCC_except_table1234
+ GCC_except_table1235
+ GCC_except_table1236
+ GCC_except_table1237
+ GCC_except_table1238
+ GCC_except_table1239
+ GCC_except_table1260
+ GCC_except_table1261
+ GCC_except_table1266
+ GCC_except_table1272
+ GCC_except_table1286
+ GCC_except_table1307
+ GCC_except_table1310
+ GCC_except_table1312
+ GCC_except_table1322
+ GCC_except_table1323
+ GCC_except_table1324
+ GCC_except_table1329
+ GCC_except_table1332
+ GCC_except_table1340
+ GCC_except_table1356
+ GCC_except_table1368
+ GCC_except_table1370
+ GCC_except_table1373
+ GCC_except_table1374
+ GCC_except_table1376
+ GCC_except_table1381
+ GCC_except_table1383
+ GCC_except_table141
+ GCC_except_table1526
+ GCC_except_table156
+ GCC_except_table1563
+ GCC_except_table1564
+ GCC_except_table1565
+ GCC_except_table1566
+ GCC_except_table157
+ GCC_except_table1570
+ GCC_except_table1571
+ GCC_except_table1575
+ GCC_except_table158
+ GCC_except_table1588
+ GCC_except_table1589
+ GCC_except_table1590
+ GCC_except_table1591
+ GCC_except_table1592
+ GCC_except_table1593
+ GCC_except_table1596
+ GCC_except_table1597
+ GCC_except_table1601
+ GCC_except_table1602
+ GCC_except_table1606
+ GCC_except_table1607
+ GCC_except_table1622
+ GCC_except_table1648
+ GCC_except_table165
+ GCC_except_table1652
+ GCC_except_table1655
+ GCC_except_table166
+ GCC_except_table1664
+ GCC_except_table1669
+ GCC_except_table168
+ GCC_except_table1685
+ GCC_except_table1691
+ GCC_except_table1692
+ GCC_except_table1749
+ GCC_except_table175
+ GCC_except_table1750
+ GCC_except_table176
+ GCC_except_table1761
+ GCC_except_table1769
+ GCC_except_table1773
+ GCC_except_table1779
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1784
+ GCC_except_table1786
+ GCC_except_table1789
+ GCC_except_table1790
+ GCC_except_table1791
+ GCC_except_table1793
+ GCC_except_table1799
+ GCC_except_table180
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1802
+ GCC_except_table1804
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table1822
+ GCC_except_table1823
+ GCC_except_table1824
+ GCC_except_table1826
+ GCC_except_table1830
+ GCC_except_table1831
+ GCC_except_table1833
+ GCC_except_table1838
+ GCC_except_table1839
+ GCC_except_table184
+ GCC_except_table1840
+ GCC_except_table1843
+ GCC_except_table1844
+ GCC_except_table1854
+ GCC_except_table1857
+ GCC_except_table1859
+ GCC_except_table1860
+ GCC_except_table1861
+ GCC_except_table1871
+ GCC_except_table1872
+ GCC_except_table1873
+ GCC_except_table1875
+ GCC_except_table1895
+ GCC_except_table1905
+ GCC_except_table1909
+ GCC_except_table1913
+ GCC_except_table1914
+ GCC_except_table1915
+ GCC_except_table1920
+ GCC_except_table1921
+ GCC_except_table1930
+ GCC_except_table1931
+ GCC_except_table1934
+ GCC_except_table1935
+ GCC_except_table1957
+ GCC_except_table1958
+ GCC_except_table1964
+ GCC_except_table1965
+ GCC_except_table1966
+ GCC_except_table1981
+ GCC_except_table199
+ GCC_except_table2001
+ GCC_except_table2002
+ GCC_except_table2010
+ GCC_except_table2011
+ GCC_except_table2076
+ GCC_except_table2077
+ GCC_except_table2094
+ GCC_except_table2095
+ GCC_except_table2100
+ GCC_except_table2109
+ GCC_except_table2120
+ GCC_except_table2121
+ GCC_except_table2122
+ GCC_except_table2123
+ GCC_except_table2125
+ GCC_except_table2128
+ GCC_except_table2129
+ GCC_except_table2147
+ GCC_except_table2148
+ GCC_except_table2153
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2160
+ GCC_except_table2162
+ GCC_except_table2164
+ GCC_except_table2165
+ GCC_except_table2166
+ GCC_except_table2167
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2172
+ GCC_except_table2173
+ GCC_except_table2175
+ GCC_except_table2177
+ GCC_except_table2178
+ GCC_except_table2179
+ GCC_except_table2181
+ GCC_except_table2182
+ GCC_except_table2183
+ GCC_except_table2184
+ GCC_except_table2191
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2194
+ GCC_except_table2201
+ GCC_except_table2202
+ GCC_except_table2216
+ GCC_except_table2219
+ GCC_except_table2220
+ GCC_except_table2221
+ GCC_except_table2224
+ GCC_except_table2225
+ GCC_except_table2227
+ GCC_except_table2229
+ GCC_except_table2230
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2237
+ GCC_except_table2238
+ GCC_except_table224
+ GCC_except_table2244
+ GCC_except_table2247
+ GCC_except_table2253
+ GCC_except_table2255
+ GCC_except_table2259
+ GCC_except_table2260
+ GCC_except_table2262
+ GCC_except_table2266
+ GCC_except_table2268
+ GCC_except_table2269
+ GCC_except_table2270
+ GCC_except_table2271
+ GCC_except_table2272
+ GCC_except_table2273
+ GCC_except_table2276
+ GCC_except_table2279
+ GCC_except_table2280
+ GCC_except_table2302
+ GCC_except_table2303
+ GCC_except_table2304
+ GCC_except_table2305
+ GCC_except_table2306
+ GCC_except_table2313
+ GCC_except_table2315
+ GCC_except_table2317
+ GCC_except_table2320
+ GCC_except_table2321
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2326
+ GCC_except_table2327
+ GCC_except_table233
+ GCC_except_table2333
+ GCC_except_table2334
+ GCC_except_table2339
+ GCC_except_table2345
+ GCC_except_table2346
+ GCC_except_table2347
+ GCC_except_table2348
+ GCC_except_table2349
+ GCC_except_table235
+ GCC_except_table2350
+ GCC_except_table2352
+ GCC_except_table2353
+ GCC_except_table2354
+ GCC_except_table2359
+ GCC_except_table2360
+ GCC_except_table2361
+ GCC_except_table2362
+ GCC_except_table2364
+ GCC_except_table2365
+ GCC_except_table2366
+ GCC_except_table2368
+ GCC_except_table2369
+ GCC_except_table237
+ GCC_except_table2371
+ GCC_except_table2372
+ GCC_except_table2378
+ GCC_except_table238
+ GCC_except_table2381
+ GCC_except_table2387
+ GCC_except_table239
+ GCC_except_table2390
+ GCC_except_table2393
+ GCC_except_table2396
+ GCC_except_table2399
+ GCC_except_table240
+ GCC_except_table2404
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table2446
+ GCC_except_table245
+ GCC_except_table2453
+ GCC_except_table2457
+ GCC_except_table2459
+ GCC_except_table2461
+ GCC_except_table2463
+ GCC_except_table2464
+ GCC_except_table2465
+ GCC_except_table2468
+ GCC_except_table2469
+ GCC_except_table2471
+ GCC_except_table2475
+ GCC_except_table2476
+ GCC_except_table2477
+ GCC_except_table2484
+ GCC_except_table2488
+ GCC_except_table2507
+ GCC_except_table2508
+ GCC_except_table2511
+ GCC_except_table2512
+ GCC_except_table2513
+ GCC_except_table2515
+ GCC_except_table2516
+ GCC_except_table2518
+ GCC_except_table2523
+ GCC_except_table2524
+ GCC_except_table2525
+ GCC_except_table2526
+ GCC_except_table2532
+ GCC_except_table254
+ GCC_except_table2540
+ GCC_except_table2541
+ GCC_except_table2542
+ GCC_except_table2543
+ GCC_except_table2546
+ GCC_except_table2547
+ GCC_except_table2548
+ GCC_except_table2549
+ GCC_except_table255
+ GCC_except_table2550
+ GCC_except_table2551
+ GCC_except_table2555
+ GCC_except_table2558
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table2577
+ GCC_except_table2578
+ GCC_except_table2579
+ GCC_except_table2580
+ GCC_except_table2581
+ GCC_except_table2582
+ GCC_except_table2583
+ GCC_except_table2584
+ GCC_except_table2585
+ GCC_except_table2587
+ GCC_except_table2594
+ GCC_except_table2595
+ GCC_except_table2596
+ GCC_except_table2597
+ GCC_except_table2598
+ GCC_except_table2599
+ GCC_except_table260
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2602
+ GCC_except_table2603
+ GCC_except_table2604
+ GCC_except_table2606
+ GCC_except_table2607
+ GCC_except_table2614
+ GCC_except_table2615
+ GCC_except_table2616
+ GCC_except_table262
+ GCC_except_table2620
+ GCC_except_table2621
+ GCC_except_table2622
+ GCC_except_table2624
+ GCC_except_table2625
+ GCC_except_table2627
+ GCC_except_table2628
+ GCC_except_table2630
+ GCC_except_table2631
+ GCC_except_table2633
+ GCC_except_table2634
+ GCC_except_table2636
+ GCC_except_table2637
+ GCC_except_table2639
+ GCC_except_table2645
+ GCC_except_table2646
+ GCC_except_table2647
+ GCC_except_table2648
+ GCC_except_table2649
+ GCC_except_table2650
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2658
+ GCC_except_table2661
+ GCC_except_table2662
+ GCC_except_table2666
+ GCC_except_table2667
+ GCC_except_table2668
+ GCC_except_table2669
+ GCC_except_table2672
+ GCC_except_table2673
+ GCC_except_table2674
+ GCC_except_table2678
+ GCC_except_table2694
+ GCC_except_table2697
+ GCC_except_table2698
+ GCC_except_table2699
+ GCC_except_table2700
+ GCC_except_table2704
+ GCC_except_table2707
+ GCC_except_table2708
+ GCC_except_table2709
+ GCC_except_table2710
+ GCC_except_table2711
+ GCC_except_table2716
+ GCC_except_table2717
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2729
+ GCC_except_table2732
+ GCC_except_table2733
+ GCC_except_table2734
+ GCC_except_table2735
+ GCC_except_table2737
+ GCC_except_table2739
+ GCC_except_table2747
+ GCC_except_table2749
+ GCC_except_table2750
+ GCC_except_table2751
+ GCC_except_table2752
+ GCC_except_table2753
+ GCC_except_table2755
+ GCC_except_table2757
+ GCC_except_table2759
+ GCC_except_table2760
+ GCC_except_table2761
+ GCC_except_table2768
+ GCC_except_table2769
+ GCC_except_table2782
+ GCC_except_table2783
+ GCC_except_table2784
+ GCC_except_table2787
+ GCC_except_table2796
+ GCC_except_table2797
+ GCC_except_table2798
+ GCC_except_table2799
+ GCC_except_table2818
+ GCC_except_table2821
+ GCC_except_table2822
+ GCC_except_table2823
+ GCC_except_table2824
+ GCC_except_table2825
+ GCC_except_table2826
+ GCC_except_table2827
+ GCC_except_table2829
+ GCC_except_table2834
+ GCC_except_table2845
+ GCC_except_table285
+ GCC_except_table2863
+ GCC_except_table2864
+ GCC_except_table2866
+ GCC_except_table2867
+ GCC_except_table2870
+ GCC_except_table2871
+ GCC_except_table2874
+ GCC_except_table2878
+ GCC_except_table2880
+ GCC_except_table2898
+ GCC_except_table2899
+ GCC_except_table2900
+ GCC_except_table2901
+ GCC_except_table2902
+ GCC_except_table2907
+ GCC_except_table2910
+ GCC_except_table292
+ GCC_except_table2923
+ GCC_except_table2939
+ GCC_except_table2942
+ GCC_except_table2943
+ GCC_except_table2947
+ GCC_except_table295
+ GCC_except_table2950
+ GCC_except_table2953
+ GCC_except_table296
+ GCC_except_table2975
+ GCC_except_table2982
+ GCC_except_table2983
+ GCC_except_table2988
+ GCC_except_table2989
+ GCC_except_table2990
+ GCC_except_table2991
+ GCC_except_table2992
+ GCC_except_table2993
+ GCC_except_table2994
+ GCC_except_table3022
+ GCC_except_table3023
+ GCC_except_table3029
+ GCC_except_table3036
+ GCC_except_table3037
+ GCC_except_table3038
+ GCC_except_table3047
+ GCC_except_table3048
+ GCC_except_table3049
+ GCC_except_table3051
+ GCC_except_table3052
+ GCC_except_table3053
+ GCC_except_table3054
+ GCC_except_table3056
+ GCC_except_table3057
+ GCC_except_table3058
+ GCC_except_table3063
+ GCC_except_table3066
+ GCC_except_table307
+ GCC_except_table3070
+ GCC_except_table3072
+ GCC_except_table3074
+ GCC_except_table3079
+ GCC_except_table3080
+ GCC_except_table3084
+ GCC_except_table3088
+ GCC_except_table3089
+ GCC_except_table3090
+ GCC_except_table3093
+ GCC_except_table3095
+ GCC_except_table3102
+ GCC_except_table3106
+ GCC_except_table3107
+ GCC_except_table3108
+ GCC_except_table3109
+ GCC_except_table311
+ GCC_except_table3110
+ GCC_except_table3111
+ GCC_except_table3112
+ GCC_except_table3113
+ GCC_except_table3120
+ GCC_except_table3121
+ GCC_except_table3122
+ GCC_except_table3126
+ GCC_except_table3127
+ GCC_except_table3129
+ GCC_except_table3134
+ GCC_except_table3136
+ GCC_except_table3141
+ GCC_except_table3142
+ GCC_except_table3144
+ GCC_except_table3145
+ GCC_except_table3147
+ GCC_except_table3148
+ GCC_except_table3149
+ GCC_except_table3150
+ GCC_except_table3154
+ GCC_except_table3156
+ GCC_except_table3157
+ GCC_except_table3158
+ GCC_except_table3163
+ GCC_except_table3170
+ GCC_except_table3173
+ GCC_except_table3174
+ GCC_except_table3182
+ GCC_except_table3185
+ GCC_except_table3194
+ GCC_except_table3195
+ GCC_except_table3196
+ GCC_except_table3200
+ GCC_except_table3214
+ GCC_except_table3215
+ GCC_except_table3218
+ GCC_except_table3219
+ GCC_except_table3220
+ GCC_except_table3222
+ GCC_except_table3223
+ GCC_except_table3224
+ GCC_except_table3225
+ GCC_except_table3226
+ GCC_except_table3227
+ GCC_except_table3229
+ GCC_except_table3238
+ GCC_except_table3239
+ GCC_except_table3240
+ GCC_except_table3241
+ GCC_except_table3254
+ GCC_except_table3262
+ GCC_except_table3263
+ GCC_except_table3271
+ GCC_except_table3280
+ GCC_except_table3281
+ GCC_except_table3286
+ GCC_except_table3287
+ GCC_except_table3288
+ GCC_except_table3289
+ GCC_except_table3290
+ GCC_except_table3294
+ GCC_except_table3295
+ GCC_except_table3296
+ GCC_except_table3297
+ GCC_except_table3298
+ GCC_except_table3299
+ GCC_except_table3301
+ GCC_except_table3304
+ GCC_except_table3305
+ GCC_except_table3306
+ GCC_except_table3307
+ GCC_except_table3308
+ GCC_except_table3309
+ GCC_except_table3316
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table385
+ GCC_except_table390
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table402
+ GCC_except_table403
+ GCC_except_table431
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table439
+ GCC_except_table443
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table459
+ GCC_except_table460
+ GCC_except_table477
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table522
+ GCC_except_table523
+ GCC_except_table524
+ GCC_except_table526
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table548
+ GCC_except_table549
+ GCC_except_table550
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table553
+ GCC_except_table559
+ GCC_except_table569
+ GCC_except_table570
+ GCC_except_table571
+ GCC_except_table572
+ GCC_except_table596
+ GCC_except_table618
+ GCC_except_table619
+ GCC_except_table620
+ GCC_except_table622
+ GCC_except_table623
+ GCC_except_table624
+ GCC_except_table625
+ GCC_except_table626
+ GCC_except_table628
+ GCC_except_table631
+ GCC_except_table632
+ GCC_except_table633
+ GCC_except_table650
+ GCC_except_table655
+ GCC_except_table667
+ GCC_except_table669
+ GCC_except_table671
+ GCC_except_table672
+ GCC_except_table704
+ GCC_except_table706
+ GCC_except_table711
+ GCC_except_table712
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table719
+ GCC_except_table72
+ GCC_except_table720
+ GCC_except_table721
+ GCC_except_table723
+ GCC_except_table724
+ GCC_except_table725
+ GCC_except_table739
+ GCC_except_table743
+ GCC_except_table745
+ GCC_except_table762
+ GCC_except_table769
+ GCC_except_table776
+ GCC_except_table780
+ GCC_except_table782
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table789
+ GCC_except_table806
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table822
+ GCC_except_table825
+ GCC_except_table877
+ GCC_except_table878
+ GCC_except_table879
+ GCC_except_table882
+ GCC_except_table890
+ GCC_except_table892
+ GCC_except_table893
+ GCC_except_table897
+ GCC_except_table898
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table931
+ GCC_except_table932
+ GCC_except_table94
+ GCC_except_table942
+ GCC_except_table944
+ GCC_except_table948
+ GCC_except_table949
+ GCC_except_table950
+ GCC_except_table953
+ GCC_except_table954
+ GCC_except_table955
+ GCC_except_table956
+ GCC_except_table957
+ GCC_except_table958
+ GCC_except_table959
+ GCC_except_table960
+ GCC_except_table961
+ GCC_except_table964
+ GCC_except_table966
+ GCC_except_table967
+ GCC_except_table968
+ GCC_except_table969
+ GCC_except_table970
+ GCC_except_table971
+ GCC_except_table987
+ GCC_except_table989
+ GCC_except_table990
+ GCC_except_table991
+ GCC_except_table992
+ GCC_except_table993
+ GCC_except_table995
+ _ADJasperPearlInFieldCalibration_DX_ATTACHMENT_KEY
+ _ADJasperPearlInFieldCalibration_DY_ATTACHMENT_KEY
+ _ADJasperPearlInFieldCalibration_PEARL_DEPTH_ATTACHMENTS_KEY
+ _ADJasperPearlInFieldCalibration_SCORE_ATTACHMENT_KEY
+ _JPC_MODULE
+ _OBJC_CLASS_$_ADAggregatedPointCloudRefiner
+ _OBJC_CLASS_$_ADBinocularDepthExecutor
+ _OBJC_CLASS_$_ADBinocularDepthExecutorParameters
+ _OBJC_CLASS_$_ADBinocularDepthFlow
+ _OBJC_CLASS_$_ADBinocularDepthOutput
+ _OBJC_CLASS_$_ADBinocularDepthPipeline
+ _OBJC_CLASS_$_ADBinocularDepthPipelineParameters
+ _OBJC_CLASS_$_ADBinocularDepthWarperMesh
+ _OBJC_CLASS_$_ADDensifiedLiDARFocusAssistFlow
+ _OBJC_CLASS_$_ADEspressoBinocularDepthInferenceDescriptor
+ _OBJC_CLASS_$_ADEspressoMetricDepthInferenceDescriptor
+ _OBJC_CLASS_$_ADFusedDepthLoggerHandler
+ _OBJC_CLASS_$_ADImageDimensions
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationExecutor
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationExecutorParameters
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationInterSessionData
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationJasperInput
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationPearlInput
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationPipeline
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationPipelineParameters
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationResult
+ _OBJC_CLASS_$_ADJasperPearlInFieldCalibrationTelemetry
+ _OBJC_CLASS_$_ADJasperPearlTelemetryData
+ _OBJC_CLASS_$_ADJasperPearlTriggeringTelemetryData
+ _OBJC_CLASS_$_ADLKTConfidenceParameters
+ _OBJC_CLASS_$_ADLKTExecutorParameters
+ _OBJC_CLASS_$_ADLKTFlow
+ _OBJC_CLASS_$_ADMetricDepthExecutor
+ _OBJC_CLASS_$_ADMetricDepthExecutorParameters
+ _OBJC_CLASS_$_ADMetricDepthFlow
+ _OBJC_CLASS_$_ADMetricDepthFrameStatistics
+ _OBJC_CLASS_$_ADMetricDepthPipeline
+ _OBJC_CLASS_$_ADMetricDepthPipelineParameters
+ _OBJC_CLASS_$_ADMillimeterRadiusPairsLensDistortionModel
+ _OBJC_CLASS_$_ADModelBuilder
+ _OBJC_CLASS_$_ADMonocularFlow
+ _OBJC_CLASS_$_ADMutableCameraCalibration
+ _OBJC_CLASS_$_ADVisualDepthBuffer
+ _OBJC_CLASS_$_ADVisualDepthExecutor
+ _OBJC_CLASS_$_ADVisualDepthExecutorParameters
+ _OBJC_CLASS_$_ADVisualDepthGeometry
+ _OBJC_CLASS_$_ADVisualDepthKeyframeInput
+ _OBJC_CLASS_$_ADVisualDepthMeshChunk
+ _OBJC_CLASS_$_ADVisualDepthMeshInput
+ _OBJC_CLASS_$_ADVisualDepthMetalDescriptor
+ _OBJC_CLASS_$_ADVisualDepthOutput
+ _OBJC_CLASS_$_ADVisualDepthPipeline
+ _OBJC_CLASS_$_ADVisualDepthPipelineParameters
+ _OBJC_CLASS_$_AggregatedDataWrapper
+ _OBJC_CLASS_$_CVPixelBufferARCWrapper
+ _OBJC_CLASS_$_MPSImageBilinearScale
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._colorScalingSession
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._coreAnalyticsToSaturationChecksRatio
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._espressoEngine
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._isPrepared
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmProcessedAuxColor
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmProcessedRefColor
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmRawAuxConfidence
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmRawAuxDisparity
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmRawAuxSegmentation
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._itmYUVColor
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._lastSaturationCheckTimestamp
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._numberOfSaturationChecks
+ _OBJC_IVAR_$_ADBinocularDepthExecutor._pipeline
+ _OBJC_IVAR_$_ADBinocularDepthExecutorParameters._coreAnalyticsEventInterval
+ _OBJC_IVAR_$_ADBinocularDepthExecutorParameters._pipelineParameters
+ _OBJC_IVAR_$_ADBinocularDepthExecutorParameters._saturationCheckInterval
+ _OBJC_IVAR_$_ADBinocularDepthExecutorParameters._saturationThreshold
+ _OBJC_IVAR_$_ADBinocularDepthFlow._executor
+ _OBJC_IVAR_$_ADBinocularDepthFlow._frameOutputPool
+ _OBJC_IVAR_$_ADBinocularDepthFlow._streamSync
+ _OBJC_IVAR_$_ADBinocularDepthOutput._auxConfidence
+ _OBJC_IVAR_$_ADBinocularDepthOutput._auxDepth
+ _OBJC_IVAR_$_ADBinocularDepthOutput._auxOutputCalibration
+ _OBJC_IVAR_$_ADBinocularDepthOutput._auxSegmentation
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._auxCalib
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._auxOutputCalib
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._auxRectifiedCalib
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._auxWarper
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._inferenceDescriptor
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._networkProvider
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._pipelineParameters
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._prioritization
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._refCalib
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._refRectifiedCalib
+ _OBJC_IVAR_$_ADBinocularDepthPipeline._refWarper
+ _OBJC_IVAR_$_ADBinocularDepthPipelineParameters._confidenceUnits
+ _OBJC_IVAR_$_ADBinocularDepthPipelineParameters._rectifiedCameraFieldOfViewHeight
+ _OBJC_IVAR_$_ADBinocularDepthPipelineParameters._rectifiedCameraFieldOfViewWidth
+ _OBJC_IVAR_$_ADBinocularDepthWarperMesh._undistortHalvedMaps
+ _OBJC_IVAR_$_ADBinocularDepthWarperMesh._undistortMaps
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistExecutor._dbgPointCloudCropped
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistExecutor._expectedSensorCrop
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistExecutor._validDepthRect
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistExecutorParameters._autoSetColorROI
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._canDelegateFailure
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._canDelegateProcess
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._delegate
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._executor
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._streamSync
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistFlow._transformKey
+ _OBJC_IVAR_$_ADDensifiedLiDARFocusAssistPipeline._teleAfType
+ _OBJC_IVAR_$_ADEspressoBinocularDepthInferenceDescriptor._auxiliaryColorInput
+ _OBJC_IVAR_$_ADEspressoBinocularDepthInferenceDescriptor._auxiliaryConfidenceOutput
+ _OBJC_IVAR_$_ADEspressoBinocularDepthInferenceDescriptor._auxiliaryDisparityOutput
+ _OBJC_IVAR_$_ADEspressoBinocularDepthInferenceDescriptor._auxiliarySegmentationOutput
+ _OBJC_IVAR_$_ADEspressoBinocularDepthInferenceDescriptor._referenceColorInput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._cameraEmbeddingInput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._confidenceOutput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._depthOutput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._jasperInput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._normalsOutput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._pearlInput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._primaryColorInput
+ _OBJC_IVAR_$_ADEspressoMetricDepthInferenceDescriptor._secondaryColorInput
+ _OBJC_IVAR_$_ADExecutorParameters._stepsToExecute
+ _OBJC_IVAR_$_ADJasperColorExecutor._opticalFlowAllocated
+ _OBJC_IVAR_$_ADJasperColorExecutor._pcRefiner
+ _OBJC_IVAR_$_ADJasperColorExecutor._vioTemporalAllocated
+ _OBJC_IVAR_$_ADJasperColorExecutorParameters._ignoreDistortionInDepthReprojection
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._lastKnownGoodFramesCount
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._sdfHistoryFrames
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._sdfHistoryRollingIndex
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._sdfHistorySize
+ _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipelineParameters._sdfHistorySize
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._currentExtrinsics
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._extrinsicsMode
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._isFirstFrame
+ _OBJC_IVAR_$_ADJasperColorInfieldCalibrationFlow._lastExtrinsicsFromInput
+ _OBJC_IVAR_$_ADJasperColorV2Pipeline._pcRefiner
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._aggregatedPointCloud
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._isPrepared
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._lastStreamSyncMatchLock
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._lastSyncMatch
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._pcAggregator
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._pceCalib
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._pearlInfraredCameraCalibration
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._pipeline
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._processedJasper
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutor._streamSync
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationExecutorParameters._pipelineParameters
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._aggPointsWrapperObj
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._diagnosticPipelineLog
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._diagnosticPipelineLogIndex
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._firstIFAFrameTimestampCurrentExecution
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._firstTimeEventFired
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._irCamFOVCoveragePercent
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._lastAlgoRadarTriggerTimestamp
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._lastIFAFrameTimestampCurrentExecution
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._lastPearlTemp
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._maxIRCamTemperatureCurrentExecution
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._minIRCamTemperatureCurrentExecution
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._numOfIFAFramesCurrentExecution
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._numOfUniqueTOFSpots
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._rotArray
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationInterSessionData._transArray
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationJasperInput._bankPointCloud
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationJasperInput._jasperBankPose
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationJasperInput._timestamp
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._depth
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._dx
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._dy
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._pose
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._prevPose
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._score
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._temperature
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPearlInput._timestamp
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipeline._pceCalib
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipeline._pipelineParameters
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._isReportTelemetry
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._logger
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._pointCloudAggregationParameters
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._pointCloudFilterParameters
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._skipISF
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationPipelineParameters._stepsToExecute
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._efl
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._pceCalib
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._principalPointX
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._principalPointY
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._telemetryData
+ _OBJC_IVAR_$_ADJasperPearlInFieldCalibrationResult._temperature
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._depthDiffThresholdAboveMedian
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjErrorCode
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjOutputValidationErrorCode
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjPPXChangeMicronFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjPPXChangeMicronFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjPPYChangeMicronFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjPPYChangeMicronFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotXChangeFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotXChangeFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotYChangeFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotYChangeFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotZChangeFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjProjRotZChangeFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjScaleChangePercentFromPrev
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._gmcjScaleChangePercentFromT0
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._intervalBetweenIFAFrames
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._irCamFOVCoveragePercent
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedGMCJBlock
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedGMCJValidation
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedIFABlock
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedJasperReflectionsFrameFilter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedPipelineCurrent
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._isAssignedPipelinePrevious
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._jasperMisalignmentAfter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._jasperMisalignmentBefore
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._jpcErrorCode
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._maxIRCamTemperature
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._minIRCamTemperature
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesRotationX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesRotationY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesRotationZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesTranslationX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesTranslationY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._motionBetweenFramesTranslationZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newEfl
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newPPX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newPPY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newRotX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newRotY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._newRotZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numJasperSpotsFlaggedAsGlare
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numJasperSpotsFlaggedAsReflectiveSurface
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numOfAggregatedFrames
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numOfUniqueTOFSpots
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlJasperCorrespondencesPostLocalDepthVarFilter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlJasperCorrespondencesPostPJDepthDiffFilter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlJasperCorrespondencesPreIFA
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlOnlyCorrespondencesPostSpatialCoverageFilter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._numPearlOnlyCorrespondencesPreIFA
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pceCalib
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlCalibSetSize
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlJapserCalibSetSize
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlTemperature
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankRotation
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankRotationX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankRotationY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankRotationZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankTranslation
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankTranslationX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankTranslationY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._pearlToLastJasperBankTranslationZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevEfl
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevPPX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevPPY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevRotX
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevRotY
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._prevRotZ
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._reprojectionErrorAfter
+ _OBJC_IVAR_$_ADJasperPearlTelemetryData._reprojectionErrorBefore
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerEndReasonIsConvergence
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerEndReasonIsMaxFrameCount
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerEndReasonIsOutputValidationMetricIncreased
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerFirstFrameTemperature
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerFirstFrameTimestamp
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerFrameCount
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerLastFrameTemperature
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caCurrentTriggerLastFrameTimestamp
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caLastTriggerLastFrameTemperature
+ _OBJC_IVAR_$_ADJasperPearlTriggeringTelemetryData._caLastTriggerLastFrameTimestamp
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._checkFlowInFOV
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._conditionNumberMaxValue
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._conditionNumberMinValue
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._gradientNormMaxValue
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._gradientNormMinValue
+ _OBJC_IVAR_$_ADLKTConfidenceParameters._scaleIdxForConfidenceComponents
+ _OBJC_IVAR_$_ADLKTExecutor._bilinearScaler
+ _OBJC_IVAR_$_ADLKTExecutor._colorConvertingSession
+ _OBJC_IVAR_$_ADLKTExecutor._downscaledInputSize
+ _OBJC_IVAR_$_ADLKTExecutor._downscaledInputTexture
+ _OBJC_IVAR_$_ADLKTExecutor._firstScaleStride
+ _OBJC_IVAR_$_ADLKTExecutor._greyscaleInput
+ _OBJC_IVAR_$_ADLKTExecutor._outputSize
+ _OBJC_IVAR_$_ADLKTExecutorParameters._confidenceParameters
+ _OBJC_IVAR_$_ADLKTExecutorParameters._confidenceUnits
+ _OBJC_IVAR_$_ADLKTFlow._canDelegateFailure
+ _OBJC_IVAR_$_ADLKTFlow._canDelegateProcess
+ _OBJC_IVAR_$_ADLKTFlow._delegate
+ _OBJC_IVAR_$_ADLKTFlow._executor
+ _OBJC_IVAR_$_ADLKTFlow._isTemporal
+ _OBJC_IVAR_$_ADLKTFlow._streamSync
+ _OBJC_IVAR_$_ADLKTOpticalFlow._conditionNumberConfidenceTex
+ _OBJC_IVAR_$_ADLKTOpticalFlow._confidenceParameters
+ _OBJC_IVAR_$_ADLKTOpticalFlow._firstScaleStride
+ _OBJC_IVAR_$_ADLKTOpticalFlow._gradientNormConfidenceTex
+ _OBJC_IVAR_$_ADLKTOpticalFlow._grayscaleTexture
+ _OBJC_IVAR_$_ADLKTTexturesDescriptor._confidenceDescriptor
+ _OBJC_IVAR_$_ADLKTTexturesDescriptor._downscaledInputDescriptor
+ _OBJC_IVAR_$_ADLKTTexturesDescriptor._outputDescriptor
+ _OBJC_IVAR_$_ADLogManager._counterTimestamp
+ _OBJC_IVAR_$_ADLogManager._forceCounterAsTimestamp
+ _OBJC_IVAR_$_ADLogManager._lastTimestamp
+ _OBJC_IVAR_$_ADMetricDepthExecutor._aggregatedPrimaryPointCloud
+ _OBJC_IVAR_$_ADMetricDepthExecutor._aggregatedSecondaryPointCloud
+ _OBJC_IVAR_$_ADMetricDepthExecutor._colorScalingSession
+ _OBJC_IVAR_$_ADMetricDepthExecutor._espressoEngine
+ _OBJC_IVAR_$_ADMetricDepthExecutor._isPrepared
+ _OBJC_IVAR_$_ADMetricDepthExecutor._itmPreProcessedCameraEmbBuffer
+ _OBJC_IVAR_$_ADMetricDepthExecutor._itmPreProcessedJasperEmbBuffer
+ _OBJC_IVAR_$_ADMetricDepthExecutor._itmPreProcessedPearl
+ _OBJC_IVAR_$_ADMetricDepthExecutor._itmPreProcessedPearlBuffer
+ _OBJC_IVAR_$_ADMetricDepthExecutor._itmPreProcessedPearlProjectedOnSecondary
+ _OBJC_IVAR_$_ADMetricDepthExecutor._lastFrameStatistics
+ _OBJC_IVAR_$_ADMetricDepthExecutor._pipeline
+ _OBJC_IVAR_$_ADMetricDepthExecutor._tiledView
+ _OBJC_IVAR_$_ADMetricDepthExecutorParameters._pipelineParameters
+ _OBJC_IVAR_$_ADMetricDepthFlow._executor
+ _OBJC_IVAR_$_ADMetricDepthFlow._frameOutputPool
+ _OBJC_IVAR_$_ADMetricDepthFlow._streamSync
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._allPosesValid
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._colorPoseRoll
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._depthSensorsIgnored
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._jasperInputSpotCount
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._jasperPoseDistance
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._jasperProjectedSpotCount
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._pearlProjectedPixelCount
+ _OBJC_IVAR_$_ADMetricDepthFrameStatistics._pearlProjectedPixelPercentage
+ _OBJC_IVAR_$_ADMetricDepthPipeline._backProjectedMap
+ _OBJC_IVAR_$_ADMetricDepthPipeline._cameraCenterEmbeddings
+ _OBJC_IVAR_$_ADMetricDepthPipeline._cameraRaysEmbeddings
+ _OBJC_IVAR_$_ADMetricDepthPipeline._downscaledJasperBuffer
+ _OBJC_IVAR_$_ADMetricDepthPipeline._inferenceDescriptor
+ _OBJC_IVAR_$_ADMetricDepthPipeline._jasperEmbeddings
+ _OBJC_IVAR_$_ADMetricDepthPipeline._lastCameraCalibration
+ _OBJC_IVAR_$_ADMetricDepthPipeline._lastPose
+ _OBJC_IVAR_$_ADMetricDepthPipeline._lastSize
+ _OBJC_IVAR_$_ADMetricDepthPipeline._networkProvider
+ _OBJC_IVAR_$_ADMetricDepthPipeline._pearlReprojector
+ _OBJC_IVAR_$_ADMetricDepthPipeline._pipelineParameters
+ _OBJC_IVAR_$_ADMetricDepthPipeline._pixelsMap
+ _OBJC_IVAR_$_ADMetricDepthPipeline._postProcessedMetricActiveDepthMaskDesc
+ _OBJC_IVAR_$_ADMetricDepthPipeline._postProcessedMetricConfLevelsDesc
+ _OBJC_IVAR_$_ADMetricDepthPipeline._raysMap
+ _OBJC_IVAR_$_ADMetricDepthPipeline._targetPearlBuffer
+ _OBJC_IVAR_$_ADMetricDepthPipeline._zMap
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._aggregationParameters
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._confidenceBucketingHighThreshold
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._confidenceBucketingLowThreshold
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._confidenceLevelRanges
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._confidenceUnits
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._maxCenterResolution
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._maxJasperDepth
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._maxRaysResolution
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._numCenterBands
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._numJasperBands
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._numRaysBands
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._pearlJasperCoFilteringMaxAllowedDisagreement
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._pearlJasperCoFilteringMaxPearlDepth
+ _OBJC_IVAR_$_ADMetricDepthPipelineParameters._pointCloudFilter
+ _OBJC_IVAR_$_ADMonocularExecutor._prepared
+ _OBJC_IVAR_$_ADMonocularFlow._executor
+ _OBJC_IVAR_$_ADNetworkProvider._knownConfigs
+ _OBJC_IVAR_$_ADNetworkProvider._modelBuilder
+ _OBJC_IVAR_$_ADPipelineParameters._requestedDimensions
+ _OBJC_IVAR_$_ADVisualDepthBuffer._calibration
+ _OBJC_IVAR_$_ADVisualDepthBuffer._confidence
+ _OBJC_IVAR_$_ADVisualDepthBuffer._image
+ _OBJC_IVAR_$_ADVisualDepthBuffer._labels
+ _OBJC_IVAR_$_ADVisualDepthBuffer._normals
+ _OBJC_IVAR_$_ADVisualDepthBuffer._pose
+ _OBJC_IVAR_$_ADVisualDepthBuffer._timestamp
+ _OBJC_IVAR_$_ADVisualDepthBuffer._uuid
+ _OBJC_IVAR_$_ADVisualDepthExecutor._completionEvent
+ _OBJC_IVAR_$_ADVisualDepthExecutor._keyframeInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._lastReceivedPrimaryColor
+ _OBJC_IVAR_$_ADVisualDepthExecutor._lastReceivedPrimaryColorPose
+ _OBJC_IVAR_$_ADVisualDepthExecutor._lastReceivedPrimaryColorTimestamp
+ _OBJC_IVAR_$_ADVisualDepthExecutor._lastReceivedSecondaryColor
+ _OBJC_IVAR_$_ADVisualDepthExecutor._meshInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._mtlCommandQueue
+ _OBJC_IVAR_$_ADVisualDepthExecutor._mtlDevice
+ _OBJC_IVAR_$_ADVisualDepthExecutor._pipeline
+ _OBJC_IVAR_$_ADVisualDepthExecutor._primaryColorCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._primaryDisparityCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._primaryTargetCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._requiredVDInit
+ _OBJC_IVAR_$_ADVisualDepthExecutor._secondaryColorCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._secondaryDisparityCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._secondaryTargetCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdColorInputCrop
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryConfOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryDepthOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryItm1
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryItm2
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryMeshIntermediate
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdPrimaryOcclusionOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryConfOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryDepthOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryItm1
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryItm2
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryMeshIntermediate
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSecondaryOcclusionOutput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSqrtInfoPrimaryMeshInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._vdSqrtInfoSecondaryMeshInput
+ _OBJC_IVAR_$_ADVisualDepthExecutor._visualDepthResolution
+ _OBJC_IVAR_$_ADVisualDepthExecutorParameters._pipelineParameters
+ _OBJC_IVAR_$_ADVisualDepthGeometry._buffer
+ _OBJC_IVAR_$_ADVisualDepthGeometry._count
+ _OBJC_IVAR_$_ADVisualDepthGeometry._offset
+ _OBJC_IVAR_$_ADVisualDepthGeometry._stride
+ _OBJC_IVAR_$_ADVisualDepthKeyframeInput._MutableKeyframes
+ _OBJC_IVAR_$_ADVisualDepthKeyframeInput._metricDepth
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._classification
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._confidence
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._faces
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._longRange
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._timestamp
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._transform
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._uuid
+ _OBJC_IVAR_$_ADVisualDepthMeshChunk._vertices
+ _OBJC_IVAR_$_ADVisualDepthMeshInput._MutableMeshChunks
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._primaryColorInput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._primaryOcclusionMapOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._primaryPredictionConfidenceOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._primaryPredictionOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._primaryRasterizedMeshInput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._secondaryColorInput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._secondaryOcclusionMapOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._secondaryPredictionConfidenceOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._secondaryPredictionOutput
+ _OBJC_IVAR_$_ADVisualDepthMetalDescriptor._secondaryRasterizedMeshInput
+ _OBJC_IVAR_$_ADVisualDepthOutput._confidenceForPrimaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._confidenceForSecondaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._depthForPrimaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._depthForSecondaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._occlusionForPrimaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._occlusionForSecondaryPoV
+ _OBJC_IVAR_$_ADVisualDepthOutput._primaryPoVCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthOutput._secondaryPoVCameraCalibration
+ _OBJC_IVAR_$_ADVisualDepthOutput._timestamp
+ _OBJC_IVAR_$_ADVisualDepthPipeline._metalDesc
+ _OBJC_IVAR_$_ADVisualDepthPipeline._minPyramidLevel
+ _OBJC_IVAR_$_ADVisualDepthPipeline._numDynamicPixels
+ _OBJC_IVAR_$_ADVisualDepthPipeline._numPriorInputs
+ _OBJC_IVAR_$_ADVisualDepthPipeline._pipelineParameters
+ _OBJC_IVAR_$_ADVisualDepthPipeline._primaryCameraID
+ _OBJC_IVAR_$_ADVisualDepthPipeline._primaryMeshPriorIdx
+ _OBJC_IVAR_$_ADVisualDepthPipeline._secondaryCameraID
+ _OBJC_IVAR_$_ADVisualDepthPipeline._secondaryMeshPriorIdx
+ _OBJC_IVAR_$_AggregatedDataWrapper._aggData
+ _OBJC_IVAR_$_CVPixelBufferARCWrapper._pearlDepth
+ _OBJC_IVAR_$_CVPixelBufferARCWrapper._pearlDx
+ _OBJC_IVAR_$_CVPixelBufferARCWrapper._pearlDy
+ _OBJC_IVAR_$_CVPixelBufferARCWrapper._pearlScore
+ _OBJC_METACLASS_$_ADBinocularDepthExecutor
+ _OBJC_METACLASS_$_ADBinocularDepthExecutorParameters
+ _OBJC_METACLASS_$_ADBinocularDepthFlow
+ _OBJC_METACLASS_$_ADBinocularDepthOutput
+ _OBJC_METACLASS_$_ADBinocularDepthPipeline
+ _OBJC_METACLASS_$_ADBinocularDepthPipelineParameters
+ _OBJC_METACLASS_$_ADBinocularDepthWarperMesh
+ _OBJC_METACLASS_$_ADDensifiedLiDARFocusAssistFlow
+ _OBJC_METACLASS_$_ADEspressoBinocularDepthInferenceDescriptor
+ _OBJC_METACLASS_$_ADEspressoMetricDepthInferenceDescriptor
+ _OBJC_METACLASS_$_ADFusedDepthLoggerHandler
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationExecutor
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationExecutorParameters
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationInterSessionData
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationJasperInput
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationPearlInput
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationPipeline
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationPipelineParameters
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationResult
+ _OBJC_METACLASS_$_ADJasperPearlInFieldCalibrationTelemetry
+ _OBJC_METACLASS_$_ADJasperPearlTelemetryData
+ _OBJC_METACLASS_$_ADJasperPearlTriggeringTelemetryData
+ _OBJC_METACLASS_$_ADLKTConfidenceParameters
+ _OBJC_METACLASS_$_ADLKTExecutorParameters
+ _OBJC_METACLASS_$_ADLKTFlow
+ _OBJC_METACLASS_$_ADMetricDepthExecutor
+ _OBJC_METACLASS_$_ADMetricDepthExecutorParameters
+ _OBJC_METACLASS_$_ADMetricDepthFlow
+ _OBJC_METACLASS_$_ADMetricDepthFrameStatistics
+ _OBJC_METACLASS_$_ADMetricDepthPipeline
+ _OBJC_METACLASS_$_ADMetricDepthPipelineParameters
+ _OBJC_METACLASS_$_ADMonocularFlow
+ _OBJC_METACLASS_$_ADVisualDepthBuffer
+ _OBJC_METACLASS_$_ADVisualDepthExecutor
+ _OBJC_METACLASS_$_ADVisualDepthExecutorParameters
+ _OBJC_METACLASS_$_ADVisualDepthGeometry
+ _OBJC_METACLASS_$_ADVisualDepthKeyframeInput
+ _OBJC_METACLASS_$_ADVisualDepthMeshChunk
+ _OBJC_METACLASS_$_ADVisualDepthMeshInput
+ _OBJC_METACLASS_$_ADVisualDepthMetalDescriptor
+ _OBJC_METACLASS_$_ADVisualDepthOutput
+ _OBJC_METACLASS_$_ADVisualDepthPipeline
+ _OBJC_METACLASS_$_ADVisualDepthPipelineParameters
+ _OBJC_METACLASS_$_AggregatedDataWrapper
+ _OBJC_METACLASS_$_CVPixelBufferARCWrapper
+ __OBJC_$_CLASS_METHODS_ADBinocularDepthOutput
+ __OBJC_$_CLASS_METHODS_ADBinocularDepthWarperMesh
+ __OBJC_$_CLASS_METHODS_ADJasperColorExecutor
+ __OBJC_$_CLASS_METHODS_ADJasperColorInFieldCalibrationControllerParameters
+ __OBJC_$_CLASS_METHODS_ADJasperColorInFieldCalibrationExecutor
+ __OBJC_$_CLASS_METHODS_ADJasperColorInFieldCalibrationInterSessionData
+ __OBJC_$_CLASS_METHODS_ADJasperColorInFieldCalibrationPipelineParameters
+ __OBJC_$_CLASS_METHODS_ADJasperPearlInFieldCalibrationTelemetry
+ __OBJC_$_CLASS_METHODS_ADMetricDepthExecutor
+ __OBJC_$_CLASS_METHODS_ADMetricDepthPipeline
+ __OBJC_$_CLASS_METHODS_ADMetricDepthPipelineParameters
+ __OBJC_$_CLASS_METHODS_ADPearlColorInFieldCalibrationInterSessionData
+ __OBJC_$_CLASS_METHODS_ADPearlColorInFieldCalibrationPipelineParameters
+ __OBJC_$_CLASS_METHODS_ADVisualDepthBuffer
+ __OBJC_$_CLASS_METHODS_ADVisualDepthMeshChunk
+ __OBJC_$_CLASS_METHODS_ADVisualDepthOutput
+ __OBJC_$_CLASS_METHODS_ADVisualDepthPipeline
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthExecutor
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthExecutorParameters
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthFlow
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthOutput
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthPipeline
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthPipelineParameters
+ __OBJC_$_INSTANCE_METHODS_ADBinocularDepthWarperMesh
+ __OBJC_$_INSTANCE_METHODS_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_$_INSTANCE_METHODS_ADEspressoBinocularDepthInferenceDescriptor
+ __OBJC_$_INSTANCE_METHODS_ADEspressoMetricDepthInferenceDescriptor
+ __OBJC_$_INSTANCE_METHODS_ADFusedDepthLoggerHandler
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationExecutor
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationExecutorParameters
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationInterSessionData
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationJasperInput
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationPearlInput
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationPipeline
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationPipelineParameters
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlInFieldCalibrationResult
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlTelemetryData
+ __OBJC_$_INSTANCE_METHODS_ADJasperPearlTriggeringTelemetryData
+ __OBJC_$_INSTANCE_METHODS_ADLKTConfidenceParameters
+ __OBJC_$_INSTANCE_METHODS_ADLKTExecutorParameters
+ __OBJC_$_INSTANCE_METHODS_ADLKTFlow
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthExecutor
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthExecutorParameters
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthFlow
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthFrameStatistics
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthPipeline
+ __OBJC_$_INSTANCE_METHODS_ADMetricDepthPipelineParameters
+ __OBJC_$_INSTANCE_METHODS_ADMonocularFlow
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthBuffer
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthExecutor
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthExecutorParameters
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthGeometry
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthKeyframeInput
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthMeshChunk
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthMeshInput
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthMetalDescriptor
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthOutput
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthPipeline
+ __OBJC_$_INSTANCE_METHODS_ADVisualDepthPipelineParameters
+ __OBJC_$_INSTANCE_METHODS_AggregatedDataWrapper
+ __OBJC_$_INSTANCE_METHODS_CVPixelBufferARCWrapper
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthExecutor
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthExecutorParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthOutput
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthPipeline
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthPipelineParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADBinocularDepthWarperMesh
+ __OBJC_$_INSTANCE_VARIABLES_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADEspressoBinocularDepthInferenceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_ADEspressoMetricDepthInferenceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationExecutor
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationExecutorParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationInterSessionData
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationJasperInput
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationPearlInput
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationPipeline
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationPipelineParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlInFieldCalibrationResult
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlTelemetryData
+ __OBJC_$_INSTANCE_VARIABLES_ADJasperPearlTriggeringTelemetryData
+ __OBJC_$_INSTANCE_VARIABLES_ADLKTConfidenceParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADLKTExecutorParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADLKTFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthExecutor
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthExecutorParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthFrameStatistics
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthPipeline
+ __OBJC_$_INSTANCE_VARIABLES_ADMetricDepthPipelineParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADMonocularFlow
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthBuffer
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthExecutor
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthExecutorParameters
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthGeometry
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthKeyframeInput
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthMeshChunk
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthMeshInput
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthMetalDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthOutput
+ __OBJC_$_INSTANCE_VARIABLES_ADVisualDepthPipeline
+ __OBJC_$_INSTANCE_VARIABLES_AggregatedDataWrapper
+ __OBJC_$_INSTANCE_VARIABLES_CVPixelBufferARCWrapper
+ __OBJC_$_PROP_LIST_ADBinocularDepthExecutor
+ __OBJC_$_PROP_LIST_ADBinocularDepthExecutorParameters
+ __OBJC_$_PROP_LIST_ADBinocularDepthFlow
+ __OBJC_$_PROP_LIST_ADBinocularDepthOutput
+ __OBJC_$_PROP_LIST_ADBinocularDepthPipeline
+ __OBJC_$_PROP_LIST_ADBinocularDepthPipelineParameters
+ __OBJC_$_PROP_LIST_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_$_PROP_LIST_ADEspressoBinocularDepthInferenceDescriptor
+ __OBJC_$_PROP_LIST_ADEspressoMetricDepthInferenceDescriptor
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationExecutor
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationExecutorParameters
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationInterSessionData
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationJasperInput
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationPearlInput
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationPipeline
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationPipelineParameters
+ __OBJC_$_PROP_LIST_ADJasperPearlInFieldCalibrationResult
+ __OBJC_$_PROP_LIST_ADJasperPearlTelemetryData
+ __OBJC_$_PROP_LIST_ADJasperPearlTriggeringTelemetryData
+ __OBJC_$_PROP_LIST_ADLKTConfidenceParameters
+ __OBJC_$_PROP_LIST_ADLKTExecutor
+ __OBJC_$_PROP_LIST_ADLKTExecutorParameters
+ __OBJC_$_PROP_LIST_ADLKTFlow
+ __OBJC_$_PROP_LIST_ADLKTOpticalFlow
+ __OBJC_$_PROP_LIST_ADMetricDepthExecutor
+ __OBJC_$_PROP_LIST_ADMetricDepthExecutorParameters
+ __OBJC_$_PROP_LIST_ADMetricDepthFlow
+ __OBJC_$_PROP_LIST_ADMetricDepthFrameStatistics
+ __OBJC_$_PROP_LIST_ADMetricDepthPipeline
+ __OBJC_$_PROP_LIST_ADMetricDepthPipelineParameters
+ __OBJC_$_PROP_LIST_ADMonocularFlow
+ __OBJC_$_PROP_LIST_ADVisualDepthBuffer
+ __OBJC_$_PROP_LIST_ADVisualDepthExecutor
+ __OBJC_$_PROP_LIST_ADVisualDepthExecutorParameters
+ __OBJC_$_PROP_LIST_ADVisualDepthGeometry
+ __OBJC_$_PROP_LIST_ADVisualDepthKeyframeInput
+ __OBJC_$_PROP_LIST_ADVisualDepthMeshChunk
+ __OBJC_$_PROP_LIST_ADVisualDepthMeshInput
+ __OBJC_$_PROP_LIST_ADVisualDepthMetalDescriptor
+ __OBJC_$_PROP_LIST_ADVisualDepthOutput
+ __OBJC_$_PROP_LIST_ADVisualDepthPipeline
+ __OBJC_$_PROP_LIST_AggregatedDataWrapper
+ __OBJC_$_PROP_LIST_CVPixelBufferARCWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADFlowSecondaryColorConsumer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADFlowSecondaryColorConsumer
+ __OBJC_$_PROTOCOL_REFS_ADFlowSecondaryColorConsumer
+ __OBJC_CLASS_PROTOCOLS_$_ADBinocularDepthFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADLKTFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADMetricDepthFlow
+ __OBJC_CLASS_PROTOCOLS_$_ADMonocularFlow
+ __OBJC_CLASS_RO_$_ADBinocularDepthExecutor
+ __OBJC_CLASS_RO_$_ADBinocularDepthExecutorParameters
+ __OBJC_CLASS_RO_$_ADBinocularDepthFlow
+ __OBJC_CLASS_RO_$_ADBinocularDepthOutput
+ __OBJC_CLASS_RO_$_ADBinocularDepthPipeline
+ __OBJC_CLASS_RO_$_ADBinocularDepthPipelineParameters
+ __OBJC_CLASS_RO_$_ADBinocularDepthWarperMesh
+ __OBJC_CLASS_RO_$_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_CLASS_RO_$_ADEspressoBinocularDepthInferenceDescriptor
+ __OBJC_CLASS_RO_$_ADEspressoMetricDepthInferenceDescriptor
+ __OBJC_CLASS_RO_$_ADFusedDepthLoggerHandler
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationExecutor
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationExecutorParameters
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationInterSessionData
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationJasperInput
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationPearlInput
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationPipeline
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationPipelineParameters
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationResult
+ __OBJC_CLASS_RO_$_ADJasperPearlInFieldCalibrationTelemetry
+ __OBJC_CLASS_RO_$_ADJasperPearlTelemetryData
+ __OBJC_CLASS_RO_$_ADJasperPearlTriggeringTelemetryData
+ __OBJC_CLASS_RO_$_ADLKTConfidenceParameters
+ __OBJC_CLASS_RO_$_ADLKTExecutorParameters
+ __OBJC_CLASS_RO_$_ADLKTFlow
+ __OBJC_CLASS_RO_$_ADMetricDepthExecutor
+ __OBJC_CLASS_RO_$_ADMetricDepthExecutorParameters
+ __OBJC_CLASS_RO_$_ADMetricDepthFlow
+ __OBJC_CLASS_RO_$_ADMetricDepthFrameStatistics
+ __OBJC_CLASS_RO_$_ADMetricDepthPipeline
+ __OBJC_CLASS_RO_$_ADMetricDepthPipelineParameters
+ __OBJC_CLASS_RO_$_ADMonocularFlow
+ __OBJC_CLASS_RO_$_ADVisualDepthBuffer
+ __OBJC_CLASS_RO_$_ADVisualDepthExecutor
+ __OBJC_CLASS_RO_$_ADVisualDepthExecutorParameters
+ __OBJC_CLASS_RO_$_ADVisualDepthGeometry
+ __OBJC_CLASS_RO_$_ADVisualDepthKeyframeInput
+ __OBJC_CLASS_RO_$_ADVisualDepthMeshChunk
+ __OBJC_CLASS_RO_$_ADVisualDepthMeshInput
+ __OBJC_CLASS_RO_$_ADVisualDepthMetalDescriptor
+ __OBJC_CLASS_RO_$_ADVisualDepthOutput
+ __OBJC_CLASS_RO_$_ADVisualDepthPipeline
+ __OBJC_CLASS_RO_$_ADVisualDepthPipelineParameters
+ __OBJC_CLASS_RO_$_AggregatedDataWrapper
+ __OBJC_CLASS_RO_$_CVPixelBufferARCWrapper
+ __OBJC_LABEL_PROTOCOL_$_ADFlowSecondaryColorConsumer
+ __OBJC_METACLASS_RO_$_ADBinocularDepthExecutor
+ __OBJC_METACLASS_RO_$_ADBinocularDepthExecutorParameters
+ __OBJC_METACLASS_RO_$_ADBinocularDepthFlow
+ __OBJC_METACLASS_RO_$_ADBinocularDepthOutput
+ __OBJC_METACLASS_RO_$_ADBinocularDepthPipeline
+ __OBJC_METACLASS_RO_$_ADBinocularDepthPipelineParameters
+ __OBJC_METACLASS_RO_$_ADBinocularDepthWarperMesh
+ __OBJC_METACLASS_RO_$_ADDensifiedLiDARFocusAssistFlow
+ __OBJC_METACLASS_RO_$_ADEspressoBinocularDepthInferenceDescriptor
+ __OBJC_METACLASS_RO_$_ADEspressoMetricDepthInferenceDescriptor
+ __OBJC_METACLASS_RO_$_ADFusedDepthLoggerHandler
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationExecutor
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationExecutorParameters
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationInterSessionData
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationJasperInput
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationPearlInput
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationPipeline
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationPipelineParameters
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationResult
+ __OBJC_METACLASS_RO_$_ADJasperPearlInFieldCalibrationTelemetry
+ __OBJC_METACLASS_RO_$_ADJasperPearlTelemetryData
+ __OBJC_METACLASS_RO_$_ADJasperPearlTriggeringTelemetryData
+ __OBJC_METACLASS_RO_$_ADLKTConfidenceParameters
+ __OBJC_METACLASS_RO_$_ADLKTExecutorParameters
+ __OBJC_METACLASS_RO_$_ADLKTFlow
+ __OBJC_METACLASS_RO_$_ADMetricDepthExecutor
+ __OBJC_METACLASS_RO_$_ADMetricDepthExecutorParameters
+ __OBJC_METACLASS_RO_$_ADMetricDepthFlow
+ __OBJC_METACLASS_RO_$_ADMetricDepthFrameStatistics
+ __OBJC_METACLASS_RO_$_ADMetricDepthPipeline
+ __OBJC_METACLASS_RO_$_ADMetricDepthPipelineParameters
+ __OBJC_METACLASS_RO_$_ADMonocularFlow
+ __OBJC_METACLASS_RO_$_ADVisualDepthBuffer
+ __OBJC_METACLASS_RO_$_ADVisualDepthExecutor
+ __OBJC_METACLASS_RO_$_ADVisualDepthExecutorParameters
+ __OBJC_METACLASS_RO_$_ADVisualDepthGeometry
+ __OBJC_METACLASS_RO_$_ADVisualDepthKeyframeInput
+ __OBJC_METACLASS_RO_$_ADVisualDepthMeshChunk
+ __OBJC_METACLASS_RO_$_ADVisualDepthMeshInput
+ __OBJC_METACLASS_RO_$_ADVisualDepthMetalDescriptor
+ __OBJC_METACLASS_RO_$_ADVisualDepthOutput
+ __OBJC_METACLASS_RO_$_ADVisualDepthPipeline
+ __OBJC_METACLASS_RO_$_ADVisualDepthPipelineParameters
+ __OBJC_METACLASS_RO_$_AggregatedDataWrapper
+ __OBJC_METACLASS_RO_$_CVPixelBufferARCWrapper
+ __OBJC_PROTOCOL_$_ADFlowSecondaryColorConsumer
+ __PromotedConst.9720
+ __PromotedConst.9721
+ __Z12GMCAlgorithmR11MatrixNxPtsILj3EdES1_S1_RKS_ILj1EdER11_GMC_ParamsR9MatrixMxNILj3ELj3EdEP12_GMC_ResultsP18GMCInnerStatistics
+ __Z13GMC_UndistortR11MatrixNxPtsILj2EdES1_RK11_GMC_ParamsPS_ILj3EdES6_
+ __Z14GMC_ControllerR11MatrixNxPtsILj2EdES1_RS_ILj1EdER11_GMC_ParamsbbP12_GMC_ResultsP18GMCInnerStatistics
+ __Z14GMC_HomographyR11MatrixNxPtsILj3EdES1_RK11_GMC_Params
+ __Z14GMC_ValidationR11MatrixNxPtsILj2EdES1_RS_ILj1EdER11_GMC_ParamsRK12_GMC_ResultsP18GMCInnerStatistics
+ __Z15normalizeCoordsRK11MatrixNxPtsILj3EdERK9MatrixMxNILj3ELj3EdE
+ __Z17GMC_AmbiguityTestR11MatrixNxPtsILj3EdES1_R9MatrixMxNILj3ELj3EdERK11_GMC_ParamsdPbPd
+ __Z17GMC_ToleranceTestRK9MatrixMxNILj3ELj3EdER11_GMC_Params
+ __Z17GMC_ToleranceTestRK9MatrixMxNILj3ELj3EdER11_GMC_ParamsRS_ILj1ELj3EdE
+ __Z17Interp1WithExtrapId18LinearInterpolatorIdEEiRK11MatrixNxPtsILj1ET_ES6_S6_PS4_b
+ __Z17isResolutionRatiommdd
+ __Z17runGmcOnGmsBufferPKyiRK8PCECalibRK14PCEShiftParamsRK14PCEDepthConfigPdP18GMCInnerStatisticsb
+ __Z17runGmcOnGmsPointsPKyibRK8PCECalibRK14PCEDepthConfigRK14PCEShiftParamsdPdP18GMCInnerStatisticsib
+ __Z18GMC_Normalise2DPtsR11MatrixNxPtsILj3EdEPS0_P9MatrixMxNILj3ELj3EdE
+ __Z18countNonZeroValuesP10__CVBuffer
+ __Z19GMC_EssentialMatrixRK9MatrixMxNILj3ELj3EdERK11_GMC_ParamsPS0_
+ __Z19GMC_SingularityTestRK9MatrixMxNILj1ELj9EdEd
+ __Z19GMC_WorldFromPoints11MatrixNxPtsILj3EdES0_RK9MatrixMxNILj3ELj3EdES4_S4_RKS1_ILj1ELj3EdEb
+ __Z19calcProjectionDistsR11MatrixNxPtsILj3EdES1_R11_GMC_ParamsRS_ILj1EdEP21ProjectionDistResults
+ __Z20GMC_BundleAdjustmentRK11MatrixNxPtsILj3EdES2_RS0_RKS_ILj1EdERK9MatrixMxNILj3ELj3EdERKS7_ILj1ELj3EdERK11_GMC_ParamsPS8_PdSI_SI_PiSJ_
+ __Z20GMC_FaceCoverageTestRK11MatrixNxPtsILj3EdERK11_GMC_ParamsS_ILj1EdEPS_ILj1EbEPjPd
+ __Z21calcEpipolarDistancesR11MatrixNxPtsILj3EdES1_R9MatrixMxNILj3ELj3EdEPS_ILj1EdE
+ __Z22GMC_ExtractTestSamplesRK11MatrixNxPtsILj3EdES2_jPS0_S3_S3_S3_
+ __Z22findJasperMisalignmentRK11MatrixNxPtsILj1EdES2_RfS3_
+ __Z22rotationMatrixToAngles9MatrixMxNILj3ELj3EdE
+ __Z23GMC_RansacFitFundMatrixR11MatrixNxPtsILj3EdES1_R11_GMC_ParamsbRS_ILj1EbEP9MatrixMxNILj3ELj3EdEPS_ILj1EjEPjPbPd
+ __Z23GMC_SpatialCoverageTestRK11MatrixNxPtsILj3EdER11_GMC_ParamsPd
+ __Z23floatToStringScientificf
+ __Z24GMC_ConstrainWorldPointsR11MatrixNxPtsILj3EdES1_RK11_GMC_ParamsP9MatrixMxNILj3ELj3EdEPS_ILj1EjEPjPS0_SB_S7_SB_
+ __Z25DistortRadialLiteInternalIdEiRK6MatrixIT_EPS1_S5_iP11MatrixNxPtsILj2ES1_EbS1_bbb
+ __Z34updatePCECalibWithGMCStereoResults12_GMC_ResultsRK8PCECalibRS0_
+ __ZGVZ24+[ADLogManager defaults]E6result
+ __ZGVZ33+[ADJasperColorExecutor defaults]E6result
+ __ZGVZ33+[ADMetricDepthExecutor defaults]E6result
+ __ZGVZ33+[ADMetricDepthPipeline defaults]E6result
+ __ZGVZ33+[ADVisualDepthPipeline defaults]E6result
+ __ZGVZ43+[ADMetricDepthPipelineParameters defaults]E6result
+ __ZGVZ50+[ADPearlColorInFieldCalibrationPipeline defaults]E6result
+ __ZGVZ51+[ADJasperColorInFieldCalibrationExecutor defaults]E6result
+ __ZGVZ58+[ADPearlColorInFieldCalibrationInterSessionData defaults]E6result
+ __ZGVZ59+[ADJasperColorInFieldCalibrationInterSessionData defaults]E6result
+ __ZGVZ60+[ADPearlColorInFieldCalibrationPipelineParameters defaults]E6result
+ __ZGVZ61+[ADJasperColorInFieldCalibrationPipelineParameters defaults]E6result
+ __ZGVZ63+[ADJasperColorInFieldCalibrationControllerParameters defaults]E6result
+ __ZGVZN14BucketsFilters7BucketsEvE4inst
+ __ZGVZN3jpc12JPCPORConfig12PORISFConfigEvE6config
+ __ZGVZN3jpc12JPCPORConfig17PORIFABlockConfigEvE6config
+ __ZGVZN3jpc12JPCPORConfig18PORGMCJBlockConfigEvE6config
+ __ZGVZN3jpc12JPCPORConfig32PORPreprocessorFilterBlockConfigEvE11preferences
+ __ZGVZN3jpc12JPCPORConfig32PORPreprocessorFilterBlockConfigEvE6config
+ __ZL13diluteInliersRK11MatrixNxPtsILj1EjEjjPS0_
+ __ZL15INSTRUMENTS_ENDjyyyy.104
+ __ZL15INSTRUMENTS_ENDjyyyy.1102
+ __ZL15INSTRUMENTS_ENDjyyyy.1289
+ __ZL15INSTRUMENTS_ENDjyyyy.1396
+ __ZL15INSTRUMENTS_ENDjyyyy.1560
+ __ZL15INSTRUMENTS_ENDjyyyy.1592
+ __ZL15INSTRUMENTS_ENDjyyyy.165
+ __ZL15INSTRUMENTS_ENDjyyyy.1755
+ __ZL15INSTRUMENTS_ENDjyyyy.1942
+ __ZL15INSTRUMENTS_ENDjyyyy.2180
+ __ZL15INSTRUMENTS_ENDjyyyy.2389
+ __ZL15INSTRUMENTS_ENDjyyyy.243
+ __ZL15INSTRUMENTS_ENDjyyyy.2463
+ __ZL15INSTRUMENTS_ENDjyyyy.249
+ __ZL15INSTRUMENTS_ENDjyyyy.2510
+ __ZL15INSTRUMENTS_ENDjyyyy.2543
+ __ZL15INSTRUMENTS_ENDjyyyy.2549
+ __ZL15INSTRUMENTS_ENDjyyyy.260
+ __ZL15INSTRUMENTS_ENDjyyyy.271
+ __ZL15INSTRUMENTS_ENDjyyyy.2737
+ __ZL15INSTRUMENTS_ENDjyyyy.2808
+ __ZL15INSTRUMENTS_ENDjyyyy.3025
+ __ZL15INSTRUMENTS_ENDjyyyy.3039
+ __ZL15INSTRUMENTS_ENDjyyyy.3045
+ __ZL15INSTRUMENTS_ENDjyyyy.3286
+ __ZL15INSTRUMENTS_ENDjyyyy.343
+ __ZL15INSTRUMENTS_ENDjyyyy.3492
+ __ZL15INSTRUMENTS_ENDjyyyy.3502
+ __ZL15INSTRUMENTS_ENDjyyyy.3565
+ __ZL15INSTRUMENTS_ENDjyyyy.3746
+ __ZL15INSTRUMENTS_ENDjyyyy.3885
+ __ZL15INSTRUMENTS_ENDjyyyy.4234
+ __ZL15INSTRUMENTS_ENDjyyyy.4417
+ __ZL15INSTRUMENTS_ENDjyyyy.4591
+ __ZL15INSTRUMENTS_ENDjyyyy.471
+ __ZL15INSTRUMENTS_ENDjyyyy.4804
+ __ZL15INSTRUMENTS_ENDjyyyy.5273
+ __ZL15INSTRUMENTS_ENDjyyyy.5418
+ __ZL15INSTRUMENTS_ENDjyyyy.558
+ __ZL15INSTRUMENTS_ENDjyyyy.5647
+ __ZL15INSTRUMENTS_ENDjyyyy.5895
+ __ZL15INSTRUMENTS_ENDjyyyy.6119
+ __ZL15INSTRUMENTS_ENDjyyyy.6291
+ __ZL15INSTRUMENTS_ENDjyyyy.6407
+ __ZL15INSTRUMENTS_ENDjyyyy.6423
+ __ZL15INSTRUMENTS_ENDjyyyy.6609
+ __ZL15INSTRUMENTS_ENDjyyyy.6615
+ __ZL15INSTRUMENTS_ENDjyyyy.6745
+ __ZL15INSTRUMENTS_ENDjyyyy.6768
+ __ZL15INSTRUMENTS_ENDjyyyy.6793
+ __ZL15INSTRUMENTS_ENDjyyyy.709
+ __ZL15INSTRUMENTS_ENDjyyyy.7158
+ __ZL15INSTRUMENTS_ENDjyyyy.7198
+ __ZL15INSTRUMENTS_ENDjyyyy.7246
+ __ZL15INSTRUMENTS_ENDjyyyy.725
+ __ZL15INSTRUMENTS_ENDjyyyy.7357
+ __ZL15INSTRUMENTS_ENDjyyyy.7513
+ __ZL15INSTRUMENTS_ENDjyyyy.7696
+ __ZL15INSTRUMENTS_ENDjyyyy.7702
+ __ZL15INSTRUMENTS_ENDjyyyy.7758
+ __ZL15INSTRUMENTS_ENDjyyyy.7768
+ __ZL15INSTRUMENTS_ENDjyyyy.7918
+ __ZL15INSTRUMENTS_ENDjyyyy.8235
+ __ZL15INSTRUMENTS_ENDjyyyy.8261
+ __ZL15INSTRUMENTS_ENDjyyyy.8424
+ __ZL15INSTRUMENTS_ENDjyyyy.8448
+ __ZL15INSTRUMENTS_ENDjyyyy.8696
+ __ZL15INSTRUMENTS_ENDjyyyy.9232
+ __ZL15INSTRUMENTS_ENDjyyyy.9298
+ __ZL15INSTRUMENTS_ENDjyyyy.9481
+ __ZL15INSTRUMENTS_ENDjyyyy.9697
+ __ZL15INSTRUMENTS_ENDjyyyy.9703
+ __ZL15INSTRUMENTS_ENDjyyyy.98
+ __ZL15INSTRUMENTS_ENDjyyyy.990
+ __ZL17INSTRUMENTS_EVENTjyyyy.105
+ __ZL17INSTRUMENTS_EVENTjyyyy.1103
+ __ZL17INSTRUMENTS_EVENTjyyyy.1290
+ __ZL17INSTRUMENTS_EVENTjyyyy.1397
+ __ZL17INSTRUMENTS_EVENTjyyyy.1561
+ __ZL17INSTRUMENTS_EVENTjyyyy.1593
+ __ZL17INSTRUMENTS_EVENTjyyyy.166
+ __ZL17INSTRUMENTS_EVENTjyyyy.1756
+ __ZL17INSTRUMENTS_EVENTjyyyy.1943
+ __ZL17INSTRUMENTS_EVENTjyyyy.2181
+ __ZL17INSTRUMENTS_EVENTjyyyy.2390
+ __ZL17INSTRUMENTS_EVENTjyyyy.244
+ __ZL17INSTRUMENTS_EVENTjyyyy.2464
+ __ZL17INSTRUMENTS_EVENTjyyyy.250
+ __ZL17INSTRUMENTS_EVENTjyyyy.2511
+ __ZL17INSTRUMENTS_EVENTjyyyy.2544
+ __ZL17INSTRUMENTS_EVENTjyyyy.2550
+ __ZL17INSTRUMENTS_EVENTjyyyy.261
+ __ZL17INSTRUMENTS_EVENTjyyyy.272
+ __ZL17INSTRUMENTS_EVENTjyyyy.2738
+ __ZL17INSTRUMENTS_EVENTjyyyy.2809
+ __ZL17INSTRUMENTS_EVENTjyyyy.3026
+ __ZL17INSTRUMENTS_EVENTjyyyy.3040
+ __ZL17INSTRUMENTS_EVENTjyyyy.3046
+ __ZL17INSTRUMENTS_EVENTjyyyy.3287
+ __ZL17INSTRUMENTS_EVENTjyyyy.344
+ __ZL17INSTRUMENTS_EVENTjyyyy.3493
+ __ZL17INSTRUMENTS_EVENTjyyyy.3503
+ __ZL17INSTRUMENTS_EVENTjyyyy.3566
+ __ZL17INSTRUMENTS_EVENTjyyyy.3747
+ __ZL17INSTRUMENTS_EVENTjyyyy.3886
+ __ZL17INSTRUMENTS_EVENTjyyyy.4235
+ __ZL17INSTRUMENTS_EVENTjyyyy.4418
+ __ZL17INSTRUMENTS_EVENTjyyyy.4592
+ __ZL17INSTRUMENTS_EVENTjyyyy.472
+ __ZL17INSTRUMENTS_EVENTjyyyy.4805
+ __ZL17INSTRUMENTS_EVENTjyyyy.5274
+ __ZL17INSTRUMENTS_EVENTjyyyy.5419
+ __ZL17INSTRUMENTS_EVENTjyyyy.559
+ __ZL17INSTRUMENTS_EVENTjyyyy.5648
+ __ZL17INSTRUMENTS_EVENTjyyyy.5896
+ __ZL17INSTRUMENTS_EVENTjyyyy.6120
+ __ZL17INSTRUMENTS_EVENTjyyyy.6292
+ __ZL17INSTRUMENTS_EVENTjyyyy.6408
+ __ZL17INSTRUMENTS_EVENTjyyyy.6424
+ __ZL17INSTRUMENTS_EVENTjyyyy.6610
+ __ZL17INSTRUMENTS_EVENTjyyyy.6616
+ __ZL17INSTRUMENTS_EVENTjyyyy.6746
+ __ZL17INSTRUMENTS_EVENTjyyyy.6769
+ __ZL17INSTRUMENTS_EVENTjyyyy.6794
+ __ZL17INSTRUMENTS_EVENTjyyyy.710
+ __ZL17INSTRUMENTS_EVENTjyyyy.7159
+ __ZL17INSTRUMENTS_EVENTjyyyy.7199
+ __ZL17INSTRUMENTS_EVENTjyyyy.7247
+ __ZL17INSTRUMENTS_EVENTjyyyy.726
+ __ZL17INSTRUMENTS_EVENTjyyyy.7358
+ __ZL17INSTRUMENTS_EVENTjyyyy.7514
+ __ZL17INSTRUMENTS_EVENTjyyyy.7697
+ __ZL17INSTRUMENTS_EVENTjyyyy.7703
+ __ZL17INSTRUMENTS_EVENTjyyyy.7759
+ __ZL17INSTRUMENTS_EVENTjyyyy.7769
+ __ZL17INSTRUMENTS_EVENTjyyyy.7919
+ __ZL17INSTRUMENTS_EVENTjyyyy.8236
+ __ZL17INSTRUMENTS_EVENTjyyyy.8262
+ __ZL17INSTRUMENTS_EVENTjyyyy.8425
+ __ZL17INSTRUMENTS_EVENTjyyyy.8449
+ __ZL17INSTRUMENTS_EVENTjyyyy.8697
+ __ZL17INSTRUMENTS_EVENTjyyyy.9233
+ __ZL17INSTRUMENTS_EVENTjyyyy.9299
+ __ZL17INSTRUMENTS_EVENTjyyyy.9482
+ __ZL17INSTRUMENTS_EVENTjyyyy.9698
+ __ZL17INSTRUMENTS_EVENTjyyyy.9704
+ __ZL17INSTRUMENTS_EVENTjyyyy.99
+ __ZL17INSTRUMENTS_EVENTjyyyy.991
+ __ZL17INSTRUMENTS_STARTjyyyy.100
+ __ZL17INSTRUMENTS_STARTjyyyy.106
+ __ZL17INSTRUMENTS_STARTjyyyy.1104
+ __ZL17INSTRUMENTS_STARTjyyyy.1291
+ __ZL17INSTRUMENTS_STARTjyyyy.1398
+ __ZL17INSTRUMENTS_STARTjyyyy.1562
+ __ZL17INSTRUMENTS_STARTjyyyy.1594
+ __ZL17INSTRUMENTS_STARTjyyyy.167
+ __ZL17INSTRUMENTS_STARTjyyyy.1757
+ __ZL17INSTRUMENTS_STARTjyyyy.1944
+ __ZL17INSTRUMENTS_STARTjyyyy.2182
+ __ZL17INSTRUMENTS_STARTjyyyy.2391
+ __ZL17INSTRUMENTS_STARTjyyyy.245
+ __ZL17INSTRUMENTS_STARTjyyyy.2465
+ __ZL17INSTRUMENTS_STARTjyyyy.251
+ __ZL17INSTRUMENTS_STARTjyyyy.2512
+ __ZL17INSTRUMENTS_STARTjyyyy.2545
+ __ZL17INSTRUMENTS_STARTjyyyy.2551
+ __ZL17INSTRUMENTS_STARTjyyyy.262
+ __ZL17INSTRUMENTS_STARTjyyyy.273
+ __ZL17INSTRUMENTS_STARTjyyyy.2739
+ __ZL17INSTRUMENTS_STARTjyyyy.2810
+ __ZL17INSTRUMENTS_STARTjyyyy.3027
+ __ZL17INSTRUMENTS_STARTjyyyy.3041
+ __ZL17INSTRUMENTS_STARTjyyyy.3047
+ __ZL17INSTRUMENTS_STARTjyyyy.3288
+ __ZL17INSTRUMENTS_STARTjyyyy.345
+ __ZL17INSTRUMENTS_STARTjyyyy.3494
+ __ZL17INSTRUMENTS_STARTjyyyy.3504
+ __ZL17INSTRUMENTS_STARTjyyyy.3567
+ __ZL17INSTRUMENTS_STARTjyyyy.3748
+ __ZL17INSTRUMENTS_STARTjyyyy.3887
+ __ZL17INSTRUMENTS_STARTjyyyy.4236
+ __ZL17INSTRUMENTS_STARTjyyyy.4419
+ __ZL17INSTRUMENTS_STARTjyyyy.4593
+ __ZL17INSTRUMENTS_STARTjyyyy.473
+ __ZL17INSTRUMENTS_STARTjyyyy.4806
+ __ZL17INSTRUMENTS_STARTjyyyy.5275
+ __ZL17INSTRUMENTS_STARTjyyyy.5420
+ __ZL17INSTRUMENTS_STARTjyyyy.560
+ __ZL17INSTRUMENTS_STARTjyyyy.5649
+ __ZL17INSTRUMENTS_STARTjyyyy.5897
+ __ZL17INSTRUMENTS_STARTjyyyy.6121
+ __ZL17INSTRUMENTS_STARTjyyyy.6293
+ __ZL17INSTRUMENTS_STARTjyyyy.6409
+ __ZL17INSTRUMENTS_STARTjyyyy.6425
+ __ZL17INSTRUMENTS_STARTjyyyy.6611
+ __ZL17INSTRUMENTS_STARTjyyyy.6617
+ __ZL17INSTRUMENTS_STARTjyyyy.6747
+ __ZL17INSTRUMENTS_STARTjyyyy.6770
+ __ZL17INSTRUMENTS_STARTjyyyy.6795
+ __ZL17INSTRUMENTS_STARTjyyyy.711
+ __ZL17INSTRUMENTS_STARTjyyyy.7160
+ __ZL17INSTRUMENTS_STARTjyyyy.7200
+ __ZL17INSTRUMENTS_STARTjyyyy.7248
+ __ZL17INSTRUMENTS_STARTjyyyy.727
+ __ZL17INSTRUMENTS_STARTjyyyy.7359
+ __ZL17INSTRUMENTS_STARTjyyyy.7515
+ __ZL17INSTRUMENTS_STARTjyyyy.7698
+ __ZL17INSTRUMENTS_STARTjyyyy.7704
+ __ZL17INSTRUMENTS_STARTjyyyy.7760
+ __ZL17INSTRUMENTS_STARTjyyyy.7770
+ __ZL17INSTRUMENTS_STARTjyyyy.7920
+ __ZL17INSTRUMENTS_STARTjyyyy.8237
+ __ZL17INSTRUMENTS_STARTjyyyy.8263
+ __ZL17INSTRUMENTS_STARTjyyyy.8426
+ __ZL17INSTRUMENTS_STARTjyyyy.8450
+ __ZL17INSTRUMENTS_STARTjyyyy.8698
+ __ZL17INSTRUMENTS_STARTjyyyy.9234
+ __ZL17INSTRUMENTS_STARTjyyyy.9300
+ __ZL17INSTRUMENTS_STARTjyyyy.9483
+ __ZL17INSTRUMENTS_STARTjyyyy.9699
+ __ZL17INSTRUMENTS_STARTjyyyy.9705
+ __ZL17INSTRUMENTS_STARTjyyyy.992
+ __ZN11MatrixNxPtsILj1EbED2Ev
+ __ZN11MatrixNxPtsILj1EdE8CopyColsERKS0_RKS_ILj1EjE
+ __ZN11MatrixNxPtsILj1EdEC1Ej
+ __ZN11MatrixNxPtsILj1EdED2Ev
+ __ZN11MatrixNxPtsILj1EjEC2Ej
+ __ZN11MatrixNxPtsILj3EdE8CopyColsERKS0_RKS_ILj1EjE
+ __ZN11MatrixNxPtsILj3EdEC1Ej
+ __ZN11MatrixNxPtsILj3EdED2Ev
+ __ZN11MatrixNxPtsILj4EdED0Ev
+ __ZN11MatrixNxPtsILj4EdED1Ev
+ __ZN11MatrixNxPtsILj9EdED2Ev
+ __ZN11_GMC_Params6_calib4_cam8_distLUT10_nonradialD2Ev
+ __ZN11_GMC_Params6_calib4_cam8_distLUT7_radialD2Ev
+ __ZN11_GMC_Params6_calib4_cam8_distLUTC1ERKS2_
+ __ZN11_GMC_Params6_calibD2Ev
+ __ZN11_GMC_ParamsD2Ev
+ __ZN13ADCommonUtils27matrixNxMToArrayColumnFirstILm4ELm4E13simd_float4x4EEP7NSArrayRKT1_
+ __ZN13ADCommonUtils29matrixNxMFromArrayColumnFirstILm4ELm3E13simd_float4x3EET1_P7NSArray
+ __ZN13ADCommonUtils29matrixNxMFromArrayColumnFirstILm4ELm4E13simd_float4x4EET1_P7NSArray
+ __ZN14BucketsFilters7BucketsEv
+ __ZN14BucketsFiltersC1Ev
+ __ZN14BucketsFiltersC2Ev
+ __ZN14GMC_DebugUtils13DEBUG_BASEDIRE
+ __ZN14GMC_DebugUtils19getDebugPathForFileERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_b
+ __ZN14JacobianMatrix17createNzPerColumnEmmbbbb
+ __ZN14JacobianMatrixC1Emmbbbb
+ __ZN14JacobianMatrixC2Emmbbbb
+ __ZN16DisparityToDepth20WorldPointsContainerD2Ev
+ __ZN16PixelBufferUtils17pixelBufferToDataEP10__CVBuffer
+ __ZN16PixelBufferUtils19pixelBufferFromDataEP6NSDataP10__CVBuffer
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBuffer6CGRect
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBufferj
+ __ZN16PixelBufferUtils23createPixelBufferNoCopyEP10__CVBufferj6CGRect
+ __ZN16PixelBufferUtils24isSameDimensionAndFormatEP10__CVBufferS1_
+ __ZN20ADFrameBoundaryGuardD2Ev
+ __ZN20PixelBufferSharedPtr13TakeOwnershipEP10__CVBuffer
+ __ZN20PixelBufferSharedPtrD0Ev
+ __ZN20PixelBufferSharedPtrD1Ev
+ __ZN21CGMC_BundleAdjustment12calcJacobianERKNS_18OptimizationParamsERK11MatrixNxPtsILj1EdEmRK11_GMC_ParamsP14JacobianMatrixPS4_
+ __ZN21CGMC_BundleAdjustment13solveLinearEqERK14JacobianMatrixRK11MatrixNxPtsILj1EdEdS6_i
+ __ZN21CGMC_BundleAdjustment17getResidualsStatsERK11MatrixNxPtsILj1EdERdS4_S4_
+ __ZN21CGMC_BundleAdjustment18OptimizationParams7ShiftByERK11MatrixNxPtsILj1EdERK11_GMC_Params
+ __ZN21CGMC_BundleAdjustment18OptimizationParamsC1EO9MatrixMxNILj1ELj3EdEOS1_ILj3ELj3EdEO11MatrixNxPtsILj3EdEb
+ __ZN21CGMC_BundleAdjustment18OptimizationParamsC1ERKS0_
+ __ZN21CGMC_BundleAdjustment18OptimizationParamsC2EO9MatrixMxNILj1ELj3EdEOS1_ILj3ELj3EdEO11MatrixNxPtsILj3EdEb
+ __ZN21CGMC_BundleAdjustment18OptimizationParamsC2ERKS0_
+ __ZN21CGMC_BundleAdjustment18OptimizationParamsD1Ev
+ __ZN21CGMC_BundleAdjustment25angleAxisToRotationMatrixE9MatrixMxNILj1ELj3EdE
+ __ZN21CGMC_BundleAdjustment25rotationMatrixToAngleAxisERK9MatrixMxNILj3ELj3EdE
+ __ZN21CGMC_BundleAdjustment30calculateCostFunctionResidualsERKNS_18OptimizationParamsERK11MatrixNxPtsILj1EdEmb
+ __ZN21CGMC_BundleAdjustment6CalcBAERK11MatrixNxPtsILj3EdERKS0_ILj1EdERK9MatrixMxNILj3ELj3EdESA_RKS7_ILj1ELj3EdERK11_GMC_ParamsPS8_PdSI_SI_Pi
+ __ZN21CGMC_BundleAdjustment9isStalledERK11MatrixNxPtsILj1EdEdRK11_GMC_Params
+ __ZN21CGMC_BundleAdjustmentC1ERK11MatrixNxPtsILj3EdES3_
+ __ZN21CGMC_BundleAdjustmentC2ERK11MatrixNxPtsILj3EdES3_
+ __ZN21CGMC_BundleAdjustmentD2Ev
+ __ZN21InstrumentsTraceGuardD2Ev
+ __ZN23PixelBufferUtilsSession29createCropScaleConvertSessionE6CGSizejS0_j6CGRectS1_
+ __ZN23PixelBufferUtilsSession35createCropScaleConvertRotateSessionE6CGSizejS0_j6CGRectS1_i
+ __ZN23PixelBufferUtilsSessionC1E6CGSizejS0_j6CGRectS1_i33PixelBufferUtilsSessionReflection
+ __ZN23PixelBufferUtilsSessionC2E6CGSizejS0_j6CGRectS1_i33PixelBufferUtilsSessionReflection
+ __ZN39GMC_BundleAdjustmentMathematicalProblem26calculateNumberOfVariablesEmbbb
+ __ZN39GMC_BundleAdjustmentMathematicalProblem32calculateNumberOfXiYiZiVariablesEm
+ __ZN39GMC_BundleAdjustmentMathematicalProblem32getColumnIndicesForConfigurationEbbb
+ __ZN39GMC_BundleAdjustmentMathematicalProblem34calculateNumberOfResidualFunctionsEmmb
+ __ZN39GMC_BundleAdjustmentMathematicalProblem39calculateNumberOfVariablesWithoutXiYiZiEbbb
+ __ZN3jpc10GMCJ_Utils24getOperationalProjAnglesEPK8PCECalib
+ __ZN3jpc10GMCJ_Utils29updatePCECalibWithGMCJResultsERKNS_11IGMC_JBlock11GmcjOutputsERK8PCECalibf
+ __ZN3jpc10JPCFactory17createPORIFABlockERKNS_12PORIFAConfigE
+ __ZN3jpc10JPCFactory24getDefaultPearlPceConfigEv
+ __ZN3jpc10JPCFactory30createEflModePORImplementationEPKN11_GMC_Params7_constsEPNSt3__110unique_ptrINS_24IPreprocessorFilterBlockENS5_14default_deleteIS7_EEEEPNS6_INS_18IPreprocessorBlockENS8_ISC_EEEEPNS6_INS_9IIFABlockENS8_ISG_EEEEPNS6_INS_11IGMC_JBlockENS8_ISK_EEEEPNS6_INS_22IOutputValidationBlockENS8_ISO_EEEE
+ __ZN3jpc10JPCFactory30createJPCModePORImplementationEPNSt3__110unique_ptrINS_24IPreprocessorFilterBlockENS1_14default_deleteIS3_EEEEPNS2_INS_18IPreprocessorBlockENS4_IS8_EEEEPNS2_INS_9IIFABlockENS4_ISC_EEEEPNS2_INS_11IGMC_JBlockENS4_ISG_EEEEPNS2_INS_22IOutputValidationBlockENS4_ISK_EEEE
+ __ZN3jpc10PearlUtils11pceRgDyToDyEstff
+ __ZN3jpc10PearlUtils13getBinForCoorEdmm
+ __ZN3jpc10PearlUtils13isInvalidRgDxEt
+ __ZN3jpc10PearlUtils14upscaleDxValueEff
+ __ZN3jpc10PearlUtils14upscaleDyValueEff
+ __ZN3jpc10PearlUtils19upscaleCoordinateRGEdf
+ __ZN3jpc10PearlUtils20upscaleCoordinateRGSEdf
+ __ZN3jpc10PearlUtils20upscaleCoordinatesRGERKNS_17Real2DCoordinatesEf
+ __ZN3jpc10PearlUtils21downscaleCoordinateRGEdf
+ __ZN3jpc10PearlUtils21upscaleCoordinatesRGSERKNS_17Real2DCoordinatesEf
+ __ZN3jpc10PearlUtils22downscaleCoordinateRGSEdf
+ __ZN3jpc10PearlUtils22downscaleCoordinatesRGERKNS_17Real2DCoordinatesEf
+ __ZN3jpc10PearlUtils22getIrCameraCalibrationE24PCECalibCameraIntrinsics
+ __ZN3jpc10PearlUtils23downscaleCoordinatesRGSERKNS_17Real2DCoordinatesEf
+ __ZN3jpc11PORIFABlock7processERKNS_18IPreprocessorBlock21JpcPreprocessorOutputEP47ADJasperPearlInFieldCalibrationInterSessionDataP26ADJasperPearlTelemetryData
+ __ZN3jpc11PORIFABlock8eraseAllEPNS_6IFA_DBE
+ __ZN3jpc11PORIFABlockC1EONSt3__16vectorINS1_10unique_ptrINS_11IIFA_FilterENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEEONS2_INS3_INS_15IFAPullCriteriaENS5_ISC_EEEENS8_ISE_EEEEmmf
+ __ZN3jpc11PORIFABlockC2EONSt3__16vectorINS1_10unique_ptrINS_11IIFA_FilterENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEEONS2_INS3_INS_15IFAPullCriteriaENS5_ISC_EEEENS8_ISE_EEEEmmf
+ __ZN3jpc11PORIFABlockD0Ev
+ __ZN3jpc11PORIFABlockD1Ev
+ __ZN3jpc11PORIFABlockD2Ev
+ __ZN3jpc12JPCException12setErrorCodeE8JPCError
+ __ZN3jpc12JPCException16setExceptionNameERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN3jpc12JPCException18setNestedExceptionERKS0_
+ __ZN3jpc12JPCException18setNestedExceptionERKSt9exception
+ __ZN3jpc12JPCException20generateExceptionStrEv
+ __ZN3jpc12JPCException7setFileEPKci
+ __ZN3jpc12JPCExceptionC1Ev
+ __ZN3jpc12JPCExceptionC2ERKS0_
+ __ZN3jpc12JPCExceptionC2Ev
+ __ZN3jpc12JPCExceptionD0Ev
+ __ZN3jpc12JPCExceptionD1Ev
+ __ZN3jpc12JPCExceptionD2Ev
+ __ZN3jpc12JPCPORConfig12PORISFConfigEv
+ __ZN3jpc12JPCPORConfig17PORIFABlockConfigEv
+ __ZN3jpc12JPCPORConfig18PORGMCJBlockConfigEv
+ __ZN3jpc12JPCPORConfig32PORPreprocessorFilterBlockConfigEv
+ __ZN3jpc12JpcInputDataD2Ev
+ __ZN3jpc13IFA_DataFrame11setRotationEPf
+ __ZN3jpc13IFA_DataFrame12initPearlPtsEv
+ __ZN3jpc13IFA_DataFrame13getPearlDepthEv
+ __ZN3jpc13IFA_DataFrame14irCoorToRGCoorE7CGPoint
+ __ZN3jpc13IFA_DataFrame14setTranslationEPf
+ __ZN3jpc13IFA_DataFrame15getPearlJasperZEj
+ __ZN3jpc13IFA_DataFrame15getPearlRgScoreEv
+ __ZN3jpc13IFA_DataFrame16isPearlSpotValidEj
+ __ZN3jpc13IFA_DataFrame17isJasperSpotValidEj
+ __ZN3jpc13IFA_DataFrame19setPearlInvalidSpotEj
+ __ZN3jpc13IFA_DataFrame20setJasperInvalidSpotEj
+ __ZN3jpc13IFA_DataFrame21getValidPearlSpotsNumEv
+ __ZN3jpc13IFA_DataFrame22getValidJasperSpotsNumEv
+ __ZN3jpc13IFA_DataFrame27rotationMatrixToEulerAnglesERK13simd_float4x4RA3_f
+ __ZN3jpc13IFA_DataFrame4initEv
+ __ZN3jpc13IFA_DataFrame9getPearlZEj
+ __ZN3jpc13IFA_DataFrameC1EPKNS_18IPreprocessorBlock21JpcPreprocessorOutputE
+ __ZN3jpc13IFA_DataFrameC2EPKNS_18IPreprocessorBlock21JpcPreprocessorOutputE
+ __ZN3jpc13IFA_DataFrameD1Ev
+ __ZN3jpc13IFA_DataFrameD2Ev
+ __ZN3jpc13JPCConfigKeys11PORIFABlock10IFA_NBIN_XE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock10IFA_NBIN_YE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock13IFA_WINDOW_WHE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock18IFA_MX_PTS_PER_BINE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock18VAL_SET_PERCENTAGEE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock19IFA_PEARL_MIN_DEPTHE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock19IFA_SIGMA_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock23IFA_WORK_DIST_MAX_DEPTHE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock23IFA_WORK_DIST_MIN_DEPTHE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock24IFA_DEPTH_DIFF_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock25PEARL_FOV_COVERAGE_NBIN_XE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock25PEARL_FOV_COVERAGE_NBIN_YE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock26MIN_UNIQUE_JASPER_SPOT_IDSE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock29IFA_ENABLE_PJDEPTHDIFF_FILTERE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock30IFA_WINDOW_OCCLUSION_EXTENSIONE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock31IFA_ENABLE_LOCALDEPTHVAR_FILTERE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock33IFA_ENABLE_SPATIALCOVERAGE_FILTERE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock33PEARL_FOV_COVERAGE_MX_PTS_PER_BINE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock34IFA_ENABLE_JPTSIDCOVERAGE_CRITERIAE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock35IFA_ENABLE_PJWORKDISTOVERLAP_FILTERE
+ __ZN3jpc13JPCConfigKeys11PORIFABlock36IFA_ENABLE_PEARLFOVCOVERAGE_CRITERIAE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock10GMCJ_MAX_ZE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock10GMCJ_MIN_ZE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock15GMCJ_BA_MAX_ITRE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock17GMCJ_IS_REFINE_BAE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock17GMCJ_RANSAC_T_VALE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_BA_CALL_TWICEE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_IS_REF_CONFIGE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_PPX_TOLERANCEE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_PPY_TOLERANCEE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_SHOULD_FIND_TE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock18GMCJ_TEST_SET_SIZEE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock19GMCJ_CORR_NUM_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock19GMCJ_OVERRIDE_R_ESTE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock20GMCJ_AMBIGUITY_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock20GMCJ_SCALE_TOLERANCEE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock20GMCJ_SHOULD_FIND_EFLE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock20GMCJ_SHOULD_FIND_PPXE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock20GMCJ_SHOULD_FIND_PPYE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock21GMCJ_NUM_RANSAC_CALLSE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock21GMCJ_PDM_MEDIAN_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock22GMCJ_BA_INITIAL_RADIUSE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock22GMCJ_INLIERS_NUM_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock22GMCJ_SINGULARITY_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock23GMCJ_BA_MAX_STALL_COUNTE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock23GMCJ_IS_UNDISTORT_CORRSE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock24GMCJ_COVERAGE_RATE_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock24GMCJ_FACE_CORR_NUM_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock26GMCJ_BA_COST_FUNC_STOP_TOLE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock26GMCJ_BA_STEP_SIZE_STOP_TOLE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock26GMCJ_ROTATION_TOLERANCES_0E
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock26GMCJ_ROTATION_TOLERANCES_1E
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock26GMCJ_ROTATION_TOLERANCES_2E
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock28GMCJ_AMBIGUITY_INLIER_MARGINE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock28GMCJ_MAX_3D_CONSTRAINT_ITERSE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock29GMCJ_FACE_COVERAGE_RATE_THRESE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock30GMCJ_BA_STEP_SIZE_EFL_STOP_TOLE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock30GMCJ_BA_STEP_SIZE_ROT_STOP_TOLE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock44GMCJ_SHOULD_INCLUDE_JASPER_RESIDUAL_FUNCTIONE
+ __ZN3jpc13JPCConfigKeys12PORGMCJBlock48GMCJ_VALIDATION_MEDIAN_JASPER_MISALIGNMENT_THRESE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock29VIO_MAX_TRANSLATION_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock29VIO_MIN_TRANSLATION_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock32JASPER_MAX_GLARE_SPOTS_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock32VIO_MAX_ROTATION_ANGLE_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock32VIO_MIN_ROTATION_ANGLE_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys26PORPreprocessorFilterBlock37JASPER_MAX_REFLECTIVE_SPOTS_THRESHOLDE
+ __ZN3jpc13JPCConfigKeys6PORISF12ISF_CAPACITYE
+ __ZN3jpc13JPCConfigKeys6PORISF14ISF_MAX_WEIGHTE
+ __ZN3jpc13JPCConfigKeys6PORISF14ISF_MIN_WEIGHTE
+ __ZN3jpc13JPCConfigKeys6PORISF15ISF_OUTLIER_NUME
+ __ZN3jpc13JPCConfigKeys6PORISF17ISF_MIN_STEP_SIZEE
+ __ZN3jpc13JPCConfigKeys6PORISF18ISF_MIN_STEP_INDEXE
+ __ZN3jpc13JPCConfigKeys6PORISF18ISF_OUTLIER_WEIGHTE
+ __ZN3jpc13JPCConfigKeys6PORISF26ISF_MIN_ENTRIES_FOR_RESULTE
+ __ZN3jpc13JPCConfigKeys6PORISF28ISF_IS_STEP_DETECTION_ACTIVEE
+ __ZN3jpc13JPCConfigKeys6PORISF28ISF_STEP_DETECTION_THRESHOLDE
+ __ZN3jpc13PORGMCJ_BlockC1ERKN11_GMC_Params7_constsEb
+ __ZN3jpc13PORGMCJ_BlockC2ERKN11_GMC_Params7_constsEb
+ __ZN3jpc13PORGMCJ_BlockD0Ev
+ __ZN3jpc13PORGMCJ_BlockD1Ev
+ __ZN3jpc16IFA_FilterRunner12applyFiltersEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc16IFA_FilterRunnerC1EONSt3__16vectorINS1_10unique_ptrINS_11IIFA_FilterENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEE
+ __ZN3jpc16IFA_FilterRunnerC2EONSt3__16vectorINS1_10unique_ptrINS_11IIFA_FilterENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEE
+ __ZN3jpc16IFA_FilterRunnerD0Ev
+ __ZN3jpc16IFA_FilterRunnerD1Ev
+ __ZN3jpc16IFA_FilterRunnerD2Ev
+ __ZN3jpc17CVPixelBufferLockD0Ev
+ __ZN3jpc17CVPixelBufferLockD1Ev
+ __ZN3jpc17IFAPRGScoreFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc17IFAPRGScoreFilterC1Eh
+ __ZN3jpc17IFAPRGScoreFilterC2Eh
+ __ZN3jpc17IFAPRGScoreFilterD0Ev
+ __ZN3jpc17IFAPRGScoreFilterD1Ev
+ __ZN3jpc17IFAPoseDiffFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc17IFAPoseDiffFilterC1Ev
+ __ZN3jpc17IFAPoseDiffFilterC2Ev
+ __ZN3jpc17IFAPoseDiffFilterD0Ev
+ __ZN3jpc17IFAPoseDiffFilterD1Ev
+ __ZN3jpc18IFAFailedExceptionC1Ev
+ __ZN3jpc18IFAFailedExceptionC2Ev
+ __ZN3jpc18IFAFailedExceptionD0Ev
+ __ZN3jpc18IFAFailedExceptionD1Ev
+ __ZN3jpc18IPreprocessorBlock21JpcPreprocessorOutputD2Ev
+ __ZN3jpc19CVPixelBufferHelperIhED0Ev
+ __ZN3jpc19CVPixelBufferHelperIhED1Ev
+ __ZN3jpc19CVPixelBufferHelperIsED0Ev
+ __ZN3jpc19CVPixelBufferHelperIsED1Ev
+ __ZN3jpc19CVPixelBufferHelperItED0Ev
+ __ZN3jpc19CVPixelBufferHelperItED1Ev
+ __ZN3jpc19GMCJFailedExceptionC2Ev
+ __ZN3jpc19GMCJFailedExceptionD0Ev
+ __ZN3jpc19GMCJFailedExceptionD1Ev
+ __ZN3jpc19GMC_StandaloneUtils17generateGmcParamsERKN11_GMC_Params7_constsERKNS_12JpcInputData17CalibrationInputs17PearlCalibrationsEm
+ __ZN3jpc19GMC_StandaloneUtils36convert_GMC_Result_to_JpcGmcjOutputsERK12_GMC_ResultsbfPKd
+ __ZN3jpc19GMC_StandaloneUtils36convert_JpcGmcjOutputs_to_GMCResultsERKNS_11IGMC_JBlock11GmcjOutputsE
+ __ZN3jpc19GMC_StandaloneUtils42add_JpcPearlCalib_Parameters_to_GMC_ParamsER11_GMC_ParamsRKNS_12JpcInputData17CalibrationInputs17PearlCalibrationsE
+ __ZN3jpc19GMC_StandaloneUtils49convertJpcCorrespondencesToGmcStandaloneDatatypesERKNSt3__16vectorINS_9IIFABlock28IFAPearlJasperCorrespondenceENS1_9allocatorIS4_EEEERKNS2_INS3_22IFAPearlCorrespondenceENS5_ISA_EEEE
+ __ZN3jpc19IFASimpleAggregatorC1Emmf
+ __ZN3jpc19IFASimpleAggregatorC2Emmf
+ __ZN3jpc19IFASimpleAggregatorD0Ev
+ __ZN3jpc19IFASimpleAggregatorD1Ev
+ __ZN3jpc20IFAJConfidenceFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc20IFAJConfidenceFilterC1Ef
+ __ZN3jpc20IFAJConfidenceFilterC2Ef
+ __ZN3jpc20IFAJConfidenceFilterD0Ev
+ __ZN3jpc20IFAJConfidenceFilterD1Ev
+ __ZN3jpc20IFAJDepthRangeFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc20IFAJDepthRangeFilterC1Eff
+ __ZN3jpc20IFAJDepthRangeFilterC2Eff
+ __ZN3jpc20IFAJDepthRangeFilterD0Ev
+ __ZN3jpc20IFAJDepthRangeFilterD1Ev
+ __ZN3jpc20IFANotReadyExceptionC2Ev
+ __ZN3jpc20IFANotReadyExceptionD0Ev
+ __ZN3jpc20IFANotReadyExceptionD1Ev
+ __ZN3jpc20IFAPJDepthDiffFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc20IFAPJDepthDiffFilterC1Ef
+ __ZN3jpc20IFAPJDepthDiffFilterC2Ef
+ __ZN3jpc20IFAPJDepthDiffFilterD0Ev
+ __ZN3jpc20IFAPJDepthDiffFilterD1Ev
+ __ZN3jpc20PORPreprocessorBlockD0Ev
+ __ZN3jpc20PORPreprocessorBlockD1Ev
+ __ZN3jpc20PORPreprocessorBlockD2Ev
+ __ZN3jpc21IFAPullCriteriaRunnerC1EONSt3__16vectorINS1_10unique_ptrINS_15IFAPullCriteriaENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEE
+ __ZN3jpc21IFAPullCriteriaRunnerC2EONSt3__16vectorINS1_10unique_ptrINS_15IFAPullCriteriaENS1_14default_deleteIS4_EEEENS1_9allocatorIS7_EEEE
+ __ZN3jpc21IFAPullCriteriaRunnerD0Ev
+ __ZN3jpc21IFAPullCriteriaRunnerD1Ev
+ __ZN3jpc21IFAPullCriteriaRunnerD2Ev
+ __ZN3jpc23IFAPLocalDepthVarFilter17check_local_depthENS_17Real2DCoordinatesEmmmPtRNSt3__16vectorItNS3_9allocatorItEEEE
+ __ZN3jpc23IFAPLocalDepthVarFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc23IFAPLocalDepthVarFilterC1Efmmf
+ __ZN3jpc23IFAPLocalDepthVarFilterC2Efmmf
+ __ZN3jpc23IFAPLocalDepthVarFilterD0Ev
+ __ZN3jpc23IFAPLocalDepthVarFilterD1Ev
+ __ZN3jpc24IFADepthCoverageCriteriaC1Ejjf
+ __ZN3jpc24IFADepthCoverageCriteriaC2Ejjf
+ __ZN3jpc24IFADepthCoverageCriteriaD0Ev
+ __ZN3jpc24IFADepthCoverageCriteriaD1Ev
+ __ZN3jpc24IFASpatialCoverageFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc24IFASpatialCoverageFilterC1Emmm
+ __ZN3jpc24IFASpatialCoverageFilterC2Emmm
+ __ZN3jpc24IFASpatialCoverageFilterD0Ev
+ __ZN3jpc24IFASpatialCoverageFilterD1Ev
+ __ZN3jpc24undistortFromPixelCenterEP19ADCameraCalibrationRKNS_17Real2DCoordinatesE
+ __ZN3jpc25IFAJPtsIDCoverageCriteriaC1Em
+ __ZN3jpc25IFAJPtsIDCoverageCriteriaC2Em
+ __ZN3jpc25IFAJPtsIDCoverageCriteriaD0Ev
+ __ZN3jpc25IFAJPtsIDCoverageCriteriaD1Ev
+ __ZN3jpc25IFAThermalTransientFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc25IFAThermalTransientFilterC1Ef
+ __ZN3jpc25IFAThermalTransientFilterC2Ef
+ __ZN3jpc25IFAThermalTransientFilterD0Ev
+ __ZN3jpc25IFAThermalTransientFilterD1Ev
+ __ZN3jpc26IFAPJWorkDistOverlapFilter5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBEP26ADJasperPearlTelemetryData
+ __ZN3jpc26IFAPJWorkDistOverlapFilterC1Eff
+ __ZN3jpc26IFAPJWorkDistOverlapFilterC2Eff
+ __ZN3jpc26IFAPJWorkDistOverlapFilterD0Ev
+ __ZN3jpc26IFAPJWorkDistOverlapFilterD1Ev
+ __ZN3jpc26PORPreprocessorFilterBlockC1ERKNS0_6ConfigE
+ __ZN3jpc26PORPreprocessorFilterBlockC2ERKNS0_6ConfigE
+ __ZN3jpc26PORPreprocessorFilterBlockD0Ev
+ __ZN3jpc26PORPreprocessorFilterBlockD1Ev
+ __ZN3jpc27IFAPearlFovCoverageCriteriaC1Emmm
+ __ZN3jpc27IFAPearlFovCoverageCriteriaC2Emmm
+ __ZN3jpc27IFAPearlFovCoverageCriteriaD0Ev
+ __ZN3jpc27IFAPearlFovCoverageCriteriaD1Ev
+ __ZN3jpc28PreprocessingFailedExceptionC2Ev
+ __ZN3jpc28PreprocessingFailedExceptionD0Ev
+ __ZN3jpc28PreprocessingFailedExceptionD1Ev
+ __ZN3jpc30PORGMCJ_OutputValidation_BlockC1ERKN11_GMC_Params7_constsE
+ __ZN3jpc30PORGMCJ_OutputValidation_BlockC2ERKN11_GMC_Params7_constsE
+ __ZN3jpc30PORGMCJ_OutputValidation_BlockD0Ev
+ __ZN3jpc30PORGMCJ_OutputValidation_BlockD1Ev
+ __ZN3jpc35doubleBufferToFloatNSDataWithBufferEPKdm
+ __ZN3jpc38GMCJOutputValidationNotPassedExceptionC2Ev
+ __ZN3jpc38GMCJOutputValidationNotPassedExceptionD0Ev
+ __ZN3jpc38GMCJOutputValidationNotPassedExceptionD1Ev
+ __ZN3jpc3JPC17setStepsToExecuteEm
+ __ZN3jpc3JPCC1EONSt3__110unique_ptrINS_24IPreprocessorFilterBlockENS1_14default_deleteIS3_EEEEONS2_INS_18IPreprocessorBlockENS4_IS8_EEEEONS2_INS_9IIFABlockENS4_ISC_EEEEONS2_INS_11IGMC_JBlockENS4_ISG_EEEEONS2_INS_22IOutputValidationBlockENS4_ISK_EEEEONS2_INS_11IISF_PBlockENS4_ISO_EEEEONS2_INS_9IGLABlockENS4_ISS_EEEEONS2_INS_11IISF_SBlockENS4_ISW_EEEEONS2_INS_13IGLA2DXMBlockENS4_IS10_EEEEb
+ __ZN3jpc3JPCC2EONSt3__110unique_ptrINS_24IPreprocessorFilterBlockENS1_14default_deleteIS3_EEEEONS2_INS_18IPreprocessorBlockENS4_IS8_EEEEONS2_INS_9IIFABlockENS4_ISC_EEEEONS2_INS_11IGMC_JBlockENS4_ISG_EEEEONS2_INS_22IOutputValidationBlockENS4_ISK_EEEEONS2_INS_11IISF_PBlockENS4_ISO_EEEEONS2_INS_9IGLABlockENS4_ISS_EEEEONS2_INS_11IISF_SBlockENS4_ISW_EEEEONS2_INS_13IGLA2DXMBlockENS4_IS10_EEEEb
+ __ZN3jpc3JPCD0Ev
+ __ZN3jpc3JPCD1Ev
+ __ZN3jpc3JPCD2Ev
+ __ZN3jpc40PreprocessingFilterInvalidFrameExceptionC2Ev
+ __ZN3jpc40PreprocessingFilterInvalidFrameExceptionD0Ev
+ __ZN3jpc40PreprocessingFilterInvalidFrameExceptionD1Ev
+ __ZN3jpc44GMCJOutputValidationMetricIncreasedExceptionC2Ev
+ __ZN3jpc44GMCJOutputValidationMetricIncreasedExceptionD0Ev
+ __ZN3jpc44GMCJOutputValidationMetricIncreasedExceptionD1Ev
+ __ZN3jpc6IFA_DB12getAggPointsEv
+ __ZN3jpc6IFA_DB12setAggPointsERKNS_9IIFABlock14AggregatedDataE
+ __ZN3jpc6IFA_DB15getLastRotationEPPf
+ __ZN3jpc6IFA_DB15setLastRotationEPf
+ __ZN3jpc6IFA_DB16getLastPearlTempEv
+ __ZN3jpc6IFA_DB16removeAllObjectsEv
+ __ZN3jpc6IFA_DB18getLastTranslationEPPf
+ __ZN3jpc6IFA_DB18setLastTemperatureEf
+ __ZN3jpc6IFA_DB18setLastTranslationEPf
+ __ZN3jpc6IFA_DB31setTelemetryNumOfUniqueTOFSpotsEm
+ __ZN3jpc6IFA_DB35setTelemetryIRCamFOVCoveragePercentEd
+ __ZN3jpc6IFA_DBC1EP47ADJasperPearlInFieldCalibrationInterSessionData
+ __ZN3jpc6IFA_DBC2EP47ADJasperPearlInFieldCalibrationInterSessionData
+ __ZN3jpc6IFA_DBD1Ev
+ __ZN3jpc6IFA_DBD2Ev
+ __ZN3jpc9IIFABlock14AggregatedDataD1Ev
+ __ZN3jpc9IIFABlock14AggregatedDataD2Ev
+ __ZN3jpc9JPCConfig12getISFConfigEv
+ __ZN3jpc9JPCConfig13getGMCJConfigEv
+ __ZN3jpc9JPCConfig15getPORIFAConfigEv
+ __ZN3jpc9JPCConfig17readJpcConfigFileEv
+ __ZN3jpc9JPCConfig21CONFIG_FILE_FILEPATH1E
+ __ZN3jpc9JPCConfig21CONFIG_FILE_FILEPATH2E
+ __ZN3jpc9JPCConfig21configDictToISFConfigEP12NSDictionaryIP8NSStringP8NSNumberE
+ __ZN3jpc9JPCConfig22configDictToGMCJConfigEP12NSDictionaryIP8NSStringP8NSNumberE
+ __ZN3jpc9JPCConfig22readJpcConfigFileInnerEPKc
+ __ZN3jpc9JPCConfig23printConfigurationToLogEP12NSDictionaryIP8NSStringP8NSNumberES7_S7_
+ __ZN3jpc9JPCConfig24configDictToPORIFAConfigEP12NSDictionaryIP8NSStringP8NSNumberE
+ __ZN3jpc9JPCConfig24prioritizeConfigurationsEP12NSDictionaryIP8NSStringP8NSNumberES7_
+ __ZN3jpc9JPCConfig33generatePORConfigFileToFilesystemEv
+ __ZN3jpc9JPCConfig34GENERATED_DEFAULT_CONFIG_FILE_PATHE
+ __ZN3jpc9JPCConfig35getPORPreprocessorFilterBlockConfigEv
+ __ZN3jpc9JPCConfig44configDictToPORPreprocessorFilterBlockConfigEP12NSDictionaryIP8NSStringP8NSNumberE
+ __ZN3jpc9MathUtils27bilinearInterpolateInSquareIfEET_S2_S2_S2_S2_S2_S2_S2_S2_S2_
+ __ZN6MatrixIbED2Ev
+ __ZN6MatrixIdEC2ERKS0_jj
+ __ZN6MatrixIdED2Ev
+ __ZN6MatrixIfED2Ev
+ __ZN7BucketsC1ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_6vectorIfNS4_IfEEEE
+ __ZN7BucketsC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_6vectorIfNS4_IfEEEE
+ __ZN7BucketsD2Ev
+ __ZNK14JacobianMatrix11qlDecomposeERK11MatrixNxPtsILj1EdE
+ __ZNK14JacobianMatrix5SolveERK11MatrixNxPtsILj1EdE
+ __ZNK21CGMC_BundleAdjustment37getNumberOfPearlJasperCorrespondencesERK11MatrixNxPtsILj1EdE
+ __ZNK3jpc11PORIFABlock12pullAndEraseEP47ADJasperPearlInFieldCalibrationInterSessionDataPK19ADCameraCalibrationP26ADJasperPearlTelemetryData
+ __ZNK3jpc11PORIFABlock13isReadyToPullEP47ADJasperPearlInFieldCalibrationInterSessionDataPK19ADCameraCalibrationP26ADJasperPearlTelemetryData
+ __ZNK3jpc11PORIFABlock20processTelemetryDataERKNS_9IIFABlock9IFAOutputEP47ADJasperPearlInFieldCalibrationInterSessionDataP26ADJasperPearlTelemetryData
+ __ZNK3jpc11PORIFABlock31updateTelemetryInterSessionDataERKNS_18IPreprocessorBlock21JpcPreprocessorOutputEdP47ADJasperPearlInFieldCalibrationInterSessionData
+ __ZNK3jpc11PORIFABlock4pullEP47ADJasperPearlInFieldCalibrationInterSessionDataPK19ADCameraCalibration
+ __ZNK3jpc12JPCException12getErrorCodeEv
+ __ZNK3jpc12JPCException21getNestedJpcExceptionEv
+ __ZNK3jpc12JPCException21getNestedStdExceptionEv
+ __ZNK3jpc12JPCException4whatEv
+ __ZNK3jpc13PORGMCJ_Block20processTelemetryDataERK11_GMC_ParamsRK12_GMC_ResultsP26ADJasperPearlTelemetryData
+ __ZNK3jpc13PORGMCJ_Block7processERKNS_9IIFABlock14AggregatedDataERKNS_12JpcInputDataEP26ADJasperPearlTelemetryData
+ __ZNK3jpc19IFASimpleAggregator13isReadyToPullEPNS_6IFA_DBE
+ __ZNK3jpc19IFASimpleAggregator4pullEPNS_6IFA_DBEPK19ADCameraCalibration
+ __ZNK3jpc19IFASimpleAggregator5applyEPNS_13IFA_DataFrameEPNS_6IFA_DBE
+ __ZNK3jpc19IFASimpleAggregator8eraseAllEPNS_6IFA_DBE
+ __ZNK3jpc20PORPreprocessorBlock26createPearlCorrespondencesERKNS_12JpcInputDataERNS_18IPreprocessorBlock21JpcPreprocessorOutputE
+ __ZNK3jpc20PORPreprocessorBlock32createPearlJasperCorrespondencesERKNS_12JpcInputDataERNS_18IPreprocessorBlock21JpcPreprocessorOutputE
+ __ZNK3jpc20PORPreprocessorBlock33createPearlCorrespondenceFromDxDyERKNS_12JpcInputDataERKNS_17Real2DCoordinatesEbff
+ __ZNK3jpc20PORPreprocessorBlock36pickDxDySamplePointsForInterpolationERKNS_12JpcInputDataERKNS_17Real2DCoordinatesERS4_RdRNSt3__16vectorIhNS9_9allocatorIhEEEE
+ __ZNK3jpc20PORPreprocessorBlock48forwardRelevantInputsToOutputWithNoPreprocessingERKNS_12JpcInputDataERNS_18IPreprocessorBlock21JpcPreprocessorOutputE
+ __ZNK3jpc20PORPreprocessorBlock48interpolateDownscaledDxDyForNonIntegerCoordinateERKNS_17Real2DCoordinatesERKNS_12JpcInputDataERNSt3__14pairIffEERh
+ __ZNK3jpc20PORPreprocessorBlock55getJasperNoPoseToIRSensorOperationalWithPoseCalibrationERKNS_12JpcInputDataE
+ __ZNK3jpc20PORPreprocessorBlock7processERKNS_12JpcInputDataE
+ __ZNK3jpc21IFAPullCriteriaRunner13isReadyToPullEPNS_6IFA_DBEPK19ADCameraCalibration
+ __ZNK3jpc24IFADepthCoverageCriteria5applyEPNS_6IFA_DBEPK19ADCameraCalibration
+ __ZNK3jpc25IFAJPtsIDCoverageCriteria5applyEPNS_6IFA_DBEPK19ADCameraCalibration
+ __ZNK3jpc26PORPreprocessorFilterBlock19getTranslationDeltaE13simd_float4x4S1_
+ __ZNK3jpc26PORPreprocessorFilterBlock22getRotationAnglesDeltaE13simd_float4x4S1_
+ __ZNK3jpc26PORPreprocessorFilterBlock25getRotationDeltaMagnitudeE13simd_float4x4S1_
+ __ZNK3jpc26PORPreprocessorFilterBlock26vioChangeWithinFrameFilterERKNS_12JpcInputDataEP26ADJasperPearlTelemetryData
+ __ZNK3jpc26PORPreprocessorFilterBlock28jasperReflectionsFrameFilterERKNS_12JpcInputDataEP26ADJasperPearlTelemetryData
+ __ZNK3jpc26PORPreprocessorFilterBlock28vioChangeBetweenFramesFilterERKNS_12JpcInputDataEP26ADJasperPearlTelemetryData
+ __ZNK3jpc26PORPreprocessorFilterBlock7processERKNS_12JpcInputDataEP26ADJasperPearlTelemetryData
+ __ZNK3jpc27IFAPearlFovCoverageCriteria5applyEPNS_6IFA_DBEPK19ADCameraCalibration
+ __ZNK3jpc30PORGMCJ_OutputValidation_Block17fillTelemetryDataEP18GMCInnerStatistics9GmcStatusP26ADJasperPearlTelemetryData
+ __ZNK3jpc30PORGMCJ_OutputValidation_Block7processERKNS_11IGMC_JBlock11GmcjOutputsERKNS_9IIFABlock14AggregatedDataERKNS_12JpcInputData17CalibrationInputs17PearlCalibrationsEP26ADJasperPearlTelemetryData
+ __ZNK3jpc3JPC18undistortRefPointsERKNS_12JpcInputDataENSt3__110shared_ptrINS_9IIFABlock9IFAOutputEEE
+ __ZNK3jpc3JPC3runERKNS_12JpcInputDataEP47ADJasperPearlInFieldCalibrationInterSessionDataRNSt3__18optionalINS_11IGMC_JBlock11GmcjOutputsEEERNS7_INS_9IGLABlock9GLAOutputEEEP26ADJasperPearlTelemetryData
+ __ZNK3jpc6IFA_DB31getTelemetryNumOfUniqueTOFSpotsEv
+ __ZNK3jpc6IFA_DB35getTelemetryIRCamFOVCoveragePercentEv
+ __ZNK7Buckets13getBucketNameEf
+ __ZNK9MatrixMxNILj1ELj9EdE4SortILj1EvEES0_v
+ __ZNK9MatrixMxNILj3ELj3EdEmlILj3ELj3ELj3EvEES_ILj3EXT_EdERKS2_
+ __ZNK9MatrixMxNILj3ELj4EdEmlERK6MatrixIdE
+ __ZNKSt3__119__shared_weak_count13__get_deleterERKSt9type_info
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED1B8ne200100Ev
+ __ZNSt3__110shared_ptrIN3jpc9IIFABlock9IFAOutputEED2B8ne200100Ev
+ __ZNSt3__110unique_ptrIN3jpc9IIFABlock9IFAOutputENS_14default_deleteIS3_EEED2B8ne200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIm20PixelBufferSharedPtrEEPvEENS_22__hash_node_destructorINS_9allocatorIS6_EEEEED1B8ne200100Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIm20PixelBufferSharedPtrEENS_22__unordered_map_hasherImS3_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS3_S8_S6_Lb1EEENS_9allocatorIS3_EEE25__emplace_unique_key_argsImJRKNS_21piecewise_construct_tENS_5tupleIJRKmEEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS3_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEED2Ev
+ __ZNSt3__112__hash_tableImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeImPvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ne200100IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_no_aliasILb0EEERS5_PKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_no_aliasILb1EEERS5_PKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__113__nth_elementB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEm
+ __ZNSt3__113unordered_mapIyNS_4pairIPhiEENS_4hashIyEENS_8equal_toIyEENS_9allocatorINS1_IKyS3_EEEEEC2ESt16initializer_listISA_E
+ __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ne200100Ev
+ __ZNSt3__113unordered_setImNS_4hashImEENS_8equal_toImEENS_9allocatorImEEED1B8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__119__shared_weak_count14__release_weakEv
+ __ZNSt3__119__shared_weak_countD2Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__shared_ptr_emplaceIN3jpc12JPCExceptionENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN3jpc12JPCExceptionENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN3jpc12JPCExceptionENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN3jpc12JPCExceptionENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceISt9exceptionNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceISt9exceptionNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceISt9exceptionNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceISt9exceptionNS_9allocatorIS1_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIPN3jpc9IIFABlock9IFAOutputENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPN3jpc9IIFABlock9IFAOutputENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPN3jpc9IIFABlock9IFAOutputENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPN3jpc9IIFABlock9IFAOutputENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEED1Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__125__independent_bits_engineINS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEmE6__evalENS_17integral_constantIbLb1EEE
+ __ZNSt3__125__throw_bad_function_callB8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_6vectorI11MatrixNxPtsILj1EdENS_9allocatorIS3_EEE16__destroy_vectorEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_6vectorINS1_IiNS_9allocatorIiEEEENS2_IS4_EEE16__destroy_vectorEED2B8ne200100Ev
+ __ZNSt3__14__fs10filesystem20__create_directoriesERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14coutE
+ __ZNSt3__14pairI12SparseMatrix11MatrixNxPtsILj1EdEED1Ev
+ __ZNSt3__14pairINS_6vectorIfNS_9allocatorIfEEEES4_ED2Ev
+ __ZNSt3__15tupleIJ11MatrixNxPtsILj2EdES2_S1_ILj1EdEEED2Ev
+ __ZNSt3__15tupleIJbffNS_6vectorIfNS_9allocatorIfEEEES4_NS1_I31ADDisparityToDepthFitWorldPointNS2_IS5_EEEEEED2Ev
+ __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
+ __ZNSt3__16__sortIRNS_6__lessIttEEPtEEvT0_S5_T_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI11MatrixNxPtsILj1EdENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIDv3_fNS_9allocatorIS1_EEE8__appendEm
+ __ZNSt3__16vectorIN3jpc18IPreprocessorBlock19PearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3jpc18IPreprocessorBlock25PearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3jpc9IIFABlock22IFAPearlCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE18__assign_with_sizeB8ne200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN3jpc9IIFABlock28IFAPearlJasperCorrespondenceENS_9allocatorIS3_EEE9push_backB8ne200100ERKS3_
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED1B8ne200100Ev
+ __ZNSt3__16vectorINS0_IiNS_9allocatorIiEEEENS1_IS3_EEED2B8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc11IIFA_FilterENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN3jpc15IFAPullCriteriaENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEED2B8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIU8__strongP8NSStringNS_9allocatorIS3_EEED2B8ne200100Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8ne200100EOi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__18functionIFNS_6vectorI7CGPointNS_9allocatorIS2_EEEERKNS1_IDv3_fNS3_IS6_EEEEEED2Ev
+ __ZNSt9exceptionD2Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTIN3jpc12JPCExceptionE
+ __ZTISt13runtime_error
+ __ZTSN3jpc12JPCExceptionE
+ __ZTSSt13runtime_error
+ __ZTTNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTV11MatrixNxPtsILj4EdE
+ __ZTV20PixelBufferSharedPtr
+ __ZTVN3jpc11PORIFABlockE
+ __ZTVN3jpc12JPCExceptionE
+ __ZTVN3jpc13PORGMCJ_BlockE
+ __ZTVN3jpc16IFA_FilterRunnerE
+ __ZTVN3jpc17CVPixelBufferLockE
+ __ZTVN3jpc17IFAPRGScoreFilterE
+ __ZTVN3jpc17IFAPoseDiffFilterE
+ __ZTVN3jpc18IFAFailedExceptionE
+ __ZTVN3jpc19CVPixelBufferHelperIhEE
+ __ZTVN3jpc19CVPixelBufferHelperIsEE
+ __ZTVN3jpc19CVPixelBufferHelperItEE
+ __ZTVN3jpc19GMCJFailedExceptionE
+ __ZTVN3jpc19IFASimpleAggregatorE
+ __ZTVN3jpc20IFAJConfidenceFilterE
+ __ZTVN3jpc20IFAJDepthRangeFilterE
+ __ZTVN3jpc20IFANotReadyExceptionE
+ __ZTVN3jpc20IFAPJDepthDiffFilterE
+ __ZTVN3jpc20PORPreprocessorBlockE
+ __ZTVN3jpc21IFAPullCriteriaRunnerE
+ __ZTVN3jpc23IFAPLocalDepthVarFilterE
+ __ZTVN3jpc24IFADepthCoverageCriteriaE
+ __ZTVN3jpc24IFASpatialCoverageFilterE
+ __ZTVN3jpc25IFAJPtsIDCoverageCriteriaE
+ __ZTVN3jpc25IFAThermalTransientFilterE
+ __ZTVN3jpc26IFAPJWorkDistOverlapFilterE
+ __ZTVN3jpc26PORPreprocessorFilterBlockE
+ __ZTVN3jpc27IFAPearlFovCoverageCriteriaE
+ __ZTVN3jpc28PreprocessingFailedExceptionE
+ __ZTVN3jpc30PORGMCJ_OutputValidation_BlockE
+ __ZTVN3jpc38GMCJOutputValidationNotPassedExceptionE
+ __ZTVN3jpc3JPCE
+ __ZTVN3jpc40PreprocessingFilterInvalidFrameExceptionE
+ __ZTVN3jpc44GMCJOutputValidationMetricIncreasedExceptionE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN3jpc12JPCExceptionENS_9allocatorIS2_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceISt9exceptionNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPN3jpc9IIFABlock9IFAOutputENS_10shared_ptrIS3_E27__shared_ptr_default_deleteIS3_S3_EENS_9allocatorIS3_EEEE
+ __ZTVSt9exception
+ __ZZ24+[ADLogManager defaults]E6result
+ __ZZ33+[ADJasperColorExecutor defaults]E6result
+ __ZZ33+[ADMetricDepthExecutor defaults]E6result
+ __ZZ33+[ADMetricDepthPipeline defaults]E6result
+ __ZZ33+[ADVisualDepthPipeline defaults]E6result
+ __ZZ37+[ADLKTOpticalFlow highQualityConfig]E17highQualityConfig
+ __ZZ41+[ADLKTOpticalFlow highPerformanceConfig]E21highPerformanceConfig
+ __ZZ43+[ADMetricDepthPipelineParameters defaults]E6result
+ __ZZ50+[ADPearlColorInFieldCalibrationPipeline defaults]E6result
+ __ZZ51+[ADJasperColorInFieldCalibrationExecutor defaults]E6result
+ __ZZ58+[ADDeviceConfiguration hasLidarToColorIncreasedBaseline:]E24increasedBaselineDevices
+ __ZZ58+[ADPearlColorInFieldCalibrationInterSessionData defaults]E6result
+ __ZZ59+[ADJasperColorInFieldCalibrationInterSessionData defaults]E6result
+ __ZZ59-[ADJasperPearlInFieldCalibrationPipeline logJpcInputData:]E9timestamp
+ __ZZ60+[ADPearlColorInFieldCalibrationPipelineParameters defaults]E6result
+ __ZZ61+[ADJasperColorInFieldCalibrationPipelineParameters defaults]E6result
+ __ZZ63+[ADJasperColorInFieldCalibrationControllerParameters defaults]E6result
+ __ZZN14BucketsFilters7BucketsEvE4inst
+ __ZZN3jpc12JPCPORConfig12PORISFConfigEvE6config
+ __ZZN3jpc12JPCPORConfig17PORIFABlockConfigEvE6config
+ __ZZN3jpc12JPCPORConfig18PORGMCJBlockConfigEvE6config
+ __ZZN3jpc12JPCPORConfig32PORPreprocessorFilterBlockConfigEvE11preferences
+ __ZZN3jpc12JPCPORConfig32PORPreprocessorFilterBlockConfigEvE6config
+ __ZZN3jpc9JPCConfig17readJpcConfigFileEvE14configFileDict
+ ___70+[ADJasperPearlInFieldCalibrationTelemetry reportTriggeringTelemetry:]_block_invoke
+ ___75+[ADJasperPearlInFieldCalibrationTelemetry reportTelemetry:firstTimeEvent:]_block_invoke
+ ___81-[ADBinocularDepthExecutor sendAnalyticsWithRefSaturationRate:auxSaturationRate:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e26_"NSMutableDictionary"8?0ls32l8
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.6379
+ ___block_literal_global.8806
+ ___sincos_stret
+ _kADDeviceConfigurationDomainName
+ _kADDeviceConfigurationKeyJasperColorInFieldSDFHistorySize
+ _kADDeviceConfigurationKeyJasperColorRemoveShortRangeOccludedPointsOnLargeBaselineDevices
+ _kADDeviceConfigurationKeyJasperPearlInFieldMaxJasperGlareSpots
+ _kADDeviceConfigurationKeyJasperPearlInFieldMaxJasperReflectiveSpots
+ _kADDeviceConfigurationKeyJasperPearlInFieldMaxRotationBetweenFrames
+ _kADDeviceConfigurationKeyJasperPearlInFieldMaxTranslationBetweenFrames
+ _kADDeviceConfigurationKeyJasperPearlInFieldMinRotationBetweenFrames
+ _kADDeviceConfigurationKeyJasperPearlInFieldMinTranslationBetweenFrames
+ _kADDeviceConfigurationKeyLoggingForceCounterAsTimestamp
+ _kADDeviceConfigurationKeyMetricDepthActiveMaskMode
+ _kADDeviceConfigurationKeyMetricDepthEmulatePeridot
+ _kADDeviceConfigurationKeyMetricDepthGraphJPEGDumpPath
+ _kADDeviceConfigurationKeyMetricDepthIgnoreActiveSensors
+ _kADDeviceConfigurationKeyMetricDepthPearlJasperCoFilteringMaxAllowedDisagreement
+ _kADDeviceConfigurationKeyMetricDepthPearlJasperCoFilteringMaxPearlDepth
+ _kADDeviceConfigurationKeyOverrideDeviceName
+ _kADDeviceConfigurationKeyVisualDepthFovScale
+ _kADDeviceConfigurationKeyVisualDepthMeshRenderRatio
+ _kADDeviceConfigurationKeyVisualDepthMinLevel
+ _kADDeviceConfigurationKeyVisualDepthOcclusionScale
+ _kADDeviceConfigurationKeyVisualDepthOutputDisparity
+ _kCGColorSpaceITUR_709
+ _nanf
+ _objc_msgSend$_computeConfidence:shiftMap:outConfidceMap:cropSizeRatio:
+ _objc_msgSend$_computeFeaturesDerivativesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:
+ _objc_msgSend$_computeFeaturesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:
+ _objc_msgSend$_createImagePyramidWithCommandBuffer:cropSizeRatio:inOutPyramidsArray:error:
+ _objc_msgSend$_createImagePyramidWithCommandBuffer:in_tex:cropSizeRatio:outPyramidsArray:error:
+ _objc_msgSend$_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:cropSizeRatio:
+ _objc_msgSend$_doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:in_uv_tex:out_uv_tex:out_w_tex:uniforms:cropSizeRatio:
+ _objc_msgSend$_downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:cropSizeRatio:
+ _objc_msgSend$_prepareLKTGPUUniforms:out_uv_tex:coeff:stride:computeConfidenceComponents:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addKeyframeInput:timestamp:
+ _objc_msgSend$addMeshInput:
+ _objc_msgSend$addPrimaryCalibration:secondaryCalibration:timestamp:
+ _objc_msgSend$aggData
+ _objc_msgSend$aggPointsWrapperObj
+ _objc_msgSend$aggregateForTime:worldToCameraTransform:
+ _objc_msgSend$aggregationParameters
+ _objc_msgSend$aggregationSize
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$applyPerformanceOverrides
+ _objc_msgSend$autoSetColorROI
+ _objc_msgSend$auxOutputCalib
+ _objc_msgSend$auxRectifiedCalib
+ _objc_msgSend$auxiliaryColorInput
+ _objc_msgSend$auxiliaryConfidenceOutput
+ _objc_msgSend$auxiliaryDisparityOutput
+ _objc_msgSend$auxiliarySegmentationOutput
+ _objc_msgSend$backProject:undistortedPixels:withZ:outPoints:
+ _objc_msgSend$blitCommandEncoder
+ _objc_msgSend$buffer
+ _objc_msgSend$bufferExists:isInput:
+ _objc_msgSend$buildISFInputDictWithEFL:principalPointtX:principalPointtY:rotationMat:
+ _objc_msgSend$buildJpcInputDataObjectWithPearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:outJpcInputs:
+ _objc_msgSend$buildMetalPipelineWithQueue:lensDistortion:
+ _objc_msgSend$caCurrentTriggerEndReasonIsConvergence
+ _objc_msgSend$caCurrentTriggerEndReasonIsMaxFrameCount
+ _objc_msgSend$caCurrentTriggerEndReasonIsOutputValidationMetricIncreased
+ _objc_msgSend$caCurrentTriggerFirstFrameTemperature
+ _objc_msgSend$caCurrentTriggerFirstFrameTimestamp
+ _objc_msgSend$caCurrentTriggerFrameCount
+ _objc_msgSend$caCurrentTriggerLastFrameTemperature
+ _objc_msgSend$caCurrentTriggerLastFrameTimestamp
+ _objc_msgSend$caLastTriggerLastFrameTemperature
+ _objc_msgSend$caLastTriggerLastFrameTimestamp
+ _objc_msgSend$cameraEmbeddingInput
+ _objc_msgSend$cameraPixels
+ _objc_msgSend$checkFlowInFOV
+ _objc_msgSend$checkPrerequisitesForProcessWithPearlWithPearlInputs:
+ _objc_msgSend$checkProjectionChanged:newCalib:
+ _objc_msgSend$clearBuffer
+ _objc_msgSend$commandBufferWithUnretainedReferences
+ _objc_msgSend$commitAndWaitUntilSubmitted
+ _objc_msgSend$computeCropForRectifiedImage:calib:
+ _objc_msgSend$conditionNumberMaxValue
+ _objc_msgSend$conditionNumberMinValue
+ _objc_msgSend$confidenceForPrimaryPoV
+ _objc_msgSend$confidenceForSecondaryPoV
+ _objc_msgSend$confidenceLevels
+ _objc_msgSend$confidenceParameters
+ _objc_msgSend$contents
+ _objc_msgSend$convertInputFormatIfNeeded:greyscaleInput:
+ _objc_msgSend$copyConfidenceAllowPixelFormatChange:outputConfidence:
+ _objc_msgSend$copyFromTexture:toTexture:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$coreAnalyticsEventInterval
+ _objc_msgSend$createCameraEmbeddingsForRightCameraCalibration:leftCameraCalibration:rightCameraPose:leftCameraPose:outputBuffer:
+ _objc_msgSend$createColorConvertingSession:
+ _objc_msgSend$createConfidenceBuffer
+ _objc_msgSend$createIntrinsicsMatrixWithEFL:principalPointX:principalPointY:
+ _objc_msgSend$createIntrinsicsMatrixWithEflX:eflY:principalPointX:principalPointY:
+ _objc_msgSend$createJasperEmbeddings:cropTo:rotateBy:outputBuffer:outputBatchOffset:
+ _objc_msgSend$createJasperEmbeddingsForRightCameraPointCloud:leftCameraPointCloud:crop:rotation:outputBuffer:
+ _objc_msgSend$createOpticalFlowBuffer
+ _objc_msgSend$createRequestedLayoutsForDimensions:layout:function:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$deallocInferenceBuffers
+ _objc_msgSend$deallocateVisualDepthBuffers
+ _objc_msgSend$defaults
+ _objc_msgSend$depthDiffThresholdAboveMedian
+ _objc_msgSend$depthForPrimaryPoV
+ _objc_msgSend$depthForSecondaryPoV
+ _objc_msgSend$depthMask
+ _objc_msgSend$descriptorWithDefaultSize:pixelFormat:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$distort:undistortedPixels:outDistorted:
+ _objc_msgSend$distortedRadii
+ _objc_msgSend$downscaleImageAndGenerateMipmapsIfNeeded:inputTexture:
+ _objc_msgSend$downscaledInputDescriptor
+ _objc_msgSend$downscaledInputSizeForLayout:
+ _objc_msgSend$dx
+ _objc_msgSend$dy
+ _objc_msgSend$echoIds
+ _objc_msgSend$efl
+ _objc_msgSend$embedDepthMapUsingFourierEncoding:outputBuffer:outputChannelOffset:outputBatchOffset:
+ _objc_msgSend$emptyFilter
+ _objc_msgSend$emulatePeridotFromJasper:jasperPoses:jasperTimestamps:jasperToPlatformTransform:pearlDepth:pearlPose:pearlCalibration:outPointCloud:outPose:outTimestamp:
+ _objc_msgSend$encodeOpticalFlowSolverToCommandBuffer:currentFeaturesArray:currentDerivitiveArray:previousFeaturesArray:previousDerivitiveArray:currentPyramidsArray:validBufferRect:outShiftMap:outConfidenceMap:
+ _objc_msgSend$encodePredictionToCommandBuffer:primaryColorInput:secondaryColorInput:primaryPredictionOutput:secondaryPredictionOutput:primaryOcclusionOutput:secondaryOcclusionOutput:predictionTimestamp:predictionPose:poseSessionID:poseReinitCount:
+ _objc_msgSend$encodePyramidFeaturesToCommandBuffer:grayscaleTexture:validBufferRect:outPyramidsArray:outFeaturesArray:outDerivitiveArray:
+ _objc_msgSend$encodeSignalEvent:value:
+ _objc_msgSend$encodeToCommandBuffer:sourceTexture:destinationTexture:
+ _objc_msgSend$executeFromFrame:toFrame:outputOpticalFlow:outputConfidence:
+ _objc_msgSend$executeFromFrame:toFrame:validBufferRect:outputOpticalFlow:outputConfidence:
+ _objc_msgSend$executeFromFrameToPreviousFrame:outputOpticalFlow:outputConfidence:
+ _objc_msgSend$executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:
+ _objc_msgSend$executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:
+ _objc_msgSend$executeWithColor:outDepthMap:
+ _objc_msgSend$executeWithColor:pointCloud:outDepthMap:outConfMap:worldToCameraTransform:cameraCalibration:
+ _objc_msgSend$executeWithColor:timestamp:pointClouds:lidarCalibration:colorMetadata:colorCameraCalibration:outputDepthMap:outputConfidenceMap:outputCalibration:
+ _objc_msgSend$executeWithOutput:
+ _objc_msgSend$executeWithPrimaryColor:secondaryColor:pearl:pointClouds:primaryColorCalibration:secondaryColorCalibration:pearlCalibration:lidarCameraCalibration:primaryColorPose:secondaryColorPose:pearlPose:pointCloudPoses:timestamp:outputDepthMap:outputUncertaintyMap:outputConfidenceMap:outputConfidenceLevels:outputNormalsMap:outputActiveDepthMaskMap:outputDepthCalibration:
+ _objc_msgSend$executeWithRefColor:auxColor:auxOutputDepth:auxOutputConfidence:timestamp:
+ _objc_msgSend$executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:
+ _objc_msgSend$executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputCalib:timestamp:
+ _objc_msgSend$executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputSegmentation:auxOutputCalib:timestamp:
+ _objc_msgSend$executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:timestamp:
+ _objc_msgSend$executeWithRefColor:auxColor:refCalib:auxCalib:timestamp:
+ _objc_msgSend$executeWithRefColor:auxColor:timestamp:
+ _objc_msgSend$expectedColorSensorROI
+ _objc_msgSend$extractIRSensorCalibFromLastSyncMatch
+ _objc_msgSend$extractJasperToPearlCalibFromLastSyncMatch
+ _objc_msgSend$extractPearlInputsFromLastSyncMatch
+ _objc_msgSend$extractPearlPrevPoseFromLastSyncMatch
+ _objc_msgSend$extractYChannelFromColorInput:toBuffer:
+ _objc_msgSend$fillSensorsMask:
+ _objc_msgSend$fillTelemetryData:jpcError:
+ _objc_msgSend$fillTelemetryDataWithPreviousCalibration:pceCalib:
+ _objc_msgSend$filterJasperPointCloud:usingPearlInput:
+ _objc_msgSend$filterUncertainty:output:
+ _objc_msgSend$firstIFAFrameTimestampCurrentExecution
+ _objc_msgSend$firstTimeEventFired
+ _objc_msgSend$fixEFLTempCoeffInISFResult:eflTempCoeff:temperature:
+ _objc_msgSend$flags
+ _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:
+ _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:alpha:confidenceUnits:
+ _objc_msgSend$generateMipmapsForTexture:
+ _objc_msgSend$getIRSensorCameraCalibFromPCECalib
+ _objc_msgSend$getJpcObjectForRunMode:isValid:
+ _objc_msgSend$getPCECalibStruct
+ _objc_msgSend$getRealDeviceName
+ _objc_msgSend$getRectifiedColorInputSaturationRate
+ _objc_msgSend$getTeleAfPlatformType
+ _objc_msgSend$gmcjErrorCode
+ _objc_msgSend$gmcjOutputValidationErrorCode
+ _objc_msgSend$gmcjPPXChangeMicronFromPrev
+ _objc_msgSend$gmcjPPXChangeMicronFromT0
+ _objc_msgSend$gmcjPPYChangeMicronFromPrev
+ _objc_msgSend$gmcjPPYChangeMicronFromT0
+ _objc_msgSend$gmcjProjRotXChangeFromPrev
+ _objc_msgSend$gmcjProjRotXChangeFromT0
+ _objc_msgSend$gmcjProjRotYChangeFromPrev
+ _objc_msgSend$gmcjProjRotYChangeFromT0
+ _objc_msgSend$gmcjProjRotZChangeFromPrev
+ _objc_msgSend$gmcjProjRotZChangeFromT0
+ _objc_msgSend$gmcjScaleChangePercentFromPrev
+ _objc_msgSend$gmcjScaleChangePercentFromT0
+ _objc_msgSend$gradientNormMaxValue
+ _objc_msgSend$gradientNormMinValue
+ _objc_msgSend$hasLidarToColorIncreasedBaseline:
+ _objc_msgSend$highPerformanceConfig
+ _objc_msgSend$highQualityConfig
+ _objc_msgSend$ignoreDistortionInDepthReprojection
+ _objc_msgSend$imageDimensionsWithWidth:height:
+ _objc_msgSend$inferencePixelBufferForDescriptor:outputUserBuffer:
+ _objc_msgSend$init
+ _objc_msgSend$initDiagnosticPipelineLog
+ _objc_msgSend$initForEspressoEngine:
+ _objc_msgSend$initForEspressoEngine:pipelineParameters:
+ _objc_msgSend$initWithAggregationParameters:jasperToColorTransform:colorCamera:
+ _objc_msgSend$initWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:
+ _objc_msgSend$initWithBands:maxResolution:sourceFactor:
+ _objc_msgSend$initWithBuffer:count:offset:stride:
+ _objc_msgSend$initWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:
+ _objc_msgSend$initWithDescriptor:forLayout:executorParameters:
+ _objc_msgSend$initWithDevice:
+ _objc_msgSend$initWithDevice:inputSize:config:confidenceParameters:
+ _objc_msgSend$initWithDistortionCenter:distortedRadii:undistortedRadii:
+ _objc_msgSend$initWithDomain:defaultValues:
+ _objc_msgSend$initWithExecutor:calculateConfidenceMap:calculateConfidenceLevels:
+ _objc_msgSend$initWithImage:confidence:labels:normals:calibration:uuid:pose:timestamp:
+ _objc_msgSend$initWithLength:
+ _objc_msgSend$initWithMetalCommandQueue:dimensions:format:
+ _objc_msgSend$initWithNetwork:requestedLayouts:espressoEngine:makeRunnable:
+ _objc_msgSend$initWithNetworkProvider:prioritization:espressoEngine:
+ _objc_msgSend$initWithOutputDimensions:
+ _objc_msgSend$initWithParameters:pceCalib:
+ _objc_msgSend$initWithPearlDepth:pearlDx:pearlDy:pearlScore:
+ _objc_msgSend$initWithPrioritization:espressoEngine:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$initWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:
+ _objc_msgSend$inputWithImage:confidence:calibration:
+ _objc_msgSend$insertEntryToDiagnosticPipelineLog:
+ _objc_msgSend$intervalBetweenIFAFrames
+ _objc_msgSend$irCamFOVCoveragePercent
+ _objc_msgSend$isAssignedGMCJBlock
+ _objc_msgSend$isAssignedGMCJValidation
+ _objc_msgSend$isAssignedIFABlock
+ _objc_msgSend$isAssignedJasperReflectionsFrameFilter
+ _objc_msgSend$isAssignedPipelineCurrent
+ _objc_msgSend$isAssignedPipelinePrevious
+ _objc_msgSend$isReadyForExecution
+ _objc_msgSend$isReportTelemetry
+ _objc_msgSend$jasperMisalignmentAfter
+ _objc_msgSend$jasperMisalignmentBefore
+ _objc_msgSend$jpcErrorCode
+ _objc_msgSend$lastAlgoRadarTriggerTimestamp
+ _objc_msgSend$lastIFAFrameTimestampCurrentExecution
+ _objc_msgSend$lastPearlTemp
+ _objc_msgSend$logJPCInputs:
+ _objc_msgSend$logJasperAggPC:timestamp:
+ _objc_msgSend$logJpcInputData:
+ _objc_msgSend$logPose:logMessagePrefix:
+ _objc_msgSend$makeRunnable
+ _objc_msgSend$maxCenterResolution
+ _objc_msgSend$maxIRCamTemperature
+ _objc_msgSend$maxIRCamTemperatureCurrentExecution
+ _objc_msgSend$maxJasperDepth
+ _objc_msgSend$maxRaysResolution
+ _objc_msgSend$meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:
+ _objc_msgSend$meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:
+ _objc_msgSend$meshChunkWithVertices:faces:confidence:classification:uuid:timestamp:longRange:
+ _objc_msgSend$meshChunks
+ _objc_msgSend$meshKeyframes
+ _objc_msgSend$metalDescriptor
+ _objc_msgSend$metricDepth
+ _objc_msgSend$minIRCamTemperature
+ _objc_msgSend$minIRCamTemperatureCurrentExecution
+ _objc_msgSend$modelBuilderForModelPath:destinationPath:buildConfigPath:forANE:
+ _objc_msgSend$motionBetweenFramesRotationX
+ _objc_msgSend$motionBetweenFramesRotationY
+ _objc_msgSend$motionBetweenFramesRotationZ
+ _objc_msgSend$motionBetweenFramesTranslationX
+ _objc_msgSend$motionBetweenFramesTranslationY
+ _objc_msgSend$motionBetweenFramesTranslationZ
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableConfidences
+ _objc_msgSend$mutablePoints
+ _objc_msgSend$newEfl
+ _objc_msgSend$newPPX
+ _objc_msgSend$newPPY
+ _objc_msgSend$newRotX
+ _objc_msgSend$newRotY
+ _objc_msgSend$newRotZ
+ _objc_msgSend$newSharedEvent
+ _objc_msgSend$normals
+ _objc_msgSend$numCenterBands
+ _objc_msgSend$numJasperBands
+ _objc_msgSend$numJasperSpotsFlaggedAsGlare
+ _objc_msgSend$numJasperSpotsFlaggedAsReflectiveSurface
+ _objc_msgSend$numOfAggregatedFrames
+ _objc_msgSend$numOfIFAFramesCurrentExecution
+ _objc_msgSend$numOfUniqueTOFSpots
+ _objc_msgSend$numPearlJasperCorrespondencesPostLocalDepthVarFilter
+ _objc_msgSend$numPearlJasperCorrespondencesPostPJDepthDiffFilter
+ _objc_msgSend$numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter
+ _objc_msgSend$numPearlJasperCorrespondencesPreIFA
+ _objc_msgSend$numPearlOnlyCorrespondencesPostSpatialCoverageFilter
+ _objc_msgSend$numPearlOnlyCorrespondencesPreIFA
+ _objc_msgSend$numRaysBands
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$occlusionForPrimaryPoV
+ _objc_msgSend$occlusionForSecondaryPoV
+ _objc_msgSend$offset
+ _objc_msgSend$outputNormalsDescriptor
+ _objc_msgSend$outputSizeForLayout:
+ _objc_msgSend$outputWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:
+ _objc_msgSend$outputWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:
+ _objc_msgSend$overrideCVCalIntrinsicsWithPCECalibIntrinsics:temperature:
+ _objc_msgSend$pceCalib
+ _objc_msgSend$pearl
+ _objc_msgSend$pearlCalibSetSize
+ _objc_msgSend$pearlDepth
+ _objc_msgSend$pearlDx
+ _objc_msgSend$pearlDy
+ _objc_msgSend$pearlJapserCalibSetSize
+ _objc_msgSend$pearlJasperCoFilteringMaxAllowedDisagreement
+ _objc_msgSend$pearlJasperCoFilteringMaxPearlDepth
+ _objc_msgSend$pearlProjectedPixelCount
+ _objc_msgSend$pearlScore
+ _objc_msgSend$pearlTemperature
+ _objc_msgSend$pearlToLastJasperBankRotation
+ _objc_msgSend$pearlToLastJasperBankRotationX
+ _objc_msgSend$pearlToLastJasperBankRotationY
+ _objc_msgSend$pearlToLastJasperBankRotationZ
+ _objc_msgSend$pearlToLastJasperBankTranslation
+ _objc_msgSend$pearlToLastJasperBankTranslationX
+ _objc_msgSend$pearlToLastJasperBankTranslationY
+ _objc_msgSend$pearlToLastJasperBankTranslationZ
+ _objc_msgSend$pointCloudAggregationParameters
+ _objc_msgSend$pointCloudByChangingPointOfViewFrom:to:
+ _objc_msgSend$pointCloudByRemovingPeridotShortRangeOccludedPoints:
+ _objc_msgSend$points
+ _objc_msgSend$poolWithDepthDescriptor:confidenceDescriptor:
+ _objc_msgSend$postProcessDisparity:outputDepth:
+ _objc_msgSend$postProcessEspressoConfidence:outputConfidence:
+ _objc_msgSend$postProcessEspressoConfidence:outputConfidence:confidenceUnits:
+ _objc_msgSend$postProcessEspressoDepth:espressoConfidence:espressoNormals:toOutputDepth:outputConfidence:outputNormals:
+ _objc_msgSend$postProcessEspressoDepth:espressoConfidence:toOutputDepth:outputConfidence:
+ _objc_msgSend$postProcessEspressoNormals:toOutputNormals:
+ _objc_msgSend$postProcessWithDepth:confidence:depthOutput:confidenceOutput:
+ _objc_msgSend$preAllocateInferencePixelBufferForDescriptor:
+ _objc_msgSend$preferencesWithDefaultValues:
+ _objc_msgSend$prepareForEngineType:roi:exifOrientation:
+ _objc_msgSend$prepareForInputRoi:
+ _objc_msgSend$prepareStereoWarpMeshesWithRefCalib:auxCalib:
+ _objc_msgSend$preprocessPearlDepth:pearlPose:pearlCalibration:colorPose:colorCalibration:outputBuffer:
+ _objc_msgSend$prevEfl
+ _objc_msgSend$prevPPX
+ _objc_msgSend$prevPPY
+ _objc_msgSend$prevPose
+ _objc_msgSend$prevRotX
+ _objc_msgSend$prevRotY
+ _objc_msgSend$prevRotZ
+ _objc_msgSend$primaryColorInput
+ _objc_msgSend$primaryOcclusionMapOutput
+ _objc_msgSend$primaryPredictionConfidenceOutput
+ _objc_msgSend$primaryPredictionOutput
+ _objc_msgSend$primaryRasterizedMeshInput
+ _objc_msgSend$principalPointX
+ _objc_msgSend$principalPointY
+ _objc_msgSend$printOutResults:
+ _objc_msgSend$processFrame:validBufferRect:intoOpticalFlowBuffer:outputConfidence:
+ _objc_msgSend$processJpcResult:
+ _objc_msgSend$processJpcResultWithStatus:gmcjResult:glaResult:result:interSessionData:temperature:eflTempCoeff:
+ _objc_msgSend$processMatch:
+ _objc_msgSend$processWithPearl:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:
+ _objc_msgSend$providerForNetwork:requestedLayouts:espressoEngine:makeRunnable:
+ _objc_msgSend$providerForNetwork:requestedLayouts:makeRunnable:
+ _objc_msgSend$pushData:streamIndex:timestamp:pose:meta:
+ _objc_msgSend$pushPointCloud:timestamp:worldToCameraTransform:
+ _objc_msgSend$rangesForUnits:
+ _objc_msgSend$readJsonMetadataFile:requestedLayouts:
+ _objc_msgSend$rectifiedCameraFieldOfViewHeight
+ _objc_msgSend$rectifiedCameraFieldOfViewWidth
+ _objc_msgSend$rectifyCameraPairForLeftCalib:rightCalib:leftRectifiedCameraToPlatformTransform:rightRectifiedCameraToPlatformTransform:prioritization:
+ _objc_msgSend$refRectifiedCalib
+ _objc_msgSend$referenceColorInput
+ _objc_msgSend$removeObject:
+ _objc_msgSend$reportTelemetry:firstTimeEvent:
+ _objc_msgSend$reprojectionErrorAfter
+ _objc_msgSend$reprojectionErrorBefore
+ _objc_msgSend$resetIFAObjects
+ _objc_msgSend$resetSdfHistory
+ _objc_msgSend$rotArray
+ _objc_msgSend$rotateConfidenceAllowPixelFormatChange:rotation:outputConfidence:
+ _objc_msgSend$runWithJpc:runMode:pearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:
+ _objc_msgSend$runnableModelPath
+ _objc_msgSend$saturationCheckInterval
+ _objc_msgSend$saturationThreshold
+ _objc_msgSend$scaleIdxForConfidenceComponents
+ _objc_msgSend$score
+ _objc_msgSend$sdfHistorySize
+ _objc_msgSend$secondaryColor
+ _objc_msgSend$secondaryColorInput
+ _objc_msgSend$secondaryOcclusionMapOutput
+ _objc_msgSend$secondaryPredictionConfidenceOutput
+ _objc_msgSend$secondaryPredictionOutput
+ _objc_msgSend$secondaryRasterizedMeshInput
+ _objc_msgSend$sendAnalyticsWithRefSaturationRate:auxSaturationRate:
+ _objc_msgSend$sensorTemperature
+ _objc_msgSend$setAggPoints:
+ _objc_msgSend$setAggPointsWrapperObj:
+ _objc_msgSend$setAllPosesValid:
+ _objc_msgSend$setCaCurrentTriggerEndReasonIsConvergence:
+ _objc_msgSend$setCaCurrentTriggerEndReasonIsMaxFrameCount:
+ _objc_msgSend$setCaCurrentTriggerEndReasonIsOutputValidationMetricIncreased:
+ _objc_msgSend$setCaCurrentTriggerFirstFrameTemperature:
+ _objc_msgSend$setCaCurrentTriggerFirstFrameTimestamp:
+ _objc_msgSend$setCaCurrentTriggerFrameCount:
+ _objc_msgSend$setCaCurrentTriggerLastFrameTemperature:
+ _objc_msgSend$setCaCurrentTriggerLastFrameTimestamp:
+ _objc_msgSend$setCaLastTriggerLastFrameTemperature:
+ _objc_msgSend$setCaLastTriggerLastFrameTimestamp:
+ _objc_msgSend$setColorInput:calib:toNetworkBuffer:isRef:crop:
+ _objc_msgSend$setColorPoseRoll:
+ _objc_msgSend$setDepthDiffThresholdAboveMedian:
+ _objc_msgSend$setDepthSensorsIgnored:
+ _objc_msgSend$setDuplicateProjectedSpotsMode:
+ _objc_msgSend$setDx:
+ _objc_msgSend$setDy:
+ _objc_msgSend$setEfl:
+ _objc_msgSend$setFilter:
+ _objc_msgSend$setFirstIFAFrameTimestampCurrentExecution:
+ _objc_msgSend$setFirstTimeEventFired:
+ _objc_msgSend$setGMCJResult:result:temperature:
+ _objc_msgSend$setGmcjErrorCode:
+ _objc_msgSend$setGmcjOutputValidationErrorCode:
+ _objc_msgSend$setGmcjPPXChangeMicronFromPrev:
+ _objc_msgSend$setGmcjPPXChangeMicronFromT0:
+ _objc_msgSend$setGmcjPPYChangeMicronFromPrev:
+ _objc_msgSend$setGmcjPPYChangeMicronFromT0:
+ _objc_msgSend$setGmcjProjRotXChangeFromPrev:
+ _objc_msgSend$setGmcjProjRotXChangeFromT0:
+ _objc_msgSend$setGmcjProjRotYChangeFromPrev:
+ _objc_msgSend$setGmcjProjRotYChangeFromT0:
+ _objc_msgSend$setGmcjProjRotZChangeFromPrev:
+ _objc_msgSend$setGmcjProjRotZChangeFromT0:
+ _objc_msgSend$setGmcjScaleChangePercentFromPrev:
+ _objc_msgSend$setGmcjScaleChangePercentFromT0:
+ _objc_msgSend$setIntervalBetweenIFAFrames:
+ _objc_msgSend$setIrCamFOVCoveragePercent:
+ _objc_msgSend$setIsAssignedGMCJBlock:
+ _objc_msgSend$setIsAssignedGMCJValidation:
+ _objc_msgSend$setIsAssignedIFABlock:
+ _objc_msgSend$setIsAssignedJasperReflectionsFrameFilter:
+ _objc_msgSend$setIsAssignedPipelineCurrent:
+ _objc_msgSend$setIsAssignedPipelinePrevious:
+ _objc_msgSend$setIsReportTelemetry:
+ _objc_msgSend$setJasperInputSpotCount:
+ _objc_msgSend$setJasperMisalignmentAfter:
+ _objc_msgSend$setJasperMisalignmentBefore:
+ _objc_msgSend$setJasperPoseDistance:
+ _objc_msgSend$setJasperProjectedSpotCount:
+ _objc_msgSend$setJasperToCameraTransform:
+ _objc_msgSend$setJpcErrorCode:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLastAlgoRadarTriggerTimestamp:
+ _objc_msgSend$setLastIFAFrameTimestampCurrentExecution:
+ _objc_msgSend$setLastPearlTemp:
+ _objc_msgSend$setLogger:
+ _objc_msgSend$setMaxIRCamTemperature:
+ _objc_msgSend$setMaxIRCamTemperatureCurrentExecution:
+ _objc_msgSend$setMinIRCamTemperature:
+ _objc_msgSend$setMinIRCamTemperatureCurrentExecution:
+ _objc_msgSend$setMotionBetweenFramesRotationX:
+ _objc_msgSend$setMotionBetweenFramesRotationY:
+ _objc_msgSend$setMotionBetweenFramesRotationZ:
+ _objc_msgSend$setMotionBetweenFramesTranslationX:
+ _objc_msgSend$setMotionBetweenFramesTranslationY:
+ _objc_msgSend$setMotionBetweenFramesTranslationZ:
+ _objc_msgSend$setNewEfl:
+ _objc_msgSend$setNewPPX:
+ _objc_msgSend$setNewPPY:
+ _objc_msgSend$setNewRotX:
+ _objc_msgSend$setNewRotY:
+ _objc_msgSend$setNewRotZ:
+ _objc_msgSend$setNumJasperSpotsFlaggedAsGlare:
+ _objc_msgSend$setNumJasperSpotsFlaggedAsReflectiveSurface:
+ _objc_msgSend$setNumOfAggregatedFrames:
+ _objc_msgSend$setNumOfIFAFramesCurrentExecution:
+ _objc_msgSend$setNumOfUniqueTOFSpots:
+ _objc_msgSend$setNumPearlJasperCorrespondencesPostLocalDepthVarFilter:
+ _objc_msgSend$setNumPearlJasperCorrespondencesPostPJDepthDiffFilter:
+ _objc_msgSend$setNumPearlJasperCorrespondencesPostPJWorkDistOverlapFilter:
+ _objc_msgSend$setNumPearlJasperCorrespondencesPreIFA:
+ _objc_msgSend$setNumPearlOnlyCorrespondencesPostSpatialCoverageFilter:
+ _objc_msgSend$setNumPearlOnlyCorrespondencesPreIFA:
+ _objc_msgSend$setPceCalib:
+ _objc_msgSend$setPearlCalibSetSize:
+ _objc_msgSend$setPearlJapserCalibSetSize:
+ _objc_msgSend$setPearlProjectedPixelCount:
+ _objc_msgSend$setPearlProjectedPixelPercentage:
+ _objc_msgSend$setPearlTemperature:
+ _objc_msgSend$setPearlToLastJasperBankRotation:
+ _objc_msgSend$setPearlToLastJasperBankRotationX:
+ _objc_msgSend$setPearlToLastJasperBankRotationY:
+ _objc_msgSend$setPearlToLastJasperBankRotationZ:
+ _objc_msgSend$setPearlToLastJasperBankTranslation:
+ _objc_msgSend$setPearlToLastJasperBankTranslationX:
+ _objc_msgSend$setPearlToLastJasperBankTranslationY:
+ _objc_msgSend$setPearlToLastJasperBankTranslationZ:
+ _objc_msgSend$setPipelineParameters:
+ _objc_msgSend$setPointCloudFilterParameters:
+ _objc_msgSend$setPose:
+ _objc_msgSend$setPrevEfl:
+ _objc_msgSend$setPrevPPX:
+ _objc_msgSend$setPrevPPY:
+ _objc_msgSend$setPrevPose:
+ _objc_msgSend$setPrevRotX:
+ _objc_msgSend$setPrevRotY:
+ _objc_msgSend$setPrevRotZ:
+ _objc_msgSend$setPrincipalPointX:
+ _objc_msgSend$setPrincipalPointY:
+ _objc_msgSend$setReprojectionErrorAfter:
+ _objc_msgSend$setReprojectionErrorBefore:
+ _objc_msgSend$setRotArray:
+ _objc_msgSend$setScore:
+ _objc_msgSend$setSecondaryColor:
+ _objc_msgSend$setStepsToExecute:
+ _objc_msgSend$setTelemetryData:
+ _objc_msgSend$setTemperature:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setTransArray:
+ _objc_msgSend$shouldExecuteForTimestamp:poseMillimeters:
+ _objc_msgSend$shouldExecuteWithInterSessionDataRun:
+ _objc_msgSend$skew:
+ _objc_msgSend$skipISF
+ _objc_msgSend$stepsToExecute
+ _objc_msgSend$stride
+ _objc_msgSend$stringWithContentsOfFile:encoding:error:
+ _objc_msgSend$telemetryData
+ _objc_msgSend$temperature
+ _objc_msgSend$textureForSize:pixelFormat:mipmapped:metalDevice:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$transArray
+ _objc_msgSend$uncertainty
+ _objc_msgSend$undistort:distortedPixels:outUndistorted:
+ _objc_msgSend$undistortColorImage:undistortedImage:
+ _objc_msgSend$undistortedRadii
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateColorROI:
+ _objc_msgSend$updatePixelBufferAllocationForImageDescriptor:pixelBuffer:
+ _objc_msgSend$updateTimestampWithOverride:
+ _objc_msgSend$updateWarper:source:target:
+ _objc_msgSend$updateWithSource:target:
+ _objc_msgSend$uuid
+ _objc_msgSend$validDepthRect
+ _objc_msgSend$waitUntilSignaledValue:timeoutMS:
+ _objc_msgSend$warpImage:processedImage:isRef:
+ _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingOpticalFlow:
+ _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingPoseDelta:previousCalibration:currentCalibration:
+ _objc_msgSend$writeMetricDepthToJPEG:timestamp:preProcessedJasper:preProcessedPearl:preProcessedPrimaryColor:rawConfOut:rawDepthOut:
+ _objc_release_x10
+ _tanf
+ _vImageBufferFill_CbCr8
+ _vImageMapping_CreateFromImageMap_Image8U
+ _vImageMapping_Release
+ _vImageRemap_Image8U
+ _vImageRotate90_CbCr16F
- +[ADNetworkProvider providerForNetwork:requestedLayouts:espressoEngine:]
- +[ADUtils fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:defaultAlpha:confidenceUnits:]
- +[ADUtils warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:previousNormals:intoCurrentNormals:usingOpticalFlow:]
- -[ADDensifiedLiDARFocusAssistExecutor initWithEngineType:]
- -[ADDensifiedLiDARFocusAssistExecutorParameters initForPipeline:]
- -[ADEspressoJasperColorInferenceDescriptor normalsOutput]
- -[ADExecutorParameters powerMeasureMode]
- -[ADExecutorParameters setPowerMeasureMode:]
- -[ADExecutorParameters setStepsToSkip:]
- -[ADExecutorParameters stepsToSkip]
- -[ADJasperColorExecutor executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:]
- -[ADJasperColorExecutor executeWithColor:pointCloud:outDepthMap:outConfMap:outNormalsMap:]
- -[ADJasperColorExecutor executeWithColor:pointCloud:outDepthMap:outConfMap:outNormalsMap:worldToCameraTransform:cameraCalibration:]
- -[ADJasperColorExecutorParameters doComputeNormals]
- -[ADJasperColorExecutorParameters doTemporalConsistency]
- -[ADJasperColorExecutorParameters setDoComputeNormals:]
- -[ADJasperColorExecutorParameters setDoTemporalConsistency:]
- -[ADJasperColorInfieldCalibrationFlow initWithExecutor:andIntersessionData:]
- -[ADJasperColorPipeline processedNormalsOutputDescriptor]
- -[ADLKTExecutor createPixelBufferForOpticalFlow]
- -[ADLKTOpticalFlow _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]
- -[ADLKTOpticalFlow _computeFeaturesWithCommandBuffer:in_tex:out_tex:]
- -[ADLKTOpticalFlow _createImagePyramidWithCommandBuffer:inOutPyramidsArray:error:]
- -[ADLKTOpticalFlow _createImagePyramidWithCommandBuffer:in_BGRATex:outPyramidsArray:error:]
- -[ADLKTOpticalFlow _doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:]
- -[ADLKTOpticalFlow _doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:scale:coeff:in_uv_tex:out_uv_tex:out_w_tex:]
- -[ADLKTOpticalFlow _downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:]
- -[ADNetworkProvider bufferNameForInputType:]
- -[ADNetworkProvider bufferNameForOutputType:]
- -[ADNetworkProvider bufferNameForType:isInput:]
- -[ADNetworkProvider descriptorForBufferOfType:isInput:pixelFormat:]
- -[ADNetworkProvider initWithNetwork:requestedLayouts:espressoEngine:]
- GCC_except_table1006
- GCC_except_table1007
- GCC_except_table1008
- GCC_except_table1016
- GCC_except_table1017
- GCC_except_table1019
- GCC_except_table1024
- GCC_except_table1025
- GCC_except_table1026
- GCC_except_table1027
- GCC_except_table1028
- GCC_except_table1030
- GCC_except_table1039
- GCC_except_table1040
- GCC_except_table1048
- GCC_except_table1049
- GCC_except_table1050
- GCC_except_table1056
- GCC_except_table1061
- GCC_except_table1062
- GCC_except_table1065
- GCC_except_table1066
- GCC_except_table1067
- GCC_except_table1076
- GCC_except_table1085
- GCC_except_table1095
- GCC_except_table1100
- GCC_except_table1105
- GCC_except_table1109
- GCC_except_table1114
- GCC_except_table1120
- GCC_except_table1121
- GCC_except_table1138
- GCC_except_table1139
- GCC_except_table1145
- GCC_except_table1146
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1149
- GCC_except_table1152
- GCC_except_table1154
- GCC_except_table1157
- GCC_except_table1158
- GCC_except_table1160
- GCC_except_table1162
- GCC_except_table1182
- GCC_except_table1183
- GCC_except_table1191
- GCC_except_table1192
- GCC_except_table1257
- GCC_except_table1258
- GCC_except_table1275
- GCC_except_table1280
- GCC_except_table1289
- GCC_except_table1300
- GCC_except_table1301
- GCC_except_table1302
- GCC_except_table1303
- GCC_except_table1305
- GCC_except_table1335
- GCC_except_table1336
- GCC_except_table1337
- GCC_except_table1342
- GCC_except_table1343
- GCC_except_table1344
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1349
- GCC_except_table1352
- GCC_except_table1354
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1359
- GCC_except_table138
- GCC_except_table1388
- GCC_except_table1391
- GCC_except_table1392
- GCC_except_table1393
- GCC_except_table1394
- GCC_except_table1395
- GCC_except_table1399
- GCC_except_table1400
- GCC_except_table1403
- GCC_except_table1405
- GCC_except_table1406
- GCC_except_table1412
- GCC_except_table1415
- GCC_except_table1421
- GCC_except_table1425
- GCC_except_table1426
- GCC_except_table1428
- GCC_except_table1432
- GCC_except_table1434
- GCC_except_table1435
- GCC_except_table1436
- GCC_except_table1437
- GCC_except_table1438
- GCC_except_table1439
- GCC_except_table1442
- GCC_except_table1445
- GCC_except_table1446
- GCC_except_table1466
- GCC_except_table1468
- GCC_except_table1469
- GCC_except_table1478
- GCC_except_table148
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1486
- GCC_except_table1487
- GCC_except_table1488
- GCC_except_table1489
- GCC_except_table1491
- GCC_except_table1492
- GCC_except_table1493
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1500
- GCC_except_table1501
- GCC_except_table1503
- GCC_except_table1504
- GCC_except_table1505
- GCC_except_table1507
- GCC_except_table1508
- GCC_except_table1510
- GCC_except_table1511
- GCC_except_table152
- GCC_except_table153
- GCC_except_table1532
- GCC_except_table1540
- GCC_except_table1544
- GCC_except_table1545
- GCC_except_table1546
- GCC_except_table1547
- GCC_except_table1548
- GCC_except_table1549
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1555
- GCC_except_table1560
- GCC_except_table1561
- GCC_except_table1562
- GCC_except_table1568
- GCC_except_table1569
- GCC_except_table1573
- GCC_except_table1579
- GCC_except_table1584
- GCC_except_table1586
- GCC_except_table160
- GCC_except_table1608
- GCC_except_table161
- GCC_except_table1611
- GCC_except_table1613
- GCC_except_table1614
- GCC_except_table1615
- GCC_except_table1616
- GCC_except_table1618
- GCC_except_table162
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table1627
- GCC_except_table1628
- GCC_except_table1629
- GCC_except_table1630
- GCC_except_table1631
- GCC_except_table1632
- GCC_except_table1633
- GCC_except_table1634
- GCC_except_table1637
- GCC_except_table1638
- GCC_except_table1643
- GCC_except_table1644
- GCC_except_table1645
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1654
- GCC_except_table1656
- GCC_except_table1657
- GCC_except_table1659
- GCC_except_table1660
- GCC_except_table1662
- GCC_except_table1665
- GCC_except_table1666
- GCC_except_table1668
- GCC_except_table1674
- GCC_except_table1675
- GCC_except_table1676
- GCC_except_table1677
- GCC_except_table1678
- GCC_except_table1679
- GCC_except_table1680
- GCC_except_table1681
- GCC_except_table1682
- GCC_except_table1683
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table169
- GCC_except_table1695
- GCC_except_table1696
- GCC_except_table1697
- GCC_except_table1698
- GCC_except_table170
- GCC_except_table1704
- GCC_except_table1707
- GCC_except_table1708
- GCC_except_table1709
- GCC_except_table1710
- GCC_except_table1712
- GCC_except_table1714
- GCC_except_table1722
- GCC_except_table1724
- GCC_except_table1725
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1728
- GCC_except_table1730
- GCC_except_table1732
- GCC_except_table1734
- GCC_except_table1735
- GCC_except_table1736
- GCC_except_table1748
- GCC_except_table1753
- GCC_except_table1754
- GCC_except_table1755
- GCC_except_table1756
- GCC_except_table1757
- GCC_except_table1759
- GCC_except_table1774
- GCC_except_table1796
- GCC_except_table1797
- GCC_except_table1807
- GCC_except_table1808
- GCC_except_table1809
- GCC_except_table1811
- GCC_except_table1812
- GCC_except_table1816
- GCC_except_table1817
- GCC_except_table1818
- GCC_except_table1825
- GCC_except_table1834
- GCC_except_table1835
- GCC_except_table1836
- GCC_except_table1837
- GCC_except_table1841
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1849
- GCC_except_table1851
- GCC_except_table1866
- GCC_except_table187
- GCC_except_table1876
- GCC_except_table1877
- GCC_except_table1878
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1890
- GCC_except_table1892
- GCC_except_table1897
- GCC_except_table1898
- GCC_except_table1902
- GCC_except_table1903
- GCC_except_table1904
- GCC_except_table1908
- GCC_except_table1917
- GCC_except_table1924
- GCC_except_table1927
- GCC_except_table1928
- GCC_except_table1936
- GCC_except_table1939
- GCC_except_table1948
- GCC_except_table1949
- GCC_except_table1950
- GCC_except_table1954
- GCC_except_table1972
- GCC_except_table1975
- GCC_except_table1978
- GCC_except_table198
- GCC_except_table1980
- GCC_except_table1982
- GCC_except_table1991
- GCC_except_table1992
- GCC_except_table1993
- GCC_except_table1994
- GCC_except_table2007
- GCC_except_table2015
- GCC_except_table2016
- GCC_except_table202
- GCC_except_table204
- GCC_except_table205
- GCC_except_table207
- GCC_except_table208
- GCC_except_table209
- GCC_except_table210
- GCC_except_table211
- GCC_except_table212
- GCC_except_table214
- GCC_except_table215
- GCC_except_table216
- GCC_except_table217
- GCC_except_table219
- GCC_except_table229
- GCC_except_table259
- GCC_except_table266
- GCC_except_table269
- GCC_except_table270
- GCC_except_table281
- GCC_except_table317
- GCC_except_table318
- GCC_except_table320
- GCC_except_table322
- GCC_except_table325
- GCC_except_table332
- GCC_except_table333
- GCC_except_table334
- GCC_except_table349
- GCC_except_table351
- GCC_except_table352
- GCC_except_table355
- GCC_except_table356
- GCC_except_table358
- GCC_except_table359
- GCC_except_table383
- GCC_except_table387
- GCC_except_table388
- GCC_except_table389
- GCC_except_table407
- GCC_except_table408
- GCC_except_table419
- GCC_except_table423
- GCC_except_table425
- GCC_except_table438
- GCC_except_table444
- GCC_except_table448
- GCC_except_table449
- GCC_except_table452
- GCC_except_table453
- GCC_except_table454
- GCC_except_table462
- GCC_except_table471
- GCC_except_table472
- GCC_except_table473
- GCC_except_table480
- GCC_except_table483
- GCC_except_table484
- GCC_except_table485
- GCC_except_table486
- GCC_except_table487
- GCC_except_table489
- GCC_except_table490
- GCC_except_table491
- GCC_except_table541
- GCC_except_table542
- GCC_except_table561
- GCC_except_table562
- GCC_except_table578
- GCC_except_table579
- GCC_except_table583
- GCC_except_table584
- GCC_except_table585
- GCC_except_table586
- GCC_except_table587
- GCC_except_table588
- GCC_except_table589
- GCC_except_table590
- GCC_except_table591
- GCC_except_table593
- GCC_except_table594
- GCC_except_table595
- GCC_except_table598
- GCC_except_table600
- GCC_except_table602
- GCC_except_table603
- GCC_except_table604
- GCC_except_table605
- GCC_except_table606
- GCC_except_table607
- GCC_except_table608
- GCC_except_table634
- GCC_except_table635
- GCC_except_table646
- GCC_except_table647
- GCC_except_table653
- GCC_except_table654
- GCC_except_table665
- GCC_except_table674
- GCC_except_table683
- GCC_except_table690
- GCC_except_table692
- GCC_except_table693
- GCC_except_table696
- GCC_except_table698
- GCC_except_table699
- GCC_except_table71
- GCC_except_table726
- GCC_except_table729
- GCC_except_table730
- GCC_except_table744
- GCC_except_table746
- GCC_except_table747
- GCC_except_table748
- GCC_except_table749
- GCC_except_table750
- GCC_except_table751
- GCC_except_table754
- GCC_except_table757
- GCC_except_table758
- GCC_except_table759
- GCC_except_table760
- GCC_except_table761
- GCC_except_table778
- GCC_except_table779
- GCC_except_table783
- GCC_except_table793
- GCC_except_table795
- GCC_except_table796
- GCC_except_table801
- GCC_except_table802
- GCC_except_table804
- GCC_except_table81
- GCC_except_table817
- GCC_except_table82
- GCC_except_table827
- GCC_except_table829
- GCC_except_table830
- GCC_except_table831
- GCC_except_table832
- GCC_except_table835
- GCC_except_table836
- GCC_except_table840
- GCC_except_table841
- GCC_except_table845
- GCC_except_table846
- GCC_except_table848
- GCC_except_table849
- GCC_except_table851
- GCC_except_table861
- GCC_except_table874
- GCC_except_table887
- GCC_except_table888
- GCC_except_table889
- GCC_except_table912
- GCC_except_table913
- GCC_except_table919
- GCC_except_table920
- GCC_except_table977
- GCC_except_table978
- GCC_except_table979
- GCC_except_table996
- _NSURLIsDirectoryKey
- _OBJC_CLASS_$_NSPipe
- _OBJC_CLASS_$_NSTask
- _OBJC_CLASS_$_NSThread
- _OBJC_IVAR_$_ADEspressoJasperColorInferenceDescriptor._normalsOutput
- _OBJC_IVAR_$_ADExecutorParameters._powerMeasureMode
- _OBJC_IVAR_$_ADExecutorParameters._stepsToSkip
- _OBJC_IVAR_$_ADJasperColorExecutor._itmCurrProcessedFusedNormals
- _OBJC_IVAR_$_ADJasperColorExecutor._itmPostProcessedNormals
- _OBJC_IVAR_$_ADJasperColorExecutor._itmPreProcessedColor
- _OBJC_IVAR_$_ADJasperColorExecutor._itmPrevProcessedFusedNormals
- _OBJC_IVAR_$_ADJasperColorExecutor._itmUnprocessedAlpha
- _OBJC_IVAR_$_ADJasperColorExecutor._itmUnprocessedNormals
- _OBJC_IVAR_$_ADJasperColorExecutor._opticalFlowEnabled
- _OBJC_IVAR_$_ADJasperColorExecutorParameters._doComputeNormals
- _OBJC_IVAR_$_ADJasperColorExecutorParameters._doTemporalConsistency
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._lastKnownGoodSpotsCount
- _OBJC_IVAR_$_ADJasperColorInFieldCalibrationPipeline._lastKnownPointsCollectionVec
- _OBJC_IVAR_$_ADJasperColorStillsPipeline._isDisparity
- _OBJC_IVAR_$_ADNetworkProvider._inputBufferMap
- _OBJC_IVAR_$_ADNetworkProvider._outputBufferMap
- __Block_object_dispose
- __Z13waitForFolderP8NSStringd
- __Z14crc32ForFolderP8NSString
- __Z15prepareAneFlagsP12NSDictionaryP8NSStringS2_b
- __Z16verifyMachoFlagsP8NSStringP12NSDictionary
- __Z17compileE5mlBundleP8NSStringS0_bS0_S0_S0_
- __Z18bundleE5mlIfNeededP8NSStringS0_S0_b
- __ZL15INSTRUMENTS_ENDjyyyy.100
- __ZL15INSTRUMENTS_ENDjyyyy.1142
- __ZL15INSTRUMENTS_ENDjyyyy.1207
- __ZL15INSTRUMENTS_ENDjyyyy.1243
- __ZL15INSTRUMENTS_ENDjyyyy.1273
- __ZL15INSTRUMENTS_ENDjyyyy.1279
- __ZL15INSTRUMENTS_ENDjyyyy.1369
- __ZL15INSTRUMENTS_ENDjyyyy.1496
- __ZL15INSTRUMENTS_ENDjyyyy.1502
- __ZL15INSTRUMENTS_ENDjyyyy.1558
- __ZL15INSTRUMENTS_ENDjyyyy.1694
- __ZL15INSTRUMENTS_ENDjyyyy.171
- __ZL15INSTRUMENTS_ENDjyyyy.1987
- __ZL15INSTRUMENTS_ENDjyyyy.2176
- __ZL15INSTRUMENTS_ENDjyyyy.2324
- __ZL15INSTRUMENTS_ENDjyyyy.246
- __ZL15INSTRUMENTS_ENDjyyyy.2515
- __ZL15INSTRUMENTS_ENDjyyyy.252
- __ZL15INSTRUMENTS_ENDjyyyy.2874
- __ZL15INSTRUMENTS_ENDjyyyy.2930
- __ZL15INSTRUMENTS_ENDjyyyy.3128
- __ZL15INSTRUMENTS_ENDjyyyy.324
- __ZL15INSTRUMENTS_ENDjyyyy.3350
- __ZL15INSTRUMENTS_ENDjyyyy.3402
- __ZL15INSTRUMENTS_ENDjyyyy.3562
- __ZL15INSTRUMENTS_ENDjyyyy.3663
- __ZL15INSTRUMENTS_ENDjyyyy.3828
- __ZL15INSTRUMENTS_ENDjyyyy.3929
- __ZL15INSTRUMENTS_ENDjyyyy.3952
- __ZL15INSTRUMENTS_ENDjyyyy.4161
- __ZL15INSTRUMENTS_ENDjyyyy.4211
- __ZL15INSTRUMENTS_ENDjyyyy.4338
- __ZL15INSTRUMENTS_ENDjyyyy.446
- __ZL15INSTRUMENTS_ENDjyyyy.4518
- __ZL15INSTRUMENTS_ENDjyyyy.4664
- __ZL15INSTRUMENTS_ENDjyyyy.4794
- __ZL15INSTRUMENTS_ENDjyyyy.4992
- __ZL15INSTRUMENTS_ENDjyyyy.530
- __ZL15INSTRUMENTS_ENDjyyyy.5463
- __ZL15INSTRUMENTS_ENDjyyyy.5522
- __ZL15INSTRUMENTS_ENDjyyyy.5683
- __ZL15INSTRUMENTS_ENDjyyyy.601
- __ZL15INSTRUMENTS_ENDjyyyy.701
- __ZL15INSTRUMENTS_ENDjyyyy.733
- __ZL15INSTRUMENTS_ENDjyyyy.845
- __ZL15INSTRUMENTS_ENDjyyyy.94
- __ZL15INSTRUMENTS_ENDjyyyy.989
- __ZL17INSTRUMENTS_EVENTjyyyy.101
- __ZL17INSTRUMENTS_EVENTjyyyy.1143
- __ZL17INSTRUMENTS_EVENTjyyyy.1208
- __ZL17INSTRUMENTS_EVENTjyyyy.1244
- __ZL17INSTRUMENTS_EVENTjyyyy.1274
- __ZL17INSTRUMENTS_EVENTjyyyy.1280
- __ZL17INSTRUMENTS_EVENTjyyyy.1370
- __ZL17INSTRUMENTS_EVENTjyyyy.1497
- __ZL17INSTRUMENTS_EVENTjyyyy.1503
- __ZL17INSTRUMENTS_EVENTjyyyy.1559
- __ZL17INSTRUMENTS_EVENTjyyyy.1695
- __ZL17INSTRUMENTS_EVENTjyyyy.172
- __ZL17INSTRUMENTS_EVENTjyyyy.1988
- __ZL17INSTRUMENTS_EVENTjyyyy.2177
- __ZL17INSTRUMENTS_EVENTjyyyy.2325
- __ZL17INSTRUMENTS_EVENTjyyyy.247
- __ZL17INSTRUMENTS_EVENTjyyyy.2516
- __ZL17INSTRUMENTS_EVENTjyyyy.253
- __ZL17INSTRUMENTS_EVENTjyyyy.2875
- __ZL17INSTRUMENTS_EVENTjyyyy.2931
- __ZL17INSTRUMENTS_EVENTjyyyy.3129
- __ZL17INSTRUMENTS_EVENTjyyyy.325
- __ZL17INSTRUMENTS_EVENTjyyyy.3351
- __ZL17INSTRUMENTS_EVENTjyyyy.3403
- __ZL17INSTRUMENTS_EVENTjyyyy.3563
- __ZL17INSTRUMENTS_EVENTjyyyy.3664
- __ZL17INSTRUMENTS_EVENTjyyyy.3829
- __ZL17INSTRUMENTS_EVENTjyyyy.3930
- __ZL17INSTRUMENTS_EVENTjyyyy.3953
- __ZL17INSTRUMENTS_EVENTjyyyy.4162
- __ZL17INSTRUMENTS_EVENTjyyyy.4212
- __ZL17INSTRUMENTS_EVENTjyyyy.4339
- __ZL17INSTRUMENTS_EVENTjyyyy.447
- __ZL17INSTRUMENTS_EVENTjyyyy.4519
- __ZL17INSTRUMENTS_EVENTjyyyy.4665
- __ZL17INSTRUMENTS_EVENTjyyyy.4795
- __ZL17INSTRUMENTS_EVENTjyyyy.4993
- __ZL17INSTRUMENTS_EVENTjyyyy.531
- __ZL17INSTRUMENTS_EVENTjyyyy.5464
- __ZL17INSTRUMENTS_EVENTjyyyy.5523
- __ZL17INSTRUMENTS_EVENTjyyyy.5684
- __ZL17INSTRUMENTS_EVENTjyyyy.602
- __ZL17INSTRUMENTS_EVENTjyyyy.702
- __ZL17INSTRUMENTS_EVENTjyyyy.734
- __ZL17INSTRUMENTS_EVENTjyyyy.846
- __ZL17INSTRUMENTS_EVENTjyyyy.95
- __ZL17INSTRUMENTS_EVENTjyyyy.990
- __ZL17INSTRUMENTS_STARTjyyyy.102
- __ZL17INSTRUMENTS_STARTjyyyy.1144
- __ZL17INSTRUMENTS_STARTjyyyy.1209
- __ZL17INSTRUMENTS_STARTjyyyy.1245
- __ZL17INSTRUMENTS_STARTjyyyy.1275
- __ZL17INSTRUMENTS_STARTjyyyy.1281
- __ZL17INSTRUMENTS_STARTjyyyy.1371
- __ZL17INSTRUMENTS_STARTjyyyy.1498
- __ZL17INSTRUMENTS_STARTjyyyy.1504
- __ZL17INSTRUMENTS_STARTjyyyy.1560
- __ZL17INSTRUMENTS_STARTjyyyy.1696
- __ZL17INSTRUMENTS_STARTjyyyy.173
- __ZL17INSTRUMENTS_STARTjyyyy.1989
- __ZL17INSTRUMENTS_STARTjyyyy.2178
- __ZL17INSTRUMENTS_STARTjyyyy.2326
- __ZL17INSTRUMENTS_STARTjyyyy.248
- __ZL17INSTRUMENTS_STARTjyyyy.2517
- __ZL17INSTRUMENTS_STARTjyyyy.254
- __ZL17INSTRUMENTS_STARTjyyyy.2876
- __ZL17INSTRUMENTS_STARTjyyyy.2932
- __ZL17INSTRUMENTS_STARTjyyyy.3130
- __ZL17INSTRUMENTS_STARTjyyyy.326
- __ZL17INSTRUMENTS_STARTjyyyy.3352
- __ZL17INSTRUMENTS_STARTjyyyy.3404
- __ZL17INSTRUMENTS_STARTjyyyy.3564
- __ZL17INSTRUMENTS_STARTjyyyy.3665
- __ZL17INSTRUMENTS_STARTjyyyy.3830
- __ZL17INSTRUMENTS_STARTjyyyy.3931
- __ZL17INSTRUMENTS_STARTjyyyy.3954
- __ZL17INSTRUMENTS_STARTjyyyy.4163
- __ZL17INSTRUMENTS_STARTjyyyy.4213
- __ZL17INSTRUMENTS_STARTjyyyy.4340
- __ZL17INSTRUMENTS_STARTjyyyy.448
- __ZL17INSTRUMENTS_STARTjyyyy.4520
- __ZL17INSTRUMENTS_STARTjyyyy.4666
- __ZL17INSTRUMENTS_STARTjyyyy.4796
- __ZL17INSTRUMENTS_STARTjyyyy.4994
- __ZL17INSTRUMENTS_STARTjyyyy.532
- __ZL17INSTRUMENTS_STARTjyyyy.5465
- __ZL17INSTRUMENTS_STARTjyyyy.5524
- __ZL17INSTRUMENTS_STARTjyyyy.5685
- __ZL17INSTRUMENTS_STARTjyyyy.603
- __ZL17INSTRUMENTS_STARTjyyyy.703
- __ZL17INSTRUMENTS_STARTjyyyy.735
- __ZL17INSTRUMENTS_STARTjyyyy.847
- __ZL17INSTRUMENTS_STARTjyyyy.96
- __ZL17INSTRUMENTS_STARTjyyyy.991
- __ZN16DisparityToDepth20WorldPointsContainerD1Ev
- __ZN16PixelBufferUtils26wrapAsDifferentPixelFormatEP10__CVBufferjPS1_
- __ZN23PixelBufferUtilsSession29createCropScaleConvertSessionE6CGSizejS0_j6CGRect
- __ZN23PixelBufferUtilsSession35createCropScaleConvertRotateSessionE6CGSizejS0_j6CGRecti
- __ZN23PixelBufferUtilsSessionC1E6CGSizejS0_j6CGRecti33PixelBufferUtilsSessionReflection
- __ZN23PixelBufferUtilsSessionC2E6CGSizejS0_j6CGRecti33PixelBufferUtilsSessionReflection
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__16vectorI31ADDisparityToDepthFitWorldPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI7CGPointNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIDv3_fNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyNS_4pairIPhiEEEENS_22__unordered_map_hasherIyS5_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS5_SA_S8_Lb1EEENS_9allocatorIS5_EEED1Ev
- __ZNSt3__112__tuple_implINS_15__tuple_indicesIJLm0ELm1ELm2ELm3ELm4ELm5EEEEJbffNS_6vectorIfNS_9allocatorIfEEEES6_NS3_I31ADDisparityToDepthFitWorldPointNS4_IS7_EEEEEEC2B8ne190102IJLm0ELm1ELm2ELm3ELm4ELm5EEJbffS6_S6_S9_EJEJEJbiiRS6_SC_RKS9_EEENS1_IJXspT_EEEENS_13__tuple_typesIJDpT0_EEENS1_IJXspT1_EEEENSG_IJDpT2_EEEDpOT3_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__113__nth_elementB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPfEEEEvT1_S8_S8_T0_
- __ZNSt3__113unordered_mapIyNS_4pairIPhiEENS_4hashIyEENS_8equal_toIyEENS_9allocatorINS1_IKyS3_EEEEEC1ESt16initializer_listISA_E
- __ZNSt3__113unordered_setIiNS_4hashIiEENS_8equal_toIiEENS_9allocatorIiEEED1B8ne190102Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__125__throw_bad_function_callB8ne190102Ev
- __ZNSt3__15tupleIJbffNS_6vectorIfNS_9allocatorIfEEEES4_NS1_I31ADDisparityToDepthFitWorldPointNS2_IS5_EEEEEED1Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
- __ZNSt3__18functionIFNS_6vectorI7CGPointNS_9allocatorIS2_EEEERKNS1_IDv3_fNS3_IS6_EEEEEED1Ev
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ____Z14crc32ForFolderP8NSString_block_invoke
- ____Z18bundleE5mlIfNeededP8NSStringS0_S0_b_block_invoke
- ___block_descriptor_40_ea8_32r_e29_v40?0r^v8{_NSRange=QQ}16^B32lr32l8
- ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.3637
- ___block_literal_global.5066
- _crc32
- _espresso_get_version_string
- _kADDeviceConfigurationKeyJasperPerformanceEmulatedDevice
- _kADDeviceConfigurationKeyJasperPerformanceOverridePath
- _kADEspressoBufferIDAleatoricUncertainty
- _kADEspressoBufferIDAlphaMap
- _kADEspressoBufferIDAnglesVector
- _kADEspressoBufferIDAuxColor
- _kADEspressoBufferIDAuxiliaryAleatoricUncertainty
- _kADEspressoBufferIDAuxiliaryConfidence
- _kADEspressoBufferIDAuxiliaryDisparity
- _kADEspressoBufferIDAuxiliaryLogarithmicVariance
- _kADEspressoBufferIDAuxiliarySTDUncertainty
- _kADEspressoBufferIDBinaryMask
- _kADEspressoBufferIDColor
- _kADEspressoBufferIDConfidence
- _kADEspressoBufferIDDepth
- _kADEspressoBufferIDDisparity
- _kADEspressoBufferIDErrorPpx
- _kADEspressoBufferIDErrorPpy
- _kADEspressoBufferIDErrorRotationX
- _kADEspressoBufferIDErrorRotationY
- _kADEspressoBufferIDErrorRotationZ
- _kADEspressoBufferIDErrorsVector
- _kADEspressoBufferIDInputOpaqueFeatures
- _kADEspressoBufferIDJasper
- _kADEspressoBufferIDLogarithmicVariance
- _kADEspressoBufferIDNormals
- _kADEspressoBufferIDOpaqueDepthFeatures
- _kADEspressoBufferIDOpaqueFeatures
- _kADEspressoBufferIDOutputOpaqueFeatures
- _kADEspressoBufferIDPCEStereo
- _kADEspressoBufferIDPearl
- _kADEspressoBufferIDPpx
- _kADEspressoBufferIDPpy
- _kADEspressoBufferIDPrevColor
- _kADEspressoBufferIDPrevConfidence
- _kADEspressoBufferIDPrevDepth
- _kADEspressoBufferIDPrevDisparity
- _kADEspressoBufferIDRefColor
- _kADEspressoBufferIDRotationX
- _kADEspressoBufferIDRotationY
- _kADEspressoBufferIDRotationZ
- _kADEspressoBufferIDSTDUncertainty
- _kADEspressoBufferIDTemporalSmoothingCurrentFeaturesRatioMin
- _kADEspressoBufferIDTemporalSmoothingPreviousFeaturesRatioMin
- _objc_msgSend$_computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:
- _objc_msgSend$_computeFeaturesWithCommandBuffer:in_tex:out_tex:
- _objc_msgSend$_createImagePyramidWithCommandBuffer:inOutPyramidsArray:error:
- _objc_msgSend$_createImagePyramidWithCommandBuffer:in_BGRATex:outPyramidsArray:error:
- _objc_msgSend$_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:
- _objc_msgSend$_doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:scale:coeff:in_uv_tex:out_uv_tex:out_w_tex:
- _objc_msgSend$_downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:
- _objc_msgSend$alphaMapOutput
- _objc_msgSend$arguments
- _objc_msgSend$bufferNameForInputType:
- _objc_msgSend$bufferNameForOutputType:
- _objc_msgSend$bufferNameForType:isInput:
- _objc_msgSend$code
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$createPixelBufferForOpticalFlow
- _objc_msgSend$dataWithContentsOfURL:
- _objc_msgSend$date
- _objc_msgSend$descriptorForBufferOfType:isInput:pixelFormat:
- _objc_msgSend$dictionaryWithContentsOfFile:
- _objc_msgSend$doComputeNormals
- _objc_msgSend$encodeOpticalFlowSolverToCommandBuffer:currentFeaturesArray:currentDerivitiveArray:previousFeaturesArray:previousDerivitiveArray:currentPyramidsArray:outShiftMap:
- _objc_msgSend$encodePyramidFeaturesToCommandBuffer:colorTexture:outPyramidsArray:outFeaturesArray:outDerivitiveArray:
- _objc_msgSend$enumerateByteRangesUsingBlock:
- _objc_msgSend$enumeratorAtPath:
- _objc_msgSend$enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
- _objc_msgSend$executableURL
- _objc_msgSend$executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:
- _objc_msgSend$executeWithColor:pointCloud:outDepthMap:outConfMap:outNormalsMap:worldToCameraTransform:cameraCalibration:
- _objc_msgSend$fileHandleForReading
- _objc_msgSend$fileSystemRepresentation
- _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:
- _objc_msgSend$fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:defaultAlpha:confidenceUnits:
- _objc_msgSend$getResourceValue:forKey:error:
- _objc_msgSend$initWithData:encoding:
- _objc_msgSend$initWithDevice:inputSize:scales:
- _objc_msgSend$initWithEngineType:
- _objc_msgSend$initWithNetwork:requestedLayouts:espressoEngine:
- _objc_msgSend$launchAndReturnError:
- _objc_msgSend$localizedDescription
- _objc_msgSend$moveItemAtPath:toPath:error:
- _objc_msgSend$nextObject
- _objc_msgSend$numberOfExecutionSteps
- _objc_msgSend$path
- _objc_msgSend$pipe
- _objc_msgSend$postProcessWithDepth:confidence:normals:depthOutput:confidenceOutput:normalsOutput:normalsRequiredRotation:
- _objc_msgSend$powerMeasureMode
- _objc_msgSend$processedNormalsOutputDescriptor
- _objc_msgSend$providerForNetwork:requestedLayouts:espressoEngine:
- _objc_msgSend$rangeOfString:
- _objc_msgSend$rangeOfString:options:
- _objc_msgSend$readDataToEndOfFileAndReturnError:
- _objc_msgSend$setArguments:
- _objc_msgSend$setExecutableURL:
- _objc_msgSend$setStandardOutput:
- _objc_msgSend$sleepForTimeInterval:
- _objc_msgSend$stepsToSkip
- _objc_msgSend$substringToIndex:
- _objc_msgSend$terminationStatus
- _objc_msgSend$useAlphaMapForTemporalConsistency
- _objc_msgSend$waitUntilExit
- _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:previousNormals:intoCurrentNormals:usingOpticalFlow:
- _objc_msgSend$warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:previousNormals:intoCurrentNormals:usingPoseDelta:previousCalibration:currentCalibration:
- _rmdir
CStrings:
+ " "
+ " Error Code: "
+ " File: "
+ " Line: "
+ "!std::isnan(curDy)"
+ "!std::isnan(dy)"
+ "#UUID:"
+ "#UUID: %s\n"
+ "#faces count: %ld\n"
+ "#timestamp:"
+ "#timestamp: %f\n"
+ "#vertices count: %ld\n"
+ "%.3f"
+ "%@/MD_montage.jpeg"
+ "%@_height%tu_width%tu"
+ "%f"
+ "%s"
+ "%s: R = [%f, %f, %f]degrees, T = [%f, %f, %f] mm"
+ "%s:%d - ERROR - Changing pixel format without copying is not supported for formats with different pixel sizes (source=%zu, new=%zu)"
+ "%s:%d - ERROR - Cropping pixel buffer without copying is not supported for multi-planar CVPixelBufferRefs"
+ "(%@,%@]"
+ "(%@,Inf]"
+ "(%d)"
+ "(-Inf,%@]"
+ "-[ADJasperPearlInFieldCalibrationExecutor executeWithInterSessionData:result:]"
+ "-[ADJasperPearlInFieldCalibrationExecutor executeWithJasperPearlInterSessionData:result:]"
+ "-[ADJasperPearlInFieldCalibrationExecutor prepare]"
+ "-[ADJasperPearlInFieldCalibrationExecutor pushPearlDepth:pearlDx:pearlDy:pearlScore:timestamp:pose:pearlSensorCalibration:]"
+ "-[ADJasperPearlInFieldCalibrationExecutor pushPearlDepth:timestamp:pose:temperature:irSensorOperationalCalibration:]"
+ "-[ADJasperPearlInFieldCalibrationPipeline checkPrerequisitesForProcessWithPearlWithPearlInputs:]"
+ "-[ADJasperPearlInFieldCalibrationPipeline processJpcResultWithStatus:gmcjResult:glaResult:result:interSessionData:temperature:eflTempCoeff:]"
+ "-[CVPixelBufferARCWrapper initWithPearlDepth:pearlDx:pearlDy:pearlScore:]"
+ "-[pushJasperPointCloud:timestamp:pose:jasperToPearlExtrinsics] is deprecated. please use pushJasperPointCloud:timestamp:pose:jasperToPearlTransform instead"
+ ".bundle"
+ "/Gather"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/Executors/ADJasperPearlInFieldCalibrationExecutor.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/GMC_J/JPC_PORGMCJ_Block.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/IFA/JPC_PORIFABlock.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/OutputValidation/JPC_PORGMCJ_OutputValidation_Block.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/Blocks/Preprocessor/JPC_PORPreprocessorBlock.mm"
+ "/Library/Caches/com.apple.xbs/Sources/AppleDepth/AppleDepth/InFieldCalibrations/JPC/JPC.mm"
+ "/_regression_layer/Add"
+ "/_regression_layer/Relu_2"
+ "/tmp/GMC_Standalone/DebugOutputs/"
+ "/tmp/jpcConfig.plist"
+ "/var/jpcConfig.plist"
+ "/var/mobile/Library/ARKit/jpcConfig.plist"
+ "0x%0X"
+ "148.0"
+ "@\"<MTLBuffer>\""
+ "@\"<MTLSharedEventSPI>\""
+ "@\"<MTLTexture>\""
+ "@\"ADAggregatedPointCloudRefiner\""
+ "@\"ADBinocularDepthExecutor\""
+ "@\"ADBinocularDepthPipeline\""
+ "@\"ADBinocularDepthPipelineParameters\""
+ "@\"ADBinocularDepthWarperMesh\""
+ "@\"ADDensifiedLiDARFocusAssistExecutor\""
+ "@\"ADEmbeddings\""
+ "@\"ADEspressoBinocularDepthInferenceDescriptor\""
+ "@\"ADEspressoMetricDepthInferenceDescriptor\""
+ "@\"ADImageDimensions\""
+ "@\"ADJasperPearlInFieldCalibrationPipeline\""
+ "@\"ADJasperPearlInFieldCalibrationPipelineParameters\""
+ "@\"ADJasperPearlTelemetryData\""
+ "@\"ADLKTConfidenceParameters\""
+ "@\"ADMetricDepthExecutor\""
+ "@\"ADMetricDepthFrameStatistics\""
+ "@\"ADMetricDepthPipeline\""
+ "@\"ADMetricDepthPipelineParameters\""
+ "@\"ADModelBuilder\""
+ "@\"ADMonocularExecutor\""
+ "@\"ADPointCloudAggregator\""
+ "@\"ADStreamSyncMatch\""
+ "@\"ADVisualDepthBuffer\""
+ "@\"ADVisualDepthGeometry\""
+ "@\"ADVisualDepthKeyframeInput\""
+ "@\"ADVisualDepthMeshInput\""
+ "@\"ADVisualDepthMetalDescriptor\""
+ "@\"ADVisualDepthPipeline\""
+ "@\"ADVisualDepthPipelineParameters\""
+ "@\"MPSImageBilinearScale\""
+ "@\"NSMutableDictionary\"8@?0"
+ "@\"NSNumber\""
+ "@\"NSObject\""
+ "@\"NSUUID\""
+ "@104@0:8@16{CGSize=dd}24{?=Q@BiifffQI}40@96"
+ "@128@0:8@16@24@32@40{?=[4]}48@112d120"
+ "@132@0:8@16@24@32@40{?=[4]}48@112d120B128"
+ "@136@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@48@56{?=[4]}64d128"
+ "@24@0:8^{__CVBuffer=}16"
+ "@28@0:8@16f24"
+ "@32@0:8@16B24B28"
+ "@32@0:8@16d24"
+ "@32@0:8@16q24"
+ "@32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
+ "@36@0:8@16@24B32"
+ "@36@0:8@16d24B32"
+ "@40@0:8@16@24q32"
+ "@40@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32"
+ "@40@0:8^{__CVBuffer=}16^{__CVBuffer=}24d32"
+ "@44@0:8@16@24Q32B40"
+ "@44@0:8@16{CGSize=dd}24I40"
+ "@44@0:8f16@20@28[3[3d]]36"
+ "@48@0:8@16q24q32q40"
+ "@48@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40"
+ "@48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40"
+ "@48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40"
+ "@48@0:8{CGSize=dd}16I32B36@40"
+ "@56@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40d48"
+ "@64@0:8@16@24@32@40@48d56"
+ "@64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56"
+ "@68@0:8@16@24@32@40@48d56B64"
+ "@80@0:8@16{?=Q@BiifffQI}24"
+ "@88@0:8d16{?=[4]}24"
+ "@88@0:8{CGSize=dd}16I32{CGSize=dd}36{CGSize=dd}52{CGSize=dd}68B84"
+ "@96@0:8@16q24q32q40@48q56q64q72@80d88"
+ "@96@0:8@16{CGSize=dd}24{?=Q@BiifffQI}40"
+ "ADBinocularDepthExecutor"
+ "ADBinocularDepthExecutorParameters"
+ "ADBinocularDepthFlow"
+ "ADBinocularDepthOutput"
+ "ADBinocularDepthPipeline"
+ "ADBinocularDepthPipelineParameters"
+ "ADBinocularDepthWarperMesh"
+ "ADConfidenceLevelRanges: L(%.3f,%.3f), M(%.3f,%.3f), H(%.3f,%.3f)"
+ "ADDensifiedLiDARFocusAssistFlow"
+ "ADEspressoBinocularDepthInferenceDescriptor"
+ "ADEspressoMetricDepthInferenceDescriptor"
+ "ADFlowSecondaryColorConsumer"
+ "ADFusedDepthLoggerHandler"
+ "ADJasperColorInFieldCalibration jasper SDF current frame failed against history frame %d with %d/%d good spots"
+ "ADJasperColorInFieldCalibration jasper SDF current frame pass against history frame %d with %d/%d good spots"
+ "ADJasperColorInFieldCalibration jasper controller fail for %d out of %d history frames"
+ "ADJasperColorInFieldCalibration jasper controller pass %d out of %d history frames"
+ "ADJasperPearlInFieldCalibration GMCJ: BA iternumber1: %d,\titerNumber2: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: BA status: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: Bad configuration in GMC_ExtractTestSamples\n"
+ "ADJasperPearlInFieldCalibration GMCJ: EPD thresh: %lf, inlier rate: %lf, tested percentile: %lf, result: %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: Fail in RANSAC: cannot find good model.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: GMC_ToleranceTest, Relative angles: (%lf, %lf, %lf), tolerances: (%lf, %lf, %lf)\n"
+ "ADJasperPearlInFieldCalibration GMCJ: GMC_ToleranceTest, angles: (%lf, %lf, %lf), tolerances: (%lf, %lf, %lf)\n"
+ "ADJasperPearlInFieldCalibration GMCJ: Num of points: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: OUTGMC angles: %lf\t%lf\t%lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: OutGMC EFL: %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: OutGMC R:\n%lf\t%lf\t%lf\n%lf\t%lf\t%lf\n%lf\t%lf\t%lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: PDM After: perc50:%lf, perc95:%lf, perc997:%lf, mean: %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: PDM Before: perc50:%lf, perc95:%lf, perc997:%lf, mean: %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: PPX diff from factory = %f um\n"
+ "ADJasperPearlInFieldCalibration GMCJ: PPY diff from factory = %f um\n"
+ "ADJasperPearlInFieldCalibration GMCJ: Required points: %d, available inliers: %d. Only these will be used in BA.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: Required points: %d, available points: %d. Only these will be used.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: WARNING: GMCJ does not work with params.consts.testSetSize > 0. Results unpredictable."
+ "ADJasperPearlInFieldCalibration GMCJ: WARNING: test set size is 0. PDM is not calculated.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: WARNING: test set size is 0. Skipping ambiguity test.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: initRotationZeroForBA is true. Initializing BA with R=Id.\n"
+ "ADJasperPearlInFieldCalibration GMCJ: isFinalAngleToleranceTestPass: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: isFinalEFLToleranceTestPass: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: nInliers after 3D constraints: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: nInliers: %d\n"
+ "ADJasperPearlInFieldCalibration GMCJ: outStats->isToleranceTestPass = %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: outStats->tests.isAmbiguityTestPass = %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: outStats->tests.isEnoughInPoints = %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: outStats->tests.isEnoughNinliers = %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: outStats->tests.isSingularityTestPass = %lf\n"
+ "ADJasperPearlInFieldCalibration GMCJ: singularityMeasure: %lf\n"
+ "ADJasperPearlInFieldCalibrationExecutor"
+ "ADJasperPearlInFieldCalibrationExecutor.mm"
+ "ADJasperPearlInFieldCalibrationExecutorParameters"
+ "ADJasperPearlInFieldCalibrationInterSessionData"
+ "ADJasperPearlInFieldCalibrationJasperInput"
+ "ADJasperPearlInFieldCalibrationPearlInput"
+ "ADJasperPearlInFieldCalibrationPipeline"
+ "ADJasperPearlInFieldCalibrationPipeline.mm"
+ "ADJasperPearlInFieldCalibrationPipelineParameters"
+ "ADJasperPearlInFieldCalibrationResult"
+ "ADJasperPearlInFieldCalibrationTelemetry"
+ "ADJasperPearlInField_IFA_Block: Could not apply aggregators"
+ "ADJasperPearlInField_IFA_Block: Could not apply filters"
+ "ADJasperPearlInField_IFA_Block: could not init"
+ "ADJasperPearlInField_IFA_Block: empty calibSet (validationSet.pearlCorrespondences.size = %zu, calibSet.pearlJasperCorrespondences.size = %zu, , validationSet.pearlJasperCorrespondences.size = %zu)"
+ "ADJasperPearlInField_IFA_Block: frame erased"
+ "ADJasperPearlInField_IFA_Block: invalid params"
+ "ADJasperPearlInField_IFA_DB: no AGG_POINTS in db"
+ "ADJasperPearlInField_IFA_DB: no PearlTemp in db"
+ "ADJasperPearlInField_IFA_DB: no rotation in db"
+ "ADJasperPearlInField_IFA_DB: no translation in db"
+ "ADJasperPearlInField_IFA_DataFrame: initPearlPts returned error"
+ "ADJasperPearlInField_IFA_DataFrame: inputData is NULL"
+ "ADJasperPearlInField_IFA_DataFrame: no jasper spots"
+ "ADJasperPearlInField_IFA_DataFrame: no pearl pts"
+ "ADJasperPearlInField_IFA_DataFrame: wrong image data type"
+ "ADJasperPearlInfieldCalibrationTelemetryUtils.mm"
+ "ADJasperPearlTelemetryData"
+ "ADJasperPearlTriggeringTelemetryData"
+ "ADLKTConfidenceParameters"
+ "ADLKTExecutorParameters"
+ "ADLKTFlow"
+ "ADMetricDepthExecutor"
+ "ADMetricDepthExecutorParameters"
+ "ADMetricDepthFlow"
+ "ADMetricDepthFrameStatistics"
+ "ADMetricDepthPipeline"
+ "ADMetricDepthPipelineParameters"
+ "ADMonocularFlow"
+ "ADPearlColorInFieldCalibration: Rotate depth: resolutions different (%lux%lu, %lux%lu)"
+ "ADVisualDepthBuffer"
+ "ADVisualDepthExecutor"
+ "ADVisualDepthExecutorParameters"
+ "ADVisualDepthGeometry"
+ "ADVisualDepthKeyframeInput"
+ "ADVisualDepthMeshChunk"
+ "ADVisualDepthMeshInput"
+ "ADVisualDepthMetalDescriptor"
+ "ADVisualDepthOutput"
+ "ADVisualDepthPipeline"
+ "ADVisualDepthPipelineParameters"
+ "AggregatedDataWrapper"
+ "AttachmentBuffers"
+ "B176@0:8@16@24{?=[4]}32@96{?=[4]}104^{JpcInputData={PearlInputs=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}{?=[4]}{?=[4]}Q}{JasperInputs=@{?=[4]}}{CalibrationInputs={PearlCalibrations={PearlPCEConfig=fffff{PearlInvalidValues=CS}}{IRSensorCalibrations=@[2d]}{IRSensorCalibrations=@[2d]}{IRProjectorCalibrations={?=[4]}}{IRProjectorCalibrations={?=[4]}}{PearlReferenceWallCalibrations=d}}{JasperCalibrations={?=[4]}}}{DeviceStateInputs=f}}168"
+ "B24@0:8^q16"
+ "B40@0:8^{maps_uv=^f^f^{vImageMapping}}16@24@32"
+ "B48@0:8@1624@32^@40"
+ "B56@0:8@16@2432@40^@48"
+ "B88@0:8d16{?=[4]}24"
+ "BD PreProcessed Auxiliary Color"
+ "BD PreProcessed Reference Color"
+ "BD Unprocessed Auxiliary Confidence"
+ "BD Unprocessed Auxiliary Disparity"
+ "BD Unprocessed Auxiliary Segmentation"
+ "BinocularDepth rectified images saturation rate ref: %f, aux: %f"
+ "Buckets"
+ "CVPixelBufferARCWrapper"
+ "CVPixelBufferGetBytesPerRow(m_pixelBuffer) % sizeof(PixelDatatype) == 0"
+ "CVPixelBufferHelper"
+ "Can either work with both aux and ref calib or none. Don't know how to handle only one"
+ "Cannot create crop rectangle"
+ "Cannot create crop rectangle error: %ld"
+ "Color dimensions expected match target buffer, actually it is (%zux%zu) vs expected (%zux%zu)"
+ "ConcatCols"
+ "Could not find default path for model \"%{public}@\""
+ "Crop dimensions expected to be x8 than target buffer, actually it is (%zux%zu) vs expected (%zux%zu)"
+ "CurrentTriggerEndReasonIsConvergence"
+ "CurrentTriggerEndReasonIsJasperMisalignmentIncreased"
+ "CurrentTriggerEndReasonIsMaxFrameCount"
+ "CurrentTriggerNumberOfFrames"
+ "D8"
+ "Deprecated, the infrastructure is kept for a future potential comeback."
+ "Error while projecting jasper points"
+ "Failed to create projected pearl, will not emulate Peridot"
+ "Failed to receive completion event in %d ms"
+ "GMC Fail: Ambiguity"
+ "GMC Fail: Bundle adjustment did not converge"
+ "GMC Fail: Face Coverage"
+ "GMC Fail: Final EFL out of tolerance"
+ "GMC Fail: Final Rotation out of tolerance"
+ "GMC Fail: Inliers Spatial Coverage"
+ "GMC Fail: Not Enough Inliers Phase 1"
+ "GMC Fail: Not Enough Inliers Phase 2"
+ "GMC Fail: Not Enough Points"
+ "GMC Fail: RANSAC"
+ "GMC Fail: Reprojection error median increased after BA"
+ "GMC Fail: Reprojection error median too large"
+ "GMC Fail: Rotation out of tolerance"
+ "GMC Fail: Spatial Coverage"
+ "GMC Pass"
+ "GMCJErrorCode"
+ "GMCJFailedException"
+ "GMCJOutputValidationErrorCode"
+ "GMCJOutputValidationMetricIncreasedException"
+ "GMCJOutputValidationNotPassedException"
+ "GMCJ_AMBIGUITY_INLIER_MARGIN"
+ "GMCJ_AMBIGUITY_THRES"
+ "GMCJ_BA_CALL_TWICE"
+ "GMCJ_BA_COST_FUNC_STOP_TOL"
+ "GMCJ_BA_INITIAL_RADIUS"
+ "GMCJ_BA_MAX_ITR"
+ "GMCJ_BA_MAX_STALL_COUNT"
+ "GMCJ_BA_STEP_SIZE_EFL_STOP_TOL"
+ "GMCJ_BA_STEP_SIZE_ROT_STOP_TOL"
+ "GMCJ_BA_STEP_SIZE_STOP_TOL"
+ "GMCJ_CORR_NUM_THRES"
+ "GMCJ_COVERAGE_RATE_THRES"
+ "GMCJ_FACE_CORR_NUM_THRES"
+ "GMCJ_FACE_COVERAGE_RATE_THRES"
+ "GMCJ_INLIERS_NUM_THRES"
+ "GMCJ_IS_REFINE_BA"
+ "GMCJ_IS_REF_CONFIG"
+ "GMCJ_IS_UNDISTORT_CORRS"
+ "GMCJ_MAX_3D_CONSTRAINT_ITERS"
+ "GMCJ_MAX_Z"
+ "GMCJ_MIN_Z"
+ "GMCJ_NUM_RANSAC_CALLS"
+ "GMCJ_OVERRIDE_R_EST"
+ "GMCJ_PDM_MEDIAN_THRES"
+ "GMCJ_PPX_TOLERANCE"
+ "GMCJ_PPY_TOLERANCE"
+ "GMCJ_RANSAC_T_VAL"
+ "GMCJ_ROTATION_TOLERANCES_0"
+ "GMCJ_ROTATION_TOLERANCES_1"
+ "GMCJ_ROTATION_TOLERANCES_2"
+ "GMCJ_SCALE_TOLERANCE"
+ "GMCJ_SHOULD_FIND_EFL"
+ "GMCJ_SHOULD_FIND_PPX"
+ "GMCJ_SHOULD_FIND_PPY"
+ "GMCJ_SHOULD_FIND_T"
+ "GMCJ_SHOULD_INCLUDE_JASPER_RESIDUAL_FUNCTION"
+ "GMCJ_SINGULARITY_THRES"
+ "GMCJ_TEST_SET_SIZE"
+ "GMCJ_VALIDATION_MEDIAN_JASPER_MISALIGNMENT_THRES"
+ "GMC_BundleAdjustment.mm"
+ "GMC_Controller"
+ "GMC_Controller.mm"
+ "GMC_ExtractTestSamples"
+ "GMC_ExtractTestSamples.mm"
+ "GMC_Validation returned GMC_FAIL_JASPER_MISALIGNMENT error \n"
+ "GMC_Validation returned GMC_FAIL_JASPER_MISALIGNMENT_INCREASED error \n"
+ "Generating JPCConfig configuration file to %{public}s has failed."
+ "Generating JPCConfig configuration file to %{public}s."
+ "GeomUtils.hpp"
+ "GetMatrixHeight() > GetMatrixWidth()"
+ "GetNumOfPoints() == rhs.GetNumOfPoints()"
+ "IFAAggregator_VAL_SET_PERCENTAGE"
+ "IFADepthCoverageCriteria: No data to pull."
+ "IFADepthCoverageCriteria: ifaDB is NULL"
+ "IFADepthCoverageCriteria: no correspodences in aggData"
+ "IFAFailedException"
+ "IFAJConfidenceFilter: Filtered jasper spots: %d\n"
+ "IFAJConfidenceFilter: no valid jasper spots as input"
+ "IFAJDepthRangeFilter: Filtered jasper spots: %d\n"
+ "IFAJPtsIDCoverageCriteria: No data to pull."
+ "IFAJPtsIDCoverageCriteria: bad jasper spot id"
+ "IFAJPtsIDCoverageCriteria: ifaDB is NULL"
+ "IFAJPtsIDCoverageCriteria: no pearlJasper correspodences in aggData"
+ "IFAJPtsIDCoverageCriteria_IsEnabled"
+ "IFAJPtsIDCoverageCriteria_MIN_UNIQUE_JASPER_SPOT_IDS"
+ "IFANotReadyException"
+ "IFAPJDepthDiffFilter: Chosen threshold: %f\n"
+ "IFAPJDepthDiffFilter: Filtered jasper spots: %d\n"
+ "IFAPJDepthDiffFilter: no spots"
+ "IFAPJDepthDiffFilter: no valid jasper spots as input"
+ "IFAPJDepthDiffFilter_DEPTH_DIFF_THRESHOLD"
+ "IFAPJDepthDiffFilter_IsEnabled"
+ "IFAPJWorkDistOverlapFilter: Filtered jasper spots: %d\n"
+ "IFAPJWorkDistOverlapFilter: no spots"
+ "IFAPJWorkDistOverlapFilter: no valid jasper spots as input"
+ "IFAPJWorkDistOverlapFilter_IsEnabled"
+ "IFAPJWorkDistOverlapFilter_WORK_DIST_MAX_DEPTH"
+ "IFAPJWorkDistOverlapFilter_WORK_DIST_MIN_DEPTH"
+ "IFAPLocalDepthVarFilter: Filtered pearl spots: %d\n"
+ "IFAPLocalDepthVarFilter: no valid pearl spots as input"
+ "IFAPLocalDepthVarFilter: pearlDepthBuffer is NULL"
+ "IFAPLocalDepthVarFilter: pearlDepthBuffer wrong type"
+ "IFAPLocalDepthVarFilter_IsEnabled"
+ "IFAPLocalDepthVarFilter_PEARL_MIN_DEPTH"
+ "IFAPLocalDepthVarFilter_SIGMA_THRESHOLD"
+ "IFAPLocalDepthVarFilter_WINDOW_OCCLUSION_EXTENSION"
+ "IFAPLocalDepthVarFilter_WINDOW_WH"
+ "IFAPRGScoreFilter: Filtered pearl spots: %d\n"
+ "IFAPRGScoreFilter: no valid pearl spots as input"
+ "IFAPearlFovCoverageCriteria: No data to pull due to aggPoints.pearlCorrespondences.size() < m_minPtsPerBin."
+ "IFAPearlFovCoverageCriteria: No data to pull due to spotBinsVec[binIndex] < m_minPtsPerBin."
+ "IFAPearlFovCoverageCriteria: No data to pull."
+ "IFAPearlFovCoverageCriteria: ifaDB is NULL"
+ "IFAPearlFovCoverageCriteria: no pearl correspodences in aggPoints"
+ "IFAPearlFovCoverageCriteria_IsEnabled"
+ "IFAPearlFovCoverageCriteria_PEARL_FOV_COVERAGE_MX_PTS_PER_BIN"
+ "IFAPearlFovCoverageCriteria_PEARL_FOV_COVERAGE_NBIN_X"
+ "IFAPearlFovCoverageCriteria_PEARL_FOV_COVERAGE_NBIN_Y"
+ "IFAPoseDiffFilter eraseAll %d\n"
+ "IFAPoseDiffFilter no pose info in dict\n"
+ "IFAPoseDiffFilter no temperature info in dict\n"
+ "IFASimpleAggregator: dataFrame is NULL"
+ "IFASimpleAggregator: dataFrame is erased"
+ "IFASimpleAggregator: ifaDB is NULL"
+ "IFASimpleAggregator: pearlJasperSpotsAdded added: %d\n"
+ "IFASimpleAggregator: pearlSpotsAdded added: %d\n"
+ "IFASpatialCoverageFilter: Filtered pearl spots: %d\n"
+ "IFASpatialCoverageFilter: no valid pearl spots as input"
+ "IFASpatialCoverageFilter_IsEnabled"
+ "IFASpatialCoverageFilter_MX_PTS_PER_BIN"
+ "IFASpatialCoverageFilter_NBIN_X"
+ "IFASpatialCoverageFilter_NBIN_Y"
+ "IFAThermalTransientFilter eraseAll %d\n"
+ "IFA_DepthDiffThresholdAboveMedian"
+ "IFA_FilterRunner: Error when applying filters"
+ "IFA_FilterRunner: dataFrame or ifaDB is NULL"
+ "IFA_FilterRunner: empty filters vector"
+ "IFA_NumSpotsAdded_JasperPearl"
+ "IFA_NumSpotsAdded_Pearl"
+ "IFA_NumSpotsFiltered_DepthDiff"
+ "IFA_NumSpotsFiltered_LocalDepthVar"
+ "IFA_NumSpotsFiltered_SpatialCoverage"
+ "IFA_NumSpotsFiltered_WorkDistOverlap"
+ "IRCamFOVCoveragePercent"
+ "IRCamFOVCoveragePercentBucket"
+ "IRCamIRProjRotXChangeFromPrevCalib"
+ "IRCamIRProjRotXChangeFromPrevCalib_GMCJ"
+ "IRCamIRProjRotXChangeFromT0"
+ "IRCamIRProjRotXChangeFromT0_GMCJ"
+ "IRCamIRProjRotYChangeFromPrevCalib"
+ "IRCamIRProjRotYChangeFromPrevCalib_GMCJ"
+ "IRCamIRProjRotYChangeFromT0"
+ "IRCamIRProjRotYChangeFromT0_GMCJ"
+ "IRCamIRProjRotZChangeFromPrevCalib"
+ "IRCamIRProjRotZChangeFromPrevCalib_GMCJ"
+ "IRCamIRProjRotZChangeFromT0"
+ "IRCamIRProjRotZChangeFromT0_GMCJ"
+ "IRCamPPXChangeMicronFromPrevCalib"
+ "IRCamPPXChangeMicronFromPrevCalib_GMCJ"
+ "IRCamPPXChangeMicronFromT0"
+ "IRCamPPXChangeMicronFromT0_GMCJ"
+ "IRCamPPYChangeMicronFromPrevCalib"
+ "IRCamPPYChangeMicronFromPrevCalib_GMCJ"
+ "IRCamPPYChangeMicronFromT0"
+ "IRCamPPYChangeMicronFromT0_GMCJ"
+ "IRCamScaleChangePercentFromPrevCalib"
+ "IRCamScaleChangePercentFromPrevCalib_GMCJ"
+ "IRCamScaleChangePercentFromT0"
+ "IRCamScaleChangePercentFromT0_GMCJ"
+ "IRSensorOpCalibration"
+ "IRSensorPreviousPose"
+ "ISF_CAPACITY"
+ "ISF_IS_STEP_DETECTION_ACTIVE"
+ "ISF_MAX_WEIGHT"
+ "ISF_MIN_ENTRIES_FOR_RESULT"
+ "ISF_MIN_STEP_INDEX"
+ "ISF_MIN_STEP_SIZE"
+ "ISF_MIN_WEIGHT"
+ "ISF_OUTLIER_NUM"
+ "ISF_OUTLIER_WEIGHT"
+ "ISF_STEP_DETECTION_THRESHOLD"
+ "Image undistortion failed with error code : %ld"
+ "Image undistortion mapping creation failed with error code : %ld"
+ "IntervalBetweenIFAFrames"
+ "JPC"
+ "JPC Configuration for key %@: Chosen Value = %@, POR/Defaults Write = %@, ConfigFile = %@"
+ "JPC PreprocessorFilterBlock: Current JPC frame is to be discarded."
+ "JPC PreprocessorFilterBlock: Jasper spots on reflective surfaces: %d."
+ "JPC PreprocessorFilterBlock: Jasper spots with glare: %d."
+ "JPC PreprocessorFilterBlock: Min translation, rotation: (%f, %f)."
+ "JPC PreprocessorFilterBlock: Pearl-Jasper frame translation: (%f, %f, %f), rotation: (%f, %f, %f)."
+ "JPCConfig: Initializing NSURL from config file filepath %{public}s has failed."
+ "JPCErrorCode"
+ "JPCException, Exception Name: "
+ "JPC_CVPixelBufferHelper.hpp"
+ "JPC_MathUtils.hpp"
+ "JPC_PORPreprocessorBlock.mm"
+ "JPC_PearlUtils.mm"
+ "JacobianMatrix.mm"
+ "Jasper Bank %d VIO"
+ "Jasper Misalignment After: median:%lf, max:%lf\n"
+ "Jasper Misalignment Before: median:%lf, max:%lf\n"
+ "Jasper Pearl In-Field calibration pipeline Telemetry event %@ fired"
+ "Jasper Pearl In-Field calibration pipeline Telemetry event %{public}@ failed to fire"
+ "Jasper Pearl In-Field calibration pipeline Triggering Telemetry event %@ fired"
+ "Jasper Pearl In-Field calibration pipeline Triggering Telemetry event %{public}@ failed to fire"
+ "Jasper Pearl In-Field calibration pipeline skipping Triggering Telemetry"
+ "Jasper and Pearl buffers have a non-supported pixel format (%s)!"
+ "JasperMisalignmentAfterGMCJ"
+ "JasperMisalignmentBeforeGMCJ"
+ "JasperPearlInFieldCalibration: ADJasperPearlInFieldCalibrationInterSessionData: processJpcResult."
+ "JasperPearlInFieldCalibration: ADJasperPearlInFieldCalibrationInterSessionData: processJpcResult: ISF initialized from PCE calib"
+ "JasperPearlInFieldCalibration: ADJasperPearlInFieldCalibrationInterSessionData: processJpcResult: ISF initialized from dictionary"
+ "JasperPearlInFieldCalibration: ADJasperPearlInFieldCalibrationInterSessionData: processJpcResult: ISF updated"
+ "JasperPearlInFieldCalibration: Building JpcInputData has failed."
+ "JasperPearlInFieldCalibration: CVPixelBufferARCWrapper: PixelBuffer Released 0x%llX"
+ "JasperPearlInFieldCalibration: CVPixelBufferARCWrapper: PixelBuffer Retained 0x%llX"
+ "JasperPearlInFieldCalibration: Deprecated function was called: %s : %s"
+ "JasperPearlInFieldCalibration: End JPC, error code: %d"
+ "JasperPearlInFieldCalibration: Executor: ADStreamSync init has failed."
+ "JasperPearlInFieldCalibration: Executor: JPC start with timestamp = %f, temperature = %f"
+ "JasperPearlInFieldCalibration: Executor: Must call prepare()."
+ "JasperPearlInFieldCalibration: Executor: No matched data from StreamSync."
+ "JasperPearlInFieldCalibration: Executor: PCECalib was set."
+ "JasperPearlInFieldCalibration: Executor: Pipeline's init has failed."
+ "JasperPearlInFieldCalibration: Executor: Prepare."
+ "JasperPearlInFieldCalibration: Executor: executeWithInterSessionData - End."
+ "JasperPearlInFieldCalibration: Executor: executeWithInterSessionData result: efl = %f principal point = [%f, %f]"
+ "JasperPearlInFieldCalibration: Executor: executeWithInterSessionData result: efl coeff = [%f, %f]"
+ "JasperPearlInFieldCalibration: Executor: executeWithInterSessionData result: rotation = [%f, %f, %f]"
+ "JasperPearlInFieldCalibration: Executor: executeWithInterSessionData."
+ "JasperPearlInFieldCalibration: Executor: init."
+ "JasperPearlInFieldCalibration: Executor: pushJasperPointCloud."
+ "JasperPearlInFieldCalibration: Executor: pushPearlDepth."
+ "JasperPearlInFieldCalibration: Incorrect PCECalib version."
+ "JasperPearlInFieldCalibration: Invalid pipeline run mode."
+ "JasperPearlInFieldCalibration: JPC Status: %d"
+ "JasperPearlInFieldCalibration: JPCException has been caught and handled gracefully: %s."
+ "JasperPearlInFieldCalibration: New ISF entry JPC, Data: EflCoeff0 = %f, PPx = %lf, PPy = %lf, RotationAngles[0] = %lf, RotationAngles[1] = %lf, RotationAngles[2] = %lf"
+ "JasperPearlInFieldCalibration: New ISF entry JPC, Temperature: %f"
+ "JasperPearlInFieldCalibration: No PCECalib was set."
+ "JasperPearlInFieldCalibration: No Pearl depth image was set."
+ "JasperPearlInFieldCalibration: Pipeline init."
+ "JasperPearlInFieldCalibration: Start JPC, Temperature: %f"
+ "JasperPearlInFieldCalibration: kJPC_EflOnlyEstimation mode."
+ "JasperPearlInFieldCalibration: kJPC_FullEstimation mode."
+ "JasperPearlInFieldCalibration: kJPC_Idle mode."
+ "JasperPearlInFieldCalibration: pushed jasper point cloud for ts:%f into streamSync"
+ "JasperPearlInFieldCalibration: pushed pearl frame for ts:%f into streamSync"
+ "JasperPearlInFieldCalibration: std::exeption has been caught and handled gracefully: %s"
+ "JasperToPearlOpCalib"
+ "JpcInputData_JasperPC"
+ "JpcInputData_JasperPC_CSV"
+ "JpcInputData_RGDEPTH"
+ "JpcInputData_RGDX"
+ "JpcInputData_RGDY"
+ "JpcInputData_RGSCORE"
+ "JpcInputData_irSensorAsmCalibration"
+ "JpcInputData_irSensorOpCalibration"
+ "JpcInputData_struct"
+ "MD PreProcessed Color"
+ "MD PreProcessed Secondary Color"
+ "MD PreProcessed pearl"
+ "MD Unprocessed Conf"
+ "MD Unprocessed Depth"
+ "MD aggregated point cloud"
+ "MD aggregated secondary point cloud"
+ "MD failed projecting pearl to secondary camera for logging with error %ld"
+ "MDNet"
+ "MatrixNxPts.hpp"
+ "Metric depth pipeline init for engine %lu"
+ "MetricDepth Executor does not have an inference buffer for color %d"
+ "MetricDepth Executor failed to allocate a color conversion session"
+ "MetricDepth only supports the ANE engine"
+ "MindfulNet"
+ "Model cost change: "
+ "Monocular null output returned"
+ "MultATagxB"
+ "Nested JPC Exception: "
+ "Nested std::exception: "
+ "NumOfAggregatedFrames"
+ "NumOfAggregatedFramesBucket"
+ "NumSpotsFlaggedAsGlare"
+ "NumSpotsFlaggedAsReflectiveSurface"
+ "PORPreprocessorFilterBlock_JASPER_MAX_GLARE_SPOTS_THRESHOLD"
+ "PORPreprocessorFilterBlock_JASPER_MAX_REFLECTIVE_SPOTS_THRESHOLD"
+ "PORPreprocessorFilterBlock_VIO_MAX_ROTATION_ANGLE_THRESHOLD"
+ "PORPreprocessorFilterBlock_VIO_MAX_TRANSLATION_THRESHOLD"
+ "PORPreprocessorFilterBlock_VIO_MIN_ROTATION_ANGLE_THRESHOLD"
+ "PORPreprocessorFilterBlock_VIO_MIN_TRANSLATION_THRESHOLD"
+ "Pearl Frame VIO"
+ "PearlCalibSetSize"
+ "PearlColorInfieldCalibration: unexpected resolution (%dx%d)"
+ "PearlJapserCalibSetSize"
+ "PearlToLastJasperBankRotation"
+ "PearlToLastJasperBankRotationBucket"
+ "PearlToLastJasperBankTranslation"
+ "PearlToLastJasperBankTranslationBucket"
+ "Pose for %@%@ is invalid"
+ "PreprocessingFailedException"
+ "PreprocessingFilterInvalidFrameException"
+ "Reading JPC config file %{public}s dictionary has failed."
+ "Received nil jasper point cloud"
+ "Received nil pearl buffer, aborting"
+ "Received nil point cloud, skipping filtering"
+ "ReprojectionError"
+ "ReprojectionErrorAfterBucket"
+ "ReprojectionErrorAfterGMCJ"
+ "ReprojectionErrorBeforeGMCJ"
+ "S4"
+ "SUPPORTED_PCE_CALIB_VERSION == pceCalib->version"
+ "SaturationPercentage"
+ "Solve"
+ "SumOfPearlJapserCalibSetSizes"
+ "T@\"<MTLBuffer>\",&,N,V_buffer"
+ "T@\"ADAggregationParameters\",&,N,V_pointCloudAggregationParameters"
+ "T@\"ADBinocularDepthExecutor\",R,&,N,V_executor"
+ "T@\"ADBinocularDepthExecutorParameters\",&,D,N"
+ "T@\"ADBinocularDepthPipeline\",R,&,N,V_pipeline"
+ "T@\"ADBinocularDepthPipelineParameters\",C,N,V_pipelineParameters"
+ "T@\"ADBinocularDepthPipelineParameters\",R,&,N,V_pipelineParameters"
+ "T@\"ADCameraCalibration\",&,N,V_calibration"
+ "T@\"ADCameraCalibration\",&,N,V_pearlInfraredCameraCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_primaryColorCameraCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_primaryDisparityCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_primaryTargetCameraCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_secondaryColorCameraCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_secondaryDisparityCalibration"
+ "T@\"ADCameraCalibration\",&,N,V_secondaryTargetCameraCalibration"
+ "T@\"ADCameraCalibration\",R,N,V_auxOutputCalib"
+ "T@\"ADCameraCalibration\",R,N,V_auxOutputCalibration"
+ "T@\"ADCameraCalibration\",R,N,V_auxRectifiedCalib"
+ "T@\"ADCameraCalibration\",R,N,V_primaryPoVCameraCalibration"
+ "T@\"ADCameraCalibration\",R,N,V_refRectifiedCalib"
+ "T@\"ADCameraCalibration\",R,N,V_secondaryPoVCameraCalibration"
+ "T@\"ADDensifiedLiDARFocusAssistExecutor\",R,&,N,V_executor"
+ "T@\"ADEspressoBinocularDepthInferenceDescriptor\",R,N,V_inferenceDescriptor"
+ "T@\"ADEspressoDensifiedLiDARFocusAssistInferenceDescriptor\",R,N"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_auxiliaryColorInput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_auxiliaryConfidenceOutput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_auxiliaryDisparityOutput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_auxiliarySegmentationOutput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_cameraEmbeddingInput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_primaryColorInput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_referenceColorInput"
+ "T@\"ADEspressoImageDescriptor\",R,N,V_secondaryColorInput"
+ "T@\"ADEspressoJasperColorInFieldCalibrationBackendInferenceDescriptor\",R,N"
+ "T@\"ADEspressoJasperColorInFieldCalibrationFrontendInferenceDescriptor\",R,N"
+ "T@\"ADEspressoJasperColorInferenceDescriptor\",R,N"
+ "T@\"ADEspressoJasperColorV2InferenceDescriptor\",R,N"
+ "T@\"ADEspressoJasperToColorTransformCorrectionBackendInfrerenceDescriptor\",R,N"
+ "T@\"ADEspressoJasperToColorTransformCorrectionFrontendInfrerenceDescriptor\",R,N"
+ "T@\"ADEspressoMetricDepthInferenceDescriptor\",R,N,V_inferenceDescriptor"
+ "T@\"ADEspressoMonocularInferenceDescriptor\",R,N"
+ "T@\"ADEspressoMonocularV2InferenceDescriptor\",R,N"
+ "T@\"ADEspressoPCEDisparityColorInferenceDescriptor\",R,N"
+ "T@\"ADEspressoPearlColorInFieldCalibrationBackendInferenceDescriptor\",R,N"
+ "T@\"ADEspressoPearlColorInFieldCalibrationFrontendInferenceDescriptor\",R,N"
+ "T@\"ADEspressoStereoInferenceDescriptor\",R,N"
+ "T@\"ADEspressoStereoV2InferenceDescriptor\",R,N"
+ "T@\"ADEspressoStillImageInferenceDescriptor\",R,N"
+ "T@\"ADImageDescriptor\",R,N,V_confidenceDescriptor"
+ "T@\"ADImageDescriptor\",R,N,V_downscaledInputDescriptor"
+ "T@\"ADImageDescriptor\",R,N,V_outputDescriptor"
+ "T@\"ADImageDescriptor\",R,N,V_primaryColorInput"
+ "T@\"ADImageDescriptor\",R,N,V_primaryOcclusionMapOutput"
+ "T@\"ADImageDescriptor\",R,N,V_primaryPredictionConfidenceOutput"
+ "T@\"ADImageDescriptor\",R,N,V_primaryPredictionOutput"
+ "T@\"ADImageDescriptor\",R,N,V_primaryRasterizedMeshInput"
+ "T@\"ADImageDescriptor\",R,N,V_secondaryColorInput"
+ "T@\"ADImageDescriptor\",R,N,V_secondaryOcclusionMapOutput"
+ "T@\"ADImageDescriptor\",R,N,V_secondaryPredictionConfidenceOutput"
+ "T@\"ADImageDescriptor\",R,N,V_secondaryPredictionOutput"
+ "T@\"ADImageDescriptor\",R,N,V_secondaryRasterizedMeshInput"
+ "T@\"ADImageDimensions\",&,N,V_requestedDimensions"
+ "T@\"ADJasperPearlInFieldCalibrationExecutorParameters\",&,D,N"
+ "T@\"ADJasperPearlInFieldCalibrationPipelineParameters\",&,N,V_pipelineParameters"
+ "T@\"ADJasperPearlInFieldCalibrationPipelineParameters\",R,&,N,V_pipelineParameters"
+ "T@\"ADJasperPearlTelemetryData\",&,N,V_telemetryData"
+ "T@\"ADJasperPointCloud\",&,N,V_bankPointCloud"
+ "T@\"ADLKTConfidenceParameters\",&,N,V_confidenceParameters"
+ "T@\"ADLKTExecutor\",R,&,N,V_executor"
+ "T@\"ADLKTExecutorParameters\",&,D,N"
+ "T@\"ADMetricDepthExecutor\",R,&,N,V_executor"
+ "T@\"ADMetricDepthExecutorParameters\",&,D,N"
+ "T@\"ADMetricDepthFrameStatistics\",R,&,N,V_lastFrameStatistics"
+ "T@\"ADMetricDepthPipeline\",R,&,N,V_pipeline"
+ "T@\"ADMetricDepthPipelineParameters\",C,N,V_pipelineParameters"
+ "T@\"ADMetricDepthPipelineParameters\",R,&,N,V_pipelineParameters"
+ "T@\"ADMonocularExecutor\",R,&,N,V_executor"
+ "T@\"ADVisualDepthBuffer\",&,N,V_metricDepth"
+ "T@\"ADVisualDepthExecutorParameters\",&,D,N"
+ "T@\"ADVisualDepthGeometry\",&,N,V_classification"
+ "T@\"ADVisualDepthGeometry\",&,N,V_confidence"
+ "T@\"ADVisualDepthGeometry\",&,N,V_faces"
+ "T@\"ADVisualDepthGeometry\",&,N,V_vertices"
+ "T@\"ADVisualDepthPipeline\",R,&,N,V_pipeline"
+ "T@\"ADVisualDepthPipelineParameters\",C,N,V_pipelineParameters"
+ "T@\"ADVisualDepthPipelineParameters\",R,&,N,V_pipelineParameters"
+ "T@\"NSArray\",R,&,N"
+ "T@\"NSData\",&,N,V_pceCalib"
+ "T@\"NSMutableArray\",&,N,V_rotArray"
+ "T@\"NSMutableArray\",&,N,V_transArray"
+ "T@\"NSNumber\",&,N,V_efl"
+ "T@\"NSNumber\",&,N,V_irCamFOVCoveragePercent"
+ "T@\"NSNumber\",&,N,V_maxIRCamTemperatureCurrentExecution"
+ "T@\"NSNumber\",&,N,V_minIRCamTemperatureCurrentExecution"
+ "T@\"NSNumber\",&,N,V_numOfUniqueTOFSpots"
+ "T@\"NSNumber\",&,N,V_principalPointX"
+ "T@\"NSNumber\",&,N,V_principalPointY"
+ "T@\"NSNumber\",&,N,V_temperature"
+ "T@\"NSNumber\",C,N,V_maxIRCamTemperature"
+ "T@\"NSNumber\",C,N,V_minIRCamTemperature"
+ "T@\"NSObject\",&,N,V_aggPointsWrapperObj"
+ "T@\"NSUUID\",&,N,V_uuid"
+ "TB,N,V_allPosesValid"
+ "TB,N,V_autoSetColorROI"
+ "TB,N,V_caCurrentTriggerEndReasonIsConvergence"
+ "TB,N,V_caCurrentTriggerEndReasonIsMaxFrameCount"
+ "TB,N,V_caCurrentTriggerEndReasonIsOutputValidationMetricIncreased"
+ "TB,N,V_checkFlowInFOV"
+ "TB,N,V_depthSensorsIgnored"
+ "TB,N,V_firstTimeEventFired"
+ "TB,N,V_forceCounterAsTimestamp"
+ "TB,N,V_ignoreDistortionInDepthReprojection"
+ "TB,N,V_isAssignedGMCJBlock"
+ "TB,N,V_isAssignedGMCJValidation"
+ "TB,N,V_isAssignedIFABlock"
+ "TB,N,V_isAssignedJasperReflectionsFrameFilter"
+ "TB,N,V_isAssignedPipelineCurrent"
+ "TB,N,V_isAssignedPipelinePrevious"
+ "TB,N,V_isReportTelemetry"
+ "TB,N,V_longRange"
+ "TB,N,V_skipISF"
+ "TI,N,V_jpcErrorCode"
+ "TI,N,V_maxCenterResolution"
+ "TI,N,V_maxRaysResolution"
+ "TI,N,V_numCenterBands"
+ "TI,N,V_numJasperBands"
+ "TI,N,V_numRaysBands"
+ "TI,R,N,V_numDynamicPixels"
+ "TI,R,N,V_sdfHistorySize"
+ "TOFUniqueSpotsNum"
+ "TOFUniqueSpotsNumBucket"
+ "TQ,N,V_caCurrentTriggerFrameCount"
+ "TQ,N,V_jasperInputSpotCount"
+ "TQ,N,V_jasperProjectedSpotCount"
+ "TQ,N,V_numOfAggregatedFrames"
+ "TQ,N,V_numOfIFAFramesCurrentExecution"
+ "TQ,N,V_numOfUniqueTOFSpots"
+ "TQ,N,V_pearlCalibSetSize"
+ "TQ,N,V_pearlJapserCalibSetSize"
+ "TQ,N,V_pearlProjectedPixelCount"
+ "TS,N,V_numPearlJasperCorrespondencesPostLocalDepthVarFilter"
+ "TS,N,V_numPearlJasperCorrespondencesPostPJDepthDiffFilter"
+ "TS,N,V_numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter"
+ "TS,N,V_numPearlJasperCorrespondencesPreIFA"
+ "TS,N,V_numPearlOnlyCorrespondencesPostSpatialCoverageFilter"
+ "TS,N,V_numPearlOnlyCorrespondencesPreIFA"
+ "T^{__CVBuffer=},N,V_dx"
+ "T^{__CVBuffer=},N,V_dy"
+ "T^{__CVBuffer=},N,V_image"
+ "T^{__CVBuffer=},N,V_labels"
+ "T^{__CVBuffer=},N,V_pearlDepth"
+ "T^{__CVBuffer=},N,V_pearlDx"
+ "T^{__CVBuffer=},N,V_pearlDy"
+ "T^{__CVBuffer=},N,V_pearlScore"
+ "T^{__CVBuffer=},N,V_score"
+ "T^{__CVBuffer=},R,N,V_auxConfidence"
+ "T^{__CVBuffer=},R,N,V_auxDepth"
+ "T^{__CVBuffer=},R,N,V_auxSegmentation"
+ "T^{__CVBuffer=},R,N,V_confidenceForPrimaryPoV"
+ "T^{__CVBuffer=},R,N,V_confidenceForSecondaryPoV"
+ "T^{__CVBuffer=},R,N,V_depthForPrimaryPoV"
+ "T^{__CVBuffer=},R,N,V_depthForSecondaryPoV"
+ "T^{__CVBuffer=},R,N,V_occlusionForPrimaryPoV"
+ "T^{__CVBuffer=},R,N,V_occlusionForSecondaryPoV"
+ "Td,N,V_caCurrentTriggerFirstFrameTimestamp"
+ "Td,N,V_caCurrentTriggerLastFrameTimestamp"
+ "Td,N,V_caLastTriggerLastFrameTimestamp"
+ "Td,N,V_coreAnalyticsEventInterval"
+ "Td,N,V_firstIFAFrameTimestampCurrentExecution"
+ "Td,N,V_gmcjPPXChangeMicronFromPrev"
+ "Td,N,V_gmcjPPXChangeMicronFromT0"
+ "Td,N,V_gmcjPPYChangeMicronFromPrev"
+ "Td,N,V_gmcjPPYChangeMicronFromT0"
+ "Td,N,V_gmcjScaleChangePercentFromPrev"
+ "Td,N,V_gmcjScaleChangePercentFromT0"
+ "Td,N,V_intervalBetweenIFAFrames"
+ "Td,N,V_irCamFOVCoveragePercent"
+ "Td,N,V_jasperMisalignmentAfter"
+ "Td,N,V_jasperMisalignmentBefore"
+ "Td,N,V_lastAlgoRadarTriggerTimestamp"
+ "Td,N,V_lastIFAFrameTimestampCurrentExecution"
+ "Td,N,V_newEfl"
+ "Td,N,V_newPPX"
+ "Td,N,V_newPPY"
+ "Td,N,V_pearlToLastJasperBankRotation"
+ "Td,N,V_pearlToLastJasperBankTranslation"
+ "Td,N,V_prevEfl"
+ "Td,N,V_prevPPX"
+ "Td,N,V_prevPPY"
+ "Td,N,V_reprojectionErrorAfter"
+ "Td,N,V_reprojectionErrorBefore"
+ "Td,N,V_saturationCheckInterval"
+ "Td,N,V_timestamp"
+ "Td,R,N,V_timestamp"
+ "Temperature"
+ "TemperatureBucket"
+ "TemperatureDeltaBetweenIFAFrames"
+ "Tf,N,V_caCurrentTriggerFirstFrameTemperature"
+ "Tf,N,V_caCurrentTriggerLastFrameTemperature"
+ "Tf,N,V_caLastTriggerLastFrameTemperature"
+ "Tf,N,V_colorPoseRoll"
+ "Tf,N,V_conditionNumberMaxValue"
+ "Tf,N,V_conditionNumberMinValue"
+ "Tf,N,V_depthDiffThresholdAboveMedian"
+ "Tf,N,V_gmcjProjRotXChangeFromPrev"
+ "Tf,N,V_gmcjProjRotXChangeFromT0"
+ "Tf,N,V_gmcjProjRotYChangeFromPrev"
+ "Tf,N,V_gmcjProjRotYChangeFromT0"
+ "Tf,N,V_gmcjProjRotZChangeFromPrev"
+ "Tf,N,V_gmcjProjRotZChangeFromT0"
+ "Tf,N,V_gradientNormMaxValue"
+ "Tf,N,V_gradientNormMinValue"
+ "Tf,N,V_jasperPoseDistance"
+ "Tf,N,V_lastPearlTemp"
+ "Tf,N,V_maxJasperDepth"
+ "Tf,N,V_motionBetweenFramesRotationX"
+ "Tf,N,V_motionBetweenFramesRotationY"
+ "Tf,N,V_motionBetweenFramesRotationZ"
+ "Tf,N,V_motionBetweenFramesTranslationX"
+ "Tf,N,V_motionBetweenFramesTranslationY"
+ "Tf,N,V_motionBetweenFramesTranslationZ"
+ "Tf,N,V_newRotX"
+ "Tf,N,V_newRotY"
+ "Tf,N,V_newRotZ"
+ "Tf,N,V_pearlJasperCoFilteringMaxAllowedDisagreement"
+ "Tf,N,V_pearlJasperCoFilteringMaxPearlDepth"
+ "Tf,N,V_pearlProjectedPixelPercentage"
+ "Tf,N,V_pearlTemperature"
+ "Tf,N,V_pearlToLastJasperBankRotationX"
+ "Tf,N,V_pearlToLastJasperBankRotationY"
+ "Tf,N,V_pearlToLastJasperBankRotationZ"
+ "Tf,N,V_pearlToLastJasperBankTranslationX"
+ "Tf,N,V_pearlToLastJasperBankTranslationY"
+ "Tf,N,V_pearlToLastJasperBankTranslationZ"
+ "Tf,N,V_prevRotX"
+ "Tf,N,V_prevRotY"
+ "Tf,N,V_prevRotZ"
+ "Tf,N,V_rectifiedCameraFieldOfViewHeight"
+ "Tf,N,V_rectifiedCameraFieldOfViewWidth"
+ "Tf,N,V_saturationThreshold"
+ "Tf,N,V_temperature"
+ "Ti,N,V_gmcjErrorCode"
+ "Ti,N,V_gmcjOutputValidationErrorCode"
+ "Ti,N,V_scaleIdxForConfidenceComponents"
+ "Total Loss: "
+ "Tq,N,V_count"
+ "Tq,N,V_offset"
+ "Tq,N,V_stepsToExecute"
+ "Tq,N,V_stride"
+ "TriggerTemperatureDifference"
+ "TriggerTimeDifference"
+ "Ts,N,V_numJasperSpotsFlaggedAsGlare"
+ "Ts,N,V_numJasperSpotsFlaggedAsReflectiveSurface"
+ "T{?=Q@BiifffQI},R,N,V_opticalFlowConfig"
+ "T{?=[4]},N,V_jasperBankPose"
+ "T{?=[4]},N,V_pose"
+ "T{?=[4]},N,V_prevPose"
+ "T{?=[4]},N,V_transform"
+ "T{AggregatedData={vector<jpc::IIFABlock::IFAPearlJasperCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlJasperCorrespondence>>=^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}}{vector<jpc::IIFABlock::IFAPearlCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlCorrespondence>>=^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}}},N,V_aggData"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_validDepthRect"
+ "VD primary color input"
+ "VD primary conf estimation"
+ "VD primary depth estimation"
+ "VD primary mesh input"
+ "VD primary mesh sqrt info"
+ "VD primary occlusion estimation"
+ "VD secondary color input"
+ "VD secondary conf estimation"
+ "VD secondary depth estimation"
+ "VD secondary mesh input"
+ "VD secondary mesh sqrt info"
+ "VD secondary occlusion estimation"
+ "Warning! Ignoring active sensors"
+ "[11@\"<MTLComputePipelineState>\"]"
+ "^{PixelBufferUtilsSession=^{__CVBuffer}^{OpaqueVTPixelTransferSession}^{OpaqueVTPixelRotationSession}{CGSize=dd}I{CGSize=dd}I{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}ii}"
+ "^{PixelBufferUtilsTiledView=^{TileConfig}QQQQQ^{__CVBuffer}}"
+ "^{__CVBuffer=}48@0:8@16Q24Q32r*40"
+ "_MutableKeyframes"
+ "_MutableMeshChunks"
+ "_aggData"
+ "_aggPointsWrapperObj"
+ "_aggregatedPrimaryPointCloud"
+ "_aggregatedSecondaryPointCloud"
+ "_allPosesValid"
+ "_autoSetColorROI"
+ "_auxCalib"
+ "_auxConfidence"
+ "_auxDepth"
+ "_auxOutputCalib"
+ "_auxOutputCalibration"
+ "_auxRectifiedCalib"
+ "_auxSegmentation"
+ "_auxWarper"
+ "_auxiliaryColorInput"
+ "_auxiliaryConfidenceOutput"
+ "_auxiliaryDisparityOutput"
+ "_auxiliarySegmentationOutput"
+ "_backProjectedMap"
+ "_bankPointCloud"
+ "_bilinearScaler"
+ "_buffer"
+ "_caCurrentTriggerEndReasonIsConvergence"
+ "_caCurrentTriggerEndReasonIsMaxFrameCount"
+ "_caCurrentTriggerEndReasonIsOutputValidationMetricIncreased"
+ "_caCurrentTriggerFirstFrameTemperature"
+ "_caCurrentTriggerFirstFrameTimestamp"
+ "_caCurrentTriggerFrameCount"
+ "_caCurrentTriggerLastFrameTemperature"
+ "_caCurrentTriggerLastFrameTimestamp"
+ "_caLastTriggerLastFrameTemperature"
+ "_caLastTriggerLastFrameTimestamp"
+ "_calibration"
+ "_cameraCenterEmbeddings"
+ "_cameraEmbeddingInput"
+ "_cameraRaysEmbeddings"
+ "_canDelegateFailure"
+ "_canDelegateProcess"
+ "_checkFlowInFOV"
+ "_classification"
+ "_colorConvertingSession"
+ "_colorPoseRoll"
+ "_colorScalingSession"
+ "_completionEvent"
+ "_computeConfidence:shiftMap:outConfidceMap:cropSizeRatio:"
+ "_computeFeaturesDerivativesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:"
+ "_computeFeaturesWithCommandBuffer:cropSizeRatio:in_tex:out_tex:"
+ "_conditionNumberConfidenceTex"
+ "_conditionNumberMaxValue"
+ "_conditionNumberMinValue"
+ "_confidenceDescriptor"
+ "_confidenceForPrimaryPoV"
+ "_confidenceForSecondaryPoV"
+ "_confidenceParameters"
+ "_coreAnalyticsEventInterval"
+ "_coreAnalyticsToSaturationChecksRatio"
+ "_count"
+ "_counterTimestamp"
+ "_createImagePyramidWithCommandBuffer:cropSizeRatio:inOutPyramidsArray:error:"
+ "_createImagePyramidWithCommandBuffer:in_tex:cropSizeRatio:outPyramidsArray:error:"
+ "_currentExtrinsics"
+ "_dbgPointCloudCropped"
+ "_depthDiffThresholdAboveMedian"
+ "_depthForPrimaryPoV"
+ "_depthForSecondaryPoV"
+ "_depthSensorsIgnored"
+ "_diagnosticPipelineLog"
+ "_diagnosticPipelineLogIndex"
+ "_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:cropSizeRatio:"
+ "_doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:in_uv_tex:out_uv_tex:out_w_tex:uniforms:cropSizeRatio:"
+ "_downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:cropSizeRatio:"
+ "_downscaledInputDescriptor"
+ "_downscaledInputSize"
+ "_downscaledInputTexture"
+ "_downscaledJasperBuffer"
+ "_dx"
+ "_dy"
+ "_efl"
+ "_espressoEngine"
+ "_expectedSensorCrop"
+ "_extrinsicsMode"
+ "_faces"
+ "_firstIFAFrameTimestampCurrentExecution"
+ "_firstScaleStride"
+ "_firstTimeEventFired"
+ "_forceCounterAsTimestamp"
+ "_gmcjErrorCode"
+ "_gmcjOutputValidationErrorCode"
+ "_gmcjPPXChangeMicronFromPrev"
+ "_gmcjPPXChangeMicronFromT0"
+ "_gmcjPPYChangeMicronFromPrev"
+ "_gmcjPPYChangeMicronFromT0"
+ "_gmcjProjRotXChangeFromPrev"
+ "_gmcjProjRotXChangeFromT0"
+ "_gmcjProjRotYChangeFromPrev"
+ "_gmcjProjRotYChangeFromT0"
+ "_gmcjProjRotZChangeFromPrev"
+ "_gmcjProjRotZChangeFromT0"
+ "_gmcjScaleChangePercentFromPrev"
+ "_gmcjScaleChangePercentFromT0"
+ "_gradientNormConfidenceTex"
+ "_gradientNormMaxValue"
+ "_gradientNormMinValue"
+ "_grayscaleTexture"
+ "_greyscaleInput"
+ "_ignoreDistortionInDepthReprojection"
+ "_image"
+ "_inferenceDescriptor"
+ "_intervalBetweenIFAFrames"
+ "_irCamFOVCoveragePercent"
+ "_isAssignedGMCJBlock"
+ "_isAssignedGMCJValidation"
+ "_isAssignedIFABlock"
+ "_isAssignedJasperReflectionsFrameFilter"
+ "_isAssignedPipelineCurrent"
+ "_isAssignedPipelinePrevious"
+ "_isFirstFrame"
+ "_isReportTelemetry"
+ "_isTemporal"
+ "_itmPreProcessedCameraEmbBuffer"
+ "_itmPreProcessedJasperEmbBuffer"
+ "_itmPreProcessedPearlBuffer"
+ "_itmPreProcessedPearlProjectedOnSecondary"
+ "_itmProcessedAuxColor"
+ "_itmProcessedRefColor"
+ "_itmRawAuxConfidence"
+ "_itmRawAuxDisparity"
+ "_itmRawAuxSegmentation"
+ "_itmYUVColor"
+ "_jasperBankPose"
+ "_jasperEmbeddings"
+ "_jasperInputSpotCount"
+ "_jasperMisalignmentAfter"
+ "_jasperMisalignmentBefore"
+ "_jasperPoseDistance"
+ "_jasperProjectedSpotCount"
+ "_jpcErrorCode"
+ "_keyframeInput"
+ "_knownConfigs"
+ "_labels"
+ "_lastAlgoRadarTriggerTimestamp"
+ "_lastCameraCalibration"
+ "_lastExtrinsicsFromInput"
+ "_lastFrameStatistics"
+ "_lastIFAFrameTimestampCurrentExecution"
+ "_lastKnownGoodFramesCount"
+ "_lastPearlTemp"
+ "_lastPose"
+ "_lastReceivedPrimaryColor"
+ "_lastReceivedPrimaryColorPose"
+ "_lastReceivedPrimaryColorTimestamp"
+ "_lastReceivedSecondaryColor"
+ "_lastSaturationCheckTimestamp"
+ "_lastSize"
+ "_lastStreamSyncMatchLock"
+ "_lastSyncMatch"
+ "_lastTimestamp"
+ "_longRange"
+ "_maxCenterResolution"
+ "_maxIRCamTemperature"
+ "_maxIRCamTemperatureCurrentExecution"
+ "_maxJasperDepth"
+ "_maxRaysResolution"
+ "_meshInput"
+ "_metalDesc"
+ "_metricDepth"
+ "_minIRCamTemperature"
+ "_minIRCamTemperatureCurrentExecution"
+ "_minPyramidLevel"
+ "_modelBuilder"
+ "_motionBetweenFramesRotationX"
+ "_motionBetweenFramesRotationY"
+ "_motionBetweenFramesRotationZ"
+ "_motionBetweenFramesTranslationX"
+ "_motionBetweenFramesTranslationY"
+ "_motionBetweenFramesTranslationZ"
+ "_mtlCommandQueue"
+ "_mtlDevice"
+ "_newEfl"
+ "_newPPX"
+ "_newPPY"
+ "_newRotX"
+ "_newRotY"
+ "_newRotZ"
+ "_numCenterBands"
+ "_numDynamicPixels"
+ "_numJasperBands"
+ "_numJasperSpotsFlaggedAsGlare"
+ "_numJasperSpotsFlaggedAsReflectiveSurface"
+ "_numOfAggregatedFrames"
+ "_numOfIFAFramesCurrentExecution"
+ "_numOfUniqueTOFSpots"
+ "_numPearlJasperCorrespondencesPostLocalDepthVarFilter"
+ "_numPearlJasperCorrespondencesPostPJDepthDiffFilter"
+ "_numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter"
+ "_numPearlJasperCorrespondencesPreIFA"
+ "_numPearlOnlyCorrespondencesPostSpatialCoverageFilter"
+ "_numPearlOnlyCorrespondencesPreIFA"
+ "_numPriorInputs"
+ "_numRaysBands"
+ "_numberOfSaturationChecks"
+ "_occlusionForPrimaryPoV"
+ "_occlusionForSecondaryPoV"
+ "_offset"
+ "_opticalFlowAllocated"
+ "_outputDescriptor"
+ "_outputSize"
+ "_pcAggregator"
+ "_pcRefiner"
+ "_pceCalib"
+ "_pearlCalibSetSize"
+ "_pearlDepth"
+ "_pearlDx"
+ "_pearlDy"
+ "_pearlInfraredCameraCalibration"
+ "_pearlJapserCalibSetSize"
+ "_pearlJasperCoFilteringMaxAllowedDisagreement"
+ "_pearlJasperCoFilteringMaxPearlDepth"
+ "_pearlProjectedPixelCount"
+ "_pearlProjectedPixelPercentage"
+ "_pearlScore"
+ "_pearlTemperature"
+ "_pearlToLastJasperBankRotation"
+ "_pearlToLastJasperBankRotationX"
+ "_pearlToLastJasperBankRotationY"
+ "_pearlToLastJasperBankRotationZ"
+ "_pearlToLastJasperBankTranslation"
+ "_pearlToLastJasperBankTranslationX"
+ "_pearlToLastJasperBankTranslationY"
+ "_pearlToLastJasperBankTranslationZ"
+ "_pixelsMap"
+ "_pointCloudAggregationParameters"
+ "_postProcessedMetricActiveDepthMaskDesc"
+ "_postProcessedMetricConfLevelsDesc"
+ "_prepareLKTGPUUniforms:out_uv_tex:coeff:stride:computeConfidenceComponents:"
+ "_prepared"
+ "_prevEfl"
+ "_prevPPX"
+ "_prevPPY"
+ "_prevRotX"
+ "_prevRotY"
+ "_prevRotZ"
+ "_primaryCameraID"
+ "_primaryColorCameraCalibration"
+ "_primaryColorInput"
+ "_primaryDisparityCalibration"
+ "_primaryMeshPriorIdx"
+ "_primaryOcclusionMapOutput"
+ "_primaryPoVCameraCalibration"
+ "_primaryPredictionConfidenceOutput"
+ "_primaryPredictionOutput"
+ "_primaryRasterizedMeshInput"
+ "_primaryTargetCameraCalibration"
+ "_principalPointX"
+ "_principalPointY"
+ "_processedJasper"
+ "_raysMap"
+ "_rectifiedCameraFieldOfViewHeight"
+ "_rectifiedCameraFieldOfViewWidth"
+ "_refCalib"
+ "_refRectifiedCalib"
+ "_refWarper"
+ "_referenceColorInput"
+ "_reprojectionErrorAfter"
+ "_reprojectionErrorBefore"
+ "_requestedDimensions"
+ "_requiredVDInit"
+ "_rotArray"
+ "_saturationCheckInterval"
+ "_saturationThreshold"
+ "_scaleIdxForConfidenceComponents"
+ "_score"
+ "_sdfHistoryFrames"
+ "_sdfHistoryRollingIndex"
+ "_sdfHistorySize"
+ "_secondaryCameraID"
+ "_secondaryColorCameraCalibration"
+ "_secondaryColorInput"
+ "_secondaryDisparityCalibration"
+ "_secondaryMeshPriorIdx"
+ "_secondaryOcclusionMapOutput"
+ "_secondaryPoVCameraCalibration"
+ "_secondaryPredictionConfidenceOutput"
+ "_secondaryPredictionOutput"
+ "_secondaryRasterizedMeshInput"
+ "_secondaryTargetCameraCalibration"
+ "_skipISF"
+ "_stepsToExecute"
+ "_stride"
+ "_targetPearlBuffer"
+ "_teleAfType"
+ "_telemetryData"
+ "_temperature"
+ "_tiledView"
+ "_timestamp"
+ "_transArray"
+ "_transform"
+ "_undistortHalvedMaps"
+ "_undistortMaps"
+ "_uuid"
+ "_validDepthRect"
+ "_vdColorInputCrop"
+ "_vdPrimaryConfOutput"
+ "_vdPrimaryDepthOutput"
+ "_vdPrimaryInput"
+ "_vdPrimaryItm1"
+ "_vdPrimaryItm2"
+ "_vdPrimaryMeshIntermediate"
+ "_vdPrimaryOcclusionOutput"
+ "_vdSecondaryConfOutput"
+ "_vdSecondaryDepthOutput"
+ "_vdSecondaryInput"
+ "_vdSecondaryItm1"
+ "_vdSecondaryItm2"
+ "_vdSecondaryMeshIntermediate"
+ "_vdSecondaryOcclusionOutput"
+ "_vdSqrtInfoPrimaryMeshInput"
+ "_vdSqrtInfoSecondaryMeshInput"
+ "_vioTemporalAllocated"
+ "_visualDepthResolution"
+ "_zMap"
+ "addChunk:"
+ "addEntriesFromDictionary:"
+ "addKeyframe:"
+ "addKeyframeInput:timestamp:"
+ "addMeshInput:"
+ "addPrimaryCalibration:secondaryCalibration:timestamp:"
+ "aggData"
+ "aggPointsWrapperObj"
+ "agg_points"
+ "aggregateForTime:worldToCameraTransform:"
+ "aggregationSize"
+ "allPosesValid"
+ "appendBytes:length:"
+ "appendData:"
+ "applyPerformanceOverrides"
+ "autoSetColorROI"
+ "auxConfidence"
+ "auxDepth"
+ "auxOutputCalib"
+ "auxOutputCalibration"
+ "auxRectifiedCalib"
+ "auxSegmentation"
+ "auxiliaryColorInput"
+ "auxiliaryConfidenceOutput"
+ "auxiliaryDisparityOutput"
+ "auxiliarySegmentationOutput"
+ "b"
+ "backProject:undistortedPixels:withZ:outPoints:"
+ "bad vertex format"
+ "bankPointCloud"
+ "bilinearInterpolateInSquare"
+ "blitCommandEncoder"
+ "bufferExists:isInput:"
+ "build metal pipeline"
+ "buildISFInputDictWithEFL:principalPointtX:principalPointtY:rotationMat:"
+ "buildJpcInputDataObjectWithPearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:outJpcInputs:"
+ "buildMetalPipelineWithQueue:lensDistortion:"
+ "build_config.plist"
+ "caCurrentTriggerEndReasonIsConvergence"
+ "caCurrentTriggerEndReasonIsMaxFrameCount"
+ "caCurrentTriggerEndReasonIsOutputValidationMetricIncreased"
+ "caCurrentTriggerFirstFrameTemperature"
+ "caCurrentTriggerFirstFrameTimestamp"
+ "caCurrentTriggerFrameCount"
+ "caCurrentTriggerLastFrameTemperature"
+ "caCurrentTriggerLastFrameTimestamp"
+ "caLastTriggerLastFrameTemperature"
+ "caLastTriggerLastFrameTimestamp"
+ "calcJacobian"
+ "calculateCostFunctionResiduals"
+ "cameraEmbeddingInput"
+ "cameraPixels"
+ "camera_embedding_bundle"
+ "cannot filter uncertainty. input and output buffers do not match"
+ "cannot filter uncertainty. wrong pixel format"
+ "cannot prepare metric depth with different espresso engine from what initialized with"
+ "cannot prepare visual depth buffers. not supported by pipeline"
+ "cannot re-enable optical flow temporal consistency after executor was prepared without it."
+ "cannot run visual depth. inputs not ready"
+ "checkFlowInFOV"
+ "checkPrerequisitesForProcessWithPearlWithPearlInputs:"
+ "checkProjectionChanged:newCalib:"
+ "classification"
+ "clear"
+ "clearBuffer"
+ "clearKeyframes:"
+ "clearing mask due to invalid pose inputs"
+ "colorPoseRoll"
+ "colorRoi"
+ "com.apple.BreathingMotion.ImageQuality"
+ "com.apple.applecamerad.JasperPearlCalibration"
+ "com.apple.applecamerad.JasperPearlCalibrationFirstTimeEvent"
+ "com.apple.applecamerad.JasperPearlCalibrationTriggering"
+ "commandBufferWithUnretainedReferences"
+ "commitAndWaitUntilSubmitted"
+ "computeCropForRectifiedImage:calib:"
+ "conditionNumberMaxValue"
+ "conditionNumberMinValue"
+ "confidenceDescriptor"
+ "confidenceForPrimaryPoV"
+ "confidenceForSecondaryPoV"
+ "confidenceParameters"
+ "contents"
+ "convertInputFormatIfNeeded:greyscaleInput:"
+ "copyConfidenceAllowPixelFormatChange:outputConfidence:"
+ "copyFromTexture:toTexture:"
+ "copyWithZone:"
+ "coreAnalyticsEventInterval"
+ "could not find json file at path %{public}@"
+ "could not open %{public}@ for write"
+ "could not read network metadata"
+ "createCameraEmbeddingsForRightCameraCalibration:leftCameraCalibration:rightCameraPose:leftCameraPose:outputBuffer:"
+ "createColorConvertingSession:"
+ "createConfidenceBuffer"
+ "createIntrinsicsMatrixWithEFL:principalPointX:principalPointY:"
+ "createIntrinsicsMatrixWithEflX:eflY:principalPointX:principalPointY:"
+ "createJasperEmbeddings:cropTo:rotateBy:outputBuffer:outputBatchOffset:"
+ "createJasperEmbeddingsForRightCameraPointCloud:leftCameraPointCloud:crop:rotation:outputBuffer:"
+ "createNzPerColumn"
+ "createOpticalFlowBuffer"
+ "createPearlCorrespondences"
+ "createPixelBufferNoCopy"
+ "createRequestedLayoutsForDimensions:"
+ "createRequestedLayoutsForDimensions:function:"
+ "createRequestedLayoutsForDimensions:layout:function:"
+ "cv3d.fused"
+ "dataWithLength:"
+ "deallocateVisualDepthBuffers"
+ "defaults"
+ "depthDiffThresholdAboveMedian"
+ "depthForPrimaryPoV"
+ "depthForSecondaryPoV"
+ "depthSensorsIgnored"
+ "depth_features"
+ "descriptorWithDefaultSize:pixelFormat:"
+ "diagnosticPipelineLog"
+ "dictionaryWithContentsOfURL:error:"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "distort:undistortedPixels:outDistorted:"
+ "distortedRadii"
+ "doubleBufferToFloatNSDataWithBuffer"
+ "downscaleImageAndGenerateMipmapsIfNeeded:inputTexture:"
+ "downscaledInputDescriptor"
+ "downscaledInputSizeForLayout:"
+ "dropLastFrame:"
+ "dx"
+ "dxDySamplePoints.first.size() == dxDySamplePoints.second.size()"
+ "dxHelper.getWidth() == dyHelper.getWidth() && dxHelper.getHeight() == dyHelper.getHeight()"
+ "dy"
+ "echoIds"
+ "efl"
+ "emptyFilter"
+ "emulatePeridotFromJasper:jasperPoses:jasperTimestamps:jasperToPlatformTransform:pearlDepth:pearlPose:pearlCalibration:outPointCloud:outPose:outTimestamp:"
+ "encodeOpticalFlowSolverToCommandBuffer:currentFeaturesArray:currentDerivitiveArray:previousFeaturesArray:previousDerivitiveArray:currentPyramidsArray:validBufferRect:outShiftMap:outConfidenceMap:"
+ "encodePredictionToCommandBuffer:primaryColorInput:secondaryColorInput:primaryPredictionOutput:secondaryPredictionOutput:primaryOcclusionOutput:secondaryOcclusionOutput:predictionTimestamp:predictionPose:poseSessionID:poseReinitCount:"
+ "encodePyramidFeaturesToCommandBuffer:grayscaleTexture:validBufferRect:outPyramidsArray:outFeaturesArray:outDerivitiveArray:"
+ "encodeSignalEvent:value:"
+ "encodeToCommandBuffer:sourceTexture:destinationTexture:"
+ "error opening mesh chunk file: %{public}@"
+ "error parsing obj file: not enough vertices and faces"
+ "error parsing obj file: seems empty"
+ "espressoRunner"
+ "estimationX <= x2"
+ "estimationX >= x1"
+ "estimationY <= y2"
+ "estimationY >= y1"
+ "executeForTimestamp:pose:"
+ "executeForTimestamp:pose:output:"
+ "executeFromFrame:toFrame:outputOpticalFlow:outputConfidence:"
+ "executeFromFrame:toFrame:validBufferRect:outputOpticalFlow:outputConfidence:"
+ "executeFromFrameToPreviousFrame:outputOpticalFlow:outputConfidence:"
+ "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointCloud:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:"
+ "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:"
+ "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNonTemporalyConsistentDepthMap:outNonTemporalyConsistentConfMap:outConfidenceLevels:"
+ "executeWithColor:timestamp:pointClouds:lidarCalibration:colorMetadata:colorCameraCalibration:outputDepthMap:outputConfidenceMap:outputCalibration:"
+ "executeWithInterSessionData:outResult:"
+ "executeWithInterSessionData:result:"
+ "executeWithJasperPearlInterSessionData:result:"
+ "executeWithOutput:"
+ "executeWithPrimaryColor:secondaryColor:pearl:pointClouds:primaryColorCalibration:secondaryColorCalibration:pearlCalibration:lidarCameraCalibration:primaryColorPose:secondaryColorPose:pearlPose:pointCloudPoses:timestamp:outputDepthMap:outputUncertaintyMap:outputConfidenceMap:outputConfidenceLevels:outputNormalsMap:outputActiveDepthMaskMap:outputDepthCalibration:"
+ "executeWithRefColor:auxColor:"
+ "executeWithRefColor:auxColor:auxOutputDepth:auxOutputConfidence:"
+ "executeWithRefColor:auxColor:auxOutputDepth:auxOutputConfidence:timestamp:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputCalib:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputCalib:timestamp:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputSegmentation:auxOutputCalib:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:auxOutputSegmentation:auxOutputCalib:timestamp:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:auxOutputDepth:auxOutputConfidence:timestamp:"
+ "executeWithRefColor:auxColor:refCalib:auxCalib:timestamp:"
+ "executeWithRefColor:auxColor:timestamp:"
+ "executor execute"
+ "expectedColorSensorROI"
+ "extractIRSensorCalibFromLastSyncMatch"
+ "extractJasperToPearlCalibFromLastSyncMatch"
+ "extractPearlInputsFromLastSyncMatch"
+ "extractPearlPrevPoseFromLastSyncMatch"
+ "extractYChannelFromColorInput:toBuffer:"
+ "f "
+ "f %d %d %d\n"
+ "f24@0:8d16"
+ "face "
+ "faces"
+ "failed allocating color input"
+ "failed allocating mesh chunk. faces:%p vertices:%p"
+ "failed converting color image to greyscale"
+ "failed converting color input %d with color session"
+ "failed copy initial prev conf"
+ "failed copy initial prev depth"
+ "failed creating confidence levels"
+ "failed crop and scale image"
+ "failed embedding jasper for left camera"
+ "failed embedding jasper for right camera"
+ "failed emulating peridot from jasper"
+ "failed executing LKT"
+ "failed executing Monocular"
+ "failed executing binocularDepth"
+ "failed executing metric depth"
+ "failed execution of DensifiedLiDARFocusAssist"
+ "failed filtering jasper (primary) with pearl"
+ "failed parsing json metadata for requested model %{public}@"
+ "failed populating depth pixel buffer from disparity"
+ "failed post processing metric active depth mask output"
+ "failed post processing metric depth confidence levels output"
+ "failed post processing metric depth confidence output"
+ "failed post processing metric depth output"
+ "failed post processing metric normals output"
+ "failed preparing half scaled camera calibration"
+ "failed preparing with default configuration. Try calling prepare with arguments matching your inputs"
+ "failed processing depth from pixel shifts"
+ "failed processing output aux confidence"
+ "failed projecting pearl for color POV"
+ "failed rotating non-temporal depth. please verify output buffer dimensions"
+ "failed setting primary color calibration"
+ "failed setting secondary color calibration"
+ "failed to create camera embeddings"
+ "failed to create jasper embeddings"
+ "failed to push point cloud into aggregator"
+ "failed to scale primary color calibration into network dimensions"
+ "failed to scale secondary color calibration into network dimensions"
+ "failed warping image"
+ "fillSensorsMask:"
+ "fillTelemetryData:jpcError:"
+ "fillTelemetryDataWithPreviousCalibration:pceCalib:"
+ "filterJasperPointCloud:usingPearlInput:"
+ "filterUncertainty:output:"
+ "firstIFAFrameTimestampCurrentExecution"
+ "firstTimeEventFired"
+ "fixEFLTempCoeffInISFResult:eflTempCoeff:temperature:"
+ "flags"
+ "flow_features"
+ "flow_matching_x4"
+ "forceCounterAsTimestamp"
+ "fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:"
+ "fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:alpha:confidenceUnits:"
+ "fvalNew = "
+ "generateMipmapsForTexture:"
+ "getDataPtr"
+ "getIRSensorCameraCalibFromPCECalib"
+ "getJpcObjectForRunMode:isValid:"
+ "getMinDistanceForTimestamp:"
+ "getPCECalibStruct"
+ "getPearlDepthAttachments"
+ "getPixelPtr"
+ "getRealDeviceName"
+ "getRectifiedColorInputSaturationRate"
+ "getTeleAfPlatformType"
+ "gmcjErrorCode"
+ "gmcjOutputValidationErrorCode"
+ "gmcjPPXChangeMicronFromPrev"
+ "gmcjPPXChangeMicronFromT0"
+ "gmcjPPYChangeMicronFromPrev"
+ "gmcjPPYChangeMicronFromT0"
+ "gmcjProjRotXChangeFromPrev"
+ "gmcjProjRotXChangeFromT0"
+ "gmcjProjRotYChangeFromPrev"
+ "gmcjProjRotYChangeFromT0"
+ "gmcjProjRotZChangeFromPrev"
+ "gmcjProjRotZChangeFromT0"
+ "gmcjScaleChangePercentFromPrev"
+ "gmcjScaleChangePercentFromT0"
+ "gradientNormMaxValue"
+ "gradientNormMinValue"
+ "hasLidarToColorIncreasedBaseline:"
+ "height_144_width_256"
+ "height_160_width_224"
+ "highPerformanceConfig"
+ "highQualityConfig"
+ "i0"
+ "i1"
+ "i136@0:8@16@24@32@40@48@56@64@72{?=IIiIBB    }80128"
+ "i32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
+ "i40@0:8^{__CVBuffer=}16q24^{__CVBuffer=}32"
+ "i48@0:8@1624@32@40"
+ "i56@0:8@16@24@324048"
+ "ignoreDistortionInDepthReprojection"
+ "ignoring empty keyframe input"
+ "ignoring empty mesh input"
+ "imageDimensionsWithWidth:height:"
+ "initDiagnosticPipelineLog"
+ "initForEspressoEngine:"
+ "initForEspressoEngine:pipelineParameters:"
+ "initForSupportedSizes:prioritization:"
+ "initWithAggregationParameters:jasperToColorTransform:colorCamera:"
+ "initWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:"
+ "initWithBuffer:count:offset:stride:"
+ "initWithColorInputSize:colorInputFormat:rasterizedMeshInputSize:occlusionSize:povcSize:predictsDisparity:"
+ "initWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:"
+ "initWithDescriptor:forLayout:executorParameters:"
+ "initWithDevice:"
+ "initWithDevice:inputSize:config:confidenceParameters:"
+ "initWithDistortionCenter:distortedRadii:undistortedRadii:"
+ "initWithExecutor:andIntersessionData:andExtrinsicsFlowMode:"
+ "initWithExecutor:calculateConfidenceMap:calculateConfidenceLevels:"
+ "initWithExecutor:forTemporalOpticalFlow:"
+ "initWithFile:"
+ "initWithImage:confidence:labels:normals:calibration:uuid:pose:timestamp:"
+ "initWithLength:"
+ "initWithMetalCommandQueue:dimensions:format:"
+ "initWithNetwork:requestedLayouts:espressoEngine:makeRunnable:"
+ "initWithNetworkProvider:prioritization:espressoEngine:"
+ "initWithOutputDimensions:"
+ "initWithPCECalibData:"
+ "initWithParameters:pceCalib:"
+ "initWithPceCalib:"
+ "initWithPearlDepth:pearlDx:pearlDy:pearlScore:"
+ "initWithPrioritization:espressoEngine:"
+ "initWithUUIDString:"
+ "initWithVertices:faces:confidence:classification:transform:uuid:timestamp:"
+ "initWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:"
+ "initWithWorkingSize:"
+ "initialized visual depth pipeline with cmdQueue %p, dimensions: (%f,%f)"
+ "inputPearlPose"
+ "inputSecondaryColor"
+ "inputSecondaryColorCalibration"
+ "inputSecondaryColorPose"
+ "inputWithImage:confidence:calibration:"
+ "inputWithImage:confidence:calibration:uuid:"
+ "inputWithImage:confidence:labels:normals:calibration:uuid:pose:timestamp:"
+ "insertEntryToDiagnosticPipelineLog:"
+ "intermediateAggregatedPointCloud"
+ "intermediateAggregatedPointCloudProjectedToPrimary"
+ "intermediateAggregatedPointCloudProjectedToPrimaryCoFiltered"
+ "intermediateAggregatedPointCloudRefined"
+ "intermediateColorCalibration"
+ "intermediateConfidenceLevelsOut"
+ "intermediateConfidenceOutProcessed"
+ "intermediateConfidenceOutProcessedRotated"
+ "intermediateDepthOutProcessed"
+ "intermediateDepthOutProcessedRotated"
+ "intermediateOpticalFlow"
+ "intermediatePrevWarpedConf"
+ "intermediatePrevWarpedDepth"
+ "intermediateProjectedJasperToPrimaryDepthMap"
+ "intermediateProjectedJasperToSecondaryDepthMap"
+ "intermediateProjectedPearlToPrimary"
+ "intermediateProjectedPearlToSecondary"
+ "intermediateScaledCalibration"
+ "intermediateSecondaryColorCalibration"
+ "intermediatepointCloudCropped"
+ "intermediatepovChangedPointCloud"
+ "interpolateDownscaledDxDyForNonIntegerCoordinate"
+ "intervalBetweenIFAFrames"
+ "inv_depth"
+ "invalid input buffer size (expected: %fx%f, got %zux%zu)"
+ "irCamFOVCoveragePercent"
+ "irSensorCalibration"
+ "isAssignedGMCJBlock"
+ "isAssignedGMCJValidation"
+ "isAssignedIFABlock"
+ "isAssignedJasperReflectionsFrameFilter"
+ "isAssignedPipelineCurrent"
+ "isAssignedPipelinePrevious"
+ "isReadyForExecution"
+ "isReportTelemetry"
+ "jasper"
+ "jasperBankPose"
+ "jasperColorInFieldSDFHistorySize"
+ "jasperColorRemoveShortRangeOccludedPointsOnLargeBaselineDevices"
+ "jasperInputSpotCount"
+ "jasperMisalignmentAfter"
+ "jasperMisalignmentBefore"
+ "jasperPearlFrameTemperature"
+ "jasperPearlInFieldCalibrationInputJasper"
+ "jasperPearlInFieldCalibrationInputPearlDepth"
+ "jasperPearlInFieldCalibrationInputPearlDx"
+ "jasperPearlInFieldCalibrationInputPearlDy"
+ "jasperPearlInFieldCalibrationInputPearlScore"
+ "jasperPearlInFieldCalibrationJasperAggReprojected"
+ "jasperPearlInFieldMaxJasperGlareSpots"
+ "jasperPearlInFieldMaxJasperReflectiveSpots"
+ "jasperPearlInFieldMaxRotationBetweenFrames"
+ "jasperPearlInFieldMaxTranslationBetweenFrames"
+ "jasperPearlInFieldMinRotationBetweenFrames"
+ "jasperPearlInFieldMinTranslationBetweenFrames"
+ "jasperPoseDistance"
+ "jasperProjectedSpotCount"
+ "jasperToPearlTransform"
+ "jasper_features_bundle"
+ "jpcErrorCode"
+ "jpc_efl_temp_coeff"
+ "jpc_last_algo_radar_trigger"
+ "jpc_last_pearl_temp"
+ "jpc_last_rotation"
+ "jpc_last_translation"
+ "jpc_ppX"
+ "jpc_ppY"
+ "jpc_rotX"
+ "jpc_rotY"
+ "jpc_rotZ"
+ "jpc_telemetry_first_time_event_fired"
+ "labels"
+ "lastAlgoRadarTriggerTimestamp"
+ "lastFrameStatistics"
+ "lastIFAFrameTimestampCurrentExecution"
+ "lastPearlTemp"
+ "lkt_bgra2gray"
+ "lkt_compute_confidence"
+ "lkt_downscale_input"
+ "logJPCInputs:"
+ "logJasperAggPC:timestamp:"
+ "logJpcInputData:"
+ "logPose:logMessagePrefix:"
+ "loggingForceCounterAsTimestamp"
+ "longRange"
+ "m_rows == mat.Rows()"
+ "makeRunnable"
+ "maxCenterResolution"
+ "maxIRCamTemperature"
+ "maxIRCamTemperatureCurrentExecution"
+ "maxJasperDepth"
+ "maxRaysResolution"
+ "memory allocation failed"
+ "meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:"
+ "meshChunkWithVertices:faces:confidence:classification:transform:uuid:timestamp:longRange:"
+ "meshChunkWithVertices:faces:confidence:classification:uuid:timestamp:"
+ "meshChunkWithVertices:faces:confidence:classification:uuid:timestamp:longRange:"
+ "meshChunkWithVerticesBuffer:verticesCount:verticesOffset:verticesStride:facesBuffer:facesCount:facesOffset:facesStride:uuid:timestamp:"
+ "meshChunks"
+ "meshKeyframes"
+ "metal execution"
+ "metalDescriptor"
+ "metric depth"
+ "metric depth executor deallocated"
+ "metric depth executor: preparing metric depth for roi: [%f,%f,%f,%f] - engine: %lu"
+ "metric depth pipeline failed to init "
+ "metric depths executor: preparing executor"
+ "metricDepth"
+ "metricDepth reducing medium confidence due to device roll angle"
+ "metricDepthActiveMaskMode"
+ "metricDepthEmulatePeridot"
+ "metricDepthGraphJPEGDumpPath"
+ "metricDepthIgnoreActiveSensors"
+ "metricDepthPearlJasperCoFilteringMaxAllowedDisagreement"
+ "metricDepthPearlJasperCoFilteringMaxPearlDepth"
+ "minIRCamTemperature"
+ "minIRCamTemperatureCurrentExecution"
+ "modelBuilderForModelPath:destinationPath:buildConfigPath:forANE:"
+ "modelInputColor"
+ "modelInputColorCameraEmbeddings"
+ "modelInputJasperEmbeddings"
+ "modelInputPearlBuffer"
+ "modelInputProjectedPearl"
+ "modelInputProjectedPointCloud"
+ "modelInputSecondaryColor"
+ "modelOutputDepth"
+ "modelOutputNormals"
+ "modelOutputUncertainty"
+ "motionBetweenFramesRotationX"
+ "motionBetweenFramesRotationY"
+ "motionBetweenFramesRotationZ"
+ "motionBetweenFramesTranslationX"
+ "motionBetweenFramesTranslationY"
+ "motionBetweenFramesTranslationZ"
+ "must provide output depth pointer"
+ "mutableBytes"
+ "mutableConfidences"
+ "mutablePoints"
+ "network confidence threshold: %@"
+ "network inputs: %@"
+ "network outputs: %@"
+ "newEfl"
+ "newPPX"
+ "newPPY"
+ "newRotX"
+ "newRotY"
+ "newRotZ"
+ "newSharedEvent"
+ "non-triangle vertices not supported"
+ "nonRunnableProviderForNetwork:"
+ "nonRunnableProviderForNetwork:espressoEngine:"
+ "nonRunnableProviderForNetwork:requestedLayouts:"
+ "normals postprocess buffer cannot be null: %p,%p"
+ "notifyNewFrameArrived:temperature:"
+ "notifyTriggeringSessionEnded"
+ "nullptr != m_dataPtr"
+ "nullptr != m_pixelBuffer"
+ "numCenterBands"
+ "numDynamicPixels"
+ "numJasperBands"
+ "numJasperSpotsFlaggedAsGlare"
+ "numJasperSpotsFlaggedAsReflectiveSurface"
+ "numOfAggregatedFrames"
+ "numOfIFAFramesCurrentExecution"
+ "numOfUniqueTOFSpots"
+ "numPearlJasperCorrespondencesPostLocalDepthVarFilter"
+ "numPearlJasperCorrespondencesPostPJDepthDiffFilter"
+ "numPearlJasperCorrespondencesPostPJWorkDistOverlapFilter"
+ "numPearlJasperCorrespondencesPreIFA"
+ "numPearlOnlyCorrespondencesPostSpatialCoverageFilter"
+ "numPearlOnlyCorrespondencesPreIFA"
+ "numRaysBands"
+ "numberWithShort:"
+ "numberWithUnsignedShort:"
+ "occlusionForPrimaryPoV"
+ "occlusionForSecondaryPoV"
+ "offset"
+ "only YUV 8 bit full range supported"
+ "out_flow_matching_x4"
+ "out_pred"
+ "out_recurrent"
+ "output pixel format does not match descriptor"
+ "outputActiveDepthMask"
+ "outputActiveDepthMaskDescriptor"
+ "outputCalibration"
+ "outputConfidence"
+ "outputConfidenceDescriptor"
+ "outputConfidenceLevelsDescriptor"
+ "outputConfideneLevels"
+ "outputDepthCalibration"
+ "outputDepthDescriptor"
+ "outputDescriptor"
+ "outputNormals"
+ "outputNormalsDescriptor"
+ "outputOpticalFlow"
+ "outputSizeForLayout:"
+ "outputWithAuxDepth:auxConfidence:auxSegmentation:auxOutputCalibration:"
+ "outputWithDepthForPrimaryPoV:depthForSecondaryPoV:"
+ "outputWithDepthForPrimaryPoV:depthForSecondaryPoV:confidenceForPrimaryPoV:confidenceForSecondaryPoV:occlusionForPrimaryPoV:occlusionForSecondaryPoV:"
+ "overrideCVCalIntrinsicsWithPCECalibIntrinsics:temperature:"
+ "overrideDeviceName"
+ "params.consts.shouldIncludeJasperResidualFunction || 0 == numberOfPearlJasperCorrespondences"
+ "pce"
+ "pceCalib"
+ "pearlCalibSetSize"
+ "pearlDepth"
+ "pearlDx"
+ "pearlDy"
+ "pearlInfraredCameraCalibration"
+ "pearlInputs.depth"
+ "pearlJapserCalibSetSize"
+ "pearlJasperCoFilteringMaxAllowedDisagreement"
+ "pearlJasperCoFilteringMaxPearlDepth"
+ "pearlProjectedPixelCount"
+ "pearlProjectedPixelPercentage"
+ "pearlReprojector"
+ "pearlScore"
+ "pearlTemperature"
+ "pearlToLastJasperBankRotation"
+ "pearlToLastJasperBankRotationX"
+ "pearlToLastJasperBankRotationY"
+ "pearlToLastJasperBankRotationZ"
+ "pearlToLastJasperBankTranslation"
+ "pearlToLastJasperBankTranslationX"
+ "pearlToLastJasperBankTranslationY"
+ "pearlToLastJasperBankTranslationZ"
+ "pickDxDySamplePointsForInterpolation"
+ "pixelBufferFromData"
+ "pixelBufferFromData:width:height:pixelFormat:"
+ "pixelBufferToData"
+ "pixelBufferToData:"
+ "plane %zu has unsupported component size (%zu/%zu)"
+ "point cloud"
+ "pointCloudAggregationParameters"
+ "pointCloudByChangingPointOfViewFrom:to:"
+ "pointCloudByRemovingPeridotShortRangeOccludedPoints:"
+ "points"
+ "postProcessDisparity:outputDepth:"
+ "postProcessEspressoConfidence:outputConfidence:"
+ "postProcessEspressoConfidence:outputConfidence:confidenceUnits:"
+ "postProcessEspressoDepth:espressoConfidence:espressoNormals:toOutputDepth:outputConfidence:outputNormals:"
+ "postProcessEspressoDepth:espressoConfidence:toOutputDepth:outputConfidence:"
+ "postProcessEspressoNormals:toOutputNormals:"
+ "postprocess buffer dimensions must match: %lu,%lu"
+ "postprocess mask"
+ "postprocess normals"
+ "postprocess pixel formats must match pipeline descriptors: %u,%u"
+ "postprocess pixel formats not supported: %u,%u"
+ "povcDimensions"
+ "pred_error:0"
+ "pred_value:0"
+ "prediction"
+ "prediction encode"
+ "predictsDisparity"
+ "preferencesWithDefaultValues:"
+ "preparation of stereo warp meshes failed"
+ "prepareForInputRoi:"
+ "prepareForInputRoi:engineType:"
+ "prepareStereoWarpMeshesWithRefCalib:auxCalib:"
+ "preprocess metal inputs"
+ "preprocessPearlDepth:pearlPose:pearlCalibration:colorPose:colorCalibration:outputBuffer:"
+ "prevEfl"
+ "prevPPX"
+ "prevPPY"
+ "prevPose"
+ "prevRotX"
+ "prevRotY"
+ "prevRotZ"
+ "prev_conf"
+ "prev_depth"
+ "prev_depth_features"
+ "prev_flow_features"
+ "prev_inv_depth"
+ "prev_prediction"
+ "prev_rgb"
+ "prev_rgb_features"
+ "primary color"
+ "primaryColorCalibration"
+ "primaryColorCameraCalibration"
+ "primaryColorCameraCalibration property set to nil. this may indicate incorrect usage."
+ "primaryColorImage"
+ "primaryColorImageProcessed"
+ "primaryColorInput"
+ "primaryConfOutputPrediction"
+ "primaryDepthPrediction"
+ "primaryDisparityCalibration"
+ "primaryDisparityCalibration property set to nil. this may indicate incorrect usage."
+ "primaryOcclusionMapOutput"
+ "primaryPoVCameraCalibration"
+ "primaryPredictionConfidenceOutput"
+ "primaryPredictionOutput"
+ "primaryRasterizedMeshInput"
+ "primaryTargetCameraCalibration"
+ "primaryTargetCameraCalibration is deprecated."
+ "principalPointX"
+ "principalPointY"
+ "printOutResults:"
+ "processFrame:validBufferRect:intoOpticalFlowBuffer:outputConfidence:"
+ "processJpcResult:"
+ "processJpcResultWithStatus:gmcjResult:glaResult:result:interSessionData:temperature:eflTempCoeff:"
+ "processMatch:"
+ "processWithPearl:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:"
+ "processedAuxColor"
+ "processedAuxConfidence"
+ "processedAuxDepth"
+ "processedRefColor"
+ "projectedPearlToSecondary"
+ "providerForNetwork:requestedLayouts:espressoEngine:makeRunnable:"
+ "providerForNetwork:requestedLayouts:makeRunnable:"
+ "pts1.GetNumOfPoints() - testSetSize == newPts1->GetNumOfPoints()"
+ "pushData:streamIndex:timestamp:pose:meta:"
+ "pushJasperPointCloud:timestamp:pose:jasperToPearlOperationalTransform:"
+ "pushJasperPointCloud:timestamp:pose:jasperToPearlTransform:"
+ "pushKeyframes:"
+ "pushMesh:"
+ "pushPearlDepth:pearlDx:pearlDy:pearlScore:timestamp:metadata:pose:prevPose:"
+ "pushPearlDepth:pearlDx:pearlDy:pearlScore:timestamp:pose:pearlSensorCalibration:"
+ "pushPearlDepth:timestamp:pose:temperature:irSensorOperationalCalibration:"
+ "pushPointCloud:timestamp:worldToCameraTransform:"
+ "pushPrimaryColor"
+ "pushPrimaryColorImage:timestamp:pose:"
+ "pushSecondaryColor"
+ "pushSecondaryColor:pose:calibration:timestamp:"
+ "pushSecondaryColorImage:timestamp:pose:"
+ "pushed primary color image for ts:%f while calib is: %p"
+ "pushed secondary color but preset do not support stereo"
+ "pushed secondary color image for ts:%f while calib is: %p"
+ "pyramids encode"
+ "q108@0:8^{__CVBuffer=}16d24{?=[4]}32f96@100"
+ "q112@0:8@16@24@32@40@48@56{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104"
+ "q128@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40d48{?=[4]}56@120"
+ "q128@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40{?=[4]}48@112@120"
+ "q136@0:8^{__CVBuffer=}16@24{?=[4]}32@96@104^{?=[4]}112^^{__CVBuffer}120^^{__CVBuffer}128"
+ "q144@0:8^{__CVBuffer=}16@24{?=[4]}32@96^{__CVBuffer=}104^{__CVBuffer=}112^{__CVBuffer=}120^{__CVBuffer=}128^{__CVBuffer=}136"
+ "q156@0:8@16@24@32@40@48^{__CVBuffer=}56^{__CVBuffer=}64d72{?=[4]}80Q144i152"
+ "q160@0:8@16d24{?=[4]}32{?=[4]}96"
+ "q160@0:8^{__CVBuffer=}16@24{?=[4]}32@96@104^{?=[4]}112^^{__CVBuffer}120^^{__CVBuffer}128^{__CVBuffer=}136^{__CVBuffer=}144^{__CVBuffer=}152"
+ "q168@0:8@16@24{?=[4]}32{?=[4]}96@160"
+ "q176@0:8^{__CVBuffer=}16{?=[4]}24@88{?=[4]}96@160@168"
+ "q184@0:8@16@24{?=[4]}32@96{?=[4]}104@168@176"
+ "q192@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40d48@56{?=[4]}64{?=[4]}128"
+ "q196@0:8^v16i24@28@36{?=[4]}44@108{?=[4]}116@180@188"
+ "q208@0:8@16^{?=[4]}24^d32{?=[4]}40^{__CVBuffer=}104{?=[4]}112@176^@184^{?=[4]}192^d200"
+ "q24@0:8^{__CVBuffer=}16"
+ "q24@0:8d16"
+ "q32@0:8@16^@24"
+ "q32@0:8@16^{__CVBuffer=}24"
+ "q32@0:8@16d24"
+ "q344@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40@48@56@64@72{?=[4]}80{?=[4]}144{?=[4]}208^{?=[4]}272d280^^{__CVBuffer}288^^{__CVBuffer}296^^{__CVBuffer}304^^{__CVBuffer}312^^{__CVBuffer}320^^{__CVBuffer}328^@336"
+ "q36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
+ "q48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^^{__CVBuffer}32^^{__CVBuffer}40"
+ "q52@0:8^{__CVBuffer=}16@24^{__CVBuffer=}32B40^{CGRect={CGPoint=dd}{CGSize=dd}}44"
+ "q56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^^{__CVBuffer}32^^{__CVBuffer}40d48"
+ "q56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16Q48"
+ "q64@0:8I16^v20^v28@36@44f52[2d]56"
+ "q64@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56"
+ "q64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56"
+ "q72@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56^@64"
+ "q72@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56d64"
+ "q72@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24^{__CVBuffer=}56^{__CVBuffer=}64"
+ "q76@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56f64Q68"
+ "q80@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32q64@72"
+ "q80@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56@64Q72"
+ "q80@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56^@64d72"
+ "q80@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56^^{__CVBuffer}64^@72"
+ "q80@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32^{__CVBuffer=}64^{__CVBuffer=}72"
+ "q88@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@64@72@80"
+ "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^^{__CVBuffer}48^^{__CVBuffer}56^^{__CVBuffer}64^@72d80"
+ "q88@0:8^{__CVBuffer=}16d24@32@40@48@56^^{__CVBuffer}64^^{__CVBuffer}72^@80"
+ "q96@0:8^{__CVBuffer=}16d24{?=[4]}32"
+ "q96@0:8d16{?=[4]}24@88"
+ "r^{PCECalib=is[2C][16C]{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibExtrinsics=[3[3d]]{PCECalibVector=ddd}}{PCECalibProjector={PCECalibVector=ddd}}{PCECalibReferencePlane=d{PCECalibVector=ddd}}ss[4C]dd[2d]d[2d][2d]d[2d]{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibExtrinsics=[3[3d]]{PCECalibVector=ddd}}{PCECalibRotationAngles=ddd}}16@0:8"
+ "rawAuxConfidence"
+ "rawAuxDisparity"
+ "rawAuxSegmentation"
+ "readJsonMetadataFile:requestedLayouts:"
+ "rectifiedCameraFieldOfViewHeight"
+ "rectifiedCameraFieldOfViewWidth"
+ "rectifyCameraPairForLeftCalib:rightCalib:leftRectifiedCameraToPlatformTransform:rightRectifiedCameraToPlatformTransform:prioritization:"
+ "recurrent"
+ "refRectifiedCalib"
+ "referenceColorInput"
+ "removeChunkWithUUID:"
+ "removeKeyframeWithUUID:"
+ "removeObject:"
+ "removedMeshChunkWithUuid:timestamp:"
+ "removedMeshChunkWithUuid:timestamp:longRange:"
+ "reportTelemetry:firstTimeEvent:"
+ "reportTriggeringTelemetry:"
+ "reprojectionErrorAfter"
+ "reprojectionErrorBefore"
+ "requestedDimensions"
+ "resetIFAObjects"
+ "resetSdfHistory"
+ "resetState"
+ "returning ADVisualDepthOutput %p"
+ "rgb"
+ "rgb_aux"
+ "rgb_features"
+ "rgb_images"
+ "rgb_ref"
+ "rotArray"
+ "rotateConfidenceAllowPixelFormatChange:rotation:outputConfidence:"
+ "runWithJpc:runMode:pearlInputs:jasperAggregatedPointCloud:farthestJasperBankPose:irSensorCalibration:jasperToPearlTransform:interSessionData:result:"
+ "runnableModelPath"
+ "running visual depth"
+ "s"
+ "s16@0:8"
+ "saturationCheckInterval"
+ "saturationThreshold"
+ "scaleIdxForConfidenceComponents"
+ "score"
+ "sdfHistorySize"
+ "secondary color"
+ "secondaryColorCalibration"
+ "secondaryColorCameraCalibration"
+ "secondaryColorCameraCalibration property set to nil. this may indicate incorrect usage."
+ "secondaryColorImage"
+ "secondaryColorImageProcessed"
+ "secondaryColorInput"
+ "secondaryConfOutputPrediction"
+ "secondaryDepthPrediction"
+ "secondaryDisparityCalibration"
+ "secondaryDisparityCalibration property set to nil. this may indicate incorrect usage."
+ "secondaryOcclusionMapOutput"
+ "secondaryPoVCameraCalibration"
+ "secondaryPredictionConfidenceOutput"
+ "secondaryPredictionOutput"
+ "secondaryRasterizedMeshInput"
+ "secondaryTargetCameraCalibration"
+ "secondaryTargetCameraCalibration is deprecated."
+ "self.pceCalib"
+ "sendAnalyticsWithRefSaturationRate:auxSaturationRate:"
+ "setAggData:"
+ "setAggPoints:"
+ "setAggPointsWrapperObj:"
+ "setAllPosesValid:"
+ "setAutoSetColorROI:"
+ "setBankPointCloud:"
+ "setBuffer:"
+ "setCaCurrentTriggerEndReasonIsConvergence:"
+ "setCaCurrentTriggerEndReasonIsMaxFrameCount:"
+ "setCaCurrentTriggerEndReasonIsOutputValidationMetricIncreased:"
+ "setCaCurrentTriggerFirstFrameTemperature:"
+ "setCaCurrentTriggerFirstFrameTimestamp:"
+ "setCaCurrentTriggerFrameCount:"
+ "setCaCurrentTriggerLastFrameTemperature:"
+ "setCaCurrentTriggerLastFrameTimestamp:"
+ "setCaLastTriggerLastFrameTemperature:"
+ "setCaLastTriggerLastFrameTimestamp:"
+ "setCalibration:"
+ "setCheckFlowInFOV:"
+ "setClassification:"
+ "setColorInput:calib:toNetworkBuffer:isRef:crop:"
+ "setColorPoseRoll:"
+ "setConditionNumberMaxValue:"
+ "setConditionNumberMinValue:"
+ "setConfidenceParameters:"
+ "setCoreAnalyticsEventInterval:"
+ "setCount:"
+ "setDepthDiffThresholdAboveMedian:"
+ "setDepthSensorsIgnored:"
+ "setDuplicateProjectedSpotsMode:"
+ "setDx:"
+ "setDy:"
+ "setEfl:"
+ "setFaces:"
+ "setFilter:"
+ "setFirstIFAFrameTimestampCurrentExecution:"
+ "setFirstTimeEventFired:"
+ "setForceCounterAsTimestamp:"
+ "setGMCJResult:result:temperature:"
+ "setGmcjErrorCode:"
+ "setGmcjOutputValidationErrorCode:"
+ "setGmcjPPXChangeMicronFromPrev:"
+ "setGmcjPPXChangeMicronFromT0:"
+ "setGmcjPPYChangeMicronFromPrev:"
+ "setGmcjPPYChangeMicronFromT0:"
+ "setGmcjProjRotXChangeFromPrev:"
+ "setGmcjProjRotXChangeFromT0:"
+ "setGmcjProjRotYChangeFromPrev:"
+ "setGmcjProjRotYChangeFromT0:"
+ "setGmcjProjRotZChangeFromPrev:"
+ "setGmcjProjRotZChangeFromT0:"
+ "setGmcjScaleChangePercentFromPrev:"
+ "setGmcjScaleChangePercentFromT0:"
+ "setGradientNormMaxValue:"
+ "setGradientNormMinValue:"
+ "setIgnoreDistortionInDepthReprojection:"
+ "setImage:"
+ "setIntervalBetweenIFAFrames:"
+ "setIrCamFOVCoveragePercent:"
+ "setIsAssignedGMCJBlock:"
+ "setIsAssignedGMCJValidation:"
+ "setIsAssignedIFABlock:"
+ "setIsAssignedJasperReflectionsFrameFilter:"
+ "setIsAssignedPipelineCurrent:"
+ "setIsAssignedPipelinePrevious:"
+ "setIsReportTelemetry:"
+ "setJasperBankPose:"
+ "setJasperInputSpotCount:"
+ "setJasperMisalignmentAfter:"
+ "setJasperMisalignmentBefore:"
+ "setJasperPoseDistance:"
+ "setJasperProjectedSpotCount:"
+ "setJasperToCameraTransform:"
+ "setJpcErrorCode:"
+ "setLabel:"
+ "setLabels:"
+ "setLastAlgoRadarTriggerTimestamp:"
+ "setLastIFAFrameTimestampCurrentExecution:"
+ "setLastPearlTemp:"
+ "setLongRange:"
+ "setMaxCenterResolution:"
+ "setMaxIRCamTemperature:"
+ "setMaxIRCamTemperatureCurrentExecution:"
+ "setMaxJasperDepth:"
+ "setMaxRaysResolution:"
+ "setMetricDepth:"
+ "setMinIRCamTemperature:"
+ "setMinIRCamTemperatureCurrentExecution:"
+ "setMotionBetweenFramesRotationX:"
+ "setMotionBetweenFramesRotationY:"
+ "setMotionBetweenFramesRotationZ:"
+ "setMotionBetweenFramesTranslationX:"
+ "setMotionBetweenFramesTranslationY:"
+ "setMotionBetweenFramesTranslationZ:"
+ "setNewEfl:"
+ "setNewPPX:"
+ "setNewPPY:"
+ "setNewRotX:"
+ "setNewRotY:"
+ "setNewRotZ:"
+ "setNumCenterBands:"
+ "setNumJasperBands:"
+ "setNumJasperSpotsFlaggedAsGlare:"
+ "setNumJasperSpotsFlaggedAsReflectiveSurface:"
+ "setNumOfAggregatedFrames:"
+ "setNumOfIFAFramesCurrentExecution:"
+ "setNumOfUniqueTOFSpots:"
+ "setNumPearlJasperCorrespondencesPostLocalDepthVarFilter:"
+ "setNumPearlJasperCorrespondencesPostPJDepthDiffFilter:"
+ "setNumPearlJasperCorrespondencesPostPJWorkDistOverlapFilter:"
+ "setNumPearlJasperCorrespondencesPreIFA:"
+ "setNumPearlOnlyCorrespondencesPostSpatialCoverageFilter:"
+ "setNumPearlOnlyCorrespondencesPreIFA:"
+ "setNumRaysBands:"
+ "setOffset:"
+ "setPceCalib:"
+ "setPearlCalibSetSize:"
+ "setPearlDepth:"
+ "setPearlDx:"
+ "setPearlDy:"
+ "setPearlInfraredCameraCalibration:"
+ "setPearlJapserCalibSetSize:"
+ "setPearlJasperCoFilteringMaxAllowedDisagreement:"
+ "setPearlJasperCoFilteringMaxPearlDepth:"
+ "setPearlProjectedPixelCount:"
+ "setPearlProjectedPixelPercentage:"
+ "setPearlScore:"
+ "setPearlTemperature:"
+ "setPearlToLastJasperBankRotation:"
+ "setPearlToLastJasperBankRotationX:"
+ "setPearlToLastJasperBankRotationY:"
+ "setPearlToLastJasperBankRotationZ:"
+ "setPearlToLastJasperBankTranslation:"
+ "setPearlToLastJasperBankTranslationX:"
+ "setPearlToLastJasperBankTranslationY:"
+ "setPearlToLastJasperBankTranslationZ:"
+ "setPointCloudAggregationParameters:"
+ "setPose:"
+ "setPrevEfl:"
+ "setPrevPPX:"
+ "setPrevPPY:"
+ "setPrevPose:"
+ "setPrevRotX:"
+ "setPrevRotY:"
+ "setPrevRotZ:"
+ "setPrimaryColorCameraCalibration:"
+ "setPrimaryDisparityCalibration:"
+ "setPrimaryTargetCameraCalibration:"
+ "setPrincipalPointX:"
+ "setPrincipalPointY:"
+ "setRectifiedCameraFieldOfViewHeight:"
+ "setRectifiedCameraFieldOfViewWidth:"
+ "setReprojectionErrorAfter:"
+ "setReprojectionErrorBefore:"
+ "setRequestedDimensions:"
+ "setRotArray:"
+ "setSaturationCheckInterval:"
+ "setSaturationThreshold:"
+ "setScaleIdxForConfidenceComponents:"
+ "setScore:"
+ "setSecondaryColorCameraCalibration:"
+ "setSecondaryDisparityCalibration:"
+ "setSecondaryTargetCameraCalibration:"
+ "setSkipISF:"
+ "setStepsToExecute:"
+ "setStride:"
+ "setTelemetryData:"
+ "setTemperature:"
+ "setTimestamp:"
+ "setTransArray:"
+ "setTransform:"
+ "setTriggeringEndReason:triggerEndReasonIsMaxFrameCount:triggerEndReasonIsValidationMetricIncreased:"
+ "setUuid:"
+ "setVertices:"
+ "shouldExecuteForTimestamp:poseMillimeters:"
+ "shouldExecuteWithInterSessionDataRun:"
+ "shouldIncludeJasperResidualFunction || 0 == numOfJasperCorrespondences"
+ "shouldIncludeJasperResidualFunction || 0 == numberOfPearlJasperCorrespondences"
+ "singleAxisDistance > 0"
+ "skew:"
+ "skipISF"
+ "solver encode"
+ "srcLengthBytes % sizeof(double) == 0"
+ "status == 0"
+ "stepsToExecute"
+ "stride"
+ "stringWithContentsOfFile:encoding:error:"
+ "supportedDimensionsForInput:expectedPixelFormat:"
+ "telemetryData"
+ "temperature"
+ "temporal_smoothness_k1"
+ "temporal_smoothness_k2"
+ "textureForSize:pixelFormat:mipmapped:metalDevice:"
+ "timeIntervalSince1970"
+ "transArray"
+ "transform"
+ "undistort:distortedPixels:outUndistorted:"
+ "undistortColorImage:undistortedImage:"
+ "undistortedRadii"
+ "unexpected number of planes %lu"
+ "unexpected pixel format type for image output (%u)"
+ "unexpected plane size"
+ "unsignedIntegerValue"
+ "unsupported prioritization for Binocular pipeline: %@"
+ "updatePixelBufferAllocationForImageDescriptor:pixelBuffer:"
+ "updateSceneMonitoringForTimestamp:"
+ "updateTimestampWithOverride:"
+ "updateWarper:source:target:"
+ "updateWithSource:target:"
+ "updating primary color calibration"
+ "updating primary disparity calibration"
+ "updating secondary color calibration"
+ "updating secondary disparity calibration"
+ "uuid"
+ "v "
+ "v %f %f %f\n"
+ "v104@0:8^{__CVBuffer=}16{?=[4]}24@\"ADCameraCalibration\"88d96"
+ "v104@0:8^{__CVBuffer=}16{?=[4]}24@88d96"
+ "v20@0:8s16"
+ "v24@0:8^d16"
+ "v24@0:8^{JpcInputData={PearlInputs=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}{?=[4]}{?=[4]}Q}{JasperInputs=@{?=[4]}}{CalibrationInputs={PearlCalibrations={PearlPCEConfig=fffff{PearlInvalidValues=CS}}{IRSensorCalibrations=@[2d]}{IRSensorCalibrations=@[2d]}{IRProjectorCalibrations={?=[4]}}{IRProjectorCalibrations={?=[4]}}{PearlReferenceWallCalibrations=d}}{JasperCalibrations={?=[4]}}}{DeviceStateInputs=f}}16"
+ "v24@0:8f16f20"
+ "v28@0:8@16I24"
+ "v28@0:8B16B20B24"
+ "v28@0:8d16f24"
+ "v32@0:8@16^^{__CVBuffer}24"
+ "v32@0:8@16^{PCECalib=is[2C][16C]{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibExtrinsics=[3[3d]]{PCECalibVector=ddd}}{PCECalibProjector={PCECalibVector=ddd}}{PCECalibReferencePlane=d{PCECalibVector=ddd}}ss[4C]dd[2d]d[2d][2d]d[2d]{PCECalibCameraIntrinsics=dd[2d][256d][256d][8d][8d]SS[4C]}{PCECalibExtrinsics=[3[3d]]{PCECalibVector=ddd}}{PCECalibRotationAngles=ddd}}24"
+ "v36@0:8@16[2d]24f32"
+ "v36@0:8r^v16@24f32"
+ "v40@0:8@16@24d32"
+ "v56@0:8@16@24^{?=[4]}32^{?=[4]}40q48"
+ "v64@0:8@16@24@32@40@4856"
+ "v64@0:8{AggregatedData={vector<jpc::IIFABlock::IFAPearlJasperCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlJasperCorrespondence>>=^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}}{vector<jpc::IIFABlock::IFAPearlCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlCorrespondence>>=^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}}}16"
+ "v72@0:8@16d24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56^{__CVBuffer=}64"
+ "v88@0:8{?=[4]}16@80"
+ "validBufferRect is larger input size"
+ "validBufferRect is larger than input size"
+ "validBufferRect origin is different than (0,0)"
+ "validDepthRect"
+ "vertex "
+ "vertices"
+ "visual depth executor deallocated"
+ "visual depth executor reinitialization required: XTheta projection changed"
+ "visual depth executor reinitialization required: distortion type changed"
+ "visual depth executor reinitialization required: no prev calib"
+ "visual depth executor: preparing executor"
+ "visual depth executor: preparing executor for visual depth roi: [%f,%f,%f,%f]"
+ "visual depth not supported in this build"
+ "visual depth pipeline deallocated"
+ "visual depth pipeline failed to init for preset"
+ "visual depth: running visual depth for timestamp:%f"
+ "visualDepth-completion-event"
+ "visualDepthFovScale"
+ "visualDepthMeshRenderRatio"
+ "visualDepthMinLevel"
+ "visualDepthOcclusionScale"
+ "visualDepthOutputDisparity"
+ "waitUntilSignaledValue:timeoutMS:"
+ "warpImage:processedImage:isRef:"
+ "warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingOpticalFlow:"
+ "warpPreviousDepth:intoCurrentDepth:previousConfidence:intoCurrentConfidence:usingPoseDelta:previousCalibration:currentCalibration:"
+ "writeMetricDepthToJPEG:timestamp:preProcessedJasper:preProcessedPearl:preProcessedPrimaryColor:rawConfOut:rawDepthOut:"
+ "writing metricDepth debug images to %@"
+ "x < getWidth()"
+ "y < getHeight()"
+ "yuv_l"
+ "yuv_r"
+ "zeroing confidence due to invalid pose inputs"
+ "zeroing point clouds due to invalid pose inputs"
+ "{?=\"scales\"Q\"nwarpings\"@\"NSMutableArray\"\"useNonLocalRegularization\"B\"nlreg_radius\"i\"nlreg_padding\"i\"nlreg_sigma_l\"f\"nlreg_sigma_c\"f\"nlreg_sigma_w\"f\"downscaleToWidth\"Q\"firstScaleStride\"I}"
+ "{?=IIiIBB    }48@0:8@16@2432I40B44"
+ "{?=Q@BiifffQI}16@0:8"
+ "{AggregatedData=\"pearlJasperCorrespondences\"{vector<jpc::IIFABlock::IFAPearlJasperCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlJasperCorrespondence>>=\"__begin_\"^{IFAPearlJasperCorrespondence}\"__end_\"^{IFAPearlJasperCorrespondence}\"__cap_\"^{IFAPearlJasperCorrespondence}}\"pearlCorrespondences\"{vector<jpc::IIFABlock::IFAPearlCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlCorrespondence>>=\"__begin_\"^{IFAPearlCorrespondence}\"__end_\"^{IFAPearlCorrespondence}\"__cap_\"^{IFAPearlCorrespondence}}}"
+ "{AggregatedData={vector<jpc::IIFABlock::IFAPearlJasperCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlJasperCorrespondence>>=^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}^{IFAPearlJasperCorrespondence}}{vector<jpc::IIFABlock::IFAPearlCorrespondence, std::allocator<jpc::IIFABlock::IFAPearlCorrespondence>>=^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}^{IFAPearlCorrespondence}}}16@0:8"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8^{__CVBuffer=}16@24"
+ "{PixelBufferSharedPtr=\"_vptr$PixelBufferSharedPtr\"^^?\"m_pixelBuffer\"^{__CVBuffer}}"
+ "{maps_uv=\"map_u\"^f\"map_v\"^f\"mapping\"^{vImageMapping}}"
+ "{unique_ptr<DisparityToDepth::DisparityToDepthFitEstimator, std::default_delete<DisparityToDepth::DisparityToDepthFitEstimator>>=\"__ptr_\"^{DisparityToDepthFitEstimator}}"
+ "{unique_ptr<DisparityToDepth::Ransac<float, float>, std::default_delete<DisparityToDepth::Ransac<float, float>>>=\"__ptr_\"^v}"
+ "{unique_ptr<DisparityToDepth::RansacLine2DModel, std::default_delete<DisparityToDepth::RansacLine2DModel>>=\"__ptr_\"^{RansacLine2DModel}}"
+ "{unique_ptr<DisparityToDepth::RansacLineModel, std::default_delete<DisparityToDepth::RansacLineModel>>=\"__ptr_\"^{RansacLineModel}}"
+ "{unique_ptr<DisparityToDepth::WorldPointsContainer, std::default_delete<DisparityToDepth::WorldPointsContainer>>=\"__ptr_\"^{WorldPointsContainer}}"
+ "{unique_ptr<PixelBufferUtilsSession, std::default_delete<PixelBufferUtilsSession>>=\"__ptr_\"^{PixelBufferUtilsSession}}"
+ "{unique_ptr<jpc::JPC, std::default_delete<jpc::JPC>>=^{JPC}}28@0:8i16^B20"
+ "{unique_ptr<std::vector<std::vector<float>>[], std::default_delete<std::vector<std::vector<float>>[]>>=\"__ptr_\"^v}"
+ "{unordered_map<unsigned long, ADCameraCalibration *, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, ADCameraCalibration *>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, ADCameraCalibration *>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, ADCameraCalibration *>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, ADCameraCalibration *>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, CGSize, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, CGSize>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, CGSize>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, CGSize>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, CGSize>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, CGSize>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, CGSize>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, PixelBufferSharedPtr, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, PixelBufferSharedPtr>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, PixelBufferSharedPtr>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, simd_float4x4, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, simd_float4x4>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, simd_float4x4>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, simd_float4x4>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, simd_float4x4>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, simd_float4x4>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, simd_float4x4>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{unordered_map<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>, std::hash<unsigned long>, std::equal_to<unsigned long>, std::allocator<std::pair<const unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::__unordered_map_hasher<unsigned long, std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::hash<unsigned long>, std::equal_to<unsigned long>>, std::__unordered_map_equal<unsigned long, std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, std::equal_to<unsigned long>, std::hash<unsigned long>>, std::allocator<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long, std::vector<float __attribute__((ext_vector_type(3)))>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
+ "{vector<ADDisparityToDepthFitWorldPoint, std::allocator<ADDisparityToDepthFitWorldPoint>>=\"__begin_\"^{ADDisparityToDepthFitWorldPoint}\"__end_\"^{ADDisparityToDepthFitWorldPoint}\"__cap_\"^{ADDisparityToDepthFitWorldPoint}}"
+ "{vector<ADJasperPearlInFieldCalibrationDiagnosticPipelineEntry, std::allocator<ADJasperPearlInFieldCalibrationDiagnosticPipelineEntry>>=\"__begin_\"^{ADJasperPearlInFieldCalibrationDiagnosticPipelineEntry}\"__end_\"^{ADJasperPearlInFieldCalibrationDiagnosticPipelineEntry}\"__cap_\"^{ADJasperPearlInFieldCalibrationDiagnosticPipelineEntry}}"
+ "{vector<CGPoint, std::allocator<CGPoint>>=\"__begin_\"^{CGPoint}\"__end_\"^{CGPoint}\"__cap_\"^{CGPoint}}"
+ "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__cap_\"^}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
+ "~CVPixelBufferLock"
+ "\xc1"
+ "\xf0ab"
- "%@=%@"
- ","
- "--ane-options"
- "--ane-options-plist"
- "--e5-compute-units"
- "--e5-require-ane-resident=strict"
- "--mil-entry-points"
- "-i"
- "-o"
- "-p"
- ".N301"
- "/usr/local/bin/espressoc"
- "/usr/local/bin/zin_ane_dump"
- "137.3"
- "@64@0:8@16{?=Q@Biifff}24"
- "@80@0:8@16{CGSize=dd}24{?=Q@Biifff}40"
- "ADJasperColorInFieldCalibration jasper controller fail for only %d good spots"
- "ADJasperColorInFieldCalibration jasper controller pass %d good spots"
- "ANE options: %@"
- "AleatoricUncertainty"
- "AlphaMap"
- "AnglesVector"
- "AuxilaryRGBImage"
- "AuxiliaryAleatoricUncertainty"
- "AuxiliaryConfidence"
- "AuxiliaryDisparity"
- "AuxiliaryLogarithmicVariance"
- "AuxiliarySTDUncertainty"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32^@40"
- "BinaryMask"
- "Could not find model for \"%{public}@\""
- "Curr Processed Fused Normals"
- "DType"
- "DenseDepth"
- "Disparity"
- "EnableContextSwitchEvents"
- "ErrorPpx"
- "ErrorPpy"
- "ErrorRotationX"
- "ErrorRotationY"
- "ErrorRotationZ"
- "ErrorsVector"
- "H14G"
- "KernelRewind"
- "LogarithmicVariance"
- "MTLPixelFormatR32Uint support is temporarily disabled"
- "NeFrequency"
- "Normals"
- "OpaqueDepthFeatures"
- "OpaqueFeatures"
- "OpaqueFeaturesInput"
- "OpaqueFeaturesOutput"
- "Optimize"
- "PCEDepth"
- "PearlDepth"
- "PostProcessed Normals"
- "Ppx"
- "Ppy"
- "Prev Processed Fused Normals"
- "PreviousConfidence"
- "PreviousDepth"
- "PreviousDisparity"
- "PreviousRGBImage"
- "PstateDCSLevel"
- "PstateSOCLevel"
- "RGBImage"
- "ReductionPerf"
- "ReferenceRGBImage"
- "RotationX"
- "RotationY"
- "RotationZ"
- "STDUncertainty"
- "ScanWeightsForCompression"
- "SparseDepth"
- "SpatialSplitMode"
- "TB,N,V_doComputeNormals"
- "TB,N,V_doTemporalConsistency"
- "TB,N,V_powerMeasureMode"
- "TemporalSmoothingCurrentFeaturesRatioMin"
- "TemporalSmoothingPreviousFeaturesRatioMin"
- "Tq,N,V_stepsToSkip"
- "T{?=Q@Biifff},R,N,V_opticalFlowConfig"
- "Unprocessed Alpha"
- "Unprocessed Normals"
- "[9@\"<MTLComputePipelineState>\"]"
- "\\n\\s*--fspatial-split="
- "\\n\\s*--optimize="
- "^{PixelBufferUtilsSession=^{__CVBuffer}^{OpaqueVTPixelTransferSession}^{OpaqueVTPixelRotationSession}{CGSize=dd}I{CGSize=dd}I{CGRect={CGPoint=dd}{CGSize=dd}}ii}"
- "_%@"
- "_computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:"
- "_computeFeaturesWithCommandBuffer:in_tex:out_tex:"
- "_createImagePyramidWithCommandBuffer:inOutPyramidsArray:error:"
- "_createImagePyramidWithCommandBuffer:in_BGRATex:outPyramidsArray:error:"
- "_doComputeNormals"
- "_doNLRegularizationWithCommandBuffer:in_uv_tex:join_tex:w_tex:out_uv_tex:"
- "_doSolverWithCommandBuffer:currentFeatures:currentDerivitive:previousFeatures:previousDerivitive:scale:coeff:in_uv_tex:out_uv_tex:out_w_tex:"
- "_doTemporalConsistency"
- "_downscale2XWithCommandBuffer:in_tex:out_tex:scaling_factor:"
- "_inputBufferMap"
- "_isDisparity"
- "_itmCurrProcessedFusedNormals"
- "_itmPostProcessedNormals"
- "_itmPrevProcessedFusedNormals"
- "_itmUnprocessedAlpha"
- "_itmUnprocessedNormals"
- "_lastKnownGoodSpotsCount"
- "_lastKnownPointsCollectionVec"
- "_opticalFlowEnabled"
- "_outputBufferMap"
- "_powerMeasureMode"
- "_stepsToSkip"
- "aggregatedPointCloud"
- "alphaMapOutRaw"
- "ane"
- "arguments"
- "bufferNameForInputType:"
- "bufferNameForOutputType:"
- "bufferNameForType:isInput:"
- "cannot re-enable temporal consistency after executor was prepare without it."
- "code"
- "compilation_arguments.plist"
- "compiled model flags verification failed"
- "componentsJoinedByString:"
- "confidenceOutProcessed"
- "confidenceOutProcessedRotated"
- "confidenceOutRaw"
- "could not find json file for requested model %{public}@"
- "could not read network metadata "
- "crc32_%u_isANE_%d_espresso_%s"
- "createPixelBufferForOpticalFlow"
- "custom_options_net.plist"
- "dataWithContentsOfURL:"
- "date"
- "depthOutRaw"
- "descriptorForBufferOfType:isInput:pixelFormat:"
- "dictionaryWithContentsOfFile:"
- "disabled"
- "doComputeNormals"
- "doTemporalConsistency"
- "enumerateByteRangesUsingBlock:"
- "enumeratorAtPath:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "executableURL"
- "executeWithColor:colorCameraCalibration:colorWorldToPlatformTransform:pointClouds:lidarCameraCalibration:pointCloudWorldToPlatformTransforms:outDepthMap:outConfMap:outNormalsMap:"
- "executeWithColor:pointCloud:outDepthMap:outConfMap:outNormalsMap:"
- "executeWithColor:pointCloud:outDepthMap:outConfMap:outNormalsMap:worldToCameraTransform:cameraCalibration:"
- "experimentalModelPlatformOverride"
- "failed reading e5rt compilation arguments at %@"
- "failed storing previous normals"
- "failed to create folder structure needed for compilation. Error: %@"
- "failed to run %{public}@ with arguments: %{public}@"
- "fileHandleForReading"
- "fileSystemRepresentation"
- "fuseCurrentDepth:previousDepth:intoOutputDepth:currentConfidence:previousConfidence:intoOutputConfidence:currentNormals:previousNormals:intoOutputNormals:usingAlpha:defaultAlpha:confidenceUnits:"
- "getResourceValue:forKey:error:"
- "hwx"
- "i40@0:8@16@24@32"
- "i92@0:8@16@24@32@40@48i5660@68@76@84"
- "initWithData:encoding:"
- "initWithEngineType:"
- "initWithNetwork:requestedLayouts:espressoEngine:"
- "isProfiling"
- "jasperPerformanceEmulatedDevice"
- "jasperPerformanceOverridePath"
- "launchAndReturnError:"
- "lidarToColorTransform"
- "lkt_bgra2yuva"
- "localizedDescription"
- "mismatch in ANE compilation flag Optimize. Expected {reduction-perf} and got {%{public}@}"
- "mismatch in ANE compilation flag Optimize. Expected {} and got {%{public}@}"
- "mismatch in ANE compilation flag SpatialSplitMode between {%{public}@} and {%{public}@}"
- "model already compiled or being compiled, no need to recompile"
- "model folder found"
- "model should be compiled for e5ml"
- "moveItemAtPath:toPath:error:"
- "network confidence threshold ranges: (%.3f,%.3f), (%.3f,%.3f), (%.3f,%.3f)"
- "network input map: %@"
- "network output map: %@"
- "nextObject"
- "no ANE found to compile for"
- "normalsOutProcessedRotated"
- "normalsOutRaw"
- "opticalFlow"
- "path"
- "pipe"
- "platform is %@ but compiling to generic platform instead"
- "powerMeasureMode"
- "prevWarpedConf"
- "prevWarpedDepth"
- "processedNormalsOutputDescriptor"
- "providerForNetwork:requestedLayouts:espressoEngine:"
- "q108@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56^{__CVBuffer=}64^{__CVBuffer=}72^{__CVBuffer=}80^{__CVBuffer=}88f96Q100"
- "q128@0:8^{__CVBuffer=}16@24^^{__CVBuffer}32^^{__CVBuffer}40^^{__CVBuffer}48{?=[4]}56@120"
- "q144@0:8^{__CVBuffer=}16@24{?=[4]}32@96@104^{?=[4]}112^^{__CVBuffer}120^^{__CVBuffer}128^^{__CVBuffer}136"
- "q56@0:8^{__CVBuffer=}16@24^^{__CVBuffer}32^^{__CVBuffer}40^^{__CVBuffer}48"
- "rangeOfString:"
- "rangeOfString:options:"
- "readDataToEndOfFileAndReturnError:"
- "reduction-perf"
- "running %@ with arguments: %@"
- "scaledCalibration"
- "setArguments:"
- "setDoComputeNormals:"
- "setDoTemporalConsistency:"
- "setExecutableURL:"
- "setPowerMeasureMode:"
- "setStandardOutput:"
- "setStepsToSkip:"
- "sleepForTimeInterval:"
- "spatialSplitMode"
- "stepsToSkip"
- "substringToIndex:"
- "terminationStatus"
- "the doTemporalConsistency property is deprecated. please use temporalConsistencyMethod instead"
- "timed out waiting for model folder. Consider removing folder %@ and try again."
- "unable to find ANE compilation flag SpatialSplitMode"
- "universal"
- "useReductionPerformance"
- "v40@?0r^v8{_NSRange=QQ}16^B32"
- "waitUntilExit"
- "waiting for model folder to appear (timeout: %.0f seconds)"
- "{?=\"scales\"Q\"nwarpings\"@\"NSMutableArray\"\"useNonLocalRegularization\"B\"nlreg_radius\"i\"nlreg_padding\"i\"nlreg_sigma_l\"f\"nlreg_sigma_c\"f\"nlreg_sigma_w\"f}"
- "{?=Q@Biifff}16@0:8"
- "{unique_ptr<DisparityToDepth::DisparityToDepthFitEstimator, std::default_delete<DisparityToDepth::DisparityToDepthFitEstimator>>=\"__ptr_\"{__compressed_pair<DisparityToDepth::DisparityToDepthFitEstimator *, std::default_delete<DisparityToDepth::DisparityToDepthFitEstimator>>=\"__value_\"^{DisparityToDepthFitEstimator}}}"
- "{unique_ptr<DisparityToDepth::Ransac<float, float>, std::default_delete<DisparityToDepth::Ransac<float, float>>>=\"__ptr_\"{__compressed_pair<DisparityToDepth::Ransac<float, float> *, std::default_delete<DisparityToDepth::Ransac<float, float>>>=\"__value_\"^v}}"
- "{unique_ptr<DisparityToDepth::RansacLine2DModel, std::default_delete<DisparityToDepth::RansacLine2DModel>>=\"__ptr_\"{__compressed_pair<DisparityToDepth::RansacLine2DModel *, std::default_delete<DisparityToDepth::RansacLine2DModel>>=\"__value_\"^{RansacLine2DModel}}}"
- "{unique_ptr<DisparityToDepth::RansacLineModel, std::default_delete<DisparityToDepth::RansacLineModel>>=\"__ptr_\"{__compressed_pair<DisparityToDepth::RansacLineModel *, std::default_delete<DisparityToDepth::RansacLineModel>>=\"__value_\"^{RansacLineModel}}}"
- "{unique_ptr<DisparityToDepth::WorldPointsContainer, std::default_delete<DisparityToDepth::WorldPointsContainer>>=\"__ptr_\"{__compressed_pair<DisparityToDepth::WorldPointsContainer *, std::default_delete<DisparityToDepth::WorldPointsContainer>>=\"__value_\"^{WorldPointsContainer}}}"
- "{unique_ptr<PixelBufferUtilsSession, std::default_delete<PixelBufferUtilsSession>>=\"__ptr_\"{__compressed_pair<PixelBufferUtilsSession *, std::default_delete<PixelBufferUtilsSession>>=\"__value_\"^{PixelBufferUtilsSession}}}"
- "{vector<ADDisparityToDepthFitWorldPoint, std::allocator<ADDisparityToDepthFitWorldPoint>>=\"__begin_\"^{ADDisparityToDepthFitWorldPoint}\"__end_\"^{ADDisparityToDepthFitWorldPoint}\"__end_cap_\"{__compressed_pair<ADDisparityToDepthFitWorldPoint *, std::allocator<ADDisparityToDepthFitWorldPoint>>=\"__value_\"^{ADDisparityToDepthFitWorldPoint}}}"
- "{vector<float __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__begin_\"^\"__end_\"^\"__end_cap_\"{__compressed_pair<float * __attribute__((ext_vector_type(3))), std::allocator<float __attribute__((ext_vector_type(3)))>>=\"__value_\"^}}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"
- "{vector<std::vector<float>, std::allocator<std::vector<float>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<float> *, std::allocator<std::vector<float>>>=\"__value_\"^v}}"

```
