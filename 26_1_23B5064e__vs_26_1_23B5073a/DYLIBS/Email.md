## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.200.72.2.3
-  __TEXT.__text: 0xccf98
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0xc83c
-  __TEXT.__gcc_except_tab: 0x1af00
-  __TEXT.__const: 0x11b8
-  __TEXT.__cstring: 0xb49c
-  __TEXT.__oslogstring: 0x5ff3
+3864.200.81.2.5
+  __TEXT.__text: 0xce2ec
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_methlist: 0xc9ac
+  __TEXT.__gcc_except_tab: 0x1b13c
+  __TEXT.__const: 0x1238
+  __TEXT.__cstring: 0xb60c
+  __TEXT.__oslogstring: 0x6033
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
   __TEXT.__constg_swiftt: 0x3e8

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x7998
+  __TEXT.__unwind_info: 0x7a80
   __TEXT.__eh_frame: 0x1f8
-  __TEXT.__objc_classname: 0x1a1d
-  __TEXT.__objc_methname: 0x1aee1
-  __TEXT.__objc_methtype: 0x46ee
-  __TEXT.__objc_stubs: 0x11b40
-  __DATA_CONST.__got: 0xc90
-  __DATA_CONST.__const: 0x41c8
-  __DATA_CONST.__objc_classlist: 0x568
-  __DATA_CONST.__objc_catlist: 0x48
+  __TEXT.__objc_classname: 0x1a44
+  __TEXT.__objc_methname: 0x1b288
+  __TEXT.__objc_methtype: 0x4714
+  __TEXT.__objc_stubs: 0x11d40
+  __DATA_CONST.__got: 0xca0
+  __DATA_CONST.__const: 0x4270
+  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5df8
+  __DATA_CONST.__objc_selrefs: 0x5e98
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH_CONST.__auth_got: 0xa88
   __AUTH_CONST.__const: 0x1828
-  __AUTH_CONST.__cfstring: 0x9ae0
-  __AUTH_CONST.__objc_const: 0x16078
+  __AUTH_CONST.__cfstring: 0x9bc0
+  __AUTH_CONST.__objc_const: 0x16310
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x5c8
+  __AUTH.__objc_data: 0x618
   __AUTH.__data: 0x158
-  __DATA.__objc_ivar: 0xbc0
-  __DATA.__data: 0x2898
-  __DATA.__bss: 0x1b90
+  __DATA.__objc_ivar: 0xbdc
+  __DATA.__data: 0x28a8
+  __DATA.__bss: 0x1ba0
   __DATA_DIRTY.__objc_data: 0x3200
-  __DATA_DIRTY.__data: 0x1e0
-  __DATA_DIRTY.__bss: 0x860
+  __DATA_DIRTY.__data: 0x1c0
+  __DATA_DIRTY.__bss: 0x850
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 970962EE-AE92-3284-AC9C-49D9670F4827
-  Functions: 4730
-  Symbols:   17596
-  CStrings:  8356
+  UUID: F02FE483-615D-371F-A221-538E10633A8E
+  Functions: 4760
+  Symbols:   17715
+  CStrings:  8410
 
