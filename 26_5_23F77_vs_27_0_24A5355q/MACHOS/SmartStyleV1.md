## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0xe11c
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x21c0
-  __TEXT.__objc_methlist: 0x162c
-  __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x4cd0
-  __TEXT.__cstring: 0x1c4a
-  __TEXT.__objc_classname: 0x25e
-  __TEXT.__objc_methtype: 0x13aa
-  __TEXT.__unwind_info: 0x328
-  __DATA_CONST.__auth_got: 0x270
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x8
+748.0.0.122.2
+  __TEXT.__text: 0x16334
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x2340
+  __TEXT.__objc_methlist: 0x175c
+  __TEXT.__const: 0xb0
+  __TEXT.__objc_methname: 0x510d
+  __TEXT.__cstring: 0x3c59
+  __TEXT.__oslogstring: 0x2a15
+  __TEXT.__objc_classname: 0x247
+  __TEXT.__objc_methtype: 0x13c4
+  __TEXT.__unwind_info: 0x3a0
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2740
-  __DATA.__objc_selrefs: 0xb68
-  __DATA.__objc_ivar: 0x1e4
+  __DATA_CONST.__auth_got: 0x2e0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x28c0
+  __DATA.__objc_selrefs: 0xc10
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0
   __DATA.__common: 0x60

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9568B202-A610-396F-84FA-4F0F2397A3FA
-  Functions: 467
-  Symbols:   1136
-  CStrings:  935
+  UUID: 29893597-5B19-3E6D-BC58-4325D8AC4F81
+  Functions: 561
+  Symbols:   1279
+  CStrings:  1213
 
