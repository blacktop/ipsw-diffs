## dyld

> `/System/ExclaveKit/usr/lib/dyld`

```diff

-27050.3.0.0.0
-  __TEXT.__text: 0x5aad0 sha256:584a1703bcdbbf590dd86fe5091af32c97ef2166b822b2e910a0eb31d5c8fbef
-  __TEXT.__const: 0x1c0a8 sha256:f0fdda36f705dc503c7e3ea35734d8aa1816f7612d7f85730f9189464e3e5489
-  __TEXT.__cstring: 0xe951 sha256:a1c525a812e7662a4265f07c18f08cd00603c4dfe0b61f62493b27a551eeb790
-  __TEXT.__unwind_info: 0x1e50 sha256:343a12ae72d0cc6cc743c8b7e9f740c6896151b370214cb7ea778ae91916ec25
-  __TEXT.__eh_frame: 0x48 sha256:3d17b4509b2d5b06173db0c130aef6438f3e3197c6464fd1461d0476aff5c62a
-  __DATA_CONST.__const: 0xab0 sha256:83cc2d883046e280a17e8e8e1fd10d4fdd505d1f3b937ceaafa1edd84585c681
-  __AUTH_CONST.__const: 0x3dc8 sha256:8c1f4ba5b9074e106b1934a9cfbfe329c8c4a89c935f489d6578f05e06c1e194
-  __AUTH.__data: 0x470 sha256:4c54f26222d11cc19887886b95aaf25b237e9575644f420769745a25a6018c2e
-  __DATA.__data: 0x1448 sha256:9a3e4bea80cd1b59946f0fc369a16b1b54c736c61c70e35585654728718466ae
+27056.1.0.0.0
+  __TEXT.__text: 0x5b73c sha256:31021d8a13978811bee5d6721ed21528745f96e8347ecadd3a31a3ee1433c42c
+  __TEXT.__const: 0x1c0a8 sha256:6c82fde3b1a48ea9bc78d8568ceb8d2df5ae4f2bf6761ae971ed0df6cbe200a1
+  __TEXT.__cstring: 0xea6c sha256:b0b089030263d824cf4325ed04683e904cf6d4910d31c6e6c2e6cbad24b2eb77
+  __TEXT.__unwind_info: 0x1e88 sha256:ead055145233855c9b8ebd6c87ffa222015b7ef779ac4df8fa92328e745ec79c
+  __TEXT.__eh_frame: 0x48 sha256:9de63d4c377e0d5fe4a5e36df26ef9ecc75d461ca0d05218cb61a2e6f7adb24d
+  __DATA_CONST.__const: 0xaf0 sha256:873a763e3caf134864b16ee97918d5f154f95875f7b87e42ff791e97256543bf
+  __AUTH_CONST.__const: 0x3eb8 sha256:5af4ff8632e9cf1afccf9926917f57c828cfec9f0371723d8cf9ac1ceb0c32f9
+  __AUTH.__data: 0x470 sha256:645213da486ceccaa84c7b56ad11a65ea52663054d1649c101426721fd2d33dd
+  __DATA.__data: 0x1448 sha256:34358da5bed0aeaedecc351b49d1b6146edcdadb8797e6394e8962213bf8a4a0
   __DATA.__ENDPOINTS: 0x62a sha256:a65b923aa527372c45dab6d6bd416f3b881efa306618230e34e6cb032783fec9
   __DATA.__thread_vars: 0x0
   __DATA.__thread_data: 0x0
   __DATA.__thread_bss: 0x0
   __DATA.__common: 0x550 sha256:e5fa86d863f367b89108b44b23ea6b051f772ee32636442cc4dc9f5de35c44d7
-  __DATA.__bss: 0xba3f8 sha256:acc462b7f8e67b3d1d668d5bf6e9bde0792baf9b991ec759f3b4bf8e9f344630
-  __DATA_DIRTY.__all_image_info: 0x170 sha256:8db598f75e9a5df88567eca07fb33f917a61e3281a2092eedf4639d72d15adce
-  UUID: 5C6137C7-2390-323E-AE2C-047674CDB4F0
-  Functions: 2727
-  Symbols:   2843
-  CStrings:  1454
+  __DATA.__bss: 0xba3f8 sha256:19a0cbf3f0f4de5c70ed7b8a99ea734919971ab7c1276bc1c8d83259374b8259
+  __DATA_DIRTY.__all_image_info: 0x170 sha256:95528d4c0d647764d4aad19bc1e6b3c660b40f0f1780380053972ee8fd13d99d
+  UUID: E8299A28-DEAB-3515-B48C-6E95C422D5B5
+  Functions: 2740
+  Symbols:   2865
+  CStrings:  1463
 
Symbols:
+ __Block_byref_object_copy_.15
+ __Block_byref_object_copy_.195
+ __Block_byref_object_copy_.20
+ __Block_byref_object_copy_.242
+ __Block_byref_object_copy_.274
+ __Block_byref_object_copy_.285
+ __Block_byref_object_copy_.302
+ __Block_byref_object_copy_.307
+ __Block_byref_object_copy_.312
+ __Block_byref_object_copy_.477
+ __Block_byref_object_dispose_.16
+ __Block_byref_object_dispose_.196
+ __Block_byref_object_dispose_.21
+ __Block_byref_object_dispose_.243
+ __Block_byref_object_dispose_.275
+ __Block_byref_object_dispose_.286
+ __Block_byref_object_dispose_.303
+ __Block_byref_object_dispose_.308
+ __Block_byref_object_dispose_.313
+ __Block_byref_object_dispose_.478
+ __ZN5dyld317OverflowSafeArrayIPKcLy4294967295EE6resizeEy
+ __ZN5dyld317OverflowSafeArrayIPKcLy4294967295EE9push_backERKS2_
+ __ZN5dyld412RuntimeState29incOverriddenCachedDylibCountEv
+ __ZN5dyld423analyzeObjCPatchClassesERKN6mach_o5ImageEU13block_pointerFvPKvPKcbEU13block_pointerFvS5_RKNS0_5FixupEE
+ __ZN5dyld436isInstallNameEligibleForObjCPatchingE7CString
+ __ZN5dyld46Loader9getLoaderER11DiagnosticsRNS_12RuntimeStateEPKcRKNS0_11LoadOptionsEb
+ __ZNK6mach_o6Header10hasSegmentE7CString
+ __ZNK7CString8containsENSt3__117basic_string_viewIcNS0_11char_traitsIcEEEE
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB9fqn220106EPKc
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB9sqn220106EPKc
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB9fqn220106EmmS3_
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB9sqn220106EmmS3_
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqn220106EPKvm
+ __ZNKSt3__16ranges6__findclB9fqn220106IRN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEEEPS7_NS_8identityEEENS_7_IfImplIXL_ZNS0_14borrowed_rangeIT_EEEEE7_SelectIDTclL_ZNS0_5__cpo5beginEEclsr3stdE7declvalIRSH_EEEENS0_8danglingEEEOSH_RKT0_T1_
+ __ZNSt3__119__unwrap_range_implIN3lsl6VectorI14dyld_uuid_infoE15CheckedIteratorIS3_EES6_E8__unwrapB9fqn220106ES6_S6_
+ __ZNSt3__119__unwrap_range_implIN3lsl6VectorI15dyld_image_infoE15CheckedIteratorIS3_EES6_E8__unwrapB9fqn220106ES6_S6_
+ __ZNSt3__119__unwrap_range_implIN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE15CheckedIteratorIS8_EESB_E8__unwrapB9fqn220106ESB_SB_
+ __ZNSt3__119__unwrap_range_implIN3lsl6VectorINS_4pairIPKN5dyld46LoaderEPKcEEE15CheckedIteratorISA_EESD_E8__unwrapB9fqn220106ESD_SD_
+ __ZNSt3__119__unwrap_range_implIN3lsl6VectorIPKN5dyld46LoaderEE15CheckedIteratorIS6_EES9_E8__unwrapB9fqn220106ES9_S9_
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9fqn220106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9fqn220106EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9fqn220106EPKcm
+ __ZNSt3__124__copy_move_unwrap_itersB9fqn220106INS_11__copy_implEN3lsl6VectorI14dyld_uuid_infoE15CheckedIteratorIS4_EES7_PS4_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
+ __ZNSt3__124__copy_move_unwrap_itersB9fqn220106INS_11__copy_implEN3lsl6VectorI15dyld_image_infoE15CheckedIteratorIS4_EES7_PS4_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
+ __ZNSt3__124__copy_move_unwrap_itersB9fqn220106INS_11__copy_implEN3lsl6VectorINS_4pairIPKN5dyld46LoaderEPKcEEE15CheckedIteratorISB_EESE_PSB_Li0EEENS4_IT0_T2_EESG_T1_SH_
+ __ZNSt3__124__copy_move_unwrap_itersB9fqn220106INS_11__copy_implEN3lsl6VectorIPKN5dyld46LoaderEE15CheckedIteratorIS7_EESA_PS7_Li0EEENS_4pairIT0_T2_EESD_T1_SE_
+ __ZNSt3__124__copy_move_unwrap_itersB9fqn220106INS_11__copy_implENS_14__bounded_iterIPcEES4_S4_Li0EEENS_4pairIT0_T2_EES6_T1_S7_
+ __ZNSt3__127__throw_bad_optional_accessB9fqn220106Ev
+ __ZNSt3__16ranges6__find13__find_unwrapB9fqn220106IN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE15CheckedIteratorISA_EESD_PS7_NS_8identityEEET_SG_T0_RKT1_RT2_
+ ___ZN5dyld423analyzeObjCPatchClassesERKN6mach_o5ImageEU13block_pointerFvPKvPKcbEU13block_pointerFvS5_RKNS0_5FixupEE_block_invoke.10
+ ___ZNK5dyld416JustInTimeLoader11applyFixupsER11DiagnosticsRNS_12RuntimeStateERNS_34DyldCacheDataConstLazyScopedWriterEbPN3lsl6VectorINSt3__14pairIPKNS_6LoaderEPKcEEEE_block_invoke.43
+ ___ZNK5dyld416JustInTimeLoader11applyFixupsER11DiagnosticsRNS_12RuntimeStateERNS_34DyldCacheDataConstLazyScopedWriterEbPN3lsl6VectorINSt3__14pairIPKNS_6LoaderEPKcEEEE_block_invoke.51
+ ___ZNK5dyld46Loader13resolveSymbolER11DiagnosticsRNS_12RuntimeStateEiPKcbbU13block_pointerFvjjRKNS0_14ResolvedSymbolEEb_block_invoke.49
+ ___ZNK5dyld46Loader13resolveSymbolER11DiagnosticsRNS_12RuntimeStateEiPKcbbU13block_pointerFvjjRKNS0_14ResolvedSymbolEEb_block_invoke.49.cold.1
+ ___ZNK5dyld46Loader17forEachBindTargetER11DiagnosticsRNS_12RuntimeStateEU13block_pointerFvjjRKNS0_14ResolvedSymbolEEbU13block_pointerFvS7_RbESC__block_invoke.35
+ ___ZNK6mach_o6Header14forEachSectionEU13block_pointerFvRKNS0_11SectionInfoERbE_block_invoke.501
+ ____ZN5dyld423analyzeObjCPatchClassesERKN6mach_o5ImageEU13block_pointerFvPKvPKcbEU13block_pointerFvS5_RKNS0_5FixupEE_block_invoke
+ ____ZN5dyld4L19getObjCPatchClassesERKN6mach_o5ImageERN5dyld33MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke_2
+ ____ZNK6mach_o6Header10hasSegmentE7CString_block_invoke
+ ____accumulator_destructor_block_invoke
+ ____find_or_create_accumulator_scoped_block_invoke
+ ____find_or_create_accumulator_scoped_block_invoke_2
+ ___find_or_create_accumulator_scoped_block_invoke.cold.1
+ ___find_or_create_accumulator_scoped_block_invoke.cold.2
+ ___tb_list_find_or_create_scoped_block_invoke
+ ___tb_message_accumulator_accumulate_block_invoke
+ __block_descriptor_tmp.104
+ __block_descriptor_tmp.110
+ __block_descriptor_tmp.112
+ __block_descriptor_tmp.147
+ __block_descriptor_tmp.201
+ __block_descriptor_tmp.246
+ __block_descriptor_tmp.263
+ __block_descriptor_tmp.27
+ __block_descriptor_tmp.278
+ __block_descriptor_tmp.284
+ __block_descriptor_tmp.289
+ __block_descriptor_tmp.306
+ __block_descriptor_tmp.311
+ __block_descriptor_tmp.316
+ __block_descriptor_tmp.319
+ __block_descriptor_tmp.464
+ __block_descriptor_tmp.470
+ __block_descriptor_tmp.473
+ __block_descriptor_tmp.481
+ __block_descriptor_tmp.484
+ __block_descriptor_tmp.487
+ __block_descriptor_tmp.493
+ __block_descriptor_tmp.496
+ __block_descriptor_tmp.500
+ __block_descriptor_tmp.504
+ __block_descriptor_tmp.507
+ __block_descriptor_tmp.529
+ __block_descriptor_tmp.542
+ __block_descriptor_tmp.56
+ __block_descriptor_tmp.569
+ __block_descriptor_tmp.6
+ __block_descriptor_tmp.61
+ __block_descriptor_tmp.64
+ __block_descriptor_tmp.81
+ __block_descriptor_tmp.85
+ __block_descriptor_tmp.86
+ __block_descriptor_tmp.89
+ __block_descriptor_tmp.9
+ __block_descriptor_tmp.96
+ __block_literal_global.15
+ __find_or_create_accumulator_scoped
+ __iterate_list_locked
+ __tb_message_accumulator_accumulate_block_invoke.cold.1
+ __tb_message_accumulator_accumulate_block_invoke.cold.2
+ __tb_message_accumulator_accumulate_block_invoke.cold.3
+ __tb_message_accumulator_accumulate_block_invoke.cold.4
+ __tb_message_accumulator_accumulate_block_invoke.cold.5
+ _tb_list_find_or_create_scoped
+ _xrt__conclave_deny_ipc
+ tb_list_find_or_create_scoped.cold.1
+ tb_null_transport_create_inplace_with_endpoint.cold.1
- __Block_byref_object_copy_.194
- __Block_byref_object_copy_.241
- __Block_byref_object_copy_.26
- __Block_byref_object_copy_.273
- __Block_byref_object_copy_.28
- __Block_byref_object_copy_.284
- __Block_byref_object_copy_.301
- __Block_byref_object_copy_.306
- __Block_byref_object_copy_.311
- __Block_byref_object_copy_.476
- __Block_byref_object_dispose_.195
- __Block_byref_object_dispose_.242
- __Block_byref_object_dispose_.27
- __Block_byref_object_dispose_.274
- __Block_byref_object_dispose_.285
- __Block_byref_object_dispose_.29
- __Block_byref_object_dispose_.302
- __Block_byref_object_dispose_.307
- __Block_byref_object_dispose_.312
- __Block_byref_object_dispose_.477
- __ZN5dyld46Loader9getLoaderER11DiagnosticsRNS_12RuntimeStateEPKcRKNS0_11LoadOptionsE
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB9fqn220100EPKc
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB9sqn220100EPKc
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB9fqn220100EmmS3_
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB9sqn220100EmmS3_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9fqn220100EPKvm
- __ZNKSt3__16ranges6__findclB9fqn220100IRN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEEEPS7_NS_8identityEEENS_7_IfImplIXL_ZNS0_14borrowed_rangeIT_EEEEE7_SelectIDTclL_ZNS0_5__cpo5beginEEclsr3stdE7declvalIRSH_EEEENS0_8danglingEEEOSH_RKT0_T1_
- __ZNSt3__119__unwrap_range_implIN3lsl6VectorI14dyld_uuid_infoE15CheckedIteratorIS3_EES6_E8__unwrapB9fqn220100ES6_S6_
- __ZNSt3__119__unwrap_range_implIN3lsl6VectorI15dyld_image_infoE15CheckedIteratorIS3_EES6_E8__unwrapB9fqn220100ES6_S6_
- __ZNSt3__119__unwrap_range_implIN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE15CheckedIteratorIS8_EESB_E8__unwrapB9fqn220100ESB_SB_
- __ZNSt3__119__unwrap_range_implIN3lsl6VectorINS_4pairIPKN5dyld46LoaderEPKcEEE15CheckedIteratorISA_EESD_E8__unwrapB9fqn220100ESD_SD_
- __ZNSt3__119__unwrap_range_implIN3lsl6VectorIPKN5dyld46LoaderEE15CheckedIteratorIS6_EES9_E8__unwrapB9fqn220100ES9_S9_
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B9fqn220100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B9fqn220100EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B9fqn220100EPKcm
- __ZNSt3__124__copy_move_unwrap_itersB9fqn220100INS_11__copy_implEN3lsl6VectorI14dyld_uuid_infoE15CheckedIteratorIS4_EES7_PS4_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
- __ZNSt3__124__copy_move_unwrap_itersB9fqn220100INS_11__copy_implEN3lsl6VectorI15dyld_image_infoE15CheckedIteratorIS4_EES7_PS4_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
- __ZNSt3__124__copy_move_unwrap_itersB9fqn220100INS_11__copy_implEN3lsl6VectorINS_4pairIPKN5dyld46LoaderEPKcEEE15CheckedIteratorISB_EESE_PSB_Li0EEENS4_IT0_T2_EESG_T1_SH_
- __ZNSt3__124__copy_move_unwrap_itersB9fqn220100INS_11__copy_implEN3lsl6VectorIPKN5dyld46LoaderEE15CheckedIteratorIS7_EESA_PS7_Li0EEENS_4pairIT0_T2_EESD_T1_SE_
- __ZNSt3__124__copy_move_unwrap_itersB9fqn220100INS_11__copy_implENS_14__bounded_iterIPcEES4_S4_Li0EEENS_4pairIT0_T2_EES6_T1_S7_
- __ZNSt3__127__throw_bad_optional_accessB9fqn220100Ev
- __ZNSt3__16ranges6__find13__find_unwrapB9fqn220100IN3lsl6VectorI18AuthenticatedValueIPKN5dyld46LoaderEEE15CheckedIteratorISA_EESD_PS7_NS_8identityEEET_SG_T0_RKT1_RT2_
- ___ZN5dyld4L19getObjCPatchClassesERKN6mach_o5ImageERN5dyld33MapIPKvbNS_11HashPointerENS_12EqualPointerEEE_block_invoke.92
- ___ZNK5dyld416JustInTimeLoader11applyFixupsER11DiagnosticsRNS_12RuntimeStateERNS_34DyldCacheDataConstLazyScopedWriterEbPN3lsl6VectorINSt3__14pairIPKNS_6LoaderEPKcEEEE_block_invoke.30
- ___ZNK5dyld416JustInTimeLoader11applyFixupsER11DiagnosticsRNS_12RuntimeStateERNS_34DyldCacheDataConstLazyScopedWriterEbPN3lsl6VectorINSt3__14pairIPKNS_6LoaderEPKcEEEE_block_invoke.37
- ___ZNK5dyld46Loader13resolveSymbolER11DiagnosticsRNS_12RuntimeStateEiPKcbbU13block_pointerFvjjRKNS0_14ResolvedSymbolEEb_block_invoke.48
- ___ZNK5dyld46Loader13resolveSymbolER11DiagnosticsRNS_12RuntimeStateEiPKcbbU13block_pointerFvjjRKNS0_14ResolvedSymbolEEb_block_invoke.48.cold.1
- ___ZNK5dyld46Loader17forEachBindTargetER11DiagnosticsRNS_12RuntimeStateEU13block_pointerFvjjRKNS0_14ResolvedSymbolEEbU13block_pointerFvS7_RbESC__block_invoke.34
- ___ZNK6mach_o6Header14forEachSectionEU13block_pointerFvRKNS0_11SectionInfoERbE_block_invoke.500
- ____add_accumulator_block_invoke
- ___block_literal_global
- ___liblibc_strstr
- __add_accumulator
- __block_descriptor_tmp.100
- __block_descriptor_tmp.146
- __block_descriptor_tmp.199
- __block_descriptor_tmp.24
- __block_descriptor_tmp.245
- __block_descriptor_tmp.262
- __block_descriptor_tmp.277
- __block_descriptor_tmp.283
- __block_descriptor_tmp.288
- __block_descriptor_tmp.305
- __block_descriptor_tmp.310
- __block_descriptor_tmp.315
- __block_descriptor_tmp.318
- __block_descriptor_tmp.33
- __block_descriptor_tmp.42
- __block_descriptor_tmp.44
- __block_descriptor_tmp.46
- __block_descriptor_tmp.463
- __block_descriptor_tmp.469
- __block_descriptor_tmp.472
- __block_descriptor_tmp.480
- __block_descriptor_tmp.483
- __block_descriptor_tmp.486
- __block_descriptor_tmp.492
- __block_descriptor_tmp.495
- __block_descriptor_tmp.499
- __block_descriptor_tmp.5
- __block_descriptor_tmp.503
- __block_descriptor_tmp.506
- __block_descriptor_tmp.541
- __block_descriptor_tmp.568
- __block_descriptor_tmp.80
- __block_descriptor_tmp.84
- __block_descriptor_tmp.88
- __block_descriptor_tmp.91
- __block_descriptor_tmp.94
- __block_descriptor_tmp.95
- _add_accumulator.cold.1
- _strstr
- _tb_list_add
- _tb_list_find
- tb_message_accumulator_accumulate.cold.1
- tb_message_accumulator_accumulate.cold.2
- tb_message_accumulator_accumulate.cold.3
- tb_message_accumulator_accumulate.cold.4
- tb_message_accumulator_accumulate.cold.5
- tb_message_accumulator_accumulate.cold.6
- tb_message_accumulator_accumulate.cold.7
- tb_message_accumulator_accumulate.cold.8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRa2ugDjIAjp_ruvsM5XnGebNK9Wr_Ox3eaahQ0/Library/Caches/com.apple.xbs/TemporaryDirectory.450478/Sources/libclosure_exclavekit/runtime.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.MacOSX.platform/Developer/SDKs/ExclaveKit.MacOSX27.0.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
+ "/AppleInternal/Library/BuildRoots/4~CRbFugA2s3lKa7_Rx4LCfe3HFYKe4SAf2n1Ok8Q/Library/Caches/com.apple.xbs/TemporaryDirectory.laqceZ/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
+ "/AppleInternal/Library/BuildRoots/4~CRshugB_pZbLXU5L2x6uf6S4SzlY67a5lSy5fnY/Library/Caches/com.apple.xbs/TemporaryDirectory.ZeJ2wU/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/Array.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/CString.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/MachOLayout.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/common/Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/Loader.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Allocator.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Allocator.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/lsl/Vector.h"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Header.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Image.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Platform.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CSDqugDGr3QpcN4-2R_LDFRA67YsCaI2PyOdTUQ/Library/Caches/com.apple.xbs/TemporaryDirectory.XdtyYX/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
+ "27056.1"
+ "B16@?0^v8"
+ "B16@?0^{tb_message_accumulator_s=QQQ*}8"
+ "Unexpected return from endpoint!"
+ "^v8@?0"
+ "__ETC"
+ "tb_list.c"
+ "thread holds resources after return from call"
+ "v24@?0^{tb_list_node_s=^{tb_list_node_s}Q^v@?}8^B16"
+ "v24@?0r^v8r^{Fixup=^v^{MappedSegment}{PointerMetaData=b16b8b1b2b1b4}BBB(?={?=Ii}{?=Q})}16"
+ "v28@?0r^v8r*16B24"
- "/AppleInternal/Library/BuildRoots/4~CQBZugCut2vfaS6xwTw013RNB5eCl25B_3SA19g/Library/Caches/com.apple.xbs/TemporaryDirectory.WUe1NI/Sources/libclosure_exclavekit/runtime.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.MacOSX.platform/Developer/SDKs/ExclaveKit.MacOSX27.0.Internal.sdk/System/ExclaveKit/usr/include/xrt/thread.h"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Library/Caches/com.apple.xbs/TemporaryDirectory.RpFfs0/Binaries/Tightbeam_exclavekit/install/TempContent/Objects/Tightbeam.build/Tightbeam_exclavekit_dyld.build/DerivedSources/tb_codec.c"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Library/Caches/com.apple.xbs/TemporaryDirectory.RpFfs0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/Transports/cL4/cL4_transport.c"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Library/Caches/com.apple.xbs/TemporaryDirectory.RpFfs0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_accumulator.c"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Library/Caches/com.apple.xbs/TemporaryDirectory.RpFfs0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/message_splitter.c"
- "/AppleInternal/Library/BuildRoots/4~CQKLugDLa32jKzyGf6vOtMkIWLo4sSQba22uumM/Library/Caches/com.apple.xbs/TemporaryDirectory.RpFfs0/Sources/Tightbeam_exclavekit/Runtime/Tightbeam/tb_connection.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Binaries/ExclavePlatform_extra_exclavekit/install/TempContent/Objects/ExclavePlatform.build/libvas.build/DerivedSources/EASM_C.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/common/serial/serial_common.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/arch/arm64/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/exception.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/process.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/sync_trace.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/concurrency/thread_id.c"
- "/AppleInternal/Library/BuildRoots/4~CQl5ugBNkTWmQ8VSD98zH_i6vFBt8wSVe1f4UAA/Library/Caches/com.apple.xbs/TemporaryDirectory.oOVfTD/Sources/ExclavePlatform_extra_exclavekit/xrt/xrt/ipc/endpoint.c"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/Array.h"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/CString.h"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/DyldSharedCache.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/MachOLayout.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/ObjCVisitor.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/common/Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/DyldAPIs.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/DyldProcessConfig.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/DyldRuntimeState.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/JustInTimeLoader.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/Loader.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/PrebuiltLoader.h"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/dyld/dyldMain.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/lsl/Allocator.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/lsl/Allocator.h"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/lsl/Vector.h"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/mach_o/Header.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/mach_o/Image.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/mach_o/Platform.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/mach_o/Symbol.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl6ugDynnXKkQh3e9dHjSEsCudvFWMwn5-BorM/Library/Caches/com.apple.xbs/TemporaryDirectory.cTeW0V/Sources/dyld_exclavekit/mach_o/UnsafeHeader.cpp"
- "/usr/lib/libodmodule.dylib"
- "27050.3"

```
