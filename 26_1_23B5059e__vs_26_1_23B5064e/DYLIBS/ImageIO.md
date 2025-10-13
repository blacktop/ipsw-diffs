## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.0.0.0.0
-  __TEXT.__text: 0x3a5124
-  __TEXT.__auth_stubs: 0x41e0
+2784.1.1.0.0
+  __TEXT.__text: 0x3a5f4c
+  __TEXT.__auth_stubs: 0x41f0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebf8
-  __TEXT.__gcc_except_tab: 0x2120c
-  __TEXT.__cstring: 0x9c0d7
+  __TEXT.__gcc_except_tab: 0x212b4
+  __TEXT.__cstring: 0x9c7d6
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd240
+  __TEXT.__unwind_info: 0xd298
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2108
-  __AUTH_CONST.__const: 0x3c840
+  __AUTH_CONST.__auth_got: 0x2110
+  __AUTH_CONST.__const: 0x3c8a0
   __AUTH_CONST.__cfstring: 0x35c60
   __AUTH_CONST.__objc_const: 0x1020
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3155804F-C960-3230-A4C2-24DBB7B7C821
-  Functions: 13161
-  Symbols:   41045
-  CStrings:  24777
+  UUID: 204D5A6F-1A9E-3101-9982-5D90DB590D46
+  Functions: 13174
+  Symbols:   41070
+  CStrings:  24807
 
Symbols:
+ GCC_except_table218
+ GCC_except_table220
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table239
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table249
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table278
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table300
+ _CGContextDrawImageApplyingToneMapping
+ __ZN10IIO_Writer23pluginUsesPixelProviderEv
+ __ZN12IIOImageRead16getBytesAtOffsetEPvmmb
+ __ZN12IIOImageRead16getBytesAtOffsetEPvmmb.cold.1
+ __ZN12IIOImageRead9getCFDataEv
+ __ZN14GlobalWebPInfo16clearFrameBufferEv
+ __ZN14GlobalWebPInfo19hasValidFrameBufferEj
+ __ZN14GlobalWebPInfoD2Ev
+ __ZN14IIO_Writer_BMP23pluginUsesPixelProviderEv
+ __ZN14IIO_Writer_TGA23pluginUsesPixelProviderEv
+ __ZN16IIOPixelProvider22convertRGB101010BufferEP13vImage_BufferS1_
+ __ZN16IIOPixelProvider35convertFloatHDRBufferUsingCGContextEP13vImage_BufferS1_j
+ __ZN16IIOPixelProvider36convertRGB101010BufferUsingCGContextEP13vImage_BufferS1_j
+ __ZN16IIOPixelProvider36convertRGB101010BufferUsingCGContextEP13vImage_BufferS1_j.cold.1
+ __ZN16IIOPixelProvider36convertRGB101010BufferUsingCGContextEP13vImage_BufferS1_j.cold.2
+ __ZN16IIOPixelProvider36convertRGB101010BufferUsingCGContextEP13vImage_BufferS1_j.cold.3
+ ___block_descriptor_tmp.101
+ ___block_descriptor_tmp.94
- GCC_except_table180
- GCC_except_table185
- GCC_except_table195
- GCC_except_table226
- GCC_except_table227
- GCC_except_table229
- GCC_except_table234
- GCC_except_table235
- GCC_except_table243
- GCC_except_table245
- GCC_except_table255
- GCC_except_table256
- GCC_except_table274
- GCC_except_table276
- GCC_except_table277
- GCC_except_table296
- __ZN12IIOImageRead16getBytesAtOffsetEPvmm
- __ZN12IIOImageRead16getBytesAtOffsetEPvmm.cold.1
- __ZN12IIOImageRead6cfDataEv
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.129
CStrings:
+ "*** Creating Float HDR CG context: %dx%d bpc=%d rb=%d bmi=0x%08X\n"
+ "*** ERROR: CGBitmapContextCreate failed for Float HDR (size: %dx%d rb: %d bpc: %d bmi: 0x%08X)\n"
+ "*** ERROR: CGBitmapContextCreate failed for HDR RGB101010 (size: %dx%d rb: %d bpc: %d bmi: 0x%08X)\n"
+ "*** ERROR: CGImageCreateWithImageInRect failed for Float HDR conversion\n"
+ "*** ERROR: CGImageCreateWithImageInRect failed for HDR RGB101010 conversion\n"
+ "*** ERROR: Failed to allocate temp buffer for Float HDR conversion\n"
+ "*** ERROR: Failed to allocate temp buffer for HDR RGB101010 conversion\n"
+ "*** ERROR: Float HDR ARGB to RGB conversion failed: '%s'\n"
+ "*** ERROR: XMPData not valid (missing: 'http://ns.adobe.com/xap/1.0/...' or '<x:xmpmeta xmlns:x=\"adobe:ns:meta...'\n)"
+ "*** ERROR: convertFloatHDRBufferUsingCGContext failed: %d\n"
+ "*** ERROR: convertRGB101010Buffer failed: %d\n"
+ "*** ERROR: convertRGB101010BufferUsingCGContext failed: %d\n"
+ "*** ERROR: invalid canvas dimensions %dx%d\n"
+ "*** ERROR: invalid canvas size %dx%d\n"
+ "*** ERROR: setFrameBuffer - bailing out\n"
+ "*** ERROR: vImage ARGB to RGB conversion failed: '%s'\n"
+ "*** Float HDR conversion: src bpc=%d bpp=%d dst bpc=%d bpp=%d\n"
+ "*** Float HDR: ARGB16U->RGB16U conversion result: %ld\n"
+ "*** Float HDR: ARGB8888->RGB888 conversion result: %ld\n"
+ "*** HDR RGB101010: ARGB8888->RGB888 conversion result: %ld\n"
+ "*** NOTE: RGB101010 with FlexGTC detected - using CoreGraphics workaround for HDR\n"
+ "*** convertRGB101010Buffer: Unsupported 16-bit destination format bpp: %d\n"
+ "*** convertRGB101010Buffer: Unsupported 8-bit destination format bpp: %d\n"
+ "*** convertRGB101010Buffer: Unsupported destination format bpc: %d bpp: %d\n"
+ "<x:xmpmeta (.)*xmlns:x=\"adobe:ns:meta/\""
+ "convertFloatHDRBufferUsingCGContext"
+ "convertRGB101010Buffer"
+ "convertRGB101010BufferUsingCGContext"
+ "decodeAnimatedWebPOptimized"
+ "setFrameBuffer"

```
