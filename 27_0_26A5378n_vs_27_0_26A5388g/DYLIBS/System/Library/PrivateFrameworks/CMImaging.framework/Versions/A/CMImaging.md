## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.0.1
-  __TEXT.__text: 0x1c8094
+761.0.0.0.3
+  __TEXT.__text: 0x1c83bc
   __TEXT.__objc_methlist: 0xd204
   __TEXT.__const: 0x1100
   __TEXT.__oslogstring: 0x13e70
-  __TEXT.__cstring: 0x240dc
+  __TEXT.__cstring: 0x24194
   __TEXT.__gcc_except_tab: 0x1538
-  __TEXT.__unwind_info: 0x2eb0
+  __TEXT.__unwind_info: 0x2ea8
   __TEXT.__eh_frame: 0x608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x4b8
   __DATA_CONST.__objc_arraydata: 0x380
-  __DATA_CONST.__got: 0xbe8
+  __DATA_CONST.__got: 0xbf8
   __AUTH_CONST.__const: 0xe50
-  __AUTH_CONST.__cfstring: 0x6960
-  __AUTH_CONST.__objc_const: 0x1f260
+  __AUTH_CONST.__cfstring: 0x69a0
+  __AUTH_CONST.__objc_const: 0x1f2a0
   __AUTH_CONST.__objc_intobj: 0xae0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x1130
   __AUTH_CONST.__auth_got: 0xaf8
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x17ac
+  __DATA.__objc_ivar: 0x17b4
   __DATA.__data: 0x12d88
   __DATA.__common: 0x1d0
   __DATA.__bss: 0x60

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7186
-  Symbols:   10302
-  CStrings:  4711
+  Symbols:   10306
+  CStrings:  4713
 
Symbols:
+ OBJC_IVAR_$_CMIStyleEngineApplyStyle._skinMaskPurpose
+ OBJC_IVAR_$_CMIStyleEngineProcessor._skinMaskPurpose
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomDstRect
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomSrcRect
CStrings:
+ "%@ColorPrimaries:%@, YCbCrMatrix:%@, TransferFunction:%@"
+ "( inputTexture.pixelFormat == outputTexture.pixelFormat ) || ( [CMIGuidedFilter isSingleChannelTexture:inputTexture] && [CMIGuidedFilter isSingleChannelTexture:outputTexture] )"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIDistortionModel/CMIDistortionModel.m %s: BayerBinningFactor is 0 overwriting it to 1"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: CMIFFTContext is invalid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DBatched"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DThreadgroup"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::applyTwiddles"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::realToComplexShim"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer2D"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer3D"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::unscrambleMixedRadix"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not get global FFT butterfly shader for radix:%zu precision:%d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not initialise CMIFFTEncode object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTContext is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTEncode object is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not allocate toDecrementFig array"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTDimension object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTExecutor object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float layout type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float precision type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal layout type is not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type is not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type not valid"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTContext.m %s: Could not allocate CMIFFTContext super object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTTransform.m %s: Could not initialise CMIFFTTransformInternal object"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture+Metal.m %s: command buffer did not complete but gave no error %ld"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture flatMap: transform() returned nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture setValue: called on already-resolved future"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture timed out"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing AGC"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing DarkCurrentTemperatureModelScaling"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ExposureTime"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionScalingFactor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionSpatialStdDev"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameAGC"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameExposureTime"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSensorTemperature"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSpatialStdDev"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing SensorTemperature"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: constantValues is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: externalMemoryDescriptor is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Failed to determine first pixel for versatile format"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unrecognized BayerPattern: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIWarpStage/CMIWarpStage.m %s: constantValues is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CMIResourceCache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CVMetalTextureCache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create buffer from cache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create residency set"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create texture from cache"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/ModuleCalibration/CMIShadingFPNCorrectionImage.m %s: Mismatch between encoded metadata and file system metadata. Encoded:%@. File system:%@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispProcessingParams is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispSessionPrepareSemaphore is nil"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Cannot parse Rect"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected precondition. Should not be called on empty array."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected type: None"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of TotalSensorCropRect failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of valid buffer rect failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: RawSensorWidth not found"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: TotalSensorCropRect not found"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.cbVWDn/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: wrong face rectangle dictionary"
+ "N/A"
+ "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3625, __builtin_return_address(0), 0) == 0 "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIDistortionModel/CMIDistortionModel.m %s: BayerBinningFactor is 0 overwriting it to 1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: CMIFFTContext is invalid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DBatched"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DThreadgroup"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::applyTwiddles"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::realToComplexShim"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer2D"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer3D"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::unscrambleMixedRadix"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not get global FFT butterfly shader for radix:%zu precision:%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not initialise CMIFFTEncode object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTContext is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTEncode object is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not allocate toDecrementFig array"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTDimension object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTExecutor object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float layout type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float precision type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal layout type is not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type is not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type not valid"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTContext.m %s: Could not allocate CMIFFTContext super object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTTransform.m %s: Could not initialise CMIFFTTransformInternal object"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture+Metal.m %s: command buffer did not complete but gave no error %ld"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture flatMap: transform() returned nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture setValue: called on already-resolved future"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFuture/CMIFuture.m %s: CMIFuture timed out"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing AGC"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing DarkCurrentTemperatureModelScaling"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ExposureTime"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionScalingFactor"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionSpatialStdDev"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameAGC"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameExposureTime"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSensorTemperature"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSpatialStdDev"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing SensorTemperature"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: constantValues is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: externalMemoryDescriptor is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Failed to determine first pixel for versatile format"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unrecognized BayerPattern: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIWarpStage/CMIWarpStage.m %s: constantValues is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CMIResourceCache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CVMetalTextureCache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create buffer from cache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create residency set"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create texture from cache"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/ModuleCalibration/CMIShadingFPNCorrectionImage.m %s: Mismatch between encoded metadata and file system metadata. Encoded:%@. File system:%@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispProcessingParams is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/ApplyStyle/CMIStyleEngineApplyStyle.m %s: ispSessionPrepareSemaphore is nil"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Cannot parse Rect"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected precondition. Should not be called on empty array."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected type: None"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of TotalSensorCropRect failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: Normalization of valid buffer rect failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: RawSensorWidth not found"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: TotalSensorCropRect not found"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2AaFFd/Sources/CameraCapture_CMImaging/CMImaging/Sources/Utilities/CMILTMRectsUtilities.m %s: wrong face rectangle dictionary"
- "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3586, __builtin_return_address(0), 0) == 0 "
- "inputTexture.pixelFormat == outputTexture.pixelFormat"
```
