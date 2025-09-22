## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-492.0.0.0.0
-  __TEXT.__text: 0x9c4ac
-  __TEXT.__auth_stubs: 0x1390
+492.40.4.0.0
+  __TEXT.__text: 0x9d358
+  __TEXT.__auth_stubs: 0x13d0
   __TEXT.__delay_stubs: 0x2ec
   __TEXT.__delay_helper: 0x230
-  __TEXT.__objc_methlist: 0x9834
-  __TEXT.__const: 0x21250
-  __TEXT.__cstring: 0x6efe
-  __TEXT.__oslogstring: 0x47f9
-  __TEXT.__gcc_except_tab: 0x1818
+  __TEXT.__objc_methlist: 0x98d4
+  __TEXT.__const: 0x21260
+  __TEXT.__cstring: 0x6f41
+  __TEXT.__oslogstring: 0x48bb
+  __TEXT.__gcc_except_tab: 0x1844
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x20e8
-  __TEXT.__objc_classname: 0x136b
-  __TEXT.__objc_methname: 0x1ab67
-  __TEXT.__objc_methtype: 0x570e
-  __TEXT.__objc_stubs: 0xfa80
-  __DATA_CONST.__got: 0x8f0
+  __TEXT.__unwind_info: 0x2130
+  __TEXT.__objc_classname: 0x1390
+  __TEXT.__objc_methname: 0x1ae02
+  __TEXT.__objc_methtype: 0x57b2
+  __TEXT.__objc_stubs: 0xfc40
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x970
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5010
+  __DATA_CONST.__objc_selrefs: 0x5080
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x768
   __DATA_CONST.__vfx_script_tbl: 0x50
   __DATA_CONST.__vfx_script_tbx: 0x48
-  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0x1c9c0
+  __AUTH_CONST.__objc_const: 0x1cbc0
   __AUTH_CONST.__objc_intobj: 0xb40
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x1e50
   __AUTH.__data: 0x9e0
-  __DATA.__objc_ivar: 0x174c
+  __DATA.__objc_ivar: 0x177c
   __DATA.__data: 0x818
   __DATA.__bss: 0xe58
   __DATA_DIRTY.__objc_data: 0x1860

   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B329599-7D52-3296-9CFF-B4EECEF4FA64
-  Functions: 4037
-  Symbols:   15000
-  CStrings:  7588
+  UUID: 37A40EA7-42F7-39AF-B193-8F062C1C59B7
+  Functions: 4058
+  Symbols:   15083
+  CStrings:  7625
 
