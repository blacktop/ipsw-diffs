## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

```diff

-740.5.0.0.0
-  __TEXT.__text: 0xdc588
-  __TEXT.__auth_stubs: 0xe20
+742.5.0.0.0
+  __TEXT.__text: 0xdc728
+  __TEXT.__auth_stubs: 0xe30
   __TEXT.__gcc_except_tab: 0xab4
-  __TEXT.__oslogstring: 0xd10b
-  __TEXT.__cstring: 0x54d4
+  __TEXT.__oslogstring: 0xd139
+  __TEXT.__cstring: 0x54dd
   __TEXT.__const: 0xb956
-  __TEXT.__unwind_info: 0x1904
+  __TEXT.__unwind_info: 0x18bc
   __TEXT.__eh_frame: 0x2b8
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x38

   __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0x560
   __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__auth_got: 0x718
-  __DATA.__bss: 0x11
+  __AUTH_CONST.__auth_got: 0x720
   __DATA.__common: 0x50
+  __DATA.__bss: 0x1
   __DATA_DIRTY.__const: 0x23d0
   __DATA_DIRTY.__data: 0x70
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1894
-  Symbols:   4400
-  CStrings:  1691
+  Functions: 1895
+  Symbols:   4403
+  CStrings:  1693
 
Symbols:
+ _IOSurfaceGetCacheMode
+ __ZN17CAVDMvHevcDecoder28removeSubDpbPicturesInAuListEii
CStrings:
+ "20:21:20"
+ "20:21:21"
+ "20:21:22"
+ "AppleAVD: ERROR: %s: Incorrect Cache Mode=%d\n"
+ "May  1 2024"
- "00:21:48"
- "00:21:49"
- "Mar  9 2024"

```
