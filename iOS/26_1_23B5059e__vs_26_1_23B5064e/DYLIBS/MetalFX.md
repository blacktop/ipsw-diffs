## MetalFX

> `/System/Library/Frameworks/MetalFX.framework/MetalFX`

```diff

-31.4.0.0.0
-  __TEXT.__text: 0x500d4
+31.5.0.0.0
+  __TEXT.__text: 0x4ff74
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x3da4
-  __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0x84f0
-  __TEXT.__cstring: 0x2ece
+  __TEXT.__objc_methlist: 0x3db4
+  __TEXT.__const: 0x260
+  __TEXT.__gcc_except_tab: 0x8464
+  __TEXT.__cstring: 0x2ef7
   __TEXT.__unwind_info: 0xc28
   __TEXT.__objc_classname: 0x5db
   __TEXT.__objc_methname: 0x52be
-  __TEXT.__objc_methtype: 0xd20
+  __TEXT.__objc_methtype: 0xd30
   __TEXT.__objc_stubs: 0x2d20
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x1f8

   __DATA_CONST.__objc_selrefs: 0x1018
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x2a38
+  __DATA_CONST.__objc_arraydata: 0x2998
   __AUTH_CONST.__auth_got: 0x4a0
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x3e40
+  __AUTH_CONST.__cfstring: 0x3e60
   __AUTH_CONST.__objc_const: 0xa818
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x2a48
+  __AUTH_CONST.__objc_arrayobj: 0x29e8
   __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0xb58
   __DATA.__data: 0x8a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83468844-608C-32DD-B3F4-9052A98D5554
-  Functions: 1191
-  Symbols:   4185
-  CStrings:  2065
+  UUID: 6DFDE59F-0527-30EA-92BE-2868D590F626
+  Functions: 1192
+  Symbols:   4187
+  CStrings:  2067
 
Symbols:
+ -[_MFXTemporalDenoisingScalingEffect reactiveMaskTextureFormat]
+ GCC_except_table114
+ GCC_except_table122
+ GCC_except_table124
+ __Z12checkTexturePU21objcproto10MTLTexture11objc_objectmmP8NSStringbb14MTLPixelFormatS2_
+ ___block_literal_global.1310
- GCC_except_table112
- GCC_except_table115
- GCC_except_table123
- __Z12checkTexturePU21objcproto10MTLTexture11objc_objectmmP8NSStringbb14MTLPixelFormat
- ___block_literal_global.1324
CStrings:
+ "%@ and %@ should have the same height for MetalFX use"
+ "%@ and %@ should have the same width for MetalFX use"
+ "luma_log_sum_denoiser"
+ "luma_log_sum_to_exposure_denoiser"
+ "{DBFNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"output_width\"I\"output_height\"I\"output_channels\"I\"input_padding\"I}"
- "%@ and Color should have the same height for MetalFX use"
- "%@ and Color should have the same width for MetalFX use"
- "tensor35"
- "{DBFNetDescriptor=\"version\"i\"image_width\"I\"image_height\"I\"input_width\"I\"input_height\"I\"input_channels\"I\"output_width\"I\"output_height\"I\"output_channels\"I}"

```
