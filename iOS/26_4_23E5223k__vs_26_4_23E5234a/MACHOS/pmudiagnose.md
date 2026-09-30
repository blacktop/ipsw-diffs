## pmudiagnose

> `/usr/libexec/pmudiagnose/pmudiagnose`

```diff

 608.100.39.0.0
-  __TEXT.__text: 0x31b8
-  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__text: 0x30ac
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__cstring: 0x112d
+  __TEXT.__cstring: 0x3f0
   __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__cfstring: 0xa0
   __DATA.__data: 0x18

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 0C8D74C1-EDC3-36B3-9F1E-26283E6267EC
+  UUID: 655BC872-8519-36A8-9DB5-FF4E6B783ABA
   Functions: 43
-  Symbols:   332
-  CStrings:  59
+  Symbols:   331
+  CStrings:  50
 
Symbols:
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/PTDObject.o
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmu_spmi.o
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmudiagnose.o
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/ptd.o
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/utilities.o
+ /Library/Caches/com.apple.xbs/27437E69-B791-4E8F-B4F7-2FBEC70D8F9E/TemporaryDirectory.EitbTS/Sources/ApplePMUFirmware/tools/pmudiagnose/
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS2_EclB9nqe210106Ev
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
+ __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEE17__destruct_at_endB9nqe210106EPS1_
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorI6regionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__127__insertion_sort_incompleteB9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEbT1_S9_T0_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS3_EEED2B9nqe210106Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9nqe210106INS_9allocatorI6regionEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE16__destroy_vectorclB9nqe210106Ev
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE5clearB9nqe210106Ev
+ __ZNSt3__17__sort3B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEbT1_S9_S9_T0_
+ __ZNSt3__17__sort4B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B9nqe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9nqe210106IRP6regionS6_EEvOT_OT0_
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/PTDObject.o
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmu_spmi.o
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/pmudiagnose.o
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/ptd.o
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Binaries/ApplePMUFirmware/install/TempContent/Objects/build/pmudiagnose/obj/utilities.o
- /Library/Caches/com.apple.xbs/301115A1-66A3-4276-8563-8800637D5AEB/TemporaryDirectory.KLu4OC/Sources/ApplePMUFirmware/tools/pmudiagnose/
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS2_EclB9foe210106Ev
- __ZNSt12length_errorC1B9foe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
- __ZNSt3__114__split_bufferI6regionRNS_9allocatorIS1_EEE17__destruct_at_endB9foe210106EPS1_
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorI6regionEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB9foe210106EPKc
- __ZNSt3__127__insertion_sort_incompleteB9foe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionEEbT1_S9_T0_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI6regionEEPS3_EEED2B9foe210106Ev
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__134__uninitialized_allocator_relocateB9foe210106INS_9allocatorI6regionEEPS2_EEvRT_T0_S7_S7_
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE16__destroy_vectorclB9foe210106Ev
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE20__throw_length_errorB9foe210106Ev
- __ZNSt3__16vectorI6regionNS_9allocatorIS1_EEE5clearB9foe210106Ev
- __ZNSt3__17__sort3B9foe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEbT1_S9_S9_T0_
- __ZNSt3__17__sort4B9foe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort5B9foe210106INS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLi0EEEvT1_S9_S9_S9_S9_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9foe210106IRP6regionS6_EEvOT_OT0_
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
Functions:
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZ16get_ptmu_regionsjPK10__CFStringS4_E3$_0P6regionLb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb : 3552 -> 3284
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJlAugAfIrECCJ7d_zc6msCJMoitshmWd_2SXT0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"

```
