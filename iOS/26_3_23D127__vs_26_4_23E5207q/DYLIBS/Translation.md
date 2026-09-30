## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-355.5.2.0.0
-  __TEXT.__text: 0x4fe18
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x53e8
-  __TEXT.__const: 0xa78
-  __TEXT.__cstring: 0x304e
-  __TEXT.__oslogstring: 0x4aa6
-  __TEXT.__gcc_except_tab: 0xb50
+365.1.1.2.0
+  __TEXT.__text: 0x5b434
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__objc_methlist: 0x5748
+  __TEXT.__const: 0xf88
+  __TEXT.__cstring: 0x3064
+  __TEXT.__oslogstring: 0x4a66
+  __TEXT.__gcc_except_tab: 0xb70
   __TEXT.__ustring: 0x90
-  __TEXT.__constg_swiftt: 0x26c
-  __TEXT.__swift5_typeref: 0x3f9
-  __TEXT.__swift5_reflstr: 0x242
-  __TEXT.__swift5_fieldmd: 0x230
-  __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_capture: 0x174
-  __TEXT.__swift_as_entry: 0x44
-  __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x18e8
-  __TEXT.__eh_frame: 0x7a8
-  __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methname: 0xb339
-  __TEXT.__objc_methtype: 0x1c58
-  __TEXT.__objc_stubs: 0x65a0
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x1cb8
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__swift5_typeref: 0x627
+  __TEXT.__swift5_capture: 0x19c
+  __TEXT.__constg_swiftt: 0x3e4
+  __TEXT.__swift5_reflstr: 0x3da
+  __TEXT.__swift5_fieldmd: 0x3a0
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x7c
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__swift_as_entry: 0x4c
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__unwind_info: 0x1c38
+  __TEXT.__eh_frame: 0x8d0
+  __TEXT.__objc_classname: 0xc96
+  __TEXT.__objc_methname: 0xbd5d
+  __TEXT.__objc_methtype: 0x1efe
+  __TEXT.__objc_stubs: 0x6bc0
+  __DATA_CONST.__got: 0x568
+  __DATA_CONST.__const: 0x1df8
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24d0
+  __DATA_CONST.__objc_selrefs: 0x2670
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x268
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__const: 0xce8
-  __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0xaa70
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_arraydata: 0x150
+  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__const: 0x1000
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0xb310
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x11f0
-  __AUTH.__data: 0x480
-  __DATA.__objc_ivar: 0x7e4
-  __DATA.__data: 0xa30
-  __DATA.__bss: 0xa00
-  __DATA.__common: 0x48
+  __AUTH.__objc_data: 0x1380
+  __AUTH.__data: 0x6b0
+  __DATA.__objc_ivar: 0x834
+  __DATA.__data: 0xbc0
+  __DATA.__bss: 0x1080
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 96533A03-3438-30E9-BC62-1A2CC460763B
-  Functions: 2504
-  Symbols:   7249
-  CStrings:  3498
+  UUID: E474C0AE-3230-3360-82BA-82818EB4C0C7
+  Functions: 2739
+  Symbols:   7640
+  CStrings:  3650
 
