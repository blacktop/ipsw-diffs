## CameraEffectsKit

> `/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`

```diff

-6311.0.0.0.0
-  __TEXT.__text: 0x109ae4
+6311.1.1.0.0
+  __TEXT.__text: 0x10a4d0
   __TEXT.__auth_stubs: 0x1c50
-  __TEXT.__objc_methlist: 0x124b4
-  __TEXT.__const: 0x1a90
-  __TEXT.__gcc_except_tab: 0x27b0
-  __TEXT.__cstring: 0x6833
-  __TEXT.__oslogstring: 0x8146
-  __TEXT.__unwind_info: 0x45b0
-  __TEXT.__objc_classname: 0x1fe9
-  __TEXT.__objc_methname: 0x37c52
-  __TEXT.__objc_methtype: 0xaad1
-  __TEXT.__objc_stubs: 0x243a0
-  __DATA_CONST.__got: 0x1a28
+  __TEXT.__objc_methlist: 0x124fc
+  __TEXT.__const: 0x1aa0
+  __TEXT.__gcc_except_tab: 0x27ac
+  __TEXT.__cstring: 0x685b
+  __TEXT.__oslogstring: 0x81d4
+  __TEXT.__unwind_info: 0x45d8
+  __TEXT.__objc_classname: 0x1fea
+  __TEXT.__objc_methname: 0x37eeb
+  __TEXT.__objc_methtype: 0xab10
+  __TEXT.__objc_stubs: 0x245e0
+  __DATA_CONST.__got: 0x1a40
   __DATA_CONST.__const: 0x36f0
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae68
+  __DATA_CONST.__objc_selrefs: 0xaf00
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0x240
   __AUTH_CONST.__auth_got: 0xe40
   __AUTH_CONST.__const: 0x1308
-  __AUTH_CONST.__cfstring: 0x6680
-  __AUTH_CONST.__objc_const: 0x298c0
+  __AUTH_CONST.__cfstring: 0x66c0
+  __AUTH_CONST.__objc_const: 0x299e0
   __AUTH_CONST.__objc_intobj: 0x720
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x4060
-  __DATA.__objc_ivar: 0x14bc
+  __DATA.__objc_ivar: 0x14dc
   __DATA.__data: 0x2670
-  __DATA.__bss: 0xa88
+  __DATA.__bss: 0xa98
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /System/Library/PrivateFrameworks/CameraUI.framework/CameraUI
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
+  - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis
   - /System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate
+  - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /System/Library/PrivateFrameworks/ProVideo.framework/ProVideo
   - /System/Library/PrivateFrameworks/iMessageApps.framework/iMessageApps
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8EF7F08-93A0-3764-87B8-B080BC219C02
-  Functions: 7185
-  Symbols:   25211
-  CStrings:  11910
+  UUID: E99DD1CA-81CD-3FAF-BFF5-C99311DAEA35
+  Functions: 7198
+  Symbols:   25271
+  CStrings:  11947
 
Symbols:
+ -[CFXRenderer createJFXAnimojiEffectRenderer]
+ -[JFXAnimojiEffectRenderer computeHighQualitySegmentation:]
+ -[JFXAnimojiEffectRenderer computeHighQualitySegmentation:].cold.1
+ -[JFXAnimojiEffectRenderer computeHighQualitySegmentation:].cold.2
+ -[JFXAnimojiEffectRenderer deviceOrientedColorBufferPool]
+ -[JFXAnimojiEffectRenderer initWithConstrainedHeadPose:rgbOnlyMemoji:]
+ -[JFXAnimojiEffectRenderer rgbOnlyMemoji]
+ -[JFXAnimojiEffectRenderer setDeviceOrientedColorBufferPool:]
+ -[JFXAnimojiEffectRenderer setupInputBufferPoolForSize:capturedImage:]
+ -[JFXAnimojiEffectRenderer setupInputBufferPoolForSize:capturedImage:].cold.1
+ -[JFXAnimojiEffectRenderer useDepth]
+ _JFXRGBOnlyMemoji
+ _JFXRGBOnlyMemoji.onceToken
+ _JFXRGBOnlyMemoji.rgbOnlyMemoji
+ _OBJC_CLASS_$_PTEffect
+ _OBJC_CLASS_$_PTEffectDescriptor
+ _OBJC_CLASS_$_PTEffectRenderRequest
+ _OBJC_IVAR_$_CFXRenderer._isAnimojiOnlyMode
+ _OBJC_IVAR_$_CFXRenderer._rgbOnlyMemoji
+ _OBJC_IVAR_$_JFXAnimojiEffectRenderer._deviceOrientedColorBufferPool
+ _OBJC_IVAR_$_JFXAnimojiEffectRenderer._effect
+ _OBJC_IVAR_$_JFXAnimojiEffectRenderer._rgbOnlyMemoji
+ _OBJC_IVAR_$_JFXAnimojiEffectRenderer._segmentationPixelBuffer
+ _OBJC_IVAR_$_JFXAnimojiEffectRenderer._transferSession
+ _OBJC_IVAR_$_JFXVideoCameraController._rgbOnlyMemoji
+ ___128-[JFXAnimojiEffectRenderer asyncLoadNewPuppet:currentPuppet:captureOrientation:interfaceOrientation:primeFrame:backgroundColor:]_block_invoke.59
+ ___JFXRGBOnlyMemoji_block_invoke
+ ___JFXRGBOnlyMemoji_block_invoke.cold.1
+ ___JFXRGBOnlyMemoji_block_invoke.cold.2
+ ___block_descriptor_72_e8_32bs40w_e28_v16?0"<MTLCommandBuffer>"8lw40l8s32l8
+ ___block_literal_global.650
+ ___block_literal_global.660
+ ___block_literal_global.662
+ ___block_literal_global.666
+ ___block_literal_global.671
+ _objc_msgSend$computeHighQualitySegmentation:
+ _objc_msgSend$createJFXAnimojiEffectRenderer
+ _objc_msgSend$deviceOrientedColorBufferPool
+ _objc_msgSend$initWithConstrainedHeadPose:rgbOnlyMemoji:
+ _objc_msgSend$initWithDescriptor:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$personSegmentationMatteFormatForColorSize:
+ _objc_msgSend$render:
+ _objc_msgSend$setActiveEffectType:
+ _objc_msgSend$setAvailableEffectTypes:
+ _objc_msgSend$setColorSize:
+ _objc_msgSend$setDeviceOrientedColorBufferPool:
+ _objc_msgSend$setInColorBuffer:
+ _objc_msgSend$setMetalCommandQueue:
+ _objc_msgSend$setOutColorBuffer:
+ _objc_msgSend$setOutPersonSegmentationMatteBuffer:
+ _objc_msgSend$setSyncInitialization:
+ _objc_msgSend$setupInputBufferPoolForSize:capturedImage:
+ _objc_msgSend$useDepth
- -[JFXAnimojiEffectRenderer initWithConstrainedHeadPose:]
- -[JFXAnimojiEffectRenderer setupInputBufferPoolForSize:]
- GCC_except_table32
- ___128-[JFXAnimojiEffectRenderer asyncLoadNewPuppet:currentPuppet:captureOrientation:interfaceOrientation:primeFrame:backgroundColor:]_block_invoke.57
- ___block_descriptor_80_e8_32s40bs48w_e28_v16?0"<MTLCommandBuffer>"8lw48l8s40l8s32l8
- ___block_literal_global.649
- ___block_literal_global.659
- ___block_literal_global.661
- ___block_literal_global.665
- ___block_literal_global.670
- _objc_msgSend$initWithConstrainedHeadPose:
CStrings:
+ "@\"PTEffect\""
+ "@24@0:8B16B20"
+ "CVPixelBufferCreate failed %d"
+ "CVTPixelTransferSessionTransferImage failed %d"
+ "NoDepthMemoji"
+ "PTEffect render: failed %d"
+ "Set NoDepthMemoji to %i using default"
+ "TB,R,N,V_rgbOnlyMemoji"
+ "T^{__CVPixelBufferPool=},N,V_deviceOrientedColorBufferPool"
+ "_deviceOrientedColorBufferPool"
+ "_isAnimojiOnlyMode"
+ "_rgbOnlyMemoji"
+ "_segmentationPixelBuffer"
+ "_transferSession"
+ "com.apple.VideoConference"
+ "computeHighQualitySegmentation:"
+ "createJFXAnimojiEffectRenderer"
+ "deviceOrientedColorBufferPool"
+ "initWithConstrainedHeadPose:rgbOnlyMemoji:"
+ "initWithDescriptor:"
+ "initWithSuiteName:"
+ "personSegmentationMatteFormatForColorSize:"
+ "render:"
+ "rgbOnlyMemoji"
+ "setActiveEffectType:"
+ "setAvailableEffectTypes:"
+ "setColorSize:"
+ "setDeviceOrientedColorBufferPool:"
+ "setInColorBuffer:"
+ "setMetalCommandQueue:"
+ "setOutColorBuffer:"
+ "setOutPersonSegmentationMatteBuffer:"
+ "setSyncInitialization:"
+ "setupInputBufferPoolForSize:capturedImage:"
+ "useDepth"
+ "v40@0:8{CGSize=dd}16^{__CVBuffer=}32"
- "initWithConstrainedHeadPose:"

```
