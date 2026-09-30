## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1574.0.0.122.2
-  __TEXT.__text: 0x2d1574
+1578.0.0.0.0
+  __TEXT.__text: 0x2d1884
   __TEXT.__auth_stubs: 0x2f10
-  __TEXT.__objc_methlist: 0x14f28
-  __TEXT.__const: 0xbdd8
+  __TEXT.__objc_methlist: 0x14f68
+  __TEXT.__const: 0xbb98
   __TEXT.__gcc_except_tab: 0x5eb8
-  __TEXT.__cstring: 0x87934
+  __TEXT.__cstring: 0x87962
   __TEXT.__oslogstring: 0xa531
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__runtimeheader: 0xda3c
   __TEXT.__cikl2metal_pre: 0x47f
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0x6e90
+  __TEXT.__unwind_info: 0x6b50
   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x2a59
-  __TEXT.__objc_methname: 0x203a2
+  __TEXT.__objc_methname: 0x204ad
   __TEXT.__objc_methtype: 0x66c9
-  __TEXT.__objc_stubs: 0x104c0
-  __DATA_CONST.__got: 0xa70
+  __TEXT.__objc_stubs: 0x104e0
+  __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x7500
   __DATA_CONST.__objc_classlist: 0x1038
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x88e8
+  __DATA_CONST.__objc_selrefs: 0x8910
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0x14a0
   __AUTH_CONST.__auth_got: 0x17a0
   __AUTH_CONST.__const: 0xd110
-  __AUTH_CONST.__cfstring: 0x19f40
-  __AUTH_CONST.__objc_const: 0x2a558
+  __AUTH_CONST.__cfstring: 0x19f80
+  __AUTH_CONST.__objc_const: 0x2a598
   __AUTH_CONST.__objc_intobj: 0xd98
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_doubleobj: 0x29b0

   __AUTH.__data: 0x1e110
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x1f10
+  __DATA.__objc_ivar: 0x1f14
   __DATA.__data: 0x57a0
   __DATA.__bss: 0x37c0
   __DATA.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E386D8A3-A537-33B0-B142-AD88FC2EDEC9
-  Functions: 14003
-  Symbols:   43333
-  CStrings:  18028
+  UUID: 3B1F67CD-3CE3-3488-AE2C-EDA7A6A1F287
+  Functions: 14008
+  Symbols:   43345
+  CStrings:  18041
 
Symbols:
+ -[CIRAWFilter isHighlightRecoveryEnabled]
+ -[CIRAWFilter isHighlightRecoverySupported]
+ -[CIRAWFilter setHighlightRecoveryEnabled:]
+ -[CIRAWFilterImpl(CustomAccessors) inputDisableHighlightRecovery]
+ -[CIRAWFilterImpl(CustomAccessors) setInputDisableHighlightRecovery:]
+ _OBJC_IVAR_$_CIRAWFilterImpl.inputDisableHighlightRecovery
+ _kCGColorSpaceExtendedLinearDisplayP3
+ _objc_msgSend$setInputDisableHighlightRecovery:
- __ZZ18linearP3ColorSpaceE4data
CStrings:
+ "1578"
+ "TB,GisHighlightRecoveryEnabled"
+ "TB,R,GisHighlightRecoverySupported"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlight(vec4 s, vec4 fwidth, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec3 sdf = s.xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = (1.0 / 1.200) * max(fwidth.x, 1e-4);\n  float mask = saturate(0.5 + ((height - distance) / w));\n  mask *= saturate(0.5 + (distance / w));\n  float alpha = saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlightFromAlpha(vec4 s, vec4 dfdxW, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((s.w - sdfZero) * sdfScale) - inset;\n  float d_norm = max(0.0, min(1.0, distance / height));\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float horiz = dfdxW.x;\n  float vert = dfdxW.y;\n  vec2 normal = vec2(horiz, vert);\n  normal /= length(normal);\n  normal *= -1.0;\n  float fwidth = abs(horiz) + abs(vert);\n  float w = (1.0 / 1.200) * max(fwidth, 1e-4);\n  float mask = saturate(0.5 + ((height - distance) / w));\n  if (inset != 0.0) {\n    mask *= saturate(0.5 + (distance / w));\n  }\n  float alpha = saturate((dot(light_dir, normal) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max(float((bias_amount * (1.0 - alpha)) + 1.0), 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "highlightRecoveryEnabled"
+ "highlightRecoverySupported"
+ "inputDisableHighlightRecovery"
+ "inputShouldRecoverHighlights"
+ "isHighlightRecoveryEnabled"
+ "isHighlightRecoverySupported"
+ "kernel vec4 _clampToFrame(sampler s, vec4 frame) {\n  vec2 p = clamp(destCoord(), frame.xy, frame.xy + frame.zw);\n  return sample(s, samplerTransform(s, p));\n}\n"
+ "setHighlightRecoveryEnabled:"
+ "setInputDisableHighlightRecovery:"
- "1574.0.0.122.2"
- "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlight(vec4 s, vec4 fwidth, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec3 sdf = s.xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = max(fwidth.x, 1e-4);\n  float mask = saturate(0.5 + (distance / w));\n  mask *= saturate(0.5 + ((height - distance) / w));\n  if (distance < (-1.0)) mask = 0.0;\n  float alpha = saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
- "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlightFromAlpha(vec4 s, vec4 dfdxW, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((s.w - sdfZero) * sdfScale) - inset;\n  float d_norm = max(0.0, min(1.0, distance / height));\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float horiz = dfdxW.x;\n  float vert = dfdxW.y;\n  vec2 normal = vec2(horiz, vert);\n  normal /= length(normal);\n  normal *= -1.0;\n  float fwidth = abs(horiz) + abs(vert);\n  float w = max(fwidth, 1e-4);\n  float mask = saturate(0.5 + (distance / w));\n  mask *= saturate(0.5 + ((height - distance) / w));\n  if (distance < (-1.0)) mask = 0.0;\n  float alpha = saturate((dot(light_dir, normal) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max(float((bias_amount * (1.0 - alpha)) + 1.0), 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
- "kernel vec4 _clampToFrame(sampler s, vec4 frame) {\n  vec2 p = clamp(destCoord(), frame.xy, frame.zw);\n  return sample(s, samplerTransform(s, p));\n}\n"

```
