## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging`

```diff

-  __TEXT.__text: 0x1cb70c
-  __TEXT.__objc_methlist: 0xd164
+  __TEXT.__text: 0x1c8094
+  __TEXT.__objc_methlist: 0xd204
   __TEXT.__const: 0x1100
-  __TEXT.__oslogstring: 0x13bbe
-  __TEXT.__cstring: 0x240a1
+  __TEXT.__oslogstring: 0x13e70
+  __TEXT.__cstring: 0x240dc
   __TEXT.__gcc_except_tab: 0x1538
-  __TEXT.__unwind_info: 0x2ea0
-  __TEXT.__eh_frame: 0x5c0
+  __TEXT.__unwind_info: 0x2eb0
+  __TEXT.__eh_frame: 0x608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x61a0
+  __DATA_CONST.__objc_selrefs: 0x61c8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x380
-  __DATA_CONST.__got: 0xba0
+  __DATA_CONST.__got: 0xbe8
   __AUTH_CONST.__const: 0xe50
-  __AUTH_CONST.__cfstring: 0x6940
-  __AUTH_CONST.__objc_const: 0x1f198
+  __AUTH_CONST.__cfstring: 0x6960
+  __AUTH_CONST.__objc_const: 0x1f260
   __AUTH_CONST.__objc_intobj: 0xae0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x1130
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__auth_got: 0xaf8
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x179c
+  __DATA.__objc_ivar: 0x17ac
   __DATA.__data: 0x12d88
-  __DATA.__common: 0x1c0
-  __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0x3980
+  __DATA.__common: 0x1d0
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__objc_data: 0x3b60
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x1b0
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7170
-  Symbols:   13329
-  CStrings:  5545
+  Functions: 7186
+  Symbols:   13360
+  CStrings:  5553
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[CMITIPConfig initialize]
+ -[CMIInferenceExecutionStreamBypass setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV1 aneExecutionPriority]
+ -[CMIInferenceExecutionStreamEspressoV1 setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV1 setAneExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV2 aneExecutionPriority]
+ -[CMIInferenceExecutionStreamEspressoV2 setANEExecutionPriority:]
+ -[CMIInferenceExecutionStreamEspressoV2 setAneExecutionPriority:]
+ -[CMITIPConfig aneExecutionPriorityOverride]
+ -[CMITIPConfig setAneExecutionPriorityOverride:]
+ -[CMITiledInferenceProcessorConfig aneExecutionPriority]
+ -[CMITiledInferenceProcessorConfig setAneExecutionPriority:]
+ GCC_except_table70
+ GCC_except_table93
+ GCC_except_table94
+ OBJC_IVAR_$_CMIInferenceExecutionStreamEspressoV1._aneExecutionPriority
+ OBJC_IVAR_$_CMIInferenceExecutionStreamEspressoV2._aneExecutionPriority
+ OBJC_IVAR_$_CMITIPConfig._aneExecutionPriorityOverride
+ OBJC_IVAR_$_CMITiledInferenceProcessorConfig._aneExecutionPriority
+ _e5rt_execution_stream_set_ane_execution_priority
+ _espresso_plan_set_priority
+ _gCMITIPConfig
+ _objc_msgSend$aneExecutionPriority
+ _objc_msgSend$aneExecutionPriorityOverride
+ _objc_msgSend$parentNetwork
+ _objc_msgSend$plan
+ _objc_msgSend$setANEExecutionPriority:
+ _objc_msgSend$setAneExecutionPriorityOverride:
- GCC_except_table79
- GCC_except_table89
- GCC_except_table92
CStrings:
+ "-[CMIInferenceExecutionStreamEspressoV1 submitAsyncWithCompletionHandler:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIDistortionModel/CMIDistortionModel.m %s: BayerBinningFactor is 0 overwriting it to 1"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: CMIFFTContext is invalid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DBatched"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DThreadgroup"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::applyTwiddles"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::realToComplexShim"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer2D"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer3D"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::unscrambleMixedRadix"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not get global FFT butterfly shader for radix:%zu precision:%d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not initialise CMIFFTEncode object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTContext is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTEncode object is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not allocate toDecrementFig array"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTDimension object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTExecutor object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float layout type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float precision type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal layout type is not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type is not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTContext.m %s: Could not allocate CMIFFTContext super object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTTransform.m %s: Could not initialise CMIFFTTransformInternal object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture+Metal.m %s: command buffer did not complete but gave no error %ld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture flatMap: transform() returned nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture setValue: called on already-resolved future"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture timed out"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing AGC"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing DarkCurrentTemperatureModelScaling"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ExposureTime"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionScalingFactor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionSpatialStdDev"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameAGC"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameExposureTime"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSensorTemperature"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSpatialStdDev"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing SensorTemperature"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: constantValues is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: externalMemoryDescriptor is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Failed to determine first pixel for versatile format"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unrecognized BayerPattern: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIWarpStage/CMIWarpStage.m %s: constantValues is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CMIResourceCache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CVMetalTextureCache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create buffer from cache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create residency set"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create texture from cache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/ModuleCalibration/CMIShadingFPNCorrectionImage.m %s: Mismatch between encoded metadata and file system metadata. Encoded:%@. File system:%@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispProcessingParams is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispSessionPrepareSemaphore is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Cannot parse Rect"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected precondition. Should not be called on empty array."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected type: None"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of TotalSensorCropRect failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of valid buffer rect failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: RawSensorWidth not found"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: TotalSensorCropRect not found"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: wrong face rectangle dictionary"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Could not load default biases for cast type %@"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] Error: Failed to load %s.plist - falling back to compiled-in version"
+ "<<<< CMITIP >>>> %s: Warning! CMITiledInferenceProcessor is configured with CMIInferenceANEExecutionPriorityHigh — this maps to ANE HW band 2 which should be reserved for streaming inferences. CMITiledInferenceProcessor is used for stills processing and running at high ANE priority will conflict with concurrent streaming inference workloads on the ANE."
+ "<<<< CMITIP >>>> %s: e5rt_execution_stream_set_ane_execution_priority failed, %s."
+ "<<<< CMITIP >>>> %s: e5rt_execution_stream_submit_async_with_timeout failed %s."
+ "<<<< CMITIP >>>> %s: espresso_plan_set_priority failed (%d)"
+ "<<<< CMITIP >>>> %s: setANEExecutionPriority failed (err:%d)"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig aneExecutionPriorityOverride:  %lu"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig aneSubmitTimeoutMs:            %llu"
+ "<<<< CMITIPConfig >>>> %s: CMITIPConfig shareIntermediates:            %d"
+ "_loadDefaultUserBiasByCastType"
+ "cmitipconfig_trace"
- "+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIDistortionModel/CMIDistortionModel.m %s: BayerBinningFactor is 0 overwriting it to 1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: CMIFFTContext is invalid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DBatched"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DThreadgroup"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::applyTwiddles"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::realToComplexShim"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer2D"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer3D"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::unscrambleMixedRadix"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not get global FFT butterfly shader for radix:%zu precision:%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not initialise CMIFFTEncode object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTContext is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTEncode object is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not allocate toDecrementFig array"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTDimension object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTExecutor object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float layout type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float precision type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal layout type is not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type is not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTContext.m %s: Could not allocate CMIFFTContext super object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTTransform.m %s: Could not initialise CMIFFTTransformInternal object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture+Metal.m %s: command buffer did not complete but gave no error %ld"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture flatMap: transform() returned nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture setValue: called on already-resolved future"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture timed out"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing AGC"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing DarkCurrentTemperatureModelScaling"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ExposureTime"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionScalingFactor"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionSpatialStdDev"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameAGC"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameExposureTime"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSensorTemperature"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSpatialStdDev"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing SensorTemperature"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: constantValues is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: externalMemoryDescriptor is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Failed to determine first pixel for versatile format"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unrecognized BayerPattern: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIWarpStage/CMIWarpStage.m %s: constantValues is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CMIResourceCache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CVMetalTextureCache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create buffer from cache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create residency set"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create texture from cache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/ModuleCalibration/CMIShadingFPNCorrectionImage.m %s: Mismatch between encoded metadata and file system metadata. Encoded:%@. File system:%@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispProcessingParams is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispSessionPrepareSemaphore is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Cannot parse Rect"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected precondition. Should not be called on empty array."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected type: None"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of TotalSensorCropRect failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of valid buffer rect failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: RawSensorWidth not found"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: TotalSensorCropRect not found"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AF2X7Z/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: wrong face rectangle dictionary"
- "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid cast type %@"
- "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] Error: Failed to load RendererTuning.plist - falling back to compiled in version"
- "<<<< CMITIP >>>> %s: CMITIPConfig aneSubmitTimeoutMs:    %llu"
- "<<<< CMITIP >>>> %s: CMITIPConfig shareIntermediates:    %d"
- "<<<< CMITIP >>>> %s: e5rt_execution_stream_execute_sync failed %s."

```
