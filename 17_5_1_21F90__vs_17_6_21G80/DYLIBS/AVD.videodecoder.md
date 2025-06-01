## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-742.5.0.0.0
-  __TEXT.__text: 0xdc728
+743.5.0.0.0
+  __TEXT.__text: 0xdc794
   __TEXT.__auth_stubs: 0xe30
   __TEXT.__gcc_except_tab: 0xab4
-  __TEXT.__oslogstring: 0xd139
-  __TEXT.__cstring: 0x54dd
+  __TEXT.__oslogstring: 0xd1a8
+  __TEXT.__cstring: 0x54d4
   __TEXT.__const: 0xb956
   __TEXT.__unwind_info: 0x18bc
   __TEXT.__eh_frame: 0x2b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: F72B7142-9412-3638-B6A1-44606C5AF01A
+  UUID: ACB01575-45AB-3F89-B542-4D14D78A363F
   Functions: 1895
   Symbols:   4403
-  CStrings:  1736
+  CStrings:  1735
 
CStrings:
+ "18:18:00"
+ "18:18:01"
+ "AppleAVD: ERROR: %s(): pic size too large - either width (%d, %d) or height (%d, %d) > max dim. %d and it's 4:2:0, 8 bit, so software decoder can handle it."
+ "AppleAVD: WARNING: %s(): pic size too wide %d %d or tall %d %d vs. %d but depth %d chroma fmt %d, so we'll attempt it anyway"
+ "Jul  5 2024"
- "20:21:20"
- "20:21:21"
- "20:21:22"
- "AppleAVD: AVC sps[%d] width %d height %d over size in %s\n"
- "AppleAVD: ERROR: %s(): picture size too large - either width (%d) or height (%d) exceeds maximum dimension of %d"
- "May  1 2024"

```
