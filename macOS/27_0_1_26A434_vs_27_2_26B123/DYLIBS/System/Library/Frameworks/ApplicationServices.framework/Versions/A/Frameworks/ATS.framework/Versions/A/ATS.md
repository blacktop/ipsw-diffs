## ATS

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/ATS`

```diff

-601.0.0.0.0
-  __TEXT.__text: 0x19528
-  __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x2cf5
-  __TEXT.__ustring: 0xe34
+603.0.0.0.0
+  __TEXT.__text: 0x26b94
+  __TEXT.__const: 0x798
+  __TEXT.__cstring: 0x4a42
+  __TEXT.__ustring: 0xfb2
   __TEXT.__gcc_except_tab: 0x7cc
   __TEXT.__oslogstring: 0x3
   __TEXT.__dlopen_cstrs: 0x2e1
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x3a8
-  __AUTH_CONST.__cfstring: 0x1780
+  __AUTH_CONST.__cfstring: 0x1f80
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH_CONST.__auth_ptr: 0x0
   __DATA.__data: 0x2a8
   __DATA.__crash_info: 0x148

   - /usr/lib/libcompression.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 689
-  Symbols:   1218
-  CStrings:  330
+  Functions: 788
+  Symbols:   1382
+  CStrings:  600
 
Symbols:
+ GetFontFormat
+ _CFBooleanGetTypeID
+ _CFDataCreate
+ _CFDictionaryGetCount
+ _CFEqual
+ _CFGetTypeID
+ _CFPropertyListCreateData
+ _CopyFontKindFormatNameForURL
+ _FontKindName
+ _GetFontFormat
+ _GetWOFFFlavor
+ _IsResourceForkLWFNFile
+ _IsType1File
+ _LocalType1Validate
+ _RunningAsAgent
+ _Type1CategoryDisplayName
+ _Type1FontKindName
+ _Type1SniffCFFURL
+ _Type1SniffResourceForkLWFNURL
+ _Type1SniffURL
+ _Type1ValidateURL
+ _ValidateAllRequested
+ _ZL26CGFontGetParserFontProcPtrP6CGFont
+ _ZL29CTFontCopyGraphicsFontProcPtrPK8__CTFontPPK18__CTFontDescriptor
+ _ZL48CTFontManagerCreateFontDescriptorsFromURLProcPtrPK7__CFURL
+ __CTFontCreateWithFontDescriptor
+ __CTFontDescriptorsFromURL
+ __ZL26CGFontGetParserFontProcPtrP6CGFont
+ __ZL28_CreateType1ValidationReportPK10__CFStringPK9__CFArrayS1_
+ __ZL29CTFontCopyGraphicsFontProcPtrPK8__CTFontPPK18__CTFontDescriptor
+ __ZL32CopyPosingFailedValidationReportPK10__CFStringS1_
+ __ZL48CTFontManagerCreateFontDescriptorsFromURLProcPtrPK7__CFURL
+ __ZN12_GLOBAL__N_114ReadEntireFileEPKcRNSt3__16vectorIhNS2_9allocatorIhEEEE
+ __ZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNSt3__16vectorIhNS2_9allocatorIhEEEE
+ __ZN12_GLOBAL__N_16Cursor7ReadIntERl
+ __ZN12_GLOBAL__N_16Cursor9ReadTokenEv
+ __ZN12_GLOBAL__N_17DecryptEPKhmtiRNSt3__16vectorIhNS2_9allocatorIhEEEE
+ __ZN12_GLOBAL__N_18Type1Doc11CIDNamedIntERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKcRl
+ __ZN12_GLOBAL__N_18Type1Doc12ContainerErrERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc13MMCountTokensERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc13RunCharStringERKNSt3__16vectorIhNS1_9allocatorIhEEEERNS2_IlNS3_IlEEEERbSB_RiiRNS1_12basic_stringIcNS1_11char_traitsIcEENS3_IcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc16CheckPrivateDictEv
+ __ZN12_GLOBAL__N_18Type1Doc16MMCountSubArraysERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEi
+ __ZN12_GLOBAL__N_18Type1Doc3ErrERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc4CritERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc4WarnERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc7MMArrayERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKc
+ __ZN12_GLOBAL__N_18Type1Doc8CritSafeERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN12_GLOBAL__N_18Type1Doc8ParsePFAEv
+ __ZN12_GLOBAL__N_18Type1Doc8ValidateEv
+ __ZN12_GLOBAL__N_18Type1Doc9HexDecodeERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEmmRNS1_6vectorIhNS5_IhEEEE
+ __ZN5woff214WOFF2StringOut4SizeEv
+ __ZN5woff214WOFF2StringOut5WriteEPKvm
+ __ZN5woff214WOFF2StringOut5WriteEPKvmm
+ __ZN5woff214WOFF2StringOutC1EPNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN5woff214WOFF2StringOutD0Ev
+ __ZN5woff214WOFF2StringOutD1Ev
+ __ZNK12_GLOBAL__N_18Type1Doc10IsPutTokenERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNK12_GLOBAL__N_18Type1Doc13IsReaderTokenERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNKSt3__111__copy_implclB9nqn220106IPNS_6vectorIhNS_9allocatorIhEEEES6_S6_Li0EEENS_4pairIT_T1_EES8_T0_S9_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9nqn220106EPKcm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS_6vectorIhNS_9allocatorIhEEEEE3$_0PZNS2_15LWFNCollectPOSTES4_mS9_E3ResLb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9nqn220106Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqn220106ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB9nqn220106EPS6_
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEED2Ev
+ __ZNSt3__114__split_bufferINS_6vectorIhNS_9allocatorIhEEEERNS2_IS4_EEE17__destruct_at_endB9nqn220106EPS4_
+ __ZNSt3__114__split_bufferINS_6vectorIhNS_9allocatorIhEEEERNS2_IS4_EEED2Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorIN12_GLOBAL__N_18Type1Doc9CharEntryEEEE7destroyB9nqn220106IS4_Li0EEEvRS5_PT_
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorIN12_GLOBAL__N_17FindingEEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16allocator_traitsIS7_EEEENS_19__allocation_resultINT0_7pointerENSB_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorINS_6vectorINS2_IhNS1_IhEEEENS1_IS4_EEEEEENS_16allocator_traitsIS7_EEEENS_19__allocation_resultINT0_7pointerENSB_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorINS_6vectorIhNS1_IhEEEEEENS_16allocator_traitsIS5_EEEENS_19__allocation_resultINT0_7pointerENS9_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorIiEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorIlEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9nqn220106INS_9allocatorImEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__127__insertion_sort_incompleteB9nqn220106INS_17_ClassicAlgPolicyERZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS_6vectorIhNS_9allocatorIhEEEEE3$_0PZNS2_15LWFNCollectPOSTES4_mS9_E3ResEEbT1_SE_T0_
+ __ZNSt3__130__uninitialized_allocator_copyB9nqn220106INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9nqn220106INS_9allocatorINS_6vectorIhNS1_IhEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE18__construct_at_endIPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE5clearB9nqn220106Ev
+ __ZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE9push_backB9nqn220106EOS2_
+ __ZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEED1B9nqn220106Ev
+ __ZNSt3__16vectorIN12_GLOBAL__N_18Type1Doc9CharEntryENS_9allocatorIS3_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS0_INS0_IhNS_9allocatorIhEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorINS0_INS0_IhNS_9allocatorIhEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB9nqn220106Ev
+ __ZNSt3__16vectorINS0_INS0_IhNS_9allocatorIhEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS0_INS0_IhNS_9allocatorIhEEEENS1_IS3_EEEENS1_IS5_EEEC2B9nqn220106Em
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE13__vdeallocateEv
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE16__destroy_vectorclB9nqn220106Ev
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyEPS3_S8_EEvT0_T1_l
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE5clearB9nqn220106Ev
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE6resizeEm
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE13__vdeallocateEv
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB9nqn220106Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyEPKS6_SC_EEvT0_T1_l
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB9nqn220106Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backB9nqn220106ERKS6_
+ __ZNSt3__16vectorIZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS0_IhNS_9allocatorIhEEEEE3ResNS4_IS8_EEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPKhEES9_EEvT0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPhEES8_EEvT0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyEPKhS7_EEvT0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__assign_with_sizeB9nqn220106INS_17_ClassicAlgPolicyEPhS6_EEvT0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB9nqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPhEES8_EES8_NS6_IPKhEET0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE18__insert_with_sizeB9nqn220106INS_17_ClassicAlgPolicyEPKhS7_EENS_11__wrap_iterIPhEENS8_IS7_EET0_T1_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE24__emplace_back_slow_pathIJhEEEPhDpOT_
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE6resizeEm
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE7reserveEm
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B9nqn220106INS_11__wrap_iterIPKhEELi0EEET_S9_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE24__emplace_back_slow_pathIJRKlEEEPlDpOT_
+ __ZNSt3__16vectorIlNS_9allocatorIlEEE24__emplace_back_slow_pathIJlEEEPlDpOT_
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB9nqn220106Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE24__emplace_back_slow_pathIJRKmEEEPmDpOT_
+ __ZNSt3__17__sort5B9nqn220106INS_17_ClassicAlgPolicyERZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS_6vectorIhNS_9allocatorIhEEEEE3$_0PZNS2_15LWFNCollectPOSTES4_mS9_E3ResLi0EEEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__19to_stringEi
+ __ZNSt3__19to_stringEl
+ __ZNSt3__19to_stringEm
+ __ZNSt3__1plB9nqn220106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEOS9_PKS6_
+ __ZNSt3__1plB9nqn220106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_OS9_
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTVN5woff214WOFF2StringOutE
+ __ZZN12_GLOBAL__N_118Type1RenderMessageE14Type1ContainerRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE7kTopics
+ __ZZN12_GLOBAL__N_18Type1Doc15CheckHintArraysERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE11kBlueArrays
+ __ZZN12_GLOBAL__N_18Type1Doc15CheckHintArraysERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE11kStemArrays
+ __ZZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE12emplace_backIJS2_EEERS2_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorIN12_GLOBAL__N_18Type1Doc9CharEntryENS_9allocatorIS3_EEE12emplace_backIJS3_EEERS3_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorIZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS0_IhNS_9allocatorIhEEEEE3ResNS4_IS8_EEE12emplace_backIJS8_EEERS8_DpOT_ENKUlvE0_clEv
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _kATSFontTestMessageTextKey
+ _kATSFontTestNameKey
+ _kATSFontTestReportTypeFull
+ _kATSFontTestSeverityInformation
+ _kATSFontTestSeverityMinorError
+ _kATSFontTestSeverityTechnicalError
+ _kATSValidationEmulateCrash
+ _kATSValidationFontFormat
+ _kATSValidationNotValidated
+ _kATSValidationRemoteValidateAll
+ _kType1FindingCategoryKey
+ _kType1FindingMessageKey
+ _kType1FindingSeverityKey
+ _kType1FindingSubSeverityKey
+ _memchr
+ _memcmp
+ _memset
+ _memset_pattern16
- FontFormatSupportedByiOS
- __ZL32CopyPosingFailedValidationReportPK10__CFString
- __ZN5woff214WOFF2MemoryOut4SizeEv
- __ZN5woff214WOFF2MemoryOut5WriteEPKvm
- __ZN5woff214WOFF2MemoryOut5WriteEPKvmm
- __ZN5woff214WOFF2MemoryOutC1EPhm
- __ZN5woff214WOFF2MemoryOutD0Ev
- __ZN5woff214WOFF2MemoryOutD1Ev
- __ZN5woff217ConvertWOFF2ToTTFEPhmPKhm
- __ZN5woff221ComputeWOFF2FinalSizeEPKhm
- __ZTVN5woff214WOFF2MemoryOutE
CStrings:
+ " - "
+ " FDs exist."
+ " array' (a Type 1 encoding has 256 entries)."
+ " axes but /BlendAxisTypes lists "
+ " but only "
+ " charstring: "
+ " coordinates."
+ " design axes (the format allows at most 4)."
+ " entries; a blend needs at least 2 master designs."
+ " glyph offset "
+ " glyphs but the dictionary was declared with "
+ " has "
+ " has an odd number of values ("
+ " is invalid (a Type 1 font must be 1, 2, or 8)."
+ " is out of range (must be 0-4)."
+ " is outside the valid range 0-255."
+ " is past the data block."
+ " length ("
+ " master designs (the format allows at most "
+ " master positions but /WeightVector declares "
+ " masters."
+ " out of range"
+ " records) runs past the "
+ " selects FD "
+ " values (the format allows at most "
+ "#PARSE_MESSAGE_HERE#"
+ "%!FontType1"
+ "%!PS-AdobeFont"
+ "%ADOBeginFontDict"
+ "' has no length."
+ "' length ("
+ "' length overruns the Private dict."
+ "' missing its charstring reader (RD/-| or the font's equivalent)."
+ "': "
+ "'POST' resources did not reconstruct a Type 1 font (no '%!' header)."
+ "(Hex)"
+ ") exceeds the maximum charstring size ("
+ ") is out of range."
+ ") runs past the end of the file."
+ ") than the declared count ("
+ ")."
+ "); alignment zones are top/bottom pairs."
+ ", "
+ "-byte data block."
+ "-|"
+ "/..namedfork/rsrc"
+ "/BlendAxisTypes"
+ "/BlendDesignMap"
+ "/BlendDesignPositions"
+ "/BlueValues"
+ "/CIDCount"
+ "/CIDFontName"
+ "/CIDInit"
+ "/CIDMapOffset"
+ "/CIDSystemInfo"
+ "/CharStrings"
+ "/Encoding"
+ "/FDArray"
+ "/FDBytes"
+ "/FamilyBlues"
+ "/FamilyOtherBlues"
+ "/FontBBox"
+ "/FontInfo"
+ "/FontMatrix"
+ "/FontName"
+ "/FontType"
+ "/GDBytes"
+ "/Ordering"
+ "/OtherBlues"
+ "/Private"
+ "/Registry"
+ "/SDBytes"
+ "/StemSnapH"
+ "/StemSnapV"
+ "/SubrCount"
+ "/SubrMapOffset"
+ "/Subrs"
+ "/Supplement"
+ "/WeightVector"
+ "/lenIV"
+ "/tmp/atscffvalidation_XXXXXX"
+ ": "
+ ": CharStrings - "
+ "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>kATSFontTestCreateReportTypeKey</key><string>kATSFontTestReportTypeSummary</string><key>kATSFontTestFontsTestedKey</key><array><dict><key>kATSFontTestArrayKey</key><array><dict><key>kATSFontTestDescriptionKey</key><string>This test checks for basic parsability; failure means we can't even successfully parse the supplied data as a font.</string><key>kATSFontTestIdentifierKey</key><string>com.apple.generalFont</string><key>kATSFontTestMessagesKey</key><array><dict><key>kATSFontTestResultKey</key><string>kATSFontTestSeverityFatalError</string><key>kATSFontTestMessageTextKey</key><string>#PARSE_MESSAGE_HERE#</string></dict></array><key>kATSFontTestNameKey</key><string>Font basic parsability</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestSeverityKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestTargetKey</key><array><string>kATSFontTestGeneralFontData</string></array><key>kATSFontTestTimeStampKey</key><string>2026-05-08 21:33:18 +0000</string><key>kATSFontTestTypeKey</key><array><string>kATSFontTestUsabilityTest</string><string>kATSFontTestStructureTest</string></array><key>kATSFontTestVersionKey</key><integer>1</integer></dict></array><key>kATSFontTestFontIdentifierKey</key><string>2671EC3A|#FONT_NAME_HERE#</string><key>kATSFontTestFontNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontPostScriptNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontTypeKey</key><string>kATSFontTestTrueTypeFontData</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array></dict></array><key>kATSFontTestForceTestExecutionKey</key><integer>1</integer><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array><key>kATSFontTestUseSandboxOptionKey</key><integer>0</integer></dict></plist>"
+ "CFF2 is not a valid standalone font format: it is defined only as a table within an OpenType font and relies on other tables (‘maxp’, ‘hmtx’/‘vmtx’, ‘fvar’, ...) that a bare CFF2 file lacks."
+ "CID-keyed charstring interpretation"
+ "CID-keyed font structure"
+ "CID-keyed font: "
+ "CID-keyed font: 'StartData' marker not found."
+ "CID-keyed font: /CIDFontName not found."
+ "CID-keyed font: /CIDSystemInfo has no /Ordering."
+ "CID-keyed font: /CIDSystemInfo has no /Registry."
+ "CID-keyed font: /CIDSystemInfo has no /Supplement."
+ "CID-keyed font: /FDArray declares no font dicts."
+ "CID-keyed font: /FDBytes out of range (1-4)."
+ "CID-keyed font: /GDBytes out of range (1-4)."
+ "CID-keyed font: CID "
+ "CID-keyed font: CID map (offset "
+ "CID-keyed font: CID map offsets are not monotonic at CID "
+ "CID-keyed font: StartData hex data is invalid."
+ "CID-keyed font: StartData length ("
+ "CID-keyed font: further charstring errors suppressed."
+ "CID-keyed font: negative /CIDCount."
+ "CID-keyed font: required /CIDCount is missing."
+ "CID-keyed font: required /CIDMapOffset is missing."
+ "CID-keyed font: required /CIDSystemInfo dictionary is missing."
+ "CID-keyed font: required /FDBytes is missing."
+ "CID-keyed font: required /GDBytes is missing."
+ "CharStrings"
+ "CharStrings: "
+ "CharStrings: count could not be read."
+ "CharStrings: declared count ("
+ "CharStrings: entry '"
+ "CharStrings: parsed "
+ "Charstring '"
+ "Charstrings: "
+ "Charstrings: further glyph errors suppressed."
+ "Cleartext"
+ "Cleartext: "
+ "Cleartext: /Encoding entry code "
+ "Cleartext: /FontBBox entry is missing."
+ "Cleartext: /FontInfo dictionary is missing."
+ "Cleartext: /FontMatrix is degenerate (zero yScale or zero determinant); glyphs would collapse."
+ "Cleartext: /FontType "
+ "Cleartext: /FontType entry is missing."
+ "Cleartext: custom /Encoding is '"
+ "Cleartext: header does not begin with '%!PS-AdobeFont' or '%!FontType1'."
+ "Cleartext: required /Encoding entry is missing."
+ "Cleartext: required /FontMatrix entry is missing."
+ "Cleartext: required /FontName entry is missing."
+ "Could not read the font file."
+ "FONDDataKind"
+ "File is too short to be a Type 1 font."
+ "FontType1"
+ "HierVariationsDataForkFontKind"
+ "LWFN: "
+ "Multiple Master"
+ "Multiple Master design-space structure"
+ "Multiple Master: "
+ "Multiple Master: /BlendAxisTypes lists no design axes."
+ "Multiple Master: /BlendDesignMap describes "
+ "Multiple Master: /BlendDesignMap is missing."
+ "Multiple Master: /BlendDesignPositions has "
+ "Multiple Master: /BlendDesignPositions is missing."
+ "Multiple Master: /BlendDesignPositions master positions do not each have "
+ "Multiple Master: /WeightVector has "
+ "Multiple Master: required /WeightVector is missing."
+ "NFNTBitmapFontKind"
+ "Not a Type 1 font: missing PFB 0x80 marker and '%!' PostScript header."
+ "OpenTypeCFF2FontKind"
+ "OpenTypeCFFCIDFileDataFontKind"
+ "OpenTypeCFFCIDMemoryFontKind"
+ "OpenTypeCFFFileDataFontKind"
+ "OpenTypeCFFMemoryFontKind"
+ "OpenTypeCIDMemoryFontKind"
+ "OpenTypeDataForkCIDFontKind"
+ "OpenTypeDataForkFontKind"
+ "OpenTypeMemoryFontKind"
+ "PFA: "
+ "PFA: eexec section is not valid hexadecimal."
+ "PFA: empty eexec section."
+ "PFA: missing 'cleartomark' trailer."
+ "PFA: missing 'eexec' keyword."
+ "PFB: "
+ "PFB: expected 0x80 marker at segment start."
+ "PFB: missing end-of-file (type 3) segment."
+ "PFB: no binary (eexec) segment found."
+ "PFB: no data segments found."
+ "PFB: segment length runs past end of file."
+ "PFB: trailer is not wrapped in a segment; treating the remainder as the trailer."
+ "PFB: trailer segment length runs past end of file."
+ "PFB: truncated segment header."
+ "PFB: truncated trailer segment header."
+ "PFB: unknown segment type."
+ "PS-AdobeFont"
+ "PostScript Type 1 container structure"
+ "Private dict"
+ "Private dict: "
+ "Private dict: /CharStrings contains no glyphs."
+ "Private dict: /CharStrings has no .notdef glyph."
+ "Private dict: /Private entry not found."
+ "Private dict: /lenIV "
+ "Private dict: required /CharStrings dictionary is missing."
+ "RD"
+ "Raw CFF font (not validated)"
+ "Raw CFF font structure and charstrings"
+ "Raw CFF/CFF2 (Compact Font Format) font: currently not implemented and ignored."
+ "Resource-CIDFont"
+ "SBITOnlyKind"
+ "SFNTDataKind"
+ "SplicedFontKind"
+ "StartData"
+ "Subrs"
+ "Subrs: "
+ "Subrs: count could not be read."
+ "Subrs: declared count ("
+ "Subrs: entry "
+ "Subrs: entry length overruns the Private dict."
+ "Subrs: fewer entries ("
+ "TTCDataKind"
+ "TTCMemoryKind"
+ "The WOFF/WOFF2 font could not be decompressed or parsed as valid font data."
+ "The font could not be parsed: the supplied data could not be interpreted as valid font data."
+ "Trailer"
+ "Trailer: "
+ "Trailer: fewer than 512 zeros before cleartomark."
+ "Trailer: missing 'cleartomark'."
+ "TrueTypeCollectionFontKind"
+ "TrueTypeDataForkFontKind"
+ "TrueTypeMemoryFontKind"
+ "TrueTypeSuitcaseFontKind"
+ "Type 1 Private dictionary structure and contents"
+ "Type 1 charstring interpretation"
+ "Type 1 eexec encryption"
+ "Type 1 font dictionary structure and contents"
+ "Type 1 font structure"
+ "Type 1 font structure is valid"
+ "Type 1 trailer structure"
+ "Type1DataForkFontKind"
+ "Type1FileDataFontKind"
+ "Type1LWFNFontKind"
+ "Type1MemoryFontKind"
+ "Type1PFBFontKind"
+ "Type1SFNTCIDFontKind"
+ "Type1SFNTFontKind"
+ "UnknownFontKind"
+ "WOFF2StreamKind"
+ "WOFFStreamKind"
+ "callothersubr bad argument count"
+ "callothersubr with too few operands"
+ "callsubr index "
+ "callsubr references undefined subr "
+ "callsubr with empty stack"
+ "category"
+ "charstring exceeds the interpreter step budget (possible malformed or adversarial subroutine expansion)"
+ "cleartomark"
+ "com.apple.TrueType.CFF.combined"
+ "div with too few operands"
+ "eexec"
+ "eexec section did not decrypt to a Private dictionary (wrong key or corrupt data)."
+ "glyph does not set width (hsbw/sbw) before drawing"
+ "kATSFontTestMessageTextKey"
+ "kATSFontTestReportTypeFull"
+ "kATSFontTestSeverityInformation"
+ "kATSFontTestSeverityMinorError"
+ "kATSFontTestSeverityTechnicalError"
+ "kFontValidationExperimental"
+ "kFontValidationStandaloneCFF"
+ "message"
+ "notvalidated"
+ "operand stack overflow"
+ "put"
+ "rb"
+ "readhexstring"
+ "readstring"
+ "subSeverities"
+ "subSeverity"
+ "subroutine recursion too deep"
+ "truncated 32-bit operand"
+ "truncated escape operator"
+ "truncated operand"
+ "unknown escape operator 12 "
+ "unknown operator "
+ "validateall"
+ "woff2_"
+ "woff_"
+ "‘cff ’"
+ "‘cid ’"
+ "‘lwfn’"
+ "‘pfa ’"
+ "‘pfb ’"
- "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>kATSFontTestCreateReportTypeKey</key><string>kATSFontTestReportTypeSummary</string><key>kATSFontTestFontsTestedKey</key><array><dict><key>kATSFontTestArrayKey</key><array><dict><key>kATSFontTestDescriptionKey</key><string>This test ensures the ‘name’ table is valid.</string><key>kATSFontTestIdentifierKey</key><string>com.apple.TrueType.name.usability</string><key>kATSFontTestNameKey</key><string>‘name’ table usability</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestSeverityKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityTechnicalError</string></array><key>kATSFontTestTargetKey</key><array><string>kATSFontTest_nameTable</string></array><key>kATSFontTestTimeStampKey</key><string>2026-05-08 21:33:18 +0000</string><key>kATSFontTestTypeKey</key><array><string>kATSFontTestUsabilityTest</string><string>kATSFontTestStructureTest</string></array><key>kATSFontTestVersionKey</key><integer>1</integer></dict></array><key>kATSFontTestFontIdentifierKey</key><string>2671EC3A|#FONT_NAME_HERE#</string><key>kATSFontTestFontNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontPostScriptNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontTypeKey</key><string>kATSFontTestTrueTypeFontData</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array></dict></array><key>kATSFontTestForceTestExecutionKey</key><integer>1</integer><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array><key>kATSFontTestUseSandboxOptionKey</key><integer>0</integer></dict></plist>"
```
