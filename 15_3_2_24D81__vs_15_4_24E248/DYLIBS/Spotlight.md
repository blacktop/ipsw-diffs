## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Versions/A/Spotlight`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x4e430
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x36b0
-  __TEXT.__const: 0x548
-  __TEXT.__cstring: 0x4d8d
-  __TEXT.__gcc_except_tab: 0xde0
-  __TEXT.__oslogstring: 0x955
+2333.22.13.7.0
+  __TEXT.__text: 0x5465c
+  __TEXT.__auth_stubs: 0x1030
+  __TEXT.__objc_methlist: 0x3b8c
+  __TEXT.__const: 0x578
+  __TEXT.__cstring: 0x4e3d
+  __TEXT.__gcc_except_tab: 0x21f0
+  __TEXT.__oslogstring: 0xc90
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xda0
-  __TEXT.__objc_classname: 0x58a
-  __TEXT.__objc_methname: 0xb8da
-  __TEXT.__objc_methtype: 0x1124
-  __TEXT.__objc_stubs: 0x9f60
-  __DATA_CONST.__got: 0xa90
+  __TEXT.__unwind_info: 0x10b0
+  __TEXT.__eh_frame: 0x60
+  __TEXT.__objc_classname: 0x58b
+  __TEXT.__objc_methname: 0xbca4
+  __TEXT.__objc_methtype: 0x1371
+  __TEXT.__objc_stubs: 0xa380
+  __DATA_CONST.__got: 0xaf0
   __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3098
+  __DATA_CONST.__objc_selrefs: 0x3298
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x8d0
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x1420
-  __AUTH_CONST.__cfstring: 0x59e0
-  __AUTH_CONST.__objc_const: 0x60a8
-  __AUTH_CONST.__objc_intobj: 0x6d8
+  __DATA_CONST.__objc_arraydata: 0x8b0
+  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x15e8
+  __AUTH_CONST.__cfstring: 0x5a80
+  __AUTH_CONST.__objc_const: 0x59d0
   __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__objc_intobj: 0x6d8
+  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x470
-  __DATA.__data: 0x6a8
-  __DATA.__bss: 0x46c
+  __DATA.__objc_ivar: 0x484
+  __DATA.__data: 0x6d0
+  __DATA.__bss: 0x474
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x108
   __DATA_DIRTY.__bss: 0x1d0

   - /System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 102FC87D-955B-3C7E-85F0-8E19C38077B9
-  Functions: 1411
-  Symbols:   4393
-  CStrings:  3899
+  UUID: 7A3B9B47-6524-3D7C-9418-5148AA782B5A
+  Functions: 1541
+  Symbols:   4646
+  CStrings:  3964
 
