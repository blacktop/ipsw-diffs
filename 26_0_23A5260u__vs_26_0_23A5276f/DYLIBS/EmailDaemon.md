## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3853.100.6.2.6
-  __TEXT.__text: 0x26774c
-  __TEXT.__auth_stubs: 0x27a0
-  __TEXT.__objc_methlist: 0x160a4
-  __TEXT.__const: 0x1f0c
-  __TEXT.__gcc_except_tab: 0x4f618
-  __TEXT.__cstring: 0x22977
-  __TEXT.__oslogstring: 0x19914
-  __TEXT.__dlopen_cstrs: 0x3bc
+3856.100.4.0.0
+  __TEXT.__text: 0x26c384
+  __TEXT.__auth_stubs: 0x27b0
+  __TEXT.__objc_methlist: 0x162ac
+  __TEXT.__const: 0x1f1c
+  __TEXT.__gcc_except_tab: 0x500b0
+  __TEXT.__cstring: 0x22b47
+  __TEXT.__oslogstring: 0x19c34
+  __TEXT.__dlopen_cstrs: 0x478
   __TEXT.__ustring: 0x2c
-  __TEXT.__swift5_typeref: 0x933
   __TEXT.__constg_swiftt: 0x7c8
+  __TEXT.__swift5_typeref: 0x933
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x702
   __TEXT.__swift5_fieldmd: 0xae4
-  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x154
   __TEXT.__swift5_types: 0xc8

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x10b68
+  __TEXT.__unwind_info: 0x10d10
   __TEXT.__eh_frame: 0xc98
-  __TEXT.__objc_classname: 0x2f59
-  __TEXT.__objc_methname: 0x3a5c8
-  __TEXT.__objc_methtype: 0x8691
-  __TEXT.__objc_stubs: 0x25b60
-  __DATA_CONST.__got: 0x1ba8
-  __DATA_CONST.__const: 0x9530
-  __DATA_CONST.__objc_classlist: 0x9c0
+  __TEXT.__objc_classname: 0x2fae
+  __TEXT.__objc_methname: 0x3abd7
+  __TEXT.__objc_methtype: 0x8851
+  __TEXT.__objc_stubs: 0x26040
+  __DATA_CONST.__got: 0x1c20
+  __DATA_CONST.__const: 0x96e8
+  __DATA_CONST.__objc_classlist: 0x9d8
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x408
+  __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc88
+  __DATA_CONST.__objc_selrefs: 0xbdc0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x6c0
+  __DATA_CONST.__objc_superrefs: 0x6d0
   __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH_CONST.__auth_got: 0x13e8
   __AUTH_CONST.__const: 0x41b8
-  __AUTH_CONST.__cfstring: 0x11620
-  __AUTH_CONST.__objc_const: 0x25518
+  __AUTH_CONST.__cfstring: 0x11600
+  __AUTH_CONST.__objc_const: 0x25940
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xc20
-  __AUTH.__data: 0x3b8
-  __DATA.__objc_ivar: 0x1744
-  __DATA.__data: 0x33e0
+  __AUTH.__objc_data: 0xd80
+  __AUTH.__data: 0x3e8
+  __DATA.__objc_ivar: 0x1768
+  __DATA.__data: 0x3460
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x25c0
+  __DATA.__bss: 0x25f0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x57d8
+  __DATA_DIRTY.__objc_data: 0x5788
   __DATA_DIRTY.__data: 0xab0
   __DATA_DIRTY.__bss: 0x13f8
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08FF4466-BEFB-3EF5-929F-231B15C780E0
-  Functions: 10814
-  Symbols:   36679
-  CStrings:  16967
+  UUID: 81225D00-9BBE-3050-BA99-59AEE9A7A371
+  Functions: 10875
+  Symbols:   36910
+  CStrings:  17054
 
