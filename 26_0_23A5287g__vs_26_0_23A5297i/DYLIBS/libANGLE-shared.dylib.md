## libANGLE-shared.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib`

```diff

-622.1.18.10.3
-  __TEXT.__text: 0x2585f0
+622.1.19.10.4
+  __TEXT.__text: 0x259980
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__const: 0x836a0
-  __TEXT.__cstring: 0x40bf0
+  __TEXT.__const: 0x836d0
+  __TEXT.__cstring: 0x414cf
   __TEXT.__gcc_except_tab: 0x2964
   __TEXT.__oslogstring: 0xf
   __TEXT.__unwind_info: 0x16a0

   __TEXT.__objc_methname: 0x180f
   __TEXT.__objc_stubs: 0x1f00
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x12f48
+  __DATA_CONST.__const: 0x12f68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7c0
   __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x169e0
+  __AUTH_CONST.__const: 0x16a88
   __AUTH_CONST.__cfstring: 0x9c0
   __DATA.__data: 0x25858
   __DATA.__bss: 0xc

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EAEE7C41-0CED-34E4-96AA-161CDC1512F3
-  Functions: 8886
-  Symbols:   25141
-  CStrings:  7121
+  UUID: A1E61030-5534-38FB-BCF9-3A5A88B79BA3
+  Functions: 8900
+  Symbols:   25165
+  CStrings:  7130
 
Symbols:
+ _GL_FramebufferShadingRateEXT
+ _GL_GetFragmentShadingRatesEXT
+ _GL_ShadingRateCombinerOpsEXT
+ _GL_ShadingRateEXT
+ __ZN12_GLOBAL__N_19Rewriter213visitUnaryPreERN2sh12TIntermUnaryE
+ __ZN12_GLOBAL__N_19Rewriter214visitUnaryPostERN2sh12TIntermUnaryE
+ __ZN2gl36ValidateCopyImageSubDataTargetRegionEPKNS_7ContextEN5angle10EntryPointEjjiiiiiiiPi
+ __ZN2gl5State14setObjectDirtyEj
+ __ZN2gl7Context11drawBuffersEiPKj
+ __ZN2rx11DisplayImpl20supportsDmaBufFormatEi
+ __ZN2sh12_GLOBAL__N_121UniformSortComparatorclEPNS_11TIntermNodeES3_
+ __ZN2sh9TCompiler12sortUniformsEPNS_12TIntermBlockE
+ __ZN5angle12_GLOBAL__N_158G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16_ANGLE_to_defaultEj
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8sn200100IPPN2sh11TIntermNodeES7_NS_20back_insert_iteratorINS4_7TVectorIS6_EEEEEENS_4pairIT_T1_EESD_T0_SE_
+ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERN2sh12_GLOBAL__N_121UniformSortComparatorENS_11__wrap_iterIPPNS2_11TIntermNodeEEEEEvT1_SB_T0_NS_15iterator_traitsISB_E15difference_typeEPNSE_10value_typeEl
+ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERN2sh12_GLOBAL__N_121UniformSortComparatorENS_11__wrap_iterIPPNS2_11TIntermNodeEEEEEvT1_SB_SB_OT0_NS_15iterator_traitsISB_E15difference_typeESG_PNSF_10value_typeEl
+ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERN2sh12_GLOBAL__N_121UniformSortComparatorENS_11__wrap_iterIPPNS2_11TIntermNodeEEEEEvT1_SB_T0_NS_15iterator_traitsISB_E15difference_typeEPNSE_10value_typeE
- __ZN2gl11Framebuffer14setReadSurfaceEPKNS_7ContextEPN3egl7SurfaceE
- __ZN2gl36ValidateCopyImageSubDataTargetRegionEPKNS_7ContextEN5angle10EntryPointEjjiiiiiiPi
- __ZNK2rx11DisplayImpl20supportsDmaBufFormatEi
CStrings:
+ "\nANGLE_ALWAYS_INLINE int ANGLE_postDecrementInt(thread int &a)\n{\n    int r = a;\n    a = as_type<int>(as_type<metal::uint>(a) - 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int2 ANGLE_postDecrementInt(thread metal::int2 &a)\n{\n    metal::int2 r = a;\n    a = as_type<metal::int2>(as_type<metal::uint2>(a) - 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int3 ANGLE_postDecrementInt(thread metal::int3 &a)\n{\n    metal::int3 r = a;\n    a = as_type<metal::int3>(as_type<metal::uint3>(a) - 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int4 ANGLE_postDecrementInt(thread metal::int4 &a)\n{\n    metal::int4 r = a;\n    a = as_type<metal::int4>(as_type<metal::uint4>(a) - 1u);\n    return r;\n}\n\n"
+ "\nANGLE_ALWAYS_INLINE int ANGLE_postIncrementInt(thread int &a)\n{\n    int r = a;\n    a = as_type<int>(as_type<metal::uint>(a) + 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int2 ANGLE_postIncrementInt(thread metal::int2 &a)\n{\n    metal::int2 r = a;\n    a = as_type<metal::int2>(as_type<metal::uint2>(a) + 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int3 ANGLE_postIncrementInt(thread metal::int3 &a)\n{\n    metal::int3 r = a;\n    a = as_type<metal::int3>(as_type<metal::uint3>(a) + 1u);\n    return r;\n}\n\nANGLE_ALWAYS_INLINE metal::int4 ANGLE_postIncrementInt(thread metal::int4 &a)\n{\n    metal::int4 r = a;\n    a = as_type<metal::int4>(as_type<metal::uint4>(a) + 1u);\n    return r;\n}\n\n"
+ "\nANGLE_ALWAYS_INLINE int ANGLE_preDecrementInt(thread int &a)\n{\n    a = as_type<int>(as_type<metal::uint>(a) - 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int2 ANGLE_preDecrementInt(thread metal::int2 &a)\n{\n    a = as_type<metal::int2>(as_type<metal::uint2>(a) - 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int3 ANGLE_preDecrementInt(thread metal::int3 &a)\n{\n    a = as_type<metal::int3>(as_type<metal::uint3>(a) - 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int4 ANGLE_preDecrementInt(thread metal::int4 &a)\n{\n    a = as_type<metal::int4>(as_type<metal::uint4>(a) - 1u);\n    return a;\n}\n\n"
+ "\nANGLE_ALWAYS_INLINE int ANGLE_preIncrementInt(thread int &a)\n{\n    a = as_type<int>(as_type<metal::uint>(a) + 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int2 ANGLE_preIncrementInt(thread metal::int2 &a)\n{\n    a = as_type<metal::int2>(as_type<metal::uint2>(a) + 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int3 ANGLE_preIncrementInt(thread metal::int3 &a)\n{\n    a = as_type<metal::int3>(as_type<metal::uint3>(a) + 1u);\n    return a;\n}\n\nANGLE_ALWAYS_INLINE metal::int4 ANGLE_preIncrementInt(thread metal::int4 &a)\n{\n    a = as_type<metal::int4>(as_type<metal::uint4>(a) + 1u);\n    return a;\n}\n\n"
+ "2.1.25630 git hash: 411446032daa"
+ "2f96bee4dd67a4369415f991d31277a2"
+ "GL_EXT_fragment_shading_rate"
+ "GL_EXT_fragment_shading_rate_attachment"
+ "GL_EXT_fragment_shading_rate_primitive"
+ "No active tessellation control shader stage in this program."
+ "No active tessellation evaluation shader stage in this program."
+ "glFramebufferShadingRateEXT"
+ "glGetFragmentShadingRatesEXT"
+ "glShadingRateCombinerOpsEXT"
+ "glShadingRateEXT"
- "\ntemplate <typename T>\nANGLE_ALWAYS_INLINE T ANGLE_postDecrementInt(thread T &a)\n{\n    T r = a;\n    a = as_type<T>(metal::make_unsigned_t<T>(a) - 1);\n    return r;\n}\n\n"
- "\ntemplate <typename T>\nANGLE_ALWAYS_INLINE T ANGLE_postIncrementInt(thread T &a)\n{\n    T r = a;\n    a = as_type<T>(metal::make_unsigned_t<T>(a) + 1);\n    return r;\n}\n\n"
- "\ntemplate <typename T>\nANGLE_ALWAYS_INLINE thread T &ANGLE_preDecrementInt(thread T &a)\n{\n    a = as_type<T>(metal::make_unsigned_t<T>(a) - 1);\n    return a;\n}\n\n"
- "\ntemplate <typename T>\nANGLE_ALWAYS_INLINE thread T &ANGLE_preIncrementInt(thread T &a)\n{\n    a = as_type<T>(metal::make_unsigned_t<T>(a) + 1);\n    return a;\n}\n\n"
- "2.1.25561 git hash: 719109946c04"
- "fb65b4aee443e65179b4978731ab87a1"

```
