## RenderBox

> `/System/Library/PrivateFrameworks/RenderBox.framework/RenderBox`

```diff

-7.0.70.0.0
-  __TEXT.__text: 0x14c3a8
-  __TEXT.__auth_stubs: 0x28d0
+7.0.75.1.0
+  __TEXT.__text: 0x14e210
+  __TEXT.__auth_stubs: 0x28f0
   __TEXT.__objc_methlist: 0x2a80
-  __TEXT.__const: 0x5cc8
-  __TEXT.__gcc_except_tab: 0x7230
-  __TEXT.__cstring: 0x5a59
-  __TEXT.__oslogstring: 0xbfd
-  __TEXT.__unwind_info: 0x5e58
+  __TEXT.__const: 0x5dd8
+  __TEXT.__gcc_except_tab: 0x7380
+  __TEXT.__cstring: 0x5b2d
+  __TEXT.__oslogstring: 0xef2
+  __TEXT.__unwind_info: 0x6140
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x42c
-  __TEXT.__objc_methname: 0x6343
+  __TEXT.__objc_methname: 0x6349
   __TEXT.__objc_methtype: 0x3441
-  __TEXT.__objc_stubs: 0x4740
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x1d28
+  __TEXT.__objc_stubs: 0x4760
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__const: 0x1d80
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_selrefs: 0x1de8
   __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x1478
+  __AUTH_CONST.__auth_got: 0x1488
   __AUTH_CONST.__const: 0x8a88
-  __AUTH_CONST.__cfstring: 0x2ae0
+  __AUTH_CONST.__cfstring: 0x2b00
   __AUTH_CONST.__objc_const: 0x4668
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 630B5068-A7D2-3665-BA75-DD63785B8FD5
-  Functions: 6811
-  Symbols:   17919
-  CStrings:  3511
+  UUID: 03DAB0F2-B4BB-37D1-81AD-1D5222457B92
+  Functions: 6834
+  Symbols:   17975
+  CStrings:  3548
 
Symbols:
+ -[RBLayer displayWithBounds:callback:].cold.10
+ -[RBLayer displayWithBounds:callback:].cold.8
+ -[RBLayer displayWithBounds:callback:].cold.9
+ -[RBLayer setSubsurface:rotated:bounds:contentsScale:contentHeadroom:displayHeadroom:]
+ GCC_except_table1040
+ GCC_except_table1070
+ GCC_except_table1072
+ GCC_except_table1089
+ GCC_except_table1131
+ GCC_except_table1168
+ GCC_except_table1207
+ GCC_except_table122
+ GCC_except_table1244
+ GCC_except_table1281
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table1346
+ GCC_except_table1376
+ GCC_except_table1379
+ GCC_except_table1409
+ GCC_except_table1439
+ GCC_except_table1729
+ GCC_except_table1762
+ GCC_except_table184
+ GCC_except_table940
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table989
+ _RBImageProviderHasStaticData
+ __ZN2RB11DisplayList15CachedTransformC1ERKS1_ff
+ __ZN2RB11DisplayList15CachedTransformC2ERNS0_7BuilderERKNS_15AffineTransformEPKNS0_8ClipNodeEPKNS0_5StyleE
+ __ZN2RB12TextureCache12prune_cachesEjjjj.cold.1
+ __ZN2RB12TextureCache12prune_cachesEjjjj.cold.2
+ __ZN2RB12TextureCache7prepareERNS_11RenderFrameEP7CGImageRKNS0_6ParamsE.cold.1
+ __ZN2RB12TextureCache7prepareERNS_11RenderFrameEP7CGImageRKNS0_6ParamsE.cold.2
+ __ZN2RB12TextureCache9use_entryEjRKNS0_6ParamsE
+ __ZN2RB12TextureCache9use_entryEjRKNS0_6ParamsE.cold.1
+ __ZN2RB12TextureCache9use_entryEjRKNS0_6ParamsE.cold.2
+ __ZN2RB12TextureCache9use_entryEjRKNS0_6ParamsE.cold.3
+ __ZN2RB13ImageProvider14convert_bitmapERNS_9CGContextEb
+ __ZN2RB13ImageProvider14convert_bitmapERNS_9CGContextEb.cold.1
+ __ZN2RB14refcounted_ptrINS_19SharedSurfaceClientEEaSERKS2_
+ __ZN2RB14refcounted_ptrINS_19SharedSurfaceClientEEaSERKS2_.cold.1
+ __ZN2RB9CGContext13create_bitmapEDv2_iNS0_12BitmapFormatENSt3__18optionalINS_10ColorSpaceEEEf
+ __ZN2RB9CGContext22apply_color_conversionERKNS_10ColorSpace10ConversionE
+ __ZNK2RB10ColorSpace26supports_vimage_conversionEv
+ __ZNK2RB13ImageProvider15bytes_per_pixelEv
+ __ZNK2RB4Fill5ImageINS_12ImageTextureEE10color_infoEv
+ __ZNK2RB7Texture15has_write_usageEv
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferINS_12packed_half4EE18apply_pixel_valuesIZNS_9CGContext22apply_color_conversionERKNS_10ColorSpace10ConversionEE3$_1EEvRKT_EUlmmmmE_EEvmmSD_ENUlPvmE_8__invokeESF_m
+ __ZZN2RB20dispatch_apply_tilesIZNS_18Typed_vImageBufferIjE18apply_pixel_valuesIZNS_9CGContext22apply_color_conversionERKNS_10ColorSpace10ConversionEE3$_0EEvRKT_EUlmmmmE_EEvmmSC_ENUlPvmE_8__invokeESE_m
+ __ZZN2RB5TableIPKNS_20FormattedRenderStateEPNS_6Device19RenderPipelineEntryEE9remove_ifIZZNS4_12prune_cachesEvENK3$_1clEvEUlT_PT0_E_EEvRKSA_ENUlPKvSH_SH_E_8__invokeESH_SH_SH_.cold.1
+ ___59-[RBLayer copyImageInRect:options:completionQueue:handler:]_block_invoke_4.cold.1
+ ___block_descriptor_92_e8_32c29_ZTSN2RB8objc_ptrIP7RBLayerEE_e9_v16?0^v8l
+ ___block_descriptor_95_e8_32rc40r_e22_v48?0Q8Q16Q24r^v32Q40lr32l8r40l8
+ _kCFBooleanTrue
+ _kCGImageProviderBitmapInfo
+ _objc_msgSend$usage
+ _vImageConvert_AnyToAny
+ _vImageConverter_CreateWithCGImageFormat
+ _vImageConverter_Release
- -[RBLayer setSubsurface:rotated:bounds:contentsScale:contentHeadroom:displayHeadroom:locked:]
- GCC_except_table1039
- GCC_except_table1069
- GCC_except_table1071
- GCC_except_table1088
- GCC_except_table1130
- GCC_except_table1167
- GCC_except_table1206
- GCC_except_table1243
- GCC_except_table1280
- GCC_except_table130
- GCC_except_table133
- GCC_except_table1345
- GCC_except_table1375
- GCC_except_table1378
- GCC_except_table1408
- GCC_except_table1438
- GCC_except_table1728
- GCC_except_table1761
- GCC_except_table939
- GCC_except_table969
- GCC_except_table971
- GCC_except_table988
- __ZN2RB11DisplayList12Interpolator8Contents10make_layerIZNKS0_5Layer7can_mixERS2_RKS4_NS_7MixableEE3$_2EEPKNS1_5LayerEjjT_
- __ZN2RB11DisplayList15CachedTransformC1ERKS1_ffj
- __ZN2RB11DisplayList15CachedTransformC2ERNS0_7BuilderERKNS_15AffineTransformEPKNS0_8ClipNodeEPKNS0_5StyleEj
- __ZN2RB12TextureCache18prepare_from_cacheERNS_11RenderFrameERKNS0_6ParamsE.cold.1
- __ZN2RB12TextureCache7prepareERNS_11RenderFrameEPU21objcproto10MTLTexture11objc_objectRKNS0_6ParamsE.cold.1
- __ZN2RB12TextureCache9use_entryEj
- __ZN2RB4Heap7emplaceINS_11DisplayList5LayerEJiiEEEPT_DpOT0_
- __ZN2RB9CGContext13create_bitmapEDv2_iNS0_12BitmapFormatENSt3__18optionalINS_10ColorSpaceEEE
- ___block_descriptor_93_e8_32c29_ZTSN2RB8objc_ptrIP7RBLayerEE_e9_v16?0^v8l
- ___block_descriptor_94_e8_32rc40r_e22_v48?0Q8Q16Q24r^v32Q40lr32l8r40l8
- _objc_retain_x25
CStrings:
+ " non-premul"
+ "%p: %p was deleted\n"
+ "%p: %p was purged\n"
+ "%p: attempting to mark %p non-volatile\n"
+ "%p: converted %p -> %p, level %d [%d, %d] %s %s\n"
+ "%p: copied IOSurface from image provider\n"
+ "%p: created external base texture %p [%d, %d] %s %s\n"
+ "%p: created image data texture %p [%d %d] %s %s%s\n"
+ "%p: created image texture %p [%d, %d] @%d %s %s\n"
+ "%p: created surface texture %p [%d, %d] %s %s%s\n"
+ "%p: created tiled texture %p [%d %d] %s %s%s\n"
+ "%p: deleted %p\n"
+ "%p: deleted cached IOSurface\n"
+ "%p: downsampled %p -> %p, level %d [%d, %d] %s %s\n"
+ "%p: failed to create texture from image data\n"
+ "%p: marked %p volatile\n"
+ "%p: read IOSurface from image property\n"
+ "%p: rendered level %d [%d, %d] %s %s\n"
+ "%p: source object deleted\n"
+ "%p: take_available [%d, %d] %p %s\n"
+ "7.0.75.1"
+ "<obsolete>"
+ "L16Float"
+ "L8Unorm"
+ "L8Unorm_sRGB"
+ "LA16Float"
+ "LA8Unorm"
+ "LA8Unorm_sRGB"
+ "RBImageProviderHasStaticData"
+ "RGBA16Unorm_Float16"
+ "deviceRGB"
+ "failed to copy bitmap: %u -> %u"
+ "gray"
+ "ignored-by-needs-background"
+ "ignored-by-needs-bg"
+ "linear-gray"
+ "read-as-bg"
+ "reads-bg"
+ "texture-cache"
+ "uncached"
+ "usage"
- "(bg-depth %d)"
- "7.0.70"
- "RGBA16Unorm_Float"
- "read-as-backdrop"
- "root-layer"

```
