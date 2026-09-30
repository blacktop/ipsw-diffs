## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1510.5.0.0.0
-  __TEXT.__text: 0x2bf338
-  __TEXT.__auth_stubs: 0x2f60
-  __TEXT.__objc_methlist: 0x14bc8
-  __TEXT.__gcc_except_tab: 0x591c
-  __TEXT.__const: 0xe418
-  __TEXT.__cstring: 0x83fa6
-  __TEXT.__oslogstring: 0x9ccd
+1510.7.0.0.0
+  __TEXT.__text: 0x2c18e8
+  __TEXT.__auth_stubs: 0x2f70
+  __TEXT.__objc_methlist: 0x14d48
+  __TEXT.__const: 0xe548
+  __TEXT.__gcc_except_tab: 0x58f0
+  __TEXT.__cstring: 0x84c1f
+  __TEXT.__oslogstring: 0x9d53
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__runtimeheader: 0xb8ec
   __TEXT.__cikl2metal_pre: 0x47f
-  __TEXT.__unwind_info: 0x6cc8
+  __TEXT.__unwind_info: 0x6d10
   __TEXT.__eh_frame: 0x208
-  __TEXT.__objc_classname: 0x299b
-  __TEXT.__objc_methname: 0x21496
+  __TEXT.__objc_classname: 0x29e3
+  __TEXT.__objc_methname: 0x2165a
   __TEXT.__objc_methtype: 0x6bdc
-  __TEXT.__objc_stubs: 0x12060
+  __TEXT.__objc_stubs: 0x12080
   __DATA_CONST.__got: 0xa18
-  __DATA_CONST.__const: 0x6b28
-  __DATA_CONST.__objc_classlist: 0xff8
+  __DATA_CONST.__const: 0x6b88
+  __DATA_CONST.__objc_classlist: 0x1010
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8cc0
+  __DATA_CONST.__objc_selrefs: 0x8d18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x368
-  __DATA_CONST.__objc_arraydata: 0x13f8
-  __AUTH_CONST.__auth_got: 0x17c8
+  __DATA_CONST.__objc_arraydata: 0x1400
+  __AUTH_CONST.__auth_got: 0x17d0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0xbb20
-  __AUTH_CONST.__cfstring: 0x194e0
-  __AUTH_CONST.__objc_const: 0x2bca0
-  __AUTH_CONST.__objc_doubleobj: 0x28b0
+  __AUTH_CONST.__const: 0xbb60
+  __AUTH_CONST.__cfstring: 0x196c0
+  __AUTH_CONST.__objc_const: 0x2c030
+  __AUTH_CONST.__objc_doubleobj: 0x2940
   __AUTH_CONST.__objc_intobj: 0xd38
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_floatobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH.__objc_data: 0x98d0
-  __AUTH.__data: 0x1db98
+  __AUTH.__objc_data: 0x99c0
+  __AUTH.__data: 0x1dfc8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x207c
-  __DATA.__data: 0x5758
+  __DATA.__objc_ivar: 0x20a0
+  __DATA.__data: 0x57d8
   __DATA.__bss: 0x3a50
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13764
-  Symbols:   15705
-  CStrings:  14854
+  Functions: 13816
+  Symbols:   15760
+  CStrings:  14905
 
