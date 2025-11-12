## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.2.2.0.0
-  __TEXT.__text: 0x3a61c0
+2784.2.2.1.2
+  __TEXT.__text: 0x3a6758
   __TEXT.__auth_stubs: 0x41f0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebf8
   __TEXT.__gcc_except_tab: 0x212b8
-  __TEXT.__cstring: 0x9c813
+  __TEXT.__cstring: 0x9ca2d
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd298
+  __TEXT.__unwind_info: 0xd2a0
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5A5FCC3E-2C66-3494-85B3-861D70941C7C
-  Functions: 13175
-  Symbols:   41072
-  CStrings:  24808
+  UUID: 29E74973-9D06-3269-9E50-03976AD088D8
+  Functions: 13182
+  Symbols:   41086
+  CStrings:  24821
 
Symbols:
+ __ZN14ASTCTextureImp20decodeRGBXFromLinearEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.3
+ __ZN14ASTCTextureImp20decodeRGBXFromMemoryEPvlP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.2
+ __ZN14ASTCTextureImp20decodeRGBXFromMemoryEPvlP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.3
+ __ZN14ASTCTextureImp22decodeRGBXFromTwiddledEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.1
+ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.2
+ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.3
+ __ZN14ASTCTextureImp25decodeRGBXFromLinearLZFSEEP19IIOImageReadSessionP13vImage_Buffer10at_alpha_t17at_block_format_t17at_texel_format_t.cold.4
+ ___block_literal_global.104
- ___block_literal_global.92
CStrings:
+ "*** ERROR: Integer overflow in buffer size calculation (blockDim: %ux%u)\n"
+ "*** ERROR: MALLOC failed for %u bytes\n"
+ "*** ERROR: MALLOC failed for %zu bytes\n"
+ "*** ERROR: dstBuffer or dstBuffer->data is NULL\n"
+ "*** ERROR: invalid dimensions %ldx%ld\n"
+ "*** ERROR: invalid dimensions %zux%zu\n"
+ "*** ERROR: invalid texture height: %d\n"
+ "*** ERROR: invalid texture width: %d\n"
+ "*** ERROR: rowBytes %ld < width*4 (%ld)\n"
+ "*** ERROR: rowBytes %zu < width*4 (%zu)\n"
+ "*** ERROR: src.rowBytes is zero, cannot clamp buffer\n"
+ "*** bad file ***  (fileSize: %u   compressedDataOffset: %u   compressedSize: %u\n"
+ "*** bad input data (input size: %zu  bytesNeeded: %zu  (%d x %d) bpp: %g)\n"
+ "got: %zu expected: %u\n"
+ "got: %zu expected: %zu\n"
- "*** bad file ***  (fileSize: %ld   compressedDataOffset: %ld   compressedSize: %ld\n"
- "*** bad input data (input size: %ld  bytesNeeded: %d  (%d x %d) bpp: %g)\n"

```
