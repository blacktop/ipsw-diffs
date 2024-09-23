## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1510.7.0.0.0
-  __TEXT.__text: 0x2c18e8
-  __TEXT.__auth_stubs: 0x2f70
+1510.11.0.0.0
+  __TEXT.__text: 0x2c1f64
+  __TEXT.__auth_stubs: 0x2f90
   __TEXT.__objc_methlist: 0x14d48
-  __TEXT.__const: 0xe548
-  __TEXT.__gcc_except_tab: 0x58f0
-  __TEXT.__cstring: 0x84c1f
-  __TEXT.__oslogstring: 0x9d53
+  __TEXT.__const: 0xe538
+  __TEXT.__gcc_except_tab: 0x5918
+  __TEXT.__cstring: 0x84c67
+  __TEXT.__oslogstring: 0x9d73
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__runtimeheader: 0xb8ec
   __TEXT.__cikl2metal_pre: 0x47f
-  __TEXT.__unwind_info: 0x6d10
+  __TEXT.__unwind_info: 0x6d18
   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x29e3
   __TEXT.__objc_methname: 0x2165a

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x368
   __DATA_CONST.__objc_arraydata: 0x1400
-  __AUTH_CONST.__auth_got: 0x17d0
+  __AUTH_CONST.__auth_got: 0x17e0
   __AUTH_CONST.__auth_ptr: 0x60
   __AUTH_CONST.__const: 0xbb60
   __AUTH_CONST.__cfstring: 0x196c0

   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x20a0
   __DATA.__data: 0x57d8
-  __DATA.__bss: 0x3a50
+  __DATA.__bss: 0x3a38
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x4a8
+  __DATA_DIRTY.__bss: 0x4b8
   __DATA_DIRTY.__common: 0x1d0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13816
-  Symbols:   15760
-  CStrings:  14905
+  Functions: 13818
+  Symbols:   15764
+  CStrings:  14907
 
Symbols:
+ _CFDataCreate
+ _CVBufferCopyAttachment
CStrings:
+ "kernel vec4 _holeFillRefine(sampler image, float maxDist) {\n  vec2 dc = destCoord();\n  vec4 sO = sample(image, samplerTransform(image, dc));\n  if (sO.r <= 1.000000e-03) return sO;\n  if (sO.r > 9.500000e-01) return vec4(sO.r, 1, 0, 1);\n  float R = sO.r * maxDist;\n  float dTheta = clamp(1.0 / (R + 2.200000e-01), 1.000000e-01, 7.500000e-01);\n  for (float t = 0.0; t < 3.141593e+00; t += dTheta) {\n    vec2 d = R * vec2(cos(t), sin(t));\n    vec4 s = sample(image, samplerTransform(image, dc + d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n    s = sample(image, samplerTransform(image, dc - d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n  }\n  return sO;\n}\n"
+ "Relased LRU"
+ "Released LRU for %!p(MISSING)"
- "kernel vec4 _holeFillRefine(sampler image, float maxDist) {\n  vec2 dc = destCoord();\n  vec4 sO = sample(image, samplerTransform(image, dc));\n  if (sO.r <= 1.000000e-03) return sO;\n  if (sO.r > 9.500000e-01) return vec4(sO.r, 1, 0, 1);\n  float R = sO.r * maxDist;\n  for (float t = 0.0; t < 3.141593e+00; t += 1.000000e-01) {\n    vec2 d = R * vec2(cos(t), sin(t));\n    vec4 s = sample(image, samplerTransform(image, dc + d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n    s = sample(image, samplerTransform(image, dc - d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n  }\n  return sO;\n}\n"

```
