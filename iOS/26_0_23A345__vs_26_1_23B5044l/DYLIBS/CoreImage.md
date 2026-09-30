## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1592.0.0.0.0
-  __TEXT.__text: 0x2d28c0
+1592.40.4.0.0
+  __TEXT.__text: 0x2d2ad4
   __TEXT.__auth_stubs: 0x2f10
   __TEXT.__objc_methlist: 0x14f80
-  __TEXT.__const: 0xbcb8
+  __TEXT.__const: 0xbc78
   __TEXT.__gcc_except_tab: 0x5eb0
-  __TEXT.__cstring: 0x89188
+  __TEXT.__cstring: 0x89198
   __TEXT.__oslogstring: 0xa5db
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__runtimeheader: 0xda3c

   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0x1490
   __AUTH_CONST.__auth_got: 0x17a0
-  __AUTH_CONST.__const: 0xd1b0
+  __AUTH_CONST.__const: 0xd2b8
   __AUTH_CONST.__cfstring: 0x1a000
   __AUTH_CONST.__objc_const: 0x2a5c8
   __AUTH_CONST.__objc_intobj: 0xd98

   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH.__objc_data: 0x9b50
-  __AUTH.__data: 0x1e010
+  __AUTH.__data: 0x1e840
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x1f18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 715E7603-B567-36CE-BDC4-2E7905CD2F93
-  Functions: 14019
-  Symbols:   43378
-  CStrings:  18050
+  UUID: EC9C0D82-0BA7-35D4-93D5-C29F0D9248E1
+  Functions: 14023
+  Symbols:   43386
+  CStrings:  18051
 
