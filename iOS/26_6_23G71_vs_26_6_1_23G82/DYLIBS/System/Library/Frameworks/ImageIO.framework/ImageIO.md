## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

 2784.6.6.0.0
-  __TEXT.__text: 0x449afc
+  __TEXT.__text: 0x44a12c
   __TEXT.__auth_stubs: 0x4280
   __TEXT.__objc_methlist: 0xd58
   __TEXT.__const: 0x31648
-  __TEXT.__gcc_except_tab: 0x265a4
-  __TEXT.__cstring: 0x9e156
+  __TEXT.__gcc_except_tab: 0x2667c
+  __TEXT.__cstring: 0x9e62a
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xed68
+  __TEXT.__unwind_info: 0xed80
   __TEXT.__eh_frame: 0x3d0
   __TEXT.__objc_classname: 0xf1
   __TEXT.__objc_methname: 0x2e87

   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x2f58
+  __DATA.__data: 0x2f98
   __DATA.__bss: 0x4f90
   __DATA.__common: 0x3928
   __DATA_DIRTY.__data: 0x168

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15506
-  Symbols:   22829
-  CStrings:  17992
+  Functions: 15504
+  Symbols:   22831
+  CStrings:  18012
 
Symbols:
+ __ZN13GlobalGIFInfo14globalColorMapEv
+ __ZZ41CGImageMetadataRegisterNamespaceForPrefixE22alreadyRegistered_lock
CStrings:
+ "*** ERROR: CG fallback rowBytes overflow rounding up: product=%u\n"
+ "*** ERROR: CG fallback rowBytes overflow: dstWidth=%zu * bpp=%u\n"
+ "*** ERROR: Extended XMP marker XMP data is NULL, skipping marker\n"
+ "*** ERROR: IOSurface does not support chroma rowBytes larger than INT32_MAX"
+ "*** ERROR: _TAG::writeToBuffer - out-of-bounds source: offset: %u  tiffStart: %u  size: %u  jpegDataSize: %ld\n"
+ "*** ERROR: copyDateTime - out-of-bounds: offset: %u  tiffStart: %u  count: %u  size: %ld\n"
+ "*** ERROR: dstRowBytes overflow: dstWidth=%zu * (bpp/8)=%u\n"
+ "*** ERROR: iio_convert_XRGB2101010ToRGB16U: MALLOC(%zu) failed\n"
+ "*** ERROR: iio_convert_XRGB2101010ToRGB16U: rowBytes overflow (width=%zu)\n"
+ "*** ERROR: image dimensions exceed UINT32_MAX: %zu x %zu\n"
+ "*** ERROR: preserveGainMapUsingCFDataRef - gain map descriptor (%u x %u, rowBytes %u) inconsistent with %ld-byte source; skipping\n"
+ "*** ERROR: subsampleRGB888 MALLOC failed (src=%p dst=%p, %zu x %u)\n"
+ "*** IOSurface does not support allocSize larger than INT32_MAX\n"
+ "*** IOSurface does not support rowBytes/allocSize larger than INT32_MAX\n"
+ "*** dest buffer size overflow [%u x %u x %zu]\n"
+ "*** invalid row bytes (src=%u dst=%u)\n"
+ "IIO_UpdatePlanarSurfaceOptions"
+ "IIO_UpdateSurfaceOptions"
+ "copyDateTime"
+ "writeToBuffer"
```
