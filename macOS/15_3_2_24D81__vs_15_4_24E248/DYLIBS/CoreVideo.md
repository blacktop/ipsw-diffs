## CoreVideo

> `/System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo`

```diff

-672.10.0.0.0
-  __TEXT.__text: 0x482bc
-  __TEXT.__auth_stubs: 0x1930
-  __TEXT.__cstring: 0x13376
+682.6.0.0.0
+  __TEXT.__text: 0x48130
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__cstring: 0x133a1
   __TEXT.__objc_databytes: 0x483
-  __TEXT.__const: 0x11e0
+  __TEXT.__const: 0x1204
   __TEXT.__oslogstring: 0x253
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__dof_CVPixelBu: 0x24a
-  __TEXT.__unwind_info: 0xf30
+  __TEXT.__unwind_info: 0xf70
   __TEXT.__objc_methname: 0x195
   __TEXT.__objc_stubs: 0x1e0
   __DATA_CONST.__got: 0x2a8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x457c0
-  __AUTH_CONST.__auth_got: 0xca8
+  __AUTH_CONST.__auth_got: 0xca0
   __AUTH_CONST.__const: 0x2c00
   __AUTH_CONST.__cfstring: 0x3100
   __AUTH_CONST.__objc_dictobj: 0x14528
   __AUTH_CONST.__objc_intobj: 0x2268
   __AUTH_CONST.__objc_arrayobj: 0x3768
-  __AUTH.__data: 0x720
   __AUTH.__objc_dataobj: 0x990
   __AUTH.__objc_databytes: 0x330
+  __AUTH.__data: 0x720
   __DATA.__data: 0x434
   __DATA.__bss: 0x318
-  __DATA.__common: 0x95
+  __DATA.__common: 0x94
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FCFE924-013C-3974-9FDF-58F9A8D71845
-  Functions: 1666
-  Symbols:   3877
+  UUID: 8912F801-7326-344E-A079-B05C0FD5D007
+  Functions: 1720
+  Symbols:   3962
   CStrings:  1467
 
Symbols:
+ CVColorPrimariesGetStringForIntegerCodePoint.cold.1
+ CVDataBufferGetTypeID.cold.1
+ CVDataBufferPoolGetTypeID.cold.1
+ CVDisplayLinkGetTypeID.cold.1
+ CVKTraceInit.cold.1
+ CVMetalBufferCacheGetTypeID.cold.1
+ CVMetalBufferGetTypeID.cold.1
+ CVMetalTextureCacheGetTypeID.cold.1
+ CVMetalTextureGetTypeID.cold.1
+ CVObjectGetTypeID.cold.1
+ CVOpenGLBufferGetTypeID.cold.1
+ CVOpenGLBufferPoolGetTypeID.cold.1
+ CVOpenGLESTextureCacheGetTypeID.cold.1
+ CVOpenGLESTextureGetTypeID.cold.1
+ CVOpenGLTextureCacheGetTypeID.cold.1
+ CVOpenGLTextureGetTypeID.cold.1
+ CVPixelBufferGetTypeID.cold.1
+ CVPixelBufferPoolGetTypeID.cold.1
+ CVTransferFunctionGetStringForIntegerCodePoint.cold.1
+ CVYCbCrMatrixGetStringForIntegerCodePoint.cold.1
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _Z27CVLockingBunchPairGetTypeIDv.cold.1
+ _Z28CVLocklessBunchPairGetTypeIDv.cold.1
+ _Z29CVPixelBufferBackingGetTypeIDv.cold.1
+ _ZL26_pixelFormatDictionaryInitv.cold.1
+ _ZL26_pixelFormatDictionaryInitv.cold.2
+ _ZL26_pixelFormatDictionaryInitv.cold.3
+ _ZL26_pixelFormatDictionaryInitv.cold.4
+ _ZL26_pixelFormatDictionaryInitv.cold.5
+ _ZL39areUniversalCompressionFormatsSupportedv.cold.1
+ _ZL41_cvDisplayLinkConvertServerMATtoClientMATy.cold.1
+ _ZL44areUniversalLossyCompressionFormatsSupportedv.cold.1
+ _ZL55translateCoreVideoAttachmentKeyToIOSurfaceKeyAndStoreItPKvS0_Pv.cold.1
+ _ZN12CVDataBuffer5allocEPK13__CFAllocator.cold.1
+ _ZN13CVDisplayLink23calculateNextWakeUpTimeEP11CVTimeStampS1_b.cold.1
+ _ZN13CVDisplayLink5allocEPK13__CFAllocator.cold.1
+ _ZN13CVMetalBuffer5allocEPK13__CFAllocator.cold.1
+ _ZN13CVPixelBuffer13setAttachmentEPK10__CFStringPKv16CVAttachmentMode.cold.1
+ _ZN13CVPixelBuffer5allocEPK13__CFAllocator.cold.1
+ _ZN14CVMetalTexture5allocEPK13__CFAllocator.cold.1
+ _ZN14CVOpenGLBuffer5allocEPK13__CFAllocator.cold.1
+ _ZN15CVCGDisplayLink15getDisplayTimesEPyS0_S0_.cold.1
+ _ZN15CVCGDisplayLink19updateDisplayTimingEv.cold.1
+ _ZN15CVOpenGLTexture5allocEPK13__CFAllocator.cold.1
+ _ZN16CVDataBufferPool5allocEPK13__CFAllocator.cold.1
+ _ZN17CVOpenGLESContext15initWithContextEPv.cold.1
+ _ZN17CVOpenGLESTexture5allocEPK13__CFAllocator.cold.1
+ _ZN17CVPixelBufferPool27initializeIOSurfaceTrackingEv.cold.1
+ _ZN17CVPixelBufferPool5allocEPK13__CFAllocator.cold.1
+ _ZN18CVLockingBunchPair5allocEPK13__CFAllocator.cold.1
+ _ZN18CVMetalBufferCache5allocEPK13__CFAllocator.cold.1
+ _ZN18CVOpenGLBufferPool5allocEPK13__CFAllocator.cold.1
+ _ZN19CVLocklessBunchPair5allocEPK13__CFAllocator.cold.1
+ _ZN19CVMetalTextureCache5allocEPK13__CFAllocator.cold.1
+ _ZN20CVOpenGLTextureCache5allocEPK13__CFAllocator.cold.1
+ _ZN20CVPixelBufferBacking25prefetchNonIOSurfacePagesEv.cold.1
+ _ZN20CVPixelBufferBacking5allocEPK13__CFAllocator.cold.1
+ _ZN22CVOpenGLESTextureCache5allocEPK13__CFAllocator.cold.1
+ ___ZL41_cvDisplayLinkConvertServerMATtoClientMATy_block_invoke.cold.1
- _strcmp
CStrings:
+ "CVMTLTextureCreate texture validation failed"
- "1"

```
