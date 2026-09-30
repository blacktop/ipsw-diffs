## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

```diff

-356.0.0.0.0
-  __TEXT.__text: 0x769d4
-  __TEXT.__auth_stubs: 0xe20
+356.100.0.0.0
+  __TEXT.__text: 0x76b30
+  __TEXT.__auth_stubs: 0xe10
   __TEXT.__objc_methlist: 0x5414
   __TEXT.__const: 0xa2c
-  __TEXT.__cstring: 0x1ddec
+  __TEXT.__cstring: 0x1de60
   __TEXT.__oslogstring: 0x2c7c
   __TEXT.__ustring: 0x66
-  __TEXT.__gcc_except_tab: 0xde8
-  __TEXT.__unwind_info: 0x1b90
+  __TEXT.__gcc_except_tab: 0xde4
+  __TEXT.__unwind_info: 0x1b98
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xa6f
-  __TEXT.__objc_methname: 0x10904
-  __TEXT.__objc_methtype: 0x2885
+  __TEXT.__objc_methname: 0x10949
+  __TEXT.__objc_methtype: 0x2874
   __TEXT.__objc_stubs: 0xc940
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x26e0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x62590
-  __AUTH_CONST.__auth_got: 0x728
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0xa40
   __AUTH_CONST.__cfstring: 0x248e0
-  __AUTH_CONST.__objc_const: 0xdad0
+  __AUTH_CONST.__objc_const: 0xdb10
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x7bc0
   __AUTH_CONST.__objc_doubleobj: 0x2370
   __AUTH_CONST.__objc_dictobj: 0x4ede0
   __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0xa3c
+  __DATA.__objc_ivar: 0xa44
   __DATA.__data: 0x788
-  __DATA.__bss: 0xaa8
+  __DATA.__bss: 0xab8
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/ARKit.framework/ARKit
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F70B677C-FEEA-38AE-831B-A37C45933D4F
-  Functions: 2478
-  Symbols:   9430
-  CStrings:  13027
+  UUID: 9098AD18-3FBF-3DEC-A34F-7297D8AF9CBA
+  Functions: 2479
+  Symbols:   9433
+  CStrings:  13028
 
Symbols:
+ -[AVTARMaskRenderer allocateTexturesIfNeededWithDestinationPixelFormat:framebufferSize:]
+ -[AVTARMaskRenderer encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:debugARFrameDepthTexture:]
+ _AVTGetCapturedColorTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._arMatteGenerator
+ _OBJC_IVAR_$_AVTARMaskRenderer._arMatteTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugARFrameColorTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugARFrameDepthTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._debugARFrameSegmentationBufferTexture
+ _OBJC_IVAR_$_AVTARMaskRenderer._framebufferSize
+ _OBJC_IVAR_$_AVTARMaskRenderer._lock
+ _objc_msgSend$allocateTexturesIfNeededWithDestinationPixelFormat:framebufferSize:
+ _objc_msgSend$encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:debugARFrameDepthTexture:
- -[AVTARMaskRenderer allocateTexturesIfNeededWithDestinationPixelFormat:size:]
- -[AVTARMaskRenderer encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:]
- _NSClassFromString
- _OBJC_IVAR_$_AVTARMaskRenderer._debugCameraColorTexture
- _OBJC_IVAR_$_AVTARMaskRenderer._debugCameraDepthTexture
- _OBJC_IVAR_$_AVTARMaskRenderer._matteGenerator
- _OBJC_IVAR_$_AVTARMaskRenderer._matteTexture
- _OBJC_IVAR_$_AVTARMaskRenderer._renderSize
- _objc_msgSend$allocateTexturesIfNeededWithDestinationPixelFormat:size:
- _objc_msgSend$encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:
CStrings:
+ "[AvatarKit] AVTARMaskRenderer - Blur masks"
+ "[AvatarKit] AVTARMaskRenderer - Composite"
+ "[AvatarKit] AVTARMaskRenderer - Convert depth texture"
+ "[AvatarKit] AVTARMaskRenderer - Debug view"
+ "[AvatarKit] AVTARMaskRenderer - Generate masks"
+ "[AvatarKit] AVTARMaskRenderer - Matte generation"
+ "_arMatteGenerator"
+ "_arMatteTexture"
+ "_debugARFrameColorTexture"
+ "_debugARFrameDepthTexture"
+ "_debugARFrameSegmentationBufferTexture"
+ "_framebufferSize"
+ "allocateTexturesIfNeededWithDestinationPixelFormat:framebufferSize:"
+ "com.apple.clips"
+ "encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:debugARFrameDepthTexture:"
+ "v32@0:8Q1624"
+ "{?=\"headZ\"f\"shadowUVOffset\"f\"shadowMaskSizeU\"f\"shadowMaskSizeV\"f\"neckU\"f\"neckV\"f\"chromaKeyColorComponents\"\"captureTexcoords\"{?=\"columns\"[4]}}"
- "JFXAnimojiEffectRenderer"
- "[AvatarKit] Blur masks"
- "[AvatarKit] Composite"
- "[AvatarKit] Convert depth texture"
- "[AvatarKit] Debug"
- "[AvatarKit] Generate masks"
- "[AvatarKit] Matte generation"
- "_debugCameraColorTexture"
- "_debugCameraDepthTexture"
- "_matteGenerator"
- "_matteTexture"
- "_renderSize"
- "allocateTexturesIfNeededWithDestinationPixelFormat:size:"
- "encodeIntermediatePassesWithCommandBuffer:sceneColorTexture:sceneOnTopTexture:generatedMasksTexture:cameraDepthDebug:"
- "v40@0:8Q16{CGSize=dd}24"
- "{?=\"headZ\"f\"shadowUVOffset\"f\"shadowMaskSizeU\"f\"shadowMaskSizeV\"f\"neckU\"f\"neckV\"f\"chromaKeyColorComponents\"\"captureDeviceTexcoords\"{?=\"columns\"[4]}}"

```
