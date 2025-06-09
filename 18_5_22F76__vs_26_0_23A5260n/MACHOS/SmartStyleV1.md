## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0xb5e8
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0x13d4
-  __TEXT.__objc_methname: 0x4301
-  __TEXT.__cstring: 0x14db
+650.0.0.122.4
+  __TEXT.__text: 0x15f8c
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__const: 0xa0
+  __TEXT.__objc_methname: 0x4aa3
+  __TEXT.__cstring: 0x3a2e
+  __TEXT.__oslogstring: 0x2780
   __TEXT.__objc_classname: 0x25e
-  __TEXT.__objc_methtype: 0x10c6
-  __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x180
+  __TEXT.__objc_methtype: 0x1357
+  __TEXT.__unwind_info: 0x318
+  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x24e8
-  __DATA.__objc_selrefs: 0xa18
-  __DATA.__objc_ivar: 0x1bc
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x2710
+  __DATA.__objc_selrefs: 0xb10
+  __DATA.__objc_ivar: 0x1e4
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0
   __DATA.__common: 0x60

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98AB36CE-92F9-3168-AF38-E3BF35ACA12E
-  Functions: 362
-  Symbols:   980
-  CStrings:  842
+  UUID: 6BD7C6C5-49E5-30C7-B2DE-5C18902092F7
+  Functions: 490
+  Symbols:   1171
+  CStrings:  1159
 
