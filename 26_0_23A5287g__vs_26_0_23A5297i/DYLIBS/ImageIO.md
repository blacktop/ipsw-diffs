## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2764.0.1.0.0
-  __TEXT.__text: 0x3a0c0c
+2769.0.4.0.0
+  __TEXT.__text: 0x3a1278
   __TEXT.__auth_stubs: 0x41d0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebb8
-  __TEXT.__gcc_except_tab: 0x21068
-  __TEXT.__cstring: 0x9ae1f
+  __TEXT.__gcc_except_tab: 0x21064
+  __TEXT.__cstring: 0x9b091
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd1d8
+  __TEXT.__unwind_info: 0xd1d0
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 58090C92-BAC7-30E5-A31D-4770DBC16875
-  Functions: 13126
-  Symbols:   40967
-  CStrings:  24684
+  UUID: 0790DC31-EFD2-3F72-ACCC-CF1DB5D7C790
+  Functions: 13128
+  Symbols:   40970
+  CStrings:  24698
 
Symbols:
+ GCC_except_table148
+ GCC_except_table151
+ __ZL32IIO_PixelBufferToCGImageBlockSetP10__CVBufferP15CGImageBlockSetP12CGImageBlock
+ __ZN10IIOScannerC2EPhyb
+ __ZN12IIOImagePlus11createImageEP13CGImageSourcePiPj.cold.2
+ __ZN13ATXReadPlugin10readHeaderER10IIOScannerj.cold.1
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.175
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.77
+ ___block_literal_global.177
+ ___block_literal_global.79
+ ___block_literal_global.89
- GCC_except_table150
- GCC_except_table152
- GCC_except_table156
- __ZL17myApplierFunctionPKvS0_Pv
- __ZN13IIODictionary4copyEv
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.166
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.44
- ___block_descriptor_tmp.86
- ___block_literal_global.176
- ___block_literal_global.88
CStrings:
+ "*** ERROR: '%c%c%c%c' - bad image size (%ld x %ld)\n"
+ "*** ERROR: '%c%c%c%c' - bad image size (%ld x %ld) rb: %ld\n"
+ "*** ERROR: IIOScanner::sizeForTypeAndCount: result size too large (%llu bytes)\n"
+ "*** ERROR: IterateChunks err = %d\n"
+ "*** ERROR: failed to read ATXHeader\n"
+ "*** IIOScanner: created with NULL buffer\n"
+ "*** IIOScanner: created with invalid buffer size: %llu\n"
+ "*** IIOScanner::copyBytes reached EOF\n"
+ "*** IIOScanner::copyBytes: null destination buffer\n"
+ "*** IIOScanner::sizeForTypeAndCount: unknown TIFF type %u\n"
+ "IIOScanner"
+ "ImageIO: CFDataGetBytes: data: %p size: %zu  offset: %zu count: %zu  dst: %p\n"
+ "IterateChunks"
+ "copyBytes"
+ "embedded profile '%c%c%c%c' does not match expected color model '%c%c%c%c' - dropping embedded profile\n"
+ "sizeForTypeAndCount"
- "*** ERROR: bad image size (%ld x %ld) rb: %ld\n"
- "embedded profile '%c%c%c%c' does not match expected color model '%c%c%c%c'\n"

```
