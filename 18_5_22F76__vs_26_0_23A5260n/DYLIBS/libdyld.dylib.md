## libdyld.dylib

> `/usr/lib/system/libdyld.dylib`

```diff

-1285.17.0.0.0
-  __TEXT.__text: 0x27f0c
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__const: 0x690
-  __TEXT.__cstring: 0x4916
+1318.0.0.0.0
+  __TEXT.__text: 0x28834
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__const: 0x600
+  __TEXT.__cstring: 0x47be
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x14a8
+  __DATA_CONST.__const: 0x1588
   __DATA_CONST.__helper: 0x8
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x1860
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__const: 0x1828
   __AUTH.__data: 0x8
-  __DATA.__crash_info: 0x40
-  __DATA.__data: 0xf8
+  __DATA.__crash_info: 0x148
+  __DATA.__data: 0x120
   __DATA.__common: 0x19
   __DATA.__bss: 0x1098
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: A6DE89C4-21C2-3694-B7ED-3D3F98B3DAC7
-  Functions: 1082
-  Symbols:   2817
-  CStrings:  545
+  UUID: AB3A1E46-6BFE-3039-95AB-E09A97E738D1
+  Functions: 1047
+  Symbols:   2762
+  CStrings:  534
 
Symbols:
+ __Z28macho_best_slice_fd_internaliN6mach_o8PlatformERKNS_19GradedArchitecturesES3_bU13block_pointerFvPK11mach_headerymE
+ __ZL7hasFilePKc
+ __ZN3lsl5BTreeINS_9UniquePtrIN5dyld45Atlas5ImageEEENSt3__14lessIS5_EELb0EE6insertEOS5_
+ __ZN5dyld317OverflowSafeArrayIcLy4294967295EE6resizeEy
+ __ZN5dyld317OverflowSafeArrayIcLy4294967295EE6resizeEy.cold.1
+ __ZN5dyld45Atlas5ImageD2Ev
+ __ZN6mach_o12Architecture10arm64e_oldE
+ __ZN6mach_o12Architecture5arm64E
+ __ZN6mach_o12Architecture6arm64eE
+ __ZN6mach_o12Architecture9arm64_altE
+ __ZN6mach_o12Architecture9arm64e_v1E
+ __ZN6mach_o12ArchitectureC1EPK11fat_arch_64
+ __ZN6mach_o12ArchitectureC1EPK8fat_arch
+ __ZN6mach_o19GradedArchitectures11currentLoadEbb
+ __ZN6mach_o19GradedArchitectures11load_arm64eE
+ __ZN6mach_o19GradedArchitectures13currentLaunchEPKc
+ __ZN6mach_o19GradedArchitectures19load_arm64e_keysOffE
+ __ZN6mach_o19GradedArchitectures24load_arm64e_osBinaryOnlyE
+ __ZN6mach_o19GradedArchitectures32load_arm64e_keysOff_osBinaryOnlyE
+ __ZN6mach_o9Universal11isUniversalENSt3__14spanIKhLm18446744073709551615EEE
+ __ZN6mach_oL12archs_arm64eE
+ __ZN6mach_oL20archs_arm64e_keysOffE
+ __ZNK6mach_o12Architecture22usesx86_64InstructionsEv
+ __ZNK6mach_o13ChainedFixups13PointerFormat14badBindOrdinalERKNS_5FixupE
+ __ZNK6mach_o19GradedArchitectures12isCompatibleENS_12ArchitectureEb
+ __ZNK6mach_o19GradedArchitectures18hasCompatibleSliceENSt3__14spanIKNS_12ArchitectureELm18446744073709551615EEEbRj
+ __ZNK6mach_o6Header10hasSectionE7CStringS1_b
+ __ZNK6mach_o6Header12uses16KPagesEv
+ __ZNK6mach_o6Policy25enforceUniqueSegmentNamesEv
+ __ZNK6mach_o9Universal10validSliceENS_12ArchitectureEyy
+ __ZNK6mach_o9Universal12forEachSliceEU13block_pointerFvNS0_5SliceERbE
+ __ZNK6mach_o9Universal12forEachSliceEU13block_pointerFvNS_12ArchitectureEyyRbE
+ __ZNK6mach_o9Universal5validEy
+ __ZNK6mach_o9Universal9bestSliceERKNS_19GradedArchitecturesEbRNS0_5SliceE
+ __ZNKSt3__111__copy_implclB8nn200100IPhS2_NS_20back_insert_iteratorIN3lsl6VectorIcEEEEEENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB8nn200100EPKc
+ __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB8nn200100EmmS3_
+ __ZNSt3__123__lower_bound_bisectingB8nn200100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPPKcEES4_NS_10__identityEN3lsl20ConstCharStarCompareEEET0_SA_RKT1_NS_15iterator_traitsISA_E15difference_typeERT3_RT2_
+ __ZNSt3__18optionalIyE4swapB8nn200100ERS1_
+ ___Block_byref_object_copy_.65
+ ___Block_byref_object_dispose_.66
+ ____ZNK6mach_o6Header10hasSectionE7CStringS1_b_block_invoke
+ ____ZNK6mach_o9Universal12forEachSliceEU13block_pointerFvNS0_5SliceERbE_block_invoke
+ ____ZNK6mach_o9Universal5validEy_block_invoke
+ ____ZNK6mach_o9Universal9bestSliceERKNS_19GradedArchitecturesEbRNS0_5SliceE_block_invoke
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.282
+ ___block_descriptor_tmp.290
+ ___block_descriptor_tmp.292
+ ___block_descriptor_tmp.297
+ ___block_descriptor_tmp.299
+ ___block_descriptor_tmp.309
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.83
+ ___block_descriptor_tmp.88
+ ___block_descriptor_tmp.95
+ ___block_descriptor_tmp.98
+ ___block_literal_global.21
+ ___block_literal_global.23
+ _arc4random_uniform
+ _geteuid
+ _macho_for_each_runnable_arch_name
- __Z28macho_best_slice_fd_internaliN6mach_o8PlatformERKN5dyld311GradedArchsES4_bU13block_pointerFvPK11mach_headerymE
- __ZN3lsl10OrderedMapIjN5dyld45Atlas7Process19ProcessUpdateRecordENSt3__14lessIjEEE6insertEONS5_4pairIKjS4_EE
- __ZN3lsl10OrderedMapIjN5dyld45Atlas7Process21ProcessNotifierRecordENSt3__14lessIjEEE6insertEONS5_4pairIKjS4_EE
- __ZN3lsl10OrderedSetINS_9UniquePtrIN5dyld45Atlas5ImageEEENSt3__14lessIS5_EEE6insertEOS5_
- __ZN5dyld311GradedArchs12forCurrentOSEbb
- __ZN5dyld311GradedArchs14arm64e_keysoffE
- __ZN5dyld311GradedArchs15launchCurrentOSEPKc
- __ZN5dyld311GradedArchs17arm64e_keysoff_pbE
- __ZN5dyld311GradedArchs6arm64eE
- __ZN5dyld311GradedArchs9arm64e_pbE
- __ZN5dyld317OverflowSafeArrayIcLy4294967295EE7reserveEy
- __ZN5dyld317OverflowSafeArrayIcLy4294967295EE7reserveEy.cold.1
- __ZN5dyld317OverflowSafeArrayIcLy4294967295EEixEy
- __ZN5dyld45Atlas5ImageD1Ev
- __ZN6mach_o8Platform5Epoch8fall2024E
- __ZNK5dyld311GradedArchs5gradeEjjb
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.10
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.11
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.12
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.13
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.14
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.15
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.16
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.3
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.4
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.5
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.6
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.7
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.8
- __ZNK6mach_o28PointerFormat_Generic_arm64e15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.9
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_3215writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_3215writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_3215writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.3
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_3215writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.4
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_3215writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.5
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.3
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.4
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.5
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.6
- __ZNK6mach_o33PointerFormat_DYLD_CHAINED_PTR_6415writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.7
- __ZNK6mach_o39PointerFormat_DYLD_CHAINED_PTR_32_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o39PointerFormat_DYLD_CHAINED_PTR_32_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o42PointerFormat_DYLD_CHAINED_PTR_32_FIRMWARE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o42PointerFormat_DYLD_CHAINED_PTR_32_FIRMWARE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o46PointerFormat_DYLD_CHAINED_PTR_64_KERNEL_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o46PointerFormat_DYLD_CHAINED_PTR_64_KERNEL_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.3
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.4
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.5
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.6
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.7
- __ZNK6mach_o47PointerFormat_DYLD_CHAINED_PTR_ARM64E_SEGMENTED15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.8
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.3
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_ARM64E_SHARED_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.4
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_X86_64_KERNEL_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.1
- __ZNK6mach_o50PointerFormat_DYLD_CHAINED_PTR_X86_64_KERNEL_CACHE15writeChainEntryERKNS_5FixupEPKvyNSt3__14spanIPKNS_13MappedSegmentELm18446744073709551615EEE.cold.2
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPhS4_NS_20back_insert_iteratorIN3lsl6VectorIcEEEEEENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE11starts_withB8nn190102EPKc
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareB8nn190102EmmS3_
- __ZNSt3__123__lower_bound_bisectingB8nn190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPPKcEES4_NS_10__identityEN3lsl20ConstCharStarCompareEEET0_SA_RKT1_NS_15iterator_traitsISA_E15difference_typeERT3_RT2_
- __ZNSt3__18optionalIyE4swapB8nn190102ERS1_
- ___Block_byref_object_copy_.63
- ___Block_byref_object_dispose_.64
- ____Z28macho_best_slice_fd_internaliN6mach_o8PlatformERKN5dyld311GradedArchsES4_bU13block_pointerFvPK11mach_headerymE_block_invoke
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.103
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.279
- ___block_descriptor_tmp.287
- ___block_descriptor_tmp.289
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.52
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.86
- ___block_descriptor_tmp.93
- ___block_descriptor_tmp.94
- ___block_literal_global.19
- ___block_literal_global.22
- ___copy_helper_block_8_80c22_ZTSN6mach_o8PlatformE
- ___destroy_helper_block_8_80
- _wmemchr
CStrings:
+ "%s slice extends beyond end of file"
+ "/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64"
+ "/System/Cryptexes/OS/System/Library/Caches/com.apple.dyld/dyld_shared_cache_arm64e"
+ "Xcode"
+ "__playground"
+ "addend (%lld) cannot fit in fixup at %.*s+0x%0lX"
+ "apple-hwtrace"
+ "bind ordinal (%u) too large in fixup at %.*s+0x%0lX"
+ "cpu type/subtype in slice (%s) does not match fat header (%s)"
+ "distance between fixups (%ld) is not encodable in chain for fixup at %.*s+0x%0lX"
+ "duplicate %s slices"
+ "duplicate segment name '%s'"
+ "fat file has too many slices (%d)"
+ "fat file too short"
+ "file does not start with FAT_MAGIC"
+ "firmware format does not support binds"
+ "overlapping slices"
+ "segIndex (%d) and segOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX"
+ "shared cache fixup formate does not support binds"
+ "slice headers extend beyond end of file"
+ "target vm address not in any segment"
+ "thumbv6m"
+ "v40@?0{Architecture=ii}8Q16Q24^B32"
+ "v40@?0{Slice={Architecture=ii}{span<const unsigned char, 18446744073709551615UL>=*Q}}8^B32"
+ "vmAddress (0x%0llX) cannot fit in fixup at %.*s+0x%0lX"
+ "vmOffset (0x%0llX) cannot fit in fixup at %.*s+0x%0lX"
- "!fixup.isBind && \"firmware format does not support binds\""
- "!fixup.isBind && \"shared cache does not support binds\""
- "ChainedFixups.cpp"
- "__PRELINK_INFO"
- "authBind24Ptr->next*stride() == delta"
- "authBind24Ptr->ordinal == fixup.bind.bindOrdinal"
- "authBindPtr->next*stride() == delta"
- "authBindPtr->ordinal == fixup.bind.bindOrdinal"
- "authRebasePtr->next*8 == delta"
- "authRebasePtr->next*stride() == delta"
- "authRebasePtr->runtimeOffset == fixup.rebase.targetVmOffset"
- "authRebasePtr->target == fixup.rebase.targetVmOffset"
- "authRebasePtr->targetSegIndex == segIndex"
- "authRebasePtr->targetSegOffset == segOffset"
- "bind24Ptr->next*stride() == delta"
- "bind24Ptr->ordinal == fixup.bind.bindOrdinal"
- "bindPtr->addend == fixup.bind.embeddedAddend"
- "bindPtr->next*4 == delta"
- "bindPtr->next*stride() == delta"
- "bindPtr->ordinal == fixup.bind.bindOrdinal"
- "fixup.bind.embeddedAddend == 0"
- "found && \"target vm address not in any segment\""
- "rebasePtr->next == delta"
- "rebasePtr->next*4 == delta"
- "rebasePtr->next*8 == delta"
- "rebasePtr->next*stride() == delta"
- "rebasePtr->target == (low56 + (this->unauthRebaseIsVmAddr() ? preferedLoadAddress : 0))"
- "rebasePtr->target == (low56+preferedLoadAddress)"
- "rebasePtr->target == fixup.rebase.targetVmOffset"
- "rebasePtr->target == low56"
- "rebasePtr->target == target"
- "rebasePtr->targetSegIndex == segIndex"
- "rebasePtr->targetSegOffset == segOffset"
- "sandboxd"
- "signExtendedAddend(bind24Ptr) == fixup.bind.embeddedAddend"
- "signExtendedAddend(bindPtr) == fixup.bind.embeddedAddend"
- "writeChainEntry"

```
