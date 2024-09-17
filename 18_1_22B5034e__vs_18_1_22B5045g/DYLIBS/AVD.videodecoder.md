## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-798.1.0.0.0
-  __TEXT.__text: 0x1146ec
+805.0.0.0.0
+  __TEXT.__text: 0x12b6b8
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__const: 0xbb7b
-  __TEXT.__oslogstring: 0xeeb3
-  __TEXT.__cstring: 0x5afc
-  __TEXT.__gcc_except_tab: 0xb44
-  __TEXT.__unwind_info: 0x18e0
+  __TEXT.__gcc_except_tab: 0xc54
+  __TEXT.__const: 0xbcdb
+  __TEXT.__oslogstring: 0xef6f
+  __TEXT.__cstring: 0x5bff
+  __TEXT.__unwind_info: 0x1a88
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x3560
+  __AUTH_CONST.__const: 0x3aa0
   __AUTH_CONST.__cfstring: 0x5e0
   __DATA.__common: 0x50
   __DATA.__bss: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2076
-  Symbols:   2518
-  CStrings:  1853
+  Functions: 2221
+  Symbols:   2684
+  CStrings:  1862
 
CStrings:
+ "AppleAVD: %!s(MISSING)(): chip id is not used while ecid and/or board id is used\n"
+ "int32_t CAHDecTansyAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "CAHDecTansyLgh"
+ "CAHDecTansyAvc"
+ "Sep  2 2024"
+ "int32_t CAHDecTansyAvx::getUpscaleConvolveStep(int, int)"
+ "AppleAVD: %!s(MISSING)(): H13A descrambler is not supported\n"
+ "22:36:38"
+ "CAHDecTansyAvx"
+ "int CAHDecTansyAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "populateDecryptionRegisters"
+ "read_obu_size"
+ "22:36:37"
+ "AppleAVD: %!s(MISSING): ERROR, obu size can't be larger than size of buffer\n"
+ "22:36:39"
+ "CAHDecTansyHevc"
+ "virtual int CAHDecTansyAvx::populatePictureRegisters()"
+ "AppleAVD: AppleAVDDecodeFrameResponse kVASetSkipToNextIDR error: %!d(MISSING)"
- "createTansyAvxDecoder"
- "19:59:58"
- "createTansyAvcDecoder"
- "19:59:59"
- "AppleAVD: %!s(MISSING)(): Tansy AVD is not supported in this AppleAVD driver!!!"
- "Aug 16 2024"
- "19:59:57"
- "createTansyHevcDecoder"
- "createTansyLghDecoder"

```
