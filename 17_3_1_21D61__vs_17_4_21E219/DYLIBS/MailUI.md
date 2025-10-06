## MailUI

> `/System/Library/PrivateFrameworks/MailUI.framework/MailUI`

```diff

-3774.400.21.0.0
-  __TEXT.__text: 0xd1854
-  __TEXT.__auth_stubs: 0x1dd0
-  __TEXT.__objc_methlist: 0x42fc
-  __TEXT.__cstring: 0x4f8a
+3774.500.171.2.2
+  __TEXT.__text: 0xcec80
+  __TEXT.__auth_stubs: 0x1d50
+  __TEXT.__objc_methlist: 0x435c
+  __TEXT.__cstring: 0x492a
   __TEXT.__const: 0x39c4
   __TEXT.__oslogstring: 0x3924
-  __TEXT.__gcc_except_tab: 0x7a0
+  __TEXT.__gcc_except_tab: 0x7b8
   __TEXT.__swift5_typeref: 0x13b6
   __TEXT.__swift5_capture: 0x694
   __TEXT.__swift5_reflstr: 0xf20

   __TEXT.__swift5_proto: 0x268
   __TEXT.__swift5_types: 0x140
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x34f0
-  __TEXT.__eh_frame: 0xf30
-  __TEXT.__objc_classname: 0xc67
-  __TEXT.__objc_methname: 0xf267
+  __TEXT.__unwind_info: 0x3234
+  __TEXT.__eh_frame: 0xd28
+  __TEXT.__objc_classname: 0xc69
+  __TEXT.__objc_methname: 0xf479
   __TEXT.__objc_methtype: 0x28bd
-  __TEXT.__objc_stubs: 0x8f60
+  __TEXT.__objc_stubs: 0x9000
   __DATA_CONST.__got: 0x630
-  __DATA_CONST.__const: 0x17d8
+  __DATA_CONST.__const: 0x17e0
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa428
-  __DATA_CONST.__objc_selrefs: 0x3300
+  __DATA_CONST.__objc_const: 0xa4e8
+  __DATA_CONST.__objc_selrefs: 0x3330
+  __DATA_CONST.__objc_protorefs: 0xe8
+  __DATA_CONST.__objc_classrefs: 0x5e0
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0x21e0
+  __AUTH_CONST.__cfstring: 0x2200
   __AUTH_CONST.__objc_const: 0x1fb8
   __AUTH_CONST.__const: 0x3490
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xef8
-  __AUTH.__objc_data: 0xc10
+  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH.__objc_data: 0xb20
   __AUTH.__data: 0x340
-  __DATA.__objc_protorefs: 0xe8
-  __DATA.__objc_classrefs: 0x5e0
-  __DATA.__objc_superrefs: 0x188
-  __DATA.__objc_ivar: 0x5a0
+  __DATA.__objc_ivar: 0x5b0
   __DATA.__data: 0x1988
-  __DATA.__bss: 0x2ca0
+  __DATA.__bss: 0x2c20
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1570
-  __DATA_DIRTY.__data: 0x1480
-  __DATA_DIRTY.__bss: 0x2300
+  __DATA_DIRTY.__objc_data: 0x1660
+  __DATA_DIRTY.__data: 0x1490
+  __DATA_DIRTY.__bss: 0x2380
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C98039EA-B144-33FE-A25E-1AAA24248FF9
-  Functions: 4637
-  Symbols:   6842
-  CStrings:  4057
+  UUID: E4609425-E9C6-36AE-B0B3-1BE2A1028E56
+  Functions: 4630
+  Symbols:   6871
+  CStrings:  4044
 
Symbols:
+ -[MessageListCellHelper isLocalMailboxSearchScope]
+ -[MessageListCellHelper isSearchResult]
+ -[MessageListCellHelper setLocalMailboxSearchScope:]
+ -[MessageListCellHelper setSearchResult:]
+ -[MessageListRecentSectionDataSource hideFollowUpUserDefaultsObserver]
+ -[MessageListRecentSectionDataSource isLocalMailboxSearchScope]
+ -[MessageListRecentSectionDataSource localMailboxSearchScopeUserDefaultsObserver]
+ -[MessageListRecentSectionDataSource setHideFollowUpUserDefaultsObserver:]
+ -[MessageListRecentSectionDataSource setLocalMailboxSearchScope:]
+ -[MessageListRecentSectionDataSource setLocalMailboxSearchScopeUserDefaultsObserver:]
+ _OBJC_IVAR_$_MessageListCellHelper._localMailboxSearchScope
+ _OBJC_IVAR_$_MessageListCellHelper._searchResult
+ _OBJC_IVAR_$_MessageListRecentSectionDataSource._hideFollowUpUserDefaultsObserver
+ _OBJC_IVAR_$_MessageListRecentSectionDataSource._localMailboxSearchScope
+ _OBJC_IVAR_$_MessageListRecentSectionDataSource._localMailboxSearchScopeUserDefaultsObserver
+ ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke.129
+ ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke_2.130
+ ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke.135
+ ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke_2.139
+ ___159-[MessageListRecentSectionDataSource initWithIdentifier:section:collectionView:listCellClass:messageList:initialLoadCompletedPromise:layoutValuesHelper:state:]_block_invoke_3
+ ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.129
+ ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.134
+ ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.134.cold.1
+ ___52-[MUISearchRankedSuggesterQuery _createTopHitsQuery]_block_invoke.88
+ ___52-[MUISearchRankedSuggesterQuery _createTopHitsQuery]_block_invoke.88.cold.1
+ ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.113
+ ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.95
+ ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.94
+ ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.102
+ ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.97
+ ___65+[MUISearchResultsSuggester(Date) suggestionResultsSortedByDate:]_block_invoke.113
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.96
+ ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.96.cold.1
+ ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.101
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.77
+ ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.80
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.144
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.144.cold.1
+ ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.148
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.146
+ ___block_literal_global.148
+ _block_copy_helper.22
+ _block_descriptor.24
+ _block_destroy_helper.23
+ _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.20
+ _kMUILocalMailboxSearchOnlyKey
+ _objc_msgSend$isLocalMailboxSearchScope
+ _objc_msgSend$isSearch
+ _objc_msgSend$isSearchResult
+ _objc_msgSend$setLocalMailboxSearchScope:
+ _objc_msgSend$setSearchResult:
+ _swift_initStackObject
- -[MessageListRecentSectionDataSource setUserDefaultsObserver:]
- -[MessageListRecentSectionDataSource userDefaultsObserver]
- _OBJC_IVAR_$_MessageListRecentSectionDataSource._userDefaultsObserver
- ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke.128
- ___100-[MessageListSectionDataSource _addedItemIDs:before:existingItemID:toThreadWithItemID:inCollection:]_block_invoke_2.129
- ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke.134
- ___108-[MessageListSectionDataSource _deleteItemsWithIDs:fromCollection:useImmediateCompletion:completionHandler:]_block_invoke_2.138
- ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.128
- ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.133
- ___40-[MUIResultSuggestionQuery _createQuery]_block_invoke.133.cold.1
- ___52-[MUISearchRankedSuggesterQuery _createTopHitsQuery]_block_invoke.87
- ___52-[MUISearchRankedSuggesterQuery _createTopHitsQuery]_block_invoke.87.cold.1
- ___62-[MessageListSectionDataSource _maybeReloadForTimedOutItemIDs]_block_invoke.112
- ___62-[MessageListSectionDataSource collection:movedItemIDs:after:]_block_invoke.94
- ___63-[MessageListSectionDataSource collection:movedItemIDs:before:]_block_invoke.93
- ___63-[MessageListSectionDataSource collectionDidFinishInitialLoad:]_block_invoke.101
- ___63-[MessageListSectionDataSource didFinishRecoveryForCollection:]_block_invoke.96
- ___65+[MUISearchResultsSuggester(Date) suggestionResultsSortedByDate:]_block_invoke.112
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.95
- ___80-[MessageListSectionDataSource collection:replacedExistingItemID:withNewItemID:]_block_invoke.95.cold.1
- ___83-[MessageListSectionDataSource collection:didFinishInitialLoadForThreadWithItemID:]_block_invoke.100
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.76
- ___87-[MessageListSectionDataSource messageListItemForItemID:indexPath:receiver:completion:]_block_invoke.78
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.143
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.143.cold.1
- ___96-[MessageListSectionDataSource _recoverFailedItemIDsIfNeededForCollection:excluding:completion:]_block_invoke.147
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.145
- ___block_literal_global.147
- _block_copy_helper.23
- _block_descriptor.25
- _block_destroy_helper.24
- _get_witness_table 10AppIntents21IntentResultContainerVys5NeverOA3EGAA0cD0HPyHC.21
CStrings:
+ "\x14"
+ "LocalMailboxSearchOnly"
+ "T@\"<EFCancelable>\",&,N,V_hideFollowUpUserDefaultsObserver"
+ "T@\"<EFCancelable>\",&,N,V_localMailboxSearchScopeUserDefaultsObserver"
+ "T@\"NSString\",?,R,C"
+ "TB,N,GisLocalMailboxSearchScope,V_localMailboxSearchScope"
+ "TB,N,GisSearchResult,V_searchResult"
+ "ZeroKeywordSearchMockData"
+ "_hideFollowUpUserDefaultsObserver"
+ "_localMailboxSearchScope"
+ "_localMailboxSearchScopeUserDefaultsObserver"
+ "_searchResult"
+ "hideFollowUpUserDefaultsObserver"
+ "isLocalMailboxSearchScope"
+ "isSearchResult"
+ "localMailboxSearchScope"
+ "localMailboxSearchScopeUserDefaultsObserver"
+ "searchResult"
+ "setHideFollowUpUserDefaultsObserver:"
+ "setLocalMailboxSearchScope:"
+ "setLocalMailboxSearchScopeUserDefaultsObserver:"
+ "setSearchResult:"
- "Attempt to copy contents into nil buffer pointer"
- "Can't unsafeBitCast between types of different sizes"
- "Division by zero"
- "Division by zero in remainder operation"
- "Division results in an overflow"
- "Division results in an overflow in remainder operation"
- "Insufficient space allocated to copy array contents"
- "Insufficient space allocated to copy string contents"
- "StaticString should have Unicode scalar representation"
- "StaticString should have pointer representation"
- "String index is out of bounds"
- "Swift/Array.swift"
- "Swift/Builtin.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"<EFCancelable>\",&,N,V_userDefaultsObserver"
- "UnsafeBufferPointer has a nil start and nonzero count"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "UnsafeRawBufferPointer with negative count"
- "_userDefaultsObserver"
- "invalid Collection: less than 'count' elements in collection"
- "invalid Collection: more than 'count' elements in collection"
- "newElements.underestimatedCount was an overestimate"
- "setUserDefaultsObserver:"
- "userDefaultsObserver"

```