Symbols:
+ +[CMISmartStyleProcessorV1 getDefaultProcessorConfigurationForStreamingAcceleratedWithFilterType:]
+ +[CMISmartStyleProcessorV1 getDefaultProcessorConfigurationForStreamingAccelerated]
+ -[CMISmartStyleProcessorInputOutputV1 computeOnlySubjectRelighting]
+ -[CMISmartStyleProcessorInputOutputV1 inputWeightPlanePixelBufferScaledForISPSMG]
+ -[CMISmartStyleProcessorInputOutputV1 setComputeOnlySubjectRelighting:]
+ -[CMISmartStyleProcessorInputOutputV1 setInputWeightPlanePixelBufferScaledForISPSMG:]
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 _createGlobalToneCurveTextureFromMetadataDict:]
+ -[CMISmartStyleProcessorUtilitiesV1 _createGlobalToneCurveTextureFromMetadataDict:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _createGlobalToneCurveTextureFromMetadataDict:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _createGlobalToneCurveTextureFromMetadataDict:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _getComponentCountOfFormat:]
+ -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.17
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.18
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.19
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.15
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createSingleChannelPixelBufferViewFromPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 createSingleChannelPixelBufferViewFromPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createSingleChannelPixelBufferViewFromPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 cropAndScale:inputValidBufferRect:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 downScalePixelBuffer:toPixelBuffer:inputROI:filterOption:rotation:]
+ -[CMISmartStyleProcessorUtilitiesV1 downScalePixelBuffer:toPixelBuffer:inputROI:gdcParams:applyGDC:rotation:]
+ -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:]
+ -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:]
+ -[CMISmartStyleProcessorUtilitiesV1 propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.4
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.5
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.6
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.7
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.8
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.9
+ -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSMGProcessingSession:]
+ -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSMGProcessingSession:].cold.1
+ -[CMISmartStyleProcessorV1 purgeResources].cold.2
+ -[CMISmartStyleProcessorV1 setUseSemanticSRLByDefault:]
+ -[CMISmartStyleProcessorV1 useSemanticSRLByDefault]
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._computeOnlySubjectRelighting
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._inputWeightPlanePixelBufferScaledForISPSMG
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._createThumbnailPipelineState
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._createThumbnailsPipelineStateWithGDC
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._extractThumbnailPipelineState
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._maskCropAndScalePipelineState
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._postLTMUnstyledThumbnailPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._preLTMLinearMetadataThumbnailPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._intermediateRendererInputUnstyledPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._intermediateRendererInputUnstyledThumbnailPixelBuffer
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._ispSMGProcessingSession
+ OBJC_IVAR_$_CMISmartStyleProcessorV1._useSemanticSRLByDefault
+ _CGRectIsNull
+ _CMSampleBufferGetImageBuffer
+ _CVBufferCopyAttachment
+ _CVBufferSetAttachment
+ _CVPixelBufferCreateWithParentPixelBuffer
+ _CVPixelBufferGetAttributes
+ _CVPixelFormatDescriptionCreateWithPixelFormatType
+ _FigCFDictionaryGetInt32IfPresent
+ _FigCapturePixelFormatIs444
+ _FigCapturePixelFormatIsBGRA
+ _FigSignalErrorAt3
+ _OBJC_CLASS_$_CMISmartStyleUtilitiesV1
+ _OBJC_CLASS_$_MTLTextureDescriptor
+ _OBJC_CLASS_$_NSConstantArray
+ _OUTLINED_FUNCTION_10
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
+ _OUTLINED_FUNCTION_3
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
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___chkstk_darwin
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _kCVImageBufferColorPrimariesKey
+ _kCVImageBufferTransferFunctionKey
+ _kCVImageBufferTransferFunction_Linear
+ _kCVImageBufferYCbCrMatrixKey
+ _kCVPixelFormatBitsPerComponent
+ _kFigCaptureStreamLTMThumbnailKey_Format
+ _kFigCaptureStreamMetadata_GlobalToneCurveLookUpTable
+ _objc_msgSend$_createGlobalToneCurveTextureFromMetadataDict:
+ _objc_msgSend$_cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:
+ _objc_msgSend$_getComponentCountOfFormat:
+ _objc_msgSend$blitPixelBuffer:inputValidBufferRect:toPixelBuffer:
+ _objc_msgSend$computeOnlySubjectRelighting
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:
+ _objc_msgSend$downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:rotation:
+ _objc_msgSend$downScalePixelBuffer:toPixelBuffer:inputROI:filterOption:rotation:
+ _objc_msgSend$downScalePixelBuffer:toPixelBuffer:inputROI:gdcParams:applyGDC:rotation:
+ _objc_msgSend$getDefaultProcessorConfigurationForStreamingAccelerated
+ _objc_msgSend$initWithOptionalMetalCommandQueue:ispSMGProcessingSession:
+ _objc_msgSend$inputWeightPlanePixelBufferScaledForISPSMG
+ _objc_msgSend$intermediateStyleRendererThumbnailSizeForUseCase:
+ _objc_msgSend$newTextureWithDescriptor:
+ _objc_msgSend$replaceRegion:mipmapLevel:withBytes:bytesPerRow:
+ _objc_msgSend$setDepth:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setInputWeightPlanePixelBufferScaledForISPSMG:
+ _objc_msgSend$setIspSMGProcessingSession:
+ _objc_msgSend$setPixelFormat:
+ _objc_msgSend$setTextureType:
+ _objc_msgSend$setUsage:
+ _objc_msgSend$setUseSemanticSRLByDefault:
+ _objc_msgSend$setWidth:
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _os_log_type_enabled
- -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.5
- -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.6
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.10
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.11
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.12
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.13
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.5
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.6
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.7
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.8
- -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.9
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:]
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.1
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.2
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.3
- -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.4
- -[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:].cold.1
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:]
- -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:].cold.1
- -[CMISmartStyleProcessorV1 process].cold.1
- -[CMISmartStyleProcessorV1 process].cold.10
- -[CMISmartStyleProcessorV1 process].cold.11
- -[CMISmartStyleProcessorV1 process].cold.12
- -[CMISmartStyleProcessorV1 process].cold.13
- -[CMISmartStyleProcessorV1 process].cold.14
- -[CMISmartStyleProcessorV1 process].cold.15
- -[CMISmartStyleProcessorV1 process].cold.16
- -[CMISmartStyleProcessorV1 process].cold.17
- -[CMISmartStyleProcessorV1 process].cold.18
- -[CMISmartStyleProcessorV1 process].cold.19
- -[CMISmartStyleProcessorV1 process].cold.2
- -[CMISmartStyleProcessorV1 process].cold.20
- -[CMISmartStyleProcessorV1 process].cold.3
- -[CMISmartStyleProcessorV1 process].cold.4
- -[CMISmartStyleProcessorV1 process].cold.5
- -[CMISmartStyleProcessorV1 process].cold.6
- -[CMISmartStyleProcessorV1 process].cold.7
- -[CMISmartStyleProcessorV1 process].cold.8
- -[CMISmartStyleProcessorV1 process].cold.9
- OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._extractLinearThumbnailPipelineState
- OBJC_IVAR_$_CMISmartStyleProcessorV1._styleRendererInputUnstyledThumbnailPixelBuffer
- _FigSignalErrorAt
- ___stack_chk_fail
- ___stack_chk_guard
- _fig_log_get_emitter
- _objc_msgSend$copyFromTexture:toTexture:
- _objc_msgSend$downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:
- _objc_retain_x25
- _objc_retain_x4
CStrings:
+ "\r"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "( inputPreLTMThumbnailFormat == kFigCaptureStreamPreLTMThumbnailFormat_YlinRGBYavg ) || ( inputPreLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_YlinRGBYavg ) || ( inputPreLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_RGB ) || ( inputPreLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_RGBRGB )"
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
+ "-[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 _getComponentCountOfFormat:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:inputValidBufferRect:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 getLTMThumbnailFormatFromSampleBuffer:outputFormat:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureOutputStyledThumbnailPixelBufferForPixelBufferRenderer:unstyledThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _requestedMemSize:]"
+ "-[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:]"
+ "-[CMISmartStyleProcessorV1 finishProcessing]"
+ "-[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:ispSMGProcessingSession:]"
+ "-[CMISmartStyleProcessorV1 init]"
+ "-[CMISmartStyleProcessorV1 prepareToProcess:]"
+ "-[CMISmartStyleProcessorV1 prewarm]"
+ "-[CMISmartStyleProcessorV1 process]"
+ "-[CMISmartStyleProcessorV1 purgeResources]"
+ "-[CMISmartStyleProcessorV1 resetState]"
+ "-[CMISmartStyleProcessorV1 setup]"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>>"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: MetalContext is nil"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Shaders compilation failed."
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Unable to init CMISmartStyleOvercaptureThumbnailGenerator."
+ "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %s: Unable to load the bundle for CMISmartStyleOvercaptureThumbnailGenerator."
+ "<<<< CMISmartStyleProcessor >>>>"
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
+ "<<<< CMISmartStyleProcessor >>>> %s: Metal command queue is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: MetalContext is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: Setting up SmartStyleProcessor with ISP SMG processing session: %p"
+ "<<<< CMISmartStyleProcessor >>>> %s: Setting up SmartStyleProcessor with provided metal command queue."
+ "<<<< CMISmartStyleProcessor >>>> %s: Smart style engine processor failed to prepare to process (err:%d)"
+ "<<<< CMISmartStyleProcessor >>>> %s: SmartStyle Processor (label:%@) is requesting memory of size:%zu"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor configuration"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor input output"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to initialize a smart style processor instance"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unable to load the bundle for smart style processor."
+ "<<<< CMISmartStyleProcessor >>>> %s: Unexpected state: after receiving valid masks curve parameter must stay valid"
+ "<<<< CMISmartStyleProcessor >>>> %s: Unsupported Smart Style version %d"
+ "<<<< CMISmartStyleProcessor >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< CMISmartStyleProcessor >>>> %s: _smartStylePixelBufferRenderer is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _styleEngineProcessor is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _subjectRelightingStage is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: _utilities is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< CMISmartStyleProcessor >>>> %s: prepareToProcess for %d"
+ "<<<< CMISmartStyleProcessor >>>> %s: requesting GPU metal heap size without preparing to process for processor (label:%@), requesting the max size:%zu "
+ "<<<< CMISmartStyleProcessorUtilities >>>>"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping data has invalid threshold bin index"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping data is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping header dataSize is invalid"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping header is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Clipping metadata is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to bind original mask pixel buffer as texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to bind refined mask pixel buffer as texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Failed to create identity transform coefficients, err = %d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Invalud clipping data grid size"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: LTM thumbnail size coming from ISP is %dx%d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size height sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size width sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Style engine processor is nil. Unable to init a smart style processor utilities"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction linear thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction to linear thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction to unstyled thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to create a metal texture cache"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get GDC params, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get component count of format"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get metal texture address"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to initialize a smart style processor instance"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: _coefficientsProcessor is nil. Unable to init a smart style processor utilities."
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
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskTexture is nil"
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
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: metal context is nil. Unable to init a smart style processor utilities."
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputFormat is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputMaskTexture is nil"
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
+ "@32@0:8@\"<MTLCommandQueue>\"16^{OpaqueFigCaptureISPProcessingSession=}24"
+ "@32@0:8@16^{OpaqueFigCaptureISPProcessingSession=}24"
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
+ "Count not create new, single channel equivalent pixel buffer"
+ "Downscaling input linear pixel buffer to the linear thumbnail pixel buffer failed"
+ "Downscaling input target pixel buffer to style engine input target styled thumbnail pixel buffer failed"
+ "Downscaling input unstyled pixel buffer to the style renderer unstyled pixel buffer failed"
+ "Downscaling input unstyled thumbnail pixel buffer to the style renderer unstyled thumbnail pixel buffer failed"
+ "Downscaling style renderer styled output to style engine input target thumbnail pixel buffer failed"
+ "Downscaling style renderer unstyled thumbnail to style engine input unstyled thumbnail pixel buffer failed"
+ "Expected to have inputUnstyledPixelBuffer to satisfy the requirements of the style pixel buffer renderer."
+ "Expected to have non empty inputUnstyledCropRect for configuring the style pixel buffer renderer"
+ "Failed to load tuning parameters"
+ "FigCFDictionaryGetCGRectIfPresent( (__bridge CFDictionaryRef)inputLTMThumbnailMetadata, kFigCaptureStreamMetadata_ValidBufferRect, &inputPostLTMThumbnailValidBufferRect )"
+ "FigCFDictionaryGetCGRectIfPresent( (__bridge CFDictionaryRef)inputLTMThumbnailMetadata, kFigCaptureStreamMetadata_ValidBufferRect, &inputPreLTMThumbnailValidBufferRect )"
+ "FigCFDictionaryGetInt32IfPresent( (__bridge CFDictionaryRef)inputLTMThumbnailMetadata, kFigCaptureStreamPreLTMThumbnailKey_Format, &inputLTMThumbnailFormat )"
+ "FigCFDictionaryGetInt32IfPresent( (__bridge CFDictionaryRef)inputPreLTMThumbnailMetadata, kFigCaptureStreamPreLTMThumbnailKey_Format, &inputPreLTMThumbnailFormat )"
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
+ "TB,N,V_computeOnlySubjectRelighting"
+ "TB,N,V_useSemanticSRLByDefault"
+ "T^{__CVBuffer=},N,V_inputWeightPlanePixelBufferScaledForISPSMG"
+ "Unable to cache pixel buffer texture"
+ "Unable to create an intermediate buffer for input unstyled thumbnail pixel buffer for configuring the renderer."
+ "Unable to create an intermediate buffer to for unstyled input thumbnail for style engine learning"
+ "Unable to create an intermediate buffer to produce styled rendering"
+ "Unable to create postLTM unstyled thumbnail pixel buffer"
+ "Unable to create preLTM linear metadata thumbnail pixel buffer"
+ "Unable to get texture address"
+ "Unsupported pixel buffer format for input"
+ "Unsupported pixel buffer format for output"
+ "Unsupported processing type"
+ "^{OpaqueFigCaptureISPProcessingSession=}"
+ "^{__CVBuffer=}24@0:8^{__CVBuffer=}16"
+ "_cmImagingAllocator is NULL"
+ "_computeOnlySubjectRelighting"
+ "_createGlobalToneCurveTextureFromMetadataDict:"
+ "_createLinearThumbnailCroppedToPreLTMPipelineState is NULL"
+ "_createLinearThumbnailCroppedToPreLTMPipelineStateWithGDC is NULL"
+ "_createLinearThumbnailPipelineState is NULL"
+ "_createLinearThumbnailPipelineStateWithGDC is NULL"
+ "_createThumbnailPipelineState"
+ "_createThumbnailPipelineState is NULL"
+ "_createThumbnailsPipelineStateWithGDC"
+ "_createThumbnailsPipelineStateWithGDC is NULL"
+ "_cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:"
+ "_extractThumbnailPipelineState"
+ "_extractThumbnailPipelineState is NULL"
+ "_getComponentCountOfFormat:"
+ "_inputWeightPlanePixelBufferScaledForISPSMG"
+ "_intermediateRendererInputUnstyledPixelBuffer"
+ "_intermediateRendererInputUnstyledThumbnailPixelBuffer"
+ "_ispSMGProcessingSession"
+ "_maskCropAndScalePipelineState"
+ "_maskCropAndScalePipelineState is NULL"
+ "_maskFalsePositiveRejectionPipelineState is NULL"
+ "_maskUndistortPipelineState is NULL"
+ "_postLTMUnstyledThumbnailPixelBuffer"
+ "_preLTMLinearMetadataThumbnailPixelBuffer"
+ "_useSemanticSRLByDefault"
+ "allocatorBackend is  nil"
+ "allocatorDesc is NULL"
+ "blitPixelBuffer:inputValidBufferRect:toPixelBuffer:"
+ "cmismartstyleovercapturethumbnailgenerator_trace"
+ "cmismartstyleprocessor_trace"
+ "cmismartstyleprocessorutilities_trace"
+ "commandBuffer is NULL"
+ "commandBufferToUse is NULL"
+ "computeEncoder is NULL"
+ "computeOnlySubjectRelighting"
+ "containsObject:"
+ "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
+ "count >= 64"
+ "createLinearThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:"
+ "createSingleChannelPixelBufferViewFromPixelBuffer:"
+ "createUnstyledThumbnailFromMetadata:ltmThumbnailPixelBuffer:cameraInfo:applyGDC:toPixelBuffer:"
+ "cropAndScale:inputValidBufferRect:toPixelBuffer:"
+ "downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:rotation:"
+ "downScalePixelBuffer:toPixelBuffer:inputROI:filterOption:rotation:"
+ "downScalePixelBuffer:toPixelBuffer:inputROI:gdcParams:applyGDC:rotation:"
+ "err"
+ "getDefaultProcessorConfigurationForStreamingAccelerated"
+ "getDefaultProcessorConfigurationForStreamingAcceleratedWithFilterType:"
+ "getLTMThumbnailFormatFromSampleBuffer:outputFormat:"
+ "gtcValues"
+ "i188@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32{?=ff[8f][8f]f}64B176Q180"
+ "i32@0:8^{opaqueCMSampleBuffer=}16^i24"
+ "i52@0:8@\"NSDictionary\"16^{__CVBuffer=}24@\"NSDictionary\"32B40^{__CVBuffer=}44"
+ "i52@0:8@16^{__CVBuffer=}24@32B40^{__CVBuffer=}44"
+ "i64@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24^{__CVBuffer=}56"
+ "i80@0:8^{__CVBuffer=}16@\"NSDictionary\"24{CGRect={CGPoint=dd}{CGSize=dd}}32@\"NSDictionary\"64^{__CVBuffer=}72"
+ "i80@0:8^{__CVBuffer=}16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@64^{__CVBuffer=}72"
+ "i80@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32Q64Q72"
+ "initWithOptionalMetalCommandQueue:ispSMGProcessingSession:"
+ "input SRL pixel buffer is NULL"
+ "inputLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_RGB || inputLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_RGBRGB"
+ "inputLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_RGBRGB"
+ "inputLTMThumbnailMetadata"
+ "inputLTMThumbnailMetadata is NULL"
+ "inputLTMThumbnailPixelBuffer"
+ "inputLTMThumbnailSampleBuffer"
+ "inputLinearPixelBuffer is NULL"
+ "inputPostLTMThumbnail valid buffer rect is not available"
+ "inputPreLTMThumbnailFormat == kFigCaptureStreamLTMThumbnailFormat_YlinRGBYavg"
+ "inputPreLTMThumbnailFormat is incorrect (YlinRGBYavg, RGB, or RGBRGB is expected)"
+ "inputWeightPlanePixelBufferScaledForISPSMG"
+ "intermediateStyleRendererThumbnailSizeForUseCase:"
+ "kCMBaseObjectError_ParamErr"
+ "newPixelBuffer"
+ "newTextureWithDescriptor:"
+ "outputFormat"
+ "postLTMImageGlobalToneCurveTexture"
+ "postLTMImageGlobalToneCurveTexture is NULL"
+ "propagatePixelBufferColorAttachments:toPixelBuffer:forceLinearTransferFunction:"
+ "refinedMaskTexture.height == originalMaskTexture.height is NULL"
+ "refinedMaskTexture.width == originalMaskTexture.width is NULL"
+ "replaceRegion:mipmapLevel:withBytes:bytesPerRow:"
+ "setComputeOnlySubjectRelighting:"
+ "setDepth:"
+ "setHeight:"
+ "setInputWeightPlanePixelBufferScaledForISPSMG:"
+ "setIspSMGProcessingSession:"
+ "setPixelFormat:"
+ "setTextureType:"
+ "setUsage:"
+ "setUseSemanticSRLByDefault:"
+ "setWidth:"
+ "smartStyleCreateThumbnail"
+ "smartStyleExtractLTMThumbnail"
+ "undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:"
+ "useSemanticSRLByDefault"
- "\n"
- "_extractLinearThumbnailPipelineState"
- "_styleRendererInputUnstyledThumbnailPixelBuffer"
- "blitPixelBuffer:toPixelBuffer:"
- "copyFromTexture:toTexture:"
- "downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:"
- "i56@0:8^{__CVBuffer=}16^{__CVBuffer=}24@\"NSDictionary\"32@\"NSDictionary\"40^{__CVBuffer=}48"
- "i56@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40^{__CVBuffer=}48"
- "inputPreLTMThumbnailFormat == kFigCaptureStreamPreLTMThumbnailFormat_YlinRGBYavg"
- "smartStyleExtractLinearThumbnail"
- "undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:"

```
