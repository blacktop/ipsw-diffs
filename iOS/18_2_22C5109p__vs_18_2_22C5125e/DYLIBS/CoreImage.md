## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1510.14.0.0.0
-  __TEXT.__text: 0x2c1e84
+1510.60.2.0.0
+  __TEXT.__text: 0x2c1ff4
   __TEXT.__auth_stubs: 0x2f90
   __TEXT.__objc_methlist: 0x14d48
-  __TEXT.__const: 0xe548
+  __TEXT.__const: 0xe568
   __TEXT.__gcc_except_tab: 0x5918
-  __TEXT.__cstring: 0x84c44
+  __TEXT.__cstring: 0x84cfd
   __TEXT.__oslogstring: 0x9d73
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__runtimeheader: 0xb8ec
   __TEXT.__cikl2metal_pre: 0x47f
-  __TEXT.__unwind_info: 0x6d18
+  __TEXT.__unwind_info: 0x6ff0
   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x29e3
-  __TEXT.__objc_methname: 0x2165a
-  __TEXT.__objc_methtype: 0x6bdc
+  __TEXT.__objc_methname: 0x2165c
+  __TEXT.__objc_methtype: 0x6bc0
   __TEXT.__objc_stubs: 0x12080
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__const: 0x6b88

   __AUTH_CONST.__objc_floatobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x99c0
-  __AUTH.__data: 0x1dfd8
+  __AUTH.__data: 0x1e090
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x20a0
-  __DATA.__data: 0x57e0
+  __DATA.__data: 0x57f0
   __DATA.__bss: 0x3a38
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13816
-  Symbols:   15762
+  Functions: 13818
+  Symbols:   15764
   CStrings:  14907
 
CStrings:
+ "kernel vec4 _headroomClamp(vec4 img, float targHR) {\n  float rgb_max = max(max(img.r, img.g), img.b);\n  return (rgb_max <= targHR) ? img : vec4((img.rgb * targHR) / rgb_max, img.a);\n}\n"
+ "srcHeadroom"
- "uniforms:"
- "{Uniforms=fffffff}20@0:8f16"

```
