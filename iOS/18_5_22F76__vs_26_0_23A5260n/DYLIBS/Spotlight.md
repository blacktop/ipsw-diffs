## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x517ac
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_methlist: 0x1fec
-  __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x4b4c
-  __TEXT.__cstring: 0x294f
-  __TEXT.__oslogstring: 0x2526
-  __TEXT.__unwind_info: 0xc18
+2374.0.1.0.0
+  __TEXT.__text: 0x53ac0
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x2064
+  __TEXT.__const: 0x190
+  __TEXT.__gcc_except_tab: 0x4e3c
+  __TEXT.__cstring: 0x2cd5
+  __TEXT.__oslogstring: 0x274f
+  __TEXT.__unwind_info: 0xd20
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x231
-  __TEXT.__objc_methname: 0x9239
-  __TEXT.__objc_methtype: 0x1e35
-  __TEXT.__objc_stubs: 0x8940
-  __DATA_CONST.__got: 0x12f8
-  __DATA_CONST.__const: 0xbc0
+  __TEXT.__objc_classname: 0x235
+  __TEXT.__objc_methname: 0x93a1
+  __TEXT.__objc_methtype: 0x16c2
+  __TEXT.__objc_stubs: 0x8ae0
+  __DATA_CONST.__got: 0x1320
+  __DATA_CONST.__const: 0xb98
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27c8
+  __DATA_CONST.__objc_selrefs: 0x2830
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x3a8
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__const: 0x688
-  __AUTH_CONST.__cfstring: 0x2b00
-  __AUTH_CONST.__objc_const: 0x3750
+  __AUTH_CONST.__auth_got: 0x838
+  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0x36d0
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x398
+  __DATA.__objc_ivar: 0x388
   __DATA.__data: 0x280
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__data: 0x11
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__data: 0xa
+  __DATA_DIRTY.__bss: 0x488
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F74FFC4B-8804-3D17-AC51-868C57621A49
-  Functions: 939
-  Symbols:   4646
-  CStrings:  2807
+  UUID: AEB7A374-9C4D-3B9F-A367-C5033775B9FE
+  Functions: 965
+  Symbols:   4719
+  CStrings:  2830
 
