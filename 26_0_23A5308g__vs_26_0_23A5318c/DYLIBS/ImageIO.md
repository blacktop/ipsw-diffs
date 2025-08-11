## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2772.0.1.0.0
-  __TEXT.__text: 0x3a1bd0
-  __TEXT.__auth_stubs: 0x41f0
+2773.0.1.1.0
+  __TEXT.__text: 0x3a1fdc
+  __TEXT.__auth_stubs: 0x41e0
   __TEXT.__objc_methlist: 0xd20
   __TEXT.__const: 0x2ebb8
-  __TEXT.__gcc_except_tab: 0x2113c
-  __TEXT.__cstring: 0x9b2d2
+  __TEXT.__gcc_except_tab: 0x211a0
+  __TEXT.__cstring: 0x9b48f
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
   __TEXT.__unwind_info: 0xd1e0

   __TEXT.__objc_methname: 0x2e13
   __TEXT.__objc_methtype: 0x24c0
   __TEXT.__objc_stubs: 0x2580
-  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__got: 0x600
   __DATA_CONST.__const: 0x4c088
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0xb10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2110
+  __AUTH_CONST.__auth_got: 0x2108
   __AUTH_CONST.__const: 0x3c840
   __AUTH_CONST.__cfstring: 0x35c60
   __AUTH_CONST.__objc_const: 0x1020

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 633AA0C4-EE47-3391-A4C4-7DF22E9B11C5
-  Functions: 13129
-  Symbols:   40975
-  CStrings:  24708
+  UUID: 30732223-E905-361A-B2C4-307BF63E204B
+  Functions: 13133
+  Symbols:   40983
+  CStrings:  24713
 
Symbols:
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table156
+ _CGContextDrawPDFPageWithOptions
+ __ZN14IIOImageSource14extractOptionsEP13IIODictionary.cold.1
+ __ZN14IIOImageSource14extractOptionsEP13IIODictionary.cold.2
+ __ZN14IIOImageSource14extractOptionsEP13IIODictionary.cold.3
+ __ZN14IIOImageSource14extractOptionsEP13IIODictionary.cold.4
+ __ZN14IIOImageSource18updateAllowedFlagsEPK7__CFSet
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.176
+ ___block_descriptor_tmp.180
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.64
+ ___block_literal_global.174
+ ___block_literal_global.178
+ ___block_literal_global.28
+ ___block_literal_global.51
+ _kCGDrawPDFPageDrawAnnotationsOptionKey
- GCC_except_table148
- GCC_except_table151
- _CGContextDrawPDFPage
- _CGContextDrawPDFPageWithAnnotations
- __ZN14IIOImageSource18updateAllowedflagsEPK7__CFSet
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.163
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.175
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.25
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.46
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.91
- ___block_literal_global.165
- ___block_literal_global.177
- ___block_literal_global.27
- ___block_literal_global.50
CStrings:
+ "*** ERROR: invalid options: cannot use empty kCGImageSourceDecodeFormatAllowlist\n"
+ "*** ERROR: invalid options: kCGImageSourceDecodeFormatAllowlist cannot be used when kCGImageSourceFailForDataNotMatchingHint is set to false\n"
+ "*** ERROR: invalid options: kCGImageSourceDecodeFormatAllowlist is not a CFArrayRef\n"
+ "*** ERROR: invalid options: kCGImageSourceFailForDataNotMatchingHint cannot be used without specifying a hint\n"
+ "*** ERROR: kCGImageSourceDecodeFormatAllowlist does not contain the provided hint '%s' - ignoring hint \n"
+ "*** NOTE: HEIC decoding is disabled -- decoding JPEG base image only (ignoring gain map)\n"
+ "*** NOTE: incorrect hint '%s' with kCGImageSourceFailForDataNotMatchingHint - dropping hint, using allowList\n"
+ "♦️  colorspace: %s\n"
- "*** ERROR: kCGImageSourceDecodeFormatAllowlist does not contain the provided hint '%s'\n"
- "*** ERROR: ❌ cannot use 'kCGImageSourceDecodeFormatAllowlist' without specifiying 'kCGImageSourceTypeIdentifierHint'\n"
- "*** JPEG with aux-image + 'fail-for-non-matching-hint are not compatible' - ignoring aux-image\n"

```
