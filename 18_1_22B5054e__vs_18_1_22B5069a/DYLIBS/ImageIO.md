## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2646.0.0.0.0
-  __TEXT.__text: 0x3fb9d8
-  __TEXT.__auth_stubs: 0x3fd0
-  __TEXT.__objc_methlist: 0x938
-  __TEXT.__const: 0x31478
-  __TEXT.__gcc_except_tab: 0x1f1d0
-  __TEXT.__cstring: 0x79c43
+2650.1.1.2.0
+  __TEXT.__text: 0x3fc318
+  __TEXT.__auth_stubs: 0x3ff0
+  __TEXT.__objc_methlist: 0x940
+  __TEXT.__const: 0x314c8
+  __TEXT.__gcc_except_tab: 0x1f210
+  __TEXT.__cstring: 0x79f61
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd210
+  __TEXT.__unwind_info: 0xd220
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x29f2
-  __TEXT.__objc_methtype: 0x1eec
-  __TEXT.__objc_stubs: 0x2260
+  __TEXT.__objc_methname: 0x2a12
+  __TEXT.__objc_methtype: 0x1efc
+  __TEXT.__objc_stubs: 0x2280
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0xf4b0
+  __DATA_CONST.__const: 0xf4d0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x940
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2000
+  __AUTH_CONST.__auth_got: 0x2010
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3caf8
-  __AUTH_CONST.__cfstring: 0xd9e0
+  __AUTH_CONST.__const: 0x3cb48
+  __AUTH_CONST.__cfstring: 0xda20
   __AUTH_CONST.__objc_const: 0x1248
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13101
-  Symbols:   15476
-  CStrings:  12535
+  Functions: 13108
+  Symbols:   15485
+  CStrings:  12554
 
Symbols:
+ _CGColorSpaceCopyFromIOSurface
+ _vImageConvert_RGBA8888toRGB888
CStrings:
+ "    CMPhotoCompressionSessionAddImage (420f): [session:%!p(MISSING)]  err=%!d(MISSING)\n"
+ "    CMPhotoCompressionSessionAddImage: [session:%!p(MISSING)] '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)' err=%!d(MISSING)\n"
+ "(DP)"
+ "(IP-S)"
+ "*** BC - unknown GL pixel format [0x%!X(MISSING)]\n"
+ "*** ERROR: dstColorSpace is extended, but requested bitsPerComponent is '%!d(MISSING)'\n"
+ "*** ERROR: dxgi-format '%!d(MISSING)' not handled\n"
+ "*** NOTE: outside sRGB: changing compType from %!s(MISSING) to %!s(MISSING)\n"
+ "*** Note: switching write plugin (auxImage): 'JPEG' --> 'HEIC'  (_transcodingMode: %!d(MISSING))\n"
+ "@32@0:8r^f16Q24"
+ "COL extended-sRGB --> P3 converting (created-surface)\n"
+ "COL extended-sRGB --> P3 converting (wrapping surface)\n"
+ "COL extended-sRGB 32-bit --> P3 16-bit\n"
+ "COL extended-sRGB-%!d(MISSING) --> P3 8-bit\n"
+ "COL extended-sRGB-16 --> P3 16-bit\n"
+ "COL input: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'  output: '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)'  \n"
+ "R16Float"
+ "[%!@(MISSING)] %!@(MISSING)"
+ "[%!p(MISSING)] {%!l(MISSING)d,%!l(MISSING)d}  rb:%!l(MISSING)d  bpc:%!l(MISSING)d  %!s(MISSING) %!s(MISSING)%!s(MISSING)"
+ "com.apple.IDSBlastDoorService"
+ "dxgi_to_gl"
+ "seq  _creatingHEIFSequence: YES\n"
+ "state->codestream != NULL"
+ "swapWriterIfNeeded"
+ "tableDataWithFloatValues:count:"
+ "v24@?0r^{CGColorTRC=i(?={CGColorTRCParametric=ffffffff}{CGColorTRCTable=Q^f{CGColorTRCBoundaryExtension=ff}{CGColorTRCBoundaryExtension=ff}})}8^{?=i{?=ffffffff}^v}16"
+ "☀️  CGImageCreateByConvertingExtendedSRGBToColorspace\n"
+ "☀️  wrappingIOSurface - using original images/IOSurface (no EncodeRequest)...\n"
- "    CMPhotoCompressionSessionAddImage: [session:%!p(MISSING)]  err=%!d(MISSING)\n"
- "*** ERROR: unsupported colorSpaceModel [JFIF] (%!d(MISSING))\n"
- "*** NOT _isSRGB + componentType: changing %!s(MISSING) to %!s(MISSING)\n"
- "COL extended-sRGB --> P3 16-bit\n"
- "COL extended-sRGB --> P3 8-bit\n"
- "COL extended-sRGB --> P3 converting\n"
- "[%!p(MISSING)] {%!l(MISSING)d,%!l(MISSING)d}  rb:%!l(MISSING)d  bpc:%!l(MISSING)d  (%!s(MISSING)) %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)"
- "seq  _creatingHEIFSequence: %!s(MISSING)\n"
- "☀️  wrappingIOSurface - using original images/IOSurface...\n"

```
