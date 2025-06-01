## pmudiagnose

> `/usr/libexec/pmudiagnose/pmudiagnose`

```diff

-371.40.3.0.0
-  __TEXT.__text: 0x13e0
-  __TEXT.__auth_stubs: 0x310
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__cstring: 0x38f
-  __TEXT.__unwind_info: 0xe4
-  __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x190
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__cfstring: 0x60
+377.100.56.0.0
+  __TEXT.__text: 0x3140
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__cstring: 0x412
+  __TEXT.__unwind_info: 0x144
+  __TEXT.__eh_frame: 0x4c
+  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__cfstring: 0xa0
   __DATA.__data: 0x18
   __DATA.__common: 0x5
   __DATA.__bss: 0x8

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 48A99C43-187D-3B78-AEBE-8F6D387861A9
-  Functions: 22
-  Symbols:   213
-  CStrings:  44
+  UUID: 50423A7C-C729-3286-8CE4-4D451F47BB9E
+  Functions: 45
+  Symbols:   335
+  CStrings:  51
 
Symbols:
+ GCC_except_table18
+ GCC_except_table3
+ _CFDataGetBytes
+ _CFDictionaryGetCount
+ _CFDictionaryGetKeysAndValues
+ _CFStringCreateWithSubstring
+ _CFStringGetCString
+ _CFStringGetLength
+ _CFStringGetMaximumSizeForEncoding
+ _CFStringHasPrefix
+ _CFStringHasSuffix
+ _IORegistryEntryCreateCFProperties
+ __Z16get_ptmu_regionsjPK10__CFStringS1_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI6regionEENS_16reverse_iteratorIPS2_EEEclB8ue170006Ev
+ __ZNKSt3__16vectorI6regionNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEE17__destruct_at_endB8ue170006EPS1_
+ __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI6regionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__124__sort5_maybe_branchlessB8ue170006INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEENS_9enable_ifIXntsr21__use_branchless_sortIT0_T1_EE5valueEvE4typeESB_SB_SB_SB_SB_SA_
+ __ZNSt3__127__insertion_sort_incompleteB8ue170006INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEbT1_S9_T0_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI6regionEENS_16reverse_iteratorIPS3_EEEEED2B8ue170006Ev
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorI6regionEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE13__vdeallocateEv
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE7__clearB8ue170006Ev
+ __ZNSt3__17__sort3B8ue170006INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEjT1_S9_S9_T0_
+ __ZNSt3__17__sort4B8ue170006INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEvT1_S9_S9_S9_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ue170006IRP6regionS5_EEvOT_OT0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ue170006IRP6regionS6_EEvOT_OT0_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ __ZTISt20bad_array_new_length
+ _fwrite
+ _malloc_type_calloc
+ _strcmp
- GCC_except_table6
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__19to_stringEi
CStrings:
+ "\n\t%s:"
+ "ERROR: IORegistryEntryCreateCFProperties failed, rc=0x%x\n"
+ "ERROR: malloc failed\n"
+ "ERROR: out of memory\n"
+ "ERROR: string conversion failed\n"
+ "ptmu-"
+ "vector"
- "\n\treg-%d:"
- "ptmu-region-"

```
