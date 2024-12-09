## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

 808.0.0.0.0
-  __TEXT.__text: 0x12b900
+  __TEXT.__text: 0x156668
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__gcc_except_tab: 0xc5c
-  __TEXT.__const: 0xbcdb
-  __TEXT.__oslogstring: 0xf00c
-  __TEXT.__cstring: 0x5bf6
-  __TEXT.__unwind_info: 0x1aa0
+  __TEXT.__gcc_except_tab: 0xe7c
+  __TEXT.__const: 0xbff3
+  __TEXT.__oslogstring: 0xef7d
+  __TEXT.__cstring: 0x5db4
+  __TEXT.__unwind_info: 0x1de0
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x3aa0
+  __AUTH_CONST.__const: 0x4520
   __AUTH_CONST.__cfstring: 0x5e0
   __DATA.__common: 0x50
   __DATA.__bss: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 2222
-  Symbols:   2684
-  CStrings:  1863
+  Functions: 2506
+  Symbols:   3014
+  CStrings:  1869
 
CStrings:
+ "22:55:20"
+ "22:55:22"
+ "CAHDecHibiscusAvc"
+ "CAHDecHibiscusAvx"
+ "CAHDecHibiscusHevc"
+ "CAHDecHibiscusLgh"
+ "CAHDecThymeAvc"
+ "CAHDecThymeAvx"
+ "CAHDecThymeHevc"
+ "CAHDecThymeLgh"
+ "int CAHDecHibiscusAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "int CAHDecThymeAvc::populateSliceRegisters(AvcSliceRegisters *, int)"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveStep(int, int)"
+ "int32_t CAHDecHibiscusAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "int32_t CAHDecThymeAvx::getUpscaleConvolveStep(int, int)"
+ "int32_t CAHDecThymeAvx::getUpscaleConvolveX0(int, int, int32_t)"
+ "virtual int CAHDecHibiscusAvx::populatePictureRegisters()"
+ "virtual int CAHDecThymeAvx::populatePictureRegisters()"
- "23:05:58"
- "23:05:59"
- "AppleAVD: %s(): Hibiscus AVD is not supported in this AppleAVD driver!!!"
- "AppleAVD: %s(): Thyme AVD is not supported in this AppleAVD driver!!!"
- "createHibiscusAvcDecoder"
- "createHibiscusAvxDecoder"
- "createHibiscusHevcDecoder"
- "createHibiscusLghDecoder"
- "createThymeAvcDecoder"
- "createThymeAvxDecoder"
- "createThymeHevcDecoder"
- "createThymeLghDecoder"

```
