## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-1660.0.0.0.0
-  __TEXT.__text: 0x3479d4
-  __TEXT.__objc_methlist: 0x15940
-  __TEXT.__const: 0xe128
-  __TEXT.__gcc_except_tab: 0xa7ec
-  __TEXT.__cstring: 0x103fd9
-  __TEXT.__oslogstring: 0xae6f
+1663.0.0.0.0
+  __TEXT.__text: 0x34919c
+  __TEXT.__objc_methlist: 0x15978
+  __TEXT.__const: 0xe198
+  __TEXT.__gcc_except_tab: 0xa868
+  __TEXT.__cstring: 0x104941
+  __TEXT.__oslogstring: 0xb283
   __TEXT.__dlopen_cstrs: 0x3fd
   __TEXT.__runtimeheader: 0xda3c
   __TEXT.__cikl2metal_pre: 0x54b
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0xa898
+  __TEXT.__unwind_info: 0xa8b0
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x1488
-  __DATA_CONST.__got: 0xae8
+  __DATA_CONST.__got: 0xaf0
   __AUTH_CONST.__const: 0xde40
-  __AUTH_CONST.__cfstring: 0x1d620
+  __AUTH_CONST.__cfstring: 0x1dba0
   __AUTH_CONST.__objc_const: 0x2b488
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xdc8

   __AUTH_CONST.__objc_doubleobj: 0x2a40
   __AUTH_CONST.__objc_floatobj: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__auth_got: 0x1848
+  __AUTH_CONST.__auth_got: 0x1858
   __AUTH.__objc_data: 0x9dd0
-  __AUTH.__data: 0x277f0
+  __AUTH.__data: 0x278a0
   __DATA.__objc_ivar: 0x1fc0
-  __DATA.__data: 0x6760
+  __DATA.__data: 0x67a8
   __DATA.__bss: 0x3ae8
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15148
-  Symbols:   28529
-  CStrings:  8820
+  Functions: 15161
+  Symbols:   28577
+  CStrings:  8880
 
