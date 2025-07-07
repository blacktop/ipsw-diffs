## SpotlightServices

> `/System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices`

```diff

-2381.0.1.0.0
-  __TEXT.__text: 0x1536fc
-  __TEXT.__auth_stubs: 0x1c70
-  __TEXT.__objc_methlist: 0xee60
+2385.1.0.1.0
+  __TEXT.__text: 0x154748
+  __TEXT.__auth_stubs: 0x1cb0
+  __TEXT.__objc_methlist: 0xef48
   __TEXT.__const: 0x29f0
-  __TEXT.__cstring: 0x30e5f
-  __TEXT.__gcc_except_tab: 0x4c10
-  __TEXT.__oslogstring: 0x962b
+  __TEXT.__cstring: 0x30ecf
+  __TEXT.__oslogstring: 0x98eb
+  __TEXT.__gcc_except_tab: 0x4c20
   __TEXT.__ustring: 0x8d6
   __TEXT.__dlopen_cstrs: 0xd1
-  __TEXT.__swift5_typeref: 0x1c2
+  __TEXT.__swift5_typeref: 0x1da
   __TEXT.__swift5_reflstr: 0x99
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x19c
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift5_capture: 0x84
-  __TEXT.__unwind_info: 0x3348
-  __TEXT.__objc_classname: 0x14ae
-  __TEXT.__objc_methname: 0x2b349
-  __TEXT.__objc_methtype: 0x30ee
-  __TEXT.__objc_stubs: 0x1c980
-  __DATA_CONST.__got: 0x2078
-  __DATA_CONST.__const: 0xfcb8
-  __DATA_CONST.__objc_classlist: 0x698
+  __TEXT.__swift5_capture: 0x94
+  __TEXT.__unwind_info: 0x3390
+  __TEXT.__objc_classname: 0x14d4
+  __TEXT.__objc_methname: 0x2b652
+  __TEXT.__objc_methtype: 0x3119
+  __TEXT.__objc_stubs: 0x1cb00
+  __DATA_CONST.__got: 0x2088
+  __DATA_CONST.__const: 0xfce8
+  __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8db8
+  __DATA_CONST.__objc_selrefs: 0x8e38
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x538
-  __DATA_CONST.__objc_arraydata: 0x1228
-  __AUTH_CONST.__auth_got: 0xe48
-  __AUTH_CONST.__const: 0x27d0
-  __AUTH_CONST.__cfstring: 0x2b240
-  __AUTH_CONST.__objc_const: 0x181c8
-  __AUTH_CONST.__objc_intobj: 0x32b8
+  __DATA_CONST.__objc_superrefs: 0x550
+  __DATA_CONST.__objc_arraydata: 0x1248
+  __AUTH_CONST.__auth_got: 0xe68
+  __AUTH_CONST.__const: 0x27f8
+  __AUTH_CONST.__cfstring: 0x2b300
+  __AUTH_CONST.__objc_const: 0x18418
+  __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0x2a0
+  __AUTH_CONST.__objc_intobj: 0x32b8
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__objc_arrayobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH.__objc_data: 0x2048
+  __AUTH.__objc_data: 0x20e8
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x1510
+  __DATA.__objc_ivar: 0x1528
   __DATA.__data: 0x1238
   __DATA.__bss: 0xc28
   __DATA.__common: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6A6CE827-88F3-3E74-B590-969CCBCFC191
-  Functions: 6355
-  Symbols:   21981
-  CStrings:  19435
+  UUID: 005C0BBE-A372-3912-9A5F-F54C45401E76
+  Functions: 6380
+  Symbols:   22068
+  CStrings:  19484
 
Symbols:
+ +[SSAppBrowseSectionBuilder appSectionWithTitle:identifier:style:highDensity:appIdentities:]
+ +[SSAppBrowseSectionBuilder appSectionWithTitle:identifier:style:highDensity:results:]
+ +[SSAppBrowseSectionBuilder titleMaxLinesForGridView]
+ +[SSBrowseSectionBuilder _resultCardSectionForResult:highDensity:]
+ +[SSBrowseSectionBuilder _sectionResultForResults:style:highDensity:withSectionTitle:]
+ +[SSBrowseSectionBuilder sectionWithTitle:identifier:style:highDensity:results:]
+ +[SSBrowseSectionBuilder titleMaxLinesForGridView]
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:]
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.1
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.2
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.3
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.4
+ +[SSSnippetUtilities createFormattedSnippetForResult:withContext:].cold.5
+ -[PRSRankingItem isUserTypedURL]
+ -[PRSRankingItem setIsUserTypedURL:]
+ -[SFSearchResult_SpotlightExtras formattedSnippet]
+ -[SFSearchResult_SpotlightExtras setFormattedSnippet:]
+ -[TPFTextPieceFinder .cxx_destruct]
+ -[TPFTextPieceFinder createPiecesWithTargets:]
+ -[TPFTextPieceFinder findLocationsOfTarget:]
+ -[TPFTextPieceFinder initWithFullText:maxLength:maxNumCandidates:]
+ -[TPFTextPieceFinder initWithFullText:maxLength:maxNumCandidates:].cold.1
+ -[TPFTextPieceFinder initWithFullText:maxLength:maxNumCandidates:].cold.2
+ -[TPFTextPieceFinder maxLength]
+ -[TPFTextPieceFinder maxNumCandidates]
+ -[TPFTextPieceFinder originalFullText]
+ -[TPFTextPieceFinder searchableFullText]
+ _NSIntersectionRange
+ _OBJC_CLASS_$_SSSnippetUtilities
+ _OBJC_CLASS_$_TPFTextPieceFinder
+ _OBJC_IVAR_$_PRSRankingItem._isUserTypedURL
+ _OBJC_IVAR_$_SFSearchResult_SpotlightExtras._formattedSnippet
+ _OBJC_IVAR_$_TPFTextPieceFinder._maxLength
+ _OBJC_IVAR_$_TPFTextPieceFinder._maxNumCandidates
+ _OBJC_IVAR_$_TPFTextPieceFinder._originalFullText
+ _OBJC_IVAR_$_TPFTextPieceFinder._searchableFullText
+ _OBJC_METACLASS_$_SSSnippetUtilities
+ _OBJC_METACLASS_$_TPFTextPieceFinder
+ _SSSpotlightPasteboardContinuityBundle
+ __OBJC_$_CLASS_METHODS_SSSnippetUtilities
+ __OBJC_$_INSTANCE_METHODS_TPFTextPieceFinder
+ __OBJC_$_INSTANCE_VARIABLES_TPFTextPieceFinder
+ __OBJC_$_PROP_LIST_TPFTextPieceFinder
+ __OBJC_CLASS_RO_$_SSSnippetUtilities
+ __OBJC_CLASS_RO_$_TPFTextPieceFinder
+ __OBJC_METACLASS_RO_$_SSSnippetUtilities
+ __OBJC_METACLASS_RO_$_TPFTextPieceFinder
+ ___46-[TPFTextPieceFinder createPiecesWithTargets:]_block_invoke
+ ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1440
+ ___block_descriptor_64_e8_32s40s48s56s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8s40l8s48l8s56l8
+ ___block_literal_global.126
+ ___block_literal_global.135
+ ___block_literal_global.1383
+ ___block_literal_global.1385
+ ___block_literal_global.1387
+ ___block_literal_global.156
+ ___block_literal_global.160
+ ___block_literal_global.175
+ ___block_literal_global.180
+ ___block_literal_global.190
+ ___block_literal_global.2029
+ ___block_literal_global.2040
+ ___block_literal_global.341
+ ___block_literal_global.349
+ ___block_literal_global.378
+ ___block_literal_global.395
+ ___block_literal_global.515
+ ___block_literal_global.519
+ ___block_literal_global.529
+ ___block_literal_global.637
+ ___block_literal_global.687
+ ___block_literal_global.743
+ ___collectTokens_block_invoke
+ _block_copy_helper.28
+ _block_descriptor.30
+ _block_destroy_helper.29
+ _collectTokens.locationAnnotationsToCheck
+ _collectTokens.onceToken
+ _objc_msgSend$_resultCardSectionForResult:highDensity:
+ _objc_msgSend$_sectionResultForResults:style:highDensity:withSectionTitle:
+ _objc_msgSend$appSectionWithTitle:identifier:style:highDensity:appIdentities:
+ _objc_msgSend$appSectionWithTitle:identifier:style:highDensity:results:
+ _objc_msgSend$createFormattedSnippetForResult:withContext:
+ _objc_msgSend$createPiecesWithTargets:
+ _objc_msgSend$findLocationsOfTarget:
+ _objc_msgSend$formattedSnippet
+ _objc_msgSend$initWithFullText:maxLength:maxNumCandidates:
+ _objc_msgSend$maxLength
+ _objc_msgSend$maxNumCandidates
+ _objc_msgSend$originalFullText
+ _objc_msgSend$rawSearchTermsFromLLMQU
+ _objc_msgSend$searchableFullText
+ _objc_msgSend$sectionWithTitle:identifier:style:highDensity:results:
+ _objc_msgSend$setFormattedSnippet:
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic _____SgXw 17SpotlightServices41SSICloudDriveAppLibraryCollectionObserverC
+ _symbolic _____SgXwz_Xx 17SpotlightServices41SSICloudDriveAppLibraryCollectionObserverC
- +[SSBrowseSectionBuilder _resultCardSectionForResult:]
- +[SSBrowseSectionBuilder _sectionResultForResults:style:withSectionTitle:]
- _SSEnableSearchToolL1RankingV2
- _SSEnableSearchToolL1RankingV2.cold.1
- _SSEnableSearchToolL1RankingV2.enabled
- _SSEnableSearchToolL1RankingV2.onceToken
- ___68+[SSRankingManager searchToolRanker:queryContext:searchToolBundles:]_block_invoke.1439
- ___SSEnableSearchToolL1RankingV2_block_invoke
- ___block_literal_global.120
- ___block_literal_global.132
- ___block_literal_global.1378
- ___block_literal_global.1382
- ___block_literal_global.150
- ___block_literal_global.159
- ___block_literal_global.163
- ___block_literal_global.168
- ___block_literal_global.178
- ___block_literal_global.183
- ___block_literal_global.188
- ___block_literal_global.2028
- ___block_literal_global.2039
- ___block_literal_global.338
- ___block_literal_global.346
- ___block_literal_global.375
- ___block_literal_global.512
- ___block_literal_global.516
- ___block_literal_global.526
- ___block_literal_global.634
- ___block_literal_global.684
- ___block_literal_global.740
- _block_copy_helper.25
- _block_descriptor.27
- _block_destroy_helper.26
- _objc_msgSend$_resultCardSectionForResult:
- _objc_msgSend$_sectionResultForResults:style:withSectionTitle:
- _objc_msgSend$appSectionWithTitle:identifier:style:results:
- _objc_msgSend$sectionWithTitle:identifier:style:results:
CStrings:
+ "%lu Items"
+ "@40@0:8@16Q24Q32"
+ "@40@0:8@16i24B28@32"
+ "@48@0:8@16@24i32B36@40"
+ "SSSnippetUtilities"
+ "T@\"NSMutableDictionary\",&,V_resourceMetadata"
+ "T@\"NSString\",&,V_resourceMetadataPath"
+ "T@\"NSString\",R,C,N,V_originalFullText"
+ "T@\"NSString\",R,C,N,V_searchableFullText"
+ "T@\"SFRichText\",&,N,V_formattedSnippet"
+ "TB,N,V_isUserTypedURL"
+ "TB,V_resourceMetadataNeedsWrite"
+ "TPFTextPieceFinder"
+ "TQ,R,N,V_maxLength"
+ "TQ,R,N,V_maxNumCandidates"
+ "[SpotlightRanking] [SearchTool] [Calendar] [PerfectMatch] Found one on one search term in the calendar item with id %@."
+ "[SpotlightRanking] [SearchTool] [Calendar] [PerfectMatch] ID:%@, title:%@, Perfect match for one on one meeting queries with single recipient calendar item. Either no person token or person tokens matched in author/recipient."
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] Failed to initialize the snippets candidate generator."
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] Snippet is only enabled for SearchToolClient"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] [SSSnippetCandidatesGenerator] bad argument: maxLength must be greater than zero"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] [SSSnippetCandidatesGenerator] fullText is nil or zero length"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] queryContext is nil"
+ "[SpotlightRanking] [SearchTool] [PQASnippet] [SnippetGeneration] result is nil"
+ "_formattedSnippet"
+ "_isUserTypedURL"
+ "_maxLength"
+ "_maxNumCandidates"
+ "_originalFullText"
+ "_resultCardSectionForResult:highDensity:"
+ "_searchableFullText"
+ "_sectionResultForResults:style:highDensity:withSectionTitle:"
+ "appSectionWithTitle:identifier:style:highDensity:appIdentities:"
+ "appSectionWithTitle:identifier:style:highDensity:results:"
+ "com.apple.spotlight.pasteboard.continuity"
+ "createFormattedSnippetForResult:withContext:"
+ "createPiecesWithTargets:"
+ "findLocationsOfTarget:"
+ "formattedSnippet"
+ "initWithFullText:maxLength:maxNumCandidates:"
+ "isUserTypedURL"
+ "maxLength"
+ "maxNumCandidates"
+ "originalFullText"
+ "searchableFullText"
+ "sectionWithTitle:identifier:style:highDensity:results:"
+ "setFormattedSnippet:"
+ "setIsUserTypedURL:"
+ "titleMaxLinesForGridView"
- "%@ Items"
- "@36@0:8@16i24@28"
- "SearchToolRetrievalSparseScoringV2"
- "T@\"NSMutableDictionary\",&,N,V_resourceMetadata"
- "T@\"NSString\",&,N,V_resourceMetadataPath"
- "TB,N,V_resourceMetadataNeedsWrite"
- "[SpotlightRanking] [SearchTool] [Calendar] Found one on one search term in the calendar item with id %@."
- "[SpotlightRanking] [SearchTool] [Calendar] ID:%@, title:%@, Perfect match for one on one meeting queries with single recipient calendar item. Either no person token or person tokens matched in author/recipient."
- "_resultCardSectionForResult:"
- "_sectionResultForResults:style:withSectionTitle:"

```