Symbols:
+ +[EDAttachmentMetadata(EDAttachmentPersistence) attachmentMetadataFromRow:]
+ +[EDConcreteLocalSearchProvider log]
+ +[EDMessageAttachmentMetadata(EDAttachmentPersistence) messageMetadataFromRow:]
+ -[EDAttachmentPersistenceManager _attachmentURLForAttachment:basePath:]
+ -[EDAttachmentPersistenceManager _attachmentURLForAttachment:basePath:].cold.1
+ -[EDAttachmentPersistenceManager _moveAttachmentAtURL:toURL:outError:].cold.1
+ -[EDAttachmentPersistenceManager _updateAttachmentURL:attachmentName:]
+ -[EDAttachmentPersistenceManager _writeFileWrapper:toURL:outError:].cold.4
+ -[EDConcreteLocalSearchProvider .cxx_destruct]
+ -[EDConcreteLocalSearchProvider _instantAnswersFromSuggestion:]
+ -[EDConcreteLocalSearchProvider _instantAnswersFromSuggestion:].cold.1
+ -[EDConcreteLocalSearchProvider _snippetHintsFromQueryResultMatchingHints:]
+ -[EDConcreteLocalSearchProvider initWithSearchableIndexManager:messagePersistence:messageQueryTransformer:]
+ -[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]
+ -[EDConcreteLocalSearchProvider maxTopHitsInCommittedSearch]
+ -[EDConcreteLocalSearchProvider maxTopHitsInCommittedSearch].cold.1
+ -[EDConcreteLocalSearchProvider messagePersistence]
+ -[EDConcreteLocalSearchProvider messageQueryTransformer]
+ -[EDConcreteLocalSearchProvider persistenceQueryForSearchableIndexQuery:]
+ -[EDConcreteLocalSearchProvider queryTransformer]
+ -[EDConcreteLocalSearchProvider searchableIndexManager]
+ -[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]
+ -[EDGroupedSender searchRelevanceScore]
+ -[EDGroupedSender searchResultType]
+ -[EDGroupedSenderQueryHandler queryHelper:didAddMessages:extraInfo:]
+ -[EDGroupedSenderQueryHandler queryHelper:didFindMessages:extraInfo:forInitialBatch:]
+ -[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:existingExtraInfo:isMove:]
+ -[EDInMemoryThreadQueryHandler _messagesInConversationIDs:limit:]
+ -[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:]
+ -[EDInMemoryThreadQueryHandler queryHelper:didAddMessages:extraInfo:]
+ -[EDInMemoryThreadQueryHandler queryHelper:didFindMessages:extraInfo:forInitialBatch:]
+ -[EDMessageQueryHandler _extraInfoForMessages:messagesToPrecache:outObjectIDs:existingExtraInfo:]
+ -[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:extraInfo:]
+ -[EDMessageQueryHandler messageList]
+ -[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]
+ -[EDMessageQueryHandler queryHelper:didFindMessages:extraInfo:forInitialBatch:]
+ -[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]
+ -[EDMessageQueryHelper _mailRankingSignalsAndSnippetsByObjectIDForMessages:data:]
+ -[EDMessageQueryHelper _startLiveSearchQuery]
+ -[EDMessageQueryHelper localSearchDidFindMessages:mailRankingAndSnippetHintsData:]
+ -[EDMessageQueryHelper localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:]
+ -[EDMessageQueryHelper remoteSearchDidFindMessages:inLocalIndex:]
+ -[EDMessageRepository test_setTestSearchProvider:]
+ -[EDThreadQueryHandler _addSnippetHintsAndMailRankingSignalsToExtraInfo:]
+ -[_EDMessageItemIDCollector queryHelper:didAddMessages:extraInfo:]
+ -[_EDMessageItemIDCollector queryHelper:didFindMessages:extraInfo:forInitialBatch:]
+ -[_EDMessageQueryHandlerList .cxx_destruct]
+ -[_EDMessageQueryHandlerList _comparatorForSortDescriptors:]
+ -[_EDMessageQueryHandlerList allMessageGlobalIDs]
+ -[_EDMessageQueryHandlerList entryComparator]
+ -[_EDMessageQueryHandlerList entryList]
+ -[_EDMessageQueryHandlerList hasItemsInList]
+ -[_EDMessageQueryHandlerList initWithQuery:]
+ -[_EDMessageQueryHandlerList insertMessagesReturningMessagesByPreviousObjectID:]
+ -[_EDMessageQueryHandlerList movesForExistingMessages:]
+ -[_EDMessageQueryHandlerList sectionPredicates]
+ -[_EDMessageQueryHandlerList sortDescriptors]
+ -[_EDMessageQueryHelperDelegateImpl queryHelper:didAddMessages:extraInfo:]
+ -[_EDMessageQueryHelperDelegateImpl queryHelper:didFindMessages:extraInfo:forInitialBatch:]
+ -[_EDMessageQueryHelperEntry .cxx_destruct]
+ -[_EDMessageQueryHelperEntry copyWithZone:]
+ -[_EDMessageQueryHelperEntry globalMessageID]
+ -[_EDMessageQueryHelperEntry initWithMessage:sortDescriptors:sectionPredicates:]
+ -[_EDMessageQueryHelperEntry isEqual:]
+ -[_EDMessageQueryHelperEntry primarySortValue]
+ -[_EDMessageQueryHelperEntry secondarySortValue]
+ -[_EDMessageQueryHelperEntry sectionIndex]
+ _EFMarkFileAsPurgeable
+ _EMMessageListAddedItemsExtraInfoKeyMailRankingAndSnippetHintsByObjectID
+ _EMMessageListChangedItemsExtraInfoKeyInstantAnswer
+ _EMTopHitsQueryDefaultLimit
+ _EMUserDefaultTopHitsInCommittedSearchLimit
+ _MDQueryResultEmbeddingDistances
+ _MDQueryResultRetrievalType
+ _OBJC_CLASS_$_EDAttachment
+ _OBJC_CLASS_$_EDConcreteLocalSearchProvider
+ _OBJC_CLASS_$_EMInstantAnswer
+ _OBJC_CLASS_$_EMMessageMailRankingAndSnippetHintsPair
+ _OBJC_CLASS_$_EMSearchableItemMailRankingAndSnippetHints
+ _OBJC_CLASS_$__EDMessageQueryHandlerList
+ _OBJC_CLASS_$__EDMessageQueryHelperEntry
+ _OBJC_IVAR_$_EDConcreteLocalSearchProvider._messagePersistence
+ _OBJC_IVAR_$_EDConcreteLocalSearchProvider._messageQueryTransformer
+ _OBJC_IVAR_$_EDConcreteLocalSearchProvider._queryTransformer
+ _OBJC_IVAR_$_EDConcreteLocalSearchProvider._searchableIndexManager
+ _OBJC_IVAR_$_EDGroupedSender._searchRelevanceScore
+ _OBJC_IVAR_$_EDGroupedSender._searchResultType
+ _OBJC_IVAR_$_EDMessageQueryHandler._messageList
+ _OBJC_IVAR_$__EDMessageQueryHandlerList._entryComparator
+ _OBJC_IVAR_$__EDMessageQueryHandlerList._entryList
+ _OBJC_IVAR_$__EDMessageQueryHandlerList._sectionPredicates
+ _OBJC_IVAR_$__EDMessageQueryHandlerList._sortDescriptors
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._globalMessageID
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._primarySortValue
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._secondarySortValue
+ _OBJC_IVAR_$__EDMessageQueryHelperEntry._sectionIndex
+ _OBJC_METACLASS_$_EDAttachment
+ _OBJC_METACLASS_$_EDConcreteLocalSearchProvider
+ _OBJC_METACLASS_$__EDMessageQueryHandlerList
+ _OBJC_METACLASS_$__EDMessageQueryHelperEntry
+ _SearchFoundationLibraryCore.frameworkLibrary
+ __DATA_EDAttachment
+ __INSTANCE_METHODS_EDAttachment
+ __IVARS_EDAttachment
+ __METACLASS_DATA_EDAttachment
+ __OBJC_$_CLASS_METHODS_EDAttachmentMetadata(EDAttachmentPersistence)
+ __OBJC_$_CLASS_METHODS_EDConcreteLocalSearchProvider
+ __OBJC_$_CLASS_METHODS_EDMessageAttachmentMetadata(EDAttachmentPersistence)
+ __OBJC_$_INSTANCE_METHODS_EDConcreteLocalSearchProvider
+ __OBJC_$_INSTANCE_METHODS__EDMessageQueryHandlerList
+ __OBJC_$_INSTANCE_METHODS__EDMessageQueryHelperEntry
+ __OBJC_$_INSTANCE_VARIABLES_EDConcreteLocalSearchProvider
+ __OBJC_$_INSTANCE_VARIABLES__EDMessageQueryHandlerList
+ __OBJC_$_INSTANCE_VARIABLES__EDMessageQueryHelperEntry
+ __OBJC_$_PROP_LIST_EDConcreteLocalSearchProvider
+ __OBJC_$_PROP_LIST_EDThreadQueryHandler.275
+ __OBJC_$_PROP_LIST__EDMessageQueryHandlerList
+ __OBJC_$_PROP_LIST__EDMessageQueryHelperEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDLocalSearchProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EDLocalSearchProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EDLocalSearchProvider
+ __OBJC_CLASS_PROTOCOLS_$_EDConcreteLocalSearchProvider
+ __OBJC_CLASS_PROTOCOLS_$__EDMessageQueryHelperEntry
+ __OBJC_CLASS_RO_$_EDConcreteLocalSearchProvider
+ __OBJC_CLASS_RO_$__EDMessageQueryHandlerList
+ __OBJC_CLASS_RO_$__EDMessageQueryHelperEntry
+ __OBJC_LABEL_PROTOCOL_$_EDLocalSearchProvider
+ __OBJC_METACLASS_RO_$_EDConcreteLocalSearchProvider
+ __OBJC_METACLASS_RO_$__EDMessageQueryHandlerList
+ __OBJC_METACLASS_RO_$__EDMessageQueryHelperEntry
+ __OBJC_PROTOCOL_$_EDLocalSearchProvider
+ __PROPERTIES_EDAttachment
+ ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke.105
+ ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke_2.106
+ ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke_2.106.cold.1
+ ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.76
+ ___106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.63
+ ___119-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:]_block_invoke
+ ___119-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:]_block_invoke_2
+ ___119-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:]_block_invoke_3
+ ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke.73
+ ___29-[EDMessageQueryHelper start]_block_invoke.35
+ ___29-[EDMessageQueryHelper start]_block_invoke.36
+ ___36+[EDConcreteLocalSearchProvider log]_block_invoke
+ ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke.45
+ ___49-[_EDMessageQueryHandlerList allMessageGlobalIDs]_block_invoke
+ ___53-[EDAttachmentPersistenceManager isDeletingMessages:]_block_invoke.88
+ ___55-[_EDMessageQueryHandlerList movesForExistingMessages:]_block_invoke
+ ___60-[EDConcreteLocalSearchProvider maxTopHitsInCommittedSearch]_block_invoke
+ ___60-[EDConcreteLocalSearchProvider maxTopHitsInCommittedSearch]_block_invoke_2
+ ___60-[_EDMessageQueryHandlerList _comparatorForSortDescriptors:]_block_invoke
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.17
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.22
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.22.cold.1
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_2
+ ___62-[EDConcreteLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_3
+ ___62-[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]_block_invoke
+ ___62-[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]_block_invoke.46
+ ___62-[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]_block_invoke.47
+ ___62-[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]_block_invoke.48
+ ___62-[EDMessageQueryHandler queryHelper:didAddMessages:extraInfo:]_block_invoke_2
+ ___64-[EDInMemoryThreadQueryHandler messagesInConversationIDs:limit:]_block_invoke
+ ___67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.59
+ ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke
+ ___72-[EDMessageQueryHelper _foundMessages:inRemoteSearch:foundInLocalIndex:]_block_invoke.55
+ ___73-[EDThreadQueryHandler _addSnippetHintsAndMailRankingSignalsToExtraInfo:]_block_invoke
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.14
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.14.cold.1
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke_2
+ ___79+[EDAttachmentPersistenceManager removeSynapseAttachmentAttributesForMessages:]_block_invoke.99
+ ___79-[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:helper:]_block_invoke
+ ___79-[EDMessageQueryHandler queryHelper:didFindMessages:extraInfo:forInitialBatch:]_block_invoke
+ ___79-[EDMessageQueryHandler queryHelper:didFindMessages:extraInfo:forInitialBatch:]_block_invoke_2
+ ___80-[_EDMessageQueryHandlerList insertMessagesReturningMessagesByPreviousObjectID:]_block_invoke
+ ___80-[_EDMessageQueryHelperEntry initWithMessage:sortDescriptors:sectionPredicates:]_block_invoke
+ ___81-[EDMessageQueryHelper _mailRankingSignalsAndSnippetsByObjectIDForMessages:data:]_block_invoke
+ ___82-[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:extraInfo:]_block_invoke
+ ___82-[EDMessageQueryHelper localSearchDidFindMessages:mailRankingAndSnippetHintsData:]_block_invoke
+ ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.63
+ ___86-[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:existingExtraInfo:isMove:]_block_invoke
+ ___86-[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:existingExtraInfo:isMove:]_block_invoke_2
+ ___95-[EDMessageQueryHelper localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:]_block_invoke
+ ___97+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:comparator:]_block_invoke_7
+ ___SearchFoundationLibraryCore_block_invoke
+ ___block_descriptor_32_e46_"NSNumber"16?0"_EDMessageQueryHelperEntry"8l
+ ___block_descriptor_40_ea8_32r_e36_v16?0"_EDMessageQueryHandlerList"8lr32l8
+ ___block_descriptor_40_ea8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_ea8_32s_e36_v16?0"_EDMessageQueryHandlerList"8ls32l8
+ ___block_descriptor_40_ea8_32s_e67_q24?0"_EDMessageQueryHelperEntry"8"_EDMessageQueryHelperEntry"16ls32l8
+ ___block_descriptor_48_ea8_32s40bs_e36_B16?0"_EDMessageQueryHelperEntry"8ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e36_v16?0"_EDMessageQueryHandlerList"8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e44_v40?0Q8"<NSCopying>"16"NSPredicate"24^B32ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40r48r_e33_v32?0"CSSearchableItem"8Q16^B24lr40l8s32l8r48l8
+ ___block_descriptor_56_ea8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e33_v32?0"CSSearchableItem"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e43_v32?0"EMMessageObjectID"8"NSArray"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48bs56w_e17_v16?0"NSArray"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_ea8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e36_v16?0"_EDMessageQueryHandlerList"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48r56r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_ea8_32s40s48s56s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.51
+ ___block_literal_global.68
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___getSFMailRankingSignalsClass_block_invoke
+ _audit_stringSearchFoundation
+ _expectedNumberEmbeddingDistances
+ _getSFMailRankingSignalsClass.softClass
+ _maxTopHitsInCommittedSearch._observationToken
+ _maxTopHitsInCommittedSearch.maxTopHitsInCommittedSearch
+ _maxTopHitsInCommittedSearch.onceToken
+ _maxValidSqDistance
+ _minValidSqDistance
+ _objc_msgSend$_addSnippetHintsAndMailRankingSignalsToExtraInfo:
+ _objc_msgSend$_comparatorForSortDescriptors:
+ _objc_msgSend$_extraInfoForMessages:messagesToPrecache:outObjectIDs:existingExtraInfo:
+ _objc_msgSend$_extraInfoForThreadObjectIDs:existingExtraInfo:isMove:
+ _objc_msgSend$_foundMessages:inRemoteSearch:foundInLocalIndex:
+ _objc_msgSend$_instantAnswersFromSuggestion:
+ _objc_msgSend$_mailRankingSignalsAndSnippetsByObjectIDForMessages:data:
+ _objc_msgSend$_messagesInConversationIDs:limit:
+ _objc_msgSend$_reportFoundMessages:before:messagesToPrecache:extraInfo:
+ _objc_msgSend$_snippetHintsFromQueryResultMatchingHints:
+ _objc_msgSend$_startLiveSearchQuery
+ _objc_msgSend$attachmentMetadata
+ _objc_msgSend$attachmentMetadataFromRow:
+ _objc_msgSend$attributeDictionary
+ _objc_msgSend$ef_lastPathComponent
+ _objc_msgSend$ef_sanitizedFileName
+ _objc_msgSend$entryComparator
+ _objc_msgSend$entryList
+ _objc_msgSend$fetchRemoteMessagesWithQuery:delegate:
+ _objc_msgSend$floatValue
+ _objc_msgSend$hasItemsInList
+ _objc_msgSend$initWithAttachmentMetadata:messageMetadata:
+ _objc_msgSend$initWithCSInstantAnswers:message:
+ _objc_msgSend$initWithIdentifiers:mailRankingAndSnippetHintsData:
+ _objc_msgSend$initWithMailRankingSignals:snippetHints:
+ _objc_msgSend$initWithMessage:sortDescriptors:sectionPredicates:
+ _objc_msgSend$initWithQuery:
+ _objc_msgSend$initWithSearchableItemIdentifier:mailRankingSignals:snippetHints:
+ _objc_msgSend$insertMessagesReturningMessagesByPreviousObjectID:
+ _objc_msgSend$instantAnswer
+ _objc_msgSend$instantAnswersSuggestions
+ _objc_msgSend$isSemanticMatch
+ _objc_msgSend$l1Score
+ _objc_msgSend$l2Score
+ _objc_msgSend$localSearchDidFindMessages:mailRankingAndSnippetHintsData:
+ _objc_msgSend$localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:
+ _objc_msgSend$localizedCompare:
+ _objc_msgSend$mailRankingAndSnippetHintsData
+ _objc_msgSend$mailRankingSignals
+ _objc_msgSend$mailRankingSignalsByPersistentID
+ _objc_msgSend$mailResultScoreL1
+ _objc_msgSend$matchingHintsByPersistentID
+ _objc_msgSend$maxTopHitsInCommittedSearch
+ _objc_msgSend$messageList
+ _objc_msgSend$messageMetadata
+ _objc_msgSend$messageMetadataFromRow:
+ _objc_msgSend$messagesWereAdded:extraInfo:
+ _objc_msgSend$movesForExistingMessages:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$primarySortValue
+ _objc_msgSend$queryHelper:didAddMessages:extraInfo:
+ _objc_msgSend$queryHelper:didFindMessages:extraInfo:forInitialBatch:
+ _objc_msgSend$sanitizedString
+ _objc_msgSend$searchRelevanceScore
+ _objc_msgSend$searchResultType
+ _objc_msgSend$secondarySortValue
+ _objc_msgSend$sectionIndex
+ _objc_msgSend$setIsSemanticMatch:
+ _objc_msgSend$setIsSyntacticMatch:
+ _objc_msgSend$setSearchRelevanceScore:
+ _objc_msgSend$setSearchResultType:
+ _objc_msgSend$setSemanticScore:
+ _objc_msgSend$setSyntacticScore:
+ _objc_msgSend$topHitsQueryInstantAnswersResult
+ _objc_msgSend$topHitsSearchWithQuery:delegate:completion:
+ _spotlightRetrievalTypeSemantic
+ _spotlightRetrievalTypeSyntactic
- +[EDAttachmentPersistenceManager _cleanedNameForName:]
- +[EDLocalSearchProvider log]
- -[EDAttachmentPersistenceManager _attachmentURLForAttachmentTableMetadata:basePath:]
- -[EDAttachmentPersistenceManager _attachmentURLForAttachmentTableMetadata:basePath:].cold.1
- -[EDAttachmentPersistenceManager _updateFileWrapperNameToStaticFileName:]
- -[EDGroupedSender isTopHit]
- -[EDGroupedSenderQueryHandler queryHelper:didAddMessages:]
- -[EDGroupedSenderQueryHandler queryHelper:didFindMessages:forInitialBatch:]
- -[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:isMove:]
- -[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:hasChanges:]
- -[EDInMemoryThreadQueryHandler queryHelper:didAddMessages:]
- -[EDInMemoryThreadQueryHandler queryHelper:didFindMessages:forInitialBatch:]
- -[EDLocalSearchProvider .cxx_destruct]
- -[EDLocalSearchProvider initWithSearchableIndexManager:messagePersistence:messageQueryTransformer:]
- -[EDLocalSearchProvider liveSearchWithQuery:delegate:]
- -[EDLocalSearchProvider messagePersistence]
- -[EDLocalSearchProvider messageQueryTransformer]
- -[EDLocalSearchProvider persistenceQueryForSearchableIndexQuery:]
- -[EDLocalSearchProvider queryTransformer]
- -[EDLocalSearchProvider searchableIndexManager]
- -[EDLocalSearchProvider topHitsSearchWithQuery:delegate:]
- -[EDMessageQueryHandler _extraInfoForMessages:messagesToPrecache:outObjectIDs:]
- -[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:]
- -[EDMessageQueryHandler queryHelper:didAddMessages:]
- -[EDMessageQueryHandler queryHelper:didFindMessages:forInitialBatch:]
- -[EDMessageQueryHelper _foundMessages:inRemoteSearch:]
- -[EDMessageQueryHelper accumulatedSnippetData]
- -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]
- -[EDMessageQueryHelper localSearchDidFindTopHits:]
- -[EDMessageQueryHelper remoteSearchDidFindMessages:]
- -[EDMessageQueryHelper setAccumulatedSnippetData:]
- -[EDRichLinkPersistence _richLinkDirectoryURLWithBasePath:].cold.3
- -[EDThreadQueryHandler _addSnippetHintsToExtraInfo:]
- -[_EDMessageItemIDCollector queryHelper:didAddMessages:]
- -[_EDMessageItemIDCollector queryHelper:didFindMessages:forInitialBatch:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didAddMessages:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didFindMessages:forInitialBatch:]
- _EMMessageListAddedItemsExtraInfoKeySnippetHintsByObjectID
- _OBJC_CLASS_$_EDLocalSearchProvider
- _OBJC_CLASS_$_EMSearchableItemSnippetData
- _OBJC_IVAR_$_EDGroupedSender._isTopHit
- _OBJC_IVAR_$_EDLocalSearchProvider._messagePersistence
- _OBJC_IVAR_$_EDLocalSearchProvider._messageQueryTransformer
- _OBJC_IVAR_$_EDLocalSearchProvider._queryTransformer
- _OBJC_IVAR_$_EDLocalSearchProvider._searchableIndexManager
- _OBJC_IVAR_$_EDMessageQueryHelper._accumulatedSnippetData
- _OBJC_METACLASS_$_EDLocalSearchProvider
- __OBJC_$_CLASS_METHODS_EDLocalSearchProvider
- __OBJC_$_INSTANCE_METHODS_EDLocalSearchProvider
- __OBJC_$_INSTANCE_VARIABLES_EDLocalSearchProvider
- __OBJC_$_PROP_LIST_EDLocalSearchProvider
- __OBJC_$_PROP_LIST_EDThreadQueryHandler.276
- __OBJC_CLASS_RO_$_EDLocalSearchProvider
- __OBJC_METACLASS_RO_$_EDLocalSearchProvider
- ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke.109
- ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke_2.110
- ___101-[EDAttachmentPersistenceManager addSynapseAttributesToAttachmentWithURL:contentType:usingGenerator:]_block_invoke_2.110.cold.1
- ___105-[EDMessageQueryHelper _calculateAndReportChangesForPersistedMessages:withPendingChangesKey:changeBlock:]_block_invoke.81
- ___106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.59
- ___109-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:hasChanges:]_block_invoke
- ___109-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:hasChanges:]_block_invoke_2
- ___109-[EDInMemoryThreadQueryHandler collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:hasChanges:]_block_invoke_3
- ___124-[EDMessageQueryHelper _performBlockAfterGenerationCheck:generation:keyPaths:removedMessages:changedMessages:addedMessages:]_block_invoke.78
- ___28+[EDLocalSearchProvider log]_block_invoke
- ___29-[EDMessageQueryHelper start]_block_invoke.42
- ___42-[EDMessageQueryHelper _getInitialResults]_block_invoke.51
- ___50-[EDMessageQueryHelper localSearchDidFindTopHits:]_block_invoke
- ___52-[EDMessageQueryHandler queryHelper:didAddMessages:]_block_invoke
- ___52-[EDMessageQueryHandler queryHelper:didAddMessages:]_block_invoke.43
- ___52-[EDThreadQueryHandler _addSnippetHintsToExtraInfo:]_block_invoke
- ___53-[EDAttachmentPersistenceManager isDeletingMessages:]_block_invoke.92
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke.15
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_2
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_2.24
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_2.24.cold.1
- ___54-[EDLocalSearchProvider liveSearchWithQuery:delegate:]_block_invoke_3
- ___54-[EDMessageQueryHelper _foundMessages:inRemoteSearch:]_block_invoke
- ___54-[EDMessageQueryHelper _foundMessages:inRemoteSearch:]_block_invoke.61
- ___57-[EDLocalSearchProvider topHitsSearchWithQuery:delegate:]_block_invoke
- ___57-[EDLocalSearchProvider topHitsSearchWithQuery:delegate:]_block_invoke_2
- ___57-[EDLocalSearchProvider topHitsSearchWithQuery:delegate:]_block_invoke_3
- ___57-[EDLocalSearchProvider topHitsSearchWithQuery:delegate:]_block_invoke_3.cold.1
- ___67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.55
- ___67-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]_block_invoke
- ___68-[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:isMove:]_block_invoke
- ___68-[EDInMemoryThreadQueryHandler _extraInfoForThreadObjectIDs:isMove:]_block_invoke_2
- ___72-[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:]_block_invoke
- ___79+[EDAttachmentPersistenceManager removeSynapseAttachmentAttributesForMessages:]_block_invoke.103
- ___85-[EDMessageQueryHelper _persistenceDidDeleteMessages:includeMessagesWithDeletedFlag:]_block_invoke.69
- ___97+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:comparator:]_block_invoke.75
- ___block_descriptor_40_ea8_32s_e43_v32?0"EMMessageObjectID"8"NSArray"16^B24ls32l8
- ___block_descriptor_48_ea8_32s40r_e33_v32?0"CSSearchableItem"8Q16^B24lr40l8s32l8
- ___block_descriptor_48_ea8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_ea8_32s40s_e33_v32?0"CSSearchableItem"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_ea8_32s40w_e45_v16?0"EMSearchableIndexTopHitsQueryResult"8lw40l8s32l8
- ___block_descriptor_64_ea8_32s40s48r_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8r48l8s40l8
- ___block_descriptor_64_ea8_32s40s48s_e41_v16?0"<EMSearchableIndexQueryBuilder>"8ls32l8s40l8s48l8
- ___block_literal_global.101
- ___block_literal_global.47
- ___block_literal_global.94
- ___block_literal_global.944
- ___block_literal_global.946
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_EmailDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_EmailDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_EmailDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_EmailDaemon
- _objc_msgSend$URLPathAllowedCharacterSet
- _objc_msgSend$_addSnippetHintsToExtraInfo:
- _objc_msgSend$_extraInfoForMessages:messagesToPrecache:outObjectIDs:
- _objc_msgSend$_foundMessages:inRemoteSearch:
- _objc_msgSend$_reportFoundMessages:before:messagesToPrecache:
- _objc_msgSend$accumulatedSnippetData
- _objc_msgSend$addCharactersInString:
- _objc_msgSend$applyTransform:reverse:range:updatedRange:
- _objc_msgSend$createFilenameForAttachmentName:
- _objc_msgSend$fetchRemoteMessagesWithQuery:delegate:useLocalIndex:
- _objc_msgSend$initWithIdentifiers:snippetData:
- _objc_msgSend$initWithSearchableItemIdentifier:snippetHints:
- _objc_msgSend$invertedSet
- _objc_msgSend$localSearchDidFindMessages:itemSnippetData:
- _objc_msgSend$localSearchDidFindTopHits:
- _objc_msgSend$messagesWereAdded:
- _objc_msgSend$pathExtension
- _objc_msgSend$queryHelper:didAddMessages:
- _objc_msgSend$queryHelper:didFindMessages:forInitialBatch:
- _objc_msgSend$rangeOfCharacterFromSet:
- _objc_msgSend$replaceCharactersInRange:withString:
- _objc_msgSend$setAccumulatedSnippetData:
- _objc_msgSend$setIsTopHit:
- _objc_msgSend$snippetData
- _objc_msgSend$stringByDeletingPathExtension
- _objc_msgSend$topHitsSearchWithQuery:delegate:
CStrings:
+ " local index"
+ "%@ Finished live query %{public}@"
+ "%@ Finished top hits query %{public}@"
+ "%@ Starting live query %{public}@"
+ "%@ Starting top hits query %{public}@"
+ "%p: %{public}@ - instantAnswers for objectID:%{public}@"
+ "%p: Adding %u filtered messages: %{public}@"
+ "%p: Found %@ messages in remote search: %@"
+ "%p: Moving objectIDs: %{public}@ before: %{public}@\n%{public}@"
+ ".."
+ "@"
+ "@\"<EDLocalSearchProvider>\""
+ "@\"<EDLocalSearchProvider>\"16@0:8"
+ "@\"<EFCancelable>\"40@0:8@\"EMQuery\"16@\"<EDLocalSearchDelegate>\"24@?<v@?>32"
+ "@\"<EFCancelable><NSProgressReporting>\"32@0:8@\"EMQuery\"16@\"<EDLocalSearchDelegate>\"24"
+ "@\"EMQuery\"24@0:8@\"EMQuery\"16"
+ "@\"NSNumber\"16@0:8"
+ "@\"NSNumber\"16@?0@\"_EDMessageQueryHelperEntry\"8"
+ "@48@0:8@16@24^@32@40"
+ "B16@?0@\"_EDMessageQueryHelperEntry\"8"
+ "Class getSFMailRankingSignalsClass(void)_block_invoke"
+ "EDAttachment"
+ "EDConcreteLocalSearchProvider"
+ "EDLocalSearchProvider.m"
+ "EmailDaemon.EDAttachment"
+ "Error occurred attempting to make file purgeable: %{public}@: %{public}@"
+ "Performing Remote Search (Search Indexer + Server Search)"
+ "SFMailRankingSignals"
+ "Spotlight live search found %lu messages matching the %lu searchableItemIdentifiers returned:\n%{public}@ for query %{public}@"
+ "Spotlight live search returned error %{public}@ for query %{public}@"
+ "Spotlight top hits and instant answers search returned error %{public}@ for query %{public}@"
+ "Spotlight top hits search found %lu messages matching the %lu searchableItemIdentifiers returned:\n%{public}@ for query %{public}@"
+ "T@\"<EDLocalSearchProvider>\",R"
+ "T@\"<EDLocalSearchProvider>\",R,V_localSearchProvider"
+ "T@\"EDAttachmentMetadata\",N,R,VattachmentMetadata"
+ "T@\"EDMessageAttachmentMetadata\",N,R,VmessageMetadata"
+ "T@\"EFLocked\",R,N,V_messageList"
+ "T@\"EFOrderedDictionary\",R,C,N,V_sectionPredicates"
+ "T@\"NSArray\",R,C,N,V_sortDescriptors"
+ "T@\"NSMutableArray\",R,N,V_entryList"
+ "T@\"NSNumber\",R"
+ "T@\"NSNumber\",R,V_searchRelevanceScore"
+ "T@,R,V_primarySortValue"
+ "T@,R,V_secondarySortValue"
+ "T@?,R,N,V_entryComparator"
+ "TQ,R,V_sectionIndex"
+ "Tq,R,V_searchResultType"
+ "[instant answers] Couldn't extract EMGlobalMessageID from messageid in csInstantAnswers from spotlight"
+ "[instant answers] created EMInstantAnswer for %{public}@"
+ "_EDMessageQueryHandlerList"
+ "_EDMessageQueryHelperEntry"
+ "_addSnippetHintsAndMailRankingSignalsToExtraInfo:"
+ "_comparatorForSortDescriptors:"
+ "_entryComparator"
+ "_entryList"
+ "_extraInfoForMessages:messagesToPrecache:outObjectIDs:existingExtraInfo:"
+ "_extraInfoForThreadObjectIDs:existingExtraInfo:isMove:"
+ "_foundMessages:inRemoteSearch:foundInLocalIndex:"
+ "_instantAnswersFromSuggestion:"
+ "_mailRankingSignalsAndSnippetsByObjectIDForMessages:data:"
+ "_messageList"
+ "_messagesInConversationIDs:limit:"
+ "_primarySortValue"
+ "_reportFoundMessages:before:messagesToPrecache:extraInfo:"
+ "_searchRelevanceScore"
+ "_searchResultType"
+ "_secondarySortValue"
+ "_sectionIndex"
+ "_snippetHintsFromQueryResultMatchingHints:"
+ "_startLiveSearchQuery"
+ "allMessageGlobalIDs"
+ "attachmentMetadata"
+ "attachmentMetadataFromRow:"
+ "collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:"
+ "ef_lastPathComponent"
+ "ef_sanitizedFileName"
+ "entryComparator"
+ "entryList"
+ "fetchRemoteMessagesWithQuery:delegate:"
+ "floatValue"
+ "hasItemsInList"
+ "initWithAttachmentMetadata:messageMetadata:"
+ "initWithCSInstantAnswers:message:"
+ "initWithIdentifiers:mailRankingAndSnippetHintsData:"
+ "initWithMailRankingSignals:snippetHints:"
+ "initWithMessage:sortDescriptors:sectionPredicates:"
+ "initWithQuery:"
+ "initWithSearchableItemIdentifier:mailRankingSignals:snippetHints:"
+ "insertMessagesReturningMessagesByPreviousObjectID:"
+ "instantAnswer"
+ "instantAnswersSuggestions"
+ "isSemanticMatch"
+ "l1Score"
+ "l2Score"
+ "localSearchDidFindMessages:mailRankingAndSnippetHintsData:"
+ "localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:"
+ "localizedCompare:"
+ "mailRankingAndSnippetHintsData"
+ "mailRankingSignals"
+ "mailRankingSignalsByPersistentID"
+ "mailResultScoreL1"
+ "matchingHintsByPersistentID"
+ "maxTopHitsInCommittedSearch"
+ "messageList"
+ "messageMetadata"
+ "messageMetadataFromRow:"
+ "messagesWereAdded:extraInfo:"
+ "movesForExistingMessages:"
+ "numberWithFloat:"
+ "primarySortValue"
+ "q24@?0@\"_EDMessageQueryHelperEntry\"8@\"_EDMessageQueryHelperEntry\"16"
+ "queryHelper:didAddMessages:extraInfo:"
+ "queryHelper:didFindMessages:extraInfo:forInitialBatch:"
+ "remoteSearchDidFindMessages:inLocalIndex:"
+ "sanitizedString"
+ "searchRelevanceScore"
+ "searchResultType"
+ "secondarySortValue"
+ "sectionIndex"
+ "setIsSemanticMatch:"
+ "setIsSyntacticMatch:"
+ "setSearchRelevanceScore:"
+ "setSearchResultType:"
+ "setSemanticScore:"
+ "setSyntacticScore:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation"
+ "test_setTestSearchProvider:"
+ "topHitsQueryInstantAnswersResult"
+ "topHitsSearchWithQuery:delegate:completion:"
+ "v16@?0@\"_EDMessageQueryHandlerList\"8"
+ "v28@0:8@\"NSArray\"16B24"
+ "v32@0:8@\"NSArray\"16@\"NSDictionary\"24"
+ "v40@0:8@\"EDMessageQueryHelper\"16@\"NSArray\"24@\"NSDictionary\"32"
+ "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@\"EMInstantAnswer\"32"
+ "v44@0:8@\"EDMessageQueryHelper\"16@\"NSArray\"24@\"NSDictionary\"32B40"
+ "v60@0:8@\"EMInMemoryThreadCollection\"16B24@\"NSArray\"28@\"EMObjectID\"36@\"NSDictionary\"44^B52"
+ "v60@0:8@16B24@28@36@44^B52"
+ "void *SearchFoundationLibrary(void)"
- "%@ Starting live query %@"
- "%p: Adding %u filtered messages: %@"
- "/."
- "@\"EDLocalSearchProvider\""
- "@\"EDLocalSearchProvider\"16@0:8"
- "Any-Latin; Latin-ASCII"
- "Could not create rich links directory, path is null"
- "Created new attachment filename %@"
- "Performing %@ remote search"
- "Spotlight search returned error %@"
- "Spotlight top hits search returned error %@"
- "T@\"EDLocalSearchProvider\",R"
- "T@\"EDLocalSearchProvider\",R,V_localSearchProvider"
- "T@\"NSMutableArray\",&,N,V_accumulatedSnippetData"
- "TB,R,V_isTopHit"
- "URLPathAllowedCharacterSet"
- "_accumulatedSnippetData"
- "_addSnippetHintsToExtraInfo:"
- "_extraInfoForMessages:messagesToPrecache:outObjectIDs:"
- "_foundMessages:inRemoteSearch:"
- "_isTopHit"
- "_reportFoundMessages:before:messagesToPrecache:"
- "accumulatedSnippetData"
- "addCharactersInString:"
- "applyTransform:reverse:range:updatedRange:"
- "collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:hasChanges:"
- "createFilenameForAttachmentName:"
- "fetchRemoteMessagesWithQuery:delegate:useLocalIndex:"
- "initWithIdentifiers:snippetData:"
- "initWithSearchableItemIdentifier:snippetHints:"
- "invertedSet"
- "isTopHit"
- "localSearchDidFindMessages:itemSnippetData:"
- "localSearchDidFindTopHits:"
- "locally indexed"
- "messagesWereAdded:"
- "pathExtension"
- "queryHelper:didAddMessages:"
- "queryHelper:didFindMessages:forInitialBatch:"
- "rangeOfCharacterFromSet:"
- "remoteSearchDidFindMessages:"
- "replaceCharactersInRange:withString:"
- "server-side"
- "setAccumulatedSnippetData:"
- "setIsTopHit:"
- "snippetData"
- "stringByDeletingPathExtension"
- "topHitsSearchWithQuery:delegate:"
- "v16@?0@\"EMSearchableIndexTopHitsQueryResult\"8"
- "v36@0:8@\"EDMessageQueryHelper\"16@\"NSArray\"24B32"
- "v52@0:8@\"EMInMemoryThreadCollection\"16B24@\"NSArray\"28@\"EMObjectID\"36^B44"
- "v52@0:8@16B24@28@36^B44"

```
