## PDFKit

> `/System/Library/Frameworks/PDFKit.framework/PDFKit`

```diff

-1266.3.2.0.0
-  __TEXT.__text: 0xac7ec
-  __TEXT.__auth_stubs: 0x2670
-  __TEXT.__objc_methlist: 0x8a34
+1266.4.2.0.0
+  __TEXT.__text: 0xacc08
+  __TEXT.__auth_stubs: 0x2690
+  __TEXT.__objc_methlist: 0x8a54
   __TEXT.__const: 0x6e0
-  __TEXT.__cstring: 0x6a4a
-  __TEXT.__gcc_except_tab: 0x1ae4
+  __TEXT.__cstring: 0x6a92
+  __TEXT.__gcc_except_tab: 0x1b14
   __TEXT.__dlopen_cstrs: 0x162
   __TEXT.__ustring: 0xb4
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__unwind_info: 0x2bc0
+  __TEXT.__unwind_info: 0x2be0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x10ed
-  __TEXT.__objc_methname: 0x173af
-  __TEXT.__objc_methtype: 0x641f
-  __TEXT.__objc_stubs: 0x14420
-  __DATA_CONST.__got: 0x4f0
+  __TEXT.__objc_methname: 0x174ed
+  __TEXT.__objc_methtype: 0x6493
+  __TEXT.__objc_stubs: 0x14460
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__const: 0x1d80
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xdfe8
-  __DATA_CONST.__objc_selrefs: 0x60f8
+  __DATA_CONST.__objc_const: 0xe008
+  __DATA_CONST.__objc_selrefs: 0x6108
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x828
+  __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x148
   __AUTH_CONST.__cfstring: 0x7660
   __AUTH_CONST.__objc_const: 0x2d18

   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1350
+  __AUTH_CONST.__auth_got: 0x1360
   __AUTH.__objc_data: 0x28f0
   __DATA.__got_weak: 0x8
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x828
-  __DATA.__objc_superrefs: 0x268
   __DATA.__objc_ivar: 0xc2c
   __DATA.__data: 0x11a0
   __DATA.__bss: 0x300

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7730FAF-5A73-3DF0-B159-74E866C9B160
-  Functions: 3361
-  Symbols:   12849
-  CStrings:  7014
+  UUID: E731A8F1-43F2-3258-BBDC-9B2FBAB271D4
+  Functions: 3367
+  Symbols:   12868
+  CStrings:  7031
 
Symbols:
+ +[PDFAnnotationDrawing drawAppearance:ofAnnotation:withBox:inContext:scaleProportional:suppressTextRendering:]
+ +[PDFPageAnalyzer _normalizedToPageTransformForPage:displayBox:boxHeight:]
+ -[PDFAnnotation drawAppearance:withBox:inContext:inRect:scaleProportional:suppressTextRendering:]
+ -[PDFPage copyDisplayList]
+ -[PDFPage ensureDisplayList]
+ -[PDFPageAnalyzer _addFormElementsFromAnalysis:displayBox:toPage:]
+ GCC_except_table312
+ GCC_except_table318
+ GCC_except_table35
+ GCC_except_table74
+ _CGDisplayListRetain
+ __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ue170006IPU8__strongP20PDFDetectedFormFieldS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8ue170006IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8ue170006IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS2_EEEclB8ue170006Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS2_EclB8ue170006Ev
+ __ZNKSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt9type_infoeqB8ue170006ERKS_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B8ue170006EOS5_
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B8ue170006Ev
+ __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB8ue170006ES3_
+ __ZNSt3__113__lower_boundB8ue170006INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES7_S5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_T1_RKT2_RT4_RT3_
+ __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE28__construct_at_end_with_sizeINS_13move_iteratorIPS1_EEEEvT_m
+ __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE5clearB8ue170006Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEEPvEEEEE7destroyB8ue170006INS_4pairIKdSA_EEvvEEvRSE_PT_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI18PDFDetectedFormRowEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIPK18CGDisplayListEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIU8__strongP20PDFDetectedFormFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119piecewise_constructE
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__121__unwrap_and_dispatchB8ue170006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
+ __ZNSt3__121__unwrap_and_dispatchB8ue170006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
+ __ZNSt3__125__throw_bad_function_callB8ue170006Ev
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS3_EEEEED2B8ue170006Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS3_EEED2B8ue170006Ev
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorI18PDFDetectedFormRowEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__14pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEC2B8ue170006IRdRS8_LPv0EEEOT_OT0_
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE22__construct_one_at_endB8ue170006IJS1_EEEvDpOT_
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE16__init_with_sizeB8ue170006IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__init_with_sizeB8ue170006IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE18__assign_with_sizeB8ue170006IPS3_S8_EEvT_T0_l
+ __ZNSt3__19__advanceB8ue170006INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___66-[PDFPageAnalyzer _addFormElementsFromAnalysis:displayBox:toPage:]_block_invoke
+ ___66-[PDFPageAnalyzer _addFormElementsFromAnalysis:displayBox:toPage:]_block_invoke_2
+ ___block_descriptor_104_ea8_32s40s48s56s64bs_e38_v24?0"VKCImageAnalysis"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_120_ea8_32s40s48s56s_e38_"PDFAnnotation"16?0"VKCFormRegion"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.45
+ _kCGContextBoundingBox
+ _memmove
+ _objc_msgSend$_addFormElementsFromAnalysis:displayBox:toPage:
+ _objc_msgSend$_normalizedToPageTransformForPage:displayBox:boxHeight:
+ _objc_msgSend$copyDisplayList
+ _objc_msgSend$drawAppearance:ofAnnotation:withBox:inContext:scaleProportional:suppressTextRendering:
+ _objc_msgSend$drawAppearance:withBox:inContext:inRect:scaleProportional:suppressTextRendering:
+ _objc_msgSend$ensureDisplayList
- +[PDFPageAnalyzer _normalizedToPageTransformForPageWithBounds:]
- -[PDFPage displayList]
- -[PDFPage getDisplayListSynchronously]
- -[PDFPageAnalyzer _addFormElementsFromAnalysis:bounds:toPage:]
- GCC_except_table311
- GCC_except_table317
- GCC_except_table47
- GCC_except_table58
- GCC_except_table67
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB7v160006IPU8__strongP20PDFDetectedFormFieldS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB7v160006IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB7v160006IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt9type_infoeqB7v160006ERKS_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B7v160006EOS5_
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B7v160006Ev
- __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB7v160006ES3_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeIdN10applesauce2CF9ObjectRefIPK8__CTFontEEEEPvEEEEE7destroyB7v160006INS_4pairIKdSA_EEvvEEvRSE_PT_
- __ZNSt3__118__lower_bound_implB7v160006INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES7_S5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_T1_RKT2_RT4_RT3_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI18PDFDetectedFormRowEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIPK18CGDisplayListEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIU8__strongP20PDFDetectedFormFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__125__throw_bad_function_callB7v160006Ev
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_6vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS4_EEE16__destroy_vectorEED2B7v160006Ev
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorI18PDFDetectedFormRowEEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__14pairIKdN10applesauce2CF9ObjectRefIPK8__CTFontEEEC2B7v160006IRdRS8_LPv0EEEOT_OT0_
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEED2B7v160006Ev
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEEC2ERKS6_
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE6assignIPS3_Li0EEEvT_S9_
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEEC2ERKS6_
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEED2B7v160006Ev
- __ZNSt3__19__advanceB7v160006INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZNSt3__1L19piecewise_constructE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___62-[PDFPageAnalyzer _addFormElementsFromAnalysis:bounds:toPage:]_block_invoke
- ___62-[PDFPageAnalyzer _addFormElementsFromAnalysis:bounds:toPage:]_block_invoke_2
- ___block_descriptor_136_ea8_32s40s48s56s64bs_e38_v24?0"VKCImageAnalysis"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_144_ea8_32s40s48s56s_e38_"PDFAnnotation"16?0"VKCFormRegion"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.44
- _objc_msgSend$_addFormElementsFromAnalysis:bounds:toPage:
- _objc_msgSend$_normalizedToPageTransformForPageWithBounds:
- _objc_msgSend$displayList
- _objc_msgSend$getDisplayListSynchronously
CStrings:
+ "/AppleInternal/Library/BuildRoots/ce7a2ab7-ccb4-11ee-8860-1e1d6dc629d0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
+ "T@\"<NSObject><NSCopying>\",?,R"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIView\",?,R,N"
+ "T@,?,R,N"
+ "TB,?"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R"
+ "TB,?,R,N"
+ "TQ,?"
+ "TQ,?,R"
+ "Td,?"
+ "Tq,?,N"
+ "_addFormElementsFromAnalysis:displayBox:toPage:"
+ "_normalizedToPageTransformForPage:displayBox:boxHeight:"
+ "analyzePageBlock: (page #%lu) FINISHED generating page image (+%g secs)"
+ "caretTransformForPosition:"
+ "copyDisplayList"
+ "drawAppearance:ofAnnotation:withBox:inContext:scaleProportional:suppressTextRendering:"
+ "drawAppearance:withBox:inContext:inRect:scaleProportional:suppressTextRendering:"
+ "ensureDisplayList"
+ "v40@0:8@16q24@32"
+ "v52@0:8i16@20q28^{CGContext=}36B44B48"
+ "v80@0:8^{CGPDFForm=}16q24^{CGContext=}32{CGRect={CGPoint=dd}{CGSize=dd}}40B72B76"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}40@0:8@16q24^d32"
- "/AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/System/Library/Frameworks/CoreGraphics.framework/PrivateHeaders/CGBuf.h"
- "T@\"<NSObject><NSCopying>\",R"
- "T@\"NSString\",R,C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@,R,N"
- "TB,N,GisSecureTextEntry"
- "TB,R"
- "Td"
- "_addFormElementsFromAnalysis:bounds:toPage:"
- "_normalizedToPageTransformForPageWithBounds:"
- "getDisplayListSynchronously"
- "v64@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56"
- "{CGAffineTransform=dddddd}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"

```
