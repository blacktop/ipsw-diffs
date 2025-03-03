## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-587.82.13.0.0
-  __TEXT.__text: 0xa7bc
-  __TEXT.__auth_stubs: 0x420
+587.100.15.0.0
+  __TEXT.__text: 0x12b4c
+  __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0xa70
+  __TEXT.__objc_methlist: 0x13d4
+  __TEXT.__const: 0x68
   __TEXT.__objc_methname: 0x4301
-  __TEXT.__cstring: 0x14db
+  __TEXT.__cstring: 0x2d72
+  __TEXT.__oslogstring: 0x209a
   __TEXT.__objc_classname: 0x25e
   __TEXT.__objc_methtype: 0x10c6
-  __TEXT.__const: 0x28
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x218
+  __TEXT.__unwind_info: 0x2b8
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x280
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3710
-  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_const: 0x24e8
+  __DATA.__objc_selrefs: 0xa18
   __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 218
-  Symbols:   823
-  CStrings:  828
+  Functions: 409
+  Symbols:   1040
+  CStrings:  1028
 
Symbols:
+ +[CMISmartStyleProcessorSettingsV1 sharedInstance].cold.1
+ -[CMISmartStyleOvercaptureThumbnailGenerator _bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:].cold.1
+ -[CMISmartStyleOvercaptureThumbnailGenerator _bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:].cold.2
+ -[CMISmartStyleOvercaptureThumbnailGenerator _compileShaders].cold.1
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.1
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.2
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.3
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.4
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.5
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.6
+ -[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:].cold.7
+ -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.1
+ -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.2
+ -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.3
+ -[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:].cold.4
+ -[CMISmartStyleProcessorInputOutputV1 init].cold.1
+ -[CMISmartStyleProcessorStillImageConfigurationV1 init].cold.1
+ -[CMISmartStyleProcessorStreamingConfigurationV1 init].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 _compileShaders].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.15
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.17
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.18
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.19
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.10
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.11
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.12
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.13
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.14
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.15
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.16
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:].cold.9
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.7
+ -[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:].cold.8
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.6
+ -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:].cold.7
+ -[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:].cold.1
+ -[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:].cold.2
+ -[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:].cold.3
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.1
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.2
+ -[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:].cold.3
+ -[CMISmartStyleProcessorV1 _configureOutputStyledThumbnailPixelBufferForPixelBufferRenderer:unstyledThumbnailPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:].cold.1
+ -[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:].cold.2
+ -[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorV1 _requestedMemSize:].cold.1
+ -[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:].cold.1
+ -[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:].cold.2
+ -[CMISmartStyleProcessorV1 finishProcessing].cold.1
+ -[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:].cold.1
+ -[CMISmartStyleProcessorV1 init].cold.1
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.1
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.10
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.11
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.12
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.13
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.14
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.15
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.16
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.2
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.3
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.4
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.5
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.6
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.7
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.8
+ -[CMISmartStyleProcessorV1 prepareToProcess:].cold.9
+ -[CMISmartStyleProcessorV1 prewarm].cold.1
+ -[CMISmartStyleProcessorV1 prewarm].cold.2
+ -[CMISmartStyleProcessorV1 prewarm].cold.3
+ -[CMISmartStyleProcessorV1 prewarm].cold.4
+ -[CMISmartStyleProcessorV1 prewarm].cold.5
+ -[CMISmartStyleProcessorV1 prewarm].cold.6
+ -[CMISmartStyleProcessorV1 process].cold.1
+ -[CMISmartStyleProcessorV1 process].cold.10
+ -[CMISmartStyleProcessorV1 process].cold.11
+ -[CMISmartStyleProcessorV1 process].cold.12
+ -[CMISmartStyleProcessorV1 process].cold.13
+ -[CMISmartStyleProcessorV1 process].cold.14
+ -[CMISmartStyleProcessorV1 process].cold.15
+ -[CMISmartStyleProcessorV1 process].cold.16
+ -[CMISmartStyleProcessorV1 process].cold.17
+ -[CMISmartStyleProcessorV1 process].cold.18
+ -[CMISmartStyleProcessorV1 process].cold.19
+ -[CMISmartStyleProcessorV1 process].cold.2
+ -[CMISmartStyleProcessorV1 process].cold.20
+ -[CMISmartStyleProcessorV1 process].cold.3
+ -[CMISmartStyleProcessorV1 process].cold.4
+ -[CMISmartStyleProcessorV1 process].cold.5
+ -[CMISmartStyleProcessorV1 process].cold.6
+ -[CMISmartStyleProcessorV1 process].cold.7
+ -[CMISmartStyleProcessorV1 process].cold.8
+ -[CMISmartStyleProcessorV1 process].cold.9
+ -[CMISmartStyleProcessorV1 purgeResources].cold.1
+ -[CMISmartStyleProcessorV1 purgeResources].cold.2
+ -[CMISmartStyleProcessorV1 resetState].cold.1
+ -[CMISmartStyleProcessorV1 resetState].cold.2
+ -[CMISmartStyleProcessorV1 setup].cold.1
+ -[CMISmartStyleProcessorV1 setup].cold.2
+ -[CMISmartStyleProcessorV1 setup].cold.3
+ -[CMISmartStyleProcessorV1 setup].cold.4
+ -[CMISmartStyleProcessorV1 setup].cold.5
+ _FigSignalErrorAt3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain_x23
+ _os_log_type_enabled
- _FigSignalErrorAt
- _fig_log_get_emitter
- _objc_retain_x22
- _objc_retain_x25
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
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
+ "-[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:]"
+ "-[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureOutputStyledThumbnailPixelBufferForPixelBufferRenderer:unstyledThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:]"
+ "-[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:]"
+ "-[CMISmartStyleProcessorV1 _requestedMemSize:]"
+ "-[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:]"
+ "-[CMISmartStyleProcessorV1 finishProcessing]"
+ "-[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:]"
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
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size height sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: PreLTM thumbnail size width sent is too big"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Style engine processor is nil. Unable to init a smart style processor utilities"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to apply GDC correction linear thumbnail as cameraInfo is nil, bypassing GDC correction"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to create a metal texture cache"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: Unable to get GDC params, bypassing GDC correction"
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
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain blue channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain green channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData doesn't contain red channel"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData has wrong size"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputLinearThumbnailData is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMetadata is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputOutputPreLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPostLTMThumbnailPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPostLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPreLTMPixelBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputPreLTMThumbnailBuffer is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputTexture for blit is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: metal context is nil. Unable to init a smart style processor utilities."
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputMaskTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputPixelBuffer is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputTexture for blit is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: pixelBuffer is NULL"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: postLTMThumbnailTexture is nil"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTM thumbnail size coming from ISP is %dx%d"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail (%d,%d) - ROI is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with clipping metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with fallback clipping metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnail ROI computed with mapped sensor rect metadata is (%f,%f,%f,%f)"
+ "<<<< CMISmartStyleProcessorUtilities >>>> %s: preLTMThumbnailTexture is nil"
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
+ "Could not bind destination pixel buffer"
+ "Could not bind source pixel buffer"
+ "Downscaling input linear pixel buffer to the linear thumbnail pixel buffer failed"
+ "Downscaling input target pixel buffer to style engine input target styled thumbnail pixel buffer failed"
+ "Downscaling input unstyled pixel buffer to the style renderer unstyled thumbnail pixel buffer failed"
+ "Downscaling style renderer styled output to style engine input target thumbnail pixel buffer failed"
+ "Downscaling style renderer unstyled thumbnail to style engine input unstyled thumbnail pixel buffer failed"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
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
+ "Unable to cache pixel buffer texture"
+ "Unable to create an intermediate buffer to for unstyled input thumbnail for style engine learning"
+ "Unable to create an intermediate buffer to produce styled rendering"
+ "Unable to find unstyled buffer to produce styled rendering"
+ "Unable to get texture address"
+ "Unsupported pixel buffer format for input"
+ "Unsupported pixel buffer format for output"
+ "Unsupported processing type"
+ "_cmImagingAllocator is NULL"
+ "_createLinearThumbnailCroppedToPreLTMPipelineState is NULL"
+ "_createLinearThumbnailCroppedToPreLTMPipelineStateWithGDC is NULL"
+ "_createLinearThumbnailPipelineState is NULL"
+ "_createLinearThumbnailPipelineStateWithGDC is NULL"
+ "_extractLinearThumbnailPipelineState is NULL"
+ "_maskFalsePositiveRejectionPipelineState is NULL"
+ "_maskUndistortPipelineState is NULL"
+ "allocatorBackend is  nil"
+ "allocatorDesc is NULL"
+ "cmismartstyleovercapturethumbnailgenerator_trace"
+ "cmismartstyleprocessor_trace"
+ "cmismartstyleprocessorutilities_trace"
+ "commandBuffer is NULL"
+ "commandBufferToUse is NULL"
+ "computeEncoder is NULL"
+ "err"
+ "input SRL pixel buffer is NULL"
+ "inputLinearPixelBuffer is NULL"
+ "kFigBaseObjectError_ParamErr"
+ "refinedMaskTexture.height == originalMaskTexture.height is NULL"
+ "refinedMaskTexture.width == originalMaskTexture.width is NULL"

```
