## SafariShared

> `/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0x1c005c
-  __TEXT.__objc_methlist: 0x12efc
-  __TEXT.__const: 0x945c8
-  __TEXT.__gcc_except_tab: 0x1cc98
-  __TEXT.__cstring: 0x1a747
+625.1.24.11.2
+  __TEXT.__text: 0x1c5e60
+  __TEXT.__objc_methlist: 0x12f4c
+  __TEXT.__const: 0x96bb8
+  __TEXT.__gcc_except_tab: 0x1cc4c
+  __TEXT.__cstring: 0x1a867
   __TEXT.__ustring: 0xcb78
-  __TEXT.__oslogstring: 0x10c82
+  __TEXT.__oslogstring: 0x10da2
   __TEXT.__dlopen_cstrs: 0xe9
-  __TEXT.__swift5_typeref: 0xb9c
-  __TEXT.__swift5_fieldmd: 0x6c0
-  __TEXT.__constg_swiftt: 0x738
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x58c
+  __TEXT.__swift5_typeref: 0xc36
+  __TEXT.__swift5_fieldmd: 0x75c
+  __TEXT.__constg_swiftt: 0x7ec
+  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__swift5_reflstr: 0x59c
   __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_proto: 0x200
-  __TEXT.__swift5_types: 0x8c
-  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_proto: 0x218
+  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__unwind_info: 0xba40
-  __TEXT.__eh_frame: 0xe00
+  __TEXT.__unwind_info: 0xbae0
+  __TEXT.__eh_frame: 0xf60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14c58
+  __DATA_CONST.__const: 0x14c50
   __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa448
+  __DATA_CONST.__objc_selrefs: 0xa498
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x850
   __DATA_CONST.__objc_arraydata: 0x9f0
-  __DATA_CONST.__got: 0x18d8
-  __AUTH_CONST.__const: 0x3d90
-  __AUTH_CONST.__cfstring: 0x16d20
-  __AUTH_CONST.__objc_const: 0x22490
+  __DATA_CONST.__got: 0x1930
+  __AUTH_CONST.__const: 0x3ed0
+  __AUTH_CONST.__cfstring: 0x16da0
+  __AUTH_CONST.__objc_const: 0x224c8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x5a0
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1d90
+  __AUTH_CONST.__auth_got: 0x1e88
   __AUTH.__objc_data: 0x2eb8
   __AUTH.__data: 0x350
-  __DATA.__objc_ivar: 0x15b0
-  __DATA.__data: 0x3c20
-  __DATA.__bss: 0x2fe0
+  __DATA.__objc_ivar: 0x15b4
+  __DATA.__data: 0x3d80
+  __DATA.__bss: 0x32e0
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x3e70
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10469
-  Symbols:   20506
-  CStrings:  4807
+  Functions: 10535
+  Symbols:   20537
+  CStrings:  4819
 
Symbols:
+ +[WBSHistoryController existingSharedHistoryControllerIfExists]
+ -[NSExtension(SafariSharedExtras) safari_sourceDisplayName]
+ -[WBSFormControlMetadata looksLikeIMEI1Field]
+ -[WBSFormControlMetadata looksLikeIMEI2Field]
+ -[WBSFormControlMetadata looksLikeNALField]
+ -[WBSFormDataController canShowSavedAccountHistoryItemInTabWithID:currentURL:]
+ -[WBSFormDataController savedAccountFromMostRecentAutoFillEventOfURL:]
+ -[WBSParsecDFeedbackDispatcher postFeedbackForSearchEngineChoiceForQueryID:endpoint:]
+ GCC_except_table258
+ GCC_except_table263
+ GCC_except_table312
+ GCC_except_table314
+ OBJC_IVAR_$_WBSHistoryItem._lastVisitLock
+ _OBJC_CLASS_$_SFEndNetworkSearchFeedback
+ _WBSDeviceIMEI1ClassificationToken
+ _WBSDeviceIMEI2ClassificationToken
+ _WBSDeviceNALClassificationToken
+ ___63+[WBSHistoryController existingSharedHistoryControllerIfExists]_block_invoke
+ ___70-[WBSFormDataController savedAccountFromMostRecentAutoFillEventOfURL:]_block_invoke
+ ___block_descriptor_40_ea8_32r_e36_v16?0"WBSSavedAccountMatchResult"8lr32l8
+ ___block_descriptor_48_ea8_32s40r_e42_"WBSHistoryVisit"16?0"WBSHistoryVisit"8ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40s48r_e13_v24?0^i8^v16ls32l8r48l8s40l8
+ ___block_descriptor_64_ea8_32s40r_e13_v24?0^i8^v16lr40l8s32l8
+ ___swift_memcpy33_8
+ ___swift_memcpy40_8
+ ___swift_memcpy48_8
+ ___unnamed_35
+ ___unnamed_57
+ _associated conformance 12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLV10CodingKeysOyx__GSHAASQ
+ _associated conformance 12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLV10CodingKeysOyx__Gs0P3KeyAAs23CustomStringConvertible
+ _associated conformance 12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLV10CodingKeysOyx__Gs0P3KeyAAs28CustomDebugStringConvertible
+ _get_enum_tag_for_layout_string 12SafariShared13WBSAgentToolsO16ForbiddenPatternO
+ _objc_msgSend$criteriaForExactFQDNPasswordMatchesOfURL:
+ _objc_msgSend$escapedPatternForString:
+ _objc_msgSend$existingSharedHistoryControllerIfExists
+ _objc_msgSend$initWithStartSearch:responseSize:statusCode:networkTimingData:
+ _objc_msgSend$isSavedAccountHistoryInAutoFillEnabled
+ _objc_msgSend$safari_localizedContainingAppDisplayName
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _swift_cvw_instantiateLayoutString
+ _swift_getTupleTypeMetadata2
+ _swift_retain_x19
+ _swift_unexpectedError
+ _symbolic SDySSSay_____GG 10SafariCore23WBSAnySendableEncodableV
+ _symbolic SDySS_____G 10SafariCore23WBSAnySendableEncodableV
+ _symbolic SS_Say_____Gt 10SafariCore23WBSAnySendableEncodableV
+ _symbolic SS______t 10SafariCore23WBSAnySendableEncodableV
+ _symbolic _____ 12SafariShared13WBSAgentToolsO16ForbiddenPatternO
+ _symbolic _____ 12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLV
+ _symbolic _____ 12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLV10CodingKeysO
+ _symbolic _____Sg 12SafariShared23WBSAgentControllerModelO
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySSSay_____GG s18_DictionaryStorageC 10SafariCore23WBSAnySendableEncodableV
+ _symbolic _____ySS_Say_____GtG s23_ContiguousArrayStorageC 10SafariCore23WBSAnySendableEncodableV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 10SafariCore23WBSAnySendableEncodableV
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 10SafariCore23WBSAnySendableEncodableV
+ _symbolic _____y_____G s11_SetStorageC s7UnicodeO15GeneralCategoryO
+ _symbolic _____y_____G s11_SetStorageC s7UnicodeO6ScalarV
+ _symbolic _____y_____G s16PartialRangeFromV SS5IndexV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s7UnicodeO15GeneralCategoryO
+ _type_layout_string 12SafariShared13WBSAgentToolsO16ForbiddenPatternO
+ _type_layout_string 29GenerativeFunctionsFoundation9GenerableRzl12SafariShared18WBSAgentControllerC21ImageMetricsRedaction33_BB0CD2D0C8036A089F40018934D354B9LLVyx_G
- -[WBSFormMetadataController formSubmissionURLStringForSearchTextField:inFrame:useStrictDetection:]
- -[WBSFormMetadataController visibleNonEmptyTextFieldsInForm:inFrame:]
- -[WBSRecentWebSearchesController _removeDuplicatedURLs]
- GCC_except_table250
- GCC_except_table251
- GCC_except_table264
- GCC_except_table266
- GCC_except_table273
- GCC_except_table280
- GCC_except_table282
- __ZL28WBSHistoryItemLastVisitQueue
- ___27-[WBSHistoryItem lastVisit]_block_invoke
- ___34-[WBSHistoryItem updateLastVisit:]_block_invoke
- ___55-[WBSRecentWebSearchesController _removeDuplicatedURLs]_block_invoke
- ___68-[WBSStartPageSectionManager setSectionsIdentifiers:enabledIndexes:]_block_invoke_2
- ___68-[WBSStartPageSectionManager setSectionsIdentifiers:enabledIndexes:]_block_invoke_3
- ___block_descriptor_32_e58_"WBSRecentWebSearchEntry"16?0"WBSRecentWebSearchEntry"8l
- ___block_descriptor_33_e49_"NSString"16?0"WBSStartPageSectionDescriptor"8l
- ___block_descriptor_56_ea8_32s40r48r_e13_v24?0^i8^v16ls32l8r40l8r48l8
- ___block_descriptor_64_ea8_32r40r_e13_v24?0^i8^v16lr32l8r40l8
- ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
- ___swift_memcpy64_8
- ___unnamed_31
- _objc_msgSend$_removeDuplicatedURLs
- _swift_retain_x28
- _symbolic SDySSSay_____GG 9PromptKit0A0V9ComponentV5ValueO
- _symbolic SS_Say_____Gt 9PromptKit0A0V9ComponentV5ValueO
- _symbolic Say_____G 9PromptKit0A0V9ComponentV5ValueO
- _symbolic _____ySSSay_____GG s18_DictionaryStorageC 9PromptKit0C0V9ComponentV5ValueO
- _symbolic _____ySS_Say_____GtG s23_ContiguousArrayStorageC 9PromptKit0D0V9ComponentV5ValueO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 9PromptKit0D0V9ComponentV5ValueO
CStrings:
+ "(?:\\??\\.[\\w$]+|(?<=[\\w$)\\].])\\[[^\\]]*\\])\\s*(?:(?:\\+|-|\\*\\*|\\*|\\/|%|\\^|<<|>>>|>>|\\|\\||&&|\\?\\?|\\||&)?=[^=]|\\+\\+|--)"
+ "(?:\\s*\\?\\.)?\\s*\\("
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.bxxFUU/Sources/SafariShared_iosmac/SafariShared/SafariShared/History/Service/WBSHistoryServiceURLCompletion.mm"
+ "22625.1.24.11.2"
+ "ControlLooksLikeIMEI1Field"
+ "ControlLooksLikeIMEI2Field"
+ "ControlLooksLikeNALField"
+ "Requested model %s is being overridden by %s."
+ "SafariShared/WBSAgentTools.swift"
+ "Sending search engine suggestions search end feedback to parsecd: %p (paired with search start feedback: %p)"
+ "Sending search engine suggestions search end feedback to parsecd: %{private}@ (paired with search start feedback: %{private}@)"
+ "\\\\u[0-9a-fA-F]{4}"
+ "\\\\u\\{[0-9a-fA-F]{1,6}\\}"
+ "cachedTokenCount"
+ "completionTokenCount"
+ "device-imei1"
+ "device-imei2"
+ "device-nal"
+ "promptTokenCount"
+ "property assignment"
+ "thoughtTokenCount"
+ "|\\s*(?:\\?\\.)?\\s*\\["
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5MM79q/Sources/SafariShared_iosmac/SafariShared/SafariShared/History/Service/WBSHistoryServiceURLCompletion.mm"
- "22625.1.22.11.4"
- "@\"WBSRecentWebSearchEntry\"16@?0@\"WBSRecentWebSearchEntry\"8"
- "com.apple.Safari.web-extension"
- "com.apple.SafariShared.WBSHistoryItem.LastVisit"
- "completionTokensCount"
- "promptTokensCount"
- "search engine"
- "searchTextFieldFormSubmissionURLString"
- "visibleNonEmptyFormTextControlsInForm"
```
