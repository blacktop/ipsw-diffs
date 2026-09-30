## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2752.0.2.0.0
-  __TEXT.__text: 0x39d814
-  __TEXT.__auth_stubs: 0x40f0
-  __TEXT.__objc_methlist: 0xd10
+2759.0.1.1.0
+  __TEXT.__text: 0x39e3bc
+  __TEXT.__auth_stubs: 0x4100
+  __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2eba8
-  __TEXT.__gcc_except_tab: 0x20b6c
-  __TEXT.__cstring: 0x9a5c5
+  __TEXT.__gcc_except_tab: 0x20c2c
+  __TEXT.__cstring: 0x9aa17
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd140
+  __TEXT.__unwind_info: 0xd150
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
-  __TEXT.__objc_methname: 0x2dee
+  __TEXT.__objc_methname: 0x2e13
   __TEXT.__objc_methtype: 0x24c0
-  __TEXT.__objc_stubs: 0x2560
-  __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x4c070
+  __TEXT.__objc_stubs: 0x2580
+  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__const: 0x4c080
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb08
+  __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2090
+  __AUTH_CONST.__auth_got: 0x2098
   __AUTH_CONST.__const: 0x3c860
-  __AUTH_CONST.__cfstring: 0x357e0
+  __AUTH_CONST.__cfstring: 0x35860
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x30

   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x2bb0
   __DATA.__bss: 0x4f40
-  __DATA.__common: 0x1e98
+  __DATA.__common: 0x1ea0
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__common: 0xdf3

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 924CAD18-4CC6-3413-AC38-93F73D3A034A
-  Functions: 13107
-  Symbols:   40906
-  CStrings:  24591
+  UUID: FD5799AC-17D6-3AE5-B57B-4A8C01CB61C8
+  Functions: 13114
+  Symbols:   40922
+  CStrings:  24616
 
Symbols:
+ -[HDRImageConverter_Metal minimumConstantBufferOffsetAlignment]
+ _CGImageProviderCopyImageBlockSet
+ __ZN14GlobalHEIFInfo12getLoopCountEv
+ __ZN14GlobalHEIFInfo12setLoopCountEj
+ __ZN14TIFFReadPlugin10initializeEP13IIODictionary.cold.7
+ __ZN19AppleJPEGReadPlugin10initializeEP13IIODictionary.cold.10
+ __ZZN13IIOReadPlugin19debugWriteIOSurfaceEP11__IOSurfaceE13uniqueBlockID
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.178
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.637
+ ___block_literal_global.110
+ ___block_literal_global.120
+ ___block_literal_global.165
+ ___block_literal_global.176
+ ___block_literal_global.183
+ ___block_literal_global.639
+ _gIIO_kCMPhotoDecompressionContainerDescription_LoopCount
+ _kCGImageProviderPreferredTileHeight
+ _kCGImageProviderPreferredTileWidth
+ _objc_msgSend$minimumConstantBufferOffsetAlignment
- ___block_descriptor_tmp.105
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.160
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.170
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.635
- ___block_literal_global.107
- ___block_literal_global.114
- ___block_literal_global.162
- ___block_literal_global.172
- ___block_literal_global.181
- ___block_literal_global.637
- _kIOSurfaceContentHeadroom
CStrings:
+ "    plane[%ld]: %ldx%ld  rb:%ld\n"
+ "    surface:  %ldx%ld  rb:%ld\n"
+ "%s %lld"
+ "*** 'kCGImageAuxiliaryDataInfoImage' is not supported yet"
+ "*** ERROR: IIOImageReadSession::getBytes: count:%ld   offset:%ld   imgSize:%ld\n"
+ "*** ERROR: combination of samplesPerPixel(%d) and extraSamples(%d) is not supported\n"
+ "*** ERROR: failed to read %d bytes at offset %ld\n"
+ "*** ERROR: invalid rowBytes[%d] < width[%d]*bpc[%d]*4\n"
+ "*** ERROR: rect:{%g,%g,%g,%g} - invalid height\n"
+ "*** ERROR: rect:{%g,%g,%g,%g} - invalid width\n"
+ "*** ERROR: unexpected data '%02X%02X %02X%02X' at offset %ld\n"
+ "*** ERROR: unhandled bitdepth (%d bpc)\n"
+ "*** ERROR: unsupported bitsPerComponent[%d] for PHOTOMETRIC_YCBCR\n"
+ "*** ERROR: unsupported combination PHOTOMETRIC_YCBCR and SAMPLEFORMAT_IEEEFP\n"
+ "*** invalid PVR file: Bits Per Pixel: %d\n"
+ "*** unhandled pixel format '%c%c%c%c'\n"
+ "*** using IOSurface [%p] from auxDataInfo  (err: %d)\n"
+ "*** using data  [%p:%ld] from auxDataInfo  (err: %d)\n"
+ "*** using pixelBuffer [%p] from auxDataInfo\n"
+ "AlphaBlend"
+ "COL %s:%d - CoreAnimation  [%p]\n"
+ "COL %s:%d - CoreGraphics  [%p]\n"
+ "COL %s:%d - vImage  [%p]\n"
+ "IOSurface-%d"
+ "Invalid skew"
+ "kCGImageProviderPreferredTileHeight"
+ "kCGImageProviderPreferredTileWidth"
+ "kCMPhotoDecompressionContainerDescription_LoopCount"
+ "minimumConstantBufferOffsetAlignment"
+ "☀️  CGImageCreateByConvertingExtendedSRGBToColorspace (mode: %d)\n"
+ "❌  failed to load 'kCMPhotoDecompressionContainerDescription_LoopCount' [%s]\n"
- "\n[%2d,%2d]:  name: %s\n"
- "          size: %d\n"
- "          type: %s\n"
- "    %ldx%ld  rb:%ld\n"
- "*** ERROR: samplesPerPixel(%d) and sxtraSamples(%d) don't match\n"
- "*** Not supported yet"
- "*** unhandled pixel format\n"
- "*/IOSurface-%d.br2"
- "=== Writing IOSurfaceRef to '%s'\n"
- "updatePropertyInfo"

```
