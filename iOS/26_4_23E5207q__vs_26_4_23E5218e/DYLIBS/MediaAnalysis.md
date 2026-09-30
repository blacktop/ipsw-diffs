## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-395.17.2.0.0
-  __TEXT.__text: 0x457030
-  __TEXT.__auth_stubs: 0x3f60
+395.19.1.0.0
+  __TEXT.__text: 0x458d10
+  __TEXT.__auth_stubs: 0x3fa0
   __TEXT.__delay_stubs: 0xc0
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x1d000
+  __TEXT.__objc_methlist: 0x1d258
   __TEXT.__const: 0x14c78
-  __TEXT.__gcc_except_tab: 0x5a1fc
-  __TEXT.__cstring: 0x290f3
-  __TEXT.__oslogstring: 0x29a9b
+  __TEXT.__gcc_except_tab: 0x5a400
+  __TEXT.__cstring: 0x29593
+  __TEXT.__oslogstring: 0x29ceb
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x3b8

   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x12308
+  __TEXT.__unwind_info: 0x123e8
   __TEXT.__eh_frame: 0x928
-  __TEXT.__objc_classname: 0x4558
-  __TEXT.__objc_methname: 0x3d451
-  __TEXT.__objc_methtype: 0xcfda
-  __TEXT.__objc_stubs: 0x29880
+  __TEXT.__objc_classname: 0x4588
+  __TEXT.__objc_methname: 0x3daf1
+  __TEXT.__objc_methtype: 0xd02a
+  __TEXT.__objc_stubs: 0x29e00
   __DATA_CONST.__got: 0x1d08
-  __DATA_CONST.__const: 0x6858
-  __DATA_CONST.__objc_classlist: 0x12a0
-  __DATA_CONST.__objc_catlist: 0x1b8
+  __DATA_CONST.__const: 0x6938
+  __DATA_CONST.__objc_classlist: 0x12b0
+  __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcae8
+  __DATA_CONST.__objc_selrefs: 0xcce0
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0xee0
+  __DATA_CONST.__objc_superrefs: 0xee8
   __DATA_CONST.__objc_arraydata: 0x11e0
-  __AUTH_CONST.__auth_got: 0x1fe0
+  __AUTH_CONST.__auth_got: 0x2000
   __AUTH_CONST.__const: 0x5948
-  __AUTH_CONST.__cfstring: 0x18120
-  __AUTH_CONST.__objc_const: 0x38650
+  __AUTH_CONST.__cfstring: 0x18400
+  __AUTH_CONST.__objc_const: 0x389c0
   __AUTH_CONST.__objc_floatobj: 0x290
   __AUTH_CONST.__objc_doubleobj: 0x480
-  __AUTH_CONST.__objc_intobj: 0x2f10
+  __AUTH_CONST.__objc_intobj: 0x2f28
   __AUTH_CONST.__objc_arrayobj: 0xc18
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x1fd0
+  __AUTH.__objc_data: 0x2070
   __AUTH.__data: 0x1d8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x3290
+  __DATA.__objc_ivar: 0x32b0
   __DATA.__data: 0x1b9c
   __DATA.__bss: 0xe89
   __DATA.__common: 0x3c1

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E1B51EA5-CFCC-3819-8237-C308330C96DE
-  Functions: 17181
-  Symbols:   58184
-  CStrings:  22188
+  UUID: DDDEF115-68E0-3990-8F2F-3A9935CC0478
+  Functions: 17233
+  Symbols:   58384
+  CStrings:  22337
 