Symbols:
+ +[EMLocalSearchInfo supportsSecureCoding]
+ -[CSSearchableItem(SFMailRankingSignals) _daysSinceDate:]
+ -[CSSearchableItem(SFMailRankingSignals) em_mailRankingSignals]
+ -[EMLocalSearchInfo .cxx_destruct]
+ -[EMLocalSearchInfo description]
+ -[EMLocalSearchInfo ef_publicDescription]
+ -[EMLocalSearchInfo encodeWithCoder:]
+ -[EMLocalSearchInfo hasEmbeddingResults]
+ -[EMLocalSearchInfo hasKeywordResults]
+ -[EMLocalSearchInfo hasQueryEmbedding]
+ -[EMLocalSearchInfo initWithCoder:]
+ -[EMLocalSearchInfo initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:rankingSignalsByObjectID:]
+ -[EMLocalSearchInfo queryStatus]
+ -[EMLocalSearchInfo rankingSignalsByObjectID]
+ -[EMMessageList queryDidFailInitialLoadWithExtraInfo:]
+ -[EMMessageList queryDidFinishInitialLoadWithExtraInfo:]
+ -[EMMessageRepository messageObjectIDsForSearchIndexerIdentifiers:]
+ -[EMSearchableIndexQuery embeddingBlock]
+ -[EMSearchableIndexQuery setEmbeddingBlock:]
+ -[EMSearchableIndexTopHitsQuery _searchHasAttributedQuery:]
+ -[EMSearchableIndexTopHitsQuery embeddingHandler]
+ -[EMSearchableIndexTopHitsQuery setEmbeddingHandler:]
+ -[_EMMessageRepositoryQueryObserver observerDidFailInitialLoad:extraInfo:]
+ -[_EMMessageRepositoryQueryObserver observerDidFinishInitialLoad:extraInfo:]
+ GCC_except_table152
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table217
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table229
+ _EMMessageListExtraInfoKeyLocalSearchInfo
+ _OBJC_CLASS_$_EMLocalSearchInfo
+ _OBJC_CLASS_$_SFMailRankingSignals
+ _OBJC_IVAR_$_EMLocalSearchInfo._hasEmbeddingResults
+ _OBJC_IVAR_$_EMLocalSearchInfo._hasKeywordResults
+ _OBJC_IVAR_$_EMLocalSearchInfo._hasQueryEmbedding
+ _OBJC_IVAR_$_EMLocalSearchInfo._queryStatus
+ _OBJC_IVAR_$_EMLocalSearchInfo._rankingSignalsByObjectID
+ _OBJC_IVAR_$_EMSearchableIndexQuery._embeddingBlock
+ _OBJC_IVAR_$_EMSearchableIndexTopHitsQuery._embeddingHandler
+ _OBJC_METACLASS_$_EMLocalSearchInfo
+ __OBJC_$_CATEGORY_CSSearchableItem_$_SFMailRankingSignals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CSSearchableItem_$_SFMailRankingSignals
+ __OBJC_$_CLASS_METHODS_EMLocalSearchInfo
+ __OBJC_$_CLASS_PROP_LIST_EMLocalSearchInfo
+ __OBJC_$_INSTANCE_METHODS_EMLocalSearchInfo
+ __OBJC_$_INSTANCE_VARIABLES_EMLocalSearchInfo
+ __OBJC_$_PROP_LIST_EMLocalSearchInfo
+ __OBJC_CLASS_PROTOCOLS_$_EMLocalSearchInfo
+ __OBJC_CLASS_RO_$_EMLocalSearchInfo
+ __OBJC_METACLASS_RO_$_EMLocalSearchInfo
+ ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.102
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.513
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.513.cold.1
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.169
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.171
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.171.cold.1
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.173
+ ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.170
+ ___54-[EMMessageList queryDidFailInitialLoadWithExtraInfo:]_block_invoke
+ ___54-[EMMessageList queryDidFailInitialLoadWithExtraInfo:]_block_invoke_2
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.543
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.543.cold.1
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.522
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.525
+ ___56-[EMMessageList queryDidFinishInitialLoadWithExtraInfo:]_block_invoke
+ ___56-[EMMessageList queryDidFinishInitialLoadWithExtraInfo:]_block_invoke_2
+ ___57-[EMSearchableIndexUserQuery initWithExpression:builder:]_block_invoke.486
+ ___57-[EMSearchableIndexUserQuery initWithExpression:builder:]_block_invoke_2
+ ___58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.175
+ ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.508
+ ___62-[EMSearchableIndexTopHitsQuery _configureTopHitsSearchQuery:]_block_invoke_5
+ ___67-[EMMessageRepository messageObjectIDsForSearchIndexerIdentifiers:]_block_invoke
+ ___74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.496
+ ___76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.494
+ ___82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.487
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.249
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.252
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.254
+ ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.262
+ ___block_descriptor_40_ea8_32s_e28_"EFFuture"16?0"NSString"8ls32l8
+ ___block_descriptor_40_ea8_32w_e27_v16?0"CSAttributedQuery"8lw32l8
+ ___block_descriptor_48_ea8_32bs40w_e27_v16?0"CSAttributedQuery"8lw40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e45_"CSSearchQuery"16?0"CSSearchQueryContext"8ls32l8s40l8
+ ___block_literal_global.266
+ ___block_literal_global.505
+ ___block_literal_global.516
+ ___block_literal_global.553
+ ___block_literal_global.556
+ ___block_literal_global.558
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _log.log.79
+ _log.onceToken.80
+ _objc_msgSend$_daysSinceDate:
+ _objc_msgSend$_searchHasAttributedQuery:
+ _objc_msgSend$collectionDidFailInitialLoad:searchInfo:
+ _objc_msgSend$collectionDidFinishInitialLoad:searchInfo:
+ _objc_msgSend$em_mailRankingSignals
+ _objc_msgSend$embeddingBlock
+ _objc_msgSend$embeddingHandler
+ _objc_msgSend$hasEmbeddingResults
+ _objc_msgSend$hasKeywordResults
+ _objc_msgSend$hasQueryEmbedding
+ _objc_msgSend$isUnsafeQuery
+ _objc_msgSend$queryDidFailInitialLoadWithExtraInfo:
+ _objc_msgSend$queryDidFinishInitialLoadWithExtraInfo:
+ _objc_msgSend$queryEmbedding
+ _objc_msgSend$rankingSignalsByObjectID
+ _objc_msgSend$setAttributedQueryHandler:
+ _objc_msgSend$setEmbeddingBlock:
+ _objc_retain_x6
- -[EMSearchableIndexTopHitsQueryResult getDaysSinceTheDate:]
- -[_EMMessageRepositoryQueryObserver observerDidFinishInitialLoad:]
- GCC_except_table164
- GCC_except_table186
- GCC_except_table187
- GCC_except_table191
- GCC_except_table193
- GCC_except_table197
- GCC_except_table198
- GCC_except_table203
- GCC_except_table208
- GCC_except_table209
- GCC_except_table213
- GCC_except_table214
- GCC_except_table220
- GCC_except_table226
- ___203-[EMSearchableIndexTopHitsQuery initWithSearchString:filterQueries:bundleID:keyboardLanguage:updatedSuggestion:generateSuggestions:logDescription:resultLimit:suggestionLimit:customFlags:feedbackQueryID:]_block_invoke.109
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.507
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.507.cold.1
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.166
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.168
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.168.cold.1
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke.170
- ___54-[EMMessageList _availableMessageListItemsForItemIDs:]_block_invoke_2.167
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.537
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.537.cold.1
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.516
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.519
- ___58-[EMMessageList _attemptToFinishRetryingPromisesByItemID:]_block_invoke.172
- ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.502
- ___74-[EMMessageRepository requestRichLinkURLsForMessageIDs:completionHandler:]_block_invoke.490
- ___76-[EMMessageRepository requestAttachmentURLsForMessageIDs:completionHandler:]_block_invoke.488
- ___82-[EMMessageRepository _removeItemsFromObservedItemsCacheIfNotObservedByObservers:]_block_invoke.481
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.243
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.246
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.248
- ___86-[EMMessageRepository _messageListItemsForObjectIDs:observationIdentifier:checkCache:]_block_invoke.256
- ___block_literal_global.260
- ___block_literal_global.499
- ___block_literal_global.510
- ___block_literal_global.547
- ___block_literal_global.550
- ___block_literal_global.552
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _log.log.86
- _log.onceToken.87
- _objc_msgSend$getDaysSinceTheDate:
CStrings:
+ "%{public}@ hasQueryEmbedding: %{BOOL}d, isUnsafeQuery: %{BOOL}d"
+ "<%@ %p queryStatus: %d, hasQueryEmbedding: %@, hasKeywordResults: %@, hasEmbeddingResults: %@ rankingSignalsByObjectID.count: %lu>"
+ "@\"EFFuture\"16@?0@\"NSString\"8"
+ "@40@0:8i16B20B24B28@32"
+ "@?<v@?B>16@0:8"
+ "CSSearchableItem+SFMailRankingSignals.m"
+ "EFPropertyKey_hasEmbeddingResults"
+ "EFPropertyKey_hasKeywordResults"
+ "EFPropertyKey_hasQueryEmbedding"
+ "EFPropertyKey_queryStatus"
+ "EFPropertyKey_rankingSignalsByObjectID"
+ "EMLocalSearchInfo"
+ "T@\"NSDictionary\",R,C,N,V_rankingSignalsByObjectID"
+ "T@?,C,N,V_embeddingBlock"
+ "T@?,C,N,V_embeddingHandler"
+ "TB,R,N,V_hasEmbeddingResults"
+ "TB,R,N,V_hasKeywordResults"
+ "TB,R,N,V_hasQueryEmbedding"
+ "Ti,R,N,V_queryStatus"
+ "_daysSinceDate:"
+ "_embeddingBlock"
+ "_embeddingHandler"
+ "_hasEmbeddingResults"
+ "_hasKeywordResults"
+ "_hasQueryEmbedding"
+ "_rankingSignalsByObjectID"
+ "_searchHasAttributedQuery:"
+ "collectionDidFailInitialLoad:searchInfo:"
+ "collectionDidFinishInitialLoad:searchInfo:"
+ "em_mailRankingSignals"
+ "embeddingBlock"
+ "embeddingHandler"
+ "hasEmbeddingResults"
+ "hasKeywordResults"
+ "hasQueryEmbedding"
+ "initWithQueryStatus:hasQueryEmbedding:hasKeywordResults:hasEmbeddingResults:rankingSignalsByObjectID:"
+ "isUnsafeQuery"
+ "localSearchInfo"
+ "messageObjectIDsForSearchIndexerIdentifiers:"
+ "observerDidFailInitialLoad:extraInfo:"
+ "observerDidFinishInitialLoad:extraInfo:"
+ "queryDidFailInitialLoadWithExtraInfo:"
+ "queryDidFinishInitialLoadWithExtraInfo:"
+ "queryEmbedding"
+ "rankingSignalsByObjectID"
+ "setAttributedQueryHandler:"
+ "setEmbeddingBlock:"
+ "setEmbeddingHandler:"
+ "v16@?0@\"CSAttributedQuery\"8"
- "EMSearchableIndexTopHitsQuery.m"
- "getDaysSinceTheDate:"
- "observerDidFinishInitialLoad:"

```