Symbols:
+ -[CIFilter isEqual:]
+ -[CIImage imageByInsertingTiledIntermediateWithTileWidth:tileHeight:]
+ -[CIRAWFilter debugDescription]
+ -[CIRAWFilter hash]
+ -[CIRAWFilter isEqual:]
+ GCC_except_table144
+ GCC_except_table240
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table254
+ GCC_except_table261
+ GCC_except_table271
+ GCC_except_table288
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table337
+ GCC_except_table345
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table419
+ GCC_except_table439
+ _CFHash
+ _CGColorSpaceContainsHeadroomAdaptiveGainCurve
+ __ZN2CI25colormatch_builtinKernels71arg_name_im_headrooms_flag5_coefs_coefs3_lookupTableScale_lut_dim_rangeE
+ __ZN2CI25colormatch_builtinKernelsL82arg_type_Sample_Float2_Float_Float3_Float3_Float_Sampler2D_Float2_Float2_DestCoordE
+ __ZN2CI28sw_headroomAdaptiveGainCurveERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CIL17recurseGraphStatsEPNS_4NodeES1_iRNSt3__16vectorIPKS0_NS2_9allocatorIS5_EEEEPNS2_3mapIS5_NS_13useCountDepthENS2_4lessIS5_EENS6_INS2_4pairIKS5_SB_EEEEEE
+ __ZN2CIL21programNodeMemoryLoadEPKNS_11ProgramNodeERK6CGRectS5_mmbRb
+ __ZN2CIL26_headroomAdaptiveGainCurveE
+ __ZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERm
+ __ZN2CIL31_headroomAdaptiveGainCurve_nameE
+ __ZNSt3__16vectorIZN2CIL32make_program_graph_if_renderableEPNS1_7ContextEPKcNS1_14GraphWithDepthERK6CGRectRKNS1_19output_swizzle_infoEPcmE10TileToTestNS_9allocatorISE_EEE20__throw_length_errorB9fqn220106Ev
+ __ZZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEERmEN13SignpostTimerD1Ev
+ __ZZNSt3__16vectorIZN2CIL32make_program_graph_if_renderableEPNS1_7ContextEPKcNS1_14GraphWithDepthERK6CGRectRKNS1_19output_swizzle_infoEPcmE10TileToTestNS_9allocatorISE_EEE12emplace_backIJSE_EEERSE_DpOT_ENKUlvE0_clEv
+ ___69-[CIImage imageByInsertingTiledIntermediateWithTileWidth:tileHeight:]_block_invoke
+ ____ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb_block_invoke_2
+ _kCGUseLegacyHDREcosystem
+ _objc_msgSend$baselineExposure
+ _objc_msgSend$boostAmount
+ _objc_msgSend$boostShadowAmount
+ _objc_msgSend$colorNoiseReductionAmount
+ _objc_msgSend$contrastAmount
+ _objc_msgSend$decoderVersion
+ _objc_msgSend$despeckleAmount
+ _objc_msgSend$detailAmount
+ _objc_msgSend$exposure
+ _objc_msgSend$extendedDynamicRangeAmount
+ _objc_msgSend$imageByInsertingTiledIntermediateWithTileWidth:tileHeight:
+ _objc_msgSend$isColorNoiseReductionSupported
+ _objc_msgSend$isContrastSupported
+ _objc_msgSend$isDespeckleSupported
+ _objc_msgSend$isDetailSupported
+ _objc_msgSend$isDraftModeEnabled
+ _objc_msgSend$isGamutMappingEnabled
+ _objc_msgSend$isHighlightRecoveryEnabled
+ _objc_msgSend$isHighlightRecoverySupported
+ _objc_msgSend$isLensCorrectionEnabled
+ _objc_msgSend$isLensCorrectionSupported
+ _objc_msgSend$isLocalToneMapSupported
+ _objc_msgSend$isLuminanceNoiseReductionSupported
+ _objc_msgSend$isMoireReductionSupported
+ _objc_msgSend$isSharpnessSupported
+ _objc_msgSend$linearSpaceFilter
+ _objc_msgSend$localToneMapAmount
+ _objc_msgSend$luminanceNoiseReductionAmount
+ _objc_msgSend$moireReductionAmount
+ _objc_msgSend$nativeSize
+ _objc_msgSend$neutralChromaticity
+ _objc_msgSend$neutralLocation
+ _objc_msgSend$neutralTemperature
+ _objc_msgSend$neutralTint
+ _objc_msgSend$orientation
+ _objc_msgSend$scaleFactor
+ _objc_msgSend$shadowBias
+ _objc_msgSend$sharpnessAmount
- -[CIImage imageByInsertingTiledIntermediateWithTileSize::]
- GCC_except_table245
- GCC_except_table250
- GCC_except_table260
- GCC_except_table262
- GCC_except_table263
- GCC_except_table280
- GCC_except_table285
- GCC_except_table290
- GCC_except_table324
- GCC_except_table328
- GCC_except_table334
- GCC_except_table335
- GCC_except_table336
- GCC_except_table359
- GCC_except_table365
- GCC_except_table381
- GCC_except_table387
- GCC_except_table388
- GCC_except_table389
- GCC_except_table397
- GCC_except_table420
- GCC_except_table441
- __ZN2CIL17recurseGraphStatsEPNS_4NodeES1_iRNSt3__16vectorIPKS0_NS2_9allocatorIS5_EEEEiPNS2_3mapIS5_NS_13useCountDepthENS2_4lessIS5_EENS6_INS2_4pairIKS5_SB_EEEEEE
- __ZN2CIL21programNodeMemoryLoadEPKNS_11ProgramNodeERK6CGRectS5_mmb
- __ZN2CIL21rebuild_and_subdivideEPNS_7ContextEPNS_11ProgramNodeE6CGRectRKNSt3__13mapIPKNS_4NodeENS_13useCountDepthENS5_4lessIS9_EENS5_9allocatorINS5_4pairIKS9_SA_EEEEEERKNS5_6vectorIS9_NSD_IS9_EEEERNS5_5dequeIPKS2_NSD_ISS_EEEERSN_RmRKNSL_IS4_NSD_IS4_EEEE
- __ZN2CIL30_gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRmRKNSt3__16vectorIS6_NS8_9allocatorIS6_EEEE
- __ZNSt3__16vectorIPKN2CI4NodeENS_9allocatorIS4_EEE11__vallocateB9fqn220106Em
- __ZNSt3__16vectorIPKN2CI4NodeENS_9allocatorIS4_EEE18__assign_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPS4_SA_EEvT0_T1_l
- __ZZN2CIL29gather_rois_for_program_graphEPNS_7ContextEPKcPNS_11ProgramNodeE6CGRectRKNSt3__16vectorIS6_NS7_9allocatorIS6_EEEEEN13SignpostTimerD1Ev
- ___58-[CIImage imageByInsertingTiledIntermediateWithTileSize::]_block_invoke
- _objc_msgSend$imageByInsertingTiledIntermediateWithTileSize::
CStrings:
+ "    baselineExposure=%g\n"
+ "    boostAmount=%g\n"
+ "    boostShadowAmount=%g\n"
+ "    colorNoiseReductionAmount=%g\n"
+ "    colorNoiseReductionAmount=unsupported\n"
+ "    contrastAmount=%g\n"
+ "    contrastAmount=unsupported\n"
+ "    data=<%lu bytes>\n"
+ "    decoderVersion=%@\n"
+ "    despeckleAmount=%g\n"
+ "    despeckleAmount=unsupported\n"
+ "    detailAmount=%g\n"
+ "    detailAmount=unsupported\n"
+ "    draftModeEnabled=%s\n"
+ "    exposure=%g\n"
+ "    extendedDynamicRangeAmount=%g\n"
+ "    gamutMappingEnabled=%d\n"
+ "    highlightRecoveryEnabled=%s\n"
+ "    highlightRecoveryEnabled=unsupported\n"
+ "    lensCorrectionEnabled=%s\n"
+ "    lensCorrectionEnabled=unsupported\n"
+ "    linearSpaceFilter=%@\n"
+ "    localToneMapAmount=%g\n"
+ "    localToneMapAmount=unsupported\n"
+ "    luminanceNoiseReductionAmount=%g\n"
+ "    luminanceNoiseReductionAmount=unsupported\n"
+ "    moireReductionAmount=%g\n"
+ "    moireReductionAmount=unsupported\n"
+ "    nativeSize={%g, %g}\n"
+ "    neutralChromaticity={%g, %g}\n"
+ "    neutralLocation={%g, %g}\n"
+ "    neutralTemperature=%g\n"
+ "    neutralTint=%g\n"
+ "    orientation=%d\n"
+ "    scaleFactor=%g\n"
+ "    shadowBias=%g\n"
+ "    sharpnessAmount=%g\n"
+ "    sharpnessAmount=unsupported\n"
+ "    url=%@\n"
+ "-[CIImage imageByInsertingTiledIntermediateWithTileWidth:tileHeight:]"
+ "1663"
+ "CIKernel type reflection is not consistent across Metal (%{public}u) and FOSL (%{public}u) for %{public}s kernel"
+ "coefs3"
+ "copyIOSurfaceCallback: CreateSurface failed for [%g %g] format '%{public}.4s' alignment %d."
+ "copyIOSurfaceCallback: could not resolve a PixelFormatType for format %{public}s."
+ "copyIOSurfaceCallback: nested render failed for rect [%g %g %g %g], task %{public}s, error %{public}@."
+ "copyIOSurfaceCallback: no CI pixel format found for PixelFormatType '%{public}.4s'."
+ "copyIOSurfaceCallback: pixel format '%{public}.4s' is internal to CoreImage."
+ "copyIOSurfaceCallback: provider size [%g %g] exceeds max texture size %zu."
+ "copyImageBlockSetOptsCallback: mmap failed for %zu bytes, errno %d."
+ "copyImageBlockSetOptsCallback: page_size %d is not a multiple of requested alignment %d."
+ "copyImageBlockSetOptsCallback: render failed for rect [%g %g %g %g], task %{public}s, error %{public}@."
+ "copyImageBlockSetOptsCallback: unsupported kCGImageBlockColorSpaceRequest."
+ "copyImageBlockSetOptsCallback: unsupported kCGImageBlockFormatRequest %{public}@."
+ "flag5"
+ "float _lookup_with_extrapolation(float X, sampler2D lut, vec2 dim) {\n  float lutCoord = (X * dim.x) + dim.y;\n  float gain = texture2D(lut, vec2(lutCoord, 0.5)).r;\n  if (X > 1.0) return gain / X; else return gain;\n}\nkernel vec4 _headroomAdaptiveGainCurve(vec4 im, vec2 headrooms, float flag5, vec3 coefs, vec3 coefs3, float lookupTableScale, sampler2D lut, vec2 dim, vec2 range) {\n  vec3 gain = vec3(1.0);\n  vec3 rgb = im.rgb * lookupTableScale;\n  vec2 maxmin = vec2(max(rgb.r, max(rgb.g, rgb.b)), min(rgb.r, min(rgb.g, rgb.b)));\n  float value = dot(coefs, rgb) + dot(coefs3.xy, maxmin);\n  if (flag5 > 0.0) {\n    gain.r = _lookup_with_extrapolation(value + (coefs3.z * rgb.r), lut, dim);\n    gain.g = _lookup_with_extrapolation(value + (coefs3.z * rgb.g), lut, dim);\n    gain.b = _lookup_with_extrapolation(value + (coefs3.z * rgb.b), lut, dim);\n  } else gain.r = gain.g = gain.b = _lookup_with_extrapolation(value, lut, dim);\n  vec4 result = vec4(im.rgb * gain, im.a);\n  result.rgb = clamp(result.rgb, range.x, range.y);\n  return result;\n}\n"
+ "hagc_lut %016llX"
+ "kCGApplyHeadroomAdaptiveGainCurve"
+ "kCGHAGCurveBackupTransform"
+ "kCGHAGCurveTargetHeadroom"
+ "kernel vec4 _colorBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cs + vec4(Lb - Ls);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = ((n < 0.0) && (l > n)) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = ((x > 1.0) && (x > l)) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _hueBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 CsSort = (Cs.r > Cs.g) ? Cs : Cs.grba;\n  CsSort = (CsSort.g > CsSort.b) ? CsSort : CsSort.rbga;\n  CsSort = (CsSort.r > CsSort.g) ? CsSort : CsSort.grba;\n  vec4 CbSort = (Cb.r > Cb.g) ? Cb : Cb.grba;\n  CbSort = (CbSort.g > CbSort.b) ? CbSort : CbSort.rbga;\n  CbSort = (CbSort.r > CbSort.g) ? CbSort : CbSort.grba;\n  float bMax = CbSort.r;\n  float bMin = CbSort.b;\n  float Sb = bMax - bMin;\n  float sMax = CsSort.r;\n  float sMin = CsSort.b;\n  vec4 CsSb = (sMax > sMin) ? (((Cs - sMin) * Sb) / (sMax - sMin)) : vec4(0.0);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  float LCsSb = ((0.3 * CsSb.r) + (0.59 * CsSb.g)) + (0.11 * CsSb.b);\n  vec4 BB = CsSb + vec4(Lb - LCsSb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = ((n < 0.0) && (l > n)) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = ((x > 1.0) && (x > l)) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _luminosityBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cb + vec4(Ls - Lb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = ((n < 0.0) && (l > n)) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = ((x > 1.0) && (x > l)) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return (fore.a < 1e-6) ? back : (((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a));\n}\n"
+ "kernel vec4 _saturationBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 CsSort = (Cs.r > Cs.g) ? Cs : Cs.grba;\n  CsSort = (CsSort.g > CsSort.b) ? CsSort : CsSort.rbga;\n  CsSort = (CsSort.r > CsSort.g) ? CsSort : CsSort.grba;\n  vec4 CbSort = (Cb.r > Cb.g) ? Cb : Cb.grba;\n  CbSort = (CbSort.g > CbSort.b) ? CbSort : CbSort.rbga;\n  CbSort = (CbSort.r > CbSort.g) ? CbSort : CbSort.grba;\n  float sMax = CsSort.r;\n  float sMin = CsSort.b;\n  float Ss = sMax - sMin;\n  float bMax = CbSort.r;\n  float bMin = CbSort.b;\n  vec4 CbSs = (bMax > bMin) ? (((Cb - bMin) * Ss) / (bMax - bMin)) : vec4(0.0);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  float LCbSs = ((0.3 * CbSs.r) + (0.59 * CbSs.g)) + (0.11 * CbSs.b);\n  vec4 BB = CbSs + vec4(Lb - LCbSs);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = ((n < 0.0) && (l > n)) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = ((x > 1.0) && (x > l)) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "lookupTableScale"
+ "non-nil"
- "-[CIImage imageByInsertingTiledIntermediateWithTileSize::]"
- "1660"
- "kernel vec4 _colorBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cs + vec4(Lb - Ls);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _hueBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 CsSort = (Cs.r > Cs.g) ? Cs : Cs.grba;\n  CsSort = (CsSort.g > CsSort.b) ? CsSort : CsSort.rbga;\n  CsSort = (CsSort.r > CsSort.g) ? CsSort : CsSort.grba;\n  vec4 CbSort = (Cb.r > Cb.g) ? Cb : Cb.grba;\n  CbSort = (CbSort.g > CbSort.b) ? CbSort : CbSort.rbga;\n  CbSort = (CbSort.r > CbSort.g) ? CbSort : CbSort.grba;\n  float bMax = CbSort.r;\n  float bMin = CbSort.b;\n  float Sb = bMax - bMin;\n  float sMax = CsSort.r;\n  float sMin = CsSort.b;\n  vec4 CsSb = (sMax > sMin) ? (((Cs - sMin) * Sb) / (sMax - sMin)) : vec4(0.0);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  float LCsSb = ((0.3 * CsSb.r) + (0.59 * CsSb.g)) + (0.11 * CsSb.b);\n  vec4 BB = CsSb + vec4(Lb - LCsSb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _luminosityBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cb + vec4(Ls - Lb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return (fore.a < 1e-6) ? back : (((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a));\n}\n"
- "kernel vec4 _saturationBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 CsSort = (Cs.r > Cs.g) ? Cs : Cs.grba;\n  CsSort = (CsSort.g > CsSort.b) ? CsSort : CsSort.rbga;\n  CsSort = (CsSort.r > CsSort.g) ? CsSort : CsSort.grba;\n  vec4 CbSort = (Cb.r > Cb.g) ? Cb : Cb.grba;\n  CbSort = (CbSort.g > CbSort.b) ? CbSort : CbSort.rbga;\n  CbSort = (CbSort.r > CbSort.g) ? CbSort : CbSort.grba;\n  float sMax = CsSort.r;\n  float sMin = CsSort.b;\n  float Ss = sMax - sMin;\n  float bMax = CbSort.r;\n  float bMin = CbSort.b;\n  vec4 CbSs = (bMax > bMin) ? (((Cb - sMin) * Ss) / (bMax - bMin)) : vec4(0.0);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  float LCbSs = ((0.3 * CbSs.r) + (0.59 * CbSs.g)) + (0.11 * CbSs.b);\n  vec4 BB = CbSs + vec4(Lb - LCbSs);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
```
