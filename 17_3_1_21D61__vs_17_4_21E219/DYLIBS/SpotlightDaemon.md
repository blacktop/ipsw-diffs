## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2274.13.3.0.0
-  __TEXT.__text: 0x71320
-  __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0x2ee0
+2274.23.0.3.0
+  __TEXT.__text: 0x71b00
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_methlist: 0x2f00
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x5055
-  __TEXT.__gcc_except_tab: 0x26c4
-  __TEXT.__oslogstring: 0x617c
-  __TEXT.__unwind_info: 0x19c4
+  __TEXT.__cstring: 0x50b5
+  __TEXT.__gcc_except_tab: 0x2728
+  __TEXT.__oslogstring: 0x6204
+  __TEXT.__unwind_info: 0x19d4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x409
-  __TEXT.__objc_methname: 0xa24e
+  __TEXT.__objc_methname: 0xa28e
   __TEXT.__objc_methtype: 0x1ba6
-  __TEXT.__objc_stubs: 0x82e0
-  __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x2ce8
+  __TEXT.__objc_stubs: 0x8340
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__const: 0x2d10
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4260
-  __DATA_CONST.__objc_selrefs: 0x25a8
-  __DATA_CONST.__objc_arraydata: 0x168
+  __DATA_CONST.__objc_selrefs: 0x25c0
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x370
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x3c40
+  __AUTH_CONST.__cfstring: 0x3c60
   __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x370
-  __DATA.__objc_superrefs: 0xd0
+  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x368
-  __DATA.__data: 0x3d8
+  __DATA.__data: 0x398
   __DATA.__thread_ptrs: 0x8
-  __DATA.__bss: 0x1a9
+  __DATA.__bss: 0x121
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xaa0
-  __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x320
+  __DATA_DIRTY.__objc_data: 0xaf0
+  __DATA_DIRTY.__data: 0x90
+  __DATA_DIRTY.__bss: 0x3a8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2040
-  Symbols:   6968
-  CStrings:  3294
+  Functions: 2045
+  Symbols:   6989
+  CStrings:  3306
 
