## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x1678c
+659.0.0.0.4
+  __TEXT.__text: 0x162ac
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x2120
-  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__objc_stubs: 0x2160
+  __TEXT.__objc_methlist: 0x159c
   __TEXT.__const: 0xa0
-  __TEXT.__objc_methname: 0x4abc
-  __TEXT.__cstring: 0x3a2e
-  __TEXT.__oslogstring: 0x2780
+  __TEXT.__objc_methname: 0x4b3d
+  __TEXT.__cstring: 0x3977
+  __TEXT.__oslogstring: 0x26a9
   __TEXT.__objc_classname: 0x25e
-  __TEXT.__objc_methtype: 0x1357
-  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_methtype: 0x13aa
+  __TEXT.__unwind_info: 0x328
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x2710
-  __DATA.__objc_selrefs: 0xb18
+  __DATA.__objc_selrefs: 0xb38
   __DATA.__objc_ivar: 0x1e4
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EEEA2FA5-5F2E-3AF0-8CC8-3CF67DDAAD53
-  Functions: 479
-  Symbols:   1163
-  CStrings:  1160
+  UUID: B76DE015-25F2-3D55-9736-1A83707A5733
+  Functions: 476
+  Symbols:   1162
+  CStrings:  1158
 
Symbols:
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.1
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.2
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.3
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.4
+ -[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:].cold.5
+ -[CMISmartStyleProcessorUtilitiesV1 cropAndScalePixelBuffer:inputValidBufferRect:toPixelBuffer:]
+ -[CMISmartStyleProcessorUtilitiesV1 undistortPixelBuffer:inputValidBufferRect:inputMetadata:cameraInfo:toPixelBuffer:]
+ -[CMISmartStyleProcessorV1 requiresReconfigurationForConfiguration:]
+ OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._maskCropAndScalePipelineStateWithGDC
+ _objc_msgSend$_cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:
+ _objc_msgSend$linearSystemOrder
+ _objc_msgSend$requiresReconfigurationForConfiguration:
+ _objc_msgSend$spotlightCount
+ _objc_msgSend$weightPlaneCount
+ _objc_retain_x4
- -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:]
- -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.1
- -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.2
- -[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:].cold.3
- -[CMISmartStyleProcessorUtilitiesV1 cropAndScale:inputValidBufferRect:toPixelBuffer:]
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:]
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.1
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.2
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.3
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.4
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.5
- -[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:].cold.6
- OBJC_IVAR_$_CMISmartStyleProcessorUtilitiesV1._maskUndistortPipelineState
- _objc_msgSend$_cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:
- _objc_msgSend$blitPixelBuffer:inputValidBufferRect:toPixelBuffer:
- _objc_msgSend$isEqual:
- _objc_retain_x3
CStrings:
+ "-[CMISmartStyleProcessorUtilitiesV1 _cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:]"
+ "_cropAndScale:inputValidBufferRect:applyGDC:inputMetadata:cameraInfo:toPixelBuffer:"
+ "_maskCropAndScalePipelineStateWithGDC"
+ "_maskCropAndScalePipelineStateWithGDC is NULL"
+ "cropAndScalePixelBuffer:inputValidBufferRect:toPixelBuffer:"
+ "i80@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@\"NSDictionary\"56@\"NSDictionary\"64^{__CVBuffer=}72"
+ "i80@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64^{__CVBuffer=}72"
+ "i84@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24B56@60@68^{__CVBuffer=}76"
+ "linearSystemOrder"
+ "requiresReconfigurationForConfiguration:"
+ "smartStyleCropAndScaleMask"
+ "spotlightCount"
+ "undistortPixelBuffer:inputValidBufferRect:inputMetadata:cameraInfo:toPixelBuffer:"
+ "weightPlaneCount"
- "-[CMISmartStyleProcessorUtilitiesV1 _cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:]"
- "-[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:]"
- "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskPixelBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %s: inputMaskTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %s: outputMaskTexture is nil"
- "Unable to get GDC params for masks, bypassing GDC correction"
- "_cropAndScaleToDestinationPixelBuffer:inputValidBufferRect:toPixelBuffer:"
- "_maskUndistortPipelineState"
- "_maskUndistortPipelineState is NULL"
- "cropAndScale:inputValidBufferRect:toPixelBuffer:"
- "i80@0:8^{__CVBuffer=}16@\"NSDictionary\"24{CGRect={CGPoint=dd}{CGSize=dd}}32@\"NSDictionary\"64^{__CVBuffer=}72"
- "i80@0:8^{__CVBuffer=}16@24{CGRect={CGPoint=dd}{CGSize=dd}}32@64^{__CVBuffer=}72"
- "inputMaskPixelBuffer"
- "outputMaskPixelBuffer"
- "smartStyleUndistortMask"
- "undistortMask:inputMetadata:inputValidBufferRect:cameraInfo:toPixelBuffer:"

```
