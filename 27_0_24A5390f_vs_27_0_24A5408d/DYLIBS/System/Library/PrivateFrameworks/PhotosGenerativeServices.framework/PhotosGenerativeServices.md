## PhotosGenerativeServices

> `/System/Library/PrivateFrameworks/PhotosGenerativeServices.framework/PhotosGenerativeServices`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0xafcfc
-  __TEXT.__objc_methlist: 0x15ac
-  __TEXT.__const: 0x6a30
-  __TEXT.__constg_swiftt: 0x1f4c
-  __TEXT.__swift5_typeref: 0x1f94
-  __TEXT.__swift5_fieldmd: 0x236c
+912.0.111.0.0
+  __TEXT.__text: 0xafa88
+  __TEXT.__objc_methlist: 0x159c
+  __TEXT.__const: 0x6ad0
+  __TEXT.__constg_swiftt: 0x1f5c
+  __TEXT.__swift5_typeref: 0x1fd4
+  __TEXT.__swift5_fieldmd: 0x2374
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0x17fd
+  __TEXT.__swift5_reflstr: 0x17cd
   __TEXT.__swift5_assocty: 0x348
-  __TEXT.__swift5_capture: 0x710
+  __TEXT.__swift5_capture: 0x750
   __TEXT.__oslogstring: 0x516
-  __TEXT.__cstring: 0x70d4
+  __TEXT.__cstring: 0x6714
   __TEXT.__swift5_proto: 0x418
-  __TEXT.__swift5_types: 0x2b4
+  __TEXT.__swift5_types: 0x2bc
   __TEXT.__swift_as_entry: 0x150
   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift_as_cont: 0x310
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2da8
-  __TEXT.__eh_frame: 0x5e20
+  __TEXT.__unwind_info: 0x2db8
+  __TEXT.__eh_frame: 0x5e58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x140
-  __DATA_CONST.__objc_classlist: 0x158
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1038
+  __DATA_CONST.__objc_selrefs: 0x1060
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x5ba0
-  __AUTH_CONST.__objc_const: 0x37b0
-  __AUTH_CONST.__auth_got: 0x13a0
+  __AUTH_CONST.__const: 0x5cb8
+  __AUTH_CONST.__objc_const: 0x37e8
+  __AUTH_CONST.__auth_got: 0x13b8
   __AUTH.__objc_data: 0x5a0
