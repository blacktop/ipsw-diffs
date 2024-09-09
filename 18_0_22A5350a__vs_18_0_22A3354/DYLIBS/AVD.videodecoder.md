## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 798.1.0.0.0
-  __TEXT.__text: 0x1146ec
+  __TEXT.__text: 0x156224
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__const: 0xbb7b
-  __TEXT.__oslogstring: 0xeeb3
-  __TEXT.__cstring: 0x5af3
-  __TEXT.__gcc_except_tab: 0xb44
-  __TEXT.__unwind_info: 0x18e0
+  __TEXT.__gcc_except_tab: 0xe74
+  __TEXT.__const: 0xbff3
+  __TEXT.__oslogstring: 0xee59
+  __TEXT.__cstring: 0x5da6
+  __TEXT.__unwind_info: 0x1dc8
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x3560
+  __AUTH_CONST.__const: 0x4520
   __AUTH_CONST.__cfstring: 0x5e0
   __DATA.__common: 0x50
   __DATA.__bss: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2076
-  Symbols:   2518
-  CStrings:  1852
+  Functions: 2504
+  Symbols:   3013
+  CStrings:  1864
 
CStrings:
+ "CAHDecThymeAvx"
+ "01:13:29"
+ "AppleAVD: %!s(MISSING)(): H13A descrambler is not supported\n"
+ "AppleAVD: %!s(MISSING)(): chip id is not used while ecid and/or board id is used\n"
+ "CAHDecTansyHevc"
+ "CAHDecHibiscusAvc"
+ "int32_t CAHDecThymeAvx::getUpscaleConvolveStep(int, int)"
+ "int32_t CAHDecThymeAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "CAHDecTansyLgh"
+ "CAHDecThymeLgh"
+ "int CAHDecTansyAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "virtual int CAHDecHibiscusAvx::populatePictureRegisters()"
+ "virtual int CAHDecTansyAvx::populatePictureRegisters()"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveStep(int, int)"
+ "01:13:28"
+ "CAHDecTansyAvc"
+ "CAHDecHibiscusLgh"
+ "int32_t CAHDecTansyAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "int CAHDecThymeAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "int32_t CAHDecTansyAvx::getUpscaleConvolveStep(int, int)"
+ "CAHDecThymeAvc"
+ "CAHDecThymeHevc"
+ "CAHDecHibiscusAvx"
+ "CAHDecHibiscusHevc"
+ "CAHDecTansyAvx"
+ "int CAHDecHibiscusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "virtual int CAHDecThymeAvx::populatePictureRegisters()"
+ "populateDecryptionRegisters"
- "03:25:33"
- "AppleAVD: %!s(MISSING)(): Thyme AVD is not supported in this AppleAVD driver!!!"
- "createThymeLghDecoder"
- "createThymeHevcDecoder"
- "createHibiscusAvxDecoder"
- "createThymeAvxDecoder"
- "AppleAVD: %!s(MISSING)(): Tansy AVD is not supported in this AppleAVD driver!!!"
- "createTansyLghDecoder"
- "createHibiscusAvcDecoder"
- "createTansyHevcDecoder"
- "createHibiscusLghDecoder"
- "createHibiscusHevcDecoder"
- "03:25:32"
- "createTansyAvcDecoder"
- "createThymeAvcDecoder"
- "AppleAVD: %!s(MISSING)(): Hibiscus AVD is not supported in this AppleAVD driver!!!"
- "createTansyAvxDecoder"

```
