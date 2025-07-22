## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2385.1.0.1.0
-  __TEXT.__text: 0x154748
-  __TEXT.__auth_stubs: 0x1cb0
-  __TEXT.__objc_methlist: 0xef48
-  __TEXT.__const: 0x29f0
-  __TEXT.__cstring: 0x30ecf
-  __TEXT.__oslogstring: 0x98eb
-  __TEXT.__gcc_except_tab: 0x4c20
+2387.1.0.0.0
+  __TEXT.__text: 0x155ef0
+  __TEXT.__auth_stubs: 0x1ce0
+  __TEXT.__objc_methlist: 0xf018
+  __TEXT.__const: 0x2a00
+  __TEXT.__cstring: 0x30f4f
+  __TEXT.__gcc_except_tab: 0x4ccc
+  __TEXT.__oslogstring: 0x9afb
   __TEXT.__ustring: 0x8d6
   __TEXT.__dlopen_cstrs: 0xd1
-  __TEXT.__swift5_typeref: 0x1da
+  __TEXT.__swift5_typeref: 0x1e6
   __TEXT.__swift5_reflstr: 0x99
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x19c

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_capture: 0x94
-  __TEXT.__unwind_info: 0x3390
-  __TEXT.__objc_classname: 0x14d4
-  __TEXT.__objc_methname: 0x2b652
+  __TEXT.__unwind_info: 0x33a8
+  __TEXT.__objc_classname: 0x14eb
+  __TEXT.__objc_methname: 0x2b95c
   __TEXT.__objc_methtype: 0x3119
-  __TEXT.__objc_stubs: 0x1cb00
-  __DATA_CONST.__got: 0x2088
-  __DATA_CONST.__const: 0xfce8
-  __DATA_CONST.__objc_classlist: 0x6a8
+  __TEXT.__objc_stubs: 0x1cd20
+  __DATA_CONST.__got: 0x2098
+  __DATA_CONST.__const: 0xfcf8
+  __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e38
+  __DATA_CONST.__objc_selrefs: 0x8ec0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x1248
-  __AUTH_CONST.__auth_got: 0xe68
-  __AUTH_CONST.__const: 0x27f8
-  __AUTH_CONST.__cfstring: 0x2b300
-  __AUTH_CONST.__objc_const: 0x18418
-  __AUTH_CONST.__objc_arrayobj: 0x828
-  __AUTH_CONST.__objc_doubleobj: 0x2a0
+  __AUTH_CONST.__auth_got: 0xe80
+  __AUTH_CONST.__const: 0x2818
+  __AUTH_CONST.__cfstring: 0x2b380
+  __AUTH_CONST.__objc_const: 0x185a8
   __AUTH_CONST.__objc_intobj: 0x32b8
+  __AUTH_CONST.__objc_doubleobj: 0x2a0
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x20e8
+  __AUTH.__objc_data: 0x2138
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x1528
+  __DATA.__objc_ivar: 0x153c
   __DATA.__data: 0x1238
   __DATA.__bss: 0xc28
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 005C0BBE-A372-3912-9A5F-F54C45401E76
-  Functions: 6380
-  Symbols:   22068
-  CStrings:  19484
+  UUID: 7CFDC385-77EB-36E2-B415-DC60F96184F4
+  Functions: 6400
+  Symbols:   22152
+  CStrings:  19524
 