Symbols:
+ _kCIFormatRG10packed
+ _atanf
+ _kCIFormatR10packed
CStrings:
+ "stride"
+ "appex"
+ "convert_r10p_to_rh"
+ " executionTime=%!d(MISSING)ms"
+ "pre"
+ "setInputMaximumDistance:"
+ "Bitmap write error: Accessing corrupted bitmap size: (%!z(MISSING)u,%!z(MISSING)u)"
+ "%!{(MISSING)public}@: inputImage must be an image with finite extent."
+ "vec2 _uv_to_dc(vec2 uv, vec4 ext) {\n  return (uv * ext.zw) + ext.xy;\n}\nkernel vec4 _distanceMaskPost(vec4 image, vec4 pre, vec4 ext, float maxDist) {\n  const float nan = 1.0 / 0.0;\n  if ((image.x == nan) || (image.y == nan)) return vec4(1.0, 0.0, 0.0, 1.0);\n  vec2 dc = destCoord();\n  vec2 sc = _uv_to_dc(image.xy, ext);\n  float dist = distance(sc, dc) / maxDist;\n  dist = clamp(dist, 0.0, 1.0);\n  if (pre.r > 0.5) dist = 0.0;\n  return vec4(dist, 0.0, 0.0, 1.0);\n}\n"
+ "setInputMaximumHoleSize:"
+ "CIAreaHoughTransform"
+ "CIFillHolesInRedMask"
+ "T@\"NSNumber\",&,N,VinputGradientMin"
+ "convert_rg10p_to_rgh"
+ "ext"
+ "T@\"NSNumber\",&,N,VinputRefinementPassCount"
+ "Bitmap write error: Writing to point (%!d(MISSING),%!d(MISSING)) out of bounds (%!z(MISSING)ux%!z(MISSING)u)"
+ "CIAreaHoughTransform area width or height is greater than 4096."
+ "computeHoughHistogram"
+ " compileWait=%!f(MISSING)ms"
+ " time=%!f(MISSING)ms"
+ "inputMaximumDistance"
+ "inputGradientMin"
+ "kernel vec4 _prepHoughTransform(vec4 s, float destDiag, float gradMin, float gradMax) {\n  float pi = 3.141593e+00;\n  vec2 dc = destCoord();\n  float sLen = length(s.xy);\n  if (sLen < gradMin) return vec4(0.0);\n  sLen = (sLen - gradMin) / (gradMax - gradMin);\n  sLen = clamp(sLen, 0.0, 1.0);\n  float theta = atan(s.x / (-s.y));\n  float thetaNorm = (((theta / pi) + 0.5) * 1.800000e+02) / 255.0;\n  float rho = abs((dc.y * cos(theta)) - (dc.x * sin(theta)));\n  float rhoNorm = rho / destDiag;\n  return vec4(rhoNorm, thetaNorm, sLen, 1.0);\n}\n"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "%!{(MISSING)public}@: inputMaximumHoleSize must be in the range 1...500."
+ "convertHoughHistogram"
+ "setInputGradientMin:"
+ "T@\"NSNumber\",&,N,VinputMaximumHoleSize"
+ "setInputRefinementPassCount:"
+ "setInputGradientMax:"
+ "destDiag"
+ "vec2 _dc_to_uv(vec2 dc, vec4 ext) {\n  return (dc - ext.xy) / ext.zw;\n}\nfloat _uv_distance(vec2 uv1, vec2 uv2, vec4 ext) {\n  vec2 dc1 = (uv1 * ext.zw) + ext.xy;\n  vec2 dc2 = (uv2 * ext.zw) + ext.xy;\n  return distance(dc1, dc2);\n}\nkernel vec4 _distanceMask(sampler image, vec4 ext, float stride) {\n  float minDist = 1.000000e+09;\n  const float nan = 1.0 / 0.0;\n  vec4 result = vec4(nan, nan, 0.0, 1.0);\n  vec2 dc = destCoord();\n  vec2 uv = _dc_to_uv(dc, ext);\n  for (int i = -1; i <= 1; i++) {\n    for (int j = -1; j <= 1; j++) {\n      vec2 off = vec2(i, j) * stride;\n      vec4 s = sample(image, samplerTransform(image, dc + off));\n      if (s.r == nan) continue;\n      float dist = _uv_distance(s.xy, uv, ext);\n      if (dist < minDist) {\n        result = s;\n        minDist = dist;\n      }\n    }\n  }\n  return result;\n}\n"
+ "T@\"NSNumber\",&,N,VinputGradientMax"
+ " compileTime=%!f(MISSING)ms"
+ "gradMin"
+ "vec2 _dc_to_uv(vec2 dc, vec4 ext) {\n  return (dc - ext.xy) / ext.zw;\n}\nkernel vec4 _distanceMaskPrep(vec4 image, vec4 ext) {\n  const float nan = 1.0 / 0.0;\n  vec2 uv = _dc_to_uv(destCoord(), ext);\n  if (image.r <= 0.5) uv = vec2(nan, nan);\n  return vec4(uv, 0.0, 1.0);\n}\n"
+ "T@\"NSNumber\",&,N,VinputMaximumDistance"
+ "kernel vec4 _holeFillPost(vec4 image) {\n  float r = (image.g > 0.5) ? 0.0 : 1.0;\n  return vec4(r, 0.0, 0.0, 1.0);\n}\n"
+ "inputMaximumHoleSize"
+ "%!@(MISSING)_%!@(MISSING)"
+ "gradMax"
+ "%!{(MISSING)public}@: inputMaximumDistance must be in the range 1...1000."
+ "CIAreaHoughTransformMetal"
+ "kernel vec4 _holeFillRefine(sampler image, float maxDist) {\n  vec2 dc = destCoord();\n  vec4 sO = sample(image, samplerTransform(image, dc));\n  if (sO.r <= 1.000000e-03) return sO;\n  if (sO.r > 9.500000e-01) return vec4(sO.r, 1, 0, 1);\n  float R = sO.r * maxDist;\n  for (float t = 0.0; t < 3.141593e+00; t += 1.000000e-01) {\n    vec2 d = R * vec2(cos(t), sin(t));\n    vec4 s = sample(image, samplerTransform(image, dc + d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n    s = sample(image, samplerTransform(image, dc - d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n  }\n  return sO;\n}\n"
+ " area=%!f(MISSING)MP"
+ "inputRefinementPassCount"
+ "CIDistanceGradientFromRedMask"
+ " fill=%!f(MISSING)ms"
+ "inputGradientMax"
+ "maxDist"
- "Bitmap write error: Accessing out of bound p:(%!{(MISSING)public}d , %!{(MISSING)public}d) size:(%!{(MISSING)public}zu , %!{(MISSING)public}zu)"
- "Bitmap write error: Accessing corrupted bitmap size: (%!{(MISSING)public}zu , %!{(MISSING)public}zu)"
- " compileWaitTime= %!f(MISSING)"
- " kernelCompileTime= %!f(MISSING)"
- " megapixels=%!f(MISSING)"
- " kernelExecutionTime=%!d(MISSING)ms"
- " ms=%!f(MISSING)"

```
