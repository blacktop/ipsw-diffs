## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

```diff

-883.11.1.0.0
-  __TEXT.__text: 0x2ba68
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x42c0
-  __TEXT.__cstring: 0x2921
+883.20.19.0.0
+  __TEXT.__text: 0x2c75c
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x4408
+  __TEXT.__cstring: 0x29c9
   __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x5ec
+  __TEXT.__gcc_except_tab: 0x630
   __TEXT.__oslogstring: 0xa37
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0xe74
-  __TEXT.__objc_classname: 0x863
-  __TEXT.__objc_methname: 0xca97
-  __TEXT.__objc_methtype: 0x2229
-  __TEXT.__objc_stubs: 0x88a0
+  __TEXT.__unwind_info: 0xeb4
+  __TEXT.__objc_classname: 0x884
+  __TEXT.__objc_methname: 0xcda5
+  __TEXT.__objc_methtype: 0x222c
+  __TEXT.__objc_stubs: 0x8980
   __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0x1a98
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x1ae0
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6200
-  __DATA_CONST.__objc_selrefs: 0x3050
-  __AUTH_CONST.__cfstring: 0x50c0
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__objc_const: 0x1ff8
+  __DATA_CONST.__objc_const: 0x6438
+  __DATA_CONST.__objc_selrefs: 0x30d8
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__objc_const: 0x2040
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH_CONST.__auth_got: 0x5e8
-  __AUTH.__objc_data: 0x780
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH.__objc_data: 0x7d0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x418
-  __DATA.__objc_superrefs: 0x180
-  __DATA.__objc_ivar: 0x4b0
-  __DATA.__data: 0x7f0
-  __DATA.__bss: 0x78
+  __DATA.__objc_classrefs: 0x420
+  __DATA.__objc_superrefs: 0x188
+  __DATA.__objc_ivar: 0x4d8
+  __DATA.__data: 0x7f8
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xd70
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 238AAD69-254A-321A-B0D0-2A0DD8594070
-  Functions: 1523
-  Symbols:   5758
-  CStrings:  3991
+  UUID: 0439C1D8-3B63-335B-8D87-1F4E5108CB29
+  Functions: 1555
+  Symbols:   5856
+  CStrings:  4033
 
Symbols:
+ +[UIImage(VideosUICore) vuiImageNamed:]
+ +[VUIDevice supportsStageManager]
+ +[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]
+ +[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:]
+ -[VUIDataImageDescriptor backgroundColor]
+ -[VUIDataImageDescriptor backgroundSize]
+ -[VUIDataImageDescriptor renderSize]
+ -[VUIDataImageDescriptor scaleWithinRenderSize]
+ -[VUIDataImageDescriptor setBackgroundColor:]
+ -[VUIDataImageDescriptor setBackgroundSize:]
+ -[VUIDataImageDescriptor setRenderAsTemplate:]
+ -[VUIDataImageDescriptor setRenderSize:]
+ -[VUIDataImageDescriptor setScaleWithinRenderSize:]
+ -[VUIDataImageDescriptor shouldRenderAsTemplate]
+ -[VUIImageBackgroundColorDecorator .cxx_destruct]
+ -[VUIImageBackgroundColorDecorator backgroundColor]
+ -[VUIImageBackgroundColorDecorator decorate:scaledWithSize:croppedToFit:]
+ -[VUIImageBackgroundColorDecorator decoratorIdentifier]
+ -[VUIImageBackgroundColorDecorator expectedSize]
+ -[VUIImageBackgroundColorDecorator initWithBackgroundColor:andSize:]
+ -[VUIImageBackgroundColorDecorator isEqual:]
+ -[VUIImageBackgroundColorDecorator loaderCropToFit]
+ -[VUIImageBackgroundColorDecorator loaderScaleToSize]
+ -[VUIImageBackgroundColorDecorator size]
+ -[VUIImageView latestImageURL]
+ -[VUIRemoteImageDescriptor boundingSize]
+ -[VUIRemoteImageDescriptor displayScaleIsPointMultiplier]
+ -[VUIRemoteImageDescriptor downloadSize]
+ -[VUIRemoteImageDescriptor setDisplayScaleIsPointMultiplier:]
+ -[VUIRemoteImageDescriptor setDownloadSize:]
+ -[VUIRemoteImageDescriptor setRenderAsTemplate:]
+ -[VUIRemoteImageDescriptor shouldRenderAsTemplate]
+ -[VUIResourceImageDescriptor initWithResourceSymbol:size:symbolConfiguration:]
+ _CGContextFillRect
+ _CGContextSetFillColorWithColor
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_VUIImageBackgroundColorDecorator
+ _OBJC_IVAR_$_VUIDataImageDescriptor._backgroundColor
+ _OBJC_IVAR_$_VUIDataImageDescriptor._backgroundSize
+ _OBJC_IVAR_$_VUIDataImageDescriptor._renderAsTemplate
+ _OBJC_IVAR_$_VUIDataImageDescriptor._renderSize
+ _OBJC_IVAR_$_VUIDataImageDescriptor._scaleWithinRenderSize
+ _OBJC_IVAR_$_VUIImageBackgroundColorDecorator._backgroundColor
+ _OBJC_IVAR_$_VUIImageBackgroundColorDecorator._size
+ _OBJC_IVAR_$_VUIImageView._latestImageURL
+ _OBJC_IVAR_$_VUIRemoteImageDescriptor._boundingSize
+ _OBJC_IVAR_$_VUIRemoteImageDescriptor._displayScaleIsPointMultiplier
+ _OBJC_IVAR_$_VUIRemoteImageDescriptor._downloadSize
+ _OBJC_IVAR_$_VUIRemoteImageDescriptor._renderAsTemplate
+ _OBJC_METACLASS_$_VUIImageBackgroundColorDecorator
+ _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:.onceToken
+ _URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:.sPointMultiplier
+ __OBJC_$_INSTANCE_METHODS_VUIImageBackgroundColorDecorator
+ __OBJC_$_INSTANCE_VARIABLES_VUIImageBackgroundColorDecorator
+ __OBJC_$_PROP_LIST_VUIImageBackgroundColorDecorator
+ __OBJC_CLASS_RO_$_VUIImageBackgroundColorDecorator
+ __OBJC_METACLASS_RO_$_VUIImageBackgroundColorDecorator
+ ___135+[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:]_block_invoke
+ ___33+[VUIDevice supportsStageManager]_block_invoke
+ ___73-[VUIImageBackgroundColorDecorator decorate:scaledWithSize:croppedToFit:]_block_invoke
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke.16
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke_2
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke_2.18
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke_3
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke_3.19
+ ___75+[VUIGraphicsImageRenderer SVGImagesWithDataDescriptors:format:completion:]_block_invoke_4
+ ___block_descriptor_32_e72_v48?0^{CGContext=}8"VUIDataImageDescriptor"16"UIImage"24{CGSize=dd}32l
+ ___block_descriptor_64_e8_32s40bs48r_e40_v16?0"UIGraphicsImageRendererContext"8lr48l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r_e40_v16?0"UIGraphicsImageRendererContext"8lr64l8s32l8s56l8s40l8s48l8
+ ___block_literal_global.14
+ ___block_literal_global.9
+ _objc_copyStruct
+ _objc_msgSend$URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:
+ _objc_msgSend$backgroundSize
+ _objc_msgSend$boundingSize
+ _objc_msgSend$displayScaleIsPointMultiplier
+ _objc_msgSend$downloadSize
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$renderSize
+ _objc_msgSend$scaleWithinRenderSize
+ _supportsStageManager.onceToken
+ _supportsStageManager.supportsStageManager
- +[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]
- +[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:]
- -[VUIDataImageDescriptor isTemplated]
- -[VUIDataImageDescriptor setTemplated:]
- -[VUIRemoteImageDescriptor size]
- _OBJC_IVAR_$_VUIDataImageDescriptor._templated
- _OBJC_IVAR_$_VUIRemoteImageDescriptor._size
- _URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:.onceToken
- _URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:.sPointMultiplier
- ___105+[VUIImageFactory URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:]_block_invoke
- ___65+[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]_block_invoke
- ___65+[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]_block_invoke.12
- ___65+[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]_block_invoke_2
- ___65+[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]_block_invoke_2.13
- ___65+[VUIGraphicsImageRenderer SVGImagesWithDatas:format:completion:]_block_invoke_3
- ___block_descriptor_56_e8_32bs40r_e40_v16?0"UIGraphicsImageRendererContext"8lr40l8s32l8
- _objc_msgSend$URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:
CStrings:
+ "\x13\x12a\x14\x16"
+ "@80@0:8@16@24@32@40{CGSize=dd}48B64B68d72"
+ "DeviceSupportsEnhancedMultitasking"
+ "DeviceSupportsSingleDisplayEnhancedMultitasking"
+ "SVGImagesWithDataDescriptors:format:completion:"
+ "T@\"NSURL\",R,N,V_latestImageURL"
+ "T@\"UIColor\",R,C,N,V_backgroundColor"
+ "TB,N,V_displayScaleIsPointMultiplier"
+ "Td,N,V_scaleWithinRenderSize"
+ "T{CGSize=dd},N,V_backgroundSize"
+ "T{CGSize=dd},N,V_renderSize"
+ "T{CGSize=dd},R,N,V_boundingSize"
+ "T{CGSize=dd},V_downloadSize"
+ "URLFromSource:extension:p3Specifier:cropCode:imageSize:displayScaleIsPointMultiplier:centerGrowth:focusSizeIncrease:"
+ "VUIImageBackgroundColorDecorator"
+ "_backgroundSize"
+ "_boundingSize"
+ "_displayScaleIsPointMultiplier"
+ "_downloadSize"
+ "_latestImageURL"
+ "_renderSize"
+ "_scaleWithinRenderSize"
+ "backgroundSize"
+ "boundingSize"
+ "cider"
+ "displayScaleIsPointMultiplier"
+ "downloadSize"
+ "initWithBackgroundColor:andSize:"
+ "initWithFormat:"
+ "initWithResourceSymbol:size:symbolConfiguration:"
+ "latestImageURL"
+ "lyze"
+ "opal"
+ "renderSize"
+ "saturn"
+ "saturn2"
+ "scaleWithinRenderSize"
+ "setBackgroundSize:"
+ "setDisplayScaleIsPointMultiplier:"
+ "setDownloadSize:"
+ "setRenderSize:"
+ "setScaleWithinRenderSize:"
+ "supportsStageManager"
+ "v48@?0^{CGContext=}8@\"VUIDataImageDescriptor\"16@\"UIImage\"24{CGSize=dd}32"
+ "vuiImageNamed:"
- "\x13\x12a\x14\x15"
- "@76@0:8@16@24@32@40{CGSize=dd}48B64d68"
- "SVGImagesWithDatas:format:completion:"
- "URLFromSource:extension:p3Specifier:cropCode:imageSize:centerGrowth:focusSizeIncrease:"
- "ascl"
- "beryl"
- "grabber"

```
