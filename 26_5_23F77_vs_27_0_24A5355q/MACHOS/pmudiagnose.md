## pmudiagnose

> `/usr/libexec/pmudiagnose/pmudiagnose`

```diff

-608.100.39.0.0
-  __TEXT.__text: 0x30ac
+727.0.0.0.0
+  __TEXT.__text: 0x30c0
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__cstring: 0x3f0
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__cstring: 0x3ef
   __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__cfstring: 0xa0
   __DATA.__data: 0x18
   __DATA.__common: 0x5
   __DATA.__bss: 0x8

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C827605F-9B93-3E1B-BC8F-309F303E07A2
+  UUID: 46FA401C-266E-3A32-9214-FA72CABDFCD7
   Functions: 43
-  Symbols:   331
+  Symbols:   332
   CStrings:  50
 
Symbols:
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/PTDObject.o
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmu_spmi.o
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmudiagnose.o
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/ptd.o
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/utilities.o
+ /Library/Caches/com.apple.xbs/680EC70B-8FB6-4AD9-B754-4A4A40BB8E60/TemporaryDirectory.gDffnG/Sources/ApplePMUFirmware/tools/pmudiagnose/
+ GCC_except_table4
+ GCC_except_table6
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS2_EclB9fqe220100Ev
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEE17__destruct_at_endB9fqe220100EPS1_
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorI6regionEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__127__insertion_sort_incompleteB9fqe220100INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEbT1_S9_T0_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS3_EEED2B9fqe220100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220100INS_9allocatorI6regionEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220100Ev
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE5clearB9fqe220100Ev
+ __ZNSt3__17__sort3B9fqe220100INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEbT1_S9_S9_T0_
+ __ZNSt3__17__sort4B9fqe220100INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B9fqe220100INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9fqe220100IRP6regionS6_EEvOT_OT0_
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/PTDObject.o
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmu_spmi.o
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmudiagnose.o
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/ptd.o
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/utilities.o
- /Library/Caches/com.apple.xbs/F41518CE-AED0-4595-A401-1407B49BBD9A/TemporaryDirectory.Pbl2JQ/Sources/ApplePMUFirmware/tools/pmudiagnose/
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS2_EclB9nqe210106Ev
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI6regionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEbT1_S9_T0_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS3_EEED2B9nqe210106Ev
- __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI6regionEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE5clearB9nqe210106Ev
- __ZNSt3__17__sort3B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEbT1_S9_S9_T0_
- __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_S9_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9nqe210106IRP6regionS6_EEvOT_OT0_
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v

```