-  __AUTH.__data: 0x88
-  __DATA.__data: 0x1850
+  __AUTH.__data: 0x120
+  __DATA.__data: 0x1810
   __DATA.__bss: 0x7e80
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0xad0
-  __DATA_DIRTY.__data: 0x1be0
+  __DATA_DIRTY.__objc_data: 0xa70
+  __DATA_DIRTY.__data: 0x1bd0
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4992
-  Symbols:   1859
-  CStrings:  565
+  Functions: 4981
+  Symbols:   1871
+  CStrings:  558
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NUOpaqueDescriptor
+ __DATA__TtC24PhotosGenerativeServices21PGSSafetyDebugCapture
+ __METACLASS_DATA__TtC24PhotosGenerativeServices21PGSSafetyDebugCapture
+ _objc_msgSend$attachmentExpressionForKey:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$valueForKey:
+ _symbolic _____ 24PhotosGenerativeServices20PGSBlockedGenerationV
+ _symbolic _____ 24PhotosGenerativeServices21PGSSafetyDebugCaptureC
+ _symbolic _____Ieghn_ 24PhotosGenerativeServices20PGSBlockedGenerationV
+ _symbolic _____ytIeghnr_ 24PhotosGenerativeServices20PGSBlockedGenerationV
+ _symbolic _____yy_____YbcSg_____G s13ManagedBufferCsRi__rlE 24PhotosGenerativeServices20PGSBlockedGenerationV So16os_unfair_lock_sV
+ _type_layout_string 24PhotosGenerativeServices20PGSBlockedGenerationV
- _objc_msgSend$number:
CStrings:
+ "_flexRangeProperties"
+ "dividePipeline:<flexRangeProperties"
+ "flexRangeProperties"
+ "kernel vec4 gainMapMultiply(__sample im, __sample gm, float f)\n{\n  float3 color = log2(1.0 + im.rgb);\n  float3 gain = log2(1.0 + gm.rgb);\n  float3 light = mix(gain, color, f);\n  light = exp2(light) - 1.0;\n  return vec4(light, 1.0);\n}"
+ "kernel vec4 lightMapDivide(__sample im, __sample lm, float2 a)\n{\n  float3 color = log2(1.0 + im.rgb);\n  float3 light = log2(1.0 + lm.rgb);\n  float3 glog2 = a.x * light + a.y * color;\n  float3 gain = exp2(glog2) - 1.0;\n  return vec4(gain, 1.0);\n}"
- "dividePipeline:<mixFactor"
- "dividePipeline:<preserveColor"
- "kernel vec4 gainMapMultiply(__sample im, __sample gm)\n{\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float luma = dot(im.rgb, weq);\n  float maxRGB = max(max(im.r, im.g), im.b);\n  luma = 0.5 * (luma + maxRGB);\n  float gain = gm.r;\n  const float e = 0.01;\n  luma = (1 - e) * luma + e;\n  gain = (1 - e) * gain + e;\n  float light = gain * luma;\n  return vec4(light, light, light, 1.0);\n}"
- "kernel vec4 gainMapMultiply(__sample im, __sample gm, float f)\n{\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float luma = dot(im.rgb, weq);\n  float maxRGB = max(max(im.r, im.g), im.b);\n  luma = 0.5 * (luma + maxRGB);\n  luma = log2(1.0 + luma);\n  float gain = log2(1.0 + gm.r);\n  float light = mix(gain, luma, f);\n  light = exp2(light) - 1.0;\n  return vec4(light, light, light, 1.0);\n}"
- "kernel vec4 gainMapMultiplyRGB(__sample im, __sample gm)\n{\n  const float e = 0.01;\n  float3 color = (1 - e) * im.rgb + e;\n  float3 gain = (1 - e) * gm.rgb + e;\n  float3 light = gain * color;\n  return vec4(light, 1.0);\n}"
- "kernel vec4 gainMapMultiplyRGB(__sample im, __sample gm, float f)\n{\n  float3 color = log2(1.0 + im.rgb);\n  float3 gain = log2(1.0 + gm.rgb);\n  float3 light = mix(gain, color, f);\n  light = exp2(light) - 1.0;\n  return vec4(light, 1.0);\n}"
- "kernel vec4 lightMapDivide(__sample im, __sample lm)\n{\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float luma = dot(im.rgb, weq);\n  float maxRGB = max(max(im.r, im.g), im.b);\n  luma = 0.5 * (luma + maxRGB);\n  float light = lm.r;\n  light = min(light, luma);\n  const float e = 0.01;\n  luma = (1.0 - e) * luma + e;\n  float gain = light/luma;\n  gain = (gain - e)/(1.0 - e);\n  return vec4(gain, gain, gain, 1.0);\n}"
- "kernel vec4 lightMapDivide(__sample im, __sample lm, float2 a)\n{\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float luma = dot(im.rgb, weq);\n  float maxRGB = max(max(im.r, im.g), im.b);\n  luma = 0.5 * (luma + maxRGB);\n  luma = log2(1.0 + luma);\n  float light = dot(lm.rgb, weq);\n  light = log2(1.0 +light);\n  float glog2 = a.x * light + a.y * luma;\n  float g = exp2(glog2) - 1.0;\n  return vec4(g, g, g, 1.0);\n}"
- "kernel vec4 lightMapDivideRGB(__sample im, __sample lm)\n{\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float iml = dot(im.rgb, weq);\n  float imx = max(max(im.r, im.g), im.b);\n  float luma = 0.5 * (iml + imx);\n  float lml = dot(lm.rgb, weq);\n  float lmx = max(max(lm.r, lm.g), lm.b);\n  float light = 0.5 * (lml + lmx);\n  light = min(light, luma);\n  const float e = 0.01;\n  luma = (1 - e) * luma + e;\n  float gain = light/luma;\n  gain = (gain - e)/(1 - e);\n  return vec4(gain, gain, gain, 1.0);\n}"
- "kernel vec4 lightMapDivideRGB(__sample im, __sample lm, float2 a)\n{\n  float3 color = log2(1.0 + im.rgb);\n  float3 light = log2(1.0 + lm.rgb);\n  float3 glog2 = a.x * light + a.y * color;\n  float3 gain = exp2(glog2) - 1.0;\n  const float3 weq = float3(1.0/3.0, 1.0/3.0, 1.0/3.0);\n  float g = dot(gain, weq);\n  return vec4(g, g, g, 1.0);\n}"
- "multiplyPipeline:<mixFactor"
- "multiplyPipeline:<preserveColor"
```