Symbols:
+ +[SDSodiumFeature isSearchCLIBundle:]
+ -[SDLockHandler initWithDelegate:options:].cold.4
+ -[SPCoreSpotlightIndexer lockedCx]
+ -[SPCoreSpotlightIndexer lockingCx]
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table527
+ GCC_except_table536
+ GCC_except_table542
+ GCC_except_table566
+ GCC_except_table567
+ GCC_except_table575
+ GCC_except_table596
+ GCC_except_table6
+ GCC_except_table632
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table664
+ GCC_except_table670
+ GCC_except_table671
+ GCC_except_table672
+ GCC_except_table677
+ GCC_except_table686
+ GCC_except_table694
+ GCC_except_table703
+ GCC_except_table708
+ GCC_except_table713
+ GCC_except_table718
+ GCC_except_table724
+ GCC_except_table730
+ GCC_except_table765
+ GCC_except_table767
+ GCC_except_table772
+ GCC_except_table808
+ GCC_except_table814
+ GCC_except_table909
+ GCC_except_table910
+ _AKSEventsRegister
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDictionaryGetValueIfPresent
+ _CFGetTypeID
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EEEclB8ue170006Ev
+ __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110__pop_heapB8ue170006INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__110__pop_heapB8ue170006INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB8ue170006EPS8_
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB8ue170006EPS8_
+ __ZNSt3__117__floyd_sift_downB8ue170006INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__117__floyd_sift_downB8ue170006INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EESC_SC_EET2_RT_T0_T1_SD_
+ __ZNSt3__14pairIU8__strongP8NSStringU8__strongP8NSNumberEaSB8ue170006ERKS7_
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE7__clearB8ue170006Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB8ue170006EPS8_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ue170006Em
+ __ZNSt3__19__sift_upB8ue170006INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZNSt3__19__sift_upB8ue170006INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.1957
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1457
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1457.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1460
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1460.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1461
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1461.cold.1
+ ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1462
+ ___31-[SPCoreSpotlightIndexer start]_block_invoke.1393
+ ___35-[SPCoreSpotlightIndexer lockingCx]_block_invoke
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.1968
+ ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.1969
+ ___42-[SDLockHandler initWithDelegate:options:]_block_invoke.12
+ ___54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.185
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1589
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1599
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1613
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1644
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1648
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1652
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1681
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1858
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1859
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1866
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1870
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1871
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1875
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1879
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1898
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1600
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1672
+ ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1694
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1469
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1470
+ ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.1471
+ ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.1421
+ ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.1956
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1909
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1911
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1911.cold.1
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1912
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1913
+ ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1913.cold.1
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.1491
+ ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.1492
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1414.cold.1
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1415
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1419
+ ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1420
+ ___block_descriptor_40_e8_32s_e28_v20?0i8^{__CFDictionary=}12ls32l8
+ ___block_literal_global.1409
+ ___block_literal_global.1411
+ ___block_literal_global.1413
+ ___block_literal_global.1423
+ ___block_literal_global.1426
+ ___block_literal_global.1434
+ ___block_literal_global.1436
+ ___block_literal_global.1438
+ ___block_literal_global.1443
+ ___block_literal_global.1445
+ ___block_literal_global.1489
+ ___block_literal_global.1494
+ ___block_literal_global.1542
+ ___block_literal_global.1806
+ ___block_literal_global.1811
+ ___block_literal_global.1816
+ ___block_literal_global.1821
+ ___block_literal_global.1826
+ ___block_literal_global.184
+ ___block_literal_global.187
+ ___block_literal_global.1915
+ ___block_literal_global.1967
+ ___block_literal_global.1980
+ ___block_literal_global.2397
+ ___block_literal_global.2399
+ ___block_literal_global.2463
+ ___block_literal_global.2470
+ ___processItemsForImport_block_invoke.2417
+ __unnamed_array_storage.1376
+ __unnamed_array_storage.1391
+ __unnamed_array_storage.1963
+ __unnamed_array_storage.2404
+ __unnamed_array_storage.2408
+ __unnamed_array_storage.2460
+ _kAKSInfoCxExpired
+ _kAKSInfoCxExpiring
+ _objc_msgSend$isSearchCLIBundle:
+ _objc_msgSend$lockedCx
+ _objc_msgSend$lockingCx
+ _protectionClassIntValue
- -[SPConcreteCoreSpotlightIndexer _startInternalQueryWithIndex:query:fetchAttributes:forBundleIds:maxCount:resultsHandler:resultQueue:postFilter:].cold.1
- GCC_except_table17
- GCC_except_table19
- GCC_except_table30
- GCC_except_table32
- GCC_except_table524
- GCC_except_table533
- GCC_except_table539
- GCC_except_table563
- GCC_except_table564
- GCC_except_table572
- GCC_except_table593
- GCC_except_table629
- GCC_except_table656
- GCC_except_table660
- GCC_except_table661
- GCC_except_table667
- GCC_except_table668
- GCC_except_table669
- GCC_except_table674
- GCC_except_table680
- GCC_except_table691
- GCC_except_table7
- GCC_except_table700
- GCC_except_table705
- GCC_except_table710
- GCC_except_table715
- GCC_except_table721
- GCC_except_table727
- GCC_except_table762
- GCC_except_table764
- GCC_except_table769
- GCC_except_table805
- GCC_except_table811
- GCC_except_table906
- GCC_except_table907
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__117basic_string_viewIcNS_11char_traitsIcEEE7compareES3_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EEEclB7v160006Ev
- __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyE22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__110__pop_heapB7v160006INS_17_ClassicAlgPolicyE27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SE_RT0_NS_15iterator_traitsISE_E15difference_typeE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEERNS5_IS8_EEE17__destruct_at_endB7v160006EPS8_
- __ZNSt3__114__split_bufferINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEERNS_9allocatorIS8_EEE17__destruct_at_endB7v160006EPS8_
- __ZNSt3__117__floyd_sift_downB7v160006INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__117__floyd_sift_downB7v160006INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEET1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEfEEEENS_16reverse_iteratorIPS8_EESC_SC_EET2_RT_T0_T1_SD_
- __ZNSt3__14pairIU8__strongP8NSStringU8__strongP8NSNumberEaSB7v160006ERKS7_
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEENS5_IS8_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEENS_9allocatorIS8_EEE22__base_destruct_at_endB7v160006EPS8_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB7v160006Em
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyER22_compareTopKCandidatesNS_11__wrap_iterIPNS_4pairIU8__strongP8NSStringU8__strongP8NSNumberEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZNSt3__19__sift_upB7v160006INS_17_ClassicAlgPolicyER27_compareCorectionCandidatesNS_11__wrap_iterIPNS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEfEEEEEEvT1_SF_OT0_NS_15iterator_traitsISF_E15difference_typeE
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___107-[SPCoreSpotlightIndexer _migrateIndexExtensionsWithEnumerator:forced:migratedBundleIds:completionHandler:]_block_invoke.1951
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1449
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1451
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1451.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1454
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1454.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1455.cold.1
- ___114-[SPCoreSpotlightIndexer _taskForQueryWithQueryString:queryContext:eventHandler:resultsHandler:completionHandler:]_block_invoke.1456
- ___31-[SPCoreSpotlightIndexer start]_block_invoke.1387
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke.1962
- ___40-[SPCoreSpotlightIndexer migrateForced:]_block_invoke_2.1963
- ___54-[MDSearchableIndexService _runLibraryDeletedCommand:]_block_invoke.183
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1583
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1593
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1607
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1638
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1642
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1646
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1675
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1852
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1853
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1860
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1864
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1865
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1869
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1873
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke.1892
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1594
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1666
- ___72-[SPCoreSpotlightIndexer _issueCommand:searchContext:completionHandler:]_block_invoke_2.1688
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1463
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke.1464
- ___72-[SPCoreSpotlightIndexer reindexAllItemsWithIndexers:completionHandler:]_block_invoke_2.1465
- ___80-[SPCoreSpotlightIndexer cleanupStringsWithProtectionClasses:completionHandler:]_block_invoke.1415
- ___84-[SPCoreSpotlightIndexer _fetchAccumulatedStorageSizeForBundleId:completionHandler:]_block_invoke.1950
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1901
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1901.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1903
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1905
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1905.cold.1
- ___85-[SPCoreSpotlightIndexer performIndexerTask:withIndexExtensionsAndCompletionHandler:]_block_invoke.1906
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke.1485
- ___93-[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:]_block_invoke_2.1486
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1408
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1408.cold.1
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1409
- ___96-[SPCoreSpotlightIndexer mergeWithProtectionClasses:power:inferPriorityIndex:completionHandler:]_block_invoke.1413
- ___block_literal_global.1403
- ___block_literal_global.1405
- ___block_literal_global.1407
- ___block_literal_global.1417
- ___block_literal_global.1420
- ___block_literal_global.1428
- ___block_literal_global.1430
- ___block_literal_global.1432
- ___block_literal_global.1437
- ___block_literal_global.1439
- ___block_literal_global.1483
- ___block_literal_global.1488
- ___block_literal_global.1536
- ___block_literal_global.1800
- ___block_literal_global.1805
- ___block_literal_global.1810
- ___block_literal_global.1815
- ___block_literal_global.182
- ___block_literal_global.1820
- ___block_literal_global.185
- ___block_literal_global.1909
- ___block_literal_global.1961
- ___block_literal_global.1974
- ___block_literal_global.2388
- ___block_literal_global.2390
- ___block_literal_global.2454
- ___block_literal_global.2461
- ___processItemsForImport_block_invoke.2408
- __unnamed_array_storage.1385
- __unnamed_array_storage.1957
- __unnamed_array_storage.2395
- __unnamed_array_storage.2399
- __unnamed_array_storage.2451
- _protectinClassIntValue
CStrings:
+ "### firstUnlock == NO, can't upgrade to priority index"
+ "Class Cx index"
+ "Failed register: AKSEventsRegister"
+ "Failed to execute internal query:\"%@\", index:%p, _suspended:%s, _suspending:%s"
+ "NSFileProtectionCompleteWhenUserInactive"
+ "Received Cx expired notification"
+ "Received Cx expiring notification"
+ "Starting pathFixup query pc: %@"
+ "T@\"<CSIndexExtensionDelegate>\",?,W"
+ "T@\"NSString\",?,R,C"
+ "[LOCK] SpringBoard first unlock"
+ "[LOCK] SpringBoard unlocked: %s"
+ "isSearchCLIBundle:"
+ "locked Cx from delegate"
+ "lockedCx"
+ "locking Cx from delegate"
+ "lockingCx"
+ "priorityIndexAvailable"
+ "v20@?0i8^{__CFDictionary=}12"
- "### firstUnlock == NO, can't upgrade"
- "Failed to execute internal query:\"%@\", index:%p"
- "Staring pathFixup query pc: %@"
- "T@\"<CSIndexExtensionDelegate>\",W"
- "The index is unavailable, dataclass:%@, index:%p, suspended:%s"
- "[LOCK] Spring Board first unlock"
- "[LOCK] Spring Board unlocked: %s"
- "priortyIndexAvailable"

```
