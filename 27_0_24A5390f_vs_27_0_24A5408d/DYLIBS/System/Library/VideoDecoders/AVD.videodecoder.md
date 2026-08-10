## AVD.videodecoder

> `/System/Library/VideoDecoders/AVD.videodecoder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-991.0.0.0.0
-  __TEXT.__text: 0x16ba28
+993.1.0.0.0
+  __TEXT.__text: 0x16bd88
   __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0xc1e3
-  __TEXT.__oslogstring: 0x16210
-  __TEXT.__cstring: 0x56b6
+  __TEXT.__oslogstring: 0x16252
+  __TEXT.__cstring: 0x56bd
   __TEXT.__gcc_except_tab: 0xd4c
-  __TEXT.__unwind_info: 0x1dc8
+  __TEXT.__unwind_info: 0x1de0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4120
-  Symbols:   3390
-  CStrings:  2073
+  Functions: 4124
+  Symbols:   3393
+  CStrings:  2074
 
Symbols:
+ __ZN14CAVDAvxDecoder15validateRefBufsEv
+ __ZN14CAVDAvxDecoder18VAUnmapPixelBufferEij
+ __ZN14CAVDLghDecoder15validateRefBufsEv
+ __ZN14CAVDLghDecoder18VAUnmapPixelBufferEij
- GCC_except_table17
Functions:
~ __ZN22AppleAVDCommandBuilder14decodeFrameFigEP26_sAppleAVDDecodeFrameFigInP27_sAppleAVDDecodeFrameFigOut : 4812 -> 4800
~ __ZN14CAVDAvxDecoder13VADecodeFrameEPhijiiiP14avd_seq_params : 3804 -> 3816
+ __ZN14CAVDAvxDecoder15validateRefBufsEv
+ __ZN14CAVDAvxDecoder18VAUnmapPixelBufferEij
~ __ZN14CAVDLghDecoder13VADecodeFrameEPhijiiiP14avd_seq_params : 4168 -> 4200
+ __ZN14CAVDLghDecoder15validateRefBufsEv
+ __ZN14CAVDLghDecoder18VAUnmapPixelBufferEij
~ __ZN14CAVDAvcDecoder24decodeGetRenderTargetRefEjjjPP9_vsurface : 992 -> 1004
~ __ZN22AppleAVDCommandBuilderC2Ejh : 516 -> 504
- __ZN22AppleAVDCommandBuilder15allocRVRAMemoryEjj
+ __ZN22AppleAVDCommandBuilder15allocRVRAMemoryEjj
~ __ZN15CAVDHevcDecoder24decodeGetRenderTargetRefEjPP9_vsurface : 900 -> 916
CStrings:
+ "21:54:05"
+ "21:54:07"
+ "AppleAVD: INFO: %{public}s(): GUARDED: ref[%u] buf=%p dec_buf=%p\n"
+ "Aug  5 2026"
+ "validateRefBufs"
- "21:35:53"
- "21:35:54"
- "21:35:55"
- "Jul 14 2026"
```
