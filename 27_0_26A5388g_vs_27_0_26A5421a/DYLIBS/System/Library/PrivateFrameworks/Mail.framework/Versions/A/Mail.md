## Mail

> `/System/Library/PrivateFrameworks/Mail.framework/Versions/A/Mail`

```diff

-3897.100.8.1.1
-  __TEXT.__text: 0xa16b0c
-  __TEXT.__objc_methlist: 0x19544
-  __TEXT.__const: 0x615b9
-  __TEXT.__cstring: 0x31d89
-  __TEXT.__gcc_except_tab: 0x4c004
-  __TEXT.__oslogstring: 0x21ed9
+3901.100.1.1.11
+  __TEXT.__text: 0xa18f40
+  __TEXT.__objc_methlist: 0x1982c
+  __TEXT.__const: 0x615c9
+  __TEXT.__cstring: 0x31f49
+  __TEXT.__gcc_except_tab: 0x4c3ec
+  __TEXT.__oslogstring: 0x22139
   __TEXT.__ustring: 0x44
   __TEXT.__swift5_typeref: 0xe634
   __TEXT.__constg_swiftt: 0xbc08
-  __TEXT.__swift5_reflstr: 0xe5c0
-  __TEXT.__swift5_fieldmd: 0x13074
+  __TEXT.__swift5_reflstr: 0xe5d0
+  __TEXT.__swift5_fieldmd: 0x13080
   __TEXT.__swift5_builtin: 0xc44
   __TEXT.__swift5_assocty: 0x1b58
   __TEXT.__swift5_proto: 0x222c

   __TEXT.__swift5_capture: 0x25c7c
   __TEXT.__swift5_mpenum: 0x760
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__unwind_info: 0x1e4a0
+  __TEXT.__unwind_info: 0x1e590
   __TEXT.__eh_frame: 0x15a18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11820
-  __DATA_CONST.__objc_classlist: 0xda8
+  __DATA_CONST.__const: 0x11890
+  __DATA_CONST.__objc_classlist: 0xdb8
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x598
+  __DATA_CONST.__objc_protolist: 0x5a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xdf80
+  __DATA_CONST.__objc_selrefs: 0xe008
   __DATA_CONST.__objc_protorefs: 0x1d0
-  __DATA_CONST.__objc_superrefs: 0x830
+  __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_arraydata: 0x270
-  __DATA_CONST.__got: 0x3768
-  __AUTH_CONST.__const: 0x89c88
-  __AUTH_CONST.__cfstring: 0x1a5c0
-  __AUTH_CONST.__objc_const: 0x2ac60
+  __DATA_CONST.__got: 0x3778
+  __AUTH_CONST.__const: 0x89d28
+  __AUTH_CONST.__cfstring: 0x1a6c0
+  __AUTH_CONST.__objc_const: 0x2b308
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0xd08
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x3468
-  __AUTH.__objc_data: 0x6298
+  __AUTH.__objc_data: 0x6338
   __AUTH.__data: 0x9f70
-  __DATA.__objc_ivar: 0x15cc
-  __DATA.__data: 0xc67c
+  __DATA.__objc_ivar: 0x162c
+  __DATA.__data: 0xc6dc
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x43798
+  __DATA.__bss: 0x437a8
   __DATA.__common: 0xd7c
   __DATA_DIRTY.__objc_data: 0x25d0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x858
+  __DATA_DIRTY.__bss: 0x868
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 42520
-  Symbols:   28492
-  CStrings:  7710
+  Functions: 42584
+  Symbols:   28615
+  CStrings:  7730
 
Symbols:
+ +[MFGenerativeSearchIdentifiersCollector isIdentifiersSearchBlockRegistered]
+ +[MFGenerativeSearchIdentifiersCollector log]
+ +[MFGenerativeSearchIdentifiersCollector registerIdentifiersSearchBlock:]
+ -[MFGenerativeSearchContext .cxx_destruct]
+ -[MFGenerativeSearchContext criterion]
+ -[MFGenerativeSearchContext initWithPhrase:suggestion:criterion:limit:isTopHits:sessionID:queryID:queryLabel:]
+ -[MFGenerativeSearchContext isTopHits]
+ -[MFGenerativeSearchContext limit]
+ -[MFGenerativeSearchContext phrase]
+ -[MFGenerativeSearchContext queryID]
+ -[MFGenerativeSearchContext queryLabel]
+ -[MFGenerativeSearchContext sessionID]
+ -[MFGenerativeSearchContext suggestion]
+ -[MFGenerativeSearchIdentifiersCollector .cxx_destruct]
+ -[MFGenerativeSearchIdentifiersCollector _processIdentifiers:]
+ -[MFGenerativeSearchIdentifiersCollector bundleID]
+ -[MFGenerativeSearchIdentifiersCollector cancel]
+ -[MFGenerativeSearchIdentifiersCollector cancelled]
+ -[MFGenerativeSearchIdentifiersCollector criterion]
+ -[MFGenerativeSearchIdentifiersCollector description]
+ -[MFGenerativeSearchIdentifiersCollector gatheredFuture]
+ -[MFGenerativeSearchIdentifiersCollector gatheredPromise]
+ -[MFGenerativeSearchIdentifiersCollector initWithSearchPhrase:processor:builder:]
+ -[MFGenerativeSearchIdentifiersCollector isCancelled]
+ -[MFGenerativeSearchIdentifiersCollector logIdentifier]
+ -[MFGenerativeSearchIdentifiersCollector options]
+ -[MFGenerativeSearchIdentifiersCollector originalCriterion]
+ -[MFGenerativeSearchIdentifiersCollector processor]
+ -[MFGenerativeSearchIdentifiersCollector queryID]
+ -[MFGenerativeSearchIdentifiersCollector searchCancelable]
+ -[MFGenerativeSearchIdentifiersCollector searchPhrase]
+ -[MFGenerativeSearchIdentifiersCollector sessionID]
+ -[MFGenerativeSearchIdentifiersCollector setBundleID:]
+ -[MFGenerativeSearchIdentifiersCollector setCancelled:]
+ -[MFGenerativeSearchIdentifiersCollector setCriterion:]
+ -[MFGenerativeSearchIdentifiersCollector setGatheredPromise:]
+ -[MFGenerativeSearchIdentifiersCollector setLogIdentifier:]
+ -[MFGenerativeSearchIdentifiersCollector setOptions:]
+ -[MFGenerativeSearchIdentifiersCollector setOriginalCriterion:]
+ -[MFGenerativeSearchIdentifiersCollector setProcessor:]
+ -[MFGenerativeSearchIdentifiersCollector setQueryID:]
+ -[MFGenerativeSearchIdentifiersCollector setSearchCancelable:]
+ -[MFGenerativeSearchIdentifiersCollector setSearchPhrase:]
+ -[MFGenerativeSearchIdentifiersCollector setSessionID:]
+ -[MFGenerativeSearchIdentifiersCollector setTarget:]
+ -[MFGenerativeSearchIdentifiersCollector setUpdatedSuggestion:]
+ -[MFGenerativeSearchIdentifiersCollector start]
+ -[MFGenerativeSearchIdentifiersCollector target]
+ -[MFGenerativeSearchIdentifiersCollector updatedSuggestion]
+ -[MFLibraryStore _searchTypeForMailbox:queryLabel:]
+ -[MFLibraryStore newApproximateMatchCountAvailable:queryIdentifier:fromLibraryStoreMessageConsumer:]
+ -[MFLibraryStore setUseGenerativeAllResultsIdentifiers:]
+ -[MFLibraryStore useGenerativeAllResultsIdentifiers]
+ -[MFLibraryStoreMessageConsumer newApproximateMatchCountAvailable:queryIdentifier:]
+ -[MFUnreadCountQueryProcessor _nts_addPersistentID:mailMessageID:isRead:]
+ -[MFUnreadCountQueryProcessor _readStateByPersistentIDFromResults:]
+ GCC_except_table355
+ GCC_except_table359
+ GCC_except_table363
+ GCC_except_table370
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table388
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table407
+ GCC_except_table439
+ GCC_except_table444
+ GCC_except_table452
+ GCC_except_table465
+ GCC_except_table485
+ GCC_except_table493
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table504
+ OBJC_IVAR_$_MFGenerativeSearchContext._criterion
+ OBJC_IVAR_$_MFGenerativeSearchContext._limit
+ OBJC_IVAR_$_MFGenerativeSearchContext._phrase
+ OBJC_IVAR_$_MFGenerativeSearchContext._queryID
+ OBJC_IVAR_$_MFGenerativeSearchContext._queryLabel
+ OBJC_IVAR_$_MFGenerativeSearchContext._sessionID
+ OBJC_IVAR_$_MFGenerativeSearchContext._suggestion
+ OBJC_IVAR_$_MFGenerativeSearchContext._topHits
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._activity
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._bundleID
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._cancelled
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._criterion
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._gatheredPromise
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._logIdentifier
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._options
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._originalCriterion
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._processor
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._queryID
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._searchCancelable
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._searchPhrase
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._sessionID
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._target
+ OBJC_IVAR_$_MFGenerativeSearchIdentifiersCollector._updatedSuggestion
+ OBJC_IVAR_$_MFLibraryStore._useGenerativeAllResultsIdentifiers
+ _EMUserDefaultGenerativeSearchResultLimit
+ _MFMessageStoreApproximateMatchCountUpdatedNotification
+ _MFNotificationKeyApproximateMatchCount
+ _OBJC_CLASS_$_MFGenerativeSearchContext
+ _OBJC_CLASS_$_MFGenerativeSearchIdentifiersCollector
+ _OBJC_METACLASS_$_MFGenerativeSearchContext
+ _OBJC_METACLASS_$_MFGenerativeSearchIdentifiersCollector
+ __47-[MFGenerativeSearchIdentifiersCollector start]_block_invoke
+ __67-[MFUnreadCountQueryProcessor _readStateByPersistentIDFromResults:]_block_invoke
+ __OBJC_$_CLASS_METHODS_MFGenerativeSearchIdentifiersCollector
+ __OBJC_$_CLASS_PROP_LIST_MFGenerativeSearchIdentifiersCollector
+ __OBJC_$_INSTANCE_METHODS_MFGenerativeSearchContext
+ __OBJC_$_INSTANCE_METHODS_MFGenerativeSearchIdentifiersCollector
+ __OBJC_$_INSTANCE_VARIABLES_MFGenerativeSearchContext
+ __OBJC_$_INSTANCE_VARIABLES_MFGenerativeSearchIdentifiersCollector
+ __OBJC_$_PROP_LIST_MFGenerativeSearchContext
+ __OBJC_$_PROP_LIST_MFGenerativeSearchIdentifiersCollector
+ __OBJC_$_PROP_LIST_MFGenerativeSearchIdentifiersCollectorBuilder
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MFGenerativeSearchIdentifiersCollectorBuilder
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MFGenerativeSearchIdentifiersCollectorBuilder
+ __OBJC_$_PROTOCOL_REFS_MFGenerativeSearchIdentifiersCollectorBuilder
+ __OBJC_CLASS_PROTOCOLS_$_MFGenerativeSearchIdentifiersCollector
+ __OBJC_CLASS_RO_$_MFGenerativeSearchContext
+ __OBJC_CLASS_RO_$_MFGenerativeSearchIdentifiersCollector
+ __OBJC_LABEL_PROTOCOL_$_MFGenerativeSearchIdentifiersCollectorBuilder
+ __OBJC_METACLASS_RO_$_MFGenerativeSearchContext
+ __OBJC_METACLASS_RO_$_MFGenerativeSearchIdentifiersCollector
+ __OBJC_PROTOCOL_$_MFGenerativeSearchIdentifiersCollectorBuilder
+ ___38-[MFMessageThread searchRelevanceRank]_block_invoke
+ ___45+[MFGenerativeSearchIdentifiersCollector log]_block_invoke
+ ___47-[MFGenerativeSearchIdentifiersCollector start]_block_invoke
+ ___62-[MFGenerativeSearchIdentifiersCollector _processIdentifiers:]_block_invoke
+ ___62-[MFGenerativeSearchIdentifiersCollector _processIdentifiers:]_block_invoke_2
+ ___67-[MFUnreadCountQueryProcessor _readStateByPersistentIDFromResults:]_block_invoke
+ ___67-[MFUnreadCountQueryProcessor _readStateByPersistentIDFromResults:]_block_invoke_2
+ ___block_descriptor_32_e29_"NSNumber"16?0"MCMessage"8l
+ ___block_descriptor_32_e48_"MFSearchableIndexQueryResult"16?0"NSString"8l
+ ___block_descriptor_40_ea8_32w_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_40_ea8_32w_e35_v36?0"NSArray"8q16B24"NSError"28l
+ ___block_descriptor_92_ea8_32s40s48s56s64s72s80s_e57_v16?0"<MFGenerativeSearchIdentifiersCollectorBuilder>"8l
+ _objc_msgSend$_nts_addPersistentID:mailMessageID:isRead:
+ _objc_msgSend$_processIdentifiers:
+ _objc_msgSend$_readStateByPersistentIDFromResults:
+ _objc_msgSend$_searchTypeForMailbox:queryLabel:
+ _objc_msgSend$addResultColumn:
+ _objc_msgSend$ef_min
+ _objc_msgSend$em_userDefaults
+ _objc_msgSend$initWithPersistence:database:statisticsPersistence:downloadStatisticsPersistence:accountsProvider:hookRegistry:
+ _objc_msgSend$initWithPhrase:suggestion:criterion:limit:isTopHits:sessionID:queryID:queryLabel:
+ _objc_msgSend$isSearchBlockRegistered
+ _objc_msgSend$newApproximateMatchCountAvailable:queryIdentifier:
+ _objc_msgSend$useGenerativeAllResultsIdentifiers
+ _sIdentifiersSearchBlock
- -[MFUnreadCountQueryProcessor _nts_addPersistentID:mailMessageID:]
- -[MFUnreadCountQueryProcessor _persistentIDsInLibraryFromResults:]
- GCC_except_table353
- GCC_except_table356
- GCC_except_table360
- GCC_except_table365
- GCC_except_table372
- GCC_except_table378
- GCC_except_table383
- GCC_except_table392
- GCC_except_table400
- GCC_except_table405
- GCC_except_table413
- GCC_except_table440
- GCC_except_table445
- GCC_except_table462
- GCC_except_table484
- GCC_except_table492
- GCC_except_table498
- GCC_except_table500
- GCC_except_table503
- _OBJC_CLASS_$_EDSearchableIndexDownloadStatisticsPersistence
- __66-[MFUnreadCountQueryProcessor _persistentIDsInLibraryFromResults:]_block_invoke
- ___66-[MFUnreadCountQueryProcessor _persistentIDsInLibraryFromResults:]_block_invoke
- ___66-[MFUnreadCountQueryProcessor _persistentIDsInLibraryFromResults:]_block_invoke_2
- ___block_descriptor_40_ea8_32w_e32_v28?0"NSArray"8B16"NSError"20l
- _objc_msgSend$_nts_addPersistentID:mailMessageID:
- _objc_msgSend$_persistentIDsInLibraryFromResults:
- _objc_msgSend$initWithPersistence:database:statisticsPersistence:downloadStatisticsPersistence:hookRegistry:
CStrings:
+ "%@ Dropping result with no read state in Mail DB (search index out of sync): %{public}@"
+ "%@ Search index returned unread state for read message: %{public}@"
+ "-[MFUnreadCountQueryProcessor _readStateByPersistentIDFromResults:]"
+ "<%@ : %p> phrase=%@ suggestionTokenCount=%lu criterionCount=%lu"
+ "@\"MFSearchableIndexQueryResult\"16@?0@\"NSString\"8"
+ "@\"NSNumber\"16@?0@\"MCMessage\"8"
+ "AllResultsIdentifiers-%@"
+ "Found %lu unread message(s) in mailbox %{public}@"
+ "Generative identifiers query"
+ "GenerativeAllResultsIdentifiers"
+ "GenerativeUncappedSearch"
+ "MessageStoreApproximateMatchCountUpdated"
+ "No identifiers search block registered"
+ "[%{public}@] All-results identifiers retrieval failed: %{public}@"
+ "[%{public}@] Canceling all-results identifiers retrieval"
+ "[%{public}@] No identifiers search block registered"
+ "[%{public}@] Processing %lu all-results identifier results in batches of %lu"
+ "[%{public}@] Starting all-results identifiers retrieval phrase=%{public}@ suggestionTokenCount=%lu criterionCount=%lu"
+ "[HDB Search] allResultsIdentifiers (searchType=%{public}@ queryLabel=%{public}@)"
+ "approximateMatchCount"
+ "generativeIdentifiersQuery"
+ "v16@?0@\"<MFGenerativeSearchIdentifiersCollectorBuilder>\"8"
+ "v36@?0@\"NSArray\"8q16B24@\"NSError\"28"
- "-[MFUnreadCountQueryProcessor _persistentIDsInLibraryFromResults:]"
- "Search index returned unread state for read message: %{public}@"
- "v28@?0@\"NSArray\"8B16@\"NSError\"20"
```
