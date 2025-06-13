## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1410.5.0.0.0
-  __TEXT.__text: 0x268b60
-  __TEXT.__auth_stubs: 0x2de0
-  __TEXT.__objc_methlist: 0x147cc
-  __TEXT.__cstring: 0x9bc4c
+1420.3.0.0.0
+  __TEXT.__text: 0x268d20
+  __TEXT.__auth_stubs: 0x2dd0
+  __TEXT.__objc_methlist: 0x147d4
+  __TEXT.__cstring: 0x9bc98
   __TEXT.__const: 0x94c0
   __TEXT.__oslogstring: 0x7cbc
   __TEXT.__gcc_except_tab: 0x41bc

   __TEXT.__unwind_info: 0x6120
   __TEXT.__eh_frame: 0x240
   __TEXT.__objc_classname: 0x28a7
-  __TEXT.__objc_methname: 0x20ee0
+  __TEXT.__objc_methname: 0x20f06
   __TEXT.__objc_methtype: 0x6d91
-  __TEXT.__objc_stubs: 0x11ee0
-  __DATA_CONST.__got: 0x5b0
-  __DATA_CONST.__const: 0x65a0
+  __TEXT.__objc_stubs: 0x11f00
+  __DATA_CONST.__got: 0x598
+  __DATA_CONST.__const: 0x65c0
   __DATA_CONST.__objc_classlist: 0xfa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1cce0
-  __DATA_CONST.__objc_selrefs: 0x8b80
+  __DATA_CONST.__objc_selrefs: 0x8b88
   __DATA_CONST.__objc_arraydata: 0x13e0
-  __AUTH_CONST.__cfstring: 0x1c280
+  __AUTH_CONST.__cfstring: 0x1c300
   __AUTH_CONST.__objc_const: 0xdf00
-  __AUTH_CONST.__const: 0xc0d8
+  __AUTH_CONST.__const: 0xc0f8
   __AUTH_CONST.__objc_doubleobj: 0x2800
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_dictobj: 0x460
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_floatobj: 0x2c0
-  __AUTH_CONST.__auth_got: 0x1708
+  __AUTH_CONST.__auth_got: 0x1700
   __AUTH.__objc_data: 0x95b0
   __AUTH.__data: 0x5be8
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x5b8
+  __DATA.__objc_classrefs: 0x5c0
   __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0x2054
   __DATA.__data: 0x35c8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A0231B8-907E-390A-9D45-B7B9BF7C37CE
-  Functions: 12917
-  Symbols:   37790
-  CStrings:  17924
+  UUID: F673745F-586F-363A-9DB7-E6A13C554D02
+  Functions: 12919
+  Symbols:   37794
+  CStrings:  17933
 
Symbols:
+ +[CIRAWFilter filterWithImageURL:options:]
+ _OBJC_CLASS_$_LSExtensionPointRecord
+ ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.305
+ ___CIMetalRenderToImageblocks_block_invoke.86
+ ___CIMetalRenderToTextures_block_invoke.76
+ ___CIMetalRenderToTextures_block_invoke.76.cold.1
+ ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.393
+ ____ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsERm_block_invoke
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.213
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.239
+ ___block_descriptor_tmp.240
+ ___block_descriptor_tmp.241
+ ___block_literal_global.165
+ _objc_msgSend$extensionPointRecordForCurrentProcess
- _CVPixelBufferGetAttributes
- ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.302
- ___CIMetalRenderToImageblocks_block_invoke.82
- ___CIMetalRenderToTextures_block_invoke.72
- ___CIMetalRenderToTextures_block_invoke.72.cold.1
- ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.389
- ___block_descriptor_tmp.209
- ___block_descriptor_tmp.217
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.236
- ___block_descriptor_tmp.237
- _kCVPixelBufferPixelFormatDescriptionKey
- _kCVPixelFormatCompressionType
- _kCVPixelFormatPlanes
CStrings:
+ "CrossForward"
+ "com.apple.widgetkit-extension"
+ "com.crossforward"
+ "extensionPointRecordForCurrentProcess"
+ "initWithOptions"

```