Symbols:
+ +[MADFetchRequest(ResultTables) allResultEntityNames]
+ +[MADManagedPhotosResult(CoreDataProperties) entityName]
+ +[MADPersistentHistoryStats fetchEarliestTransactionDateFromDatabase:intoStats:]
+ +[MADPersistentHistoryStats fetchPageCountsOfPersistentHistoryTablesFromDatabase:intoStats:]
+ +[MADPersistentHistoryStats fetchTotalPageCountFromDatabase:intoStats:]
+ +[MADPersistentHistoryStats fetchTransactionCountFromDatabase:intoStats:]
+ +[MADPersistentHistoryStats fetchUnusedPageCountFromDatabase:intoStats:]
+ +[MADPersistentHistoryStats pageSize]
+ +[MADPersistentHistoryStats statsFromDatabase:]
+ +[MADSQLiteDatabase _openSQLiteDatabaseAtPath:]
+ +[MADSQLiteDatabase openDatabaseAtPath:]
+ +[PHTextUnderstandingIdentificationDocument(MediaAnalysis) mad_shortNameForKind:]
+ -[MADFetchRequest(Asset) fetchTotalAssetCount]
+ -[MADFetchRequest(ResultTables) _fetchCountForFetchRequestWithEntityName:]
+ -[MADFetchRequest(ResultTables) fetchTotalResultCount]
+ -[MADPersistentHistoryStats .cxx_destruct]
+ -[MADPersistentHistoryStats _pageCountAsPercentOfFile:]
+ -[MADPersistentHistoryStats changesPageCountPercent]
+ -[MADPersistentHistoryStats changesPageCount]
+ -[MADPersistentHistoryStats daysSinceEarliestTransaction]
+ -[MADPersistentHistoryStats earliestTransactionDate]
+ -[MADPersistentHistoryStats filePageCount]
+ -[MADPersistentHistoryStats payloadPageCount]
+ -[MADPersistentHistoryStats persistentHistoryPageCountPercent]
+ -[MADPersistentHistoryStats persistentHistoryPageCount]
+ -[MADPersistentHistoryStats setChangesPageCount:]
+ -[MADPersistentHistoryStats setEarliestTransactionDate:]
+ -[MADPersistentHistoryStats setFilePageCount:]
+ -[MADPersistentHistoryStats setTransactionCount:]
+ -[MADPersistentHistoryStats setTransactionStringsPageCount:]
+ -[MADPersistentHistoryStats setTransactionsPageCount:]
+ -[MADPersistentHistoryStats setUnusedPageCount:]
+ -[MADPersistentHistoryStats transactionCount]
+ -[MADPersistentHistoryStats transactionStringsPageCountPercent]
+ -[MADPersistentHistoryStats transactionStringsPageCount]
+ -[MADPersistentHistoryStats transactionsPageCountPercent]
+ -[MADPersistentHistoryStats transactionsPageCount]
+ -[MADPersistentHistoryStats unusedPageCount]
+ -[MADSQLiteDatabase _prepareStatement:]
+ -[MADSQLiteDatabase close]
+ -[MADSQLiteDatabase dealloc]
+ -[MADSQLiteDatabase initWithOpenedSQLite3Database:]
+ -[MADSQLiteDatabase prepareQueryStatement:stepThroughResultsWithBlock:]
+ -[PHTextUnderstandingIdentificationDocument(MediaAnalysis) mad_descriptionWithPrefix:]
+ _OBJC_CLASS_$_MADPersistentHistoryStats
+ _OBJC_CLASS_$_MADSQLiteDatabase
+ _OBJC_CLASS_$_PHTextUnderstandingIdentificationDocument
+ _OBJC_IVAR_$_MADPersistentHistoryStats._changesPageCount
+ _OBJC_IVAR_$_MADPersistentHistoryStats._earliestTransactionDate
+ _OBJC_IVAR_$_MADPersistentHistoryStats._filePageCount
+ _OBJC_IVAR_$_MADPersistentHistoryStats._transactionCount
+ _OBJC_IVAR_$_MADPersistentHistoryStats._transactionStringsPageCount
+ _OBJC_IVAR_$_MADPersistentHistoryStats._transactionsPageCount
+ _OBJC_IVAR_$_MADPersistentHistoryStats._unusedPageCount
+ _OBJC_IVAR_$_MADSQLiteDatabase._database
+ _OBJC_METACLASS_$_MADPersistentHistoryStats
+ _OBJC_METACLASS_$_MADSQLiteDatabase
+ _VCPAnalyticsFieldAssetCount
+ _VCPAnalyticsFieldDatabaseSizeExcludingPersistentHistory
+ _VCPAnalyticsFieldPersistentHistoryCount
+ _VCPAnalyticsFieldPersistentHistoryPercentage
+ _VCPAnalyticsFieldResultCount
+ __OBJC_$_CATEGORY_CLASS_METHODS_PHTextUnderstandingIdentificationDocument_$_MediaAnalysis
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PHTextUnderstandingIdentificationDocument_$_MediaAnalysis
+ __OBJC_$_CATEGORY_PHTextUnderstandingIdentificationDocument_$_MediaAnalysis
+ __OBJC_$_CLASS_METHODS_MADFetchRequest(Asset|MomentsScheduledAsset|BackgroundAnalysisProgressHistory|KeyValueStore|ProcessingStatus|ChangeToken|ResultTables)
+ __OBJC_$_CLASS_METHODS_MADPersistentHistoryStats
+ __OBJC_$_CLASS_METHODS_MADSQLiteDatabase
+ __OBJC_$_CLASS_PROP_LIST_MADPersistentHistoryStats
+ __OBJC_$_INSTANCE_METHODS_MADFetchRequest(Asset|MomentsScheduledAsset|BackgroundAnalysisProgressHistory|KeyValueStore|ProcessingStatus|ChangeToken|ResultTables)
+ __OBJC_$_INSTANCE_METHODS_MADPersistentHistoryStats
+ __OBJC_$_INSTANCE_METHODS_MADSQLiteDatabase
+ __OBJC_$_INSTANCE_VARIABLES_MADPersistentHistoryStats
+ __OBJC_$_INSTANCE_VARIABLES_MADSQLiteDatabase
+ __OBJC_$_PROP_LIST_MADPersistentHistoryStats
+ __OBJC_CLASS_RO_$_MADPersistentHistoryStats
+ __OBJC_CLASS_RO_$_MADSQLiteDatabase
+ __OBJC_METACLASS_RO_$_MADPersistentHistoryStats
+ __OBJC_METACLASS_RO_$_MADSQLiteDatabase
+ ___35-[VCPMADCoreAnalyticsManager flush]_block_invoke.237
+ ___71+[MADPersistentHistoryStats fetchTotalPageCountFromDatabase:intoStats:]_block_invoke
+ ___72+[MADPersistentHistoryStats fetchUnusedPageCountFromDatabase:intoStats:]_block_invoke
+ ___73+[MADPersistentHistoryStats fetchTransactionCountFromDatabase:intoStats:]_block_invoke
+ ___74-[MADFetchRequest(ResultTables) _fetchCountForFetchRequestWithEntityName:]_block_invoke
+ ___80+[MADPersistentHistoryStats fetchEarliestTransactionDateFromDatabase:intoStats:]_block_invoke
+ ___92+[MADPersistentHistoryStats fetchPageCountsOfPersistentHistoryTablesFromDatabase:intoStats:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e27_v24?0^{sqlite3_stmt=}8^B16ls32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8s40l8r56l8
+ ___block_literal_global.231
+ _objc_msgSend$_fetchCountForFetchRequestWithEntityName:
+ _objc_msgSend$_openSQLiteDatabaseAtPath:
+ _objc_msgSend$_pageCountAsPercentOfFile:
+ _objc_msgSend$_prepareStatement:
+ _objc_msgSend$allResultEntityNames
+ _objc_msgSend$cardCategory
+ _objc_msgSend$cardGroupNumber
+ _objc_msgSend$cardNumber
+ _objc_msgSend$cardProvider
+ _objc_msgSend$cardRestrictions
+ _objc_msgSend$cardType
+ _objc_msgSend$country
+ _objc_msgSend$dateOfBirth
+ _objc_msgSend$emailAddress
+ _objc_msgSend$entityName
+ _objc_msgSend$expirationDate
+ _objc_msgSend$extractionVersion
+ _objc_msgSend$fetchEarliestTransactionDateFromDatabase:intoStats:
+ _objc_msgSend$fetchPageCountsOfPersistentHistoryTablesFromDatabase:intoStats:
+ _objc_msgSend$fetchTotalPageCountFromDatabase:intoStats:
+ _objc_msgSend$fetchTransactionCountFromDatabase:intoStats:
+ _objc_msgSend$fetchUnusedPageCountFromDatabase:intoStats:
+ _objc_msgSend$initWithOpenedSQLite3Database:
+ _objc_msgSend$issueDate
+ _objc_msgSend$issuedBy
+ _objc_msgSend$kind
+ _objc_msgSend$mad_shortNameForKind:
+ _objc_msgSend$organizationHours
+ _objc_msgSend$organizationName
+ _objc_msgSend$persistentHistoryPageCount
+ _objc_msgSend$phoneNumber
+ _objc_msgSend$placeOfBirth
+ _objc_msgSend$postalAddress
+ _objc_msgSend$prepareQueryStatement:stepThroughResultsWithBlock:
+ _objc_msgSend$region
+ _objc_msgSend$setChangesPageCount:
+ _objc_msgSend$setEarliestTransactionDate:
+ _objc_msgSend$setFilePageCount:
+ _objc_msgSend$setTransactionCount:
+ _objc_msgSend$setTransactionStringsPageCount:
+ _objc_msgSend$setTransactionsPageCount:
+ _objc_msgSend$setUnusedPageCount:
+ _objc_msgSend$sex
+ _objc_msgSend$urlAddress
+ _sqlite3_errmsg
+ _sqlite3_errstr
+ _sqlite3_exec
+ _sqlite3_open_v2
- __OBJC_$_CLASS_METHODS_MADFetchRequest(Asset|MomentsScheduledAsset|BackgroundAnalysisProgressHistory|KeyValueStore|ProcessingStatus|ChangeToken)
- __OBJC_$_INSTANCE_METHODS_MADFetchRequest(Asset|MomentsScheduledAsset|BackgroundAnalysisProgressHistory|KeyValueStore|ProcessingStatus|ChangeToken)
- ___35-[VCPMADCoreAnalyticsManager flush]_block_invoke.225
- ___block_literal_global.219
CStrings:
+ "%@kind: %@\n%@name: %@\n%@emailAddress: %@\n%@phoneNumber: %@\n%@postalAddress: %@\n%@urlAddress: %@\n%@dateOfBirth: %@\n%@placeOfBirth: %@\n%@sex: %@\n%@organizationName: %@\n%@organizationHours: %@\n%@cardType: %@\n%@cardProvider: %@\n%@cardNumber: %@\n%@cardGroupNumber: %@\n%@issueDate: %@\n%@expirationDate: %@\n%@issuedBy: %@\n%@region: %@\n%@country: %@\n%@cardCategory: %@\n%@cardRestrictions: %@\n%@extractionVersion: %@\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CI63ugCAV5-_PzHSjVUwM4162LzqOB6MrLLMr2E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRlugBJDH3GSt75hvoPnJtPl6iI1qNyiEn3R0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/bpe_model.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/filesystem.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/mmap.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_factory.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_interface.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/model_interface.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/normalizer.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/unigram_model.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/util.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/src/util.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/Library/Caches/com.apple.xbs/56300B45-F87D-47EC-AEB8-C52440520C28/TemporaryDirectory.M5cqHl/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/AdaptiveSegmentAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/AudioAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/AudioClassifier.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/AudioVideoEmbeddingFuser.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/BlurAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsBodyDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerMPS.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlock.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockBinary.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockGPU.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockScalar.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockVector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNData.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNDataGPU.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorMPS.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFastGestureRecognition.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFlattenBlock.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlock.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockGPU.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockScalar.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNGazeAnalysis.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetectorEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNHandsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNMLEnhancerEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspressoV2.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNModel.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2Data.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPersonDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPersonKeypointsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorV2.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPetsKeypointsDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlock.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockGPU.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockVector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimator.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorMPS.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorMPS.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CNNVisionCore.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CVUtilities.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CameraMotionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CameraMotionSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CommSafety/MADVideoSessionSafetyClassificationTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/CommSafety/VCPMADImageSafetyClassificationTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Convexhull.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/DatabaseReader.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/DescriptorAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/DescriptorSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EdgeDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EffectsAnalyzer.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EmbeddingSummarizationAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeStats.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE1.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE2.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsHW.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsSW.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ExifAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Frame.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/FreeFormSearch.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/FullVideoAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/GaborFilter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Histogram.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/HomeKitMotionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/HoughTransform.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Human.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageBackboneAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageBlurAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageCaptionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageCompositionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageConverter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptor.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptorWrapper.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageExposureAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageExposurePreAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageFaceDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageFaceExpressionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageFaceQualityAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHandsAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHumanActionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerHolistic.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerTopDown.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageLivePhotoBlurAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageMotionFlowAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImagePetsAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImagePetsKeypointsAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageQualityAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerBinary.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFull.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFullEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/InterAssetAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/InterestingnessAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/IrisAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/JunkAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LandmarkDetector.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LandmarkValidator.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LightMotionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LightVideoAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LivePhotoKeyFrameAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/LoudnessAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MADImageASTCFormatReader.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MADMovieBlastDoorAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MADVectorDatabase.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MatrixOperationsForFace.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MediaAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MetaTrackDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFieldAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPBackwarp.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPCorrelation.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowFeatureExtractor.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowUtils.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPMoFlowSingleEspresso.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPModelR2D2.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlowAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionFlowSubtleMotionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MotionSearch.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MovieAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MovieCurationAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MovieHighlightAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MovingObjectAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/MovingObjectSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/NSDictionary+MediaAnalysis.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Object.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ObjectDetection.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ObjectTracking.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ObstructionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PHAssetResourceManager+MediaAnalysis.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ParallaxAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PhotoAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/Face/VCPMADPersonIdentificationTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceCropManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceProcessingVersionManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceUtils.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisURLProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosAutoCounterWorker.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosFace.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceDetectionManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceIdentificationManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosSceneprintAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPSceneProcessingImageManager.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPVideoStabilizationAssetProcessingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADChangeRequest+PersistentHistory.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADChangeRequest+ProcessingStatus.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADFetchRequest+BackgroundAnalysisProgressHistory.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADManagedProcessingStatus.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PnPSolver.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/PreEncodeAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/QualityAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/RotationAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/RotationSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Rotator.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Scaler.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SceneAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SceneChangeAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Segment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Service/MADPersonalizedEmbeddingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Service/VCPMADServiceImageAsset.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SettlingEffectAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/ShapeModel.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SlowMotionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SmartStyleMetaAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SongDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/StillImageMetaAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/TensorModel.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingCalibration.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingSafety.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThreshold.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/TextEncoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/TrackSegment.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/TrackingAnalysis.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/Transforms.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPAnalysisProgressQuery.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPColorNormalizationAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPContentAnalysis.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPDownloadManager.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPFrameAnalysisStats.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPInternetReachability.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPMovieAssetWriter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPPoolBasedPixelBufferCreator.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImage.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImageLoader.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPPriorityAnalysis.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPRTLandmarkDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptor.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptorWrapper.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPSimpleMovieAssetWriter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPTimeMeasurement.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPURLAsset.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPVideoEmbeddings.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VCPWallpaperAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VanishingPointDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoActivityAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoActivityDescriptor.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoAnalysisCommon.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoAnimalDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNActionClassifier.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAutoplay.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNBackbone.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNCameraMotion.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNHighlight.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCNNQuality.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionEncoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoFaceMeshAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseFilter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoFullFaceDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoGlobalAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoGyroStabilizer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoHumanActionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoInterpolator.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrame.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrameAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoLightFaceDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFaceAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFocusAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaLivePhotoMetaAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaMotionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaOrientationAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoMetaSegmentAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoObjectTracker.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoPersonDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoPetsActionAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoPetsAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoPixelStabilizer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoRanker.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoSafetyClassifier.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoSaliencyAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoSceneClassifier.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoStabilizer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoTrackStandardDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSubsamplingDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSyncDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VideoTransformerBackbone.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceTranscoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceWriter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEVCAlphaSequenceWriter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADPNGAlphaSequenceWriter.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADVideoRemoveBackgroundCropTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageCaptionTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageEmbeddingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLEnhancementTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLScalingTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIDocumentRecognitionTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIFaceTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIMachineReadableCodeDetectionTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIRectangleDetectionTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVISceneClassificationTask.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VoiceDetector.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/VoiceDetectorV2.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/MediaAnalysis/WatchFaceAnalyzer.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/MovieCurationResults.m"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPCaptureAnalysisSession.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPCoreMLFeatureProviderGestureVideo.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureClassifier.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureImageRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureMitigator.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureVideoRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseImageRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseVideoRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseEspressoSession.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseImageRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseVideoRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPMotionFlowRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPPetsPoseImageRequest.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessor.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessorSession.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/VideoProcessing/VCPVideoSyncFrameDecoder.mm"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/MediaAnalysis/Image/MAImageAnalysisRequest.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/MediaAnalysis/MAComputeRequest.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAAssetByteStream.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAMovieAnalysisRequest.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/Proto/MAImageComputeResult+CFDictionary.cpp"
+ "/Library/Caches/com.apple.xbs/C9EEDCF9-F38F-432A-9B2E-BDC4D323AFD2/TemporaryDirectory.XngAkN/Sources/MediaAnalysis/iCloud/Proto/VCPProtoImageHumanPoseResult+CFDictionary.cpp"
+ "@24@0:8^{sqlite3=}16"
+ "ACHANGE"
+ "ATRANSACTION"
+ "ATRANSACTIONSTRING"
+ "BusinessCard"
+ "DatabaseSizeExcludingPersistentHistory"
+ "DriverLicense"
+ "EmployeeCard"
+ "Failed to close database: %s (%d)."
+ "Failed to enable WAL - %d %s"
+ "Failed to open DB - %d"
+ "Failed to prepare \"%@\": %s (%d)"
+ "Failed to step statement: %s (%d)"
+ "GreenCard"
+ "InsuranceCard"
+ "MADPersistentHistoryStats"
+ "MADSQLiteDatabase"
+ "MedicalCard"
+ "MembershipCard"
+ "NationalID"
+ "PRAGMA freelist_count;"
+ "PRAGMA journal_mode = WAL"
+ "PRAGMA page_count;"
+ "Passport"
+ "PersistentHistoryCount"
+ "PersistentHistoryPercentage"
+ "PhotosIDExtraction"
+ "ResultCount"
+ "ResultTables"
+ "SELECT COUNT(*) from ATRANSACTION;"
+ "SELECT ZTIMESTAMP  FROM ATRANSACTION  ORDER BY ZTIMESTAMP ASC  LIMIT 1;"
+ "SELECT m.tbl_name tbl_name, sum(pageno) page_count  FROM   dbstat d, sqlite_master m  WHERE     d.name = m.name     AND m.tbl_name IN ('ACHANGE', 'ATRANSACTION', 'ATRANSACTIONSTRING')     AND d.aggregate = TRUE  GROUP BY m.tbl_name;"
+ "SocialSecurityNumber"
+ "Spotlight"
+ "StateID"
+ "StudentCard"
+ "T@\"NSDate\",C,N,V_earliestTransactionDate"
+ "Tq,N,V_changesPageCount"
+ "Tq,N,V_filePageCount"
+ "Tq,N,V_transactionCount"
+ "Tq,N,V_transactionStringsPageCount"
+ "Tq,N,V_transactionsPageCount"
+ "Tq,N,V_unusedPageCount"
+ "TransitCard"
+ "[MACD|%@] Failed to fetch count: %@"
+ "[MADPersistentHistoryStats] Failed to fetch earliest transaction date"
+ "[MADPersistentHistoryStats] Failed to fetch page counts of persistent history tables"
+ "[MADPersistentHistoryStats] Failed to fetch total page count"
+ "[MADPersistentHistoryStats] Failed to fetch transaction count"
+ "[MADPersistentHistoryStats] Failed to fetch unused page count"
+ "[MADPersistentHistoryStats] No valid database (%@) or stats (%@)"
+ "^{sqlite3=}24@0:8r*16"
+ "^{sqlite3_stmt=}24@0:8@16"
+ "_changesPageCount"
+ "_earliestTransactionDate"
+ "_fetchCountForFetchRequestWithEntityName:"
+ "_filePageCount"
+ "_openSQLiteDatabaseAtPath:"
+ "_pageCountAsPercentOfFile:"
+ "_prepareStatement:"
+ "_transactionCount"
+ "_transactionStringsPageCount"
+ "_transactionsPageCount"
+ "_unusedPageCount"
+ "allResultEntityNames"
+ "cardCategory"
+ "cardGroupNumber"
+ "cardNumber"
+ "cardProvider"
+ "cardRestrictions"
+ "cardType"
+ "changesPageCount"
+ "changesPageCountPercent"
+ "country"
+ "d24@0:8q16"
+ "dateOfBirth"
+ "daysSinceEarliestTransaction"
+ "earliestTransactionDate"
+ "emailAddress"
+ "entityName"
+ "expirationDate"
+ "extractionVersion"
+ "fetchEarliestTransactionDateFromDatabase:intoStats:"
+ "fetchPageCountsOfPersistentHistoryTablesFromDatabase:intoStats:"
+ "fetchTotalAssetCount"
+ "fetchTotalPageCountFromDatabase:intoStats:"
+ "fetchTotalResultCount"
+ "fetchTransactionCountFromDatabase:intoStats:"
+ "fetchUnusedPageCountFromDatabase:intoStats:"
+ "filePageCount"
+ "initWithOpenedSQLite3Database:"
+ "issueDate"
+ "issuedBy"
+ "kind"
+ "mad_descriptionWithPrefix:"
+ "mad_shortNameForKind:"
+ "openDatabaseAtPath:"
+ "organizationHours"
+ "organizationName"
+ "pageSize"
+ "payloadPageCount"
+ "persistentHistoryPageCount"
+ "persistentHistoryPageCountPercent"
+ "phoneNumber"
+ "placeOfBirth"
+ "postalAddress"
+ "prepareQueryStatement:stepThroughResultsWithBlock:"
+ "region"
+ "setChangesPageCount:"
+ "setEarliestTransactionDate:"
+ "setFilePageCount:"
+ "setTransactionCount:"
+ "setTransactionStringsPageCount:"
+ "setTransactionsPageCount:"
+ "setUnusedPageCount:"
+ "sex"
+ "statsFromDatabase:"
+ "transactionCount"
+ "transactionStringsPageCount"
+ "transactionStringsPageCountPercent"
+ "transactionsPageCount"
+ "transactionsPageCountPercent"
+ "unusedPageCount"
+ "urlAddress"
+ "v24@?0^{sqlite3_stmt=}8^B16"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CHoJugBqlT7SMJpMwMp5lNUARVYDGofuKEixb6M/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CInYugBPKS_107SJp7WfIZyKyO6BIkJk8sA9BDs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/AdaptiveSegmentAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/AudioAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/AudioClassifier.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/AudioVideoEmbeddingFuser.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/BlurAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsBodyDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNANSTHandsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNBlurAnalyzerMPS.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlock.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockBinary.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockGPU.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockScalar.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNConvBlockVector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNData.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNDataGPU.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFaceLandmarkDetectorMPS.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFastGestureRecognition.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFlattenBlock.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlock.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockGPU.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNFullConnectionBlockScalar.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNGazeAnalysis.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNHandKeypointsDetectorEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNHandsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNMLEnhancerEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNMLScalerEspressoV2.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNModel.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNModelEspressoV2Data.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPersonDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPersonKeypointsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPetsDetectorV2.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPetsKeypointsDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlock.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockGPU.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoolingBlockVector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimator.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNPoseEstimatorMPS.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNSmileDetectorMPS.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CNNVisionCore.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CVUtilities.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CameraMotionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CameraMotionSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CommSafety/MADVideoSessionSafetyClassificationTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/CommSafety/VCPMADImageSafetyClassificationTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Convexhull.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/DatabaseReader.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/DescriptorAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/DescriptorSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EdgeDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EffectsAnalyzer.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EmbeddingSummarizationAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeStats.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE1.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsAVE2.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsHW.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/EncodeStatsSW.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ExifAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/FineSubjectMotionSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Frame.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/FreeFormSearch.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/FullVideoAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/GaborFilter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Histogram.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/HomeKitMotionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/HoughTransform.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Human.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageBackboneAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageBlurAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageCaptionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageCompositionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageConverter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptor.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageDescriptorWrapper.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageExposureAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageExposurePreAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageFaceDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageFaceExpressionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageFaceQualityAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHandsAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHumanActionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerHolistic.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageHumanPoseAnalyzerTopDown.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageLivePhotoBlurAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageMotionFlowAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImagePetsAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImagePetsKeypointsAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageQualityAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerBinary.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFull.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ImageSaliencyAnalyzerFullEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/InterAssetAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/InterestingnessAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/IrisAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/JunkAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LandmarkDetector.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LandmarkValidator.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LightMotionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LightVideoAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LivePhotoKeyFrameAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/LoudnessAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MADImageASTCFormatReader.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MADMovieBlastDoorAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MADVectorDatabase.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MatrixOperationsForFace.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MediaAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MetaTrackDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFieldAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPBackwarp.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPCorrelation.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowFeatureExtractor.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPFlowUtils.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPMoFlowSingleEspresso.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlow/VCPModelR2D2.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlowAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionFlowSubtleMotionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MotionSearch.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MovieAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MovieCurationAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MovieHighlightAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MovingObjectAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/MovingObjectSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/NSDictionary+MediaAnalysis.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Object.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ObjectDetection.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ObjectTracking.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ObstructionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PHAssetResourceManager+MediaAnalysis.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ParallaxAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PhotoAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/Face/VCPMADPersonIdentificationTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceCropManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceProcessingVersionManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFaceUtils.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPFullAnalysisURLProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosAutoCounterWorker.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosFace.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceDetectionManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosQuickFaceIdentificationManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPPhotosSceneprintAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPSceneProcessingImageManager.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Photos/VCPVideoStabilizationAssetProcessingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADChangeRequest+PersistentHistory.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADChangeRequest+ProcessingStatus.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADFetchRequest+BackgroundAnalysisProgressHistory.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PhotosDataStore/MADManagedProcessingStatus.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PnPSolver.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/PreEncodeAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/QualityAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/RotationAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/RotationSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Rotator.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Scaler.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SceneAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SceneChangeAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Segment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Service/MADPersonalizedEmbeddingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Service/VCPMADServiceImageAsset.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SettlingEffectAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/ShapeModel.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SlowMotionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SmartStyleMetaAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SongDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/StillImageMetaAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SubjectMotionSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/SubtleMotionSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/TensorModel.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingCalibration.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingSafety.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Text/MADTextEmbeddingThreshold.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/TextEncoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/TrackSegment.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/TrackingAnalysis.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/Transforms.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPAnalysisProgressQuery.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPColorNormalizationAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPContentAnalysis.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPDownloadManager.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPFrameAnalysisStats.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPInternetReachability.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPMovieAssetWriter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPPoolBasedPixelBufferCreator.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImage.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalysisImageLoader.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPPreAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPPriorityAnalysis.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPRTLandmarkDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptor.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPSceneprintDescriptorWrapper.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPSimpleMovieAssetWriter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPTimeMeasurement.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPURLAsset.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPVideoEmbeddings.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VCPWallpaperAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VanishingPointDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoActivityAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoActivityDescriptor.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoAnalysisCommon.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoAnimalDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNActionClassifier.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNAutoplay.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNBackbone.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNCameraMotion.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNHighlight.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCNNQuality.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoCaptionEncoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoFaceMeshAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoFacePoseFilter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoFullFaceDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoGlobalAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoGyroStabilizer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoHumanActionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoInterpolator.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrame.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoKeyFrameAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoLightFaceDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFaceAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaFocusAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaLivePhotoMetaAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaMotionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaOrientationAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoMetaSegmentAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoObjectTracker.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoPersonDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoPetsActionAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoPetsAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoPixelStabilizer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoRanker.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoSafetyClassifier.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoSaliencyAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoSceneClassifier.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoStabilizer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoTrackStandardDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSubsamplingDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoTrackSyncDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VideoTransformerBackbone.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceTranscoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEICSAlphaSequenceWriter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADHEVCAlphaSequenceWriter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADPNGAlphaSequenceWriter.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/MADVideoRemoveBackgroundCropTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageCaptionTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADImageEmbeddingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLEnhancementTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADMLScalingTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIDocumentRecognitionTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIFaceTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIMachineReadableCodeDetectionTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVIRectangleDetectionTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VisualIntelligence/VCPMADVISceneClassificationTask.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VoiceDetector.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/VoiceDetectorV2.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/MediaAnalysis/WatchFaceAnalyzer.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/MovieCurationResults.m"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPCaptureAnalysisSession.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPCoreMLFeatureProviderGestureVideo.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureClassifier.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureImageRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureMitigator.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandGestureVideoRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseImageRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHandPoseVideoRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseEspressoSession.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseImageRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPHumanPoseVideoRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPMotionFlowRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPPetsPoseImageRequest.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessor.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPVideoProcessorSession.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/VideoProcessing/VCPVideoSyncFrameDecoder.mm"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/MediaAnalysis/Image/MAImageAnalysisRequest.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/MediaAnalysis/MAComputeRequest.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAAssetByteStream.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/MediaAnalysis/Movie/MAMovieAnalysisRequest.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/Proto/MAImageComputeResult+CFDictionary.cpp"
- "/Library/Caches/com.apple.xbs/52766C88-BEAF-494A-A697-400A2496FB5E/TemporaryDirectory.3hHKOz/Sources/MediaAnalysis/iCloud/Proto/VCPProtoImageHumanPoseResult+CFDictionary.cpp"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/bpe_model.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/filesystem.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/mmap.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_factory.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/model_interface.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/normalizer.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/unigram_model.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/src/util.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1106: exception: failed to insert key: negative value"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1108: exception: failed to insert key: zero-length key"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1122: exception: failed to insert key: invalid null character"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: wrong key order"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1339: exception: failed to modify unit: too large offset"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1675: exception: failed to build double-array: invalid null character"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1677: exception: failed to build double-array: negative value"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:1692: exception: failed to build double-array: wrong key order"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:743: exception: failed to resize pool: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/darts_clone/darts.h:859: exception: failed to build rank index: std::bad_alloc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/Library/Caches/com.apple.xbs/FCCC2C4A-33F8-4DE7-AA59-0DD53EE1052A/TemporaryDirectory.QSYWY5/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"

```
