## dyld

> `/usr/lib/dyld`

```diff

-1228.0.0.0.0
+1227.0.0.0.0
   __TEXT.__text: 0x70054
   __TEXT.__const: 0x1c38
-  __TEXT.__cstring: 0xe60a
+  __TEXT.__cstring: 0xe649
   __TEXT.__info_plist: 0x4e6
   __TEXT.__unwind_info: 0x4a0
   __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x6108
-  __DATA.__data: 0x1ec8
+  __DATA_CONST.__const: 0x60c0
+  __DATA.__data: 0x1eb0
   __DATA.__common: 0x8f0
   __DATA.__bss: 0x51c
   __DATA_DIRTY.__data: 0x14

   __DATA_DIRTY.__bss: 0x28
   __TPRO_CONST.__allocator: 0x44000
   __TPRO_CONST.__data: 0x8
-  Functions: 2315
-  Symbols:   3126
-  CStrings:  1832
+  Functions: 2314
+  Symbols:   3123
+  CStrings:  1834
 
Symbols:
+ _ZN12objc_visitor7Visitor12forEachClassEbRKNS0_11DataSectionEU13block_pointerFvRNS_5ClassEbRbE.cold.1
+ __Block_byref_object_copy_.116
+ __Block_byref_object_copy_.160
+ __Block_byref_object_copy_.48
+ __Block_byref_object_copy_.50
+ __Block_byref_object_copy_.52
+ __Block_byref_object_copy_.54
+ __Block_byref_object_copy_.56
+ __Block_byref_object_copy_.85
+ __Block_byref_object_copy_.93
+ __Block_byref_object_copy_.97
+ __Block_byref_object_dispose_.117
+ __Block_byref_object_dispose_.161
+ __Block_byref_object_dispose_.49
+ __Block_byref_object_dispose_.51
+ __Block_byref_object_dispose_.53
+ __Block_byref_object_dispose_.55
+ __Block_byref_object_dispose_.57
+ __Block_byref_object_dispose_.86
+ __Block_byref_object_dispose_.94
+ __Block_byref_object_dispose_.98
+ __ZN12objc_visitor7Visitor12forEachClassEbRKNS0_11DataSectionEU13block_pointerFvRNS_5ClassEbRbE
+ __ZNK12objc_visitor7Visitor19findObjCDataSectionEPKc
+ ___ZN5dyld412RuntimeState22buildInterposingTablesEv_block_invoke.89
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.58
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.58.cold.1
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.62
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.62.cold.1
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.62.cold.2
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.62.cold.3
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.62.cold.4
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.69
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.69.cold.1
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.69.cold.2
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.74
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.74.cold.1
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.74.cold.2
+ ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.79
+ ___ZN5dyld412RuntimeState9setUpTLVsEPKN5dyld313MachOAnalyzerE_block_invoke.123
+ ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.143
+ ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.151
+ ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.155
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.162
+ ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.162.cold.1
+ ____ZNK12objc_visitor7Visitor19findObjCDataSectionEPKc_block_invoke
+ __block_descriptor_tmp.101
+ __block_descriptor_tmp.146
+ __block_descriptor_tmp.154
+ __block_descriptor_tmp.158
+ __block_descriptor_tmp.30
+ __block_descriptor_tmp.61
+ __block_descriptor_tmp.71
- _ZN12objc_visitor7Visitor12forEachClassEbRKNS0_7SectionEU13block_pointerFvRNS_5ClassEbRbE.cold.1
- __Block_byref_object_copy_.115
- __Block_byref_object_copy_.159
- __Block_byref_object_copy_.47
- __Block_byref_object_copy_.49
- __Block_byref_object_copy_.51
- __Block_byref_object_copy_.53
- __Block_byref_object_copy_.55
- __Block_byref_object_copy_.84
- __Block_byref_object_copy_.92
- __Block_byref_object_copy_.96
- __Block_byref_object_dispose_.116
- __Block_byref_object_dispose_.160
- __Block_byref_object_dispose_.48
- __Block_byref_object_dispose_.50
- __Block_byref_object_dispose_.52
- __Block_byref_object_dispose_.54
- __Block_byref_object_dispose_.56
- __Block_byref_object_dispose_.85
- __Block_byref_object_dispose_.93
- __Block_byref_object_dispose_.97
- __ZN12objc_visitor7Visitor12forEachClassEbRKNS0_7SectionEU13block_pointerFvRNS_5ClassEbRbE
- __ZNK12objc_visitor7Visitor11findSectionENSt3__14spanIPKcLm18446744073709551615EEES4_
- __ZZNK12objc_visitor7Visitor19findObjCDataSectionEPKcE16objcDataSegments
- ___ZN5dyld412RuntimeState22buildInterposingTablesEv_block_invoke.88
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.57
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.57.cold.1
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.61
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.61.cold.1
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.61.cold.2
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.61.cold.3
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.61.cold.4
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.68
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.68.cold.1
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.68.cold.2
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.73
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.73.cold.1
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.73.cold.2
- ___ZN5dyld412RuntimeState23appendInterposingTuplesEPKNS_6LoaderEPKhj_block_invoke.78
- ___ZN5dyld412RuntimeState9setUpTLVsEPKN5dyld313MachOAnalyzerE_block_invoke.122
- ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.142
- ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.150
- ___ZNK5dyld413ProcessConfig13PathOverrides18forEachPathVariantEPKcN5dyld38PlatformEbbRbU13block_pointerFvS3_NS1_4TypeES6_E_block_invoke.154
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.161
- ___ZZN5dyld412RuntimeState16setObjCNotifiersEPFvPKcPK11mach_headerEPFvS5_PvS5_PKvEPFvjPK29_dyld_objc_notify_mapped_infoEPFvSF_EPFvjSF_U13block_pointerFvjEEENK3$_0clEv_block_invoke.161.cold.1
- ____ZNK12objc_visitor7Visitor11findSectionENSt3__14spanIPKcLm18446744073709551615EEES4__block_invoke
- __block_descriptor_tmp.104
- __block_descriptor_tmp.125
- __block_descriptor_tmp.138
- __block_descriptor_tmp.141
- __block_descriptor_tmp.145
- __block_descriptor_tmp.153
- __block_descriptor_tmp.167
- __block_descriptor_tmp.64
- __block_descriptor_tmp.87
- _ccsha384_vng_arm_hw_compress
- _ccsha384_vng_arm_hw_di
CStrings:
+ "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Binaries/libignition/install/Symbols/ignition_core"
+ "1227"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Jun 20 20:32:59 PDT 2024; root:libignition-56~29992/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Jun 20 20:32:59 PDT 2024; root:libignition-56~29992/libignition_core/RELEASE_ARM64E"
+ "avoid"
+ "overrides dylib in dyld cache, so cannot be delayed: %!s(MISSING)\n"
- "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/libignition/install/Symbols/ignition_core"
- "1228"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jul  1 21:46:46 PDT 2024; root:libignition-56~31290/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Jul  1 21:46:46 PDT 2024; root:libignition-56~31290/libignition_core/RELEASE_ARM64E"

```
