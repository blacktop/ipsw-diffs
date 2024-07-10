## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/Contents/MacOS/CIInpainting`

```diff

-1500.71.0.0.0
-  __TEXT.__text: 0x1b004
+1500.75.0.0.0
+  __TEXT.__text: 0x1c9e0
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_stubs: 0x25c0
-  __TEXT.__objc_methlist: 0xc74
-  __TEXT.__gcc_except_tab: 0x322c
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x25e9
-  __TEXT.__oslogstring: 0x3c8
+  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_methlist: 0xca4
+  __TEXT.__gcc_except_tab: 0x35a0
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x2921
+  __TEXT.__oslogstring: 0x419
   __TEXT.__objc_classname: 0x195
   __TEXT.__objc_methtype: 0xa91
-  __TEXT.__objc_methname: 0x3398
+  __TEXT.__objc_methname: 0x34f4
   __TEXT.__dlopen_cstrs: 0xdf
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x938
+  __TEXT.__unwind_info: 0x970
   __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x348
-  __DATA_CONST.__cfstring: 0x13e0
+  __DATA_CONST.__cfstring: 0x1580
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_doubleobj: 0x70
+  __DATA_CONST.__objc_doubleobj: 0x90
   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1248
-  __DATA.__objc_selrefs: 0xba8
-  __DATA.__objc_ivar: 0xbc
+  __DATA.__objc_const: 0x1278
+  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x500
   __DATA.__bss: 0x1b8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 370
-  Symbols:   183
-  CStrings:  257
+  Functions: 377
+  Symbols:   182
+  CStrings:  270
 
Symbols:
- _kCIFormatRGBA16
CStrings:
+ "CIInpaintFilter.inputExcludeMaskSurroundMultiplier"
+ "in_attn_mask"
+ "in_img_1"
+ "in_img_2"
+ "inputExcludeMaskSurroundMultiplier"
+ "kernel vec4 CIIP_add (__sample a, __sample b) { return vec4(a.r - b.r, 0.0, 0.0, 1.0); }"
+ "kernel vec4 CIIP_add (__sample a, __sample b) { return vec4(a.rgb + b.rgb, a.a); }"
+ "kernel vec4 CIIP_addR (__sample a, __sample b) { return vec4(a.r + b.r, a.gb, a.a); }"
+ "kernel vec4 CIIP_redOnly (__sample s) { return vec4(s.r,0,0,1); }"
+ "kernel vec4 CIIP_rgb_01_to_neg1pos1 (__sample s) { s.rgb = clamp(s.rgb, 0.0, 1.0); s.rgb = s.rgb * 2.0 -1.0; return s; }"
+ "kernel vec4 CIIP_rgb_neg1pos1_to_01 (__sample s) { s.rgb = (s.rgb + 1.0) / 2.0; s.rgb = clamp(s.rgb, 0.0, 1.0); return s; }"
+ "kernel vec4 CIIP_threshNegInf (__sample s) { float negInf = -1.0E20; float v = (s.r>0.01) ? negInf : 0.0; return vec4(v,0,0,1); }"
+ "out_img"

```
