## FontValidator

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/Current/Frameworks/ATS.framework/Versions/Current/Support/FontValidator`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__dlopen_cstrs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`

```diff

-601.0.0.0.0
-  __TEXT.__text: 0x12510
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_stubs: 0xc00
+603.0.0.0.0
+  __TEXT.__text: 0x24950
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0xf40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x2a0
-  __TEXT.__cstring: 0x42a9
-  __TEXT.__gcc_except_tab: 0xf7c
-  __TEXT.__const: 0x16c
-  __TEXT.__ustring: 0xdea
+  __TEXT.__objc_methlist: 0x3e4
+  __TEXT.__cstring: 0x8462
+  __TEXT.__gcc_except_tab: 0x1a74
+  __TEXT.__const: 0x35c
+  __TEXT.__ustring: 0x1010
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__objc_methname: 0xb01
-  __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methtype: 0xdf
+  __TEXT.__objc_classname: 0x6f
+  __TEXT.__objc_methname: 0xef0
+  __TEXT.__objc_methtype: 0xf6
   __TEXT.__info_plist: 0x107
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__const: 0xe60
-  __DATA_CONST.__cfstring: 0x2ec0
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x7a8
+  __DATA_CONST.__const: 0x1260
+  __DATA_CONST.__cfstring: 0x3b60
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x740
-  __DATA.__objc_selrefs: 0x398
-  __DATA.__objc_ivar: 0x58
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x1f8
-  __DATA.__common: 0x18
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__objc_intobj: 0x120
+  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__objc_const: 0xb60
+  __DATA.__objc_selrefs: 0x4a8
+  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_data: 0x230
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0x240
+  __DATA.__common: 0x20
   __RESTRICT.__restrict: 0x0
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 263
-  Symbols:   953
-  CStrings:  693
+  - /usr/lib/libz.1.dylib
+  Functions: 414
+  Symbols:   1270
+  CStrings:  1114
 
Symbols:
+ +[FVFinding findingWithDict:]
+ +[FVFinding findingsWithArray:]
+ -[FVClassifiedFinding .cxx_destruct]
+ -[FVClassifiedFinding failureCode]
+ -[FVClassifiedFinding findingClass]
+ -[FVClassifiedFinding messages]
+ -[FVClassifiedFinding name]
+ -[FVClassifiedFinding setFailureCode:]
+ -[FVClassifiedFinding setFindingClass:]
+ -[FVClassifiedFinding setMessages:]
+ -[FVClassifiedFinding setName:]
+ -[FVFinding .cxx_destruct]
+ -[FVFinding code]
+ -[FVFinding issue]
+ -[FVFinding messages]
+ -[FVReport format]
+ -[FVReport maxCode]
+ -[FVReport osInstallable]
+ -[FVReport result]
+ -[FVValidationFont format]
+ -[FVValidationFont issues]
+ -[FVValidationFont warningFindings]
+ -[ProcessURLInfo inputURL]
+ -[ProcessURLInfo setSymLinkedURL:]
+ -[ProcessURLInfo symLinkedURL]
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table14
+ GCC_except_table36
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table78
+ GCC_except_table88
+ GCC_except_table92
+ GCC_except_table93
+ GCC_except_table94
+ GetFontFormat
+ OBJC_IVAR_$_FVClassifiedFinding._failureCode
+ OBJC_IVAR_$_FVClassifiedFinding._findingClass
+ OBJC_IVAR_$_FVClassifiedFinding._messages
+ OBJC_IVAR_$_FVClassifiedFinding._name
+ OBJC_IVAR_$_FVFinding._code
+ OBJC_IVAR_$_FVFinding._issue
+ OBJC_IVAR_$_FVFinding._messages
+ OBJC_IVAR_$_FVReport._format
+ OBJC_IVAR_$_FVReport._maxCode
+ OBJC_IVAR_$_FVReport._osInstallable
+ OBJC_IVAR_$_FVReport._result
+ OBJC_IVAR_$_FVValidationFont._format
+ OBJC_IVAR_$_FVValidationFont._issues
+ OBJC_IVAR_$_FVValidationFont._warningFindings
+ OBJC_IVAR_$_ProcessURLInfo._symLinkedURL
+ _CFDictionaryGetCount
+ _CFEqual
+ _CFPropertyListCreateData
+ _CTFontCopyMetadata
+ _CopyFontFormatNameForURL
+ _CopyFontKindFormatNameForURL
+ _FileIsFontCollection
+ _FontIsOSInstallable
+ _FontKindName
+ _GetFontFormat
+ _GetWOFFFlavor
+ _IsResourceForkLWFNFile
+ _IsType1File
+ _LocalType1Validate
+ _NSURLFileResourceTypeDirectory
+ _NSURLFileResourceTypeKey
+ _NSURLFileResourceTypeSymbolicLink
+ _OBJC_CLASS_$_FVClassifiedFinding
+ _OBJC_CLASS_$_FVFinding
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSPipe
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_FVClassifiedFinding
+ _OBJC_METACLASS_$_FVFinding
+ _RunningAsAgent
+ _Type1CategoryDisplayName
+ _Type1FileIsOSInstallable
+ _Type1FontKindName
+ _Type1SniffCFFURL
+ _Type1SniffResourceForkLWFNURL
+ _Type1SniffURL
+ _Type1ValidateURL
+ _ValidateAllRequested
+ _ZL17WarningSeveritiesv
+ _ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjib
+ _ZL25ContainerTagForFormatNameP8NSString
+ _ZL26CGFontGetParserFontProcPtrP6CGFont
+ _ZL29CTFontCopyGraphicsFontProcPtrPK8__CTFontPPK18__CTFontDescriptor
+ _ZL48CTFontManagerCreateFontDescriptorsFromURLProcPtrPK7__CFURL
+ __CTFontCopyMetadata
+ __CTFontCopyTable
+ __CTFontCreateWithFontDescriptor
+ __OBJC_$_CLASS_METHODS_FVFinding
+ __OBJC_$_INSTANCE_METHODS_FVClassifiedFinding
+ __OBJC_$_INSTANCE_METHODS_FVFinding
+ __OBJC_$_INSTANCE_VARIABLES_FVClassifiedFinding
+ __OBJC_$_INSTANCE_VARIABLES_FVFinding
+ __OBJC_$_PROP_LIST_FVClassifiedFinding
+ __OBJC_$_PROP_LIST_FVFinding
+ __OBJC_CLASS_RO_$_FVClassifiedFinding
+ __OBJC_CLASS_RO_$_FVFinding
+ __OBJC_METACLASS_RO_$_FVClassifiedFinding
+ __OBJC_METACLASS_RO_$_FVFinding
+ __Z7strrchrB9nqn220106Ua9enable_ifIXLb1EEEPKci
+ __ZL10gWhiteList
+ __ZL11MakeFindingP8NSStringP7NSArrayIS0_EP8NSNumber
+ __ZL13OptionMatchesPKcS0_m
+ __ZL13gFilesCounted
+ __ZL14RunningOnMacOSv
+ __ZL15RuleDisplayNameP12NSDictionary
+ __ZL16CountFilesAtPathP5NSURLbbPy
+ __ZL16RuleMessageArrayP12NSDictionary
+ __ZL17ReportTypeMatchesPKcS0_
+ __ZL17WarningSeveritiesv
+ __ZL18CanonicalizeOptionPKcPcm
+ __ZL18gFileCountComplete
+ __ZL20CopyRuleMessageTextsP12NSDictionaryP5NSSetIP8NSStringEPb
+ __ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjib
+ __ZL22FormatRejectionMessageP5NSURL
+ __ZL22ResourceForkIsRejectedP14ProcessURLInfojb
+ __ZL25ContainerTagForFormatNameP8NSString
+ __ZL26CGFontGetParserFontProcPtrP6CGFont
+ __ZL26RuleSubSeverityForSeverityP12NSDictionaryP8NSString
+ __ZL28ResourceForkRejectionMessageP5NSURL
+ __ZL28_CreateType1ValidationReportPK10__CFStringPK9__CFArrayS1_
+ __ZL29CTFontCopyGraphicsFontProcPtrPK8__CTFontPPK18__CTFontDescriptor
+ __ZL29DefaultReportTypeIsOldSummaryv
+ __ZL32CopyPosingFailedValidationReportPK10__CFStringS1_
+ __ZL33CopyReportWithFormatRejectionRulePK14__CFDictionaryP8NSStringS3_
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
+ __ZNK12_GLOBAL__N_18Type1Doc10IsPutTokenERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNK12_GLOBAL__N_18Type1Doc13IsReaderTokenERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNKSt3__111__copy_implclB9nqn220106IPNS_6vectorIhNS_9allocatorIhEEEES6_S6_Li0EEENS_4pairIT_T1_EES8_T0_S9_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9nqn220106EPKcm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS_6vectorIhNS_9allocatorIhEEEEE3$_0PZNS2_15LWFNCollectPOSTES4_mS9_E3ResLb0EEEvT1_SE_T0_NS_15iterator_traitsISE_E15difference_typeEb
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqn220106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9nqn220106Em
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
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
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZZL15FatalSeveritiesvE10severities
+ __ZZL15FatalSeveritiesvE9onceToken
+ __ZZL17WarningSeveritiesvE10severities
+ __ZZL17WarningSeveritiesvE9onceToken
+ __ZZL20ParseValidationLevelPKcP18FontValidatorLevelE11kLevelNames
+ __ZZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjibE16errorNameMapping
+ __ZZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjibE9onceToken
+ __ZZL25ContainerTagForFormatNameP8NSStringE4once
+ __ZZL25ContainerTagForFormatNameP8NSStringE4tags
+ __ZZN12_GLOBAL__N_118Type1RenderMessageE14Type1ContainerRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE7kTopics
+ __ZZN12_GLOBAL__N_18Type1Doc15CheckHintArraysERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE11kBlueArrays
+ __ZZN12_GLOBAL__N_18Type1Doc15CheckHintArraysERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE11kStemArrays
+ __ZZNSt3__16vectorIN12_GLOBAL__N_17FindingENS_9allocatorIS2_EEE12emplace_backIJS2_EEERS2_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorIN12_GLOBAL__N_18Type1Doc9CharEntryENS_9allocatorIS3_EEE12emplace_backIJS3_EEERS3_DpOT_ENKUlvE0_clEv
+ __ZZNSt3__16vectorIZN12_GLOBAL__N_115LWFNCollectPOSTEPKhmPNS0_IhNS_9allocatorIhEEEEE3ResNS4_IS8_EEE12emplace_backIJS8_EEERS8_DpOT_ENKUlvE0_clEv
+ __ZZZ17FontValidatorCoreEUb_E14kSpinnerFrames
+ ___NSArray0__struct
+ ____ZL15FatalSeveritiesv_block_invoke
+ ____ZL17WarningSeveritiesv_block_invoke
+ ____ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjib_block_invoke
+ ____ZL25ContainerTagForFormatNameP8NSString_block_invoke
+ ___block_descriptor_41_ea8_32s_e5_v8?0l
+ ___block_descriptor_83_ea8_32s40r48r56r64r72r_e22_v16?0"NSDictionary"8l
+ ___copy_helper_block_ea8_32s40r48r56r64r72r
+ ___destroy_helper_block_ea8_32s40r48r56r64r72r
+ ___tolower
+ _crc32
+ _dispatch_get_global_queue
+ _dispatch_group_async
+ _dispatch_group_create
+ _dispatch_group_wait
+ _fflush
+ _flockfile
+ _fread
+ _fseek
+ _ftell
+ _funlockfile
+ _isatty
+ _kATSValidationFontFormat
+ _kATSValidationNotValidated
+ _kATSValidationRemoteValidateAll
+ _kFVFindingActualSeverity
+ _kFVFindingCode
+ _kFVFindingIssue
+ _kFVFindingMessages
+ _kFVReportFormat
+ _kFVReportMaxCode
+ _kFVReportOSInstallable
+ _kFVReportResult
+ _kFVReportValidationFontFormat
+ _kFVReportValidationFontIssues
+ _kFVRuleSubSeverities
+ _kFontValidationAppleFontDistributionStr
+ _kFontValidationAppleLicensedFontDistributionStr
+ _kFontValidationNotValidatedStr
+ _kType1FindingCategoryKey
+ _kType1FindingMessageKey
+ _kType1FindingSeverityKey
+ _kType1FindingSubSeverityKey
+ _memchr
+ _memcmp
+ _memset
+ _memset_pattern16
+ _objc_msgSend$URLByResolvingSymlinksInPath
+ _objc_msgSend$bytes
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$copy
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$failureCode
+ _objc_msgSend$fileHandleForReading
+ _objc_msgSend$fileHandleWithNullDevice
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$findingClass
+ _objc_msgSend$findingWithDict:
+ _objc_msgSend$findingsWithArray:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$inputURL
+ _objc_msgSend$messages
+ _objc_msgSend$name
+ _objc_msgSend$pipe
+ _objc_msgSend$readDataToEndOfFile
+ _objc_msgSend$setFailureCode:
+ _objc_msgSend$setFindingClass:
+ _objc_msgSend$setMessages:
+ _objc_msgSend$setStandardError:
+ _objc_msgSend$setStandardOutput:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$stringByAppendingString:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _strrchr
- FontFormatSupportedByiOS
- GCC_except_table2
- GCC_except_table23
- GCC_except_table26
- GCC_except_table27
- GCC_except_table28
- GCC_except_table33
- GCC_except_table37
- GCC_except_table38
- GCC_except_table42
- GCC_except_table45
- GCC_except_table49
- GCC_except_table51
- GCC_except_table58
- GCC_except_table62
- GCC_except_table64
- GCC_except_table74
- GCC_except_table76
- GCC_except_table83
- GCC_except_table84
- _CGFontGetParserFont
- _CTFontCopyGraphicsFont
- _CTFontManagerCreateFontDescriptorsFromURL
- _ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryji
- _ZN13AppleMetadataC2EPK8__CTFont
- __ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryji
- __ZL32CopyPosingFailedValidationReportPK10__CFString
- __ZZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjiE16errorNameMapping
- __ZZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryjiE9onceToken
- ____ZL21GetSimplifiedCTReportP14ProcessURLInfoP12NSDictionaryji_block_invoke
- ___block_descriptor_65_ea8_32s40r48r56r_e22_v16?0"NSDictionary"8l
- ___copy_helper_block_ea8_32s40r48r56r
- ___destroy_helper_block_ea8_32s40r48r56r
CStrings:
+ "\t\t-75               Allow-listed by -whiteList: the finding is exempt and the font passes. It\n\t\t                  is the least negative code, so it surfaces as the file's code only when\n\t\t                  nothing un-rescued remains -- \"-75\" means rescued and passed\n"
+ "\t\t250               carutil could not be executed (-carutilPath)\n\t\t249               -tmpDir path is not valid\n\t\t248               -tmpDir path could not be written to\n"
+ "\n\t\t*************    PRIVATE/APPLE_INTERNAL OPTIONS\n\t\t-carFiles         Inspect .car files for fonts. NOTE: it will turn on -local for in-process validation\n\t\t-carutilPath      Path to carutil tool. Default is /usr/local/bin/carutil\n\t\t-experimental     Enable experimental validators (currently 'CFF '/'CFF2' table validation, including their Type 2\n\t\t                  charstrings)\n\t\t-iosOnly          Alias for -platform iOS\n\t\t-greedy           Adjusts priorities for operation queues to be high user level priorities. Makes sense only with\n\t\t                  -multiThread which is off by default\n\t\t-limitedRemote    Validates remotely without asking for the non-sfnt formats, the way an\n\t\t                  ordinary ATSFontValidate client does. Every other run of this tool asks,\n\t\t                  so this is the only way to see what such a client receives -- a raw Type 1,\n\t\t                  LWFN, bare CFF or WOFF comes back not validated (-99). For testing\n\t\t-local            Performs all validation in-process (Default)\n\t\t-multiThread      Run multi-threaded. Only available with -local\n\t\t-mode             Deprecated alias for -level. Both accept the older level names as well:\n\t\t                  security=minimum, usability=medium, compatibility=default, install=strict.\n\t\t-pedantic         alias for -onlyFonts\n\t\t-report           Short-cut for -reportType with the platform's default shape\n\t\t-reportType       oldSummary    (DEPRECATED)\n\t\t                   The pre-2026 summary report: the `validation` wrapper, name-only\n\t\t                   failure/warning lists and `error`/`error_desc`. \n\t\t-showSuccesses    Report shows names of successful tests\n\t\t-tagAssetInfo     Extracts tag and asset names from asset car plist and data. Provides cleaner output but is slower\n\t\t-tmpDir           Specify location where temporary files may be written\n\t\t-whiteList        Path to a JSON allow-list of known fonts whose validation failures are reported as warnings (the\n\t\t                  font passes). The file is an array of objects, each with any of \"filename\", \"fontname\" and\n\t\t                  \"crc\"; an entry matches only when every key it declares matches. For a font collection, a\n\t\t                  \"fontname\" entry exempts only that face — use \"filename\" and/or \"crc\" to exempt every face.\n\t\t                  Generate a \"crc\" with:\n\t\t                     cksum -o 3 <file> | awk '{printf \"%08x\\n\", $1}'\n"
+ "\n\n\tValidates font files are adequate to use with platform specified (macOS default).\n\t  How tolerant validation is can be specified by the -level parameter; strict is recommended\n\t  when checking fonts for submission, as it also fails a format the platform will not install.\n\t  If a directory is specified, it recursively examines font files found\n\t  Compound option names may be written camelCase, dash- or underscore-separated, in any case:\n\t  -reportType, -report-type and -report_type are the same option.\n\t  An option name may be abbreviated to a prefix as a convenience. Nothing is guaranteed when a\n\t  prefix could match more than one option, so use it carefully.\n\t  Arguments are processed strictly left to right: when two of them disagree the later one\n\t  wins, and an option only affects the paths that follow it. Put every option before the\n\t  first path.\n\n\t\t-appleFonts       Report Apple designed or licensed fonts as failures (Apps should not bundle them)\n\t\t-duplicates       Report a font whose PostScript name is already installed on the system\n\t\t-dynamic          Perform dynamic validation (runtime checks against CoreText APIs)\n\t\t-help             Show help information and exit. -h and --help are the same\n\t\t-level            How tolerant validation is, from most to least: minimum|medium|default|strict|maximum\n\t\t                  (default is default)\n\t\t                     minimum    fails only on defects that could cause memory-safety issues\n\t\t                     medium     minimum, and fails on severe structural defects\n\t\t                     default    medium, and fails on any other font specification violation;\n\t\t                                a format the platform will not install is not held against it\n\t\t                                (the one exception is noted under -102 below)\n\t\t                     strict     default, and also fails a format the platform will not install.\n\t\t                                The font is still validated: the format is reported as one more\n\t\t                                issue (-102), alongside whatever else was found\n\t\t                     maximum    strict, and fails on lower-value specification violations\n\t\t-onlyFailures     Report only the files that failed. The run tallies still count every file\n\t\t-onlyFonts        Report files that were not validated as failures: a file that is not a font\n\t\t                  (-100) and a font whose format this run did not examine (-99). Both are\n\t\t                  left out of the report otherwise\n\t\t-platform         Target platform to use fonts: macOS (default), iOS|tvOS|visionOS|watchOS\n\t\t-progress         Show progress file count progress and percentage complete if needed\n\t\t-quiet            Suppress progress information and the per-file diagnostics on stderr. The\n\t\t                  summary report types suppress those diagnostics whether or not this is given\n\t\t-relativePath     File paths in reports are relative to the base path passed in. Useful when\n\t\t                  processing directory paths\n\t\t-remote           Perform validation in a separate process%s\n\t\t-reportOutput     Report file path when -reportType used. stdout used if not specified\n\t\t-reportType       Type of report to generate: summary|detailed|full (default is %s)\n\t\t                     summary    the result, the worst code found and whether the format is\n\t\t                                OS-installable, per file and per face\n\t\t                     detailed   summary + per-issue codes and messages\n\t\t                     full       detailed + warnings and the font format\n\t\t-showWarnings     Report shows warnings\n\t\t-version          Show tool version and exit\n\t\t-warningAsFailure Warnings are treated as failures\n%s\n\tReport codes\n\t  A code says what was found. Whether the file failed is the report's `result`: the same code\n\t  can accompany a pass or a failure depending on -level and -warningAsFailure, so a consumer\n\t  deciding pass/fail reads `result` and never infers it from a code.\n\t  If you must judge from the code alone, -101 is the boundary: -101 and lower are failures and\n\t  nothing above it is. The exception is -100, reported only when -onlyFonts asks for non-fonts,\n\t  where treating them as failures is the point of the option.\n\n\t\t 0                No issues found\n%s\t\t-99               Not validated: a format a -remote run does not examine. Not a failure;\n\t\t                  reported only with -onlyFonts\n\t\t-100              Not a font file. Not a failure; reported only with -onlyFonts\n\t\t-101              Structural failure. No level relaxes it\n\t\t-102              The target platform will not install this font; the issue message says why.\n\t\t                  One issue among the font's others, so max_code reports it only when nothing\n\t\t                  more significant was found; os_installable says so whatever the max_code\n\t\t-103              Apple designed font (-appleFonts)\n\t\t-104              Apple licensed font (-appleFonts)\n\t\t-201              A failure the level relaxed, and one to address to be safe: a parser without\n\t\t                  its own bounds checks could hit a memory-safety issue on this defect\n\t\t-202              A failure the level relaxed; a specification violation with no memory-safety\n\t\t                  concern. Address it to comply with the specification\n\t\t-301              A warning. Shown with -showWarnings; -warningAsFailure makes it a failure\n\n\tExit status\n\t\t0                 Every file was validated and none failed\n\t\t255               One or more files failed validation\n\t\t254               -onlyFonts was given, nothing failed, and a file was counted that was not\n\t\t                  validated as a font. In practice that is a font whose format this run did\n\t\t                  not examine (-99); a file that is not a font (-100) counts as a failure\n\t\t                  under -onlyFonts and gives 255 instead\n\t\t252               Invalid option, missing value, unreadable path, or no input file\n\t\t251               The validation library could not be loaded\n%s\t\t247               -reportOutput path is not valid\n\t\t246               -reportOutput path could not be opened for writing\n\t\n\n\tVersion %s\n"
+ " - "
+ " -carFiles -carutilPath [PATH_TO_EXECUTABLE] -experimental -iosOnly -greedy -limitedRemote -local -multiThread -pedantic -tagAssetInfo -tmpDir [PATH_TMP_DIR] -whiteList [PATH_TO_JSON]"
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
+ "%08lx"
+ "%@%@"
+ "%@: %@"
+ "%ADOBeginFontDict"
+ "%s failed Type 1 validation\n"
+ "%s report type unknown\n"
+ "%s: format is not installable on the target OS\n"
+ "%s: not validated -- the format is not validated by a remote run\n"
+ "%s: note -- both an Apple font distribution violation and a structural validation failure fired\n"
+ "%s: the font data is in the resource fork, which the target platform does not support\n"
+ "%u files %c\n"
+ "%u/%llu files (%.0f%%) %c\n"
+ "%u/%llu+ files %c\n"
+ "' has no length."
+ "' length ("
+ "' length overruns the Private dict."
+ "' missing its charstring reader (RD/-| or the font's equivalent)."
+ "': "
+ "'POST' resources did not reconstruct a Type 1 font (no '%!' header)."
+ "("
+ "(Hex)"
+ "(macOS only)"
+ ") exceeds the maximum charstring size ("
+ ") is out of range."
+ ") runs past the end of the file."
+ ") than the declared count ("
+ ")."
+ "); alignment zones are top/bottom pairs."
+ "--help"
+ "--info"
+ "-appleFonts"
+ "-byte data block."
+ "-carFiles"
+ "-carutilPath"
+ "-experimental"
+ "-iosOnly"
+ "-level"
+ "-limitedRemote"
+ "-limitedRemote is only available in macOS"
+ "-mode"
+ "-multiThread"
+ "-onlyFailures"
+ "-onlyFonts"
+ "-platform"
+ "-progress"
+ "-relativePath"
+ "-remote"
+ "-remote is only available in macOS"
+ "-reportOutput"
+ "-reportType"
+ "-tagAssetInfo"
+ "-tmpDir"
+ "-warningAsFailure"
+ "-whiteList"
+ "-|"
+ ".notdef"
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
+ "3.5.1"
+ ": "
+ ": CharStrings - "
+ "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>kATSFontTestCreateReportTypeKey</key><string>kATSFontTestReportTypeSummary</string><key>kATSFontTestFontsTestedKey</key><array><dict><key>kATSFontTestArrayKey</key><array><dict><key>kATSFontTestDescriptionKey</key><string>This test checks for basic parsability; failure means we can't even successfully parse the supplied data as a font.</string><key>kATSFontTestIdentifierKey</key><string>com.apple.generalFont</string><key>kATSFontTestMessagesKey</key><array><dict><key>kATSFontTestResultKey</key><string>kATSFontTestSeverityFatalError</string><key>kATSFontTestMessageTextKey</key><string>#PARSE_MESSAGE_HERE#</string></dict></array><key>kATSFontTestNameKey</key><string>Font basic parsability</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestSeverityKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestTargetKey</key><array><string>kATSFontTestGeneralFontData</string></array><key>kATSFontTestTimeStampKey</key><string>2026-05-08 21:33:18 +0000</string><key>kATSFontTestTypeKey</key><array><string>kATSFontTestUsabilityTest</string><string>kATSFontTestStructureTest</string></array><key>kATSFontTestVersionKey</key><integer>1</integer></dict></array><key>kATSFontTestFontIdentifierKey</key><string>2671EC3A|#FONT_NAME_HERE#</string><key>kATSFontTestFontNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontPostScriptNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontTypeKey</key><string>kATSFontTestTrueTypeFontData</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array></dict></array><key>kATSFontTestForceTestExecutionKey</key><integer>1</integer><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array><key>kATSFontTestUseSandboxOptionKey</key><integer>0</integer></dict></plist>"
+ "@\"NSNumber\""
+ "Allow-list file must contain a JSON array of {filename,fontname,crc} objects: '%s'"
+ "Apple font distribution policy violation"
+ "Apple licensed font distribution policy violation"
+ "AssetType"
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
+ "Collection_"
+ "Could not read allow-list file: '%s'"
+ "Could not read the font file."
+ "ExpertEncoding"
+ "FONDDataKind"
+ "FVClassifiedFinding"
+ "FVFinding"
+ "FV_FORCE_LEGACY_REPORT_DEFAULT"
+ "File is too short to be a Type 1 font."
+ "FontType1"
+ "HierVariationsDataForkFontKind"
+ "ISOLatin1Encoding"
+ "LWFN: "
+ "MixedFormatCollection"
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
+ "NP"
+ "Not a Type 1 font: missing PFB 0x80 marker and '%!' PostScript header."
+ "Not validated: format not validated by a remote run"
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
+ "Processing validation reports...\n"
+ "RD"
+ "Raw CFF font (not validated)"
+ "Raw CFF font structure and charstrings"
+ "Raw CFF/CFF2 (Compact Font Format) font: currently not implemented and ignored."
+ "Resource-CIDFont"
+ "SBITOnlyKind"
+ "SFNTDataKind"
+ "SplicedFontKind"
+ "StandardEncoding"
+ "StartData"
+ "Subrs"
+ "Subrs: "
+ "Subrs: count could not be read."
+ "Subrs: declared count ("
+ "Subrs: entry "
+ "Subrs: entry length overruns the Private dict."
+ "Subrs: fewer entries ("
+ "T@\"NSArray\",&,V_messages"
+ "T@\"NSArray\",R,V_issues"
+ "T@\"NSArray\",R,V_messages"
+ "T@\"NSArray\",R,V_warningFindings"
+ "T@\"NSNumber\",R,V_code"
+ "T@\"NSNumber\",R,V_osInstallable"
+ "T@\"NSNumber\",R,V_result"
+ "T@\"NSString\",&,V_name"
+ "T@\"NSString\",R,V_format"
+ "T@\"NSString\",R,V_issue"
+ "T@\"NSURL\",&,V_symLinkedURL"
+ "T@\"NSURL\",R"
+ "TTCDataKind"
+ "TTCMemoryKind"
+ "The %@ format cannot be installed on the target platform."
+ "The WOFF/WOFF2 font could not be decompressed or parsed as valid font data."
+ "The font could not be parsed: the supplied data could not be interpreted as valid font data."
+ "The font data is in the resource fork, which the target platform does not support, so the font is unusable on it."
+ "This font's format cannot be installed on the target platform."
+ "This test ensures the font's format is one the target platform will install"
+ "Ti,V_failureCode"
+ "Ti,V_findingClass"
+ "Tq,R,V_maxCode"
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
+ "URLByResolvingSymlinksInPath"
+ "Unknown -level value: '%s' (expected %s)"
+ "Unknown platform: '%s'"
+ "UnknownFontKind"
+ "Usage:\n\t%s [-appleFonts -duplicates -dynamic -help -level LEVEL -onlyFailures -onlyFonts -platform PLATFORM -progress -quiet -relativePath -remote -reportOutput OUTPUT_FILE_PATH -reportType TYPE -showWarnings -version -warningAsFailure%s] FONT_FILE_OR_DIR_PATH[...FONT_FILE_OR_DIR_PATH_N]"
+ "WOFF2StreamKind"
+ "WOFFStreamKind"
+ "_code"
+ "_failureCode"
+ "_findingClass"
+ "_format"
+ "_issue"
+ "_issues"
+ "_maxCode"
+ "_messages"
+ "_osInstallable"
+ "_symLinkedURL"
+ "_warningFindings"
+ "actualSeverity"
+ "allow-list file not specified\n"
+ "begin"
+ "bytes"
+ "callothersubr bad argument count"
+ "callothersubr with too few operands"
+ "callsubr index "
+ "callsubr references undefined subr "
+ "callsubr with empty stack"
+ "caseInsensitiveCompare:"
+ "category"
+ "charstring exceeds the interpreter step budget (possible malformed or adversarial subroutine expansion)"
+ "cleartomark"
+ "code"
+ "com.apple.TrueType.CFF.combined"
+ "com.apple.font.format.installable"
+ "compatibility"
+ "copy"
+ "crc"
+ "dataWithContentsOfFile:"
+ "dataWithContentsOfURL:options:error:"
+ "def"
+ "default"
+ "detailed"
+ "div with too few operands"
+ "dup"
+ "eexec"
+ "eexec section did not decrypt to a Private dictionary (wrong key or corrupt data)."
+ "end"
+ "failureCode"
+ "fileHandleForReading"
+ "fileHandleWithNullDevice"
+ "fileSystemRepresentation"
+ "file_failed"
+ "filename"
+ "findingClass"
+ "findingWithDict:"
+ "findingsWithArray:"
+ "full"
+ "getResourceValue:forKey:error:"
+ "glyph does not set width (hsbw/sbw) before drawing"
+ "iOS"
+ "inputURL"
+ "install"
+ "issue"
+ "issues"
+ "kFontValidationExperimental"
+ "kFontValidationStandaloneCFF"
+ "macOS"
+ "maxCode"
+ "max_code"
+ "maximum"
+ "medium"
+ "message"
+ "messages"
+ "minimum"
+ "minimum|medium|default|strict|maximum"
+ "noaccess"
+ "notvalidated"
+ "oldSummary"
+ "operand stack overflow"
+ "osInstallable"
+ "os_installable"
+ "pipe"
+ "platform not specified"
+ "put"
+ "rb"
+ "readDataToEndOfFile"
+ "readhexstring"
+ "readonly"
+ "readstring"
+ "security"
+ "setFailureCode:"
+ "setFindingClass:"
+ "setMessages:"
+ "setStandardError:"
+ "setStandardOutput:"
+ "setSymLinkedURL:"
+ "setWithArray:"
+ "static report type not specified\n"
+ "strict"
+ "stringByAppendingString:"
+ "subSeverities"
+ "subSeverity"
+ "subroutine recursion too deep"
+ "summary"
+ "symLinkedURL"
+ "truncated 32-bit operand"
+ "truncated escape operator"
+ "truncated operand"
+ "tvOS"
+ "unknown escape operator 12 "
+ "unknown operator "
+ "usability"
+ "v20@0:8i16"
+ "validateall"
+ "validation level not specified (expected minimum|medium|default|strict|maximum)\n"
+ "visionOS"
+ "warningFindings"
+ "watchOS"
+ "woff2_"
+ "woff_"
+ "‘NFNT’"
+ "‘cff ’"
+ "‘cff2’"
+ "‘cid ’"
+ "‘dfnt’"
+ "‘hvf ’"
+ "‘lwfn’"
+ "‘pfa ’"
+ "‘pfb ’"
+ "‘sfnt’"
+ "‘ttcf’"
+ "‘typ1’"
+ "‘woff’"
- "\t\t-apple_fonts    Report Apple fonts as error (Apps should not bundle them)\n\t\t-car_files      Inspect .car files for fonts. NOTE: it will turn on -local for in-process validation\n\t\t-tag_asset_info Extracts tag and asset names from asset car plist and data. Provides cleaner output but is slower\n\t\t-carutil_path   Path to carutil tool. Default is /usr/local/bin/carutil\n\t\t-multi_thread   Run multi-threaded. Only available with -local\n\t\t-greedy         Adjusts priorities for operation queues to be high user level priorities. Makes sense only with -multi-thread\n\t\t-tmp_dir        Specify location where temporary files may be written\n"
- "\n\n\tValidates font files are adequate to use with the OS. If a directory is specified, it recursively examines font files found\n\n\t\t-local          Performs all validation in-process. Default validation is performed by a separate process\n\t\t-quiet          Suppress progress information and errors\n\t\t-ios_only       Fonts not supported by iOS are treated as errors\n\t\t-duplicates     check for duplicates\n\t\t-dynamic        perform dynamic validation (runtime checks against ATS/CT APIs)\n\t\t-only_fonts     Any file that isn't a font file will be reported as an error\n%s\t\t-pedantic       Reports non-font files as errors\n\t\t-showSuccesses  Report shows names of successful tests\n\t\t-showWarnings   Report shows warnings\n\t\t-warningAsError Warning presence indicates validation failure. (-showWarnings implied)\n\t\t-report_output  Specify a file to hold the report. If not specified stdout will be used\n\t\t-relative_path  File paths in report are relative to the base path passed in. Warning: this may yield similar paths if 2 input directorys contain similar directory structures\n\t\n\n\tVersion %s\n"
- "%s is not supported by iOS\n"
- "-apple_fonts"
- "-apple_fonts -car_files -tag_asset_info -multi_thread -greedy -carutil_path [PATH_TO_EXECUTABLE] -tmp_dir [PATH_TMP_DIR] "
- "-car_files"
- "-carutil_path"
- "-ios_only"
- "-multi-thread"
- "-multi_thread"
- "-only_fonts"
- "-relative_path"
- "-report_output"
- "-tag_asset_info"
- "-tmp_dir"
- "3.0.2"
- "<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><dict><key>kATSFontTestCreateReportTypeKey</key><string>kATSFontTestReportTypeSummary</string><key>kATSFontTestFontsTestedKey</key><array><dict><key>kATSFontTestArrayKey</key><array><dict><key>kATSFontTestDescriptionKey</key><string>This test ensures the ‘name’ table is valid.</string><key>kATSFontTestIdentifierKey</key><string>com.apple.TrueType.name.usability</string><key>kATSFontTestNameKey</key><string>‘name’ table usability</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string></array><key>kATSFontTestSeverityKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityTechnicalError</string></array><key>kATSFontTestTargetKey</key><array><string>kATSFontTest_nameTable</string></array><key>kATSFontTestTimeStampKey</key><string>2026-05-08 21:33:18 +0000</string><key>kATSFontTestTypeKey</key><array><string>kATSFontTestUsabilityTest</string><string>kATSFontTestStructureTest</string></array><key>kATSFontTestVersionKey</key><integer>1</integer></dict></array><key>kATSFontTestFontIdentifierKey</key><string>2671EC3A|#FONT_NAME_HERE#</string><key>kATSFontTestFontNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontPostScriptNameKey</key><string>#FONT_NAME_HERE#</string><key>kATSFontTestFontTypeKey</key><string>kATSFontTestTrueTypeFontData</string><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array></dict></array><key>kATSFontTestForceTestExecutionKey</key><integer>1</integer><key>kATSFontTestResultKey</key><array><string>kATSFontTestSeverityFatalError</string><string>kATSFontTestSeverityMajorError</string><string>kATSFontTestSeverityInformation</string></array><key>kATSFontTestUseSandboxOptionKey</key><integer>0</integer></dict></plist>"
- "Usage:\n\t%s [-help -version -local -quiet -ios_only -pedantic %s[-report|-report_output OUTPUT_FILE_PATH -relative_path] [FONT_FILE_OR_DIR_PATH...]]"
```