Symbols:
+ -[SPCSSearchQuery disabledBundlesWithParseDisabledBundles:filterEventBundle:]
+ -[SPCSSearchQuery filterQueriesWithParseFilterQueries:onlyApps:filterOrphanedFiles:]
+ -[SPCSSearchQuery skipResult:installedApps:]
+ -[SPCSSearchQuery skipResult:installedApps:].cold.1
+ -[SPCSSearchQuery skipResult:installedApps:].cold.2
+ -[SPSearchTopHitResult secondaryTitleStringFromAttrsForMemories:]
+ -[SPSearchTopHitResult secondaryTitleStringFromAttrsForMemories:].cold.1
+ -[SPZKWQueryTask _isInBiometryLockout]
+ -[SPZKWQueryTask _isLocked]
+ -[SPZKWQueryTask _sendRankingFeedback]
+ -[SPZKWQueryTask _updateResultWithState:sections:]
+ -[SPZKWQueryTask endFeedbackWithStartSearchFeedback:]
+ -[SPZKWQueryTask startFeedbackWithQueryId:]
+ GCC_except_table106
+ GCC_except_table115
+ GCC_except_table126
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table21
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table96
+ GCC_except_table97
+ GCC_except_table98
+ _MDItemAppEntitySubtitle
+ _MDMessageLpDescription
+ _MDMessageLpTitle
+ _OBJC_CLASS_$_SSRankingUtilities
+ _OBJC_IVAR_$_SPCSSearchQuery._indexResultsRegistry
+ _SSPommesRankingIsEnabled
+ _SSSectionIdentifierSyndicatedFilesMessages
+ _SSSectionIdentifierZKW
+ __Z14getContainerIdPK28CSSearchableItemAttributeSet
+ __Z14getMaxHeapSizeP8NSStringbbil
+ __Z19collectIndexResultsP7NSArrayIP16CSSearchableItemEPK20SPSearchQueryContextbilR20IndexResultsRegistry
+ __ZL34logSPResultValueItemHashTableEntryyPK8NSStringPvPS_RK31SPResultValueItemHashTableEntry
+ __ZL34logSPResultValueItemHashTableEntryyPK8NSStringPvPS_RK31SPResultValueItemHashTableEntry.cold.1
+ __ZN12IndexResults12removeResultEyPK8NSStringPK28CSSearchableItemAttributeSet
+ __ZN12IndexResults13collectResultEyPK8NSStringP16CSSearchableItemd
+ __ZN12IndexResults13collectResultEyPK8NSStringP16CSSearchableItemd.cold.1
+ __ZN12IndexResults13printHeapInfoEyPK8NSStringb
+ __ZN12IndexResults15printTablesInfoEyPK8NSStringd
+ __ZN12IndexResults19printAllResultsInfoEyPK8NSStringdb
+ __ZN12IndexResults19printRetrievedItemsEyPK8NSString
+ __ZN12IndexResultsC1EjP8NSStringP8NSNumberRKNSt3__18functionIFb17SPResultValueItemS6_EEE
+ __ZN12IndexResultsC2EOS_
+ __ZN12IndexResultsC2ERKS_
+ __ZN12IndexResultsC2EjP8NSStringP8NSNumberRKNSt3__18functionIFb17SPResultValueItemS6_EEE
+ __ZN12IndexResultsD1Ev
+ __ZN17SPResultValueItemD2Ev
+ __ZN20IndexResultsRegistry12removeResultEP8NSStringPK28CSSearchableItemAttributeSet
+ __ZN20IndexResultsRegistry13collectResultEjP8NSStringP8NSNumberP16CSSearchableItemdRKNSt3__18functionIFb17SPResultValueItemS8_EEE
+ __ZN20IndexResultsRegistry14processResultsEPK20SPSearchQueryContextU13block_pointerFv12IndexResults17SPResultValueItemE
+ __ZN20IndexResultsRegistry18getIndexResultsIdxEP8NSStringP8NSNumber
+ __ZN20IndexResultsRegistry23getOrCreateIndexResultsEjP8NSStringP8NSNumberRKNSt3__18functionIFb17SPResultValueItemS6_EEE
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn200100EPKvm
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn200100ERKS6_S9_
+ __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EEC2B8nn200100EOS4_
+ __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EEC2B8nn200100ERKS4_
+ __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EED2B8nn200100Ev
+ __ZNSt3__110__pop_heapB8nn200100INS_17_ClassicAlgPolicyENS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
+ __ZNSt3__111__sift_downB8nn200100INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_OT0_NS_15iterator_traitsISA_E15difference_typeESA_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZNSt3__114__split_bufferI12IndexResultsRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__114__split_bufferI17SPResultValueItemRNS_9allocatorIS1_EEE5clearB8nn200100Ev
+ __ZNSt3__116allocator_traitsINS_9allocatorI17SPResultValueItemEEE7destroyB8nn200100IS2_Li0EEEvRS3_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorI17SPResultValueItemEEE9constructB8nn200100IS2_JRS2_ELi0EEEvRS3_PT_DpOT0_
+ __ZNSt3__117__floyd_sift_downB8nn200100INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI12IndexResultsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI17SPResultValueItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI31SPResultValueItemHashTableEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn200100EPKcm
+ __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn200100EPKcm
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_4pairIU8__strongP22SFMutableResultSectionU8__strongP19NSMutableOrderedSetIP20SPSearchTopHitResultEEEEEPvEEEEEclB8nn200100EPSM_
+ __ZNSt3__125__throw_bad_function_callB8nn200100Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorI12IndexResultsEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorI17SPResultValueItemEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn200100INS_9allocatorI31SPResultValueItemHashTableEntryEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__14pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IU8__strongP22SFMutableResultSectionU8__strongP19NSMutableOrderedSetIP20SPSearchTopHitResultEEEED1Ev
+ __ZNSt3__16vectorI12IndexResultsNS_9allocatorIS1_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorI12IndexResultsNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI12IndexResultsNS_9allocatorIS1_EEE20__throw_out_of_rangeB8nn200100Ev
+ __ZNSt3__16vectorI12IndexResultsNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI12IndexResultsNS_9allocatorIS1_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE16__init_with_sizeB8nn200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__init_with_sizeB8nn200100IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEEC2B8nn200100EmRKS1_
+ __ZNSt3__19__sift_upB8nn200100INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZnwmSt19__type_descriptor_t
+ ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.319
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.195
+ ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.195.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.111
+ ___23-[SPZKWQueryTask start]_block_invoke.111.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.120
+ ___23-[SPZKWQueryTask start]_block_invoke.124
+ ___23-[SPZKWQueryTask start]_block_invoke.124.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke.124.cold.2
+ ___23-[SPZKWQueryTask start]_block_invoke.134
+ ___23-[SPZKWQueryTask start]_block_invoke_2
+ ___23-[SPZKWQueryTask start]_block_invoke_2.cold.1
+ ___23-[SPZKWQueryTask start]_block_invoke_2.cold.2
+ ___23-[SPZKWQueryTask start]_block_invoke_2.cold.3
+ ___27+[SPCSSearchQuery activate]_block_invoke.183
+ ___29+[SPCSSearchQuery initialize]_block_invoke.171
+ ___30-[SPRecommendationQuery start]_block_invoke.160
+ ___31-[SPRecommendationQuery begin:]_block_invoke.103
+ ___31-[SPRecommendationQuery begin:]_block_invoke.104
+ ___31-[SPRecommendationQuery begin:]_block_invoke.92
+ ___31-[SPRecommendationQuery begin:]_block_invoke.92.cold.1
+ ___31-[SPRecommendationQuery begin:]_block_invoke.95
+ ___34+[SPFederatedQueryTask initialize]_block_invoke.251
+ ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.107
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.460
+ ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.465
+ ___47-[SPCSSearchQuery updateMailAttachmentResults:]_block_invoke.230
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.348
+ ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.352
+ ___65-[SPSearchTopHitResult secondaryTitleStringFromAttrsForMemories:]_block_invoke
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.414
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.419
+ ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.433
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.167
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.170
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.171
+ ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.172
+ ____ZN12IndexResults15printTablesInfoEyPK8NSStringd_block_invoke
+ ____ZN12IndexResults15printTablesInfoEyPK8NSStringd_block_invoke_2
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.653
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.653.cold.1
+ ____ZN20IndexResultsRegistry14processResultsEPK20SPSearchQueryContextU13block_pointerFv12IndexResults17SPResultValueItemE_block_invoke
+ ____ZN20IndexResultsRegistry14processResultsEPK20SPSearchQueryContextU13block_pointerFv12IndexResults17SPResultValueItemE_block_invoke.119
+ ___block_descriptor_192_ea8_32bs40c18_ZTS12IndexResults_e52_v88?0{SPResultValueItemHashTableEntry=TdiffffQ}8l
+ ___block_descriptor_40_ea8_32s_e799_v240?0{IndexResults=I{function<bool (SPResultValueItem, SPResultValueItem)>={__value_func<bool (SPResultValueItem, SPResultValueItem)>=(type=[24C])^v}}{vector<SPResultValueItem, std::allocator<SPResultValueItem>>=^{SPResultValueItem}^{SPResultValueItem}^{SPResultValueItem}}{tt_hash_table<SPResultValueItemHashTableEntry>=I{vector<SPResultValueItemHashTableEntry, std::allocator<SPResultValueItemHashTableEntry>>=^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}}}{tt_hash_table<SPResultValueItemHashTableEntry>=I{vector<SPResultValueItemHashTableEntry, std::allocator<SPResultValueItemHashTableEntry>>=^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}}}}8{SPResultValueItem=Tdiffff}160ls32l8
+ ___block_literal_global.109
+ ___block_literal_global.121
+ ___block_literal_global.147
+ ___block_literal_global.173
+ ___block_literal_global.177
+ ___block_literal_global.185
+ ___block_literal_global.204
+ ___block_literal_global.215
+ ___block_literal_global.230
+ ___block_literal_global.256
+ ___block_literal_global.259
+ ___block_literal_global.261
+ ___block_literal_global.278
+ ___block_literal_global.293
+ ___block_literal_global.304
+ ___block_literal_global.314
+ ___block_literal_global.321
+ ___block_literal_global.325
+ ___block_literal_global.339
+ ___block_literal_global.401
+ ___block_literal_global.409
+ ___block_literal_global.422
+ ___block_literal_global.435
+ ___block_literal_global.487
+ ___block_literal_global.511
+ ___block_literal_global.514
+ ___block_literal_global.529
+ ___block_literal_global.651
+ ___block_literal_global.86
+ ___block_literal_global.90
+ ___block_literal_global.91
+ ___copy_helper_block_ea8_40c18_ZTS12IndexResults
+ ___destroy_helper_block_ea8_40c18_ZTS12IndexResults
+ _isSupportedMessageAttachmentFiles
+ _objc_msgSend$_isInBiometryLockout
+ _objc_msgSend$_isLocked
+ _objc_msgSend$_sendRankingFeedback
+ _objc_msgSend$_updateResultWithState:sections:
+ _objc_msgSend$disabledBundlesWithParseDisabledBundles:filterEventBundle:
+ _objc_msgSend$endFeedbackWithStartSearchFeedback:
+ _objc_msgSend$filterQueriesWithParseFilterQueries:onlyApps:filterOrphanedFiles:
+ _objc_msgSend$initWithQueryID:kind:sourceKind:sections:
+ _objc_msgSend$initWithQueryID:sourceKind:error:
+ _objc_msgSend$initWithQueryID:sourceKind:sections:
+ _objc_msgSend$logSections:message:queryId:query:isSearchToolClient:
+ _objc_msgSend$longValue
+ _objc_msgSend$retrievalType
+ _objc_msgSend$secondaryTitleStringFromAttrsForMemories:
+ _objc_msgSend$sendEmptyResponseIfNecessaryForSourceKind:
+ _objc_msgSend$setEntityType:
+ _objc_msgSend$setString:
+ _objc_msgSend$skipResult:installedApps:
+ _objc_msgSend$startFeedbackWithQueryId:
+ _objc_retain_x11
+ _secondaryTitleStringFromAttrsForMemories:.onceToken
+ _secondaryTitleStringFromAttrsForMemories:.sTrimSet
- -[SPCSSearchQuery addSearchResult:withFoundBundleID:].cold.1
- GCC_except_table104
- GCC_except_table112
- GCC_except_table113
- GCC_except_table120
- GCC_except_table124
- GCC_except_table134
- GCC_except_table139
- GCC_except_table160
- GCC_except_table162
- GCC_except_table163
- GCC_except_table50
- GCC_except_table59
- GCC_except_table61
- GCC_except_table63
- GCC_except_table65
- GCC_except_table67
- GCC_except_table69
- _OBJC_IVAR_$_SPCSSearchQuery._foundBundleIDs
- _OBJC_IVAR_$_SPCSSearchQuery._resultHeaps
- _OBJC_IVAR_$_SPCSSearchQuery._resultRankTables
- _OBJC_IVAR_$_SPCSSearchQuery._resultRecencyTables
- _OBJC_IVAR_$_SPCSSearchQuery._retrievedIds
- _SPZKWSectionBundleID
- _SSSnippetModernizationEnabled
- __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEiP8NSStringb
- __Z14getContainerIdPK16CSSearchableItem
- __Z19printRetrievedItemsyRKNSt3__13setIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEEEiS2_b
- __Z21getRetrievalTypeIndexib
- __ZL34logSPResultValueItemHashTableEntryPvP8NSStringRK31SPResultValueItemHashTableEntry
- __ZN12_GLOBAL__N_113installedAppsEv
- __ZN13tt_hash_tableI31SPResultValueItemHashTableEntryE32container_table_check_and_insertI37SPResultItemHashTableEntryRankingLessEEbRKS0_PS0_T_
- __ZN13tt_hash_tableI31SPResultValueItemHashTableEntryE32container_table_check_and_insertI37SPResultItemHashTableEntryRecencyLessEEbRKS0_T_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
- __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EEC2B8nn190102ERKS4_
- __ZNSt3__110__function12__value_funcIFb17SPResultValueItemS2_EED2B8nn190102Ev
- __ZNSt3__110__pop_heapB8nn190102INS_17_ClassicAlgPolicyENS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_S9_RT0_NS_15iterator_traitsIS9_E15difference_typeE
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_4pairIU8__strongP22SFMutableResultSectionU8__strongP19NSMutableOrderedSetIP20SPSearchTopHitResultEEEEEPvEENS_22__hash_node_destructorINS6_ISM_EEEEE5resetB8nn190102EPSM_
- __ZNSt3__110unique_ptrINS_11__tree_nodeIU8__strongP8NSStringPvEENS_22__tree_node_destructorINS_9allocatorIS6_EEEEE5resetB8nn190102EPS6_
- __ZNSt3__112__destroy_atB8nn190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS1_IU8__strongP22SFMutableResultSectionU8__strongP19NSMutableOrderedSetIP20SPSearchTopHitResultEEEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZNSt3__114__split_bufferI13tt_hash_tableI31SPResultValueItemHashTableEntryERNS_9allocatorIS3_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferI13tt_hash_tableI31SPResultValueItemHashTableEntryERNS_9allocatorIS3_EEED2Ev
- __ZNSt3__114__split_bufferI17SPResultValueItemRNS_9allocatorIS1_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEERNS7_IS9_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEERNS7_IS9_EEED2Ev
- __ZNSt3__114__split_bufferINS_6vectorI17SPResultValueItemNS_9allocatorIS2_EEEERNS3_IS5_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferINS_6vectorI17SPResultValueItemNS_9allocatorIS2_EEEERNS3_IS5_EEED2Ev
- __ZNSt3__117__floyd_sift_downB8nn190102INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEET1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI13tt_hash_tableI31SPResultValueItemHashTableEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI17SPResultValueItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI31SPResultValueItemHashTableEntryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_3setIU8__strongP8NSStringNS_4lessIS5_EENS1_IS5_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorI17SPResultValueItemNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__121__murmur2_or_cityhashImLm64EE18__hash_len_0_to_16B8nn190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_17_to_32B8nn190102EPKcm
- __ZNSt3__121__murmur2_or_cityhashImLm64EE19__hash_len_33_to_64B8nn190102EPKcm
- __ZNSt3__125__throw_bad_function_callB8nn190102Ev
- __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorI13tt_hash_tableI31SPResultValueItemHashTableEntryEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorINS_3setIU8__strongP8NSStringNS_4lessIS5_EENS1_IS5_EEEEEES9_EEvRT_PT0_SE_SE_
- __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSD_SD_
- __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE25__emplace_unique_key_argsIS3_JS3_EEENS_4pairINS_15__tree_iteratorIS3_PNS_11__tree_nodeIS3_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16__treeIU8__strongP8NSStringNS_4lessIS3_EENS_9allocatorIS3_EEE7destroyEPNS_11__tree_nodeIS3_PvEE
- __ZNSt3__16vectorI13tt_hash_tableI31SPResultValueItemHashTableEntryENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorI13tt_hash_tableI31SPResultValueItemHashTableEntryENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRlS2_EEEPS3_DpOT_
- __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE12emplace_backIJRS1_EEES6_DpOT_
- __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEE16__init_with_sizeB8nn190102IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI31SPResultValueItemHashTableEntryNS_9allocatorIS1_EEEC2B8nn190102EmRKS1_
- __ZNSt3__16vectorINS0_I17SPResultValueItemNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEENS7_IS9_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_3setIU8__strongP8NSStringNS_4lessIS4_EENS_9allocatorIS4_EEEENS7_IS9_EEE24__emplace_back_slow_pathIJS9_EEEPS9_DpOT_
- __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERNS_8functionIFb17SPResultValueItemS3_EEENS_11__wrap_iterIPS3_EEEEvT1_SA_OT0_NS_15iterator_traitsISA_E15difference_typeE
- __ZNSt3__19allocatorI17SPResultValueItemE7destroyB8nn190102EPS1_
- __ZNSt3__19allocatorI17SPResultValueItemE9constructB8nn190102IS1_JRS1_EEEvPT_DpOT0_
- __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE7destroyB8nn190102EPS1_
- __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE9constructB8nn190102IS1_JRKS1_EEEvPT_DpOT0_
- __ZNSt3__19allocatorI31SPResultValueItemHashTableEntryE9constructB8nn190102IS1_JRS1_EEEvPT_DpOT0_
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __Znwm
- ___107-[SPFederatedQueryTask sendResults:reset:partiallyComplete:update:complete:unchanged:delayedTopHit:reason:]_block_invoke.313
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189
- ___121-[SPParsecQuery query:didFinishWithResults:withSuggestions:withCorrections:withAlternativeResults:suggestionsAreBlended:]_block_invoke.189.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.110
- ___23-[SPZKWQueryTask start]_block_invoke.114
- ___23-[SPZKWQueryTask start]_block_invoke.115
- ___23-[SPZKWQueryTask start]_block_invoke.115.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.115.cold.2
- ___23-[SPZKWQueryTask start]_block_invoke.115.cold.3
- ___23-[SPZKWQueryTask start]_block_invoke.119.cold.1
- ___23-[SPZKWQueryTask start]_block_invoke.119.cold.2
- ___23-[SPZKWQueryTask start]_block_invoke.95
- ___23-[SPZKWQueryTask start]_block_invoke.95.cold.1
- ___27+[SPCSSearchQuery activate]_block_invoke.180
- ___29+[SPCSSearchQuery initialize]_block_invoke.168
- ___30-[SPRecommendationQuery start]_block_invoke.154
- ___31-[SPRecommendationQuery begin:]_block_invoke.86
- ___31-[SPRecommendationQuery begin:]_block_invoke.86.cold.1
- ___31-[SPRecommendationQuery begin:]_block_invoke.89
- ___31-[SPRecommendationQuery begin:]_block_invoke.97
- ___31-[SPRecommendationQuery begin:]_block_invoke.98
- ___34+[SPFederatedQueryTask initialize]_block_invoke.245
- ___39-[SPParsecQuery queryDidFinishLoading:]_block_invoke.101
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke.453
- ___40-[SPFederatedQueryTask addAndStartQuery]_block_invoke_2.458
- ___47-[SPCSSearchQuery constructResultsForResponse:]_block_invoke.235
- ___47-[SPCSSearchQuery constructResultsForResponse:]_block_invoke_2
- ___47-[SPCSSearchQuery constructResultsForResponse:]_block_invoke_2.236
- ___47-[SPCSSearchQuery updateMailAttachmentResults:]_block_invoke.241
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.342
- ___51-[SPFederatedQueryTask sendFinishedDomains:reason:]_block_invoke.346
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.407
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.412
- ___76-[SPFederatedQueryTask storeCompletedSearch:withSections:suggestionResults:]_block_invoke.426
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke.161
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_2.164
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_3.165
- ___91-[SPParsecQuery findLocalCopies:appIdentifiers:adamIDs:alternativeResults:withQueryString:]_block_invoke_4.166
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.667
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.667.cold.1
- ___block_descriptor_48_ea8_32s40s_e52_v88?0{SPResultValueItemHashTableEntry=TdiffffQ}8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.103
- ___block_literal_global.115
- ___block_literal_global.141
- ___block_literal_global.170
- ___block_literal_global.174
- ___block_literal_global.182
- ___block_literal_global.198
- ___block_literal_global.228
- ___block_literal_global.250
- ___block_literal_global.257
- ___block_literal_global.272
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.308
- ___block_literal_global.315
- ___block_literal_global.319
- ___block_literal_global.333
- ___block_literal_global.394
- ___block_literal_global.402
- ___block_literal_global.415
- ___block_literal_global.428
- ___block_literal_global.480
- ___block_literal_global.504
- ___block_literal_global.507
- ___block_literal_global.522
- ___block_literal_global.665
- ___block_literal_global.84
- ___block_literal_global.85
- _dispatch_group_notify
- _memcpy
- _objc_msgSend$initWithQueryID:kind:sections:
- _objc_msgSend$initWithQueryID:sections:
- _objc_msgSend$logSections:prefix:queryId:query:isSearchToolClient:
- _objc_msgSend$sendEmptyResponseIfNecessary
- _objc_msgSend$unsignedIntegerValue
- _objc_msgSend$unsignedLongValue
- _objc_release_x2
CStrings:
+ "0 2"
+ "@24@0:8Q16"
+ "@28@0:8@16B24"
+ "@32@0:8@16B24B28"
+ "No bundleID for result %@"
+ "Siri Suggestions"
+ "Skipping restricted app %@"
+ "Skipping settings %@ for disabled app %@"
+ "Skipping settings %@ for non-installed %@"
+ "Skipping settings %@ for non-installed app %@"
+ "Skipping settings %@ for restricted app %@"
+ "Skipping shortcut %@ for disabled app %@"
+ "Skipping shortcut %@ for restricted app %@"
+ "T@\"SPSearchQuery\",&,V_query"
+ "[qid=%llu][\"%@\"][SpotlightRanking] Got result for bundle %@"
+ "[qid=%llu][\"%@\"][SpotlightRanking] dropping expired (%@) item (%@) from %@"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (min: %f, max: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (minScore: %f, maxScore: %f - minTS: %f, maxTS: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> hash tables added %d items for bundle = %@, retrievalType = %d (min timestamp: %f, max timestamp: %f, queryTime: %f)"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> queue: %p, bundle = %@, item = %lu has `nil` container id"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> retrieved %d (out of %ld) items for bundle = %@, retrievalType = %d: %@"
+ "[qid=%llu][\"%@\"][SpotlightRanking]<_resultHeaps> retrieved %ld items for bundle = %@, retrievalType = %d"
+ "[qid=%llu][\"%@\"][SpotlightRanking][thread=%p]<_resultHeaps> create IndexResults for bundle = %@, retrievalType = %d index:%@"
+ "_indexResultsRegistry"
+ "_isInBiometryLockout"
+ "_isLocked"
+ "_sendRankingFeedback"
+ "_updateResultWithState:sections:"
+ "cannot put existingEntry to RecencyTables"
+ "cannot put newEntry to RankingTables or RecencyTables"
+ "disabledBundlesWithParseDisabledBundles:filterEventBundle:"
+ "discarded oldEntry from RecencyTables"
+ "endFeedbackWithStartSearchFeedback:"
+ "filterQueriesWithParseFilterQueries:onlyApps:filterOrphanedFiles:"
+ "initWithQueryID:kind:sourceKind:sections:"
+ "initWithQueryID:sourceKind:error:"
+ "initWithQueryID:sourceKind:sections:"
+ "logSections:message:queryId:query:isSearchToolClient:"
+ "longValue"
+ "put existingEntry to RecencyTables"
+ "put newEntry to RankingTables"
+ "put newEntry to RecencyTables"
+ "retrievalType"
+ "secondaryTitleStringFromAttrsForMemories:"
+ "sendEmptyResponseIfNecessaryForSourceKind:"
+ "setEntityType:"
+ "setString:"
+ "skipResult:installedApps:"
+ "startFeedbackWithQueryId:"
+ "v240@?0{IndexResults=I@@@{function<bool (SPResultValueItem, SPResultValueItem)>={__value_func<bool (SPResultValueItem, SPResultValueItem)>=(type=[24C])^v}}{vector<SPResultValueItem, std::allocator<SPResultValueItem>>=^{SPResultValueItem}^{SPResultValueItem}^{SPResultValueItem}}{tt_hash_table<SPResultValueItemHashTableEntry>=I{vector<SPResultValueItemHashTableEntry, std::allocator<SPResultValueItemHashTableEntry>>=^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}}}{tt_hash_table<SPResultValueItemHashTableEntry>=I{vector<SPResultValueItemHashTableEntry, std::allocator<SPResultValueItemHashTableEntry>>=^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}^{SPResultValueItemHashTableEntry}}}}8{SPResultValueItem=Tdif@fff@@}160"
+ "v32@0:8Q16@24"
+ "{BundleIdToResultMap=\"map\"{unordered_map<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}\"syndicatedLinkSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInAppsSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInMessagesSection\"@\"SFMutableResultSection\"\"syndicatedFilesInMessagesSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInNotesSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInFilesSection\"@\"SFMutableResultSection\"\"syndicatedGeneralPhotosSection\"@\"SFMutableResultSection\"\"contactResultsSection\"@\"SFMutableResultSection\"\"peopleResultsSection\"@\"SFMutableResultSection\"\"photosSection\"@\"SFMutableResultSection\"}"
+ "{IndexResultsRegistry=\"queryId\"Q\"redactedQuery\"@\"NSString\"\"results\"{vector<IndexResults, std::allocator<IndexResults>>=\"__begin_\"^{IndexResults}\"__end_\"^{IndexResults}\"__cap_\"^{IndexResults}}\"indexMapping\"@\"NSMutableDictionary\"}"
- "%@ %@"
- "(!(_kMDItemBundleID = %@))"
- "(!(_kMDItemBundleID=%@))"
- "DOMAIN_ZKWS"
- "Got result for bundle %@"
- "Skipping Settings item for app %@"
- "Skipping for uninstalled %@"
- "Skipping shortcut for disabled app %@"
- "T@\"SPSearchQuery\",&,N,V_query"
- "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
- "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
- "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
- "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
- "[SpotlightRanking]<_resultHeaps>: queue: %p, bundle = %@, item = %lu has nil container id"
- "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (min: %f, max: %f)"
- "[qid=%llu][SpotlightRanking]<_resultHeaps> added %d items for bundle = %@, retrievalType = %d (minScore: %f, maxScore: %f - minTS: %f, maxTS: %f)"
- "[qid=%llu][SpotlightRanking]<_resultHeaps> hash tables added %d items for bundle = %@, retrievalType = %d (min timestamp: %f, max timestamp: %f, queryTime: %f)"
- "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d (out of %d) items for bundle = %@, retrievalType = %d: %@"
- "[qid=%llu][SpotlightRanking]<_resultHeaps> retrieved %d items for bundle = %@, retrievalType = %d"
- "_foundBundleIDs"
- "_resultHeaps"
- "_resultRankTables"
- "_resultRecencyTables"
- "_retrievedIds"
- "add to hashtable"
- "cannot put newEntry to RecencyTables "
- "cannot put oldEntry to RecencyTables"
- "initWithQueryID:kind:sections:"
- "initWithQueryID:sections:"
- "logSections:prefix:queryId:query:isSearchToolClient:"
- "sendEmptyResponseIfNecessary"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "{BundleIdToResultMap=\"map\"{unordered_map<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>, std::hash<std::string>, std::equal_to<std::string>, std::allocator<std::pair<const std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>>>=\"__table_\"{__hash_table<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::hash<std::string>, std::equal_to<std::string>>, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::equal_to<std::string>, std::hash<std::string>>, std::allocator<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::hash<std::string>, std::equal_to<std::string>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<std::string, std::__hash_value_type<std::string, std::pair<SFMutableResultSection *, NSMutableOrderedSet<SPSearchTopHitResult *> *>>, std::equal_to<std::string>, std::hash<std::string>>>=\"__value_\"f}}}\"syndicatedLinkSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInAppsSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInMessagesSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInNotesSection\"@\"SFMutableResultSection\"\"syndicatedPhotosInFilesSection\"@\"SFMutableResultSection\"\"syndicatedGeneralPhotosSection\"@\"SFMutableResultSection\"\"contactResultsSection\"@\"SFMutableResultSection\"\"peopleResultsSection\"@\"SFMutableResultSection\"\"photosSection\"@\"SFMutableResultSection\"}"
- "{vector<std::set<NSString *>, std::allocator<std::set<NSString *>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::set<NSString *> *, std::allocator<std::set<NSString *>>>=\"__value_\"^v}}"
- "{vector<std::vector<SPResultValueItem>, std::allocator<std::vector<SPResultValueItem>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::vector<SPResultValueItem> *, std::allocator<std::vector<SPResultValueItem>>>=\"__value_\"^v}}"
- "{vector<tt_hash_table<SPResultValueItemHashTableEntry>, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<tt_hash_table<SPResultValueItemHashTableEntry> *, std::allocator<tt_hash_table<SPResultValueItemHashTableEntry>>>=\"__value_\"^v}}"

```
