## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

-1510.7.0.0.0
-  __TEXT.__text: 0xadcc
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x448
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x1528
-  __TEXT.__cstring: 0x1835
+1510.11.0.0.0
+  __TEXT.__text: 0xb3fc
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x45c
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x1620
+  __TEXT.__cstring: 0x1925
   __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methname: 0x1239
-  __TEXT.__objc_methtype: 0x23c
-  __TEXT.__oslogstring: 0x57a
+  __TEXT.__objc_methname: 0x1262
+  __TEXT.__objc_methtype: 0x24a
+  __TEXT.__oslogstring: 0x5b6
   __TEXT.__dlopen_cstrs: 0x91
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x300
+  __TEXT.__unwind_info: 0x438
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x1f8
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__cfstring: 0xc60
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x608
-  __DATA.__objc_selrefs: 0x5e0
+  __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x130
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 165
-  Symbols:   160
-  CStrings:  420
+  Functions: 169
+  Symbols:   162
+  CStrings:  427
 
Symbols:
+ _objc_retain_x24
+ _CGRectIntegral
CStrings:
+ "blendBack:mask:"
+ "kernel vec4 CIIP_y_plus_y (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(a.r + b.r, 0.0, 0.0, 1.0); }"
+ "kernel vec4 CIIP_replace_y (__sample a, __sample b) __attribute__((preserves_opacity)) { return vec4(b.r * a.a, a.gb, a.a); }"
+ "kernel vec4 CIIP_y_diff (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(a.r - b.r, 0.0, 0.0, 1.0); }"
+ "dilateSize"
+ "inputMaximumDistance"
+ "kernel vec4 CIIP_y_clamp_m1p1 (__sample a) __attribute__((outputFormat(kCIFormatRh))) { float Y = clamp(a.r, -1.0, 1.0); return vec4(Y, 0.0, 0.0, 1.0); }"
+ "kernel vec4 CIIP_ycc_neg1pos1_to_01 (__sample s) __attribute__((preserves_opacity)) { s.rgb = (s.rgb + 1.0) / 2.0; s.rgb = clamp(s.rgb, 0.0, s.a); return s; }"
+ "CIConvolution5X5"
+ "smallBlurSize"
+ "CIDistanceGradientFromRedMask"
+ "@32@0:8@16@24"
+ "vectorWithValues:count:"
+ "kernel vec4 CIIP_ycc_01_to_neg1pos1 (__sample s) __attribute__((preserves_opacity)) { s.rgb = clamp(s.rgb, 0.0, 1.0); s.rgb = s.rgb * 2.0 -1.0; return s; }"
+ "%!{(MISSING)public}@: CIInpaintModel.smallBlurSize default set to %!g(MISSING)."
+ "CIInpaintFilter.smallBlurSize"
+ "inputWeights"
- "CIMorphologyRectangleMaximum"
- "inputWidth"
- "blendBack:"
- "integerValue"
- "kernel vec4 CIIP_rgb_01_to_neg1pos1 (__sample s) __attribute__((preserves_opacity)) { s.rgb = clamp(s.rgb, 0.0, 1.0); s.rgb = s.rgb * 2.0 -1.0; return s; }"
- "kernel vec4 CIIP_addR (__sample a, __sample b) __attribute__((preserves_opacity)) { return vec4(a.r + b.r, a.gb, a.a); }"
- "kernel vec4 CIIP_add (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(a.r - b.r, 0.0, 0.0, 1.0); }"
- "inputHeight"
- "kernel vec4 CIIP_add (__sample a, __sample b) __attribute__((preserves_opacity)) { return vec4(a.rgb + b.rgb, a.a); }"
- "kernel vec4 CIIP_rgb_neg1pos1_to_01 (__sample s) __attribute__((preserves_opacity)) { s.rgb = (s.rgb + 1.0) / 2.0; s.rgb = clamp(s.rgb, 0.0, 1.0); return s; }"

```
