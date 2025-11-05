## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput`

```diff

-3479.227.0.0.0
-  __TEXT.__text: 0x7e848
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0xa1c4
-  __TEXT.__const: 0x480
-  __TEXT.__cstring: 0x13ee5
-  __TEXT.__ustring: 0x3f76
-  __TEXT.__dlopen_cstrs: 0x1a7
-  __TEXT.__oslogstring: 0x604
-  __TEXT.__unwind_info: 0x1cc8
-  __TEXT.__objc_classname: 0x1520
-  __TEXT.__objc_methname: 0x1815a
-  __TEXT.__objc_methtype: 0x369b
-  __TEXT.__objc_stubs: 0xc5a0
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__const: 0x14f8
-  __DATA_CONST.__objc_classlist: 0x598
-  __DATA_CONST.__objc_catlist: 0x28
+3479.319.0.0.0
+  __TEXT.__text: 0x84e44
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_methlist: 0xb138
+  __TEXT.__dlopen_cstrs: 0x24a
+  __TEXT.__const: 0x4d0
+  __TEXT.__cstring: 0x14ce8
+  __TEXT.__ustring: 0x59d8
+  __TEXT.__oslogstring: 0x663
+  __TEXT.__unwind_info: 0x1d90
+  __TEXT.__objc_classname: 0x1547
+  __TEXT.__objc_methname: 0x18f53
+  __TEXT.__objc_methtype: 0x373f
+  __TEXT.__objc_stubs: 0xcb20
+  __DATA_CONST.__got: 0x640
+  __DATA_CONST.__const: 0x15b0
+  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5108
-  __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x23fb0
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0x1a30
-  __AUTH_CONST.__cfstring: 0x38ee0
-  __AUTH_CONST.__objc_const: 0x12730
-  __AUTH_CONST.__objc_arrayobj: 0x3b88
-  __AUTH_CONST.__objc_dictobj: 0xc0d0
-  __AUTH_CONST.__objc_intobj: 0xc90
+  __DATA_CONST.__objc_selrefs: 0x53b8
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x3f8
+  __DATA_CONST.__objc_arraydata: 0x271c8
+  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__const: 0x1b80
+  __AUTH_CONST.__cfstring: 0x40480
+  __AUTH_CONST.__objc_const: 0x115f0
+  __AUTH_CONST.__objc_arrayobj: 0x3e88
+  __AUTH_CONST.__objc_dictobj: 0xc490
+  __AUTH_CONST.__objc_intobj: 0xca8
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0xb20
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0xb48
   __DATA.__data: 0xbd0
-  __DATA.__bss: 0x810
+  __DATA.__bss: 0x860
   __DATA_DIRTY.__objc_data: 0x2f30
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 18A3ADAB-9112-34B5-BE04-AE74613666D5
-  Functions: 3785
-  Symbols:   8913
-  CStrings:  16570
+  UUID: 447364BE-F2EB-393C-AAC2-F3BEED0BEC41
+  Functions: 3875
+  Symbols:   9130
+  CStrings:  17708
 
Symbols:
+ +[NSAttributedString(TIExtras) _attributedString:matchesAttributedString:]
+ +[NSAttributedString(TIExtras) _ti_attributedString:matchesAttributedStringIgnoringNullity:]
+ +[NSAttributedString(TIExtras) _ti_decodeWithCoder:forKey:attributeIterator:]
+ +[TIAttributedDocumentState _attributedString:byTrimmingWordsAfterIndex:]
+ +[TIAttributedDocumentState _attributedString:byTrimmingWordsBeforeIndex:]
+ +[TIAttributedDocumentState _selectedTextByDeletingInteriorSentences:outTruncatedRange:]
+ +[TIAttributedDocumentState attributedDocumentStateWithContextBefore:markedText:selectedRange:contextAfter:]
+ +[TIAttributedDocumentState attributedDocumentStateWithContextBefore:selectedText:contextAfter:]
+ +[TIAttributedDocumentState attributedDocumentStateWithDocumentState:]
+ +[TIAttributedDocumentState supportsSecureCoding]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithPlainText:selectedRange:]
+ +[TIAttributedDocumentState(TestSupport) attributedDocumentStateForTestingWithText:selectedRange:]
+ +[TIAttributedDocumentState(TestSupport) unboundedAttributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:]
+ +[TIAttributedDocumentState(TestSupport) unboundedAttributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:]
+ +[TIKeyboardCandidate keyboardCandidateInputStringUsedWithAutofillExtraThatSignifiesOTPExtra]
+ +[TIKeyboardSecureCandidateRGBColor darkSecondaryLabelColor]
+ +[TIKeyboardSecureCandidateRGBColor lightSecondaryLabelColor]
+ -[NSAttributedString(TIExtras) _ti_attributedStringByAppendingAttributedString:]
+ -[NSAttributedString(TIExtras) _ti_attributedStringByAppendingString:]
+ -[NSAttributedString(TIExtras) _ti_attributedStringByKeepingAttributes:]
+ -[NSAttributedString(TIExtras) _ti_attributedStringByRemovingAttributes:]
+ -[NSAttributedString(TIExtras) _ti_attributedStringWithIterator:]
+ -[NSAttributedString(TIExtras) _ti_attributedSubstringFromIndex:]
+ -[NSAttributedString(TIExtras) _ti_attributedSubstringToIndex:]
+ -[NSAttributedString(TIExtras) _ti_encodeWithCoder:forKey:attributeIterator:]
+ -[NSAttributedString(TIExtras) _ti_encodeWithCoder:forKey:keepingAttributes:]
+ -[NSAttributedString(TIExtras) _ti_encodeWithCoder:forKey:removingAttributes:]
+ -[NSAttributedString(TIExtras) _ti_stringByReplacingCharactersInRange:withString:]
+ -[NSAttributedString(TIExtras) _ti_stringByReplacingOccurrencesOfString:withString:options:range:]
+ -[NSMutableAttributedString(TIExtras) _ti_replaceOccurrencesOfString:withString:options:range:]
+ -[NSString(TIExtras) _indexByTrimmingWordsAfterIndex:]
+ -[NSString(TIExtras) _indexByTrimmingWordsBeforeIndex:]
+ -[TIAttributedDocumentState .cxx_destruct]
+ -[TIAttributedDocumentState attributedString]
+ -[TIAttributedDocumentState contextAfterInput]
+ -[TIAttributedDocumentState contextBeforeInput]
+ -[TIAttributedDocumentState copyWithZone:]
+ -[TIAttributedDocumentState description]
+ -[TIAttributedDocumentState documentIsEmpty]
+ -[TIAttributedDocumentState documentState]
+ -[TIAttributedDocumentState encodeWithCoder:]
+ -[TIAttributedDocumentState hashString:intoHashValue:]
+ -[TIAttributedDocumentState hash]
+ -[TIAttributedDocumentState initWithCoder:]
+ -[TIAttributedDocumentState initWithContextBefore:markedText:selectedText:contextAfter:selectedRangeInMarkedText:]
+ -[TIAttributedDocumentState initWithUnboundedContextBefore:markedText:selectedText:unboundedContextAfter:selectedRangeInMarkedText:]
+ -[TIAttributedDocumentState initWithUnboundedContextBefore:markedText:selectedText:unboundedContextAfter:selectedRangeInMarkedText:truncatedRangeInSelectedText:]
+ -[TIAttributedDocumentState isEqual:]
+ -[TIAttributedDocumentState isEqualIgnoringMarkedText:]
+ -[TIAttributedDocumentState isTextEqualIgnoringMarkedText:]
+ -[TIAttributedDocumentState markedText]
+ -[TIAttributedDocumentState selectedRangeInMarkedText]
+ -[TIAttributedDocumentState selectedText]
+ -[TIAttributedDocumentState string]
+ -[TIAttributedDocumentState truncatedRangeInSelectedText]
+ -[TIAttributedDocumentState(SecureCoding) documentStateWithAttributeIterator:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterCollapsingSelection]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterCursorAdjustment:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterDeletingBackward]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterDeletingForward]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterInsertingText:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterInsertingTextAfterSelection:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterReplacingText:withText:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterSettingMarkedText:selectedRange:]
+ -[TIAttributedDocumentState(StateTransitions) documentStateAfterUnmarkingText]
+ -[TIAttributedDocumentState(TestSupport) initWithText:selectedRange:]
+ -[TIInputModeController _archivedInputModeConfigurationFrom:]
+ -[TIInputModeController _inputModeConfiguration]
+ -[TIInputModeController _inputModesFromInputModeConfiguration:]
+ -[TIInputModeController archivedInputModeConfiguration]
+ -[TIInputModeController inputModesFromArchivedInputModeConfiguration:]
+ -[TIInputModeController transformedInputModesFromInputModes:sourcePlatform:targetPlatform:preferredLanguages:preferredLocale:]
+ -[TIKeyboardCandidate isOneTimeCodeThatRequiresAuthentication]
+ -[TIKeyboardCandidate isSecureCandidateDoubleLines]
+ -[TIKeyboardCandidate setIsOneTimeCodeThatRequiresAuthentication:]
+ -[TIKeyboardCandidate setIsSecureCandidateDoubleLines:]
+ -[TIKeyboardSecureCandidateRenderTraits isInlinePromptUI]
+ -[TIKeyboardSecureCandidateRenderTraits setIsInlinePromptUI:]
+ -[TIKeyboardState attributedDocumentState]
+ -[TIKeyboardState setAttributedDocumentState:]
+ -[TIPreferencesController personaUniqueIdentifierSelf]
+ -[TIPreferencesController registerRemoteDeviceWithIDSIdentifier:user:]
+ -[TIPreferencesController remoteDeviceIDSIdentifer]
+ -[TIPreferencesController updateLastUsedDictionaryLanguageInMultilingualKeyboard:activeDictationlanguage:]
+ AssistantServicesLibraryCore.frameworkLibrary
+ CarbonLibraryCore.frameworkLibrary
+ OBJC_IVAR_$_TIAttributedDocumentState._contextAfterInput
+ OBJC_IVAR_$_TIAttributedDocumentState._contextBeforeInput
+ OBJC_IVAR_$_TIAttributedDocumentState._markedText
+ OBJC_IVAR_$_TIAttributedDocumentState._selectedRangeInMarkedText
+ OBJC_IVAR_$_TIAttributedDocumentState._selectedText
+ OBJC_IVAR_$_TIAttributedDocumentState._truncatedRangeInSelectedText
+ OBJC_IVAR_$_TIKeyboardCandidate._isOneTimeCodeThatRequiresAuthentication
+ OBJC_IVAR_$_TIKeyboardCandidate._isSecureCandidateDoubleLines
+ OBJC_IVAR_$_TIKeyboardSecureCandidateRenderTraits._isInlinePromptUI
+ OBJC_IVAR_$_TIKeyboardState._attributedDocumentState
+ TIGetIndicScriptComposerRules.__rules
+ TIGetIndicScriptComposerRules.onceToken
+ TIGetMacInputSourcesMap.__macInputSourcesMap
+ TIGetMacInputSourcesMap.onceToken
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFStringCreateArrayWithFindResults
+ _CarbonLibrary
+ _GetInputModeWithHardwareLayoutIfSupported
+ _NSInvalidArgumentException
+ _NSRangeException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_TIAttributedDocumentState
+ _OBJC_METACLASS_$_TIAttributedDocumentState
+ _TIActiveMultilingualKeyboardDictationMappingsPreference
+ _TIArchivedInputModeConfigurationInputModesKey
+ _TIArchivedInputModeConfigurationPlatformKey
+ _TIArchivedInputModeConfigurationPlatform_iOS
+ _TIArchivedInputModeConfigurationPlatform_macOS
+ _TIArchivedInputModeConfigurationPreferredLanguagesKey
+ _TIArchivedInputModeConfigurationPreferredLocaleKey
+ _TIArchivedInputModeConfigurationVersionKey
+ _TIGetIndicScriptComposerRules
+ _TIGetMacInputSourcesMap
+ _TIInputModePropertiesTypeToSiriEnabled
+ _TIInputModePropertiesTypeToSiriEnabledUnderDevelopment
+ _TIIsTypeToSiriModeEnabled
+ _TIKeyboardDidShowGenmojiTipPreference
+ _TIPersonaUniqueIdentifierSelfPreference
+ _TIRemoteDeviceIDSIdentifierPreference
+ __78+[TIDocumentState _selectedTextByDeletingInteriorSentences:outTruncatedRange:]_block_invoke.2
+ __Block_byref_object_copy_.11566
+ __Block_byref_object_copy_.13047
+ __Block_byref_object_copy_.2005
+ __Block_byref_object_copy_.268
+ __Block_byref_object_copy_.2963
+ __Block_byref_object_copy_.7114
+ __Block_byref_object_copy_.925
+ __Block_byref_object_dispose_.11567
+ __Block_byref_object_dispose_.13048
+ __Block_byref_object_dispose_.2006
+ __Block_byref_object_dispose_.269
+ __Block_byref_object_dispose_.2964
+ __Block_byref_object_dispose_.7115
+ __Block_byref_object_dispose_.926
+ __NSMethodExceptionProem
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSAttributedString_$_TIExtras
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableAttributedString_$_TIExtras
+ __OBJC_$_CATEGORY_NSMutableAttributedString_$_TIExtras
+ __OBJC_$_CLASS_METHODS_TIAttributedDocumentState(StateTransitions|SecureCoding|TestSupport)
+ __OBJC_$_CLASS_PROP_LIST_TIAttributedDocumentState
+ __OBJC_$_INSTANCE_METHODS_TIAttributedDocumentState(StateTransitions|SecureCoding|TestSupport)
+ __OBJC_$_INSTANCE_VARIABLES_TIAttributedDocumentState
+ __OBJC_$_PROP_LIST_TIAttributedDocumentState
+ __OBJC_CLASS_PROTOCOLS_$_TIAttributedDocumentState
+ __OBJC_CLASS_RO_$_TIAttributedDocumentState
+ __OBJC_METACLASS_RO_$_TIAttributedDocumentState
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPNS_6vectorI18TIHandwritingPointNS_9allocatorIS5_EEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeI8NSHolderI19TIInputContextEntryEPvEENS_22__tree_node_destructorINS_9allocatorIS6_EEEEE5resetB8nn190102EPS6_
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI18TIHandwritingPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorI18TIHandwritingPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__13setI8NSHolderI19TIInputContextEntryENS_4lessIS3_EENS_9allocatorIS3_EEE6insertB8nn190102INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEEEvT_SG_
+ __ZNSt3__16vectorI18TIHandwritingPointNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorINS0_I18TIHandwritingPointNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB8nn190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ ___35-[TIKeyboardState encodeWithCoder:]_block_invoke
+ ___35-[TIKeyboardState encodeWithCoder:]_block_invoke_2
+ ___40-[TIAttributedDocumentState description]_block_invoke
+ ___54-[NSString(TIExtras) _indexByTrimmingWordsAfterIndex:]_block_invoke
+ ___55-[NSString(TIExtras) _indexByTrimmingWordsBeforeIndex:]_block_invoke
+ ___65-[NSAttributedString(TIExtras) _ti_attributedStringWithIterator:]_block_invoke
+ ___65-[NSAttributedString(TIExtras) _ti_attributedStringWithIterator:]_block_invoke_2
+ ___72-[NSAttributedString(TIExtras) _ti_attributedStringByKeepingAttributes:]_block_invoke
+ ___72-[NSAttributedString(TIExtras) _ti_attributedStringByKeepingAttributes:]_block_invoke_2
+ ___AssistantServicesLibraryCore_block_invoke
+ ___CarbonLibraryCore_block_invoke
+ ___TIGetIndicScriptComposerRules_block_invoke
+ ___TIGetMacInputSourcesMap_block_invoke
+ ___block_descriptor_32_e36_"NSDictionary"16?0"NSDictionary"8l
+ ___block_descriptor_40_8_32r_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_48_8_32s40bs_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32l
+ ___block_descriptor_64_8_32s40bs_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_64_8_32s40s_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_64_8_32s40s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32l
+ ___getAFPreferencesClass_block_invoke
+ ___getTISCopyCurrentKeyboardInputSourceSymbolLoc_block_invoke
+ ___getTISGetInputSourcePropertySymbolLoc_block_invoke
+ ___getkTISPropertyInputSourceIDSymbolLoc_block_invoke
+ __block_literal_global.10016
+ __block_literal_global.1034
+ __block_literal_global.1110
+ __block_literal_global.12236
+ __block_literal_global.12522
+ __block_literal_global.12581
+ __block_literal_global.12829
+ __block_literal_global.13337
+ __block_literal_global.13789
+ __block_literal_global.2023
+ __block_literal_global.2423
+ __block_literal_global.2615
+ __block_literal_global.267
+ __block_literal_global.291
+ __block_literal_global.311
+ __block_literal_global.32.12514
+ __block_literal_global.322
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.328
+ __block_literal_global.330
+ __block_literal_global.336
+ __block_literal_global.338
+ __block_literal_global.350
+ __block_literal_global.352
+ __block_literal_global.357
+ __block_literal_global.362
+ __block_literal_global.367
+ __block_literal_global.372
+ __block_literal_global.377
+ __block_literal_global.38.12508
+ __block_literal_global.399
+ __block_literal_global.4.8722
+ __block_literal_global.4122
+ __block_literal_global.4128
+ __block_literal_global.4404
+ __block_literal_global.471
+ __block_literal_global.4941
+ __block_literal_global.5030
+ __block_literal_global.531
+ __block_literal_global.535
+ __block_literal_global.549
+ __block_literal_global.5523
+ __block_literal_global.580
+ __block_literal_global.6001
+ __block_literal_global.678
+ __block_literal_global.6855
+ __block_literal_global.7.8725
+ __block_literal_global.7.9117
+ __block_literal_global.7180
+ __block_literal_global.75.1071
+ __block_literal_global.7705
+ __block_literal_global.7849
+ __block_literal_global.788
+ __block_literal_global.8143
+ __block_literal_global.817
+ __block_literal_global.85.2409
+ __block_literal_global.8699
+ __block_literal_global.8718
+ __block_literal_global.876
+ __block_literal_global.9085
+ __block_literal_global.9113
+ __block_literal_global.9673
+ __block_literal_global.9834
+ __tiAttributedStringForString
+ _audit_stringAssistantServices
+ _audit_stringCarbon
+ _objc_msgSend$_archivedInputModeConfigurationFrom:
+ _objc_msgSend$_attributedString:byTrimmingWordsAfterIndex:
+ _objc_msgSend$_attributedString:byTrimmingWordsBeforeIndex:
+ _objc_msgSend$_indexByTrimmingWordsAfterIndex:
+ _objc_msgSend$_indexByTrimmingWordsBeforeIndex:
+ _objc_msgSend$_inputModeConfiguration
+ _objc_msgSend$_inputModesFromInputModeConfiguration:
+ _objc_msgSend$_ti_attributedString:matchesAttributedStringIgnoringNullity:
+ _objc_msgSend$_ti_attributedStringByAppendingAttributedString:
+ _objc_msgSend$_ti_attributedStringByKeepingAttributes:
+ _objc_msgSend$_ti_attributedStringByRemovingAttributes:
+ _objc_msgSend$_ti_attributedStringWithIterator:
+ _objc_msgSend$_ti_attributedSubstringFromIndex:
+ _objc_msgSend$_ti_attributedSubstringToIndex:
+ _objc_msgSend$_ti_replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$_ti_stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$_ti_stringByReplacingOccurrencesOfString:withString:options:range:
+ _objc_msgSend$addAttributes:range:
+ _objc_msgSend$appendAttributedString:
+ _objc_msgSend$attributedDocumentState
+ _objc_msgSend$attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:
+ _objc_msgSend$attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:
+ _objc_msgSend$attributedDocumentStateForTestingWithText:selectedRange:
+ _objc_msgSend$attributedDocumentStateWithContextBefore:markedText:selectedRange:contextAfter:
+ _objc_msgSend$attributedDocumentStateWithContextBefore:selectedText:contextAfter:
+ _objc_msgSend$attributedSubstringFromRange:
+ _objc_msgSend$attributesAtIndex:effectiveRange:
+ _objc_msgSend$documentStateWithAttributeIterator:
+ _objc_msgSend$enumerateAttributesInRange:options:usingBlock:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$isEqualIgnoringMarkedText:
+ _objc_msgSend$isEqualToAttributedString:
+ _objc_msgSend$isInlinePromptUI
+ _objc_msgSend$isSecureCandidateDoubleLines
+ _objc_msgSend$mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:
+ _objc_msgSend$preferredLocale
+ _objc_msgSend$raise:format:
+ _objc_msgSend$removeAttribute:range:
+ _objc_msgSend$replaceCharactersInRange:withAttributedString:
+ _objc_msgSend$setIsSecureCandidateDoubleLines:
+ _objc_msgSend$sharedPreferences
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$transformedInputModesFromInputModes:sourcePlatform:targetPlatform:preferredLanguages:preferredLocale:
+ _objc_msgSend$unboundedAttributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:
+ generateIdentifier.count.9926
+ getAFPreferencesClass.softClass
+ getTISCopyCurrentKeyboardInputSourceSymbolLoc.ptr
+ getTISGetInputSourcePropertySymbolLoc.ptr
+ getkTISPropertyInputSourceIDSymbolLoc.ptr
+ sharedInstance.instance.13338
+ sharedInstance.instance.8700
+ sharedInstance.onceToken.13336
+ sharedInstance.onceToken.7848
+ sharedInstance.onceToken.8698
+ sharedPreferencesController.once.734
+ sharedPreferencesController.once.771
+ sharedPreferencesController.sharedController.735
+ sharedPreferencesController.sharedController.772
- _TIISTypetoSiriMode
- __78+[TIDocumentState _selectedTextByDeletingInteriorSentences:outTruncatedRange:]_block_invoke.4
- __Block_byref_object_copy_.11296
- __Block_byref_object_copy_.12738
- __Block_byref_object_copy_.1984
- __Block_byref_object_copy_.263
- __Block_byref_object_copy_.2958
- __Block_byref_object_copy_.6863
- __Block_byref_object_copy_.914
- __Block_byref_object_dispose_.11297
- __Block_byref_object_dispose_.12739
- __Block_byref_object_dispose_.1985
- __Block_byref_object_dispose_.264
- __Block_byref_object_dispose_.2959
- __Block_byref_object_dispose_.6864
- __Block_byref_object_dispose_.915
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8nn180100IPNS_6vectorI18TIHandwritingPointNS_9allocatorIS5_EEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorI18TIHandwritingPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn180100INS_9allocatorINS_6vectorI18TIHandwritingPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__13setI8NSHolderI19TIInputContextEntryENS_4lessIS3_EENS_9allocatorIS3_EEE6insertB8nn180100INS_21__tree_const_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEEEvT_SG_
- __ZNSt3__16vectorI18TIHandwritingPointNS_9allocatorIS1_EEE11__vallocateB8nn180100Em
- __ZNSt3__16vectorINS0_I18TIHandwritingPointNS_9allocatorIS1_EEEENS2_IS4_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS4_RS5_EE
- __ZNSt3__16vectorINS0_I18TIHandwritingPointNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB8nn180100Ev
- __ZSt28__throw_bad_array_new_lengthB8nn180100v
- ___53+[TIDocumentState _string:byTrimmingWordsAfterIndex:]_block_invoke
- ___54+[TIDocumentState _string:byTrimmingWordsBeforeIndex:]_block_invoke
- __block_literal_global.1023
- __block_literal_global.1099
- __block_literal_global.11930
- __block_literal_global.12216
- __block_literal_global.12275
- __block_literal_global.12524
- __block_literal_global.13026
- __block_literal_global.13478
- __block_literal_global.2001
- __block_literal_global.2417
- __block_literal_global.2610
- __block_literal_global.264
- __block_literal_global.286
- __block_literal_global.307
- __block_literal_global.309
- __block_literal_global.319
- __block_literal_global.32.12208
- __block_literal_global.321
- __block_literal_global.323
- __block_literal_global.325
- __block_literal_global.327
- __block_literal_global.333
- __block_literal_global.335
- __block_literal_global.347
- __block_literal_global.349
- __block_literal_global.354
- __block_literal_global.359
- __block_literal_global.364
- __block_literal_global.38.12202
- __block_literal_global.4.8451
- __block_literal_global.4143
- __block_literal_global.4149
- __block_literal_global.4245
- __block_literal_global.458
- __block_literal_global.4777
- __block_literal_global.4866
- __block_literal_global.511
- __block_literal_global.515
- __block_literal_global.529
- __block_literal_global.5358
- __block_literal_global.560
- __block_literal_global.5835
- __block_literal_global.64
- __block_literal_global.6616
- __block_literal_global.668
- __block_literal_global.6931
- __block_literal_global.7.8454
- __block_literal_global.7.8845
- __block_literal_global.75.1060
- __block_literal_global.7591
- __block_literal_global.777
- __block_literal_global.7881
- __block_literal_global.798
- __block_literal_global.8428
- __block_literal_global.8447
- __block_literal_global.865
- __block_literal_global.8813
- __block_literal_global.8841
- __block_literal_global.9415
- __block_literal_global.9571
- __block_literal_global.9753
- _strncmp
- generateIdentifier.count.9663
- sharedInstance.instance.13027
- sharedInstance.instance.8429
- sharedInstance.onceToken.13025
- sharedInstance.onceToken.7590
- sharedInstance.onceToken.8427
- sharedPreferencesController.once.715
- sharedPreferencesController.once.752
- sharedPreferencesController.sharedController.716
- sharedPreferencesController.sharedController.753
CStrings:
+ "\x15\t<\t"
+ "\x15\tM\t0\t"
+ "\x15\tM\t7\t"
+ "\x15\n<\n"
+ "\x15\n<\nM\n0\n"
+ "\x15\nM\n0\n"
+ "\x15\rM\r\x15\r"
+ "\x15\rM\r/\r"
+ "\x15\rM\r0\r"
+ "\x15\rM\r2\r"
+ "\x15\rM\r5\r"
+ "\x15\rM\r7\r"
+ "\x16\t<\t"
+ "\x16\tM\t0\t"
+ "\x16\n<\n"
+ "\x16\n<\nM\n0\n"
+ "\x16\nM\n0\n"
+ "\x16\rM\r/\r"
+ "\x16\rM\r0\r"
+ "\x16\rM\r5\r"
+ "\x17\t<\t"
+ "\x17\tM\t0\t"
+ "\x17\n<\n"
+ "\x17\n<\nM\n0\n"
+ "\x17\nM\n0\n"
+ "\x17\nM\n9\n"
+ "\x17\rM\r\x17\r"
+ "\x17\rM\r(\r"
+ "\x17\rM\r/\r"
+ "\x17\rM\r0\r"
+ "\x17\rM\r2\r"
+ "\x17\rM\r5\r"
+ "\x18\tM\t0\t"
+ "\x18\nM\n0\n"
+ "\x18\rM\r/\r"
+ "\x18\rM\r0\r"
+ "\x18\rM\r5\r"
+ "\x19\tM\t0\t"
+ "\x19\rM\r\x15\r"
+ "\x19\rM\r\x19\r"
+ "\x19\rM\r/\r"
+ "\x19\rM\r0\r"
+ "\x19\rM\r5\r"
+ "\x1a\tM\t0\t"
+ "\x1a\nM\n0\n"
+ "\x1a\rM\r\x1a\r"
+ "\x1a\rM\r\x1b\r"
+ "\x1a\rM\r/\r"
+ "\x1a\rM\r0\r"
+ "\x1a\rM\r5\r"
+ "\x1b\tM\t0\t"
+ "\x1b\tM\t5\t"
+ "\x1b\rM\r/\r"
+ "\x1b\rM\r0\r"
+ "\x1b\rM\r5\r"
+ "\x1c\t<\t"
+ "\x1c\tM\t\x1e\t"
+ "\x1c\tM\t0\t"
+ "\x1c\n<\n"
+ "\x1c\n<\nM\n0\n"
+ "\x1c\nM\n0\n"
+ "\x1c\nM\n9\n"
+ "\x1c\rM\r/\r"
+ "\x1c\rM\r0\r"
+ "\x1c\rM\r5\r"
+ "\x1d\tM\t0\t"
+ "\x1d\rM\r/\r"
+ "\x1d\rM\r0\r"
+ "\x1d\rM\r5\r"
+ "\x1e\rM\r\x1a\r"
+ "\x1e\rM\r\x1c\r"
+ "\x1e\rM\r\x1e\r"
+ "\x1e\rM\r/\r"
+ "\x1e\rM\r0\r"
+ "\x1e\rM\r5\r"
+ "\x1f\tM\t\x1f\t"
+ "\x1f\tM\t \t"
+ "\x1f\tM\t0\t"
+ "\x1f\tM\t5\t"
+ "\x1f\nM\n0\n"
+ "\x1f\nM\n9\n"
+ "\x1f\rM\r\x1f\r"
+ "\x1f\rM\r/\r"
+ "\x1f\rM\r0\r"
+ "\x1f\rM\r5\r"
+ " \tM\t \t"
+ " \tM\t0\t"
+ " \tM\t5\t"
+ " \rM\r/\r"
+ " \rM\r0\r"
+ " \rM\r5\r"
+ "!\t<\t"
+ "!\tM\t!\t"
+ "!\tM\t\"\t"
+ "!\tM\t0\t"
+ "!\tM\t5\t"
+ "!\nM\n0\n"
+ "!\rM\r!\r"
+ "!\rM\r\"\r"
+ "!\rM\r/\r"
+ "!\rM\r0\r"
+ "!\rM\r5\r"
+ "\"\t<\t"
+ "\"\tM\t\"\t"
+ "\"\tM\t0\t"
+ "\"\tM\t5\t"
+ "\"\rM\r/\r"
+ "\"\rM\r0\r"
+ "\"\rM\r5\r"
+ "#\tM\t0\t"
+ "#\nM\n9\n"
+ "#\rM\r\x1f\r"
+ "#\rM\r!\r"
+ "#\rM\r#\r"
+ "#\rM\r/\r"
+ "#\rM\r0\r"
+ "#\rM\r5\r"
+ "$\tM\t$\t"
+ "$\tM\t0\t"
+ "$\nM\n0\n"
+ "$\nM\n9\n"
+ "$\rM\r$\r"
+ "$\rM\r%\r"
+ "$\rM\r(\r"
+ "$\rM\r/\r"
+ "$\rM\r0\r"
+ "$\rM\r2\r"
+ "$\rM\r5\r"
+ "$\rM\r8\r"
+ "%\tM\t0\t"
+ "%\nM\n0\n"
+ "%\rM\r/\r"
+ "%\rM\r0\r"
+ "%\rM\r5\r"
+ "%@: Index %lu out of bounds; string length %lu"
+ "%@: Range {%lu, %lu} out of bounds; string length %lu"
+ "%@: nil argument"
+ "%s  TIKeyboardState with TIAttributedDocumentState: non-serializable attribute encountered: %@"
+ "%s: %@"
+ "&\tM\t&\t"
+ "&\tM\t'\t"
+ "&\tM\t(\t"
+ "&\tM\t,\t"
+ "&\tM\t-\t"
+ "&\tM\t.\t"
+ "&\tM\t/\t"
+ "&\tM\t0\t"
+ "&\tM\t5\t"
+ "&\nM\n0\n"
+ "&\nM\n5\n"
+ "&\nM\n9\n"
+ "&\rM\r&\r"
+ "&\rM\r'\r"
+ "&\rM\r/\r"
+ "&\rM\r0\r"
+ "&\rM\r5\r"
+ "'\tM\t0\t"
+ "'\nM\n0\n"
+ "'\nM\n5\n"
+ "'\rM\r/\r"
+ "'\rM\r0\r"
+ "'\rM\r5\r"
+ "(\tM\t0\t"
+ "(\nM\n0\n"
+ "(\nM\n9\n"
+ "(\rM\r$\r"
+ "(\rM\r%\r"
+ "(\rM\r&\r"
+ "(\rM\r'\r"
+ "(\rM\r(\r"
+ "(\rM\r.\r"
+ "(\rM\r/\r"
+ "(\rM\r0\r"
+ "(\rM\r1\r"
+ "(\rM\r5\r"
+ "*\tM\t0\t"
+ "*\nM\n0\n"
+ "*\nM\n9\n"
+ "*\rM\r*\r"
+ "*\rM\r/\r"
+ "*\rM\r0\r"
+ "*\rM\r2\r"
+ "*\rM\r5\r"
+ "+\t<\t"
+ "+\tM\t0\t"
+ "+\n<\n"
+ "+\n<\nM\n0\n"
+ "+\nM\n0\n"
+ "+\rM\r/\r"
+ "+\rM\r0\r"
+ "+\rM\r2\r"
+ "+\rM\r5\r"
+ ",\tM\t0\t"
+ ",\nM\n0\n"
+ ",\nM\n9\n"
+ ",\rM\r,\r"
+ ",\rM\r/\r"
+ ",\rM\r0\r"
+ ",\rM\r2\r"
+ ",\rM\r5\r"
+ "-\tM\t0\t"
+ "-\nM\n0\n"
+ "-\rM\r/\r"
+ "-\rM\r0\r"
+ "-\rM\r5\r"
+ "-[TIInputModeController _archivedInputModeConfigurationFrom:]"
+ "-[TIInputModeController inputModesFromArchivedInputModeConfiguration:]"
+ "-[TIKeyboardState encodeWithCoder:]_block_invoke_2"
+ ".\tM\t0\t"
+ ".\nM\n0\n"
+ ".\nM\n9\n"
+ ".\rM\r*\r"
+ ".\rM\r/\r"
+ ".\rM\r0\r"
+ ".\rM\r2\r"
+ ".\rM\r5\r"
+ "/\tM\t0\t"
+ "/\rM\r/\r"
+ "/\rM\r0\r"
+ "/\rM\r5\r"
+ "/System/Library/Frameworks/Carbon.framework/Contents/MacOS/Carbon"
+ "/System/Library/PrivateFrameworks/AssistantServices.framework/Contents/MacOS/AssistantServices"
+ "0\tM\t\x15\t"
+ "0\tM\t\x16\t"
+ "0\tM\t\x17\t"
+ "0\tM\t\x18\t"
+ "0\tM\t\x19\t"
+ "0\tM\t\x1a\t"
+ "0\tM\t\x1b\t"
+ "0\tM\t\x1c\t"
+ "0\tM\t\x1d\t"
+ "0\tM\t\x1e\t"
+ "0\tM\t\x1f\t"
+ "0\tM\t \t"
+ "0\tM\t!\t"
+ "0\tM\t\"\t"
+ "0\tM\t#\t"
+ "0\tM\t$\t"
+ "0\tM\t%\t"
+ "0\tM\t&\t"
+ "0\tM\t'\t"
+ "0\tM\t(\t"
+ "0\tM\t)\t"
+ "0\tM\t*\t"
+ "0\tM\t+\t"
+ "0\tM\t,\t"
+ "0\tM\t-\t"
+ "0\tM\t.\t"
+ "0\tM\t/\t"
+ "0\tM\t0\t"
+ "0\tM\t1\t"
+ "0\tM\t2\t"
+ "0\tM\t3\t"
+ "0\tM\t4\t"
+ "0\tM\t5\t"
+ "0\tM\t6\t"
+ "0\tM\t7\t"
+ "0\tM\t8\t"
+ "0\tM\t9\t"
+ "0\tM\tX\t"
+ "0\tM\tY\t"
+ "0\tM\tZ\t"
+ "0\tM\t[\t"
+ "0\tM\t\\\t"
+ "0\tM\t]\t"
+ "0\tM\t^\t"
+ "0\tM\t_\t"
+ "0\tM\tx\t"
+ "0\tM\ty\t"
+ "0\tM\tz\t"
+ "0\tM\t{\t"
+ "0\tM\t|\t"
+ "0\tM\t}\t"
+ "0\tM\t~\t"
+ "0\tM\t\x7f\t"
+ "0\nM\n0\n"
+ "0\nM\n9\n"
+ "0\rM\r/\r"
+ "0\rM\r0\r"
+ "0\rM\r5\r"
+ "1\tM\t\x15\t"
+ "1\tM\t\x16\t"
+ "1\tM\t\x17\t"
+ "1\tM\t\x18\t"
+ "1\tM\t\x19\t"
+ "1\tM\t\x1a\t"
+ "1\tM\t\x1b\t"
+ "1\tM\t\x1c\t"
+ "1\tM\t\x1d\t"
+ "1\tM\t\x1e\t"
+ "1\tM\t\x1f\t"
+ "1\tM\t \t"
+ "1\tM\t!\t"
+ "1\tM\t\"\t"
+ "1\tM\t#\t"
+ "1\tM\t$\t"
+ "1\tM\t%\t"
+ "1\tM\t&\t"
+ "1\tM\t'\t"
+ "1\tM\t(\t"
+ "1\tM\t)\t"
+ "1\tM\t*\t"
+ "1\tM\t+\t"
+ "1\tM\t,\t"
+ "1\tM\t-\t"
+ "1\tM\t.\t"
+ "1\tM\t/\t"
+ "1\tM\t0\t"
+ "1\tM\t1\t"
+ "1\tM\t2\t"
+ "1\tM\t3\t"
+ "1\tM\t4\t"
+ "1\tM\t5\t"
+ "1\tM\t6\t"
+ "1\tM\t7\t"
+ "1\tM\t8\t"
+ "1\tM\t9\t"
+ "1\tM\tX\t"
+ "1\tM\tY\t"
+ "1\tM\tZ\t"
+ "1\tM\t[\t"
+ "1\tM\t\\\t"
+ "1\tM\t]\t"
+ "1\tM\t^\t"
+ "1\tM\t_\t"
+ "1\tM\tx\t"
+ "1\tM\ty\t"
+ "1\tM\tz\t"
+ "1\tM\t{\t"
+ "1\tM\t|\t"
+ "1\tM\t}\t"
+ "1\tM\t~\t"
+ "1\tM\t\x7f\t"
+ "1\rM\r/\r"
+ "1\rM\r0\r"
+ "1\rM\r1\r"
+ "1\rM\r5\r"
+ "2\tM\t0\t"
+ "2\n<\n"
+ "2\nM\n9\n"
+ "2\rM\r*\r"
+ "2\rM\r/\r"
+ "2\rM\r0\r"
+ "2\rM\r2\r"
+ "2\rM\r5\r"
+ "3\tM\t0\t"
+ "3\rM\r/\r"
+ "3\rM\r0\r"
+ "3\rM\r5\r"
+ "4\tM\t0\t"
+ "4\rM\r/\r"
+ "4\rM\r0\r"
+ "4\rM\r5\r"
+ "5\tM\t0\t"
+ "5\nM\n0\n"
+ "5\nM\n9\n"
+ "5\rM\r/\r"
+ "5\rM\r0\r"
+ "5\rM\r2\r"
+ "5\rM\r5\r"
+ "6\tM\t0\t"
+ "6\rM\r\x1a\r"
+ "6\rM\r/\r"
+ "6\rM\r0\r"
+ "6\rM\r2\r"
+ "6\rM\r5\r"
+ "6\rM\r6\r"
+ "7\tM\t0\t"
+ "7\rM\r/\r"
+ "7\rM\r0\r"
+ "7\rM\r5\r"
+ "8\tM\t0\t"
+ "8\n<\n"
+ "8\n<\nM\n0\n"
+ "8\nM\n0\n"
+ "8\nM\n5\n"
+ "8\rM\r%\r"
+ "8\rM\r/\r"
+ "8\rM\r0\r"
+ "8\rM\r2\r"
+ "8\rM\r5\r"
+ "8\rM\r8\r"
+ "9\tM\t#\t"
+ "9\tM\t(\t"
+ "9\tM\t.\t"
+ "9\tM\t/\t"
+ "9\tM\t0\t"
+ "9\tM\t2\t"
+ "9\tM\t5\t"
+ "9\nM\n0\n"
+ "9\rM\r(\r"
+ "9\rM\r.\r"
+ "9\rM\r/\r"
+ "9\rM\r0\r"
+ "9\rM\r2\r"
+ "9\rM\r5\r"
+ "; attributedDocumentState = %@"
+ "; isInlinePromptUI = %@"
+ "@\"NSAttributedString\""
+ "@\"NSDictionary\"16@?0@\"NSDictionary\"8"
+ "@\"TIAttributedDocumentState\""
+ "@40@0:8{_NSRange=QQ}16@32"
+ "@56@0:8@16@24Q32{_NSRange=QQ}40"
+ "@hw=%@"
+ "AFPreferences"
+ "ActiveMultilingualKeyboardDictationMappings"
+ "Beng"
+ "Deva"
+ "Gujr"
+ "Guru"
+ "KeyboardDidShowGenmojiTip"
+ "MacInputSourcesMap.plist"
+ "Mlym"
+ "OTP"
+ "PersonaUniqueIdentifierSelf"
+ "Q56@0:8@16@24Q32{_NSRange=QQ}40"
+ "RemoteDeviceIDSIdentifier"
+ "SecureCoding"
+ "T@\"NSAttributedString\",R,N"
+ "T@\"NSAttributedString\",R,N,V_contextAfterInput"
+ "T@\"NSAttributedString\",R,N,V_contextBeforeInput"
+ "T@\"NSAttributedString\",R,N,V_markedText"
+ "T@\"NSAttributedString\",R,N,V_selectedText"
+ "T@\"TIAttributedDocumentState\",&,N,V_attributedDocumentState"
+ "TB,N,V_isInlinePromptUI"
+ "TB,N,V_isOneTimeCodeThatRequiresAuthentication"
+ "TB,N,V_isSecureCandidateDoubleLines"
+ "TIAttributedDocumentState"
+ "TIIndicScriptComposerRules.plist"
+ "TISCopyCurrentKeyboardInputSource"
+ "TISGetInputSourceProperty"
+ "UIKeyboardTypeToSiriEnabled"
+ "UIKeyboardTypeToSiriUnderDevelopment"
+ "Unable to find class %s"
+ "X\tM\t0\t"
+ "Y\tM\t0\t"
+ "Z\tM\t0\t"
+ "[\tM\t0\t"
+ "\\\tM\t0\t"
+ "\\\nM\n9\n"
+ "]\tM\t0\t"
+ "^\tM\t0\t"
+ "_\tM\t0\t"
+ "_archivedInputModeConfigurationFrom:"
+ "_attributedDocumentState"
+ "_attributedString:byTrimmingWordsAfterIndex:"
+ "_attributedString:byTrimmingWordsBeforeIndex:"
+ "_attributedString:matchesAttributedString:"
+ "_indexByTrimmingWordsAfterIndex:"
+ "_indexByTrimmingWordsBeforeIndex:"
+ "_inputModeConfiguration"
+ "_inputModesFromInputModeConfiguration:"
+ "_isInlinePromptUI"
+ "_isOneTimeCodeThatRequiresAuthentication"
+ "_isSecureCandidateDoubleLines"
+ "_ti_attributedString:matchesAttributedStringIgnoringNullity:"
+ "_ti_attributedStringByAppendingAttributedString:"
+ "_ti_attributedStringByAppendingString:"
+ "_ti_attributedStringByKeepingAttributes:"
+ "_ti_attributedStringByRemovingAttributes:"
+ "_ti_attributedStringWithIterator:"
+ "_ti_attributedSubstringFromIndex:"
+ "_ti_attributedSubstringToIndex:"
+ "_ti_decodeWithCoder:forKey:attributeIterator:"
+ "_ti_encodeWithCoder:forKey:attributeIterator:"
+ "_ti_encodeWithCoder:forKey:keepingAttributes:"
+ "_ti_encodeWithCoder:forKey:removingAttributes:"
+ "_ti_replaceOccurrencesOfString:withString:options:range:"
+ "_ti_stringByReplacingCharactersInRange:withString:"
+ "_ti_stringByReplacingOccurrencesOfString:withString:options:range:"
+ "addAttributes:range:"
+ "appendAttributedString:"
+ "archivedInputModeConfiguration"
+ "attributedDocumentState"
+ "attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:"
+ "attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:markedText:selectedRangeInMarkedText:"
+ "attributedDocumentStateForTestingWithPlainText:selectedRange:"
+ "attributedDocumentStateForTestingWithText:selectedRange:"
+ "attributedDocumentStateWithContextBefore:markedText:selectedRange:contextAfter:"
+ "attributedDocumentStateWithContextBefore:selectedText:contextAfter:"
+ "attributedDocumentStateWithDocumentState:"
+ "attributedString"
+ "attributedSubstringFromRange:"
+ "attributesAtIndex:effectiveRange:"
+ "bn@sw=Bengali-Alphabetic"
+ "com.apple.inputmethod.AinuIM.Ainu"
+ "com.apple.inputmethod.Korean.2SetKorean"
+ "com.apple.inputmethod.Korean.390Sebulshik"
+ "com.apple.inputmethod.Korean.3SetKorean"
+ "com.apple.inputmethod.Korean.GongjinCheongRomaja"
+ "com.apple.inputmethod.Korean.HNCRomaja"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.FullWidthRoman"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.HalfWidthKana"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Japanese.Katakana"
+ "com.apple.inputmethod.Kotoeri.KanaTyping.Roman"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.FullWidthRoman"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.HalfWidthKana"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Japanese.Katakana"
+ "com.apple.inputmethod.Kotoeri.RomajiTyping.Roman"
+ "com.apple.inputmethod.SCIM.ITABC"
+ "com.apple.inputmethod.SCIM.Shuangpin"
+ "com.apple.inputmethod.SCIM.WBH"
+ "com.apple.inputmethod.SCIM.WBX"
+ "com.apple.inputmethod.TCIM.Cangjie"
+ "com.apple.inputmethod.TCIM.Jianyi"
+ "com.apple.inputmethod.TCIM.Pinyin"
+ "com.apple.inputmethod.TCIM.Shuangpin"
+ "com.apple.inputmethod.TCIM.WBH"
+ "com.apple.inputmethod.TCIM.Zhuyin"
+ "com.apple.inputmethod.TCIM.ZhuyinEten"
+ "com.apple.inputmethod.TYIM.Cangjie"
+ "com.apple.inputmethod.TYIM.Phonetic"
+ "com.apple.inputmethod.TYIM.Stroke"
+ "com.apple.inputmethod.TYIM.Sucheng"
+ "com.apple.inputmethod.Tamil.AnjalIM"
+ "com.apple.inputmethod.Tamil.Tamil99"
+ "com.apple.inputmethod.TransliterationIM.bn"
+ "com.apple.inputmethod.TransliterationIM.gu"
+ "com.apple.inputmethod.TransliterationIM.hi"
+ "com.apple.inputmethod.TransliterationIM.kn"
+ "com.apple.inputmethod.TransliterationIM.ml"
+ "com.apple.inputmethod.TransliterationIM.mr"
+ "com.apple.inputmethod.TransliterationIM.pa"
+ "com.apple.inputmethod.TransliterationIM.ta"
+ "com.apple.inputmethod.TransliterationIM.te"
+ "com.apple.inputmethod.TransliterationIM.ur"
+ "com.apple.inputmethod.VietnameseIM.VietnameseSimpleTelex"
+ "com.apple.inputmethod.VietnameseIM.VietnameseTelex"
+ "com.apple.inputmethod.VietnameseIM.VietnameseVIQR"
+ "com.apple.inputmethod.VietnameseIM.VietnameseVNI"
+ "com.apple.keylayout."
+ "darkSecondaryLabelColor"
+ "documentStateWithAttributeIterator:"
+ "enumerateAttributesInRange:options:usingBlock:"
+ "gu@sw=Gujarati-Alphabetic"
+ "hi@sw=Hindi-Alphabetic"
+ "iOS"
+ "initWithString:attributes:"
+ "inputModes"
+ "inputModesFromArchivedInputModeConfiguration:"
+ "isEqualToAttributedString:"
+ "isInlinePromptUI"
+ "isOneTimeCodeThatRequiresAuthentication"
+ "isSecureCandidateDoubleLines"
+ "isTextEqualIgnoringMarkedText:"
+ "ja_JP-Kana@hw=KANA"
+ "kTISPropertyInputSourceID"
+ "keyboardCandidateInputStringUsedWithAutofillExtraThatSignifiesOTPExtra"
+ "kn@sw=Kannada-Alphabetic"
+ "lightSecondaryLabelColor"
+ "macOS"
+ "ml@sw=Malayalam-Alphabetic"
+ "mostPreferredLanguageOf:withPreferredLanguages:forUsage:options:"
+ "mr@sw=Marathi-Alphabetic"
+ "or@sw=Oriya-Alphabetic"
+ "pa@sw=Punjabi-Alphabetic"
+ "personaUniqueIdentifierSelf"
+ "platform"
+ "preferredLocale"
+ "raise:format:"
+ "registerRemoteDeviceWithIDSIdentifier:user:"
+ "remoteDeviceIDSIdentifer"
+ "removeAttribute:range:"
+ "replaceCharactersInRange:withAttributedString:"
+ "setAttributedDocumentState:"
+ "setIsInlinePromptUI:"
+ "setIsOneTimeCodeThatRequiresAuthentication:"
+ "setIsSecureCandidateDoubleLines:"
+ "sharedPreferences"
+ "softlink:r:path:/System/Library/Frameworks/Carbon.framework/Carbon"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
+ "sortedArrayUsingSelector:"
+ "ta@hw=Tamil99"
+ "ta@sw=Tamil-Alphabetic"
+ "te@sw=Telugu-Alphabetic"
+ "transformedInputModesFromInputModes:sourcePlatform:targetPlatform:preferredLanguages:preferredLocale:"
+ "type_to_siri_under_development"
+ "unboundedAttributedDocumentStateForTestingWithContextBefore:selectedText:contextAfter:"
+ "unboundedAttributedDocumentStateForTestingWithPlainContextBefore:selectedText:contextAfter:"
+ "updateLastUsedDictionaryLanguageInMultilingualKeyboard:activeDictationlanguage:"
+ "ur@sw=Urdu-Alphabetic"
+ "ur_PK"
+ "v32@0:8@\"NSArray\"16@24"
+ "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"
+ "x\tM\t0\t"
+ "z\tM\t0\t"
+ "}\tM\t0\t"
+ "~\tM\t0\t"
+ "\x7f\tM\t0\t"
+ "\x95\t\xcd\t\x95\t"
+ "\x95\t\xcd\t\x9f\t"
+ "\x95\t\xcd\t\xa4\t"
+ "\x95\t\xcd\t\xa8\t"
+ "\x95\t\xcd\t\xac\t"
+ "\x95\t\xcd\t\xae\t"
+ "\x95\t\xcd\t\xaf\t"
+ "\x95\t\xcd\t\xb0\t"
+ "\x95\t\xcd\t\xb2\t"
+ "\x95\t\xcd\t\xb7\t"
+ "\x95\t\xcd\t\xb8\t"
+ "\x95\t\xcd\t\xf0\t"
+ "\x95\n\xbc\n"
+ "\x95\n\xcd\n\xb0\n"
+ "\x95\n\xcd\n\xb7\n"
+ "\x96\t\xcd\t\xac\t"
+ "\x96\t\xcd\t\xaf\t"
+ "\x96\t\xcd\t\xb0\t"
+ "\x96\t\xcd\t\xf0\t"
+ "\x96\n\xbc\n"
+ "\x96\n\xcd\n\xb0\n"
+ "\x97\t\xcd\t\x97\t"
+ "\x97\t\xcd\t\xa6\t"
+ "\x97\t\xcd\t\xa7\t"
+ "\x97\t\xcd\t\xa8\t"
+ "\x97\t\xcd\t\xac\t"
+ "\x97\t\xcd\t\xae\t"
+ "\x97\t\xcd\t\xaf\t"
+ "\x97\t\xcd\t\xb0\t"
+ "\x97\t\xcd\t\xb2\t"
+ "\x97\t\xcd\t\xf0\t"
+ "\x97\n\xbc\n"
+ "\x97\n\xcd\n\xb0\n"
+ "\x98\t\xcd\t\xa8\t"
+ "\x98\t\xcd\t\xac\t"
+ "\x98\t\xcd\t\xaf\t"
+ "\x98\t\xcd\t\xb0\t"
+ "\x98\t\xcd\t\xf0\t"
+ "\x98\n\xcd\n\xb0\n"
+ "\x99\t\xcd\t\x95\t"
+ "\x99\t\xcd\t\x96\t"
+ "\x99\t\xcd\t\x97\t"
+ "\x99\t\xcd\t\x98\t"
+ "\x99\t\xcd\t\xac\t"
+ "\x99\t\xcd\t\xae\t"
+ "\x99\t\xcd\t\xaf\t"
+ "\x99\t\xcd\t\xb0\t"
+ "\x99\t\xcd\t\xf0\t"
+ "\x99\n\xcd\n\xb0\n"
+ "\x9a\t\xcd\t\x9a\t"
+ "\x9a\t\xcd\t\x9b\t"
+ "\x9a\t\xcd\t\x9e\t"
+ "\x9a\t\xcd\t\xa8\t"
+ "\x9a\t\xcd\t\xac\t"
+ "\x9a\t\xcd\t\xaf\t"
+ "\x9a\t\xcd\t\xb0\t"
+ "\x9a\t\xcd\t\xf0\t"
+ "\x9a\n\xcd\n\xb0\n"
+ "\x9b\t\xcd\t\xac\t"
+ "\x9b\t\xcd\t\xaf\t"
+ "\x9b\t\xcd\t\xb0\t"
+ "\x9b\t\xcd\t\xf0\t"
+ "\x9b\n\xcd\n\xb0\n"
+ "\x9b\n\xcd\n\xb5\n"
+ "\x9c\t\xcd\t\x9c\t"
+ "\x9c\t\xcd\t\x9d\t"
+ "\x9c\t\xcd\t\x9e\t"
+ "\x9c\t\xcd\t\xac\t"
+ "\x9c\t\xcd\t\xaf\t"
+ "\x9c\t\xcd\t\xb0\t"
+ "\x9c\t\xcd\t\xf0\t"
+ "\x9c\n\xbc\n"
+ "\x9c\n\xcd\n\x9e\n"
+ "\x9c\n\xcd\n\xb0\n"
+ "\x9d\t\xcd\t\xac\t"
+ "\x9d\t\xcd\t\xaf\t"
+ "\x9d\t\xcd\t\xb0\t"
+ "\x9d\t\xcd\t\xf0\t"
+ "\x9d\n\xcd\n\xb0\n"
+ "\x9e\t\xcd\t\x9a\t"
+ "\x9e\t\xcd\t\x9b\t"
+ "\x9e\t\xcd\t\x9c\t"
+ "\x9e\t\xcd\t\x9d\t"
+ "\x9e\t\xcd\t\xa7\t"
+ "\x9e\t\xcd\t\xac\t"
+ "\x9e\t\xcd\t\xaf\t"
+ "\x9e\t\xcd\t\xb0\t"
+ "\x9e\t\xcd\t\xf0\t"
+ "\x9e\n\xcd\n\xb0\n"
+ "\x9f\t\xcd\t\x9f\t"
+ "\x9f\t\xcd\t\xac\t"
+ "\x9f\t\xcd\t\xae\t"
+ "\x9f\t\xcd\t\xaf\t"
+ "\x9f\t\xcd\t\xb0\t"
+ "\x9f\t\xcd\t\xf0\t"
+ "\x9f\n\xcd\n\x9f\n"
+ "\x9f\n\xcd\n\xa0\n"
+ "\x9f\n\xcd\n\xb0\n"
+ "\x9f\n\xcd\n\xb5\n"
+ "\xa0\t\xcd\t\xac\t"
+ "\xa0\t\xcd\t\xaf\t"
+ "\xa0\t\xcd\t\xb0\t"
+ "\xa0\t\xcd\t\xf0\t"
+ "\xa0\n\xcd\n\xa0\n"
+ "\xa0\n\xcd\n\xb0\n"
+ "\xa1\t\xcd\t\x97\t"
+ "\xa1\t\xcd\t\xa1\t"
+ "\xa1\t\xcd\t\xac\t"
+ "\xa1\t\xcd\t\xae\t"
+ "\xa1\t\xcd\t\xaf\t"
+ "\xa1\t\xcd\t\xb0\t"
+ "\xa1\t\xcd\t\xf0\t"
+ "\xa1\n\xbc\n"
+ "\xa1\n\xcd\n\xa1\n"
+ "\xa1\n\xcd\n\xa2\n"
+ "\xa1\n\xcd\n\xb0\n"
+ "\xa1\n\xcd\n\xb5\n"
+ "\xa2\t\xcd\t\xac\t"
+ "\xa2\t\xcd\t\xaf\t"
+ "\xa2\t\xcd\t\xb0\t"
+ "\xa2\t\xcd\t\xf0\t"
+ "\xa2\n\xbc\n"
+ "\xa2\n\xcd\n\xa2\n"
+ "\xa2\n\xcd\n\xb0\n"
+ "\xa3\t\xcd\t\x9f\t"
+ "\xa3\t\xcd\t\xa0\t"
+ "\xa3\t\xcd\t\xa1\t"
+ "\xa3\t\xcd\t\xa2\t"
+ "\xa3\t\xcd\t\xa3\t"
+ "\xa3\t\xcd\t\xac\t"
+ "\xa3\t\xcd\t\xae\t"
+ "\xa3\t\xcd\t\xaf\t"
+ "\xa3\t\xcd\t\xb0\t"
+ "\xa3\t\xcd\t\xf0\t"
+ "\xa3\n\xcd\n\xb0\n"
+ "\xa4\t\xcd\t\xa4\t"
+ "\xa4\t\xcd\t\xa5\t"
+ "\xa4\t\xcd\t\xa8\t"
+ "\xa4\t\xcd\t\xac\t"
+ "\xa4\t\xcd\t\xae\t"
+ "\xa4\t\xcd\t\xaf\t"
+ "\xa4\t\xcd\t\xb0\t"
+ "\xa4\t\xcd\t\xb2\t"
+ "\xa4\t\xcd\t\xf0\t"
+ "\xa4\n\xcd\n\xa4\n"
+ "\xa4\n\xcd\n\xb0\n"
+ "\xa5\t\xcd\t\xac\t"
+ "\xa5\t\xcd\t\xaf\t"
+ "\xa5\t\xcd\t\xb0\t"
+ "\xa5\t\xcd\t\xf0\t"
+ "\xa5\n\xcd\n\xb0\n"
+ "\xa6\t\xcd\t\x97\t"
+ "\xa6\t\xcd\t\x98\t"
+ "\xa6\t\xcd\t\xa6\t"
+ "\xa6\t\xcd\t\xa7\t"
+ "\xa6\t\xcd\t\xa8\t"
+ "\xa6\t\xcd\t\xac\t"
+ "\xa6\t\xcd\t\xad\t"
+ "\xa6\t\xcd\t\xae\t"
+ "\xa6\t\xcd\t\xaf\t"
+ "\xa6\t\xcd\t\xb0\t"
+ "\xa6\t\xcd\t\xf0\t"
+ "\xa6\n\xcd\n\x98\n"
+ "\xa6\n\xcd\n\xa6\n"
+ "\xa6\n\xcd\n\xa7\n"
+ "\xa6\n\xcd\n\xad\n"
+ "\xa6\n\xcd\n\xae\n"
+ "\xa6\n\xcd\n\xaf\n"
+ "\xa6\n\xcd\n\xb0\n"
+ "\xa6\n\xcd\n\xb5\n"
+ "\xa7\t\xcd\t\xa8\t"
+ "\xa7\t\xcd\t\xac\t"
+ "\xa7\t\xcd\t\xae\t"
+ "\xa7\t\xcd\t\xaf\t"
+ "\xa7\t\xcd\t\xb0\t"
+ "\xa7\t\xcd\t\xf0\t"
+ "\xa7\n\xcd\n\xb0\n"
+ "\xa8\t\xcd\t\x9f\t"
+ "\xa8\t\xcd\t\xa0\t"
+ "\xa8\t\xcd\t\xa1\t"
+ "\xa8\t\xcd\t\xa4\t"
+ "\xa8\t\xcd\t\xa5\t"
+ "\xa8\t\xcd\t\xa6\t"
+ "\xa8\t\xcd\t\xa7\t"
+ "\xa8\t\xcd\t\xa8\t"
+ "\xa8\t\xcd\t\xac\t"
+ "\xa8\t\xcd\t\xae\t"
+ "\xa8\t\xcd\t\xaf\t"
+ "\xa8\t\xcd\t\xb0\t"
+ "\xa8\t\xcd\t\xb8\t"
+ "\xa8\t\xcd\t\xf0\t"
+ "\xa8\n\xcd\n\xb0\n"
+ "\xaa\t\xcd\t\x9f\t"
+ "\xaa\t\xcd\t\xa4\t"
+ "\xaa\t\xcd\t\xa8\t"
+ "\xaa\t\xcd\t\xaa\t"
+ "\xaa\t\xcd\t\xac\t"
+ "\xaa\t\xcd\t\xae\t"
+ "\xaa\t\xcd\t\xaf\t"
+ "\xaa\t\xcd\t\xb0\t"
+ "\xaa\t\xcd\t\xb2\t"
+ "\xaa\t\xcd\t\xb8\t"
+ "\xaa\t\xcd\t\xf0\t"
+ "\xaa\n\xcd\n\xb0\n"
+ "\xab\t\xcd\t\x9f\t"
+ "\xab\t\xcd\t\xac\t"
+ "\xab\t\xcd\t\xaf\t"
+ "\xab\t\xcd\t\xb0\t"
+ "\xab\t\xcd\t\xb2\t"
+ "\xab\t\xcd\t\xf0\t"
+ "\xab\n\xbc\n"
+ "\xab\n\xcd\n\xb0\n"
+ "\xac\t\xcd\t\x9c\t"
+ "\xac\t\xcd\t\x9d\t"
+ "\xac\t\xcd\t\xa1\t"
+ "\xac\t\xcd\t\xa2\t"
+ "\xac\t\xcd\t\xa6\t"
+ "\xac\t\xcd\t\xa7\t"
+ "\xac\t\xcd\t\xac\t"
+ "\xac\t\xcd\t\xad\t"
+ "\xac\t\xcd\t\xaf\t"
+ "\xac\t\xcd\t\xb0\t"
+ "\xac\t\xcd\t\xb2\t"
+ "\xac\t\xcd\t\xf0\t"
+ "\xac\n\xcd\n\xb0\n"
+ "\xad\t\xcd\t\xac\t"
+ "\xad\t\xcd\t\xaf\t"
+ "\xad\t\xcd\t\xb0\t"
+ "\xad\t\xcd\t\xb2\t"
+ "\xad\t\xcd\t\xf0\t"
+ "\xad\n\xcd\n\xb0\n"
+ "\xae\t\xcd\t\xa4\t"
+ "\xae\t\xcd\t\xa6\t"
+ "\xae\t\xcd\t\xa8\t"
+ "\xae\t\xcd\t\xaa\t"
+ "\xae\t\xcd\t\xab\t"
+ "\xae\t\xcd\t\xac\t"
+ "\xae\t\xcd\t\xad\t"
+ "\xae\t\xcd\t\xae\t"
+ "\xae\t\xcd\t\xaf\t"
+ "\xae\t\xcd\t\xb0\t"
+ "\xae\t\xcd\t\xb2\t"
+ "\xae\t\xcd\t\xf0\t"
+ "\xae\n\xcd\n\xb0\n"
+ "\xaf\t\xcd\t\xac\t"
+ "\xaf\t\xcd\t\xaf\t"
+ "\xaf\t\xcd\t\xb0\t"
+ "\xaf\t\xcd\t\xf0\t"
+ "\xaf\n\xcd\n\xb0\n"
+ "\xb0\t\xcd\t\x95\t"
+ "\xb0\t\xcd\t\x96\t"
+ "\xb0\t\xcd\t\x97\t"
+ "\xb0\t\xcd\t\x98\t"
+ "\xb0\t\xcd\t\x99\t"
+ "\xb0\t\xcd\t\x9a\t"
+ "\xb0\t\xcd\t\x9b\t"
+ "\xb0\t\xcd\t\x9c\t"
+ "\xb0\t\xcd\t\x9d\t"
+ "\xb0\t\xcd\t\x9e\t"
+ "\xb0\t\xcd\t\x9f\t"
+ "\xb0\t\xcd\t\xa0\t"
+ "\xb0\t\xcd\t\xa1\t"
+ "\xb0\t\xcd\t\xa2\t"
+ "\xb0\t\xcd\t\xa3\t"
+ "\xb0\t\xcd\t\xa4\t"
+ "\xb0\t\xcd\t\xa5\t"
+ "\xb0\t\xcd\t\xa6\t"
+ "\xb0\t\xcd\t\xa7\t"
+ "\xb0\t\xcd\t\xa8\t"
+ "\xb0\t\xcd\t\xaa\t"
+ "\xb0\t\xcd\t\xab\t"
+ "\xb0\t\xcd\t\xac\t"
+ "\xb0\t\xcd\t\xad\t"
+ "\xb0\t\xcd\t\xae\t"
+ "\xb0\t\xcd\t\xaf\t"
+ "\xb0\t\xcd\t\xb0\t"
+ "\xb0\t\xcd\t\xb2\t"
+ "\xb0\t\xcd\t\xb6\t"
+ "\xb0\t\xcd\t\xb7\t"
+ "\xb0\t\xcd\t\xb8\t"
+ "\xb0\t\xcd\t\xb9\t"
+ "\xb0\t\xcd\t\xce\t"
+ "\xb0\t\xcd\t\xdc\t"
+ "\xb0\t\xcd\t\xdd\t"
+ "\xb0\t\xcd\t\xdf\t"
+ "\xb0\t\xcd\t\xf0\t"
+ "\xb0\t\xcd\t\xf1\t"
+ "\xb0\n\xcd\n\x95\n"
+ "\xb0\n\xcd\n\x95\n\xcd\n\xb7\n"
+ "\xb0\n\xcd\n\x96\n"
+ "\xb0\n\xcd\n\x97\n"
+ "\xb0\n\xcd\n\x98\n"
+ "\xb0\n\xcd\n\x99\n"
+ "\xb0\n\xcd\n\x9a\n"
+ "\xb0\n\xcd\n\x9b\n"
+ "\xb0\n\xcd\n\x9c\n"
+ "\xb0\n\xcd\n\x9c\n\xcd\n\x9e\n"
+ "\xb0\n\xcd\n\x9d\n"
+ "\xb0\n\xcd\n\x9e\n"
+ "\xb0\n\xcd\n\x9f\n"
+ "\xb0\n\xcd\n\xa0\n"
+ "\xb0\n\xcd\n\xa1\n"
+ "\xb0\n\xcd\n\xa2\n"
+ "\xb0\n\xcd\n\xa3\n"
+ "\xb0\n\xcd\n\xa4\n"
+ "\xb0\n\xcd\n\xa5\n"
+ "\xb0\n\xcd\n\xa6\n"
+ "\xb0\n\xcd\n\xa7\n"
+ "\xb0\n\xcd\n\xa8\n"
+ "\xb0\n\xcd\n\xaa\n"
+ "\xb0\n\xcd\n\xab\n"
+ "\xb0\n\xcd\n\xac\n"
+ "\xb0\n\xcd\n\xad\n"
+ "\xb0\n\xcd\n\xae\n"
+ "\xb0\n\xcd\n\xaf\n"
+ "\xb0\n\xcd\n\xb0\n"
+ "\xb0\n\xcd\n\xb2\n"
+ "\xb0\n\xcd\n\xb3\n"
+ "\xb0\n\xcd\n\xb5\n"
+ "\xb0\n\xcd\n\xb6\n"
+ "\xb0\n\xcd\n\xb7\n"
+ "\xb0\n\xcd\n\xb8\n"
+ "\xb0\n\xcd\n\xb9\n"
+ "\xb0\n\xcd\n\xf9\n"
+ "\xb2\t\xcd\t\x95\t"
+ "\xb2\t\xcd\t\x97\t"
+ "\xb2\t\xcd\t\x98\t"
+ "\xb2\t\xcd\t\x9f\t"
+ "\xb2\t\xcd\t\xa1\t"
+ "\xb2\t\xcd\t\xa2\t"
+ "\xb2\t\xcd\t\xa6\t"
+ "\xb2\t\xcd\t\xaa\t"
+ "\xb2\t\xcd\t\xab\t"
+ "\xb2\t\xcd\t\xac\t"
+ "\xb2\t\xcd\t\xae\t"
+ "\xb2\t\xcd\t\xaf\t"
+ "\xb2\t\xcd\t\xb0\t"
+ "\xb2\t\xcd\t\xb2\t"
+ "\xb2\t\xcd\t\xb8\t"
+ "\xb2\t\xcd\t\xf0\t"
+ "\xb2\n\xcd\n\xb0\n"
+ "\xb3\n\xcd\n\xb0\n"
+ "\xb5\n\xcd\n\xb0\n"
+ "\xb6\t\xcd\t\x9a\t"
+ "\xb6\t\xcd\t\x9b\t"
+ "\xb6\t\xcd\t\x9f\t"
+ "\xb6\t\xcd\t\xa4\t"
+ "\xb6\t\xcd\t\xa8\t"
+ "\xb6\t\xcd\t\xac\t"
+ "\xb6\t\xcd\t\xae\t"
+ "\xb6\t\xcd\t\xaf\t"
+ "\xb6\t\xcd\t\xb0\t"
+ "\xb6\t\xcd\t\xb2\t"
+ "\xb6\t\xcd\t\xf0\t"
+ "\xb6\n\xcd\n\xb0\n"
+ "\xb7\t\xcd\t\x95\t"
+ "\xb7\t\xcd\t\x9f\t"
+ "\xb7\t\xcd\t\xa0\t"
+ "\xb7\t\xcd\t\xa3\t"
+ "\xb7\t\xcd\t\xaa\t"
+ "\xb7\t\xcd\t\xab\t"
+ "\xb7\t\xcd\t\xac\t"
+ "\xb7\t\xcd\t\xae\t"
+ "\xb7\t\xcd\t\xaf\t"
+ "\xb7\t\xcd\t\xb0\t"
+ "\xb7\t\xcd\t\xf0\t"
+ "\xb7\n\xcd\n\xb0\n"
+ "\xb8\t\xcd\t\x95\t"
+ "\xb8\t\xcd\t\x96\t"
+ "\xb8\t\xcd\t\x9f\t"
+ "\xb8\t\xcd\t\xa4\t"
+ "\xb8\t\xcd\t\xa5\t"
+ "\xb8\t\xcd\t\xa8\t"
+ "\xb8\t\xcd\t\xaa\t"
+ "\xb8\t\xcd\t\xab\t"
+ "\xb8\t\xcd\t\xac\t"
+ "\xb8\t\xcd\t\xae\t"
+ "\xb8\t\xcd\t\xaf\t"
+ "\xb8\t\xcd\t\xb0\t"
+ "\xb8\t\xcd\t\xb2\t"
+ "\xb8\t\xcd\t\xf0\t"
+ "\xb8\n\xcd\n\xb0\n"
+ "\xb9\t\xcd\t\xa3\t"
+ "\xb9\t\xcd\t\xa8\t"
+ "\xb9\t\xcd\t\xac\t"
+ "\xb9\t\xcd\t\xae\t"
+ "\xb9\t\xcd\t\xaf\t"
+ "\xb9\t\xcd\t\xb0\t"
+ "\xb9\t\xcd\t\xb2\t"
+ "\xb9\t\xcd\t\xf0\t"
+ "\xb9\n\xcd\n\xae\n"
+ "\xb9\n\xcd\n\xaf\n"
+ "\xb9\n\xcd\n\xb0\n"
+ "\xb9\n\xcd\n\xb5\n"
+ "\xce\t\xcd\t\xac\t"
+ "\xce\t\xcd\t\xaf\t"
+ "\xce\t\xcd\t\xb0\t"
+ "\xce\t\xcd\t\xf0\t"
+ "\xdc\t"
+ "\xdc\t\xcd\t\x97\t"
+ "\xdc\t\xcd\t\xac\t"
+ "\xdc\t\xcd\t\xaf\t"
+ "\xdc\t\xcd\t\xb0\t"
+ "\xdc\t\xcd\t\xf0\t"
+ "\xdd\t"
+ "\xdd\t\xcd\t\xac\t"
+ "\xdd\t\xcd\t\xaf\t"
+ "\xdd\t\xcd\t\xb0\t"
+ "\xdd\t\xcd\t\xf0\t"
+ "\xdf\t\xcd\t\xac\t"
+ "\xdf\t\xcd\t\xaf\t"
+ "\xdf\t\xcd\t\xb0\t"
+ "\xdf\t\xcd\t\xf0\t"
+ "\xf0\t\xcd\t\x95\t"
+ "\xf0\t\xcd\t\x96\t"
+ "\xf0\t\xcd\t\x97\t"
+ "\xf0\t\xcd\t\x98\t"
+ "\xf0\t\xcd\t\x99\t"
+ "\xf0\t\xcd\t\x9a\t"
+ "\xf0\t\xcd\t\x9b\t"
+ "\xf0\t\xcd\t\x9c\t"
+ "\xf0\t\xcd\t\x9d\t"
+ "\xf0\t\xcd\t\x9e\t"
+ "\xf0\t\xcd\t\x9f\t"
+ "\xf0\t\xcd\t\xa3\t"
+ "\xf0\t\xcd\t\xa5\t"
+ "\xf0\t\xcd\t\xa6\t"
+ "\xf0\t\xcd\t\xa7\t"
+ "\xf0\t\xcd\t\xa8\t"
+ "\xf0\t\xcd\t\xaa\t"
+ "\xf0\t\xcd\t\xab\t"
+ "\xf0\t\xcd\t\xac\t"
+ "\xf0\t\xcd\t\xae\t"
+ "\xf0\t\xcd\t\xaf\t"
+ "\xf0\t\xcd\t\xb0\t"
+ "\xf0\t\xcd\t\xb2\t"
+ "\xf0\t\xcd\t\xb6\t"
+ "\xf0\t\xcd\t\xce\t"
+ "\xf0\t\xcd\t\xdc\t"
+ "\xf0\t\xcd\t\xdd\t"
+ "\xf0\t\xcd\t\xdf\t"
+ "\xf0\t\xcd\t\xf0\t"
+ "\xf0\t\xcd\t\xf1\t"
+ "\xf1\t\xcd\t\xac\t"
+ "\xf1\t\xcd\t\xaf\t"
+ "\xf1\t\xcd\t\xb0\t"
+ "\xf1\t\xcd\t\xf0\t"
+ "\xf9\n\xcd\n\xb0\n"
- "fd"

```
