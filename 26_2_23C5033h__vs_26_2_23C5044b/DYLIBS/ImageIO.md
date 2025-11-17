## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.2.2.1.2
-  __TEXT.__text: 0x3a6758
-  __TEXT.__auth_stubs: 0x41f0
+2784.2.5.1.4
+  __TEXT.__text: 0x3a819c
+  __TEXT.__auth_stubs: 0x4220
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebf8
-  __TEXT.__gcc_except_tab: 0x212b8
-  __TEXT.__cstring: 0x9ca2d
+  __TEXT.__gcc_except_tab: 0x21404
+  __TEXT.__cstring: 0x9d0af
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd2a0
+  __TEXT.__unwind_info: 0xd2c0
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2110
+  __AUTH_CONST.__auth_got: 0x2128
   __AUTH_CONST.__const: 0x3c8a0
   __AUTH_CONST.__cfstring: 0x35c60
   __AUTH_CONST.__objc_const: 0x1020

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 29E74973-9D06-3269-9E50-03976AD088D8
-  Functions: 13182
-  Symbols:   41086
-  CStrings:  24821
+  UUID: 253CF3E7-4989-3FB2-9403-9461EB6C470A
+  Functions: 13186
+  Symbols:   41101
+  CStrings:  24843
 
Symbols:
+ __ZN14GlobalWebPInfo15copyFrameBufferEPPhPmPj
+ __ZN15HEIFWritePlugin21hasISOGainMapForIndexEP8IIOArrayj
+ __ZN15HEIFWritePlugin29getMeteorPlusMetadataForIndexEP8IIOArrayj
+ __ZN19IIOImageDestination25adjustWriteModesForWriterE23CGImagePluginWriteModesP7CGImagei17CGColorSpaceModel16CGImageAlphaInfojP12CGColorSpaceP13IIODictionary
+ __ZN19IIOImageDestination29preserveGainMapUsingCFDataRefEPK14__CFDictionaryPK10__CFStringjbbjjjm
+ __ZNK14GlobalWebPInfo19getCachedFrameIndexEv
+ ___block_literal_global.115
+ _vImageHorizontalReflect_Planar8
+ _vImageRotate90_Planar8
+ _vImageVerticalReflect_Planar8
- __ZN19IIOImageDestination25adjustWriteModesForWriterE23CGImagePluginWriteModesi17CGColorSpaceModel16CGImageAlphaInfojP12CGColorSpaceP13IIODictionary
- ___block_literal_global.104
CStrings:
+ "*** ERROR: destination height (%zu) exceeds UINT32_MAX\n"
+ "*** ERROR: destination width (%zu) exceeds UINT32_MAX\n"
+ "*** ERROR: integer overflow in destination buffer size: %zu × %zu\n"
+ "*** ERROR: linearDataSize (%zu) < required sliceBytes (%u) for blockDim %ux%u\n"
+ "*** ERROR: preserveGainMapFromSource for '%c%c%c%c' - unhandled pixelformat: '%c%c%c%c'\n"
+ "*** ERROR: srcBuffer (%p) is not 16-byte aligned - required by libate.dylib (caller must provide aligned buffer)\n"
+ "*** ERROR: tempLinearBufferSize (%u) < required sliceBytes (%u) for blockDim %ux%u\n"
+ "*** ERROR: vImageScale_Planar8 failed: %ld\n"
+ "*** INFO: CFDataRef path calling addAuxiliaryDataInfo with URI: '%s' (gainMapType='%c%c%c%c')\n"
+ "*** INFO: IOSurface representation NOT available for '%c%c%c%c' (surface=%p, w=%d, h=%d)\n"
+ "*** INFO: IOSurface representation available for '%c%c%c%c' (%dx%d)\n"
+ "*** INFO: No '%c%c%c%c' gain map in source - skipping\n"
+ "*** INFO: No gain map data available for '%c%c%c%c' - skipping\n"
+ "*** INFO: Using CFDataRef fallback path for '%c%c%c%c'\n"
+ "*** INFO: calling addAuxiliaryDataInfo with URI: (gainMapType='%c%c%c%c')\n"
+ "*** WARNING: CMPhotoScaleAndRotateSessionTransformImage failed for '%c%c%c%c' with error: %d\n"
+ "ASTC-LZFSE: src.blocks=%p src.sliceBytes=%zu linearDataSize=%zu dest.texels=%p dest=%ux%u blockDim=%ux%u\n"
+ "ASTC-Linear: src.blocks=%p src.sliceBytes=%zu bytes_read=%zu dest.texels=%p dest=%ux%u blockDim=%ux%u\n"
+ "ASTC-Memory: src.blocks=%p src.sliceBytes=%zu srcBytes=%zd dest.texels=%p dest=%ux%u blockDim=%ux%u\n"
+ "ASTC-Twiddled: src.blocks=%p src.sliceBytes=%u tempLinearBufferSize=%u dest.texels=%p dest=%ux%u blockDim=%ux%u\n"
+ "preserveGainMapFromSource"
+ "preserveGainMapUsingCFDataRef"

```