Symbols:
+ -[NSLocale(LTLocaleIdentifier) _lt_displayNameForContext:inTargetLocale:alongsideLocales:]
+ -[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:]
+ -[NSLocale(LTLocaleIdentifier) _lt_isTraditionalCantonese]
+ -[_LTAlignment initWithIdentifier:sourceRange:targetRange:targetText:shouldTranslate:]
+ -[_LTLanguageAvailability _installationStatusWithCompletion:]
+ -[_LTLanguageAvailability _supportedLocaleListWithCompletion:]
+ -[_LTLanguageAvailability currentLanguageStatusSnapshotWithLocaleList:completion:]
+ -[_LTLanguageAvailability initWithPreferredStrategy:]
+ -[_LTLanguageAvailability localeProviderSupportedLocaleListWithCompletion:]
+ -[_LTLanguageAvailability preferredStrategy]
+ -[_LTLanguageListHelper .cxx_destruct]
+ -[_LTLanguageListHelper displayNameForLocale:context:inTargetLocale:]
+ -[_LTLanguageListHelper initWithLocaleList:]
+ -[_LTLanguageListHelper localeList]
+ -[_LTLanguageStatus engineType]
+ -[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:]
+ -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:].cold.1
+ -[_LTLanguageStatusMulticaster _multicastObservations:taskHint:engineType:progress:]
+ -[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]
+ -[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]
+ -[_LTLanguageStatusMulticaster languageStatusChangedForTaskHint:engineType:progress:observations:]
+ -[_LTLanguageStatusObservation initWithLocale:progress:downloadSize:status:sources:rank:]
+ -[_LTLanguageStatusObservation sources]
+ -[_LTLanguageStatusSnapshot .cxx_destruct]
+ -[_LTLanguageStatusSnapshot _setInitialSupportedStatus]
+ -[_LTLanguageStatusSnapshot _statusForLocale:withEngine:]
+ -[_LTLanguageStatusSnapshot _statusForPair:withEngine:]
+ -[_LTLanguageStatusSnapshot initWithLocaleList:]
+ -[_LTLanguageStatusSnapshot setStatus:forLocale:withEngine:]
+ -[_LTLanguageStatusSnapshot statusFromSingleEngineForPair:]
+ -[_LTLanguageVariantFilter .cxx_destruct]
+ -[_LTLanguageVariantFilter _uniqueSupportedLanguages]
+ -[_LTLanguageVariantFilter delegate]
+ -[_LTLanguageVariantFilter initWithSupportedLocales:]
+ -[_LTLanguageVariantFilter keyboardsForFilter:]
+ -[_LTLanguageVariantFilter preferredLanguagesForFilter:]
+ -[_LTLanguageVariantFilter recommendedLocales]
+ -[_LTLanguageVariantFilter requiredLocalesForFilter:]
+ -[_LTLanguageVariantFilter setDelegate:]
+ -[_LTLanguageVariantFilter supportedLocales]
+ -[_LTLocalePair initWithSourceIdentifier:targetIdentifier:]
+ -[_LTMultiParagraphTranslationRequest _addAlignmentAttributesToResult:requestIdentifier:]
+ -[_LTMultiParagraphTranslationRequest _alignmentAttributeKeyFromRequestIdentifier:alignmentIdentifier:]
+ -[_LTMultiParagraphTranslationRequest _generateParagraphRequests].cold.1
+ -[_LTMultiParagraphTranslationRequest _getStoredAttributesForRequestIdentifier:alignmentIdentifier:]
+ -[_LTMultiParagraphTranslationRequest _initWithText:attributedText:localePair:completionHandler:]
+ -[_LTMultiParagraphTranslationRequest _saveAttributes:forRequestUniqueID:alignmentIdentifier:]
+ -[_LTMultiParagraphTranslationRequest attributedText]
+ -[_LTMultiParagraphTranslationRequest initWithAttributedString:localePair:completionHandler:]
+ -[_LTParagraphTranslationRequest attributedText]
+ -[_LTParagraphTranslationRequest setAttributedText:]
+ -[_LTSpeechRecognitionResult detailedModelVersion]
+ -[_LTSpeechRecognitionResult setDetailedModelVersion:]
+ -[_LTSupportedLocaleList .cxx_destruct]
+ -[_LTSupportedLocaleList _allLocalePairsForLocales:]
+ -[_LTSupportedLocaleList allSupportedPairs]
+ -[_LTSupportedLocaleList copyWithZone:]
+ -[_LTSupportedLocaleList localePairsForStrategy:]
+ -[_LTSupportedLocaleList setLocales:forStrategy:]
+ -[_LTSupportedLocaleList setSupportedPairs:forStrategy:]
+ -[_LTSupportedLocaleList supportsLocalePair:forStrategy:]
+ -[_LTTextInput containsAlignment]
+ -[_LTTextInput initWithSourceAttributedText:clientIdentifier:]
+ -[_LTTextInput sourceAttributedText]
+ -[_LTTextResult initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:]
+ -[_LTTextResult sourceAttributedText]
+ -[_LTTextResult targetAttributedText]
+ -[_LTTextSession initWithSourceLocale:targetLocale:preferredStrategy:]
+ -[_LTTextSession initWithSourceLocale:targetLocale:preferredStrategy:isHeadless:]
+ -[_LTTextSession onDeviceEngineType]
+ -[_LTTextSession preferredStrategy]
+ -[_LTTextSession translateAttributedString:completionHandler:]
+ -[_LTTranslationContext onDeviceEngineType]
+ -[_LTTranslationContext setOnDeviceEngineType:]
+ -[_LTTranslationRequest allowsAIInference]
+ -[_LTTranslationRequest onDeviceEngineType]
+ -[_LTTranslationRequest setAllowsAIInference:]
+ -[_LTTranslationRequest setOnDeviceEngineType:]
+ GCC_except_table129
+ GCC_except_table14
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table50
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table70
+ GCC_except_table73
+ _OBJC_CLASS_$__LTLanguageListHelper
+ _OBJC_CLASS_$__LTLanguageStatusSnapshot
+ _OBJC_CLASS_$__LTLanguageVariantFilter
+ _OBJC_CLASS_$__LTSupportedLocaleList
+ _OBJC_IVAR_$__LTLanguageAvailability._cachedSupportedLocaleList
+ _OBJC_IVAR_$__LTLanguageAvailability._preferredStrategy
+ _OBJC_IVAR_$__LTLanguageAvailability._supportedLocaleListCompletionHandler
+ _OBJC_IVAR_$__LTLanguageListHelper._localeList
+ _OBJC_IVAR_$__LTLanguageStatus._engineType
+ _OBJC_IVAR_$__LTLanguageStatusObservation._sources
+ _OBJC_IVAR_$__LTLanguageStatusSnapshot._aiLocaleStatus
+ _OBJC_IVAR_$__LTLanguageStatusSnapshot._supportedLocaleList
+ _OBJC_IVAR_$__LTLanguageStatusSnapshot._traditionalLocaleStatus
+ _OBJC_IVAR_$__LTLanguageVariantFilter._delegate
+ _OBJC_IVAR_$__LTLanguageVariantFilter._supportedLocales
+ _OBJC_IVAR_$__LTMultiParagraphTranslationRequest._attributedText
+ _OBJC_IVAR_$__LTMultiParagraphTranslationRequest._savedAttributes
+ _OBJC_IVAR_$__LTParagraphTranslationRequest._attributedText
+ _OBJC_IVAR_$__LTSpeechRecognitionResult._detailedModelVersion
+ _OBJC_IVAR_$__LTSupportedLocaleList._aiSupportedPairs
+ _OBJC_IVAR_$__LTSupportedLocaleList._legacySupportedPairs
+ _OBJC_IVAR_$__LTTextInput._sourceAttributedText
+ _OBJC_IVAR_$__LTTextResult._sourceAttributedText
+ _OBJC_IVAR_$__LTTextResult._targetAttributedText
+ _OBJC_IVAR_$__LTTranslationContext._onDeviceEngineType
+ _OBJC_IVAR_$__LTTranslationRequest._allowsAIInference
+ _OBJC_IVAR_$__LTTranslationRequest._onDeviceEngineType
+ _OBJC_METACLASS_$__LTLanguageListHelper
+ _OBJC_METACLASS_$__LTLanguageStatusSnapshot
+ _OBJC_METACLASS_$__LTLanguageVariantFilter
+ _OBJC_METACLASS_$__LTSupportedLocaleList
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __DATA__TtC11Translation15_LTASTextResult
+ __DATA__TtC11Translation17_AttributeManager
+ __IVARS__TtC11Translation15_LTASTextResult
+ __IVARS__TtC11Translation17_AttributeManager
+ __LTDefaultStrategyForCurrentHostApp
+ __LTPreserveGenmojiAttributeKey
+ __METACLASS_DATA__TtC11Translation15_LTASTextResult
+ __METACLASS_DATA__TtC11Translation17_AttributeManager
+ __OBJC_$_INSTANCE_METHODS__LTLanguageListHelper
+ __OBJC_$_INSTANCE_METHODS__LTLanguageStatusSnapshot
+ __OBJC_$_INSTANCE_METHODS__LTLanguageVariantFilter
+ __OBJC_$_INSTANCE_METHODS__LTSupportedLocaleList
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageListHelper
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageStatusSnapshot
+ __OBJC_$_INSTANCE_VARIABLES__LTLanguageVariantFilter
+ __OBJC_$_INSTANCE_VARIABLES__LTSupportedLocaleList
+ __OBJC_$_PROP_LIST__LTLanguageListHelper
+ __OBJC_$_PROP_LIST__LTLanguageVariantFilter
+ __OBJC_$_PROP_LIST__LTSupportedLocaleList
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__LTLanguageVariantFilterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__LTLanguageVariantFilterDelegate
+ __OBJC_$_PROTOCOL_REFS__LTLanguageVariantFilterDelegate
+ __OBJC_CLASS_PROTOCOLS_$__LTLanguageVariantFilter
+ __OBJC_CLASS_PROTOCOLS_$__LTSupportedLocaleList
+ __OBJC_CLASS_RO_$__LTLanguageListHelper
+ __OBJC_CLASS_RO_$__LTLanguageStatusSnapshot
+ __OBJC_CLASS_RO_$__LTLanguageVariantFilter
+ __OBJC_CLASS_RO_$__LTSupportedLocaleList
+ __OBJC_LABEL_PROTOCOL_$__LTLanguageVariantFilterDelegate
+ __OBJC_METACLASS_RO_$__LTLanguageListHelper
+ __OBJC_METACLASS_RO_$__LTLanguageStatusSnapshot
+ __OBJC_METACLASS_RO_$__LTLanguageVariantFilter
+ __OBJC_METACLASS_RO_$__LTSupportedLocaleList
+ __OBJC_PROTOCOL_$__LTLanguageVariantFilterDelegate
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke.21
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke.cold.1
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_2
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_3
+ ___104-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke_3.cold.1
+ ___110-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
+ ___119-[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:]_block_invoke
+ ___46-[_LTLanguageVariantFilter recommendedLocales]_block_invoke
+ ___46-[_LTLanguageVariantFilter recommendedLocales]_block_invoke_2
+ ___46-[_LTLanguageVariantFilter recommendedLocales]_block_invoke_3
+ ___46-[_LTLanguageVariantFilter recommendedLocales]_block_invoke_4
+ ___53-[_LTLanguageAvailability initWithPreferredStrategy:]_block_invoke
+ ___53-[_LTLanguageAvailability initWithPreferredStrategy:]_block_invoke.2
+ ___53-[_LTLanguageAvailability initWithPreferredStrategy:]_block_invoke.cold.1
+ ___53-[_LTLanguageVariantFilter _uniqueSupportedLanguages]_block_invoke
+ ___53-[_LTLanguageVariantFilter requiredLocalesForFilter:]_block_invoke
+ ___57-[_LTSupportedLocaleList supportsLocalePair:forStrategy:]_block_invoke
+ ___61-[_LTLanguageAvailability _installationStatusWithCompletion:]_block_invoke
+ ___61-[_LTLanguageAvailability _installationStatusWithCompletion:]_block_invoke_2
+ ___61-[_LTLanguageAvailability _installationStatusWithCompletion:]_block_invoke_3
+ ___61-[_LTLanguageAvailability _installationStatusWithCompletion:]_block_invoke_4
+ ___62-[_LTLanguageAvailability _supportedLocaleListWithCompletion:]_block_invoke
+ ___62-[_LTLanguageAvailability _supportedLocaleListWithCompletion:]_block_invoke_2
+ ___62-[_LTLanguageAvailability _supportedLocaleListWithCompletion:]_block_invoke_3
+ ___62-[_LTTextSession translateAttributedString:completionHandler:]_block_invoke
+ ___65-[_LTMultiParagraphTranslationRequest _generateParagraphRequests]_block_invoke.16
+ ___65-[_LTMultiParagraphTranslationRequest _generateParagraphRequests]_block_invoke.22
+ ___65-[_LTMultiParagraphTranslationRequest _generateParagraphRequests]_block_invoke_2.17
+ ___75-[_LTLanguageAvailability localeProviderSupportedLocaleListWithCompletion:]_block_invoke
+ ___75-[_LTLanguageAvailability localeProviderSupportedLocaleListWithCompletion:]_block_invoke_2
+ ___75-[_LTLanguageAvailability localeProviderSupportedLocaleListWithCompletion:]_block_invoke_3
+ ___75-[_LTLanguageAvailability localeProviderSupportedLocaleListWithCompletion:]_block_invoke_4
+ ___82-[_LTLanguageAvailability currentLanguageStatusSnapshotWithLocaleList:completion:]_block_invoke
+ ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke
+ ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke.2
+ ___83-[_LTLanguageStatus initWithTaskHint:engineType:useDedicatedMachPort:observations:]_block_invoke_2
+ ___84-[_LTLanguageStatusMulticaster _multicastObservations:taskHint:engineType:progress:]_block_invoke
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.243
+ ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.243.cold.1
+ ___93-[NSLocale(LTLocaleIdentifier) _lt_displaySubnameForContext:inTargetLocale:alongsideLocales:]_block_invoke
+ ___Block_byref_object_copy_.14
+ ___Block_byref_object_dispose_.15
+ ___block_descriptor_32_e48_"NSLocale"16?0"_LTLanguageStatusObservation"8l
+ ___block_descriptor_40_e8_32s_e23_B16?0"_LTLocalePair"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e32_v16?0"_LTSupportedLocaleList"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8lr40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e32_v16?0"_LTSupportedLocaleList"8lw32l8w40l8
+ ___block_descriptor_56_e8_32bs40bs48w_e32_v16?0"_LTSupportedLocaleList"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32bs40w48w_e35_v16?0"_LTLanguageStatusSnapshot"8lw40l8w48l8s32l8
+ ___block_descriptor_64_e8_32bs40r48w56w_e32_v16?0"_LTSupportedLocaleList"8lw48l8r40l8w56l8s32l8
+ ___block_descriptor_64_e8_32s40r48r56r_e17_v16?0"NSArray"8lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e35_v16?0"_LTLanguageStatusSnapshot"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e35_v32?0"NSAttributedString"8Q16^B24lw56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_65_e8_32s40w_e46_v24?0"<_LTTextTranslationService>"8?<v?>16lw40l8s32l8
+ ___block_descriptor_65_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_66_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_73_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_81_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_literal_global.43
+ ___block_literal_global.69
+ ___swift_get_extra_inhabitant_index.45Tm
+ ___swift_memcpy0_1
+ ___swift_memcpy16_8
+ ___swift_store_extra_inhabitant_index.46Tm
+ _associated conformance 10Foundation15AttributeScopesO11TranslationE0D10AttributesV04SkipdB0OAA19AttributedStringKeyAD5ValueAaIP_SH
+ _associated conformance 10Foundation15AttributeScopesO11TranslationE0D10AttributesVAA0B5ScopeAdA30DecodingConfigurationProviding
+ _associated conformance 10Foundation15AttributeScopesO11TranslationE0D10AttributesVAA0B5ScopeAdA30EncodingConfigurationProviding
+ _associated conformance 11Translation0A7SessionC8StrategyV12InternalTypeOSHAASQ
+ _associated conformance So21NSAttributedStringKeyaSHSCSQ
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So21NSAttributedStringKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.11
+ _block_copy_helper.14
+ _block_copy_helper.79
+ _block_copy_helper.85
+ _block_copy_helper.91
+ _block_descriptor.13
+ _block_descriptor.16
+ _block_descriptor.81
+ _block_descriptor.87
+ _block_descriptor.93
+ _block_destroy_helper.12
+ _block_destroy_helper.15
+ _block_destroy_helper.80
+ _block_destroy_helper.86
+ _block_destroy_helper.92
+ _bzero
+ _dyld_program_sdk_at_least
+ _kLTPreferAIAdapterOverLegacyModelsPreferenceKey
+ _memmove
+ _objc_msgSend$_allLocalePairsForLocales:
+ _objc_msgSend$_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:
+ _objc_msgSend$_initWithText:attributedText:localePair:completionHandler:
+ _objc_msgSend$_installationStatusWithCompletion:
+ _objc_msgSend$_lt_displayNameForContext:inTargetLocale:alongsideLocales:
+ _objc_msgSend$_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:
+ _objc_msgSend$_lt_isTraditionalCantonese
+ _objc_msgSend$_multicastObservations:taskHint:engineType:progress:
+ _objc_msgSend$_reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:
+ _objc_msgSend$_setInitialSupportedStatus
+ _objc_msgSend$_startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:
+ _objc_msgSend$_statusForLocale:withEngine:
+ _objc_msgSend$_statusForPair:withEngine:
+ _objc_msgSend$_supportedLocaleListWithCompletion:
+ _objc_msgSend$_uniqueSupportedLanguages
+ _objc_msgSend$allSupportedPairs
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$cancel:
+ _objc_msgSend$containsAlignment
+ _objc_msgSend$currentLanguageStatusSnapshotWithLocaleList:completion:
+ _objc_msgSend$engineType
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithAttributedString:localePair:completionHandler:
+ _objc_msgSend$initWithLocale:progress:downloadSize:status:sources:rank:
+ _objc_msgSend$initWithLocaleList:
+ _objc_msgSend$initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:
+ _objc_msgSend$initWithPreferredStrategy:
+ _objc_msgSend$initWithSourceAttributedText:clientIdentifier:
+ _objc_msgSend$initWithSourceLocale:targetLocale:preferredStrategy:isHeadless:
+ _objc_msgSend$initWithTaskHint:engineType:useDedicatedMachPort:observations:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$keyboardsForFilter:
+ _objc_msgSend$launchAppWithCompletionHandler:
+ _objc_msgSend$localeList
+ _objc_msgSend$localePairsForStrategy:
+ _objc_msgSend$localeProviderSupportedLocaleListWithCompletion:
+ _objc_msgSend$lt_filterUsingBlock:
+ _objc_msgSend$onDeviceEngineType
+ _objc_msgSend$preferredLanguagesForFilter:
+ _objc_msgSend$preferredStrategy
+ _objc_msgSend$prepareDownloadsWithCompletion:
+ _objc_msgSend$requiredLocalesForFilter:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setAttributes:range:
+ _objc_msgSend$setLocales:forStrategy:
+ _objc_msgSend$setOnDeviceEngineType:
+ _objc_msgSend$setStatus:forLocale:withEngine:
+ _objc_msgSend$setSupportedPairs:forStrategy:
+ _objc_msgSend$sourceAttributedText
+ _objc_msgSend$sources
+ _objc_msgSend$startLanguageStatusChangeObservation:taskHint:engineType:completion:
+ _objc_msgSend$statusForSourceSample:toLanguage:completion:
+ _objc_msgSend$statusFromSingleEngineForPair:
+ _objc_msgSend$supportedLanguagesWithCompletion:
+ _objc_msgSend$supportsLocalePair:forStrategy:
+ _objc_msgSend$targetAttributedText
+ _objc_msgSend$translateAttributedString:completionHandler:
+ _objc_msgSend$translateString:completionHandler:
+ _objc_msgSend$unionSet:
+ _objc_msgSend$userInfo
+ _objectdestroy.77Tm
+ _swift_endAccess
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _symbolic $s10Foundation19AttributedStringKeyP
+ _symbolic $s10Foundation30DecodingConfigurationProvidingP
+ _symbolic $s10Foundation30EncodingConfigurationProvidingP
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SDySSSiG
+ _symbolic SDySi_____G 10Foundation18AttributeContainerV
+ _symbolic SDy_____ypG_____Spy_____GIggyy_ So21NSAttributedStringKeya So8_NSRangeV 10ObjectiveC8ObjCBoolV
+ _symbolic Si______t 10Foundation18AttributeContainerV
+ _symbolic Sny_____G 10Foundation16AttributedStringV5IndexV
+ _symbolic Sny_____GSg 10Foundation16AttributedStringV5IndexV
+ _symbolic So13_LTLocalePairC
+ _symbolic So8NSStringC
+ _symbolic _____ 10Foundation15AttributeScopesO
+ _symbolic _____ 10Foundation15AttributeScopesO11TranslationE0D10AttributesV
+ _symbolic _____ 10Foundation15AttributeScopesO11TranslationE0D10AttributesV04SkipdB0O
+ _symbolic _____ 10Foundation16AttributedStringV
+ _symbolic _____ 10Foundation34AttributeScopeCodableConfigurationV
+ _symbolic _____ 10Foundation6LocaleV
+ _symbolic _____ 11Translation0A7SessionC8StrategyV
+ _symbolic _____ 11Translation0A7SessionC8StrategyV12InternalTypeO
+ _symbolic _____ 11Translation15_LTASTextResultC
+ _symbolic _____ 11Translation17_AttributeManagerC
+ _symbolic _____ So21NSAttributedStringKeya
+ _symbolic _____ So8_NSRangeV
+ _symbolic _____Sg 10Foundation16AttributedStringV
+ _symbolic _____Sg 10Foundation18AttributeContainerV
+ _symbolic _____Sg_ABt 10Foundation16AttributedStringV
+ _symbolic ______SDySSSiGt So21NSAttributedStringKeya
+ _symbolic _____ySSSiG s18_DictionaryStorageC
+ _symbolic _____ySi_____G s18_DictionaryStorageC 10Foundation18AttributeContainerV
+ _symbolic _____y_____G s16IndexingIteratorV 10Foundation16AttributedStringV4RunsV
+ _symbolic _____y_____SDySSSiGG s18_DictionaryStorageC So21NSAttributedStringKeya
+ _symbolic _____y______SDySSSiGtG s23_ContiguousArrayStorageC So21NSAttributedStringKeya
+ _symbolic _____y_____ypG s18_DictionaryStorageC So21NSAttributedStringKeya
+ _type_layout_string 10Foundation15AttributeScopesO11TranslationE0D10AttributesV
+ _type_layout_string 11Translation0A7SessionC8StrategyV
+ _type_layout_string So21NSAttributedStringKeya
+ _type_layout_string So8_NSRangeV
- -[_LTLanguageAvailability _installedLocalesWithCompletion:]
- -[_LTLanguageAvailability currentlyInstalledLocalesWithCompletion:]
- -[_LTLanguageAvailability localeProviderSupportedLocalePairsWithCompletion:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:useDedicatedMachPort:].cold.1
- -[_LTLanguageStatusMulticaster _multicastObservations:taskHint:progress:]
- -[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]
- -[_LTLanguageStatusMulticaster languageStatusChangedForTaskHint:progress:observations:]
- -[_LTTextSession initWithSourceLocale:targetLocale:]
- -[_LTTextSession initWithSourceLocale:targetLocale:isHeadless:]
- -[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:].cold.2
- -[_LTTextTranslationRequest preserveGenmoji]
- -[_LTTextTranslationRequest setPreserveGenmoji:]
- GCC_except_table127
- GCC_except_table17
- GCC_except_table24
- GCC_except_table57
- GCC_except_table59
- GCC_except_table62
- GCC_except_table69
- _OBJC_IVAR_$__LTLanguageAvailability._cachedSupportedLocalePairs
- _OBJC_IVAR_$__LTLanguageAvailability._supportedLocalePairsCompletionHandler
- _OBJC_IVAR_$__LTTextTranslationRequest._preserveGenmoji
- __LTTranslationAdaptiveImageAttributeKey
- __OBJC_$_CLASS_PROP_LIST_NSLocale_$_LTLocaleIdentifier
- __OBJC_$_PROP_LIST_NSLocale_$_LTLocaleIdentifier
- ___108-[_LTLanguageStatusMulticaster _reconnectIfStreamingWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke
- ___31-[_LTLanguageAvailability init]_block_invoke
- ___31-[_LTLanguageAvailability init]_block_invoke.2
- ___31-[_LTLanguageAvailability init]_block_invoke.cold.1
- ___59-[_LTLanguageAvailability _installedLocalesWithCompletion:]_block_invoke
- ___59-[_LTLanguageAvailability _installedLocalesWithCompletion:]_block_invoke_2
- ___59-[_LTLanguageAvailability _installedLocalesWithCompletion:]_block_invoke_3
- ___63-[_LTLanguageAvailability _supportedLocalePairsWithCompletion:]_block_invoke_2
- ___63-[_LTLanguageAvailability _supportedLocalePairsWithCompletion:]_block_invoke_3
- ___65-[_LTMultiParagraphTranslationRequest _generateParagraphRequests]_block_invoke.9
- ___65-[_LTMultiParagraphTranslationRequest _generateParagraphRequests]_block_invoke_3
- ___67-[_LTLanguageAvailability currentlyInstalledLocalesWithCompletion:]_block_invoke
- ___72-[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:]_block_invoke
- ___72-[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:]_block_invoke.1
- ___72-[_LTLanguageStatus initWithTaskHint:useDedicatedMachPort:observations:]_block_invoke_2
- ___73-[_LTLanguageStatusMulticaster _multicastObservations:taskHint:progress:]_block_invoke
- ___76-[_LTLanguageAvailability localeProviderSupportedLocalePairsWithCompletion:]_block_invoke
- ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.231
- ___88-[_LTTextTranslationRequest _replaceAdaptiveImageGlyphsIfNeededForText:requestUniqueID:]_block_invoke.231.cold.1
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke.21
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke.cold.1
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke_2
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke_3
- ___93-[_LTLanguageStatusMulticaster _startWithConnectionIdentifier:taskHint:useDedicatedMachPort:]_block_invoke_3.cold.1
- ___97-[_LTLanguageAvailability _checkStatusWithSourceLanguage:targetLanguage:sourceSample:completion:]_block_invoke.13
- ___97-[_LTLanguageAvailability _checkStatusWithSourceLanguage:targetLanguage:sourceSample:completion:]_block_invoke_2.11
- ___97-[_LTLanguageAvailability _checkStatusWithSourceLanguage:targetLanguage:sourceSample:completion:]_block_invoke_2.14
- ___97-[_LTLanguageAvailability _checkStatusWithSourceLanguage:targetLanguage:sourceSample:completion:]_block_invoke_3
- ___99-[_LTLanguageStatusMulticaster _closeConnectionForced:forIdentifier:taskHint:useDedicatedMachPort:]_block_invoke
- ___Block_byref_object_copy_.17
- ___Block_byref_object_dispose_.18
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_48_e8_32w40w_e17_v16?0"NSArray"8lw32l8w40l8
- ___block_descriptor_56_e8_32bs40w48w_e29_v24?0"NSArray"8"NSArray"16lw40l8w48l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e35_v32?0"NSAttributedString"8Q16^B24lw48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_57_e8_32s40w_e46_v24?0"<_LTTextTranslationService>"8?<v?>16lw40l8s32l8
- ___block_descriptor_57_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_58_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e29_v24?0"NSArray"8"NSArray"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
- ___block_descriptor_73_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___swift_get_extra_inhabitant_index.34Tm
- ___swift_memcpy32_8
- ___swift_store_extra_inhabitant_index.35Tm
- _block_copy_helper.12
- _block_copy_helper.62
- _block_copy_helper.68
- _block_copy_helper.74
- _block_descriptor.14
- _block_descriptor.64
- _block_descriptor.70
- _block_descriptor.76
- _block_destroy_helper.13
- _block_destroy_helper.63
- _block_destroy_helper.69
- _block_destroy_helper.75
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_closeConnectionForced:forIdentifier:taskHint:useDedicatedMachPort:
- _objc_msgSend$_installedLocalesWithCompletion:
- _objc_msgSend$_multicastObservations:taskHint:progress:
- _objc_msgSend$_reconnectIfStreamingWithConnectionIdentifier:taskHint:useDedicatedMachPort:
- _objc_msgSend$_startWithConnectionIdentifier:taskHint:useDedicatedMachPort:
- _objc_msgSend$currentlyInstalledLocalesWithCompletion:
- _objc_msgSend$initWithSourceLocale:targetLocale:isHeadless:
- _objc_msgSend$localeProviderSupportedLocalePairsWithCompletion:
- _objc_msgSend$lt_displaySubnameForContext:inTargetLocale:
- _objc_msgSend$preserveGenmoji
- _objc_msgSend$startLanguageStatusChangeObservation:taskHint:completion:
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objectdestroy.60Tm
- _type_layout_string 11Translation0A7SessionC7RequestV
CStrings:
+ "%@:%@:%@"
+ "@\"<_LTLanguageVariantFilterDelegate>\""
+ "@\"NSArray\"24@0:8@\"_LTLanguageVariantFilter\"16"
+ "@\"NSLocale\"16@?0@\"_LTLanguageStatusObservation\"8"
+ "@\"_LTSupportedLocaleList\""
+ "@24@0:8q16"
+ "@44@0:8@16@24q32B40"
+ "@44@0:8q16q24B32@?36"
+ "@48@0:8@16@24@32@?40"
+ "@64@0:8@16d24Q32q40Q48q56"
+ "@68@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40@56B64"
+ "AI"
+ "AIInferencePrioritizedOverLegacyModels"
+ "AllEngines"
+ "App is linked before 26.4, so defaulting to low latency strategy"
+ "App is linked on or after 26.4, so defaulting to high fidelity strategy"
+ "B32@0:8@16q24"
+ "CANTONESE_TRADITIONAL_SUBTITLE"
+ "Finding default fallback for locale: %{private}@"
+ "Install status for validated language pairing (%{public}@): %{public}@"
+ "Q32@0:8@16q24"
+ "Skipping range (%zu, %zu) (No attributes)"
+ "Supported"
+ "T@\"<_LTLanguageVariantFilterDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",R,C,N,V_localeList"
+ "T@\"NSArray\",R,C,N,V_supportedLocales"
+ "T@\"NSAttributedString\",C,N,V_attributedText"
+ "T@\"NSAttributedString\",R,C,N,V_attributedText"
+ "T@\"NSAttributedString\",R,C,N,V_sourceAttributedText"
+ "T@\"NSAttributedString\",R,C,N,V_targetAttributedText"
+ "T@\"NSString\",&,N,V_detailedModelVersion"
+ "TB,N,V_allowsAIInference"
+ "TQ,R,N,V_sources"
+ "Tq,N,V_onDeviceEngineType"
+ "Tq,R,N,V_engineType"
+ "Tq,R,N,V_preferredStrategy"
+ "Traditional"
+ "Translation.DoNotTranslate"
+ "Translation.InternalSequence"
+ "Unsupported"
+ "_LTLanguageListHelper"
+ "_LTLanguageStatusSnapshot"
+ "_LTLanguageVariantFilter"
+ "_LTLanguageVariantFilterDelegate"
+ "_LTPreserveGenmoji"
+ "_LTSupportedLocaleList"
+ "_TtC11Translation15_LTASTextResult"
+ "_TtC11Translation17_AttributeManager"
+ "_aiLocaleStatus"
+ "_aiSupportedPairs"
+ "_allLocalePairsForLocales:"
+ "_allowsAIInference"
+ "_attributedText"
+ "_cachedSupportedLocaleList"
+ "_closeConnectionForced:forIdentifier:taskHint:engineType:useDedicatedMachPort:"
+ "_detailedModelVersion"
+ "_engineType"
+ "_initWithText:attributedText:localePair:completionHandler:"
+ "_installationStatusWithCompletion:"
+ "_legacySupportedPairs"
+ "_localeList"
+ "_lt_displayNameForContext:inTargetLocale:alongsideLocales:"
+ "_lt_displaySubnameForContext:inTargetLocale:alongsideLocales:"
+ "_lt_isTraditionalCantonese"
+ "_multicastObservations:taskHint:engineType:progress:"
+ "_onDeviceEngineType"
+ "_preferredStrategy"
+ "_reconnectIfStreamingWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:"
+ "_setInitialSupportedStatus"
+ "_sourceAttributedText"
+ "_sources"
+ "_startWithConnectionIdentifier:taskHint:engineType:useDedicatedMachPort:"
+ "_statusForLocale:withEngine:"
+ "_statusForPair:withEngine:"
+ "_storage"
+ "_supportedLocaleList"
+ "_supportedLocaleListCompletionHandler"
+ "_supportedLocaleListWithCompletion:"
+ "_supportedLocales"
+ "_targetAttributedText"
+ "_traditionalLocaleStatus"
+ "_uniqueSupportedLanguages"
+ "ai_adapter_inference"
+ "allSupportedPairs"
+ "allowsAIInference"
+ "arrayByAddingObjectsFromArray:"
+ "attributedText"
+ "containsAlignment"
+ "currentLanguageStatusSnapshotWithLocaleList:completion:"
+ "de_DE"
+ "detailedModelVersion"
+ "displayNameForLocale:context:inTargetLocale:"
+ "doNotTranslate"
+ "en_GB"
+ "engineType"
+ "es_MX"
+ "fr_FR"
+ "i"
+ "initWithArray:"
+ "initWithAttributedString:localePair:completionHandler:"
+ "initWithIdentifier:sourceRange:targetRange:targetText:shouldTranslate:"
+ "initWithLocale:progress:downloadSize:status:sources:rank:"
+ "initWithLocaleList:"
+ "initWithLocalePair:sourceAttributedText:targetAttributedText:clientIdentifier:"
+ "initWithPreferredStrategy:"
+ "initWithSourceAttributedText:clientIdentifier:"
+ "initWithSourceIdentifier:targetIdentifier:"
+ "initWithSourceLocale:targetLocale:preferredStrategy:"
+ "initWithSourceLocale:targetLocale:preferredStrategy:isHeadless:"
+ "initWithSupportedLocales:"
+ "initWithTaskHint:engineType:useDedicatedMachPort:observations:"
+ "intersectSet:"
+ "it_IT"
+ "keyboardsForFilter:"
+ "languageStatusChangedForTaskHint:engineType:progress:observations:"
+ "localeList"
+ "localePairsForStrategy:"
+ "localeProviderSupportedLocaleListWithCompletion:"
+ "no attributed string provided: constructing one from the plain string"
+ "onDeviceEngineType"
+ "preferredLanguagesForFilter:"
+ "preferredStrategy"
+ "pt_BR"
+ "pt_PT"
+ "recommendedLocales"
+ "requiredLocalesForFilter:"
+ "setAllowsAIInference:"
+ "setAttributedText:"
+ "setAttributes:range:"
+ "setDetailedModelVersion:"
+ "setLocales:forStrategy:"
+ "setOnDeviceEngineType:"
+ "setStatus:forLocale:withEngine:"
+ "setSupportedPairs:forStrategy:"
+ "sourceAttributedText"
+ "sources"
+ "startLanguageStatusChangeObservation:taskHint:engineType:completion:"
+ "statusFromSingleEngineForPair:"
+ "supportsLocalePair:forStrategy:"
+ "targetAttributedText"
+ "translateAttributedString:completionHandler:"
+ "unionSet:"
+ "v16@?0@\"_LTLanguageStatusSnapshot\"8"
+ "v16@?0@\"_LTSupportedLocaleList\"8"
+ "v24@0:8@?<v@?@\"_LTSupportedLocaleList\">16"
+ "v32@0:8@\"_LTSupportedLocaleList\"16@?<v@?@\"_LTLanguageStatusSnapshot\">24"
+ "v40@0:8Q16@24q32"
+ "v44@0:8@16q24q32B40"
+ "v44@0:8q16q24B32@\"NSArray\"36"
+ "v44@0:8q16q24B32@36"
+ "v48@0:8@\"NSUUID\"16q24q32@?<v@?@\"NSError\">40"
+ "v48@0:8@16q24q32@?40"
+ "v48@0:8B16@20q28q36B44"
+ "\x82"
- "%@:%@"
- "Both source ('%{public}@') and target ('%{public}@') languages are at least downloading, saying this pairing is downloading"
- "Both source ('%{public}@') and target ('%{public}@') languages are installed"
- "CTAdaptiveImageProvider"
- "Either source ('%{public}@') and/or target ('%{public}@') language isn't installed or downloading, saying this pairing is supported but not installed or downloading"
- "Not attempting to replace Genmoji since client didn't request this"
- "TB,N,V_preserveGenmoji"
- "_cachedSupportedLocalePairs"
- "_closeConnectionForced:forIdentifier:taskHint:useDedicatedMachPort:"
- "_installedLocalesWithCompletion:"
- "_multicastObservations:taskHint:progress:"
- "_preserveGenmoji"
- "_reconnectIfStreamingWithConnectionIdentifier:taskHint:useDedicatedMachPort:"
- "_startWithConnectionIdentifier:taskHint:useDedicatedMachPort:"
- "_supportedLocalePairsCompletionHandler"
- "currentlyInstalledLocalesWithCompletion:"
- "initWithSourceLocale:targetLocale:isHeadless:"
- "languageStatusChangedForTaskHint:progress:observations:"
- "localeProviderSupportedLocalePairsWithCompletion:"
- "preserveGenmoji"
- "r"
- "setPreserveGenmoji:"
- "startLanguageStatusChangeObservation:taskHint:completion:"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
- "v24@?0@\"NSArray\"8@\"NSArray\"16"
- "v36@0:8q16B24@\"NSArray\"28"
- "v36@0:8q16B24@28"
- "v40@0:8@\"NSUUID\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8B16@20q28B36"

```
