## AppleProResHWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResHWEncoder.videoencoder`

```diff

-501.4.0.0.0
-  __TEXT.__text: 0x21f30
+550.45.0.0.0
+  __TEXT.__text: 0x2076c
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__const: 0x74440
-  __TEXT.__gcc_except_tab: 0x35c
-  __TEXT.__cstring: 0x13f0
-  __TEXT.__oslogstring: 0x3bc3
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__const: 0x746a8
+  __TEXT.__gcc_except_tab: 0x350
+  __TEXT.__cstring: 0x2385
+  __TEXT.__oslogstring: 0x3e76
+  __TEXT.__unwind_info: 0x458
   __DATA_CONST.__got: 0x2d0
   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x188

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
-  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 9EA1E292-1FFE-3B00-BBC4-50C8BB4311FD
-  Functions: 450
-  Symbols:   1334
-  CStrings:  412
+  UUID: 805664A2-2020-36E9-903C-FA5A6930845B
+  Functions: 477
+  Symbols:   1396
+  CStrings:  436
 
Symbols:
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table51
+ _CVPixelBufferFillExtendedPixels
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ __Z18getEncodeStatsPtrsP20EncodeStatsBufOffs_sPPhS2_S2_S2_S2_.cold.1
+ __Z18getEncodeStatsPtrsP20EncodeStatsBufOffs_sPPhS2_S2_S2_S2_.cold.2
+ __Z23reportDecodeSessionInfojjjjjhjjbbjNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbjNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __Z28GetTargetCompressedFrameSizejjPjbjf
+ __Z28GetTargetCompressedFrameSizejjPjbjf.cold.1
+ __ZL25ProResEncoder_EncodeFrameP20OpaqueVTVideoEncoderP25OpaqueVTVideoEncoderFrameP10__CVBuffer6CMTimeS5_PK14__CFDictionaryPj.cold.34
+ __ZL25ProResEncoder_EncodeFrameP20OpaqueVTVideoEncoderP25OpaqueVTVideoEncoderFrameP10__CVBuffer6CMTimeS5_PK14__CFDictionaryPj.cold.35
+ __ZL34setFrameHeaderToOriginalDimensionsPhP10__CVBufferj
+ __ZL37ProResEncoder_AdjustMaxSizeMultiplierP27ProResEncoderPrivateStoragejj
+ __ZL40ProResEncoder_AdjustTargetSizeMultiplierP27ProResEncoderPrivateStoragejj
+ __ZN19ProResFrameReceiver12P1ParseFrameEP16DoubleEncodeInfoP15ProResFrameInfoP14QpmAndEstStatsPh.cold.2
+ __ZN19ProResFrameReceiver13getNumHWHangsEv
+ __ZN19ProResFrameReceiver14P2PrepareFrameEP16DoubleEncodeInfoP15ProResFrameInfoP14QpmAndEstStatsPhRm.cold.2
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__111__sift_downB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
+ __ZNSt3__111__sift_downB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_OT0_NS_15iterator_traitsIS8_E15difference_typeES8_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
+ __ZNSt3__116__insertion_sortB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_T0_
+ __ZNSt3__116__insertion_sortB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_T0_
+ __ZNSt3__117__floyd_sift_downB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEET1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEET1_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorINS_4pairIttEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIPPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__partial_sort_implB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEESB_EET1_SC_SC_T2_OT0_
+ __ZNSt3__119__partial_sort_implB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEES7_EET1_S8_S8_T2_OT0_
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__126__insertion_sort_unguardedB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_T0_
+ __ZNSt3__126__insertion_sort_unguardedB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEbT1_SC_T0_
+ __ZNSt3__127__insertion_sort_incompleteB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEbT1_S8_T0_
+ __ZNSt3__131__partition_with_equals_on_leftB9foe210106INS_17_ClassicAlgPolicyENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEERNS_6__lessIvvEEEET0_SC_SC_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB9foe210106INS_17_ClassicAlgPolicyEPNS_4pairIttEERNS_6__lessIvvEEEET0_S8_S8_T1_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__132__partition_with_equals_on_rightB9foe210106INS_17_ClassicAlgPolicyENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEERNS_6__lessIvvEEEENS4_IT0_bEESC_SC_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB9foe210106INS_17_ClassicAlgPolicyEPNS_4pairIttEERNS_6__lessIvvEEEENS2_IT0_bEES8_S8_T1_
+ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE26__maybe_remove_front_spareB9foe210106Eb
+ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE9pop_frontEv
+ __ZNSt3__15dequeIPvNS_9allocatorIS1_EEED2B9foe210106Ev
+ __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE16__init_with_sizeB9foe210106IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB9foe210106IPhS5_EENS_11__wrap_iterIS5_EENS6_IPKhEET_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__17__sort3B9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEELi0EEEbT1_SC_SC_T0_
+ __ZNSt3__17__sort3B9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEELi0EEEbT1_S8_S8_T0_
+ __ZNSt3__17__sort5B9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEELi0EEEvT1_SC_SC_SC_SC_T0_
+ __ZNSt3__17__sort5B9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEELi0EEEvT1_S8_S8_S8_S8_T0_
+ __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
+ __ZNSt3__19__sift_upB9foe210106INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ____Z23reportDecodeSessionInfojjjjjhjjbbjNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
+ ____Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbjNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
+ ___block_descriptor_tmp.32
- GCC_except_table11
- GCC_except_table30
- GCC_except_table35
- GCC_except_table41
- GCC_except_table44
- GCC_except_table45
- GCC_except_table49
- _IOSurfaceGetBitDepthOfComponentOfPlane
- __Z23reportDecodeSessionInfojjjjjhjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
- __ZL50ProResEncoder_AdjustBitRateAndTargetSizeMultiplierP27ProResEncoderPrivateStoragejj
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__111__sift_downB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_OT0_NS_15iterator_traitsISC_E15difference_typeESC_
- __ZNSt3__111__sift_downB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_OT0_NS_15iterator_traitsIS8_E15difference_typeES8_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
- __ZNSt3__116__insertion_sortB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_T0_
- __ZNSt3__116__insertion_sortB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_T0_
- __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEET1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEET1_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIttEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__partial_sort_implB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEESB_EET1_SC_SC_T2_OT0_
- __ZNSt3__119__partial_sort_implB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEES7_EET1_S8_S8_T2_OT0_
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__126__insertion_sort_unguardedB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_T0_
- __ZNSt3__126__insertion_sort_unguardedB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEbT1_SC_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEbT1_S8_T0_
- __ZNSt3__131__partition_with_equals_on_leftB8ne200100INS_17_ClassicAlgPolicyENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEERNS_6__lessIvvEEEET0_SC_SC_T1_
- __ZNSt3__131__partition_with_equals_on_leftB8ne200100INS_17_ClassicAlgPolicyEPNS_4pairIttEERNS_6__lessIvvEEEET0_S8_S8_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne200100INS_17_ClassicAlgPolicyENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEERNS_6__lessIvvEEEENS4_IT0_bEESC_SC_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8ne200100INS_17_ClassicAlgPolicyEPNS_4pairIttEERNS_6__lessIvvEEEENS2_IT0_bEES8_S8_T1_
- __ZNSt3__15dequeIPvNS_9allocatorIS1_EEE26__maybe_remove_front_spareB8ne200100Eb
- __ZNSt3__15dequeIPvNS_9allocatorIS1_EEED2B8ne200100Ev
- __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE16__init_with_sizeB8ne200100IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorINS_4pairIttEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB8ne200100IPhS5_EENS_11__wrap_iterIS5_EENS6_IPKhEET_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEELi0EEEvT1_SC_SC_SC_T0_
- __ZNSt3__17__sort4B8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEELi0EEEvT1_S8_S8_S8_T0_
- __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_16reverse_iteratorINS_11__wrap_iterIPNS_4pairIttEEEEEEEEvT1_SC_OT0_NS_15iterator_traitsISC_E15difference_typeE
- __ZNSt3__19__sift_upB8ne200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPNS_4pairIttEEEEvT1_S8_OT0_NS_15iterator_traitsIS8_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ____Z23reportDecodeSessionInfojjjjjhjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
- ____Z23reportEncodeSessionInfojjjjjhbjjjjbjjbbNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_block_invoke
- ___block_descriptor_tmp.31
- __os_crash
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU0ugDgjjCGqCxFoF91gpVVGmaUFc4b3iWZ6Qk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "AppleProResHW (0x%x): %s(): setFrameHeaderToOriginalDimensions: Invalid parameters\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Encode stats buffers were not allocated\n\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error getting max compression size excluding alpha\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Error getting target compressed frame size\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): F# %d: FrameParse error, the bitstream is corrupted, %d\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to get encode stats on first DE pass\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Failed to get encode stats on second DE pass\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Invalid surface ID %d\n\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): MaxPixelsPerFrame (%llu) not supported\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported feature: RAW Compressed\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): planeCount %lu is not 0, 1 or 4 for RAW full resolution encoding case.\n"
+ "GetTargetCompressedFrameSize"
+ "HWHangs"
+ "V63"
+ "V64"
+ "WARNING AppleProResHW (0x%x): %d: %s(): input cfa_pattern %d does not match with output format CFA/bayer_pattern [0,%d]\n"
+ "getEncodeStatsPtrs"
+ "setFrameHeaderToOriginalDimensions"
- "AppleProResHW (0x%x): %s(): F# %d: FrameParse error, the bitstream is corrupted, %d"
- "ERROR AppleProResHW (0x%x): %d: %s(): Error get max compression size excluding alpha\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): MaxPixelsPerFrame (%d) not supported\n"
- "ERROR AppleProResHW (0x%x): %d: %s(): planeCount %lu is not 0 or 4 for RAW full resolution encoding case.\n"
- "ERROR: AppleProResHW (0x%x): %s(): F# %d: FrameParse error, the bitstream is corrupted, crashing system\n"

```
