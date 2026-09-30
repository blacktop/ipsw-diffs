## CharacterPicker

> `/System/Library/PrivateFrameworks/CharacterPicker.framework/Versions/A/CharacterPicker`

```diff

-249.228.200.0.0
-  __TEXT.__text: 0x51b84
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x6084
-  __TEXT.__cstring: 0x3266
+249.308.200.0.0
+  __TEXT.__text: 0x5433c
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_methlist: 0x6eac
+  __TEXT.__cstring: 0x328b
   __TEXT.__const: 0x6d1
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__oslogstring: 0xd14
+  __TEXT.__gcc_except_tab: 0x7f4
+  __TEXT.__oslogstring: 0xe92
   __TEXT.__ustring: 0x28
   __TEXT.__dlopen_cstrs: 0x34a
-  __TEXT.__unwind_info: 0x1758
-  __TEXT.__objc_classname: 0xb51
-  __TEXT.__objc_methname: 0x12dde
-  __TEXT.__objc_methtype: 0x4d71
-  __TEXT.__objc_stubs: 0xd980
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x608
+  __TEXT.__unwind_info: 0x17c8
+  __TEXT.__objc_classname: 0xb5c
+  __TEXT.__objc_methname: 0x12ee5
+  __TEXT.__objc_methtype: 0x4d92
+  __TEXT.__objc_stubs: 0xd9e0
+  __DATA_CONST.__got: 0x768
+  __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x45e8
+  __DATA_CONST.__objc_selrefs: 0x4ad8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x438
-  __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x1590
-  __AUTH_CONST.__cfstring: 0x3aa0
-  __AUTH_CONST.__objc_const: 0xe0f0
+  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__const: 0x15c0
+  __AUTH_CONST.__cfstring: 0x3ae0
+  __AUTH_CONST.__objc_const: 0xc6f8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH.__objc_data: 0x1950
-  __DATA.__objc_ivar: 0x764
+  __DATA.__objc_ivar: 0x768
   __DATA.__data: 0xb50
   __DATA.__bss: 0x370
   __DATA_DIRTY.__objc_data: 0x4b0

   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/Versions/A/EmojiFoundation
   - /System/Library/PrivateFrameworks/InputAnalytics.framework/Versions/A/InputAnalytics
+  - /System/Library/PrivateFrameworks/InputToolKit.framework/Versions/A/InputToolKit
+  - /System/Library/PrivateFrameworks/InputToolKitUI.framework/Versions/A/InputToolKitUI
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/Stickers.framework/Versions/A/Stickers

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: D85F5F3F-63B4-389B-A14C-2A0976BE177D
-  Functions: 2444
-  Symbols:   6614
-  CStrings:  4963
+  UUID: 9C6A31B7-1894-33E3-8504-A33A489237F3
+  Functions: 2503
+  Symbols:   6684
+  CStrings:  4981
 
Symbols:
+ +[CPCharacterDatabase sharedDatabase].cold.1
+ +[CPKCache emojiLocaleData].cold.1
+ +[CPKCalculatedGeometry geometryForEmojiWithCombinedSetting:].cold.1
+ +[CPKCalculatedGeometry geometryForEmojiWithCombinedSetting:].cold.2
+ +[CPKCalculatedGeometry geometryForImageGlyphs].cold.1
+ +[CPKCalculatedGeometry geometryForSymbols].cold.1
+ +[CPKCategoryData _stickersAndEmojiToSymbolSFMapping].cold.1
+ +[CPKCategoryData tooltipIdentifierForItemKey:].cold.1
+ +[CPKDefaultDataSource preferredEmojiLocale].cold.1
+ +[CPKEmojiGraphics macOSDefaultEmojiGraphicsWithCombinedSetting:].cold.1
+ +[CPKEmojiGraphics macOSDefaultEmojiGraphicsWithCombinedSetting:].cold.2
+ +[CPKEmojiIMSharedResources CPDataClass].cold.1
+ +[CPKEmojiIMSharedResources sharedInstance].cold.1
+ +[CPKGenerationRemoteViewController serviceViewControllerInterface].cold.1
+ +[CPKGenmojiListener sharedListener].cold.1
+ +[CPKPreferences sharedPreferences].cold.1
+ +[CPKSignalAnalytics getIAGenmojiImageTypeFromImageGlyph:].cold.2
+ +[CPKState state].cold.1
+ +[CPKStickersDataSource sharedSource].cold.1
+ +[CPKSuggestedEmojiController sharedController].cold.1
+ +[CPSearchManager sharedSearchManager].cold.1
+ -[CPKFont initWithName:size:].cold.1
+ -[CPKPopover .cxx_destruct]
+ -[CPKPopover identifier]
+ -[CPKPopover privateStorage]
+ -[CPKPopover setDataSource:usingBlockOnMainThread:].cold.1
+ -[CPKPopover setIdentifier:]
+ -[CPKPopover setPrivateStorage:]
+ -[CPKPopoverController initWithController:].cold.1
+ -[CPKPopoverController initWithEmojiCreationMode:popover:]
+ -[CPKPopoverController initWithUICreation:emojiCreationMode:popover:]
+ -[CPKPrivateStorage .cxx_destruct]
+ -[CPKSearchView isRTL]
+ -[CPKSuggestedEmojiController emojisAndStickersForString:leftContext:language:].cold.1
+ -[CPSearchManager emojiTokensForSearchString:inLanguages:maxResults:usingBlock:].cold.1
+ -[RemoteGenerationViewService exportedInterface].cold.1
+ -[RemoteGenerationViewService remoteViewControllerInterface].cold.1
+ CPKLoggingGetDefaultLog.cold.1
+ CPKLoggingGetUserInterfaceLog.cold.1
+ CPKShowGenmojiCreationFirstOnNextSession.cold.1
+ CPKShowGenmojiCreationFirstOnNextSession.cold.2
+ CPKSignalAnalyticsLog.cold.1
+ CPXPCConnection.cold.1
+ CPXPCQueue.cold.1
+ EmojiPickerSignpostLog.cold.1
+ GCC_except_table25
+ GCC_except_table41
+ GCC_except_table59
+ GCC_except_table63
+ IsWorkingInCharacterViewer.cold.1
+ IsWorkingInEmojiDFRIM.cold.1
+ LogCurrentTimeWithType.cold.1
+ LogEmojiDFRCurrentTime.cold.1
+ OBJC_IVAR_$_CPKPopover._identifier
+ OBJC_IVAR_$_CPKPopover._privateStorage
+ RemoteGenerationViewServiceLogger.cold.1
+ SetGetKeyedGlobalParam.cold.1
+ SharedEmojiPreference.cold.1
+ ShouldDrawPreReleaseStamp.cold.1
+ _AddCharactersViewToArbitrator.cold.1
+ _CPKGenmojiCreationIsAvailable
+ _CPKPrivateSettingsPasteboardName
+ _CPKShouldShowGenmojiCreationFirstOnNextSession.cold.1
+ _CPKShowGenmojiCreationFirstOnNextSession
+ _GetStateValue.cold.1
+ _IsCombinedPicker.cold.1
+ _NoGlyphExistForLongCharacter.cold.1
+ _OUTLINED_FUNCTION_4
+ _SetValueAndReturnChangeStatus.cold.1
+ _StateChangeDictionary.cold.1
+ _SystemSupportsGenmoji.cold.1
+ _SystemSupportsGenmoji.cold.2
+ _SystemSupportsGenmoji.generativeModelsAvailabilityClass
+ _SystemSupportsGenmoji.onceToken
+ __30-[CPKPopover _popoverDidOpen:]_block_invoke.408
+ __51-[CPKPopover setDataSource:usingBlockOnMainThread:]_block_invoke.238
+ __51-[CPKPopover setDataSource:usingBlockOnMainThread:]_block_invoke_2.240
+ __CPKShouldShowGenmojiCreationFirstOnNextSession
+ __SystemSupportsGenmoji
+ __ZNKSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEE13__get_deleterERKSt9type_info
+ __ZNKSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEE13__get_deleterERKSt9type_info
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPS4_EclB8ne190102Ev
+ __ZNKSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110shared_ptrI11_STKStickerEC2B8ne190102IS1_Z18make_ns_shared_ptrIS1_ENS0_IT_EEPS5_EUlP11objc_objectE_Li0EEES7_T0_
+ __ZNSt3__110shared_ptrI13EMFEmojiTokenEC2B8ne190102IS1_Z18make_ns_shared_ptrIS1_ENS0_IT_EEPS5_EUlP11objc_objectE_Li0EEES7_T0_
+ __ZNSt3__114__split_bufferINS_10shared_ptrI11_STKStickerEERNS_9allocatorIS3_EEE5clearB8ne190102Ev
+ __ZNSt3__114__split_bufferINS_10shared_ptrI13EMFEmojiTokenEERNS_9allocatorIS3_EEE5clearB8ne190102Ev
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI11_STKStickerEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10shared_ptrI13EMFEmojiTokenEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEED1Ev
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEED0Ev
+ __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEED1Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI8_NSRangeNS_6vectorINS_10shared_ptrI11_STKStickerEENS1_IS8_EEEEEEPvEEEEEclB8ne190102EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI8_NSRangeNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS1_IS8_EEEEEEPvEEEEEclB8ne190102EPSD_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEbT1_S7_T0_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPS5_EEED2B8ne190102Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
+ __ZNSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEjT1_S7_S7_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEvT1_S7_S7_S7_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZTINSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ __ZTINSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ __ZTSNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ __ZTVNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS7_EEEE
+ ___31-[CPKPopover windowWillClosed:]_block_invoke
+ ____SystemSupportsGenmoji_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSEvent"8l
+ ___block_descriptor_48_e8_32s40s_e26_"NSEvent"16?0"NSEvent"8l
+ ___block_descriptor_72_e8_32s40s48s_e48_v24?0"NSEmojiImageTextAttachment"8"NSError"16l
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s_e5_v8?0l
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s
+ ___copy_helper_block_e8_32s40s48s
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___copy_helper_block_e8_32s40s48s56s64s
+ ___copy_helper_block_e8_32s40s48s56s64s72b
+ ___destroy_helper_block_e8_32s40s
+ ___destroy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ __block_literal_global.115
+ __block_literal_global.143
+ __block_literal_global.22
+ __block_literal_global.31
+ __block_literal_global.46
+ _itk_dispatchMainAfterDelay
+ _memcpy
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$characterPickerPopoverShouldImmediatelyResign
+ _objc_msgSend$initWithEmojiCreationMode:popover:
+ _objc_msgSend$initWithUICreation:emojiCreationMode:popover:
+ _objc_msgSend$pasteboardWithName:
+ _objc_msgSend$privateStorage
+ _objc_msgSend$setPrivateStorage:
+ _objc_retainBlock
- -[CPKPopover _privateStorage]
- -[CPKPopoverController initWithUICreation:]
- -[CPKPrivateStorage dealloc]
- GCC_except_table1
- GCC_except_table20
- GCC_except_table29
- GCC_except_table37
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table64
- GCC_except_table65
- GCC_except_table67
- OBJC_IVAR_$_CPKPopover._CPKPrivate
- _OBJC_CLASS_$_NSAutoreleasePool
- _SupportsGenmoji.generativeModelsAvailabilityClass
- _SupportsGenmoji.onceToken
- __30-[CPKPopover _popoverDidOpen:]_block_invoke.256
- __51-[CPKPopover setDataSource:usingBlockOnMainThread:]_block_invoke.87
- __51-[CPKPopover setDataSource:usingBlockOnMainThread:]_block_invoke_2.89
- __ZNKSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEE13__get_deleterERKSt9type_info
- __ZNKSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEE13__get_deleterERKSt9type_info
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEENS_16reverse_iteratorIPS4_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPS4_EclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI13EMFEmojiTokenEEEENS_16reverse_iteratorIPS4_EEEclB8ne180100Ev
- __ZNKSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110shared_ptrI11_STKStickerEC2B8ne180100IS1_Z18make_ns_shared_ptrIS1_ENS0_IT_EEPS5_EUlP11objc_objectE_vEES7_T0_
- __ZNSt3__110shared_ptrI13EMFEmojiTokenEC2B8ne180100IS1_Z18make_ns_shared_ptrIS1_ENS0_IT_EEPS5_EUlP11objc_objectE_vEES7_T0_
- __ZNSt3__114__split_bufferINS_10shared_ptrI11_STKStickerEERNS_9allocatorIS3_EEE5clearB8ne180100Ev
- __ZNSt3__114__split_bufferINS_10shared_ptrI13EMFEmojiTokenEERNS_9allocatorIS3_EEE5clearB8ne180100Ev
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10shared_ptrI11_STKStickerEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10shared_ptrI13EMFEmojiTokenEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEED1Ev
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEED0Ev
- __ZNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEED1Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI8_NSRangeNS_6vectorINS_10shared_ptrI11_STKStickerEENS1_IS8_EEEEEEPvEEEEEclB8ne180100EPSD_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeI8_NSRangeNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS1_IS8_EEEEEEPvEEEEEclB8ne180100EPSD_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEbT1_S7_T0_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEENS_16reverse_iteratorIPS5_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPS5_EEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10shared_ptrI13EMFEmojiTokenEEEENS_16reverse_iteratorIPS5_EEEEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_10shared_ptrI11_STKStickerEEEEPKS4_S7_PS4_EET2_RT_T0_T1_S9_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10shared_ptrI11_STKStickerEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10shared_ptrI13EMFEmojiTokenEEEENS_16reverse_iteratorIPS4_EES8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS3_RS5_EE
- __ZNSt3__16vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS3_EEE7__clearB8ne180100Ev
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEjT1_S7_S7_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZNK29MatchingRangesToResultsMapper24copyUniqueMatchingRangesEbE3$_0P8_NSRangeEEvT1_S7_S7_S7_T0_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZTINSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- __ZTINSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- __ZTSNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- __ZTSNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI11_STKStickerEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper20_getStickersForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- __ZTVNSt3__120__shared_ptr_pointerIPKNS_6vectorINS_10shared_ptrI13EMFEmojiTokenEENS_9allocatorIS4_EEEEZNK29MatchingRangesToResultsMapper18_getEmojisForRangeERK8_NSRangeE3$_0NS5_IS8_EEEE
- ____SupportsGenmoji_block_invoke
- ___block_descriptor_48_e8_32o40o_e17_v16?0"NSEvent"8l
- ___block_descriptor_48_e8_32o40o_e26_"NSEvent"16?0"NSEvent"8l
- ___block_descriptor_72_e8_32o40o48o_e48_v24?0"NSEmojiImageTextAttachment"8"NSError"16l
- ___block_descriptor_81_e8_32o40o48o56o64b_e5_v8?0l
- ___block_descriptor_88_e8_32o40o48o56o64o_e5_v8?0l
- ___block_descriptor_89_e8_32o40o48o56o64o72b_e5_v8?0l
- ___copy_helper_block_e8_32o40o48o56o64o
- ___copy_helper_block_e8_32o40o48o56o64o72b
- ___destroy_helper_block_e8_32o40o48o56o64o
- ___destroy_helper_block_e8_32o40o48o56o64o72b
- __block_literal_global.114
- __block_literal_global.142
- __block_literal_global.19
- __block_literal_global.28
- __block_literal_global.43
- _objc_msgSend$characterPickerPopoverShouldImmediatelyResign:
- _objc_msgSend$drain
- _objc_msgSend$initWithUICreation:
CStrings:
+ "2H"
+ "@\"CPKPrivateStorage\""
+ "@\"NSUUID\""
+ "@32@0:8B16B20@24"
+ "Adam: Layout is RTL %d"
+ "During CPKPopoverController initWithController, template controller is nonnil, but state dict is nil, bypassing state dictionary %@"
+ "EmojiPicker: flag: %d, hardwareSupported: %d, gmsAvailability: %d, supports: %d"
+ "EmojiPicker: supportedByTextField: %d, supported by system: %d, supports: %d"
+ "Failed to write to pasteboard"
+ "Reading ShouldShowGenmojiCreationFirstOnNextSession=%d"
+ "Setting ShouldShowGenmojiCreationFirstOnNextSession=1, ret=%d"
+ "T@\"<CPKCharacterEntity>\",&,N,V_lastSelectedEntity"
+ "T@\"<CPKPopoverDelegate>\",W,V_CPKDelegate"
+ "T@\"<CPKTargetProvider>\",W,V_CPKTargetProvider"
+ "T@\"CPKDataProvider\",&,N,V_delayedSettingProvider"
+ "T@\"CPKPopoverController\",&,N,V_tempRetainer"
+ "T@\"CPKPrivateStorage\",&,N,V_privateStorage"
+ "T@\"CPKWindow\",&,N,V_detachedWindow"
+ "T@\"CPKWindow\",&,N,V_detachingWindow"
+ "T@\"EMFEmojiLocaleData\",&,N,V_emojiLocaleData"
+ "T@\"EMFEmojiPreferences\",&,N,V_emojiPreference"
+ "T@\"NSDictionary\",&,N,V_selectionAttributeForTextView"
+ "T@\"NSUUID\",C,N,V_identifier"
+ "T@\"NSView\",W,N,V_positioningView"
+ "T@\"NSWindow\",W,N,V_alternateLargeWindow"
+ "T@\"NSWindow\",W,N,V_lastKeyWindow"
+ "T@,&,N,V_globalEventMonitor"
+ "T@,&,N,V_localEventMonitor"
+ "T@,&,V_CPKUserInfo"
+ "T@,W,N,V_lastActionObject"
+ "TB,N,V_displayAsWindow"
+ "TB,N,V_displayingPopover"
+ "TB,N,V_lastTargetValidation"
+ "TB,N,V_needsRebuildView"
+ "TB,N,V_settingDataSource"
+ "TB,N,V_showEmojiOnly"
+ "TB,N,V_showingLargeWindow"
+ "TB,N,V_skipOpeningAnimation"
+ "TQ,N,V_preferredEdge"
+ "Tq,N,V_detachedWindowLevel"
+ "T{CGPoint=dd},N,V_displayAsWindowLoc"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_positioningRect"
+ "T{_NSRange=QQ},N,V_lastSelectionOnTarget"
+ "__CPKPrivateSettingsPasteboardName"
+ "characterPickerPopoverShouldImmediatelyResign"
+ "initWithEmojiCreationMode %d"
+ "initWithEmojiCreationMode:popover:"
+ "initWithUICreation:emojiCreationMode:popover:"
+ "pasteboardWithName:"
+ "privateStorage"
+ "setPrivateStorage:"
- "EmojiPicker: flag: %d, hardwareSupported: %d, supportedByTextField: %d, gmsAvailability: %d, supports: %d"
- "T@\"<CPKCharacterEntity>\",&,V_lastSelectedEntity"
- "T@\"<CPKPopoverDelegate>\",V_CPKDelegate"
- "T@\"<CPKTargetProvider>\",V_CPKTargetProvider"
- "T@\"CPKDataProvider\",&,V_delayedSettingProvider"
- "T@\"CPKPopoverController\",&,V_tempRetainer"
- "T@\"CPKWindow\",&,V_detachedWindow"
- "T@\"CPKWindow\",&,V_detachingWindow"
- "T@\"EMFEmojiLocaleData\",&,V_emojiLocaleData"
- "T@\"EMFEmojiPreferences\",&,V_emojiPreference"
- "T@\"NSDictionary\",&,V_selectionAttributeForTextView"
- "T@\"NSView\",V_positioningView"
- "T@\"NSWindow\",V_alternateLargeWindow"
- "T@,&,V_globalEventMonitor"
- "T@,&,V_localEventMonitor"
- "T@,V_lastActionObject"
- "TB,V_displayAsWindow"
- "TB,V_displayingPopover"
- "TB,V_lastTargetValidation"
- "TB,V_needsRebuildView"
- "TB,V_settingDataSource"
- "TB,V_showEmojiOnly"
- "TB,V_showingLargeWindow"
- "TB,V_skipOpeningAnimation"
- "TQ,V_preferredEdge"
- "T^v,V_CPKUserInfo"
- "Tq,V_detachedWindowLevel"
- "T{CGPoint=dd},V_displayAsWindowLoc"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},V_positioningRect"
- "T{_NSRange=QQ},V_lastSelectionOnTarget"
- "^v"
- "_CPKPrivate"
- "characterPickerPopoverShouldImmediatelyResign:"
- "drain"
- "initWithUICreation:"
- "v24@0:8^v16"

```