Symbols:
+ __ZN2CI8TileTask13addROIForNodeEPNS_11ProgramNodeE6CGRect
+ __ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFString6CGRect
+ __ZNK2CI14WarpKernelNode18can_sample_nearestEv
+ __ZNK2CI15ColorKernelNode18can_sample_nearestEv
+ __ZNK2CI17GeneralKernelNode18can_sample_nearestEv
+ __ZNK2CI4Node18can_sample_nearestEv
+ ____ZN2CI8TileTask13addROIForNodeEPNS_11ProgramNodeE6CGRect_block_invoke
+ ____ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFString6CGRect_block_invoke
+ ___block_descriptor_128_e8_32r40r48r56r64r72r80r88r96r_e99_v32?0r*8i16S20^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_40_e38_{Texture=(?={?=QQ}{?=II}{?=^v^v})}8?0l
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.232
+ ___block_descriptor_tmp.234
+ ___block_descriptor_tmp.236
+ ___block_descriptor_tmp.240
+ ___block_descriptor_tmp.262
+ ___block_descriptor_tmp.271
+ ___block_descriptor_tmp.274
+ ___block_descriptor_tmp.278
+ ___block_descriptor_tmp.282
+ ___block_literal_global.196
+ ___block_literal_global.207
+ ___block_literal_global.238
+ ___block_literal_global.242
- __ZN2CI8TileTask13addROIForNodeEPNS_11ProgramNodeERK6CGRect
- __ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFStringRK6CGRect
- ____ZN2CI8TileTask13addROIForNodeEPNS_11ProgramNodeERK6CGRect_block_invoke
- ____ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFStringRK6CGRect_block_invoke
- ___block_descriptor_120_e8_32r40r48r56r64r72r80r88r_e99_v32?0r*8i16S20^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8
- ___block_descriptor_40_e33_{Texture=(?=Q{?=II}{?=^v^v})}8?0l
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.197
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.202
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.233
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.239
- ___block_descriptor_tmp.248
- ___block_descriptor_tmp.261
- ___block_descriptor_tmp.270
- ___block_descriptor_tmp.273
- ___block_descriptor_tmp.277
- ___block_descriptor_tmp.280
- ___block_literal_global.195
- ___block_literal_global.237
- ___block_literal_global.241
CStrings:
+ "1592.40.4"
+ "float _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170834e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nfloat _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glow(sampler s, float radius, float bias_amount, vec4 color, float sdfScale, float sdfZero) {\n  vec2 dc = destCoord();\n  float distance = (sample(s, samplerCoord(s)).x - sdfZero) * sdfScale;\n  float distanceFraction = distance / radius;\n  float strength = exp(((-0.5) * distanceFraction) * distanceFraction);\n  strength /= max((bias_amount * (1.0 - strength)) + 1.0, 1e-4);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale / radius);\n  float mask = _saturate(0.5 + (distanceFraction / w));\n  color *= strength * mask;\n  return color;\n}\n"
+ "float _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170834e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _sdfFill(sampler s, float scale, float bias) {\n  vec2 dc = destCoord();\n  float sdf = sample(s, samplerCoord(s)).x;\n  float t = (sdf * scale) + bias;\n  float r = _computeSmoothedFWidthTransformed(s, dc, scale) * 0.5;\n  float c = smoothstep(-r, r, t);\n  return vec4(c, 0.0, 0.0, 1.0);\n}\n"
+ "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170834e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _glassHighlight(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec2 dc = destCoord();\n  vec3 sdf = sample(s, samplerCoord(s)).xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = _saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  mask *= _saturate(0.5 + (distance / w));\n  float alpha = _saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170834e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _simplifiedShapeAwareGradientMask(sampler s, float borderWidth, vec2 opacityBounds, vec2 contourOpacityBounds, float sdfScale, float sdfZero, vec4 bounds) {\n  vec2 dc = destCoord();\n  float distance = (-(sample(s, samplerCoord(s)).r - sdfZero)) * sdfScale;\n  float distanceFraction = _saturate(distance / borderWidth);\n  float verticalDistance = _saturate((dc.y - bounds.y) / bounds.w);\n  float verticalTransparency = mix(opacityBounds.y, opacityBounds.x, verticalDistance);\n  float verticalContourTransparency = mix(contourOpacityBounds.y, contourOpacityBounds.x, verticalDistance);\n  float transparencyWithContour = mix(verticalContourTransparency, verticalTransparency, distanceFraction);\n  transparencyWithContour = smoothstep(0.0, 1.0, transparencyWithContour);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + (distanceFraction / w));\n  transparencyWithContour = mix(1.0, transparencyWithContour, mask);\n  return vec4(transparencyWithContour);\n}\n"
+ "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170834e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nkernel vec4 _glassHighlightFromAlpha(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color, vec2 center) {\n  vec2 dc = destCoord();\n  vec4 sample_val = sample(s, samplerCoord(s));\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((sample_val.w - sdfZero) * sdfScale) - inset;\n  float d_norm = _saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  vec2 normal = normalize(dc - center);\n  bool fullBleed = inset == 0.0;\n  float w = _computeSmoothedFWidthCommon(s, dc, sdfScale, 3);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  if (!fullBleed) {\n    mask *= _saturate(0.5 + (distance / w));\n  }\n  float alpha = _saturate((dot(light_dir, normal) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max(float((bias_amount * (1.0 - alpha)) + 1.0), 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "inout"
+ "{Texture=(?={?=QQ}{?=II}{?=^v^v})}8@?0"
- "1592"
- "float _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170218e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nfloat _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glow(sampler s, float radius, float bias_amount, vec4 color, float sdfScale, float sdfZero) {\n  vec2 dc = destCoord();\n  float distance = (sample(s, samplerCoord(s)).x - sdfZero) * sdfScale;\n  float distanceFraction = distance / radius;\n  float strength = exp(((-0.5) * distanceFraction) * distanceFraction);\n  strength /= max((bias_amount * (1.0 - strength)) + 1.0, 1e-4);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale / radius);\n  float mask = _saturate(0.5 + (distanceFraction / w));\n  color *= strength * mask;\n  return color;\n}\n"
- "float _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170218e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _sdfFill(sampler s, float scale, float bias) {\n  vec2 dc = destCoord();\n  float sdf = sample(s, samplerCoord(s)).x;\n  float t = (sdf * scale) + bias;\n  float r = _computeSmoothedFWidthTransformed(s, dc, scale) * 0.5;\n  float c = smoothstep(-r, r, t);\n  return vec4(c, 0.0, 0.0, 1.0);\n}\n"
- "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170218e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _glassHighlight(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec2 dc = destCoord();\n  vec3 sdf = sample(s, samplerCoord(s)).xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = _saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  mask *= _saturate(0.5 + (distance / w));\n  float alpha = _saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
- "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170218e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nfloat _computeSmoothedFWidthTransformed(sampler s, vec2 dc, float scale) {\n  return _computeSmoothedFWidthCommon(s, dc, scale, 0);\n}\nkernel vec4 _simplifiedShapeAwareGradientMask(sampler s, float borderWidth, vec2 opacityBounds, vec2 contourOpacityBounds, float sdfScale, float sdfZero, vec4 bounds) {\n  vec2 dc = destCoord();\n  float distance = (-(sample(s, samplerCoord(s)).r - sdfZero)) * sdfScale;\n  float distanceFraction = _saturate(distance / borderWidth);\n  float verticalDistance = _saturate((dc.y - bounds.y) / bounds.w);\n  float verticalTransparency = mix(opacityBounds.y, opacityBounds.x, verticalDistance);\n  float verticalContourTransparency = mix(contourOpacityBounds.y, contourOpacityBounds.x, verticalDistance);\n  float transparencyWithContour = mix(verticalContourTransparency, verticalTransparency, distanceFraction);\n  transparencyWithContour = smoothstep(0.0, 1.0, transparencyWithContour);\n  float w = _computeSmoothedFWidthTransformed(s, dc, sdfScale);\n  float mask = _saturate(0.5 + (distanceFraction / w));\n  transparencyWithContour = mix(1.0, transparencyWithContour, mask);\n  return vec4(transparencyWithContour);\n}\n"
- "float _saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nfloat _computeSmoothedFWidthCommon(sampler s, vec2 dc, float scale, int channel) {\n  vec2 base_coord = samplerTransform(s, dc);\n  vec2 delta_x = samplerTransform(s, dc + vec2(1.0, 0.0)) - base_coord;\n  vec2 delta_y = samplerTransform(s, dc + vec2(0.0, 1.0)) - base_coord;\n  vec2 sample_offsets[41];\n  float sample_weights[41];\n  float smoothed_fwidth = 0.0;\n  for (int i = 0; i < 41; i++) {\n    vec2 offset = sample_offsets[i];\n    vec2 sample_coord = (base_coord + (offset.x * delta_x)) + (offset.y * delta_y);\n    vec4 left = sample(s, sample_coord - delta_x);\n    vec4 right = sample(s, sample_coord + delta_x);\n    vec4 down = sample(s, sample_coord - delta_y);\n    vec4 up = sample(s, sample_coord + delta_y);\n    float dfdx = (0.5 * scale) * (right[channel] - left[channel]);\n    float dfdy = (0.5 * scale) * (up[channel] - down[channel]);\n    float fwidth = abs(dfdx) + abs(dfdy);\n    smoothed_fwidth += fwidth * sample_weights[i];\n  }\n  smoothed_fwidth /= 3.170218e+00;\n  return (1.0 / 1.200) * clamp(smoothed_fwidth, 1e-4, 2.0);\n}\nkernel vec4 _glassHighlightFromAlpha(sampler s, vec4 values0, vec4 values1, float sdfZero, vec4 color, vec2 center) {\n  vec2 dc = destCoord();\n  vec4 sample_val = sample(s, samplerCoord(s));\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((sample_val.w - sdfZero) * sdfScale) - inset;\n  float d_norm = _saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  vec2 normal = normalize(dc - center);\n  bool fullBleed = inset == 0.0;\n  float w = _computeSmoothedFWidthCommon(s, dc, sdfScale, 3);\n  float mask = _saturate(0.5 + ((height - distance) / w));\n  if (!fullBleed) {\n    mask *= _saturate(0.5 + (distance / w));\n  }\n  float alpha = _saturate((dot(light_dir, normal) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max(float((bias_amount * (1.0 - alpha)) + 1.0), 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
- "{Texture=(?=Q{?=II}{?=^v^v})}8@?0"

```
