## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage`

```diff

-1663.0.0.0.0
-  __TEXT.__text: 0x3524dc
-  __TEXT.__objc_methlist: 0x16040
+1667.21.2.0.0
+  __TEXT.__text: 0x352aa4
+  __TEXT.__objc_methlist: 0x16050
   __TEXT.__const: 0xe268
-  __TEXT.__gcc_except_tab: 0xaa64
-  __TEXT.__cstring: 0x1059a1
+  __TEXT.__gcc_except_tab: 0xaa58
+  __TEXT.__cstring: 0x105a08
   __TEXT.__oslogstring: 0xb95c
   __TEXT.__dlopen_cstrs: 0x3fd
-  __TEXT.__runtimeheader: 0xda3c
+  __TEXT.__runtimeheader: 0x15aa4
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
   __TEXT.__cruft: 0x36d1
-  __TEXT.__unwind_info: 0xaab0
+  __TEXT.__unwind_info: 0xaab8
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9060
+  __DATA_CONST.__objc_selrefs: 0x9080
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1478
-  __DATA_CONST.__got: 0xb30
-  __AUTH_CONST.__const: 0x10410
+  __DATA_CONST.__got: 0xb38
+  __AUTH_CONST.__const: 0x10440
   __AUTH_CONST.__cfstring: 0x1de40
   __AUTH_CONST.__objc_const: 0x2bdb8
   __AUTH_CONST.__weak_auth_got: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15312
-  Symbols:   29326
-  CStrings:  9008
+  Functions: 15316
+  Symbols:   29336
+  CStrings:  9009
 
Symbols:
+ -[CIContext isUberShaderAvailable]
+ -[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]
+ GCC_except_table210
+ GCC_except_table218
+ GCC_except_table233
+ GCC_except_table240
+ GCC_except_table266
+ GCC_except_table281
+ GCC_except_table293
+ GCC_except_table300
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table317
+ GCC_except_table337
+ GCC_except_table340
+ _OBJC_CLASS_$_NSProgress
+ __ZNK2CI12MetalContext24is_uber_shader_availableEv
+ ___62-[CIRAWFilter downloadResourcesWithTimeout:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32o40b_e5_v8?0l
+ _objc_msgSend$progressWithTotalUnitCount:
+ _objc_msgSend$setCompletedUnitCount:
- GCC_except_table208
- GCC_except_table222
- GCC_except_table232
- GCC_except_table238
- GCC_except_table265
- GCC_except_table299
- GCC_except_table303
- GCC_except_table305
- GCC_except_table316
- GCC_except_table336
- GCC_except_table339
CStrings:
+ "1667.21.2"
+ "commandBuffer=%p "
+ "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec4 left = sample(s, base_coord - delta_x);\n  vec4 right = sample(s, base_coord + delta_x);\n  vec4 down = sample(s, base_coord - delta_y);\n  vec4 up = sample(s, base_coord + delta_y);\n  float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n  float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n  float fwidth = abs(dfdx) + abs(dfdy);\n  return (1.0 / 1.200) * clamp(fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _glassHighlight(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec2 dc = destCoord();\n  vec3 sdf = sample(s, samplerCoord(s)).xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = _saturate(distance / height);\n  float effectiveCurvature = curvature * smoothstep(1.0, 3.0, height);\n  float h = mix(1.0, 1.0 - d_norm, effectiveCurvature);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  mask *= _saturate(0.5 + (distance / w));\n  float alpha = h * _saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= mask * alpha;\n  return color;\n}\n"
- "1663"
- "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec4 left = sample(s, base_coord - delta_x);\n  vec4 right = sample(s, base_coord + delta_x);\n  vec4 down = sample(s, base_coord - delta_y);\n  vec4 up = sample(s, base_coord + delta_y);\n  float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n  float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n  float fwidth = abs(dfdx) + abs(dfdy);\n  return (1.0 / 1.200) * clamp(fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _glassHighlight(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec2 dc = destCoord();\n  vec3 sdf = sample(s, samplerCoord(s)).xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = _saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  mask *= _saturate(0.5 + (distance / w));\n  float alpha = h * _saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= mask * alpha;\n  return color;\n}\n"
```
