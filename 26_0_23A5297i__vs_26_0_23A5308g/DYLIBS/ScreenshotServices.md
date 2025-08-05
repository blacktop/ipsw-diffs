## ScreenshotServices

> `/System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices`

```diff

-409.0.0.0.0
-  __TEXT.__text: 0x1ce78
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x2524
+412.0.0.0.0
+  __TEXT.__text: 0x1d0dc
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__objc_methlist: 0x254c
   __TEXT.__const: 0x3ec
-  __TEXT.__cstring: 0x1e23
-  __TEXT.__oslogstring: 0x1189
+  __TEXT.__cstring: 0x1e62
+  __TEXT.__oslogstring: 0x11c8
   __TEXT.__gcc_except_tab: 0x3a0
   __TEXT.__dlopen_cstrs: 0x4ae
-  __TEXT.__unwind_info: 0xa90
+  __TEXT.__unwind_info: 0xab0
   __TEXT.__objc_classname: 0x832
-  __TEXT.__objc_methname: 0x649f
-  __TEXT.__objc_methtype: 0xfb4
-  __TEXT.__objc_stubs: 0x58c0
-  __DATA_CONST.__got: 0x6a8
+  __TEXT.__objc_methname: 0x6565
+  __TEXT.__objc_methtype: 0xfc5
+  __TEXT.__objc_stubs: 0x59a0
+  __DATA_CONST.__got: 0x6a0
   __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_selrefs: 0x1b68
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0x1f00
+  __AUTH_CONST.__cfstring: 0x1f20
   __AUTH_CONST.__objc_const: 0x4b50
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x108

   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x260
   __DATA.__data: 0x6e0
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C794B38F-BFB8-3BC2-A3F5-8A259BA58CC5
-  Functions: 935
-  Symbols:   3784
-  CStrings:  2031
+  UUID: 9602CD2A-4D24-3A5A-837A-64D9724ADCA3
+  Functions: 940
+  Symbols:   3797
+  CStrings:  2040
 
Symbols:
+ +[SSChromeHelper roundedCropHandleThickness]
+ +[SSChromeHelper roundedCropsCornerRadius]
+ +[SSChromeHelper screenshotBottomMargin:]
+ +[SSChromeHelper screenshotBottomMarginPhone]
+ +[SSChromeHelper screenshotTopMargin:]
+ +[SSChromeHelper screenshotTopMarginPhone]
+ -[UIImage(SSImageSurface) ss_dataWithFileFormat:addProperties:imageDescription:]
+ -[UIImage(SSImageSurface) ss_heicDataWithImageDescription:]
+ -[UIImage(SSImageSurface) ss_pngDataWithImageDescription:]
+ GCC_except_table34
+ _OBJC_CLASS_$_UTType
+ __SSDelayDismissalForFullHeightVICard
+ __SSDeviceSupportsHDRCaptureForMainScreen
+ ___block_literal_global.138
+ ___block_literal_global.54
+ ___block_literal_global.70
+ ___block_literal_global.77
+ _objc_msgSend$hasRemoteViewController
+ _objc_msgSend$screenshotBottomMargin:
+ _objc_msgSend$screenshotBottomMarginPhone
+ _objc_msgSend$screenshotTopMargin:
+ _objc_msgSend$screenshotTopMarginPhone
+ _objc_msgSend$ss_CGImageBacked
+ _objc_msgSend$ss_dataWithFileFormat:addProperties:imageDescription:
+ _objc_msgSend$ss_hdrSurfaceCGImage
+ _objc_msgSend$ss_heicDataWithImageDescription:
+ _objc_msgSend$ss_imageDataWithDataType:image:hdrImage:properties:imageDescription:
+ _objc_msgSend$ss_pngDataWithImageDescription:
+ _objc_msgSend$ss_sdrSurfaceCGImage
+ _objc_msgSend$typeWithIdentifier:
- +[SSChromeHelper screenshotTopBottomMargin:]
- +[SSChromeHelper screenshotTopBottomMarginPhone]
- -[UIImage(SSImageSurface) ss_dataWithFileFormat:addProperties:]
- -[UIImage(SSImageSurface) ss_heicData]
- -[UIImage(SSImageSurface) ss_jpegData]
- -[UIImage(SSImageSurface) ss_pngData]
- _UIImageHEICRepresentation
- _UTTypeJPEG
- ___block_literal_global.134
- ___block_literal_global.51
- ___block_literal_global.64
- ___block_literal_global.71
- _kCGImageDestinationEncodeToISOHDR
- _objc_msgSend$screenshotTopBottomMargin:
- _objc_msgSend$screenshotTopBottomMarginPhone
- _objc_msgSend$ss_dataWithFileFormat:addProperties:
- _objc_msgSend$ss_heicData
- _objc_msgSend$ss_pngData
- _objc_msgSend$ss_ppkHeicDataWithProperties:
CStrings:
+ "@36@0:8@16B24@28"
+ "com.apple.ScreenshotServices.delayDismissalForFullHeightVICard"
+ "device lock state changed %llu"
+ "device lock state changed, %llu"
+ "roundedCropHandleThickness"
+ "roundedCropsCornerRadius"
+ "screenshotBottomMargin:"
+ "screenshotBottomMarginPhone"
+ "screenshotTopMargin:"
+ "screenshotTopMarginPhone"
+ "ss_dataWithFileFormat:addProperties:imageDescription:"
+ "ss_heicDataWithImageDescription:"
+ "ss_imageDataWithDataType:image:hdrImage:properties:imageDescription:"
+ "ss_pngDataWithImageDescription:"
+ "typeWithIdentifier:"
- "screenshotTopBottomMargin:"
- "screenshotTopBottomMarginPhone"
- "ss_dataWithFileFormat:addProperties:"
- "ss_heicData"
- "ss_jpegData"
- "ss_pngData"
- "ss_ppkHeicDataWithProperties:"

```
