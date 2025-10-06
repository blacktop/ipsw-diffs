## BrailleTranslation

> `/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation`

```diff

-344.0.0.0.0
-  __TEXT.__text: 0x22ee8
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x1700
-  __TEXT.__const: 0xbb4
-  __TEXT.__cstring: 0x14d7
+346.2.4.0.0
+  __TEXT.__text: 0x21988
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x15d0
+  __TEXT.__const: 0xc06
+  __TEXT.__cstring: 0x148a
   __TEXT.__oslogstring: 0x3f6
-  __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__ustring: 0xc2
+  __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__swift5_typeref: 0x1fe
-  __TEXT.__constg_swiftt: 0x974
-  __TEXT.__swift5_reflstr: 0x2aa
-  __TEXT.__swift5_fieldmd: 0x2b8
-  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_typeref: 0x1d4
+  __TEXT.__constg_swiftt: 0xa00
+  __TEXT.__swift5_reflstr: 0x29a
+  __TEXT.__swift5_fieldmd: 0x2c4
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x934
-  __TEXT.__objc_classname: 0x3a7
-  __TEXT.__objc_methname: 0x3405
-  __TEXT.__objc_methtype: 0xb78
-  __TEXT.__objc_stubs: 0x2840
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0x120
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x78
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__unwind_info: 0x8f4
+  __TEXT.__objc_classname: 0x323
+  __TEXT.__objc_methname: 0x3247
+  __TEXT.__objc_methtype: 0x9ce
+  __TEXT.__objc_stubs: 0x2700
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37b8
-  __DATA_CONST.__objc_selrefs: 0xd88
+  __DATA_CONST.__objc_const: 0x33a8
+  __DATA_CONST.__objc_selrefs: 0xd60
   __DATA_CONST.__objc_arraydata: 0x138
   __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_const: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0xe8
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH.__objc_data: 0x0
-  __AUTH.__data: 0x160
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x1a0
-  __DATA.__objc_superrefs: 0xc0
-  __DATA.__objc_ivar: 0x154
-  __DATA.__data: 0x5d0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__const: 0x1c8
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH.__objc_data: 0xfd0
+  __AUTH.__data: 0x360
+  __DATA.__objc_protorefs: 0x28
+  __DATA.__objc_classrefs: 0x178
+  __DATA.__objc_superrefs: 0xa8
+  __DATA.__objc_ivar: 0x150
+  __DATA.__data: 0x550
   __DATA.__bss: 0xb8
   __DATA.__common: 0x30
-  __DATA_DIRTY.__const: 0x1f8
-  __DATA_DIRTY.__objc_const: 0xaa0
-  __DATA_DIRTY.__objc_data: 0x1648
-  __DATA_DIRTY.__data: 0x158
+  __DATA_DIRTY.__const: 0xc0
+  __DATA_DIRTY.__objc_const: 0x788
+  __DATA_DIRTY.__objc_data: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 55264F01-47A4-3392-B39B-7416DF391F04
-  Functions: 847
-  Symbols:   1971
-  CStrings:  1098
+  UUID: 87FB80B3-6025-3951-882D-C40C12E2DD90
+  Functions: 829
+  Symbols:   1913
+  CStrings:  1079
 
Symbols:
+ +[BRLTJBrailleStateManager manager]
+ -[BRLTJBrailleStateManager .cxx_destruct]
+ -[BRLTJBrailleStateManager delete]
+ -[BRLTJBrailleStateManager displayedBraille]
+ -[BRLTJBrailleStateManager displayedScript]
+ -[BRLTJBrailleStateManager escapeCommand]
+ -[BRLTJBrailleStateManager forwardDelete]
+ -[BRLTJBrailleStateManager initWithUnderlyingObject:]
+ -[BRLTJBrailleStateManager insertBrailleChar:]
+ -[BRLTJBrailleStateManager isCandidateSelectionActive]
+ -[BRLTJBrailleStateManager isEditing]
+ -[BRLTJBrailleStateManager isShowingAlert]
+ -[BRLTJBrailleStateManager isShowingTerminalOutput]
+ -[BRLTJBrailleStateManager isWordDescriptionActive]
+ -[BRLTJBrailleStateManager returnCommand]
+ -[BRLTJBrailleStateManager scriptLocationForBrailleLocation:]
+ -[BRLTJBrailleStateManager selectCandidate]
+ -[BRLTJBrailleStateManager setBrailleSelection:]
+ -[BRLTJBrailleStateManager setDelegate:]
+ -[BRLTJBrailleStateManager setIsShowingAlert:]
+ -[BRLTJBrailleStateManager setIsShowingTerminalOutput:]
+ -[BRLTJBrailleStateManager setScript:]
+ -[BRLTJBrailleStateManager setTranslationDelegate:outputMode:inputMode:candidateSelectionLanguage:]
+ -[BRLTJBrailleStateManager showNextCandidate]
+ -[BRLTJBrailleStateManager showNextWordDescription]
+ -[BRLTJBrailleStateManager showPreviousCandidate]
+ -[BRLTJBrailleStateManager showPreviousWordDescription]
+ -[BRLTJBrailleStateManager startCandidateSelection]
+ -[BRLTJBrailleStateManager underlyingObject]
+ -[BRLTJBrailleStateManager wordDescriptionCommand]
+ -[BRLTJBrailleString .cxx_destruct]
+ -[BRLTJBrailleString NSFocus]
+ -[BRLTJBrailleString NSSelection]
+ -[BRLTJBrailleString NSStage]
+ -[BRLTJBrailleString NSSuggestion]
+ -[BRLTJBrailleString initWithUnderlyingObject:]
+ -[BRLTJBrailleString isStageEmpty]
+ -[BRLTJBrailleString stageSignalledString]
+ -[BRLTJBrailleString stageString]
+ -[BRLTJBrailleString string]
+ -[BRLTJBrailleString underlyingObject]
+ -[BRLTJEditableString .cxx_destruct]
+ -[BRLTJEditableString NSFocus]
+ -[BRLTJEditableString NSSelection]
+ -[BRLTJEditableString NSSuggestion]
+ -[BRLTJEditableString append:]
+ -[BRLTJEditableString initWithString:selection:focus:token:]
+ -[BRLTJEditableString initWithString:selection:focus:token:suggestion:]
+ -[BRLTJEditableString initWithUnderlyingObject:]
+ -[BRLTJEditableString init]
+ -[BRLTJEditableString string]
+ -[BRLTJEditableString tokenForLocation:]
+ -[BRLTJEditableString underlyingObject]
+ -[BRLTJJapaneseProcessor .cxx_destruct]
+ -[BRLTJJapaneseProcessor init]
+ -[BRLTJJapaneseProcessor isWordDescriptionLike:]
+ -[BRLTJJapaneseProcessor longVowelExpressedFor:partOfSpeech:]
+ -[BRLTJJapaneseProcessor replaceKataWithHira:]
+ -[BRLTJJapaneseProcessor spacedYomiOfWordDescription:]
+ -[BRLTJMecabraWrapper .cxx_destruct]
+ -[BRLTJMecabraWrapper analyzeString:]
+ -[BRLTJMecabraWrapper dealloc]
+ -[BRLTJMecabraWrapper getCurrentCandidateAnalysisString]
+ -[BRLTJMecabraWrapper getCurrentCandidateSurface]
+ -[BRLTJMecabraWrapper init]
+ -[BRLTJMecabraWrapper learnCandidate:]
+ -[BRLTJMecabraWrapper moveToNextCandidate]
+ -[BRLTJTranslatorWrapper .cxx_destruct]
+ -[BRLTJTranslatorWrapper arrayFromData:]
+ -[BRLTJTranslatorWrapper brailleForText:]
+ -[BRLTJTranslatorWrapper initWithTranslationDelegate:outputMode:inputMode:]
+ -[BRLTJTranslatorWrapper inputMode]
+ -[BRLTJTranslatorWrapper outputMode]
+ -[BRLTJTranslatorWrapper setInputMode:]
+ -[BRLTJTranslatorWrapper setOutputMode:]
+ -[BRLTJTranslatorWrapper textForBraille:]
+ _BRLTJIndexForUnicharIndex
+ _BRLTJRangeForUnicharRange
+ _BRLTJUnicharIndexForIndex
+ _BRLTJUnicharRangeForRange
+ _OBJC_CLASS_$_BRLTJBrailleStateManager
+ _OBJC_CLASS_$_BRLTJBrailleStateManagerInternal
+ _OBJC_CLASS_$_BRLTJBrailleString
+ _OBJC_CLASS_$_BRLTJBrailleStringInternal
+ _OBJC_CLASS_$_BRLTJEditableString
+ _OBJC_CLASS_$_BRLTJEditableStringInternal
+ _OBJC_CLASS_$_BRLTJJapaneseProcessor
+ _OBJC_CLASS_$_BRLTJMecabraWrapper
+ _OBJC_CLASS_$_BRLTJTranslatorWrapper
+ _OBJC_CLASS_$__TtC18BrailleTranslation15BRLTJTranslator
+ _OBJC_CLASS_$__TtC18BrailleTranslation21BRLTJCandidateManager
+ _OBJC_CLASS_$__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ _OBJC_CLASS_$__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ _OBJC_CLASS_$__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ _OBJC_IVAR_$_BRLTJBrailleStateManager._underlyingObject
+ _OBJC_IVAR_$_BRLTJBrailleString._underlyingObject
+ _OBJC_IVAR_$_BRLTJEditableString._underlyingObject
+ _OBJC_IVAR_$_BRLTJJapaneseProcessor._kataToHira
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._candidateRefForSurface
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._context
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._currentAnalysis
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._currentSurface
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._mecabra
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._reachedEnd
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._string
+ _OBJC_IVAR_$_BRLTJTranslatorWrapper._inputMode
+ _OBJC_IVAR_$_BRLTJTranslatorWrapper._outputMode
+ _OBJC_IVAR_$_BRLTJTranslatorWrapper._translationDelegate
+ _OBJC_METACLASS_$_BRLTJBrailleStateManager
+ _OBJC_METACLASS_$_BRLTJBrailleStateManagerInternal
+ _OBJC_METACLASS_$_BRLTJBrailleString
+ _OBJC_METACLASS_$_BRLTJBrailleStringInternal
+ _OBJC_METACLASS_$_BRLTJEditableString
+ _OBJC_METACLASS_$_BRLTJEditableStringInternal
+ _OBJC_METACLASS_$_BRLTJJapaneseProcessor
+ _OBJC_METACLASS_$_BRLTJMecabraWrapper
+ _OBJC_METACLASS_$_BRLTJTranslatorWrapper
+ _OBJC_METACLASS_$__TtC18BrailleTranslation15BRLTJTranslator
+ _OBJC_METACLASS_$__TtC18BrailleTranslation21BRLTJCandidateManager
+ _OBJC_METACLASS_$__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ _OBJC_METACLASS_$__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ _OBJC_METACLASS_$__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ __CATEGORY_BRLTJBrailleStateManagerInternal_$_BrailleTranslation
+ __CATEGORY_BRLTJBrailleStringInternal_$_BrailleTranslation
+ __CATEGORY_BRLTJEditableStringInternal_$_BrailleTranslation
+ __CLASS_PROPERTIES_BRLTJBrailleStateManagerInternal
+ __DATA_BRLTJBrailleStateManagerInternal
+ __DATA_BRLTJBrailleStringInternal
+ __DATA_BRLTJEditableStringInternal
+ __DATA__TtC18BrailleTranslation15BRLTJTranslator
+ __DATA__TtC18BrailleTranslation18BRLTJStateNotifier
+ __DATA__TtC18BrailleTranslation21BRLTJCandidateManager
+ __DATA__TtC18BrailleTranslation27BRLTJWordDescriptionManager
+ __DATA__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ __DATA__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ __DATA__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ __IVARS_BRLTJBrailleStateManagerInternal
+ __IVARS_BRLTJBrailleStringInternal
+ __IVARS_BRLTJEditableStringInternal
+ __IVARS__TtC18BrailleTranslation15BRLTJTranslator
+ __IVARS__TtC18BrailleTranslation18BRLTJStateNotifier
+ __IVARS__TtC18BrailleTranslation21BRLTJCandidateManager
+ __IVARS__TtC18BrailleTranslation27BRLTJWordDescriptionManager
+ __IVARS__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ __IVARS__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ __IVARS__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ __METACLASS_DATA_BRLTJBrailleStateManagerInternal
+ __METACLASS_DATA_BRLTJBrailleStringInternal
+ __METACLASS_DATA_BRLTJEditableStringInternal
+ __METACLASS_DATA__TtC18BrailleTranslation15BRLTJTranslator
+ __METACLASS_DATA__TtC18BrailleTranslation18BRLTJStateNotifier
+ __METACLASS_DATA__TtC18BrailleTranslation21BRLTJCandidateManager
+ __METACLASS_DATA__TtC18BrailleTranslation27BRLTJWordDescriptionManager
+ __METACLASS_DATA__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ __METACLASS_DATA__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ __METACLASS_DATA__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ __OBJC_$_CLASS_METHODS_BRLTJBrailleStateManager
+ __OBJC_$_CLASS_METHODS_BRLTJBrailleStateManagerInternal
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleStateManager
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleStateManagerInternal
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleStateManagerInternal(BrailleTranslation)
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleString
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleStringInternal
+ __OBJC_$_INSTANCE_METHODS_BRLTJBrailleStringInternal(BrailleTranslation)
+ __OBJC_$_INSTANCE_METHODS_BRLTJEditableString
+ __OBJC_$_INSTANCE_METHODS_BRLTJEditableStringInternal
+ __OBJC_$_INSTANCE_METHODS_BRLTJEditableStringInternal(BrailleTranslation)
+ __OBJC_$_INSTANCE_METHODS_BRLTJJapaneseProcessor
+ __OBJC_$_INSTANCE_METHODS_BRLTJMecabraWrapper
+ __OBJC_$_INSTANCE_METHODS_BRLTJTranslatorWrapper
+ __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation15BRLTJTranslator
+ __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation21BRLTJCandidateManager
+ __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult
+ __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult
+ __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJBrailleStateManager
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJBrailleString
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJEditableString
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJJapaneseProcessor
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJMecabraWrapper
+ __OBJC_$_INSTANCE_VARIABLES_BRLTJTranslatorWrapper
+ __OBJC_$_PROP_LIST_BRLTJBrailleStateManager
+ __OBJC_$_PROP_LIST_BRLTJBrailleString
+ __OBJC_$_PROP_LIST_BRLTJEditableString
+ __OBJC_$_PROP_LIST_BRLTJTranslatorWrapper
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRLTJBrailleStateManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BRLTJBrailleStateManagerDelegate
+ __OBJC_CLASS_RO_$_BRLTJBrailleStateManager
+ __OBJC_CLASS_RO_$_BRLTJBrailleString
+ __OBJC_CLASS_RO_$_BRLTJEditableString
+ __OBJC_CLASS_RO_$_BRLTJJapaneseProcessor
+ __OBJC_CLASS_RO_$_BRLTJMecabraWrapper
+ __OBJC_CLASS_RO_$_BRLTJTranslatorWrapper
+ __OBJC_LABEL_PROTOCOL_$_BRLTJBrailleStateManagerDelegate
+ __OBJC_METACLASS_RO_$_BRLTJBrailleStateManager
+ __OBJC_METACLASS_RO_$_BRLTJBrailleString
+ __OBJC_METACLASS_RO_$_BRLTJEditableString
+ __OBJC_METACLASS_RO_$_BRLTJJapaneseProcessor
+ __OBJC_METACLASS_RO_$_BRLTJMecabraWrapper
+ __OBJC_METACLASS_RO_$_BRLTJTranslatorWrapper
+ __OBJC_PROTOCOL_$_BRLTJBrailleStateManagerDelegate
+ __PROPERTIES_BRLTJBrailleStateManagerInternal
+ __PROPERTIES_BRLTJBrailleStringInternal
+ __PROPERTIES_BRLTJEditableStringInternal
+ __PROTOCOLS_BRLTJEditableStringInternal
+ __PROTOCOLS_BRLTJEditableStringInternal.2
+ _objc_msgSend$rangeOfComposedCharacterSequenceAtIndex:
+ _objc_msgSend$setTranslationDelegate:outputMode:inputMode:candidateSelectionLanguage:
+ _symbolic $s18BrailleTranslation29BRLTJCandidateManagerProtocolP
+ _symbolic $s18BrailleTranslation30BRLTJTranslationResultProtocolP
+ _symbolic SSSg
+ _symbolic So19BRLTJMecabraWrapperCSg
+ _symbolic So22BRLTJTranslatorWrapperCSg
+ _symbolic So32BRLTJBrailleStateManagerDelegate_p
+ _symbolic _____ 18BrailleTranslation012BRLTJTextForaB6ResultC
+ _symbolic _____ 18BrailleTranslation019BRLTJBrailleForTextB6ResultC
+ _symbolic _____ 18BrailleTranslation021BRLTJBrailleForScriptB6ResultC
+ _symbolic _____ 18BrailleTranslation15BRLTJTranslatorC
+ _symbolic _____ 18BrailleTranslation18BRLTJBrailleStringC
+ _symbolic _____ 18BrailleTranslation18BRLTJStateNotifierC
+ _symbolic _____ 18BrailleTranslation19BRLTJEditableStringC
+ _symbolic _____ 18BrailleTranslation21BRLTJCandidateManagerC
+ _symbolic _____ 18BrailleTranslation24BRLTJBrailleStateManagerC
+ _symbolic _____ 18BrailleTranslation27BRLTJWordDescriptionManagerC
+ _symbolic _____ So19BRLTTranslationModeV
+ _symbolic _____Sg 18BrailleTranslation15BRLTJTranslatorC
+ _symbolic _____Sg 18BrailleTranslation18BRLTJBrailleStringC
+ _symbolic _____Sg 18BrailleTranslation18BRLTJStateNotifierC
+ _symbolic ______p 18BrailleTranslation29BRLTJCandidateManagerProtocolP
- +[BRLTJaBrailleStateManager manager]
- -[BRLTJaBrailleForJaTranslationResult .cxx_destruct]
- -[BRLTJaBrailleForJaTranslationResult initWithTranslator:source:]
- -[BRLTJaBrailleForJaTranslationResult targetLocationForSourceLocation:]
- -[BRLTJaBrailleForJaTranslationResult underlyingObject]
- -[BRLTJaBrailleStateManager .cxx_destruct]
- -[BRLTJaBrailleStateManager delegate]
- -[BRLTJaBrailleStateManager delete]
- -[BRLTJaBrailleStateManager displayedBraille]
- -[BRLTJaBrailleStateManager displayedScript]
- -[BRLTJaBrailleStateManager escapeCommand]
- -[BRLTJaBrailleStateManager forwardDelete]
- -[BRLTJaBrailleStateManager initWithUnderlyingObject:]
- -[BRLTJaBrailleStateManager insertBrailleChar:]
- -[BRLTJaBrailleStateManager isCandidateSelectionActive]
- -[BRLTJaBrailleStateManager isEditing]
- -[BRLTJaBrailleStateManager isShowingAlert]
- -[BRLTJaBrailleStateManager isShowingTerminalOutput]
- -[BRLTJaBrailleStateManager isWordDescriptionActive]
- -[BRLTJaBrailleStateManager returnCommand]
- -[BRLTJaBrailleStateManager scriptLocationForBrailleLocation:]
- -[BRLTJaBrailleStateManager selectCandidate]
- -[BRLTJaBrailleStateManager setBrailleSelection:]
- -[BRLTJaBrailleStateManager setDelegate:]
- -[BRLTJaBrailleStateManager setIsShowingAlert:]
- -[BRLTJaBrailleStateManager setIsShowingTerminalOutput:]
- -[BRLTJaBrailleStateManager setScript:]
- -[BRLTJaBrailleStateManager setTranslator:]
- -[BRLTJaBrailleStateManager showNextCandidate]
- -[BRLTJaBrailleStateManager showNextWordDescription]
- -[BRLTJaBrailleStateManager showPreviousCandidate]
- -[BRLTJaBrailleStateManager showPreviousWordDescription]
- -[BRLTJaBrailleStateManager startCandidateSelection]
- -[BRLTJaBrailleStateManager translator]
- -[BRLTJaBrailleStateManager underlyingObject]
- -[BRLTJaBrailleStateManager wordDescriptionCommand]
- -[BRLTJaEditableString .cxx_destruct]
- -[BRLTJaEditableString NSFocus]
- -[BRLTJaEditableString NSSelection]
- -[BRLTJaEditableString NSSuggestion]
- -[BRLTJaEditableString append:]
- -[BRLTJaEditableString initWithString:selection:focus:suggestion:tokenRanges:]
- -[BRLTJaEditableString initWithString:selection:focus:token:]
- -[BRLTJaEditableString initWithString:selection:focus:token:suggestion:]
- -[BRLTJaEditableString init]
- -[BRLTJaEditableString string]
- -[BRLTJaEditableString tokenDict]
- -[BRLTJaEditableString tokenForLocation:]
- -[BRLTJaEditableString underlyingObject]
- -[BRLTJaJaForBrailleTranslationResult .cxx_destruct]
- -[BRLTJaJaForBrailleTranslationResult initWithTranslator:source:]
- -[BRLTJaJaForBrailleTranslationResult target]
- -[BRLTJaJaForBrailleTranslationResult underlyingObject]
- -[BRLTJaMecabraWrapper .cxx_destruct]
- -[BRLTJaMecabraWrapper analyzeString:]
- -[BRLTJaMecabraWrapper dealloc]
- -[BRLTJaMecabraWrapper getCurrentCandidateAnalysisString]
- -[BRLTJaMecabraWrapper getCurrentCandidateSurface]
- -[BRLTJaMecabraWrapper init]
- -[BRLTJaMecabraWrapper learnCandidate:]
- -[BRLTJaMecabraWrapper moveToNextCandidate]
- -[BRLTJaStagedString .cxx_destruct]
- -[BRLTJaStagedString NSFocus]
- -[BRLTJaStagedString NSSelection]
- -[BRLTJaStagedString NSStage]
- -[BRLTJaStagedString NSSuggestion]
- -[BRLTJaStagedString initWithString:selection:focus:suggestion:tokenRanges:stage:]
- -[BRLTJaStagedString initWithUnderlyingObject:]
- -[BRLTJaStagedString isStageEmpty]
- -[BRLTJaStagedString stageSignalledString]
- -[BRLTJaStagedString stageString]
- -[BRLTJaStagedString string]
- -[BRLTJaStagedString underlyingObject]
- -[BRLTJaTranslator .cxx_destruct]
- -[BRLTJaTranslator initWithTranslationDelegate:]
- -[BRLTJaTranslator translationDelegate]
- -[BRLTJaTranslator underlyingObject]
- -[BRLTJaTranslatorWrapper .cxx_destruct]
- -[BRLTJaTranslatorWrapper arrayFromData:]
- -[BRLTJaTranslatorWrapper brailleForText:]
- -[BRLTJaTranslatorWrapper initWithTranslationDelegate:]
- -[BRLTJaTranslatorWrapper textForBraille:]
- -[BRLTJapaneseProcessor .cxx_destruct]
- -[BRLTJapaneseProcessor init]
- -[BRLTJapaneseProcessor isWordDescriptionLike:]
- -[BRLTJapaneseProcessor longVowelExpressedFor:partOfSpeech:]
- -[BRLTJapaneseProcessor replaceKataWithHira:]
- -[BRLTJapaneseProcessor spacedYomiOfWordDescription:]
- _OBJC_CLASS_$_BRLTJaBrailleForJaTranslationResult
- _OBJC_CLASS_$_BRLTJaBrailleForJaTranslationResultInternal
- _OBJC_CLASS_$_BRLTJaBrailleStateManager
- _OBJC_CLASS_$_BRLTJaBrailleStateManagerInternal
- _OBJC_CLASS_$_BRLTJaEditableString
- _OBJC_CLASS_$_BRLTJaEditableStringInternal
- _OBJC_CLASS_$_BRLTJaJaForBrailleTranslationResult
- _OBJC_CLASS_$_BRLTJaJaForBrailleTranslationResultInternal
- _OBJC_CLASS_$_BRLTJaMecabraWrapper
- _OBJC_CLASS_$_BRLTJaStagedString
- _OBJC_CLASS_$_BRLTJaStagedStringInternal
- _OBJC_CLASS_$_BRLTJaTranslator
- _OBJC_CLASS_$_BRLTJaTranslatorInternal
- _OBJC_CLASS_$_BRLTJaTranslatorWrapper
- _OBJC_CLASS_$_BRLTJapaneseProcessor
- _OBJC_CLASS_$__TtC18BrailleTranslation22BRLTJaCandidateManager
- _OBJC_CLASS_$__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- _OBJC_IVAR_$_BRLTJaBrailleForJaTranslationResult._underlyingObject
- _OBJC_IVAR_$_BRLTJaBrailleStateManager._underlyingObject
- _OBJC_IVAR_$_BRLTJaEditableString._underlyingObject
- _OBJC_IVAR_$_BRLTJaJaForBrailleTranslationResult._underlyingObject
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._candidateRefForSurface
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._context
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._currentAnalysis
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._currentSurface
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._mecabra
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._reachedEnd
- _OBJC_IVAR_$_BRLTJaMecabraWrapper._string
- _OBJC_IVAR_$_BRLTJaStagedString._underlyingObject
- _OBJC_IVAR_$_BRLTJaTranslator._underlyingObject
- _OBJC_IVAR_$_BRLTJaTranslatorWrapper._translationDelegate
- _OBJC_IVAR_$_BRLTJapaneseProcessor._kataToHira
- _OBJC_METACLASS_$_BRLTJaBrailleForJaTranslationResult
- _OBJC_METACLASS_$_BRLTJaBrailleForJaTranslationResultInternal
- _OBJC_METACLASS_$_BRLTJaBrailleStateManager
- _OBJC_METACLASS_$_BRLTJaBrailleStateManagerInternal
- _OBJC_METACLASS_$_BRLTJaEditableString
- _OBJC_METACLASS_$_BRLTJaEditableStringInternal
- _OBJC_METACLASS_$_BRLTJaJaForBrailleTranslationResult
- _OBJC_METACLASS_$_BRLTJaJaForBrailleTranslationResultInternal
- _OBJC_METACLASS_$_BRLTJaMecabraWrapper
- _OBJC_METACLASS_$_BRLTJaStagedString
- _OBJC_METACLASS_$_BRLTJaStagedStringInternal
- _OBJC_METACLASS_$_BRLTJaTranslator
- _OBJC_METACLASS_$_BRLTJaTranslatorInternal
- _OBJC_METACLASS_$_BRLTJaTranslatorWrapper
- _OBJC_METACLASS_$_BRLTJapaneseProcessor
- _OBJC_METACLASS_$__TtC18BrailleTranslation22BRLTJaCandidateManager
- _OBJC_METACLASS_$__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- __CLASS_PROPERTIES_BRLTJaBrailleStateManagerInternal
- __DATA_BRLTJaBrailleForJaTranslationResultInternal
- __DATA_BRLTJaBrailleStateManagerInternal
- __DATA_BRLTJaEditableStringInternal
- __DATA_BRLTJaJaForBrailleTranslationResultInternal
- __DATA_BRLTJaStagedStringInternal
- __DATA_BRLTJaTranslatorInternal
- __DATA__TtC18BrailleTranslation22BRLTJaCandidateManager
- __DATA__TtC18BrailleTranslation28BRLTJaWordDescriptionManager
- __DATA__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- __IVARS_BRLTJaBrailleForJaTranslationResultInternal
- __IVARS_BRLTJaBrailleStateManagerInternal
- __IVARS_BRLTJaEditableStringInternal
- __IVARS_BRLTJaJaForBrailleTranslationResultInternal
- __IVARS_BRLTJaStagedStringInternal
- __IVARS_BRLTJaTranslatorInternal
- __IVARS__TtC18BrailleTranslation22BRLTJaCandidateManager
- __IVARS__TtC18BrailleTranslation28BRLTJaWordDescriptionManager
- __IVARS__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- __METACLASS_DATA_BRLTJaBrailleForJaTranslationResultInternal
- __METACLASS_DATA_BRLTJaBrailleStateManagerInternal
- __METACLASS_DATA_BRLTJaEditableStringInternal
- __METACLASS_DATA_BRLTJaJaForBrailleTranslationResultInternal
- __METACLASS_DATA_BRLTJaStagedStringInternal
- __METACLASS_DATA_BRLTJaTranslatorInternal
- __METACLASS_DATA__TtC18BrailleTranslation22BRLTJaCandidateManager
- __METACLASS_DATA__TtC18BrailleTranslation28BRLTJaWordDescriptionManager
- __METACLASS_DATA__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- __OBJC_$_CLASS_METHODS_BRLTJaBrailleStateManager
- __OBJC_$_CLASS_METHODS_BRLTJaBrailleStateManagerInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaBrailleForJaTranslationResult
- __OBJC_$_INSTANCE_METHODS_BRLTJaBrailleForJaTranslationResultInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaBrailleStateManager
- __OBJC_$_INSTANCE_METHODS_BRLTJaBrailleStateManagerInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaEditableString
- __OBJC_$_INSTANCE_METHODS_BRLTJaEditableStringInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaJaForBrailleTranslationResult
- __OBJC_$_INSTANCE_METHODS_BRLTJaJaForBrailleTranslationResultInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaMecabraWrapper
- __OBJC_$_INSTANCE_METHODS_BRLTJaStagedString
- __OBJC_$_INSTANCE_METHODS_BRLTJaStagedStringInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaTranslator
- __OBJC_$_INSTANCE_METHODS_BRLTJaTranslatorInternal
- __OBJC_$_INSTANCE_METHODS_BRLTJaTranslatorWrapper
- __OBJC_$_INSTANCE_METHODS_BRLTJapaneseProcessor
- __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation22BRLTJaCandidateManager
- __OBJC_$_INSTANCE_METHODS__TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaBrailleForJaTranslationResult
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaBrailleStateManager
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaEditableString
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaJaForBrailleTranslationResult
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaMecabraWrapper
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaStagedString
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaTranslator
- __OBJC_$_INSTANCE_VARIABLES_BRLTJaTranslatorWrapper
- __OBJC_$_INSTANCE_VARIABLES_BRLTJapaneseProcessor
- __OBJC_$_PROP_LIST_BRLTJaBrailleForJaTranslationResult
- __OBJC_$_PROP_LIST_BRLTJaBrailleStateManager
- __OBJC_$_PROP_LIST_BRLTJaEditableString
- __OBJC_$_PROP_LIST_BRLTJaJaForBrailleTranslationResult
- __OBJC_$_PROP_LIST_BRLTJaStagedString
- __OBJC_$_PROP_LIST_BRLTJaTranslator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRLTBrailleTranslationDelegateProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRLTJaBrailleStateManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRLTBrailleTranslationDelegateProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRLTJaBrailleStateManagerDelegate
- __OBJC_$_PROTOCOL_REFS_BRLTBrailleTranslationDelegateProtocol
- __OBJC_CLASS_RO_$_BRLTJaBrailleForJaTranslationResult
- __OBJC_CLASS_RO_$_BRLTJaBrailleStateManager
- __OBJC_CLASS_RO_$_BRLTJaEditableString
- __OBJC_CLASS_RO_$_BRLTJaJaForBrailleTranslationResult
- __OBJC_CLASS_RO_$_BRLTJaMecabraWrapper
- __OBJC_CLASS_RO_$_BRLTJaStagedString
- __OBJC_CLASS_RO_$_BRLTJaTranslator
- __OBJC_CLASS_RO_$_BRLTJaTranslatorWrapper
- __OBJC_CLASS_RO_$_BRLTJapaneseProcessor
- __OBJC_LABEL_PROTOCOL_$_BRLTBrailleTranslationDelegateProtocol
- __OBJC_LABEL_PROTOCOL_$_BRLTJaBrailleStateManagerDelegate
- __OBJC_METACLASS_RO_$_BRLTJaBrailleForJaTranslationResult
- __OBJC_METACLASS_RO_$_BRLTJaBrailleStateManager
- __OBJC_METACLASS_RO_$_BRLTJaEditableString
- __OBJC_METACLASS_RO_$_BRLTJaJaForBrailleTranslationResult
- __OBJC_METACLASS_RO_$_BRLTJaMecabraWrapper
- __OBJC_METACLASS_RO_$_BRLTJaStagedString
- __OBJC_METACLASS_RO_$_BRLTJaTranslator
- __OBJC_METACLASS_RO_$_BRLTJaTranslatorWrapper
- __OBJC_METACLASS_RO_$_BRLTJapaneseProcessor
- __OBJC_PROTOCOL_$_BRLTBrailleTranslationDelegateProtocol
- __OBJC_PROTOCOL_$_BRLTJaBrailleStateManagerDelegate
- __PROPERTIES_BRLTJaBrailleStateManagerInternal
- __PROPERTIES_BRLTJaEditableStringInternal
- __PROPERTIES_BRLTJaJaForBrailleTranslationResultInternal
- __PROPERTIES_BRLTJaStagedStringInternal
- __PROPERTIES_BRLTJaTranslatorInternal
- __PROTOCOLS_BRLTJaEditableStringInternal
- __PROTOCOLS_BRLTJaEditableStringInternal.2
- ___swift_memcpy16_8
- ___swift_noop_void_return
- _bzero
- _objc_msgSend$delegate
- _objc_msgSend$initWithString:NSSelection:NSFocus:NSSuggestion:tokenRangeDict:
- _objc_msgSend$initWithString:NSSelection:NSFocus:NSSuggestion:tokenRangeDict:stage:
- _objc_msgSend$initWithString:selection:focus:suggestion:tokenRanges:
- _objc_msgSend$initWithString:selection:focus:suggestion:tokenRanges:stage:
- _objc_msgSend$initWithTranslationDelegate:
- _objc_msgSend$initWithTranslator:source:
- _objc_msgSend$setTranslator:
- _objc_msgSend$target
- _objc_msgSend$targetLocationForSourceLocation:
- _objc_msgSend$tokenDict
- _objc_msgSend$translationDelegate
- _objc_retain_x28
- _symbolic $s18BrailleTranslation06BRLTJaB14ResultProtocolP
- _symbolic $s18BrailleTranslation30BRLTJaCandidateManagerProtocolP
- _symbolic So20BRLTJaMecabraWrapperCSg
- _symbolic So23BRLTJaTranslatorWrapperCSg
- _symbolic So33BRLTJaBrailleStateManagerDelegate_pSg
- _symbolic So38BRLTBrailleTranslationDelegateProtocol_pSg
- _symbolic _____ 18BrailleTranslation011BRLTJaJaForaB6ResultC
- _symbolic _____ 18BrailleTranslation06BRLTJaA12StateManagerC
- _symbolic _____ 18BrailleTranslation06BRLTJaa5ForJaB6ResultC
- _symbolic _____ 18BrailleTranslation06BRLTJaa9ForScriptB6ResultC
- _symbolic _____ 18BrailleTranslation16BRLTJaTranslatorC
- _symbolic _____ 18BrailleTranslation18BRLTJaStagedStringC
- _symbolic _____ 18BrailleTranslation20BRLTJaEditableStringC
- _symbolic _____ 18BrailleTranslation22BRLTJaCandidateManagerC
- _symbolic _____ 18BrailleTranslation28BRLTJaWordDescriptionManagerC
- _symbolic _____ So8_NSRangeV
- _symbolic _____Sg 18BrailleTranslation16BRLTJaTranslatorC
- _symbolic _____Sg 18BrailleTranslation18BRLTJaStagedStringC
- _symbolic ______p 18BrailleTranslation30BRLTJaCandidateManagerProtocolP
- _symbolic _____y_____SiG s18_DictionaryStorageC So8_NSRangeV
CStrings:
+ "(BRLTJEditableString) string = \""
+ "(BRLTJStagedString) string = \""
+ "@\"BRLTJBrailleStateManagerInternal\""
+ "@\"BRLTJBrailleStringInternal\""
+ "@\"BRLTJEditableStringInternal\""
+ "@40@0:8@16Q24Q32"
+ "BRLTJBrailleStateManager"
+ "BRLTJBrailleStateManagerDelegate"
+ "BRLTJBrailleStateManagerInternal"
+ "BRLTJBrailleString"
+ "BRLTJBrailleStringInternal"
+ "BRLTJEditableString"
+ "BRLTJEditableStringInternal"
+ "BRLTJJapaneseProcessor"
+ "BRLTJMecabraWrapper"
+ "BRLTJTranslatorWrapper"
+ "BrailleTranslation.BRLTJBrailleForScriptTranslationResult"
+ "BrailleTranslation.BRLTJBrailleForTextTranslationResult"
+ "BrailleTranslation.BRLTJEditableString"
+ "BrailleTranslation.BRLTJTextForBrailleTranslationResult"
+ "BrailleTranslation.BRLTJTranslator"
+ "Insert: commit stage to script"
+ "Show current candidate description: %s"
+ "Show current word description: %s"
+ "Start word description with stage = %@"
+ "T@\"BRLTJBrailleStateManagerInternal\",N,R"
+ "T@\"BRLTJBrailleStateManagerInternal\",R,V_underlyingObject"
+ "T@\"BRLTJBrailleString\",R,N"
+ "T@\"BRLTJBrailleStringInternal\",N,R"
+ "T@\"BRLTJBrailleStringInternal\",R,V_underlyingObject"
+ "T@\"BRLTJEditableString\",R,N"
+ "T@\"BRLTJEditableStringInternal\",N,R"
+ "T@\"BRLTJEditableStringInternal\",R,V_underlyingObject"
+ "TQ,N,V_inputMode"
+ "TQ,N,V_outputMode"
+ "_TtC18BrailleTranslation15BRLTJTranslator"
+ "_TtC18BrailleTranslation18BRLTJStateNotifier"
+ "_TtC18BrailleTranslation21BRLTJCandidateManager"
+ "_TtC18BrailleTranslation27BRLTJWordDescriptionManager"
+ "_TtC18BrailleTranslation36BRLTJBrailleForTextTranslationResult"
+ "_TtC18BrailleTranslation36BRLTJTextForBrailleTranslationResult"
+ "_TtC18BrailleTranslation38BRLTJBrailleForScriptTranslationResult"
+ "_inputMode"
+ "_outputMode"
+ "candidateSelectionLanguage"
+ "initWithTranslationDelegate:outputMode:inputMode:"
+ "inputMode"
+ "notifier"
+ "outputMode"
+ "rangeOfComposedCharacterSequenceAtIndex:"
+ "setInputMode:"
+ "setOutputMode:"
+ "setTranslationDelegate:outputMode:inputMode:candidateSelectionLanguage:"
+ "v48@0:8@16Q24Q32@40"
- "(BRLTJaEditableString) string = \""
- "(BRLTJaStagedString) string = \""
- "@\"BRLTJaBrailleForJaTranslationResultInternal\""
- "@\"BRLTJaBrailleStateManagerInternal\""
- "@\"BRLTJaEditableStringInternal\""
- "@\"BRLTJaJaForBrailleTranslationResultInternal\""
- "@\"BRLTJaStagedStringInternal\""
- "@\"BRLTJaTranslatorInternal\""
- "@\"NSString\"48@0:8@\"NSString\"16@\"NSString\"24Q32^@40"
- "@\"NSString\"72@0:8@\"NSString\"16@\"NSString\"24Q32{_NSRange=QQ}40^@56@\"BRLTTextFormattingRanges\"64"
- "@48@0:8@16@24Q32^@40"
- "@72@0:8@16@24Q32{_NSRange=QQ}40^@56@64"
- "@80@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40{_NSRange=QQ}56@72"
- "@96@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40{_NSRange=QQ}56@72{_NSRange=QQ}80"
- "BRLTBrailleTranslationDelegateProtocol"
- "BRLTJaBrailleForJaTranslationResult"
- "BRLTJaBrailleForJaTranslationResultInternal"
- "BRLTJaBrailleStateManager"
- "BRLTJaBrailleStateManagerDelegate"
- "BRLTJaBrailleStateManagerInternal"
- "BRLTJaEditableString"
- "BRLTJaEditableStringInternal"
- "BRLTJaJaForBrailleTranslationResult"
- "BRLTJaJaForBrailleTranslationResultInternal"
- "BRLTJaMecabraWrapper"
- "BRLTJaStagedString"
- "BRLTJaStagedStringInternal"
- "BRLTJaTranslator"
- "BRLTJaTranslatorInternal"
- "BRLTJaTranslatorWrapper"
- "BRLTJapaneseProcessor"
- "BrailleTranslation.BRLTJaBrailleForJaTranslationResult"
- "BrailleTranslation.BRLTJaBrailleForScriptTranslationResult"
- "BrailleTranslation.BRLTJaJaForBrailleTranslationResult"
- "BrailleTranslation.BRLTJaTranslator"
- "T@\"<BRLTBrailleTranslationDelegateProtocol>\",N,R,VtranslationDelegate"
- "T@\"<BRLTBrailleTranslationDelegateProtocol>\",R,N"
- "T@\"<BRLTJaBrailleStateManagerDelegate>\",C,N"
- "T@\"<BRLTJaBrailleStateManagerDelegate>\",N,&,Vdelegate"
- "T@\"BRLTJaBrailleForJaTranslationResultInternal\",R,V_underlyingObject"
- "T@\"BRLTJaBrailleStateManagerInternal\",N,R"
- "T@\"BRLTJaBrailleStateManagerInternal\",R,V_underlyingObject"
- "T@\"BRLTJaEditableString\",R,N"
- "T@\"BRLTJaEditableStringInternal\",N,R"
- "T@\"BRLTJaEditableStringInternal\",R,V_underlyingObject"
- "T@\"BRLTJaJaForBrailleTranslationResultInternal\",R,V_underlyingObject"
- "T@\"BRLTJaStagedString\",R,N"
- "T@\"BRLTJaStagedStringInternal\",N,R"
- "T@\"BRLTJaStagedStringInternal\",R,V_underlyingObject"
- "T@\"BRLTJaTranslator\",C,N"
- "T@\"BRLTJaTranslatorInternal\",N,&,Vtranslator"
- "T@\"BRLTJaTranslatorInternal\",R,V_underlyingObject"
- "T@\"NSDictionary\",N,R"
- "T@\"NSDictionary\",R,N"
- "_TtC18BrailleTranslation22BRLTJaCandidateManager"
- "_TtC18BrailleTranslation28BRLTJaWordDescriptionManager"
- "_TtC18BrailleTranslation39BRLTJaBrailleForScriptTranslationResult"
- "initWithString:NSSelection:NSFocus:NSSuggestion:tokenRangeDict:"
- "initWithString:NSSelection:NSFocus:NSSuggestion:tokenRangeDict:stage:"
- "initWithString:selection:focus:suggestion:tokenRanges:"
- "initWithString:selection:focus:suggestion:tokenRanges:stage:"
- "initWithTranslationDelegate:"
- "initWithTranslator:source:"
- "setTarget:"
- "setTranslator:"
- "targetLocationForSourceLocation:"
- "tokenDict"
- "translationWrapper"

```