Symbols:
+ +[SPAppDefaults isAppleInternalInstall].cold.1
+ +[SPAppDefaults localSuggestionsEnabled].cold.1
+ +[SPAppDefaults showDebugLocalSuggestionsEnabled].cold.1
+ +[SPApplicationQuery getAppDisplayNameList].cold.1
+ +[SPApplicationQuery getAppleApps].cold.1
+ +[SPApplicationQuery getAppleInternalApps].cold.1
+ +[SPApplicationQuery getAppleSystemApps].cold.1
+ +[SPApplicationQuery getFrequentlyUsedAppleInternalApps].cold.1
+ +[SPApplicationQuery isNonHomeDirectoryFilePath:].cold.1
+ +[SPCoreSpotlightManagedQuery getHomeDir]
+ +[SPCoreSpotlightManagedQuery getHomeDir].cold.1
+ +[SPCoreSpotlightQuery defaultPrefetchedAttributes].cold.1
+ +[SPCoreSpotlightResult attrHasPhotosAlbumMemoryResult:]
+ +[SPCoreSpotlightResult titleStringFromAttrsForAlbumMemory:]
+ +[SPCoreSpotlightResult titleStringFromAttrsForAlbumMemory:].cold.1
+ +[SPDefaults getShowExtensionStatus].cold.1
+ +[SPFileRadarSupport getSharedInstance].cold.1
+ +[SPPhotoUtilities bundlesIndexingPhotos].cold.1
+ +[SPQueryTask queryClassesSearchTool].cold.1
+ +[SPQueryTask queryClasses].cold.1
+ +[SPQueryTask(Ranking) syntheticLocalSections].cold.1
+ +[SPUISearchModel sharedGeneralInstance].cold.1
+ -[SFSearchResult_SpotlightExtras(SPResultExtensions) contactImage].cold.1
+ -[SFSearchResult_SpotlightExtras(SPResultExtensions) hasAlternateData].cold.1
+ -[SFSearchResult_SpotlightExtras(SPResultExtensions) isPhotoImageOrMovie].cold.1
+ -[SFSearchResult_SpotlightExtras(SPResultExtensions) safariDocumentImage].cold.1
+ -[SFSearchResult_SpotlightExtras(SPResultExtensions) unknownImage].cold.1
+ -[SPApplicationQuery _sendFilteredResponseOfKind:].cold.1
+ -[SPApplicationQueryResult valueForAttribute:].cold.1
+ -[SPCoreSpotlightManagedQuery getEnabledIndexPaths].cold.1
+ -[SPCoreSpotlightQuery .cxx_construct]
+ -[SPCoreSpotlightQuery _prepareFoundBundleIDs]
+ -[SPCoreSpotlightQuery collectSearchResults:]
+ -[SPCoreSpotlightQuery topHitNominatedByPommesScoringforBundleIdentifier:].cold.1
+ -[SPCoreSpotlightResult fullAttributeSet]
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:].cold.1
+ -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:]
+ -[SPFileRadarSupport dumpSearchResultCategories]
+ -[SPFileRadarSupport searchResultCategoriesLogPath]
+ -[SPKDictionaryQuery start].cold.1
+ -[SPMessageTracing signpostLog].cold.1
+ -[SPMetadataPattern mutableFilterResults:queryState:].cold.1
+ -[SPMetadataQuery _prepareQuery].cold.1
+ -[SPMetadataQuery isPeopleSearch]
+ -[SPMetadataQuery setIsPeopleSearch:]
+ -[SPMetadataResult fullAttributeSet]
+ -[SPMetadataResult isValidObjectTypeIfDateAttribute:value:].cold.1
+ -[SPMetadataResult updateRecentSpotlightEngagementData:date:renderPosition:].cold.1
+ -[SPQueryTask(Ranking) resultRankingFeedbackWithResult:duplicateResults:originalResultsId:].cold.1
+ -[_SPResultsArrays ecrGroundedPersons]
+ -[_SPResultsArrays setEcrGroundedPersons:]
+ AAFMediaTypeXML_block_invoke.onceToken.382
+ GCC_except_table101
+ GCC_except_table107
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table132
+ GCC_except_table15
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table3
+ GCC_except_table30
+ GCC_except_table34
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table5
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table8
+ GCC_except_table80
+ GCC_except_table9
+ GCC_except_table91
+ GCC_except_table95
+ OBJC_IVAR_$_SPCoreSpotlightQuery._foundBundleIDs
+ OBJC_IVAR_$_SPCoreSpotlightQuery._resultHeaps
+ OBJC_IVAR_$_SPCoreSpotlightQuery._resultRankTables
+ OBJC_IVAR_$_SPCoreSpotlightQuery._resultRecencyTables
+ OBJC_IVAR_$_SPMetadataQuery._isPeopleSearch
+ OBJC_IVAR_$__SPResultsArrays._ecrGroundedPersons
+ SPLogInit.cold.1
+ _CFHash
+ _MDItemAppEntityTitle
+ _MDItemEndDate
+ _MDItemExternalID
+ _MDItemPhotosTitle
+ _MDItemShortcutLastUsedDate
+ _MDQueryResultEmbeddingDistances
+ _MDQueryResultNewMatchedExtraQueriesField
+ _MDQueryResultRetrievalType
+ _MDQueryResultScoreL1
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_SPECRGroundedPerson
+ _PRSRankingEventsBundleString
+ _Z19printRetrievedItemsyRKNSt3__13setIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEEEiS2_b.cold.1
+ _ZN17SPResultValueItemC2EP16CSSearchableItemd.cold.1
+ __119-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]_block_invoke.cold.1
+ __119-[SPQueryTask(Ranking) rankAndPrune:maxResults:totalResultCount:query:currentLocale:isAdvancedQuerySyntax:currentTime:]_block_invoke.511
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.405
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.416
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.421
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.424
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke.cold.1
+ __32-[SPMetadataQuery _prepareQuery]_block_invoke_2.410
+ __35-[SPCoreSpotlightResult markAsUsed]_block_invoke.182
+ __35-[SPCoreSpotlightResult markAsUsed]_block_invoke.cold.1
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.334
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.383
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.423
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.423.cold.1
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.337
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.424
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.cold.2
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.cold.3
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_3.359
+ __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_3.427
+ __40-[SPCoreSpotlightQuery responseSections]_block_invoke.134
+ __40-[SPCoreSpotlightQuery responseSections]_block_invoke.137
+ __42-[SPApplicationQuery startWithFuzzyValue:]_block_invoke.387
+ __42-[SPApplicationQuery startWithFuzzyValue:]_block_invoke_2.393
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.314
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.319
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.324
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.326
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.331
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.315
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.320
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.325
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.327
+ __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.332
+ __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke.266
+ __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke.285
+ __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_2.286
+ __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_3.287
+ __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_4.290
+ __50-[SPApplicationQuery _sendFilteredResponseOfKind:]_block_invoke.715
+ __50-[SPApplicationQuery _sendFilteredResponseOfKind:]_block_invoke.729
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.32
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.38
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.41
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.49
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.33
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.39
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.42
+ __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.50
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_SPCoreSpotlightResult
+ __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEP8NSStringb
+ __Z14getContainerIdPK16CSSearchableItem
+ __Z18computeHybridScoreffP8NSString
+ __Z18getGreaterOperatoribP8NSString
+ __Z19printRetrievedItemsyRKNSt3__13setIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEEEiS2_b
+ __Z21getRetrievalTypeIndexib
+ __Z24baseDenseGreaterOperatorRK17SPResultValueItemS1_
+ __Z25baseHybridGreaterOperatorRK17SPResultValueItemS1_
+ __Z25baseSparseGreaterOperatorRK17SPResultValueItemS1_
+ __Z26rankingbitsGreaterOperatorRK17SPResultValueItemS1_
+ __Z28calendarDenseGreaterOperatorRK17SPResultValueItemS1_
+ __Z29calendarHybridGreaterOperatorRK17SPResultValueItemS1_
+ __Z29calendarSparseGreaterOperatorRK17SPResultValueItemS1_
+ __ZGVZ18computeHybridScoreffP8NSStringE19isCleanSlateEnabled
+ __ZL8getScoreR17SPResultValueItemb
+ __ZN13tt_hash_tableI31SPResultValueItemHashTableEntryE32container_table_check_and_insertI37SPResultItemHashTableEntryRankingLessEEbRKS0_PS0_T_
+ __ZN13tt_hash_tableI31SPResultValueItemHashTableEntryE32container_table_check_and_insertI37SPResultItemHashTableEntryRecencyLessEEbRKS0_T_
+ __ZN17SPResultValueItemC1EP16CSSearchableItemd
+ __ZN17SPResultValueItemC2EP16CSSearchableItemd
+ __ZN17SPResultValueItemD1Ev
+ __ZN31SPResultValueItemHashTableEntryD1Ev
+ __ZNK37SPResultItemHashTableEntryRankingLessclERK31SPResultValueItemHashTableEntryS2_
+ __ZNK37SPResultItemHashTableEntryRecencyLessclERK31SPResultValueItemHashTableEntryS2_
+ __ZNKSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EE7__cloneEPNS0_6__baseIS9_EE
+ __ZNKSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EE7__cloneEv
+ __ZNKSt3__18functionIFb17SPResultValueItemS1_EEclES1_S1_
+ __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EEC2B8nn190102ERKS4_
+ __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EED2B8nn190102Ev
+ __ZNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EE7destroyEv
+ __ZNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EED0Ev
+ __ZNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EED1Ev
+ __ZNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EEclEOS2_SB_
+ __ZNSt3__110__pop_heapB8nn190102INS_17_ClassicAlgPolicyENS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__114__split_bufferI13tt_hash_tableI31SPResultValueItemHashTableEntryERNS_9allocatorIS3_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferI13tt_hash_tableI31SPResultValueItemHashTableEntryERNS_9allocatorIS3_EEED2Ev
+ __ZNSt3__114__split_bufferI17SPResultValueItemRNS_9allocatorIS1_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferI17SPResultValueItemRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferINS_6vectorI17SPResultValueItemNS_9allocatorIS2_EEEERNS3_IS5_EEE5clearB8nn190102Ev
+ __ZNSt3__114__split_bufferINS_6vectorI17SPResultValueItemNS_9allocatorIS2_EEEERNS3_IS5_EEED2Ev
+ __ZNSt3__117__floyd_sift_downB8nn190102INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI13tt_hash_tableI31SPResultValueItemHashTableEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI17SPResultValueItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI31SPResultValueItemHashTableEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorI17SPResultValueItemNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__122__libcpp_verbose_abortEPKcz
+ __ZNSt3__125__throw_bad_function_callB8nn190102Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorI13tt_hash_tableI31SPResultValueItemHashTableEntryEEES4_EEvRT_PT0_S9_S9_
+ __ZNSt3__16vectorI13tt_hash_tableI31SPResultValueItemHashTableEntryENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorI13tt_hash_tableI31SPResultValueItemHashTableEntryENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRlS2_EEEPS3_DpOT_
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__init_with_sizeB8nn190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEEC2B8nn190102EmRKS1_
+ __ZNSt3__16vectorINS0_I17SPResultValueItemNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn190102Ev
+ __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__19allocatorI17SPResultValueItemE7destroyB8nn190102EPS1_
+ __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE7destroyB8nn190102EPS1_
+ __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE9constructB8nn190102IS1_JRKS1_EEEvPT_DpOT0_
+ __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE9constructB8nn190102IS1_JRS1_EEEvPT_DpOT0_
+ __ZSt28__throw_bad_array_new_lengthB8nn190102v
+ __ZSt9terminatev
+ __ZTVNSt3__110__function6__funcIPFbRK17SPResultValueItemS4_ENS_9allocatorIS6_EEFbS2_S2_EEE
+ __ZZ18computeHybridScoreffP8NSStringE19isCleanSlateEnabled
+ __ZZ25canLogIdentifierForBundleP8NSStringE12debugEnabled
+ __ZZ25canLogIdentifierForBundleP8NSStringE30ALLOWED_BUNDELS_FOR_ID_LOGGING
+ __ZZ25canLogIdentifierForBundleP8NSStringE9onceToken
+ __ZZ44-[SPCoreSpotlightQuery buildGroupedResults:]E13sTimebaseInfo
+ __ZZ48-[SPCoreSpotlightQuery createSearchQueryContext]E19onceAttributesToken
+ __ZZ48-[SPCoreSpotlightQuery createSearchQueryContext]E26sSmallCompletionAttributes
+ __ZZ48-[SPCoreSpotlightQuery createSearchQueryContext]E28sDefaultCompletionAttributes
+ __ZZ51+[SPCoreSpotlightQuery defaultPrefetchedAttributes]E30sCSDefaultPrefetchedAttributes
+ __ZZ51+[SPCoreSpotlightQuery defaultPrefetchedAttributes]E9onceToken
+ __ZZ74-[SPCoreSpotlightQuery topHitNominatedByPommesScoringforBundleIdentifier:]E30pommesScoringBundleIdentifiers
+ __ZZ74-[SPCoreSpotlightQuery topHitNominatedByPommesScoringforBundleIdentifier:]E9onceToken
+ __ZdlPv
+ __ZdlPvSt19__type_descriptor_t
+ __Znwm
+ ___119-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:]_block_invoke
+ ___40-[SPCoreSpotlightQuery responseSections]_block_invoke_2
+ ___46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_5
+ ___46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_6
+ ___48-[SPFileRadarSupport dumpSearchResultCategories]_block_invoke
+ ___60+[SPCoreSpotlightResult titleStringFromAttrsForAlbumMemory:]_block_invoke
+ ____Z25canLogIdentifierForBundleP8NSString_block_invoke
+ ___block_descriptor_104_ea8_32s40s48s56s64s72r80r88w_e17_v16?0"NSArray"8l
+ ___block_descriptor_40_e57_q24?0"<SSPommesRankingItem>"8"<SSPommesRankingItem>"16l
+ ___block_descriptor_40_ea8_32s_e41_v32?0"NSString"8"NSMutableArray"16^B24l
+ ___block_descriptor_40_ea8_32s_e49_v32?0"NSString"8"SFMutableResultSection"16^B24l
+ ___block_descriptor_40_ea8_32s_e52_v88?0{SPResultValueItemHashTableEntry=TdiffffQ}8l
+ ___block_descriptor_40_ea8_32w_e5_v8?0l
+ ___block_descriptor_41_e8_32s_e15_v32?08Q16^B24l
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_48_ea8_32s40r_e41_v32?0"NSString"8"NSMutableArray"16^B24l
+ ___block_descriptor_48_ea8_32s40w_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_ea8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_48_ea8_32s40w_e30_v24?0"NSString"8"NSArray"16l
+ ___block_descriptor_48_ea8_32s40w_e42_v32?0"NSString"8"NSArray"16"NSArray"24l
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0l
+ ___block_descriptor_51_e8_32s_e57_q24?0"<SSPommesRankingItem>"8"<SSPommesRankingItem>"16l
+ ___block_descriptor_56_e8_32s40bs48bs_e57_q24?0"<SSPommesRankingItem>"8"<SSPommesRankingItem>"16l
+ ___block_descriptor_56_ea8_32s40s48w_e5_v8?0l
+ ___block_descriptor_64_ea8_32s40s48s56w_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48r56r64r72r80r88r_e26_v24?0"NSDictionary"8^B16l
+ ___clang_call_terminate
+ ___copy_helper_block_e8_32s40b48b
+ ___copy_helper_block_e8_32s40s48r56r64r72r80r88r
+ ___copy_helper_block_ea8_32s
+ ___copy_helper_block_ea8_32s40r
+ ___copy_helper_block_ea8_32s40s48s56s64s72r80r88w
+ ___copy_helper_block_ea8_32s40s48s56w
+ ___copy_helper_block_ea8_32s40s48w
+ ___copy_helper_block_ea8_32s40w
+ ___copy_helper_block_ea8_32w
+ ___cxa_begin_catch
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r
+ ___destroy_helper_block_ea8_32s
+ ___destroy_helper_block_ea8_32s40r
+ ___destroy_helper_block_ea8_32s40s48s56s64s72r80r88w
+ ___destroy_helper_block_ea8_32s40s48s56w
+ ___destroy_helper_block_ea8_32s40s48w
+ ___destroy_helper_block_ea8_32s40w
+ ___destroy_helper_block_ea8_32w
+ ___floatuntisf
+ ___getGreaterOperator_block_invoke
+ ___getGreaterOperator_block_invoke_2
+ ___gxx_personality_v0
+ __block_literal_global.101
+ __block_literal_global.128
+ __block_literal_global.146
+ __block_literal_global.159
+ __block_literal_global.184
+ __block_literal_global.228
+ __block_literal_global.241
+ __block_literal_global.267
+ __block_literal_global.269
+ __block_literal_global.274
+ __block_literal_global.282
+ __block_literal_global.289
+ __block_literal_global.292
+ __block_literal_global.296
+ __block_literal_global.304
+ __block_literal_global.312
+ __block_literal_global.336
+ __block_literal_global.340
+ __block_literal_global.375
+ __block_literal_global.385
+ __block_literal_global.389
+ __block_literal_global.410
+ __block_literal_global.412
+ __block_literal_global.426
+ __block_literal_global.429
+ __block_literal_global.691
+ __block_literal_global.693
+ __block_literal_global.698
+ __block_literal_global.706
+ __block_literal_global.717
+ __block_literal_global.732
+ __block_literal_global.83
+ __block_literal_global.85
+ __createResultForLockedQuery_block_invoke.840
+ __getGreaterOperator_block_invoke.604
+ __getGreaterOperator_block_invoke.607
+ __processResultsInSection_block_invoke.582
+ __processResultsInSection_block_invoke.595
+ _abort
+ _getEcrGroundedPersonFromGroundedOutput
+ _getGreaterOperator
+ _getpwuid
+ _getuid
+ _isAppleInternalInstall
+ _objc_msgSend$CalendarL1Compare:to:queryTime:
+ _objc_msgSend$_prepareFoundBundleIDs
+ _objc_msgSend$addCharactersInRange:
+ _objc_msgSend$appEntityType
+ _objc_msgSend$attrHasPhotosAlbumMemoryResult:
+ _objc_msgSend$collectSearchResults:
+ _objc_msgSend$curationScore
+ _objc_msgSend$defaultList
+ _objc_msgSend$domainIdentifier
+ _objc_msgSend$dumpSearchResultCategories
+ _objc_msgSend$ecrGroundedPersons
+ _objc_msgSend$expirationDate
+ _objc_msgSend$floatValue
+ _objc_msgSend$getHomeDir
+ _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:
+ _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithItemContentType:
+ _objc_msgSend$initWithName:relationLabel:ecrToken:queryRawToken:
+ _objc_msgSend$initWithQueryString:queryContext:
+ _objc_msgSend$isAppEntitySearch
+ _objc_msgSend$isCardEventSearch
+ _objc_msgSend$isSearchToolClient
+ _objc_msgSend$mailConversationID
+ _objc_msgSend$nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:isSearchToolClient:qu:currentTime:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$parseQUQuery:
+ _objc_msgSend$photosContainerIdentifier
+ _objc_msgSend$prepareSectionForL1Ranking:
+ _objc_msgSend$searchResultCategoriesLogPath
+ _objc_msgSend$setAttribute:forKey:
+ _objc_msgSend$setEcrGroundedPersons:
+ _objc_msgSend$setIsPeopleSearch:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:isSearchToolClient:
+ _objc_msgSend$titleStringFromAttrsForAlbumMemory:
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:
+ _objc_msgSend$writeToURL:atomically:encoding:error:
+ _processResultsInSection
+ bootDriveIsFast.cold.1
+ kPlaceHolderInputName_block_invoke.onceToken
+ kPlaceHolderInputName_block_invoke.sectionBundlesRequiringMapping
+ titleStringFromAttrsForAlbumMemory:.onceToken
+ titleStringFromAttrsForAlbumMemory:.sTrimSet
- -[SPCoreSpotlightQuery queryPattern]
- -[SPCoreSpotlightQuery resultWithIdentifier:title:url:bundleIdentifier:]
- -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:]
- -[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:].cold.1
- -[SPCoreSpotlightResult initWithSearchResult:]
- AAFMediaTypeXML_block_invoke.onceToken.380
- GCC_except_table100
- GCC_except_table131
- GCC_except_table55
- GCC_except_table76
- GCC_except_table83
- GCC_except_table94
- OBJC_IVAR_$_SPCoreSpotlightQuery._queryPattern
- SPQueryKindIsSearchToolSearch.isSearchToolDebugMode
- SPQueryKindIsSearchToolSearch.isSearchToolRanking
- SPQueryKindIsSearchToolSearch.onceToken
- _SPQueryKindIsSearchToolSearch
- _SPRoundToNSignificantDigits
- _SSDefaultsSetResources
- __119-[SPQueryTask(Ranking) rankAndPrune:maxResults:totalResultCount:query:currentLocale:isAdvancedQuerySyntax:currentTime:]_block_invoke.506
- __25+[SPQueryTask deactivate]_block_invoke.cold.1
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.401
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.412
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.417
- __32-[SPMetadataQuery _prepareQuery]_block_invoke.420
- __32-[SPMetadataQuery _prepareQuery]_block_invoke_2.406
- __35-[SPCoreSpotlightResult markAsUsed]_block_invoke.173
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.332
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.357
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.381
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke.424
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.335
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_2.425
- __39-[SPQueryTask(Ranking) finishResponse:]_block_invoke_3.428
- __42-[SPApplicationQuery startWithFuzzyValue:]_block_invoke.391
- __42-[SPApplicationQuery startWithFuzzyValue:]_block_invoke_2.397
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.513
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.518
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke.523
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.514
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.519
- __44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_2.524
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke.269
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke.286
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke.289
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_2.292
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_3.295
- __46+[SPApplicationQuery _createApplicationsQuery]_block_invoke_4.298
- __50-[SPApplicationQuery _sendFilteredResponseOfKind:]_block_invoke.719
- __50-[SPApplicationQuery _sendFilteredResponseOfKind:]_block_invoke.733
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.31
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.34
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.40
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke.42
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.32
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.35
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.41
- __51-[SPCoreSpotlightManagedQuery createAndStartQuery:]_block_invoke_2.43
- __83-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:]_block_invoke.cold.1
- ___44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_5
- ___44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_6
- ___44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_7
- ___44-[SPCoreSpotlightQuery createAndStartQuery:]_block_invoke_8
- ___83-[SPCoreSpotlightResult initWithAttributeSet:fetchedAttributes:ranker:queryString:]_block_invoke
- ___SPQueryKindIsSearchToolSearch_block_invoke
- ___block_descriptor_40_e8_32bs_e57_q24?0"<SSPommesRankingItem>"8"<SSPommesRankingItem>"16l
- ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32s_e49_v32?0"NSString"8"SFMutableResultSection"16^B24l
- ___block_descriptor_43_e57_q24?0"<SSPommesRankingItem>"8"<SSPommesRankingItem>"16l
- ___block_descriptor_48_e8_32s40r_e41_v32?0"NSString"8"NSMutableArray"16^B24l
- ___block_descriptor_48_e8_32s40s_e26_v24?0"NSDictionary"8^B16l
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8l
- ___block_descriptor_96_e8_32s40s48s56s64r72r80w_e17_v16?0"NSArray"8l
- ___copy_helper_block_e8_32s40s48s56s64r72r80w
- ___destroy_helper_block_e8_32s40s48s56s64r72r80w
- __block_literal_global.1023
- __block_literal_global.109
- __block_literal_global.137
- __block_literal_global.155
- __block_literal_global.158
- __block_literal_global.215
- __block_literal_global.224
- __block_literal_global.237
- __block_literal_global.254
- __block_literal_global.275
- __block_literal_global.276
- __block_literal_global.277
- __block_literal_global.291
- __block_literal_global.297
- __block_literal_global.300
- __block_literal_global.301
- __block_literal_global.307
- __block_literal_global.308
- __block_literal_global.330
- __block_literal_global.334
- __block_literal_global.338
- __block_literal_global.379
- __block_literal_global.383
- __block_literal_global.393
- __block_literal_global.408
- __block_literal_global.414
- __block_literal_global.427
- __block_literal_global.430
- __block_literal_global.572
- __block_literal_global.620
- __block_literal_global.637
- __block_literal_global.695
- __block_literal_global.697
- __block_literal_global.702
- __block_literal_global.710
- __block_literal_global.721
- __block_literal_global.736
- __block_literal_global.87
- __block_literal_global.93
- __createResultForLockedQuery_block_invoke.844
- __processResultsInSection_block_invoke.593
- __processResultsInSection_block_invoke.597
- __processResultsInSection_block_invoke.608
- __processResultsInSection_block_invoke_2.594
- __processResultsInSection_block_invoke_2.598
- _objc_msgSend$initWithAttributeSet:fetchedAttributes:ranker:queryString:
- _objc_msgSend$initWithContentsOfURL:
- _objc_msgSend$logForTrigger:queryID:
- _objc_msgSend$nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:queryKind:clientBundleID:qu:currentTime:
- _objc_msgSend$parseQUQuery:isSearchToolClient:
- _objc_msgSend$resourcesForClient:options:
- _objc_msgSend$thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:queryKind:clientBundleID:isSearchToolClient:
- _sSRResources
- buildGroupedResults:.sTimebaseInfo
- createSearchQueryContext.onceAttributesToken
- createSearchQueryContext.sDefaultCompletionAttributes
- createSearchQueryContext.sSmallCompletionAttributes
- defaultPrefetchedAttributes.onceToken
- defaultPrefetchedAttributes.sCSDefaultPrefetchedAttributes
- sMessagesChatDomain_block_invoke.onceToken
- sMessagesChatDomain_block_invoke.sectionBundlesRequiringMapping
- topHitNominatedByPommesScoringforBundleIdentifier:.onceToken
- topHitNominatedByPommesScoringforBundleIdentifier:.pommesScoringBundleIdentifiers
CStrings:
+ "%@"
+ "%@/SearchResultCategories.log"
+ ".cxx_construct"
+ "@52@0:8@16@24@32@40B48"
+ "@56@0:8@16@24@32@40B48B52"
+ "Added %@empty ecrGroundedOutput to spqueryrespone"
+ "AlbumEntity"
+ "CalendarL1Compare:to:queryTime:"
+ "Error getting enabled index paths: %@"
+ "Got result for bundle %@"
+ "MemoryEntity"
+ "Received kLSHiddenAppsEligibilityChangedNotification"
+ "SPCoreSpotlightQuery.mm"
+ "SearchToolCleanSlateDenseRetrieval"
+ "SharedAlbumEntity"
+ "System hiding %@"
+ "System not hiding %@"
+ "T@\"NSArray\",&,V_ecrGroundedPersons"
+ "TB,N,V_isPeopleSearch"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (min: %f, max: %f)"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (minScore: %f, maxScore: %f - minTS: %f, maxTS: %f)"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d (out of %d) items for bundle = %@, retrievalType = %d: %@"
+ "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d items for bundle = %@, retrievalType = %d"
+ "[qid=%llu][SpotlightRanking]<_resultRankingHeaps> added %d items for bundle = %@, retrievalType = %d (minEmbeddingScore: %f, maxEmbeddingScore: %f, minPommesL1Score: %f, maxPommesL1Score: %f, minHybridScore: %f, maxHybridScore: %f)"
+ "_ecrGroundedPersons"
+ "_foundBundleIDs"
+ "_prepareFoundBundleIDs"
+ "_resultHeaps"
+ "_resultRankTables"
+ "_resultRecencyTables"
+ "addCharactersInRange:"
+ "appEntityType"
+ "attrHasPhotosAlbumMemoryResult:"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "collectSearchResults:"
+ "com.apple.spotlight.events"
+ "curationScore"
+ "domainIdentifier"
+ "dumpSearchResultCategories"
+ "ecrGroundedPersons"
+ "expirationDate"
+ "failed to get passwd entry for uid %u"
+ "floatValue"
+ "fullAttributeSet"
+ "getHomeDir"
+ "initWithAttributeSet:fetchedAttributes:ranker:queryString:isAppEntitySearch:isSearchToolQuery:"
+ "initWithAttributeSet:fetchedAttributes:ranker:queryString:isSearchToolQuery:"
+ "initWithContentsOfURL:error:"
+ "initWithFormat:"
+ "initWithItemContentType:"
+ "initWithName:relationLabel:ecrToken:queryRawToken:"
+ "initWithQueryString:queryContext:"
+ "isAppEntitySearch"
+ "isCardEventSearch"
+ "mailConversationID"
+ "nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:isSearchToolClient:qu:currentTime:"
+ "non "
+ "numberWithUnsignedLong:"
+ "parseQUQuery:"
+ "personRelationMap"
+ "photosContainerIdentifier"
+ "prepareSectionForL1Ranking:"
+ "rawQueryToken"
+ "searchResultCategoriesLogPath"
+ "setAttribute:forKey:"
+ "setEcrGroundedPersons:"
+ "stringWithCString:encoding:"
+ "tap-to-radar://new?componentid=624062&title=%@&description=%@&attachments=%@,%@"
+ "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:isSearchToolClient:"
+ "titleStringFromAttrsForAlbumMemory:"
+ "unsignedLongValue"
+ "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v88@?0{SPResultValueItemHashTableEntry=Tdif@fff@@Q}8"
+ "writeToURL:atomically:encoding:error:"
+ "{vector<std::vector<SPResultValueItem>, std::allocator<std::vector<SPResultValueItem>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<SPResultValueItem> *, std::allocator<std::vector<SPResultValueItem>>>=\"__value_\"^v}}"
+ "{vector<tt_hash_table<SPResultValueItemHashTableEntry>, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<tt_hash_table<SPResultValueItemHashTableEntry> *, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__value_\"^v}}"
- "Added empty ecrGroundedOutput to spqueryrespone"
- "Added non empty ecrGroundedOutput to spqueryrespone"
- "Resources object is nil at [SPQueryTask deactivate]"
- "SPCoreSpotlightQuery.m"
- "SRResourcesOwner"
- "SearchToolRanking"
- "com.apple.intelligenceflow"
- "com.apple.omniSearch"
- "com.apple.ondeviceeval"
- "initWithAttributeSet:fetchedAttributes:ranker:queryString:"
- "initWithContentsOfURL:"
- "initWithSearchResult:"
- "logForTrigger:queryID:"
- "nominateLocalTopHitsFromSections:withItemRanker:sectionHeader:maxInitiallyVisibleResults:shortcutResult:isBullseyeNonCommittedSearch:isBullseyeCommittedSearch:parsecEnabled:maxNumAppsInTopHitSection:queryId:queryKind:clientBundleID:qu:currentTime:"
- "parseQUQuery:isSearchToolClient:"
- "resourcesForClient:options:"
- "resultWithIdentifier:title:url:bundleIdentifier:"
- "tap-to-radar://new?componentid=624062&title=%@&description=%@&attachments=%@"
- "thresholdResultsInSection:userQuery:queryID:isEntitiesSearch:currentTime:isScopedSearch:queryKind:clientBundleID:isSearchToolClient:"

```
