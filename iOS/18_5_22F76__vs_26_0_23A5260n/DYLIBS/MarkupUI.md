## MarkupUI

> `/System/Library/PrivateFrameworks/MarkupUI.framework/MarkupUI`

```diff

-522.200.0.0.0
-  __TEXT.__text: 0x27e80
+546.0.0.0.0
+  __TEXT.__text: 0x28604
   __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x3c44
+  __TEXT.__objc_methlist: 0x3d24
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x5d4
-  __TEXT.__cstring: 0x29df
+  __TEXT.__gcc_except_tab: 0x5b4
+  __TEXT.__cstring: 0x29a3
   __TEXT.__dlopen_cstrs: 0x112
-  __TEXT.__unwind_info: 0xaa0
-  __TEXT.__objc_classname: 0x603
-  __TEXT.__objc_methname: 0xbab5
-  __TEXT.__objc_methtype: 0x27c6
-  __TEXT.__objc_stubs: 0x9140
-  __DATA_CONST.__got: 0x628
+  __TEXT.__unwind_info: 0xac0
+  __TEXT.__objc_classname: 0x610
+  __TEXT.__objc_methname: 0xbe87
+  __TEXT.__objc_methtype: 0x292c
+  __TEXT.__objc_stubs: 0x9320
+  __DATA_CONST.__got: 0x6c0
   __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__objc_classlist: 0xf0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2cd0
+  __DATA_CONST.__objc_selrefs: 0x2d68
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x50
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0x828
-  __AUTH_CONST.__const: 0x150
-  __AUTH_CONST.__cfstring: 0x2620
-  __AUTH_CONST.__objc_const: 0x4820
+  __AUTH_CONST.__const: 0x130
+  __AUTH_CONST.__cfstring: 0x2640
+  __AUTH_CONST.__objc_const: 0x49f8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x26c
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x284
   __DATA.__data: 0xa58
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5DE4A448-45CC-3F24-81C0-05434C39532D
-  Functions: 1001
-  Symbols:   4263
-  CStrings:  2855
+  UUID: F8526A6D-F325-33BC-B5FE-902418D17B51
+  Functions: 1015
+  Symbols:   4337
+  CStrings:  2899
 
Symbols:
+ +[MUImageWriter outputTypesSupportingHDR]
+ -[MUImageContentViewController enableHDRAnnotations]
+ -[MUImageWriter _renderImageForBaseImage:controller:wantsHDR:]
+ -[MUImageWriter addGainMapImageToImageDestination:sdrImage:hdrImage:imageMetadata:imageOptions:]
+ -[MUImageWriter addHDRImageToImageDestination:hdrImage:imageMetadata:imageOptions:]
+ -[MarkupViewController dataRepresentationEmbeddingSourceImageAndEditModel:withDestinationType:error:]
+ -[_MUBaseImage dealloc]
+ -[_MUBaseImage hdrImage]
+ -[_MUBaseImage headroom]
+ -[_MUBaseImage imageMetadata]
+ -[_MUBaseImage imageOptions]
+ -[_MUBaseImage imageSourceRef]
+ -[_MUBaseImage initWithBaseImage:allowHDR:]
+ -[_MUBaseImage sdrImage]
+ GCC_except_table14
+ GCC_except_table153
+ GCC_except_table77
+ _CGColorSpaceIsHDR
+ _CGImageGetContentHeadroom
+ _CGImageSetHeadroom
+ _GetHeadroomFromImage
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$__MUBaseImage
+ _OBJC_IVAR_$__MUBaseImage._hdrImage
+ _OBJC_IVAR_$__MUBaseImage._headroom
+ _OBJC_IVAR_$__MUBaseImage._imageMetadata
+ _OBJC_IVAR_$__MUBaseImage._imageOptions
+ _OBJC_IVAR_$__MUBaseImage._imageSourceRef
+ _OBJC_IVAR_$__MUBaseImage._sdrImage
+ _OBJC_METACLASS_$__MUBaseImage
+ _UTTypeHEIC
+ __MUWriteOutputToTemp
+ __OBJC_$_CLASS_METHODS_MUImageWriter
+ __OBJC_$_INSTANCE_METHODS__MUBaseImage
+ __OBJC_$_INSTANCE_VARIABLES__MUBaseImage
+ __OBJC_$_PROP_LIST__MUBaseImage
+ __OBJC_CLASS_RO_$__MUBaseImage
+ __OBJC_METACLASS_RO_$__MUBaseImage
+ _kCGColorSpaceDisplayP3_PQ
+ _kCGGenerateAdaptiveSoftClipCurve
+ _kCGGenerateFlexGTC
+ _kCGImageDestinationEncodeAlternateColorSpace
+ _kCGImageDestinationEncodeBaseColorSpace
+ _kCGImageDestinationEncodeBasePixelFormatRequest
+ _kCGImageDestinationEncodeGainMapPixelFormatRequest
+ _kCGImageDestinationEncodeGainMapSubsampleFactor
+ _kCGImageDestinationEncodeGenerateGainMapWithBaseImage
+ _kCGImageDestinationEncodeIsBaseImage
+ _kCGImageDestinationEncodeRequest
+ _kCGImageDestinationEncodeRequestOptions
+ _kCGImageDestinationEncodeToISOGainmap
+ _kCGImageDestinationLossyCompressionQuality
+ _kCGImageSourceDecodeRequest
+ _kCGImageSourceDecodeRequestOptions
+ _kCGImageSourceDecodeToHDR
+ _kCGImageSourceDecodeToSDR
+ _objc_msgSend$_renderImageForBaseImage:controller:wantsHDR:
+ _objc_msgSend$addGainMapImageToImageDestination:sdrImage:hdrImage:imageMetadata:imageOptions:
+ _objc_msgSend$annotationHeadroom
+ _objc_msgSend$defaultMaxHDRGain
+ _objc_msgSend$enableHDRAnnotations
+ _objc_msgSend$hdrImage
+ _objc_msgSend$headroom
+ _objc_msgSend$imageMetadata
+ _objc_msgSend$imageOptions
+ _objc_msgSend$imageSourceRef
+ _objc_msgSend$initWithBaseImage:allowHDR:
+ _objc_msgSend$isHighDynamicRange
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$outputTypesSupportingHDR
+ _objc_msgSend$renderAnnotationsOnImage:wantsHDR:opaque:withTransform:shouldApplyCropRect:forPreview:
+ _objc_msgSend$sdrImage
+ _objc_msgSend$setMaxHDRGain:
+ _objc_msgSend$setPreferredImageDynamicRange:
- -[MUImageWriter writeUsingBaseImage:withAnnotationsFromController:asImageOfType:toConsumer:embedSourceImageAndAnnotationsAsMetadata:encryptPrivateMetadata:error:].cold.2
- GCC_except_table151
- GCC_except_table3
- GCC_except_table75
- _CGBitmapGetAlignedBytesPerRow
- _CGColorSpaceSupportsOutput
- _CGColorSpaceUsesITUR_2100TF
- _MUGlowHDREnabled._glowHDREnabled
- _MUGlowHDREnabled.onceToken
- ___MUGlowHDREnabled_block_invoke
- _objc_msgSend$appliedCropRect
- _objc_msgSend$cropAnnotation
- _objc_msgSend$integralDrawingBounds
CStrings:
+ "%s: Failed to create any CGImageRef given input: %@"
+ "@36@0:8B16@20^@28"
+ "Headroom"
+ "T^{CGImage=},R,N,V_hdrImage"
+ "T^{CGImage=},R,N,V_sdrImage"
+ "T^{CGImageMetadata=},R,N,V_imageMetadata"
+ "T^{CGImageSource=},R,N,V_imageSourceRef"
+ "T^{__CFDictionary=},R,N,V_imageOptions"
+ "Td,R,N,V_headroom"
+ "^{CGImage=}"
+ "^{CGImage=}16@0:8"
+ "^{CGImage=}36@0:8@16@24B32"
+ "^{CGImageMetadata=}"
+ "^{CGImageMetadata=}16@0:8"
+ "^{CGImageSource=}"
+ "^{CGImageSource=}16@0:8"
+ "^{__CFDictionary=}"
+ "^{__CFDictionary=}16@0:8"
+ "_MUBaseImage"
+ "_hdrImage"
+ "_headroom"
+ "_imageMetadata"
+ "_imageOptions"
+ "_imageSourceRef"
+ "_renderImageForBaseImage:controller:wantsHDR:"
+ "_sdrImage"
+ "addGainMapImageToImageDestination:sdrImage:hdrImage:imageMetadata:imageOptions:"
+ "addHDRImageToImageDestination:hdrImage:imageMetadata:imageOptions:"
+ "annotationHeadroom"
+ "dataRepresentationEmbeddingSourceImageAndEditModel:withDestinationType:error:"
+ "defaultMaxHDRGain"
+ "enableHDRAnnotations"
+ "hdrImage"
+ "headroom"
+ "imageAnalysisInteraction:visualIntelligenceVluEnabledDidChange:"
+ "imageMetadata"
+ "imageOptions"
+ "imageSourceRef"
+ "initWithBaseImage:allowHDR:"
+ "isHighDynamicRange"
+ "isVisualIntelligenceSheetPresentedDidChangeForImageAnalysisInteraction:"
+ "numberWithUnsignedInt:"
+ "outputTypesSupportingHDR"
+ "public.heic"
+ "renderAnnotationsOnImage:wantsHDR:opaque:withTransform:shouldApplyCropRect:forPreview:"
+ "sdrImage"
+ "setMaxHDRGain:"
+ "setPreferredImageDynamicRange:"
+ "v48@0:8^{CGImageDestination=}16^{CGImage=}24^{CGImageMetadata=}32@40"
+ "v56@0:8^{CGImageDestination=}16^{CGImage=}24^{CGImage=}32^{CGImageMetadata=}40@48"
- "%s: Failed to create a CGImageRef given input: %@"
- "CGBitmapContextCreate failed. Unable to draw annotations to image."
- "ImageKit"
- "Phoebe"
- "appliedCropRect"
- "cropAnnotation"
- "integralDrawingBounds"

```