Symbols:
+ -[PTEffectPersonSegmentation dealloc]
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:]
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:].cold.1
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:].cold.2
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:].cold.3
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:].cold.4
+ -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:].cold.5
+ -[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]
+ -[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork].cold.1
+ -[PTEffectPersonSegmentation rotateInput:rotationDegrees:]
+ -[PTEffectPersonSegmentation rotateInput:rotationDegrees:].cold.1
+ -[PTEffectPersonSegmentation rotateOutput:segmentationOutput:rotationDegrees:]
+ -[PTEffectPersonSegmentation rotatedNetworkState]
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:transform:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:]
+ -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:transform:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:].cold.1
+ -[PTEffectPersonSegmentation setRotatedNetworkState:]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 outputPixelBuffer]
+ -[PTEffectPersonSegmentationViSegHQVisionCoreE5 segmentationSize]
+ -[PTEffectPersonSegmentationVision colorSize]
+ -[PTEffectPersonSegmentationVision outputPixelBuffer]
+ -[PTEffectPersonSegmentationVision segmentationSize]
+ -[PTPixelBufferUtil createPixelbufferFromCIImage:pixelFormat:]
+ -[PTPixelBufferUtil createPixelbufferFromCIImage:pixelFormat:].cold.1
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:]
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:]
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.1
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.2
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.3
+ -[PTPixelBufferUtil readPixelBufferFromFile:pixelFormat:ciOptions:].cold.4
+ _CGColorSpaceCopyICCData
+ _CVBufferSetAttachment
+ _OBJC_CLASS_$_CIContext
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_UTType
+ _OBJC_IVAR_$_PTEffect._pixelRotationSession
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._asyncInitQueue
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._colorSize
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._lastRotation
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._personSegmentationProvider
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._personSegmentationProviderRotated
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._ptUtil
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._rotated180InputPixelBuffer
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._rotatedInputPixelBuffer
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._rotatedNetworkState
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._unrotated180OutputSegmentation
+ _OBJC_IVAR_$_PTEffectPersonSegmentation._unrotatedOutputSegmentation
+ _OBJC_IVAR_$_PTEffectPersonSegmentationViSegHQVisionCoreE5._segmentationSize
+ _OBJC_IVAR_$_PTEffectPersonSegmentationVision._colorSize
+ _VTPixelRotationSessionInvalidate
+ _VTPixelTransferSessionInvalidate
+ __OBJC_$_PROP_LIST_PTEffectPersonSegmentation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PTEffectPersonSegmentationProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PTEffectPersonSegmentationProvider
+ __OBJC_$_PROTOCOL_REFS_PTEffectPersonSegmentationProvider
+ __OBJC_LABEL_PROTOCOL_$_PTEffectPersonSegmentationProvider
+ __OBJC_PROTOCOL_$_PTEffectPersonSegmentationProvider
+ ___59-[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]_block_invoke
+ ___59-[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]_block_invoke.cold.1
+ ___59-[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]_block_invoke.cold.2
+ ___59-[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]_block_invoke.cold.3
+ ___59-[PTEffectPersonSegmentation lazyInstantiateRotatedNetwork]_block_invoke.cold.4
+ _kCGImageSourceTypeIdentifierHint
+ _kCVImageBufferICCProfileKey
+ _kCVPixelBufferMetalCompatibilityKey
+ _objc_msgSend$colorSpace
+ _objc_msgSend$context
+ _objc_msgSend$createPixelbufferFromCIImage:pixelFormat:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$extent
+ _objc_msgSend$imageWithContentsOfURL:options:
+ _objc_msgSend$initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:
+ _objc_msgSend$lazyInstantiateRotatedNetwork
+ _objc_msgSend$readPixelBufferFromFile:pixelFormat:ciOptions:
+ _objc_msgSend$render:toCVPixelBuffer:bounds:colorSpace:
+ _objc_msgSend$rotateInput:rotationDegrees:
+ _objc_msgSend$rotateOutput:segmentationOutput:rotationDegrees:
+ _objc_msgSend$rotatedNetworkState
+ _objc_msgSend$runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:transform:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:
+ _objc_msgSend$setRotatedNetworkState:
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$typeWithFilenameExtension:
- -[PTBackgroundReplacement replaceBackground:inColor:inColorPyramid:inSegmentation:effectRenderRequest:outColor:frameIndex:].cold.4
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:]
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.1
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.2
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.3
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.4
- -[PTEffectPersonSegmentation initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:].cold.5
- -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:]
- -[PTEffectPersonSegmentation runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:].cold.1
- -[PTEffectPersonSegmentationViSegHQVisionCoreE5 outputPixelbuffer]
- -[PTEffectRenderer render:waitUntilCompleted:gpuCompleted:].cold.12
- -[PTEffectResources segmentationSize]
- -[PTEffectResources setSegmentationSize:]
- _OBJC_IVAR_$_PTEffectPersonSegmentation._personSegmentation
- _OBJC_IVAR_$_PTEffectResources._segmentationSize
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PTEffectPersonSegmentation
- __OBJC_$_PROTOCOL_METHOD_TYPES_PTEffectPersonSegmentation
- __OBJC_$_PROTOCOL_REFS_PTEffectPersonSegmentation
- __OBJC_LABEL_PROTOCOL_$_PTEffectPersonSegmentation
- __OBJC_PROTOCOL_$_PTEffectPersonSegmentation
- _objc_msgSend$initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:
- _objc_msgSend$runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:
- _objc_msgSend$setSegmentationSize:
CStrings:
+ "@\"<PTEffectPersonSegmentationProvider>\""
+ "@68@0:8@16{CGSize=dd}24@40B48@52@60"
+ "Error rotating pixelbuffer"
+ "Initialized rotatedNetwork"
+ "Initializing rotated network"
+ "Invalid filename %@"
+ "Invalid state"
+ "PTEffectPersonSegmentationProvider"
+ "S\xf0\xf0\xf0b#"
+ "T@\"<PTEffectPersonSegmentationProvider>\",&,V_personSegmentationProvider"
+ "Tq,V_rotatedNetworkState"
+ "Unable to create a pixel buffer"
+ "Unable to load image using core image"
+ "Unsupported person segmentation type"
+ "^{OpaqueVTPixelRotationSession=}"
+ "^{__CVBuffer=}28@0:8@16I24"
+ "^{__CVBuffer=}28@0:8^{__CVBuffer=}16i24"
+ "^{__CVBuffer=}36@0:8@16I24@28"
+ "_lastRotation"
+ "_personSegmentationProviderRotated"
+ "_pixelRotationSession"
+ "_ptUtil"
+ "_rotated180InputPixelBuffer"
+ "_rotatedInputPixelBuffer"
+ "_rotatedNetworkState"
+ "_unrotated180OutputSegmentation"
+ "_unrotatedOutputSegmentation"
+ "colorSpace"
+ "context"
+ "createPixelbufferFromCIImage:pixelFormat:"
+ "dictionaryWithDictionary:"
+ "extent"
+ "fileManager"
+ "fileName '%s' specified does not exist"
+ "i104@0:8@16@24{CGAffineTransform=dddddd}32^{__CVBuffer=}80@88@96"
+ "imageWithContentsOfURL:options:"
+ "initWithMetalContext:colorSize:msrColorPyramid:prewarmOnly:asyncInitQueue:sharedResources:"
+ "lazyInstantiateRotatedNetwork"
+ "readPixelBufferFromFile:pixelFormat:"
+ "readPixelBufferFromFile:pixelFormat:ciOptions:"
+ "render:toCVPixelBuffer:bounds:colorSpace:"
+ "rotateInput:rotationDegrees:"
+ "rotateOutput:segmentationOutput:rotationDegrees:"
+ "rotatedNetworkState"
+ "runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:transform:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:"
+ "setRotatedNetworkState:"
+ "stringByStandardizingPath"
+ "strongSelf->_personSegmentationProviderRotated"
+ "typeWithFilenameExtension:"
- "#\xf0\xf0\xf0b#"
- "@\"<PTEffectPersonSegmentation>\""
- "@76@0:8@16{CGSize=dd}24@40@48q56B64@68"
- "Only 0 rotation supported"
- "Rotation is not supported for segmentation"
- "T@,&,V_personSegmentationProvider"
- "T{?=QQQ},V_segmentationSize"
- "i56@0:8@16@24^{__CVBuffer=}32@40@48"
- "initWithMetalContext:colorSize:msrColorPyramid:cvmNetwork:effectQuality:prewarmOnly:sharedResources:"
- "outputPixelbuffer"
- "runPersonSegmentationToOutPersonSegmentationMatteBuffer:inColor:inSegmentationRGBA:inSegmentationRGBATexture:outUpscaledSegmentation:"
- "setSegmentationSize:"

```