Symbols:
+ +[CMISmartStyleProcessorV1 getRequiredMemorySizeForProcessingType:]
+ -[CMISmartStyleProcessorInputOutputV1 inputWeightSegmentMapPixelBufferScaledForISPSMG]
+ -[CMISmartStyleProcessorInputOutputV1 inputWeightSegmentMapPixelBuffer]
+ -[CMISmartStyleProcessorInputOutputV1 outputTargetPixelBuffer]
+ -[CMISmartStyleProcessorInputOutputV1 setInputWeightSegmentMapPixelBuffer:]
+ -[CMISmartStyleProcessorInputOutputV1 setInputWeightSegmentMapPixelBufferScaledForISPSMG:]
+ -[CMISmartStyleProcessorInputOutputV1 setOutputTargetPixelBuffer:]
+ -[CMISmartStyleProcessorStillImageConfigurationV1 pixelBufferAttributesWithCapacityForWeightSegmentMap]
+ -[CMISmartStyleProcessorStreamingConfigurationV1 pixelBufferAttributesWithCapacityForWeightSegmentMap]
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 copyCoefficientsFrom:to:]
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.17
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.18
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.19
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.20
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.15
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.17
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapScaledForISPSTENFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapScaledForISPSTENFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapScaledForISPSTENFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 initWithMetalContext:]
+ -[CMISmartStyleProcessorUtilitiesV1 initWithMetalContext:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 prewarm]
+ -[CMISmartStyleProcessorUtilitiesV1 prewarm].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 prewarm].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.6
+ -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSTENProcessingSession:]
+ -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSTENProcessingSession:].cold.1
+ -[CMISmartStyleProcessorV1 prewarm].cold.11
+ -[CMISmartStyleProcessorV1 waitForSchedule]
+ -[CMISmartStyleProcessorV1 waitForSchedule].cold.1
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._inputWeightSegmentMapPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._inputWeightSegmentMapPixelBufferScaledForISPSMG
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._outputTargetPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._styleEngineWeightSegmentMapProcessor
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._instanceLabelEncodedFirst8Char
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._instanceLabelEncodedLast8Char
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._ispSTENProcessingSession
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._shouldDownscaleForTargetGeneration
+ _CFStringGetBytes
+ _CFStringGetLength
+ _FigCapturePortTypeIsFrontSuperWideColorCamera
+ _FigSignalErrorAt3
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CMISmartStyleProcessor
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gGMFigKTraceEnabled
+ _kdebug_trace
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UTF8String
+ _objc_msgSend$copyCoefficientsFrom:to:
+ _objc_msgSend$initWithMetalContext:
+ _objc_msgSend$inputWeightSegmentMapPixelBuffer
+ _objc_msgSend$inputWeightSegmentMapPixelBufferScaledForISPSMG
+ _objc_msgSend$ispCaptureDevice
+ _objc_msgSend$outputTargetPixelBuffer
+ _objc_msgSend$requiredMemorySizeForProcessingType:configuration:
+ _objc_msgSend$setInputWeightPlanePixelBuffer:
+ _objc_msgSend$setIspCaptureDevice:
+ _objc_msgSend$setIspSTENProcessingSession:
+ _objc_msgSend$setOutputWeightPlanePixelBuffer:
+ _objc_msgSend$setOutputWeightPlaneScaledForISPSTENPixelBuffer:
+ _objc_msgSend$waitForSchedule
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
+ _os_log_type_enabled
+ _strlen
+ _strncpy
- -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.5
- -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.6
- -[CMISmartStyleProcessorInputOutputV1 inputWeightPlanePixelBufferScaledForISPSMG]
- -[CMISmartStyleProcessorInputOutputV1 setInputWeightPlanePixelBufferScaledForISPSMG:]
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.10
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.11
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.12
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.13
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.5
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.6
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.7
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.8
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.9
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.3
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.4
- -[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:].cold.1
- -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:].cold.5
- -[CMISmartStyleProcessorV1 _requestedMemSize:].cold.1
- -[CMISmartStyleProcessorV1 process].cold.18
- -[CMISmartStyleProcessorV1 process].cold.19
- -[CMISmartStyleProcessorV1 process].cold.20
- -[CMISmartStyleProcessorV1 styleRendererOutputStyledThumbnailPixelBuffer]
- OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._inputWeightPlanePixelBufferScaledForISPSMG
- _FigSignalErrorAtGM
- _fig_log_get_emitter
- _kFigCapturePortType_FrontFacingSuperWideCamera
- _objc_msgSend$inputWeightPlanePixelBufferScaledForISPSMG
- _objc_msgSend$isEqual:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x27
- _objc_setProperty_nonatomic_copy
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-1"
+ "-[CMISmartStyleOvercaptureThumbnailGenerator _bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:]"
+ "-[CMISmartStyleOvercaptureThumbnailGenerator _metalPixelFormatForPixelbuffer:]"
+ "-[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:]"
+ "-[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:]"
+ "-[CMISmartStyleProcessorInputOutputV1 init]"
+ "-[CMISmartStyleProcessorInputOutputV1 setInputSmartStyle:]"
+ "-[CMISmartStyleProcessorStillImageConfigurationV1 init]"
+ "-[CMISmartStyleProcessorStreamingConfigurationV1 init]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _compileShaders]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _createGlobalToneCurveTextureFromMetadataDict:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _getComponentCountOfFormat:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 copyCoefficientsFrom:to:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createWeightSegmentMapScaledForISPSTENFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 initWithMetalContext:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 prewarm]"
+ "-[CMISmartStyleProcessorUtilitiesV1 propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:]"
+ "-[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureOutputStyledThumbnailPixelBufferForPixelBufferRenderer:unstyledThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _requestedMemSize:]"
+ "-[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:]"
+ "-[CMISmartStyleProcessorV1 finishProcessing]"
+ "-[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSMGProcessingSession:]"
+ "-[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSTENProcessingSession:]"
+ "-[CMISmartStyleProcessorV1 init]"
+ "-[CMISmartStyleProcessorV1 prepareToProcess:]"
+ "-[CMISmartStyleProcessorV1 prewarm]"
+ "-[CMISmartStyleProcessorV1 process]"
+ "-[CMISmartStyleProcessorV1 purgeResources]"
+ "-[CMISmartStyleProcessorV1 resetState]"
+ "-[CMISmartStyleProcessorV1 setInstanceLabel:]"
+ "-[CMISmartStyleProcessorV1 setup]"
+ "-[CMISmartStyleProcessorV1 waitForSchedule]"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: MetalContext is nil"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Shaders compilation failed."
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Unable to init CMISmartStyleOvercaptureThumbnailGenerator."
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Unable to load the bundle for CMISmartStyleOvercaptureThumbnailGenerator."
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : Shifting inputImageRect.origin by deltaMapRegionToRenderRect.origin = ( %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : deltaMapRegionToRenderRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : imageSize = ( %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : inputImageRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : inputOriginalImageRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : inputReferenceForDeltaMapComputationCropRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : inputUnstyledCropRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : outputDeltaMapCropRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : outputImageRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: %p : outputStyledCropRect = ( %d ; %d ; %d ; %d )"
+ "<<<< CMISmartStyleProcessor >>>> %s: Already prepared to process processingType: %d"
+ "<<<< CMISmartStyleProcessor >>>> %s: Found Styles metal event in metadata in CMISmartStyleProcessorV1 instance %@"
+ "<<<< CMISmartStyleProcessor >>>> %s: Instance '%@' encoded as first8=0x%llx last8=0x%llx"
+ "<<<< CMISmartStyleProcessor >>>> %s: Metal command queue is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: MetalContext is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: Setting up SmartStyleProcessor with ISP SMG processing session: %p"
+ "<<<< CMISmartStyleProcessor >>>> %s: Setting up SmartStyleProcessor with ISP STEN processing session: %p"
+ "<<<< CMISmartStyleProcessor >>>> %s: Setting up SmartStyleProcessor with provided metal command queue."
+ "<<<< CMISmartStyleProcessor >>>> %s: Smart style engine processor failed to prepare to process (err:%d)"
+ "<<<< CMISmartStyleProcessor >>>> %s: SmartStyle Processor (label:%@) is requesting memory of size:%zu"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor configuration"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor input output"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor instance"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to load the bundle for smart style processor."
+ "<<<< CMISmartStyleProcessor >>>> %s: Unexpected SRL state: after receiving valid masks curve parameter must stay valid"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unsupported Smart Style version %d"
+ "<<<< CMISmartStyleProcessor >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< CMISmartStyleProcessor >>>> %s: _smartStylePixelBufferRenderer is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _styleEngineProcessor is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _subjectRelightingStage is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _utilities is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: prepareToProcess for %d"
+ "<<<< CMISmartStyleProcessor >>>> %s: requesting GPU metal heap size without preparing to process for processor (label:%@), requesting the max size:%zu "
+ "<<<< CMISmartStyleProcessor >>>> %s: utilities prewarm failed"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping data has invalid threshold bin index"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping data is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping header dataSize is invalid"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping header is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping metadata is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to bind original mask pixel buffer as texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to bind refined mask pixel buffer as texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to copy coefficients, err = %d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to create a metal context"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to create identity transform coefficients, err = %d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to create weight segment map - err = %d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to finish weight segment map generation - err = %d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Invalud clipping data grid size"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: LTM thumbnail size coming from ISP is %dx%d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size height sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size width sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Style engine prepare to process failed"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Style engine processor is nil. Unable to init a smart style processor utilities"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Style engine setup failed"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction linear thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction to linear thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction to unstyled thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to create a metal texture cache"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get GDC params, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get component count of format"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get metal texture address"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to initialize a smart style utilities processor instance"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: _coefficientsProcessor is nil. Unable to init a smart style processor utilities."
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: _styleEngineWeightSegmentMapProcessor is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: blitEncoder is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: cameraInfo is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: commandBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: commandEncoder is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: gridOriginX should be >= 0"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: gridOriginX+extentX should be lower than rawSensorWidth"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: gridOriginY should be >= 0"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: gridOriginY+extentY should be lower than rawSensorHeight"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnail format is incorrect (RGB or RGBRGB is expected)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnail format is incorrect (RGBRGB is expected)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailFormat format is not available"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailMetadata is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailPixelBuffer is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLTMThumbnailSampleBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain blue channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain green channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain red channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData has wrong size"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMetadata is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputOutputPostLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputOutputPreLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPostLTMThumbnailPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPostLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPreLTMPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPreLTMThumbnailBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputTexture for blit is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: metalContext is nil. Unable to init a smart style processor utilities"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputFormat is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputPixelBuffer is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputTexture for blit is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: pixelBuffer is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: postLTMThumbnail (%d,%d) - ROI is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: postLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTM thumbnail size coming from ISP is %dx%d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail (%d,%d) - ROI is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with clipping metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with fallback clipping metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with mapped sensor rect metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: pretLTMThumbnail (%d,%d) - ROI is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: rawSensorHeight is 0"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: rawSensorWidth is 0"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: totalSensorCropRect metadata not found"
+ "CMISmartStyleRendererStatusInputError"
+ "CMISmartStyleRendererStatusRenderingFailed"
+ "CMISmartStyleStatusConfigurationFailed"
+ "CMISmartStyleStatusInputError"
+ "CMISmartStyleStatusOtherAllocationFailed"
+ "CMISmartStyleStatusOtherError"
+ "CMISmartStyleStatusRenderingError"
+ "CMISmartStyleStatusStyleEngineError"
+ "Configuring the renderer needs either the unstyled pixel buffer or unstyled thumbnail pixel buffer along with proper crop rects for the pixel buffer"
+ "Could not bind destination pixel buffer"
+ "Could not bind source pixel buffer"
+ "Downscaling input linear pixel buffer to the linear thumbnail pixel buffer failed"
+ "Downscaling input target pixel buffer to style engine input target styled thumbnail pixel buffer failed"
+ "Downscaling input unstyled pixel buffer to the style renderer unstyled pixel buffer failed"
+ "Downscaling input unstyled thumbnail pixel buffer to the style renderer unstyled thumbnail pixel buffer failed"
+ "Downscaling style renderer styled output to style engine input target thumbnail pixel buffer failed"
+ "Downscaling style renderer unstyled thumbnail to style engine input unstyled thumbnail pixel buffer failed"
+ "Expected to have inputUnstyledPixelBuffer to satisfy the requirements of the style pixel buffer renderer."
+ "Expected to have non empty inputUnstyledCropRect for configuring the style pixel buffer renderer"
+ "Failed to load tuning parameters"
+ "FigMetalAllocator setupWithDescriptor failed"
+ "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
+ "Input target thumbnail pixel buffer dimensions don;t match StyleEngine thumbnail configuration"
+ "Renderer failed to prewarm"
+ "Renderer failed to reset state"
+ "Smart style configuration is not conforming to still or streaming configuration"
+ "Smart style configuration is not set"
+ "Smart style renderer failed to prepare to process"
+ "Smart style renderer failed to process"
+ "Style engine failed to prewarm"
+ "Style engine failed to process"
+ "Style engine failed to purge resources"
+ "Style engine failed to reset state"
+ "Style engine failed to setup"
+ "Style engine setup failed"
+ "Style processor subprocessors need to be on the same command queue"
+ "Style renderer failed to purge resources"
+ "Style renderer failed to setup"
+ "T^{__CVBuffer=},N,V_inputWeightSegmentMapPixelBuffer"
+ "T^{__CVBuffer=},N,V_inputWeightSegmentMapPixelBufferScaledForISPSMG"
+ "T^{__CVBuffer=},N,V_outputTargetPixelBuffer"
+ "UTF8String"
+ "Unable to cache pixel buffer texture"
+ "Unable to create an intermediate buffer for input unstyled thumbnail pixel buffer for configuring the renderer."
+ "Unable to create an intermediate buffer to for unstyled input thumbnail for style engine learning"
+ "Unable to create an intermediate buffer to produce styled rendering"
+ "Unable to get texture address"
+ "Unsupported pixel buffer format for input"
+ "Unsupported pixel buffer format for output"
+ "Unsupported processing type"
+ "_cmImagingAllocator is NULL"
+ "_createLinearThumbnailCroppedToPreLTMPipelineState is NULL"
+ "_createLinearThumbnailCroppedToPreLTMPipelineStateWithGDC is NULL"
+ "_createLinearThumbnailPipelineState is NULL"
+ "_createLinearThumbnailPipelineStateWithGDC is NULL"
+ "_createThumbnailPipelineState is NULL"
+ "_createThumbnailsPipelineStateWithGDC is NULL"
+ "_extractThumbnailPipelineState is NULL"
+ "_inputWeightSegmentMapPixelBuffer"
+ "_inputWeightSegmentMapPixelBufferScaledForISPSMG"
+ "_instanceLabelEncodedFirst8Char"
+ "_instanceLabelEncodedLast8Char"
+ "_ispSTENProcessingSession"
+ "_maskCropAndScalePipelineState is NULL"
+ "_maskCropAndScalePipelineStateWithGDC is NULL"
+ "_maskFalsePositiveRejectionPipelineState is NULL"
+ "_outputTargetPixelBuffer"
+ "_shouldDownscaleForTargetGeneration"
+ "_styleEngineWeightSegmentMapProcessor"
+ "allocatorBackend is  nil"
+ "allocatorDesc is NULL"
+ "cmismartstyleovercapturethumbnailgenerator_trace"
+ "cmismartstyleprocessor_trace"
+ "cmismartstyleprocessorutilities_trace"
+ "commandBuffer is NULL"
+ "commandBufferToUse is NULL"
+ "computeEncoder is NULL"
+ "copyCoefficientsFrom:to:"
+ "copyStatsForOtherEffectsTo:"
+ "createWeightSegmentMapFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:"
+ "createWeightSegmentMapScaledForISPSTENFromMetadata:inputUnstyledThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:"
+ "err"
+ "err == CMIStyleEngineStatusNoError"
+ "getRequiredMemorySizeForProcessingType:"
+ "i24@0:8@\"<MTLBuffer>\"16"
+ "initWithMetalContext:"
+ "initWithOptionalMetalCommandQueue:ispSTENProcessingSession:"
+ "input SRL pixel buffer is NULL"
+ "inputLinearPixelBuffer is NULL"
+ "inputWeightSegmentMapPixelBuffer"
+ "inputWeightSegmentMapPixelBufferScaledForISPSMG"
+ "ispCaptureDevice"
+ "kCMBaseObjectError_ParamErr"
+ "outputTargetPixelBuffer"
+ "pixelBufferAttributesWithCapacityForWeightSegmentMap"
+ "postLTMImageGlobalToneCurveTexture is NULL"
+ "refinedMaskTexture.height == originalMaskTexture.height is NULL"
+ "refinedMaskTexture.width == originalMaskTexture.width is NULL"
+ "requiredMemorySizeForProcessingType:configuration:"
+ "setInputWeightPlanePixelBuffer:"
+ "setInputWeightSegmentMapPixelBuffer:"
+ "setInputWeightSegmentMapPixelBufferScaledForISPSMG:"
+ "setIspCaptureDevice:"
+ "setIspSTENProcessingSession:"
+ "setOutputTargetPixelBuffer:"
+ "setOutputWeightPlanePixelBuffer:"
+ "setOutputWeightPlaneScaledForISPSTENPixelBuffer:"
+ "waitForSchedule"
- "\r"
- "%s signalled err=%d at <>:%d"
- "T^{__CVBuffer=},N,V_inputWeightPlanePixelBufferScaledForISPSMG"
- "T^{__CVBuffer=},R,N"
- "T^{__CVBuffer=},R,N,V_styleRendererOutputStyledThumbnailPixelBuffer"
- "_inputWeightPlanePixelBufferScaledForISPSMG"
- "inputWeightPlanePixelBufferScaledForISPSMG"
- "styleRendererOutputStyledThumbnailPixelBuffer"

```
