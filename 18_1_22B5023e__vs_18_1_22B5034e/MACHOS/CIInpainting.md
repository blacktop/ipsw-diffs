## CIInpainting

> `/System/Library/CoreImage/CIInpainting.cifilter/CIInpainting`

```diff

-1500.91.0.0.0
-  __TEXT.__text: 0xc874
+1510.5.0.0.0
+  __TEXT.__text: 0xa13c
   __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x440
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x18f4
-  __TEXT.__cstring: 0x17e5
-  __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methname: 0x135c
-  __TEXT.__objc_methtype: 0x2cb
-  __TEXT.__oslogstring: 0x366
+  __TEXT.__objc_stubs: 0x1160
+  __TEXT.__objc_methlist: 0x3f0
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x13a4
+  __TEXT.__cstring: 0x17dd
+  __TEXT.__objc_classname: 0x40
+  __TEXT.__objc_methname: 0x118c
+  __TEXT.__objc_methtype: 0x234
+  __TEXT.__oslogstring: 0x4bb
   __TEXT.__dlopen_cstrs: 0x91
   __TEXT.__inpbpm: 0x944
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x3d8
   __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x270
-  __DATA_CONST.__cfstring: 0xcc0
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__cfstring: 0xb80
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x678
-  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_const: 0x5d8
+  __DATA.__objc_selrefs: 0x5a8
   __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x140
-  __DATA.__bss: 0xe0
+  __DATA.__objc_data: 0xf0
+  __DATA.__bss: 0x100
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 160
-  Symbols:   164
-  CStrings:  445
+  Functions: 157
+  Symbols:   160
+  CStrings:  404
 
Symbols:
+ _objc_retain_x25
- _kCIFormatRh
- _kCIKernelOutputFormat
- _OBJC_CLASS_$_NSMutableArray
- _objc_retain_x24
- _OBJC_CLASS_$_NSMutableDictionary
CStrings:
+ "kernel vec4 CIIP_orMasks (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(1.0 - clamp(1.0-a.x,0.0,1.0) * clamp(1.0-b.x,0.0,1.0), 0.0, 0.0, 1.0); }"
+ "kernel vec4 CIIP_invertMaskR (__sample s) __attribute__((outputFormat(kCIFormatRh))) { return vec4(1.0-s.x,0,0,1);; }"
+ "mlmodelc"
+ "%!{(MISSING)public}@: using model \"%!{(MISSING)public}@\" at path: %!{(MISSING)public}@."
+ "fileURLWithPath:isDirectory:"
+ "%!{(MISSING)public}@: could not load the default inpaint model.\n"
+ "kernel vec4 CIIP_add (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(a.r - b.r, 0.0, 0.0, 1.0); }"
+ "kernel vec4 CIIP_threshNegInf (__sample s) __attribute__((outputFormat(kCIFormatRh))) { float negInf = -1.0E20; float v = (s.r>0.01) ? negInf : 0.0; return vec4(v,0,0,1); }"
+ "kernel vec4 CIIP_post (__sample s) __attribute__((preserves_opacity)) { return vec4((s.rgb+1.0)/2.0,s.a); }"
+ "kernel vec4 CIIP_rgb_neg1pos1_to_01 (__sample s) __attribute__((preserves_opacity)) { s.rgb = (s.rgb + 1.0) / 2.0; s.rgb = clamp(s.rgb, 0.0, 1.0); return s; }"
+ "refinementModelPath"
+ "CIInpaintRepair"
+ "CIInpaintRefine"
+ "URLForResource:withExtension:"
+ "_logName"
+ "kernel vec4 CIIP_add (__sample a, __sample b) __attribute__((preserves_opacity)) { return vec4(a.rgb + b.rgb, a.a); }"
+ "kernel vec4 CIIP_addR (__sample a, __sample b) __attribute__((preserves_opacity)) { return vec4(a.r + b.r, a.gb, a.a); }"
+ "kernel vec4 CIIP_redOnly (__sample s) __attribute__((outputFormat(kCIFormatRh))) { return vec4(s.r,0,0,1); }"
+ "kernel vec4 interleavedToPlanar(sampler s, float tileSize) __attribute__((outputFormat(kCIFormatRh))) \n { \n vec2 dc = destCoord(); \n float y = dc.y; \n y = (y<tileSize) ? y : \n (y<tileSize*2.0) ? (y - tileSize) : \n (y - 2.0*tileSize); \n vec4 c = sample(s, samplerTransform(s, vec2(dc.x, y))); \n if (dc.y < tileSize) \n return vec4(c.x, 0.0, 0.0, 1.0); \n if (dc.y < tileSize*2.0) \n return vec4(c.y, 0.0, 0.0, 1.0); \n return vec4(c.z, 0.0, 0.0, 1.0); \n }"
+ "kernel vec4 CIIP_rgb_01_to_neg1pos1 (__sample s) __attribute__((preserves_opacity)) { s.rgb = clamp(s.rgb, 0.0, 1.0); s.rgb = s.rgb * 2.0 -1.0; return s; }"
+ "deep_transfer"
+ "%!{(MISSING)public}@: could not load the default refinement model.\n"
+ "kernel vec4 CIIP_andMasks (__sample a, __sample b) __attribute__((outputFormat(kCIFormatRh))) { return vec4(clamp(a.x,0.0,1.0) * clamp(b.x,0.0,1.0), 0.0, 0.0, 1.0); }"
+ "%!{(MISSING)public}@: The inpaint.mlmodelc is no longer part of the filter bundle. It needs to be passed to the filter using the inputModel argument.\n"
+ "%!{(MISSING)public}@: The deep_transfer.mlmodelc is no longer part of the filter bundle. It needs to be passed to the filter using the inputRefinementModel argument.\n"
+ "inpaintModelPath"
- "tileSize"
- "+[TiledInpaint processWithInputs:arguments:output:error:]"
- "originX"
- "Progressive, "
- "unsignedLongValue"
- "kernel vec4 interleavedToPlanar(sampler s, float tileSize) \n { \n vec2 dc = destCoord(); \n float y = dc.y; \n y = (y<tileSize) ? y : \n (y<tileSize*2.0) ? (y - tileSize) : \n (y - 2.0*tileSize); \n vec4 c = sample(s, samplerTransform(s, vec2(dc.x, y))); \n if (dc.y < tileSize) \n return vec4(c.x, 0.0, 0.0, 1.0); \n if (dc.y < tileSize*2.0) \n return vec4(c.y, 0.0, 0.0, 1.0); \n return vec4(c.z, 0.0, 0.0, 1.0); \n }"
- "longValue"
- "addObject:"
- "maskRegion.size.width == tileSize"
- "countX"
- "innerContext"
- "version"
- "%!@(MISSING)_outcombined_scale%!d(MISSING).png"
- "countY"
- "startTaskToClear:error:"
- "(%!z(MISSING)u x %!z(MISSING)u) = %!z(MISSING)u   (%!z(MISSING)u x %!z(MISSING)u)  (%!f(MISSING))\n"
- "roiTileCount"
- "apply:mask:area:countX:countY:tileSize:tileStride:tileScale:colorSpace:orientation:hint:version:method:dumpImageIndex:"
- "kernel vec4 CIIP_redOnly (__sample s) { return vec4(s.r,0,0,1); }"
- "maskRegion.size.height == tileSize"
- "kernel vec4 CIIP_orMasks (__sample a, __sample b) { return vec4(1.0 - clamp(1.0-a.x,0.0,1.0) * clamp(1.0-b.x,0.0,1.0), 0.0, 0.0, 1.0); }"
- "kernel vec4 CIIP_andMasks (__sample a, __sample b) { return vec4(clamp(a.x,0.0,1.0) * clamp(b.x,0.0,1.0), 0.0, 0.0, 1.0); }"
- "dictionary"
- "%!@(MISSING)_dst_scale%!d(MISSING).png"
- "array"
- "defaultTileProgressive"
- "srcImg"
- "CIInpaintFilter.inputTileProgressive"
- "tileScale"
- "cs"
- "waitUntilCompletedAndReturnError:"
- "%!{(MISSING)public}@: CIInpaintModel.inputMultipass default set to %!d(MISSING)."
- "applyWithExtent:roiCallback:arguments:options:"
- "dstFull"
- "workingColorSpace"
- "kernel vec4 CIIP_add (__sample a, __sample b) { return vec4(a.rgb + b.rgb, a.a); }"
- "kernel vec4 CIIP_rgb_neg1pos1_to_01 (__sample s) { s.rgb = (s.rgb + 1.0) / 2.0; s.rgb = clamp(s.rgb, 0.0, 1.0); return s; }"
- "method"
- "%!{(MISSING)public}@: CIInpaintModel.inputTileProgressive default set to %!d(MISSING)."
- "numberWithUnsignedLong:"
- "roiTileIndex"
- "kernel vec4 CIIP_rgb_01_to_neg1pos1 (__sample s) { s.rgb = clamp(s.rgb, 0.0, 1.0); s.rgb = s.rgb * 2.0 -1.0; return s; }"
- "kernel vec4 CIIP_addR (__sample a, __sample b) { return vec4(a.r + b.r, a.gb, a.a); }"
- "orientation"
- "originY"
- "inRegion.size.height == tileSize"
- "kernel vec4 CIIP_add (__sample a, __sample b) { return vec4(a.r - b.r, 0.0, 0.0, 1.0); }"
- "defaultMultipass"
- "tileStride"
- "hint"
- "%!l(MISSING)dx%!l(MISSING)d Tiles, %!s(MISSING)Scale %!f(MISSING)"
- "setObject:forKeyedSubscript:"
- "v20@?0i8i12i16"
- "kernel vec4 CIIP_post (__sample s) { return vec4((s.rgb+1.0)/2.0,s.a); }"
- "inRegion.size.width == tileSize"
- "kernel vec4 CIIP_invertMaskR (__sample s) { return vec4(1.0-s.x,0,0,1);; }"
- "dumpImageIndex"
- "@136@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32Q64Q72Q80Q88d96^{CGColorSpace=}104i112@116i124i128i132"
- "@60@0:8i16@20{CGRect={CGPoint=dd}{CGSize=dd}}28"
- "(1 x 1) = 1   (%!z(MISSING)u x %!z(MISSING)u)  (%!f(MISSING))\n"
- "applyWithExtent:arguments:options:"
- "kernel vec4 CIIP_threshNegInf (__sample s) { float negInf = -1.0E20; float v = (s.r>0.01) ? negInf : 0.0; return vec4(v,0,0,1); }"
- "CIInpaintFilter.inputMultipass"
- "mskImg"
- "TiledInpaint"
- "imageWithIOSurface:options:"
- "roiTileArrayForInput:arguments:outputRect:"

```
