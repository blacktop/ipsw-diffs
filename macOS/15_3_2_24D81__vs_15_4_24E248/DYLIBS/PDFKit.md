## PDFKit

> `/System/iOSSupport/System/Library/Frameworks/PDFKit.framework/Versions/A/PDFKit`

```diff

-1332.3.9.0.0
-  __TEXT.__text: 0xaa208
+1332.4.5.4.1
+  __TEXT.__text: 0xa9824
   __TEXT.__auth_stubs: 0x2ad0
-  __TEXT.__objc_methlist: 0x89c4
+  __TEXT.__objc_methlist: 0x9f8c
   __TEXT.__const: 0x844
   __TEXT.__cstring: 0x6459
-  __TEXT.__gcc_except_tab: 0x1740
+  __TEXT.__gcc_except_tab: 0x1718
   __TEXT.__ustring: 0xb4
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__oslogstring: 0x1a
-  __TEXT.__swift5_typeref: 0xd6
+  __TEXT.__swift5_typeref: 0xce
   __TEXT.__swift5_capture: 0x24
   __TEXT.__constg_swiftt: 0xac
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2ab0
-  __TEXT.__eh_frame: 0x15c
+  __TEXT.__unwind_info: 0x2a40
+  __TEXT.__eh_frame: 0x19c
   __TEXT.__objc_classname: 0x107e
-  __TEXT.__objc_methname: 0x1780c
-  __TEXT.__objc_methtype: 0x64ea
-  __TEXT.__objc_stubs: 0x13ca0
-  __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0x1d68
+  __TEXT.__objc_methname: 0x178bf
+  __TEXT.__objc_methtype: 0x6576
+  __TEXT.__objc_stubs: 0x13ce0
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__const: 0x1d60
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6000
+  __DATA_CONST.__objc_selrefs: 0x66d0
   __DATA_CONST.__objc_arraydata: 0x150
   __AUTH_CONST.__auth_got: 0x1580
   __AUTH_CONST.__const: 0x940
   __AUTH_CONST.__cfstring: 0x75c0
-  __AUTH_CONST.__objc_const: 0x10b48
+  __AUTH_CONST.__objc_const: 0xe320
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x90

   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0x7f0
   __DATA.__objc_superrefs: 0x268
-  __DATA.__objc_ivar: 0xc10
-  __DATA.__data: 0x1018
+  __DATA.__objc_ivar: 0xc14
+  __DATA.__data: 0x1010
   __DATA.__bss: 0x6e8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3E049303-A62A-34A3-9516-F2E34C250642
-  Functions: 3358
-  Symbols:   9424
-  CStrings:  7021
+  UUID: 8B02124D-3840-368B-AA72-F0EE56C53D99
+  Functions: 3375
+  Symbols:   9491
+  CStrings:  7032
 
Symbols:
+ +[PDFAnnotation MarkupTypeForMarkupStyle:].cold.1
+ +[PDFAnnotation PDFAnnotationKeysForRedactionDiscoverability].cold.1
+ +[PDFAnnotation PDFAnnotationKeysWithStringValues].cold.1
+ +[PDFAnnotation PDFKitAnnotationKeys].cold.1
+ +[PDFAnnotation PDFKitAnnotationUndoManagerDisplayNames].cold.1
+ +[PDFAnnotation PDFKitAppearanceDictionaryArray].cold.1
+ +[PDFAnnotation PDFKitBorderStyleArray].cold.1
+ +[PDFAnnotation PDFKitFieldTypeArray].cold.1
+ +[PDFAnnotation PDFKitHighlightingModeArray].cold.1
+ +[PDFAnnotation PDFKitSubtypeArray].cold.1
+ +[PDFAnnotation PDFMarkupColors].cold.1
+ +[PDFAnnotation PDFMarkupStyleLabels].cold.1
+ +[PDFAnnotation PDFTextBorderColors].cold.1
+ +[PDFAnnotation PDFTextColors].cold.1
+ +[PDFAnnotation PresentableStringForAnnotationKey:].cold.1
+ +[PDFAnnotation SubtypeForPDFMarkupStyle:].cold.1
+ +[PDFPage displayListCreationQueue].cold.1
+ +[PDFPageAnalyzer sharedInstance].cold.1
+ +[PDFPageEvaluator asyncWorkQueue].cold.1
+ +[PDFTilePool sharedPool].cold.1
+ +[XPCExtensionInterface extensionInterface].cold.1
+ +[XPCExtensionInterface hostInterface].cold.1
+ -[PDFAnnotation _isValidAnnotationKey:].cold.1
+ -[PDFAnnotation getPDFKeyMappingDictionary].cold.1
+ -[PDFAnnotation setValue:forAnnotationKey:].cold.1
+ -[PDFPageIconLayer updateAsPageIndex:forDocument:].cold.1
+ -[PDFRevealManager PDFRVPresenter].cold.1
+ -[PDFScannerResult containsPoint:onPageLayer:].cold.1
+ -[PDFScannerResult pointIsOnButton:onPageLayer:].cold.1
+ -[PDFScannerResult setButtonPressed:].cold.1
+ -[PDFThumbnailsCollectionView datasourceQueue].cold.1
+ -[PDFThumbnailsCollectionView imageDrawingOperationQueue].cold.1
+ -[PDFThumbnailsCollectionView supportedUTTypes].cold.1
+ -[PDFTilePool _colorizeTileEdgesForRequest:context:tileSize:].cold.1
+ -[PDFTilePool _createContextForTileSurface:ofRequest:].cold.1
+ -[PDFTilePool tileSurfacePadding]
+ AKAnnotationClass.cold.1
+ AKArrowAnnotationClass.cold.1
+ AKArrowShapeAnnotationClass.cold.1
+ AKBorderMaskAnnotationClass.cold.1
+ AKControllerClass.cold.1
+ AKCropAnnotationClass.cold.1
+ AKDidEndEditingTextAnnotationNotificationString.cold.1
+ AKDoodleAnnotationClass.cold.1
+ AKEditingTextAnnotationKeyString.cold.1
+ AKHeartAnnotationClass.cold.1
+ AKImageAnnotationClass.cold.1
+ AKInkAnnotationClass.cold.1
+ AKLoupeAnnotationClass.cold.1
+ AKOvalAnnotationClass.cold.1
+ AKPageModelControllerClass.cold.1
+ AKPolygonAnnotationClass.cold.1
+ AKRectAnnotationClass.cold.1
+ AKRedactionRectAnnotationClass.cold.1
+ AKSignatureAnnotationClass.cold.1
+ AKSpeechBubbleAnnotationClass.cold.1
+ AKStarAnnotationClass.cold.1
+ AKTextBoxAnnotationClass.cold.1
+ AKTextFieldAnnotationClass.cold.1
+ AKThoughtBubbleAnnotationClass.cold.1
+ AKToolbarViewClass.cold.1
+ AKTriangleAnnotationClass.cold.1
+ AKWillBeginEditingTextAnnotationNotificationString.cold.1
+ GCC_except_table44
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table72
+ GetDefaultsWriteAnnotationLoggingEnabled.cold.1
+ OBJC_IVAR_$_PDFTileSurface.tilePadding
+ PDFKitDeviceIsN56.cold.1
+ PDFKitDeviceIsN61.cold.1
+ PDFKitDeviceIsiPad.cold.1
+ PDFKitDeviceIsiPhone.cold.1
+ PDFMarkupMenuColorForMenuIcon.cold.1
+ PDFMarkupMenuString.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _PDFLog.cold.1
+ _UTTypeUTF8PlainText
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPU8__strongP20PDFDetectedFormFieldS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8ne190102IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8ne190102IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS2_EclB8ne190102Ev
+ __ZNKSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B8ne190102EOS5_
+ __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B8ne190102Ev
+ __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB8ne190102ES3_
+ __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE5clearB8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI18PDFDetectedFormRowEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPK18CGDisplayListEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP20PDFDetectedFormFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__123__lower_bound_bisectingB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_RKT1_NS_15iterator_traitsISB_E15difference_typeERT3_RT2_
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS3_EEED2B8ne190102Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI18PDFDetectedFormRowEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE22__construct_one_at_endB8ne190102IJS1_EEEvDpOT_
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__init_with_sizeB8ne190102IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE18__assign_with_sizeB8ne190102IPS3_S8_EEvT_T0_l
+ __ZNSt3__19__advanceB8ne190102INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___block_descriptor_81_e8_32s40s48s56s_e20_v16?0^{CGContext=}8ls32l8s40l8s48l8s56l8
+ __block_literal_global.114
+ __block_literal_global.53
+ __block_literal_global.73
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ _objc_msgSend$setContentsRect:
+ _objc_msgSend$tileSurfacePadding
- GCC_except_table46
- GCC_except_table51
- GCC_except_table61
- GCC_except_table65
- GCC_except_table74
- GCC_except_table75
- GCC_except_table76
- _UTTypeUTF16PlainText
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPU8__strongP20PDFDetectedFormFieldS7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8ne180100IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__120__move_backward_loopINS_17_ClassicAlgPolicyEEclB8ne180100IP18PDFDetectedFormRowS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS2_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS2_EclB8ne180100Ev
- __ZNKSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEEC2B8ne180100EOS5_
- __ZNSt3__110__function12__value_funcIFvP12CGPDFScannerEED2B8ne180100Ev
- __ZNSt3__110unique_ptrI12CGPDFScannerNS_8functionIFvPS1_EEEE5resetB8ne180100ES3_
- __ZNSt3__113__lower_boundB8ne180100INS_17_ClassicAlgPolicyENS_11__wrap_iterIPU8__strongP20PDFDetectedFormFieldEES7_S5_NS_10__identityEZN18PDFDetectedFormRow11insertFieldES4_EUlS4_S4_E_EET0_SB_T1_RKT2_RT4_RT3_
- __ZNSt3__114__split_bufferI18PDFDetectedFormRowRNS_9allocatorIS1_EEE5clearB8ne180100Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI18PDFDetectedFormRowEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPK18CGDisplayListEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongP20PDFDetectedFormFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_20__move_backward_loopINS_17_ClassicAlgPolicyEEENS_23__move_backward_trivialEEEPU8__strongP20PDFDetectedFormFieldSA_SA_Li0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS3_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI18PDFDetectedFormRowEEPS3_EEED2B8ne180100Ev
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorI18PDFDetectedFormRowEENS_16reverse_iteratorIPS2_EES6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorI18PDFDetectedFormRowEEPS2_S4_S4_EET2_RT_T0_T1_S5_
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI18PDFDetectedFormRowNS_9allocatorIS1_EEE22__construct_one_at_endB8ne180100IJS1_EEEvDpOT_
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIPK18CGDisplayListEntryNS_9allocatorIS3_EEE16__init_with_sizeB8ne180100IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE16__init_with_sizeB8ne180100IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE18__assign_with_sizeB8ne180100IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIU8__strongP20PDFDetectedFormFieldNS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EEPS3_
- __ZNSt3__19__advanceB8ne180100INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEEEEvRT_NS_15iterator_traitsIS7_E15difference_typeENS_26bidirectional_iterator_tagE
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___block_descriptor_77_e8_32s40s48s56s_e20_v16?0^{CGContext=}8ls32l8s40l8s48l8s56l8
- __block_literal_global.112
- __block_literal_global.52
- __block_literal_global.72
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_PDFKit
- _symbolic _____Sg 10Foundation3URLV
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "T@\"UIConversationContext\",?,&,N"
+ "conversationContext"
+ "insertInputSuggestion:"
+ "setContentsRect:"
+ "setConversationContext:"
+ "textView:insertInputSuggestion:"
+ "tilePadding"
+ "tileSurfacePadding"
+ "v24@0:8@\"UIConversationContext\"16"
+ "v24@0:8@\"UIInputSuggestion\"16"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
- "R2L"

```
