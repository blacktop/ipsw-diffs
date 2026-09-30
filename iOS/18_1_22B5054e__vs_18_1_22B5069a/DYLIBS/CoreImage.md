## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1510.11.0.0.0
-  __TEXT.__text: 0x2c1f64
+1510.14.0.0.0
+  __TEXT.__text: 0x2c1e84
   __TEXT.__auth_stubs: 0x2f90
   __TEXT.__objc_methlist: 0x14d48
-  __TEXT.__const: 0xe538
+  __TEXT.__const: 0xe548
   __TEXT.__gcc_except_tab: 0x5918
-  __TEXT.__cstring: 0x84c67
+  __TEXT.__cstring: 0x84c44
   __TEXT.__oslogstring: 0x9d73
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__runtimeheader: 0xb8ec

   __DATA_CONST.__objc_arraydata: 0x1400
   __AUTH_CONST.__auth_got: 0x17e0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0xbb60
+  __AUTH_CONST.__const: 0xbb40
   __AUTH_CONST.__cfstring: 0x196c0
   __AUTH_CONST.__objc_const: 0x2c030
   __AUTH_CONST.__objc_doubleobj: 0x2940

   __AUTH_CONST.__objc_floatobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH.__objc_data: 0x99c0
-  __AUTH.__data: 0x1dfc8
+  __AUTH.__data: 0x1dfd8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x20a0
-  __DATA.__data: 0x57d8
+  __DATA.__data: 0x57e0
   __DATA.__bss: 0x3a38
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13818
-  Symbols:   15764
+  Functions: 13816
+  Symbols:   15762
   CStrings:  14907
 
CStrings:
+ "kernel vec4 _lumaMap(vec4 pixel, sampler2D table, vec2 normalizer) {\n  float luma = dot(pixel, vec4(0.299, 0.587, 0.114, 0.0));\n  vec4 result = texture2D(table, vec2((normalizer.x * luma) + normalizer.y, 0.5));\n  result.a = pixel.a;\n  return result;\n}\n"
- "kernel vec4 _lumaMap(vec4 pixel, sampler table) {\n  float luma = dot(pixel, vec4(0.299, 0.587, 0.114, 0.0));\n  float lumaCoord = (clamp(luma, 0.0, 1.0) * 255.0) + 0.5;\n  vec4 result = sample(table, samplerTransform(table, vec2(lumaCoord, 0.5)));\n  result.a = pixel.a;\n  return result;\n}\n"

```
