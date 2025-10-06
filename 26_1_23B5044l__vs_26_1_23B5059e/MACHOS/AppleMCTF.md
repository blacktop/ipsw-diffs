## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.88.0.0.0
-  __TEXT.__text: 0x75aa8
+904.97.1.0.0
+  __TEXT.__text: 0x76130
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x236d5
-  __TEXT.__const: 0x1eaf8
+  __TEXT.__cstring: 0x23831
+  __TEXT.__const: 0x1f1c8
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__unwind_info: 0x610
   __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4188
+  __DATA_CONST.__const: 0x41b0
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x198
-  __DATA.__bss: 0x860
+  __DATA.__bss: 0x910
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB04649E-56E2-38D3-AF7C-4B68FE81EFBD
-  Functions: 614
+  UUID: A7852B08-1E09-36B8-90C8-7C0BB4C12AAC
+  Functions: 619
   Symbols:   354
-  CStrings:  2980
+  CStrings:  2988
 
CStrings:
+ "%lld %d AVE %s: %s LookAhead Frame Count %d"
+ "%lld %d AVE %s: %s LookAhead Frame Count %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d snr %d noise level %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d snr %d noise level %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d s %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x noise level %d rIdx %d s %d\n"
+ "%s LookAhead Frame Count %d"
+ "%s LookAhead Frame Count %d\n"
+ "21:24:06"
+ "904.97.1"
+ "AVE_MCTF_CalculateNoiseLevel_TotalGainSNR"
+ "Oct  1 2025"
+ "SetLookAheadInfo"
- "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d"
- "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d\n"
- "20:27:11"
- "904.88.0"
- "Sep 16 2025"

```