Symbols:
+ +[SSFilterUtilities appFilterForResult:]
+ +[SSFilterUtilities filtersForResult:]
+ +[SSSnippetHighlightTool isSegmentHighlighted:]
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.6
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.7
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.8
+ -[PRSRankingItem hasPreExtractedCustomerNames]
+ -[PRSRankingItem isMeCardEmailInAdditionalRecipients]
+ -[PRSRankingItem isMeCardEmailInPrimaryRecipients]
+ -[PRSRankingItem setHasPreExtractedCustomerNames:]
+ -[PRSRankingItem setIsMeCardEmailInAdditionalRecipients:]
+ -[PRSRankingItem setIsMeCardEmailInPrimaryRecipients:]
+ -[SPSearchQueryContext hasPersonIsSelfTokenFromLLMQU]
+ -[SPSearchQueryContext setHasPersonIsSelfTokenFromLLMQU:]
+ -[SSSnippetHighlightTool .cxx_destruct]
+ -[SSSnippetHighlightTool findAndMergeHighlightRangesInSnippet:]
+ -[SSSnippetHighlightTool initWithTerms:]
+ -[SSSnippetHighlightTool makeHighlightedSnippet:]
+ -[SSSnippetHighlightTool setTerms:]
+ -[SSSnippetHighlightTool terms]
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_SSSnippetHighlightTool
+ _OBJC_IVAR_$_PRSRankingItem._hasPreExtractedCustomerNames
+ _OBJC_IVAR_$_PRSRankingItem._isMeCardEmailInAdditionalRecipients
+ _OBJC_IVAR_$_PRSRankingItem._isMeCardEmailInPrimaryRecipients
+ _OBJC_IVAR_$_SPSearchQueryContext._hasPersonIsSelfTokenFromLLMQU
+ _OBJC_IVAR_$_SSSnippetHighlightTool._terms
+ _OBJC_METACLASS_$_SSSnippetHighlightTool
+ _SSSectionIdentifierWebPrefix
+ _SSSemanticSearchMD7Enabled
+ _SSSemanticSearchMD7Enabled.cold.1
+ _SSSemanticSearchMD7Enabled.ffStatus
+ _SSSemanticSearchMD7Enabled.onceToken
+ _TextHighlightAttributeName
+ __OBJC_$_CLASS_METHODS_SSSnippetHighlightTool
+ __OBJC_$_INSTANCE_METHODS_SSSnippetHighlightTool
+ __OBJC_$_INSTANCE_VARIABLES_SSSnippetHighlightTool
+ __OBJC_$_PROP_LIST_SSSnippetHighlightTool
+ __OBJC_CLASS_RO_$_SSSnippetHighlightTool
+ __OBJC_METACLASS_RO_$_SSSnippetHighlightTool
+ ___63-[SSSnippetHighlightTool findAndMergeHighlightRangesInSnippet:]_block_invoke
+ ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1414
+ ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1449
+ ___SSSemanticSearchMD7Enabled_block_invoke
+ ___block_literal_global.1397
+ ___block_literal_global.1398
+ ___block_literal_global.1400
+ ___block_literal_global.1402
+ ___block_literal_global.2038
+ ___block_literal_global.2049
+ ___block_literal_global.344
+ ___block_literal_global.352
+ ___block_literal_global.381
+ ___block_literal_global.39
+ ___block_literal_global.500
+ ___block_literal_global.518
+ ___block_literal_global.522
+ ___block_literal_global.532
+ ___block_literal_global.690
+ ___block_literal_global.746
+ _objc_msgSend$appFilterForResult:
+ _objc_msgSend$attribute:atIndex:effectiveRange:
+ _objc_msgSend$filtersForResult:
+ _objc_msgSend$findAndMergeHighlightRangesInSnippet:
+ _objc_msgSend$hasPersonIsSelfTokenFromLLMQU
+ _objc_msgSend$hasPreExtractedCustomerNames
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$initWithTerms:
+ _objc_msgSend$isMeCardEmailInAdditionalRecipients
+ _objc_msgSend$isMeCardEmailInPrimaryRecipients
+ _objc_msgSend$isSegmentHighlighted:
+ _objc_msgSend$makeHighlightedSnippet:
+ _objc_msgSend$normalizedSearchString
+ _objc_msgSend$setHasPersonIsSelfTokenFromLLMQU:
+ _objc_msgSend$setHasPreExtractedCustomerNames:
+ _objc_msgSend$setIsMeCardEmailInAdditionalRecipients:
+ _objc_msgSend$setIsMeCardEmailInPrimaryRecipients:
+ _objc_msgSend$terms
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic _____SgXw 8Dispatch0A8WorkItemC
+ _symbolic _____SgXwz_Xx 8Dispatch0A8WorkItemC
- +[SSApplicationResultBuilder onenessBadgingImage]
- _SSSemanticSearchMD6Enabled
- _SSSemanticSearchMD6Enabled.cold.1
- _SSSemanticSearchMD6Enabled.ffStatus
- _SSSemanticSearchMD6Enabled.onceToken
- ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1405
- ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1440
- ___SSSemanticSearchMD6Enabled_block_invoke
- ___block_literal_global.1380
- ___block_literal_global.1385
- ___block_literal_global.1387
- ___block_literal_global.1388
- ___block_literal_global.2029
- ___block_literal_global.2040
- ___block_literal_global.341
- ___block_literal_global.349
- ___block_literal_global.378
- ___block_literal_global.395
- ___block_literal_global.515
- ___block_literal_global.519
- ___block_literal_global.529
- ___block_literal_global.637
- ___block_literal_global.687
- ___block_literal_global.743
- _objc_msgSend$onenessBadgingImage
- _symbolic _____Sgz_Xx 8Dispatch0A8WorkItemC
CStrings:
+ "MeCard email match in additionalRecipients in favor of item with match in primaryRecipients (demoted: %@|%@, promoted: %@|%@)"
+ "SSSnippetHighlightTool"
+ "SearchUnifiedEmbeddingMD7"
+ "T@\"NSArray\",&,N,V_terms"
+ "TB,N,V_hasPersonIsSelfTokenFromLLMQU"
+ "TB,N,V_hasPreExtractedCustomerNames"
+ "TB,N,V_isMeCardEmailInAdditionalRecipients"
+ "TB,N,V_isMeCardEmailInPrimaryRecipients"
+ "[SpotlightRanking] [SearchTool] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in additionalRecipients"
+ "[SpotlightRanking] [SearchTool] [Mail] For ID:%@, subject:%@, found meCard email:%@ match in primaryRecipients"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] Non snippet Found. Full Text: %@ Search String: %@"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] highlight found"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] no highlight found but match was found"
+ "_hasPersonIsSelfTokenFromLLMQU"
+ "_hasPreExtractedCustomerNames"
+ "_isMeCardEmailInAdditionalRecipients"
+ "_isMeCardEmailInPrimaryRecipients"
+ "_kMDItemBundleID==com.apple.shortcuts || _kMDItemBundleID==com.apple.duetexpertd"
+ "appFilterForResult:"
+ "attribute:atIndex:effectiveRange:"
+ "com.apple.SSSnippetHighlightTool.TextHighlightAttribute"
+ "filtersForResult:"
+ "findAndMergeHighlightRangesInSnippet:"
+ "hasPersonIsSelfTokenFromLLMQU"
+ "hasPreExtractedCustomerNames"
+ "initWithString:attributes:"
+ "initWithTerms:"
+ "isMeCardEmailInAdditionalRecipients"
+ "isMeCardEmailInPrimaryRecipients"
+ "isSegmentHighlighted:"
+ "makeHighlightedSnippet:"
+ "me"
+ "personEmails"
+ "setHasPersonIsSelfTokenFromLLMQU:"
+ "setHasPreExtractedCustomerNames:"
+ "setIsMeCardEmailInAdditionalRecipients:"
+ "setIsMeCardEmailInPrimaryRecipients:"
+ "setTerms:"
+ "v40@0:8@16d24d32"
- "SearchUnifiedEmbeddingMD6"
- "_kMDItemBundleID==com.apple.shortcuts || (_kMDItemBundleID==com.apple.duetexpertd && _kMDItemDomainIdentifier==com.apple.proactive.suggestedActions)"
- "onenessBadgingImage"
- "v40@0:8d16d24d32"

```
