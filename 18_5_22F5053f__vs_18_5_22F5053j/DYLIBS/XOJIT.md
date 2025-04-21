## XOJIT

> `/System/Library/PrivateFrameworks/XOJIT.framework/XOJIT`

```diff

-63.0.0.0.0
-  __TEXT.__text: 0x25b21c
+68.0.0.0.0
+  __TEXT.__text: 0x25cfb4
   __TEXT.__auth_stubs: 0x11f0
   __TEXT.__init_offsets: 0x118
-  __TEXT.__const: 0x1e564
+  __TEXT.__const: 0x1e5b4
   __TEXT.__oslogstring: 0x16b
   __TEXT.__swift5_typeref: 0x290
   __TEXT.__swift5_capture: 0x54
-  __TEXT.__cstring: 0x7b8f5
+  __TEXT.__cstring: 0x7baf6
   __TEXT.__swift5_reflstr: 0x252
   __TEXT.__swift5_assocty: 0x28
   __TEXT.__constg_swiftt: 0x620

   __TEXT.__swift5_types: 0x94
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x4fe8
+  __TEXT.__unwind_info: 0x5000
   __TEXT.__eh_frame: 0xa18
   __TEXT.__objc_methname: 0x36
   __DATA_CONST.__got: 0x100

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __DATA_CONST.__orc_runtime: 0x7c2278
+  __DATA_CONST.__orc_runtime: 0x7c22a8
   __AUTH_CONST.__auth_got: 0x8f8
   __AUTH_CONST.__auth_ptr: 0x118
-  __AUTH_CONST.__const: 0x8c08
+  __AUTH_CONST.__const: 0x8c60
   __AUTH_CONST.__objc_const: 0x770
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xa50
+  __AUTH.__data: 0xa58
   __DATA.__data: 0xb40
   __DATA.__common: 0x142
   __DATA.__bss: 0x1290
-  __DATA_DIRTY.__data: 0x1d0
+  __DATA_DIRTY.__data: 0x1c8
   __DATA_DIRTY.__bss: 0x73f0
   __DATA_DIRTY.__common: 0x1498
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8317
-  Symbols:   31630
-  CStrings:  19845
+  Functions: 8329
+  Symbols:   31656
+  CStrings:  19862
 
Symbols:
+ __ZN4llvm23SmallVectorTemplateBaseIPNS_7jitlink4EdgeELb1EE9push_backES3_
+ __ZN4llvm3orc17MachOFuncVariants12notifyFailedERNS0_29MaterializationResponsibilityE
+ __ZN4llvm3orc17MachOFuncVariants16modifyPassConfigERNS0_29MaterializationResponsibilityERNS_7jitlink9LinkGraphERNS4_17PassConfigurationE
+ __ZN4llvm3orc17MachOFuncVariants23notifyRemovingResourcesERNS0_8JITDylibEm
+ __ZN4llvm3orc17MachOFuncVariants27notifyTransferringResourcesERNS0_8JITDylibEmm
+ __ZN4llvm3orc17MachOFuncVariantsD0Ev
+ __ZN4llvm3orc17MachOFuncVariantsD1Ev
+ __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE11DestroyImplIZNS_3orc13MachOPlatform19MachOPlatformPlugin16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_6EEvPv
+ __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE15CallbacksHolderIZNS_3orc17MachOFuncVariants16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_0SE_vE9CallbacksE
+ __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE8CallImplIZNS_3orc17MachOFuncVariants16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_0EES2_PvS5_
+ __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE8MoveImplIZNS_3orc13MachOPlatform19MachOPlatformPlugin16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_6EEvPvSG_
+ __ZN4llvm7jitlink9LinkGraph21transferDefinedSymbolERNS0_6SymbolERNS0_5BlockEyNSt3__18optionalIyEE
+ __ZN5xojit5XOJIT18addNullableSymbolsEN4llvm8DenseSetINS1_3orc15SymbolStringPtrENS1_12DenseMapInfoIS4_vEEEE
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN4llvm3orc17MachOFuncVariants21lowerFunctionVariantsERNS3_29MaterializationResponsibilityERNS2_7jitlink9LinkGraphEE3$_0PPNS7_4EdgeELb0EEEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEb
+ __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZN4llvm3orc17MachOFuncVariants21lowerFunctionVariantsERNS3_29MaterializationResponsibilityERNS2_7jitlink9LinkGraphEE3$_0PPNS7_4EdgeEEEbT1_SF_T0_
+ __ZNSt3__16vectorIN4llvm3orc6shared19AllocActionCallPairENS_9allocatorIS4_EEE9push_backB8nn190102EOS4_
+ __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZN4llvm3orc17MachOFuncVariants21lowerFunctionVariantsERNS3_29MaterializationResponsibilityERNS2_7jitlink9LinkGraphEE3$_0PPNS7_4EdgeEEEjT1_SF_SF_T0_
+ __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZN4llvm3orc17MachOFuncVariants21lowerFunctionVariantsERNS3_29MaterializationResponsibilityERNS2_7jitlink9LinkGraphEE3$_0PPNS7_4EdgeEEEvT1_SF_SF_SF_T0_
+ __ZTVN4llvm3orc17MachOFuncVariantsE
- __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE11DestroyImplIZNS_3orc13MachOPlatform19MachOPlatformPlugin16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_8EEvPv
- __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE8CallImplIZNS_3orc13MachOPlatform19MachOPlatformPlugin16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE4$_11EES2_PvS5_
- __ZN4llvm6detail18UniqueFunctionBaseINS_5ErrorEJRNS_7jitlink9LinkGraphEEE8MoveImplIZNS_3orc13MachOPlatform19MachOPlatformPlugin16modifyPassConfigERNS8_29MaterializationResponsibilityES5_RNS3_17PassConfigurationEE3$_8EEvPvSG_
- __ZN4llvm8ExpectedINSt3__110unique_ptrINS_6object12SymbolicFileENS1_14default_deleteIS4_EEEEED2Ev
- __ZN5xojit5XOJIT26addNullableSymbolsFromPathEN4llvm8DenseSetINS1_3orc15SymbolStringPtrENS1_12DenseMapInfoIS4_vEEEE
CStrings:
+ " \"default\" variant for "
+ " contains extraneous edges in final record"
+ " does not contain a \"default\" entry"
+ " function variant record at "
+ " function variant symbol "
+ " function variant table at "
+ " is at non-zero offset "
+ " is missing target edge"
+ " is not a multiple of 64 bytes"
+ " points to empty variant table at "
+ " should be the final entry in the variant table"
+ " size of function variant table at "
+ " variant edge at "
+ " variant table for "
+ " within __func_variant block "
+ ", anonymous function variant symbol at "
+ "__LD,__func_variants"

```
