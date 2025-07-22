## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3858.100.10.2.1
-  __TEXT.__text: 0x26ce24
-  __TEXT.__auth_stubs: 0x27b0
-  __TEXT.__objc_methlist: 0x162e4
+3860.100.5.2.1
+  __TEXT.__text: 0x279854
+  __TEXT.__auth_stubs: 0x27d0
+  __TEXT.__objc_methlist: 0x169b4
   __TEXT.__const: 0x1f1c
-  __TEXT.__gcc_except_tab: 0x501b8
-  __TEXT.__cstring: 0x22b97
-  __TEXT.__oslogstring: 0x19d94
-  __TEXT.__dlopen_cstrs: 0x478
+  __TEXT.__gcc_except_tab: 0x52404
+  __TEXT.__cstring: 0x22f67
+  __TEXT.__oslogstring: 0x1a5b4
+  __TEXT.__dlopen_cstrs: 0x3bc
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0x7c8
   __TEXT.__swift5_typeref: 0x933

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x10d88
+  __TEXT.__unwind_info: 0x112f0
   __TEXT.__eh_frame: 0xcc0
-  __TEXT.__objc_classname: 0x2fae
-  __TEXT.__objc_methname: 0x3ac8c
-  __TEXT.__objc_methtype: 0x8851
-  __TEXT.__objc_stubs: 0x260c0
-  __DATA_CONST.__got: 0x1c40
-  __DATA_CONST.__const: 0x96e8
-  __DATA_CONST.__objc_classlist: 0x9d8
+  __TEXT.__objc_classname: 0x3049
+  __TEXT.__objc_methname: 0x3b6f6
+  __TEXT.__objc_methtype: 0x88a3
+  __TEXT.__objc_stubs: 0x26860
+  __DATA_CONST.__got: 0x1c38
+  __DATA_CONST.__const: 0x9bc8
+  __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbde8
+  __DATA_CONST.__objc_selrefs: 0xbfa0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x6d0
+  __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x680
-  __AUTH_CONST.__auth_got: 0x13e8
-  __AUTH_CONST.__const: 0x4200
-  __AUTH_CONST.__cfstring: 0x11660
-  __AUTH_CONST.__objc_const: 0x25990
+  __AUTH_CONST.__auth_got: 0x13f8
+  __AUTH_CONST.__const: 0x43c0
+  __AUTH_CONST.__cfstring: 0x117e0
+  __AUTH_CONST.__objc_const: 0x26768
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0xd80
+  __AUTH.__objc_data: 0xf10
   __AUTH.__data: 0x3e8
-  __DATA.__objc_ivar: 0x176c
-  __DATA.__data: 0x3460
+  __DATA.__objc_ivar: 0x182c
+  __DATA.__data: 0x3470
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x25f0
+  __DATA.__bss: 0x2600
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x5788
-  __DATA_DIRTY.__data: 0xab0
-  __DATA_DIRTY.__bss: 0x1408
-  __DATA_DIRTY.__common: 0x40
+  __DATA_DIRTY.__data: 0xaa0
+  __DATA_DIRTY.__bss: 0x1418
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5B923EE-DD0A-32A5-A8DC-25C0CA53C937
-  Functions: 10885
-  Symbols:   36940
-  CStrings:  17072
+  UUID: 09662AC9-5D75-388D-A2FE-DF833FD65ADE
+  Functions: 11095
+  Symbols:   37659
+  CStrings:  17271
 
Symbols:
+ +[EDInMemoryThread _dateSortDescriptors]
+ +[EDInMemoryThread _dateSortDescriptors].cold.1
+ +[EDInMemoryThread log]
+ +[EDInMemoryThreadCollection _comparatorForInThreadProxiesWithSortDescriptors:]
+ +[EDInMemoryThreadCollection _comparisonForSortDescriptor:value1:value2:]
+ +[EDSectionQueryItemHelper _sectionIndexForItem:sectionPredicates:sectionIdentifier:]
+ +[EDSectionQueryItemHelper sectionQueryItemHelperWithQuery:]
+ -[EDBiomeBlackPearlLogger _database]
+ -[EDBiomeBlackPearlLogger _database].cold.1
+ -[EDInMemoryThread .cxx_destruct]
+ -[EDInMemoryThread _addMessagesToThread:]
+ -[EDInMemoryThread _calculateAndApplyChange]
+ -[EDInMemoryThread _calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:]
+ -[EDInMemoryThread _combinedCCList]
+ -[EDInMemoryThread _combinedFlagColors]
+ -[EDInMemoryThread _combinedFlagColors].cold.1
+ -[EDInMemoryThread _combinedFlags]
+ -[EDInMemoryThread _combinedHasAttachments]
+ -[EDInMemoryThread _combinedHasUnflagged]
+ -[EDInMemoryThread _combinedIsBlocked]
+ -[EDInMemoryThread _combinedIsVIP]
+ -[EDInMemoryThread _combinedMailboxes]
+ -[EDInMemoryThread _combinedReadLater]
+ -[EDInMemoryThread _combinedSenderList]
+ -[EDInMemoryThread _combinedToList]
+ -[EDInMemoryThread _createThreadWithObjectID:]
+ -[EDInMemoryThread _isSortedByDate:]
+ -[EDInMemoryThread _maxSearchRelevanceScore]
+ -[EDInMemoryThread _newestDisplayDate]
+ -[EDInMemoryThread _recalculateDisplayMessage]
+ -[EDInMemoryThread addMessages:]
+ -[EDInMemoryThread changeMessages:forKeyPaths:threadIsEmpty:]
+ -[EDInMemoryThread copyWithZone:]
+ -[EDInMemoryThread description]
+ -[EDInMemoryThread displayMessage]
+ -[EDInMemoryThread initWithMessages:originatingQuery:threadScope:]
+ -[EDInMemoryThread initWithMessages:originatingQuery:threadScope:].cold.1
+ -[EDInMemoryThread messageListItem]
+ -[EDInMemoryThread messages]
+ -[EDInMemoryThread newestMessage]
+ -[EDInMemoryThread oldestMessage]
+ -[EDInMemoryThread originatingQuery]
+ -[EDInMemoryThread removeMessages:threadIsEmpty:]
+ -[EDInMemoryThread setDisplayMessage:]
+ -[EDInMemoryThread setThread:]
+ -[EDInMemoryThread threadScope]
+ -[EDInMemoryThread thread]
+ -[EDInMemoryThread updateMessage:fromOldObjectID:]
+ -[EDInMemoryThreadCollection .cxx_destruct]
+ -[EDInMemoryThreadCollection _cachedInMemoryThreadForConversationID:]
+ -[EDInMemoryThreadCollection _cachedInMemoryThreadForConversationID:].cold.1
+ -[EDInMemoryThreadCollection _createInMemoryThreadForConversationID:]
+ -[EDInMemoryThreadCollection _createInMemoryThreadForConversationID:messages:cacheResults:]
+ -[EDInMemoryThreadCollection _didMergeInThreads:]
+ -[EDInMemoryThreadCollection _hasLoaded]
+ -[EDInMemoryThreadCollection _inMemoryThreadsForObjectIDs:cacheResults:]
+ -[EDInMemoryThreadCollection _mergeInThreads:extraInfo:forMove:]
+ -[EDInMemoryThreadCollection _messageListItemChangeAffectsSorting:]
+ -[EDInMemoryThreadCollection _messagesByConversationIDForMessages:]
+ -[EDInMemoryThreadCollection _notifyObserverOfOldestThreadsByMailboxObjectIDs]
+ -[EDInMemoryThreadCollection _removeThreadProxies:forMove:]
+ -[EDInMemoryThreadCollection _threadsWereDeleted]
+ -[EDInMemoryThreadCollection _updateCurrentOldestThreadWithThreadIfApplicable:forMailbox:]
+ -[EDInMemoryThreadCollection _updateOldestThreadsForMailboxes:]
+ -[EDInMemoryThreadCollection _updateThreadProxy:threadIsEmpty:thread:]
+ -[EDInMemoryThreadCollection _updateThreadProxy:threadIsEmpty:thread:].cold.1
+ -[EDInMemoryThreadCollection clearInMemoryThreadCache]
+ -[EDInMemoryThreadCollection clearOldestThreadsByMailboxObjectIDs]
+ -[EDInMemoryThreadCollection comparator]
+ -[EDInMemoryThreadCollection conversationIDDidChangeForMessages:fromConversationID:]
+ -[EDInMemoryThreadCollection conversationNotificationLevelDidChangeForConversation:conversationID:]
+ -[EDInMemoryThreadCollection dataSource]
+ -[EDInMemoryThreadCollection dateSortOrder]
+ -[EDInMemoryThreadCollection delegate]
+ -[EDInMemoryThreadCollection enumerateObjectIDsInBatchesOfSize:block:]
+ -[EDInMemoryThreadCollection inMemoryThreadCache]
+ -[EDInMemoryThreadCollection inMemoryThreadClass]
+ -[EDInMemoryThreadCollection inMemoryThreadForConversationID:]
+ -[EDInMemoryThreadCollection initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:]
+ -[EDInMemoryThreadCollection initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:inMemoryThreadClass:]
+ -[EDInMemoryThreadCollection initializeOldestThreadsByMailbox]
+ -[EDInMemoryThreadCollection itemIDs]
+ -[EDInMemoryThreadCollection limitedCache]
+ -[EDInMemoryThreadCollection logClient]
+ -[EDInMemoryThreadCollection mailboxTypeResolver]
+ -[EDInMemoryThreadCollection messageListItemForObjectID:error:]
+ -[EDInMemoryThreadCollection messagesForThread:]
+ -[EDInMemoryThreadCollection messagesWereAdded:extraInfo:]
+ -[EDInMemoryThreadCollection messagesWereChanged:forKeyPaths:deleted:]
+ -[EDInMemoryThreadCollection messagesWereChanged:forKeyPaths:deleted:].cold.1
+ -[EDInMemoryThreadCollection notifyObserverOfOldestThreadsByMailboxObjectIDs]
+ -[EDInMemoryThreadCollection objectIDDidChangeForMessage:oldObjectID:oldConversationID:]
+ -[EDInMemoryThreadCollection query]
+ -[EDInMemoryThreadCollection removeThreadProxies:forMove:]
+ -[EDInMemoryThreadCollection sectionIdentifierForThreadObjectID:]
+ -[EDInMemoryThreadCollection setLimitedCache:]
+ -[EDInMemoryThreadCollection setLogClient:]
+ -[EDInMemoryThreadCollection threadScope]
+ -[EDInMemoryThreadCollection threadsAndMessagesForObjectIDs:]
+ -[EDInMemoryThreadQueryHandler assertCorrectSchedulerForCollection:]
+ -[EDInMemoryThreadQueryHandler initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:]
+ -[EDInMemoryThreadQueryHandler initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:].cold.1
+ -[EDMessageQueryHelper _snippetsByObjectIDForMessages:itemSnippetData:]
+ -[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]
+ -[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]
+ -[EDMessageRepository _performQuery:withObserver:observationIdentifier:completionHandler:]
+ -[EDMessageRepository _performQuery:withObserver:observationIdentifier:completionHandler:].cold.1
+ -[EDMessageRepository performQuery:withObserver:observationIdentifier:completionHandler:]
+ -[EDPersistenceDatabase performWithOptions:caller:block:].cold.3
+ -[EDPersistenceHookRegistry _registerSelector:types:]
+ -[EDSectionQueryItemHelper .cxx_destruct]
+ -[EDSectionQueryItemHelper _createSectionComparator]
+ -[EDSectionQueryItemHelper _idForItem:]
+ -[EDSectionQueryItemHelper _sectionIndexForItem:sectionIdentifier:]
+ -[EDSectionQueryItemHelper comparatorForItemComparator:]
+ -[EDSectionQueryItemHelper idForItem:]
+ -[EDSectionQueryItemHelper initWithQuery:sectionPredicates:]
+ -[EDSectionQueryItemHelper query]
+ -[EDSectionQueryItemHelper removeIDs:]
+ -[EDSectionQueryItemHelper sectionComparator]
+ -[EDSectionQueryItemHelper sectionIdentifierForID:]
+ -[EDSectionQueryItemHelper sectionIdentifierForItem:]
+ -[EDSectionQueryItemHelper sectionNumberForID:]
+ -[EDSectionQueryItemHelper sectionNumbersForIDs:]
+ -[EDSectionQueryItemHelper sectionPredicates]
+ -[EDSectionQueryItemHelper shouldSectionItemsRemainInSection]
+ -[EDSectionQueryItemHelper updateSectionForItem:]
+ -[EDSortableThreadProxy .cxx_destruct]
+ -[EDSortableThreadProxy _copySortPropertiesForDescriptors:thread:]
+ -[EDSortableThreadProxy _setValueFromThreadAndReturnIfChanged:keyPath:isPrimary:]
+ -[EDSortableThreadProxy _sortValueForRawValue:keyPath:]
+ -[EDSortableThreadProxy _targetForSelector:]
+ -[EDSortableThreadProxy calculateChangeFromThread:]
+ -[EDSortableThreadProxy conversationID]
+ -[EDSortableThreadProxy date]
+ -[EDSortableThreadProxy description]
+ -[EDSortableThreadProxy ef_publicDescription]
+ -[EDSortableThreadProxy forwardingTargetForSelector:]
+ -[EDSortableThreadProxy initWithThread:originatingQuery:]
+ -[EDSortableThreadProxy objectID]
+ -[EDSortableThreadProxy primarySortValue]
+ -[EDSortableThreadProxy properties]
+ -[EDSortableThreadProxy respondsToSelector:]
+ -[EDSortableThreadProxy setDate:]
+ -[EDSortableThreadProxy setPrimarySortValue:]
+ -[EDSortableThreadProxy setProperties:]
+ -[EDSortableThreadProxy updateFromThread:addingAdditionalInformation:query:]
+ -[EDSortableThreadProxyAdditionalProperties .cxx_destruct]
+ -[EDSortableThreadProxyAdditionalProperties allowAuthenticationWarning]
+ -[EDSortableThreadProxyAdditionalProperties businessID]
+ -[EDSortableThreadProxyAdditionalProperties businessLogoID]
+ -[EDSortableThreadProxyAdditionalProperties category]
+ -[EDSortableThreadProxyAdditionalProperties ccList]
+ -[EDSortableThreadProxyAdditionalProperties displayDate]
+ -[EDSortableThreadProxyAdditionalProperties displayMessageGlobalID]
+ -[EDSortableThreadProxyAdditionalProperties flagColors]
+ -[EDSortableThreadProxyAdditionalProperties flags]
+ -[EDSortableThreadProxyAdditionalProperties generatedSummary]
+ -[EDSortableThreadProxyAdditionalProperties hasAttachments]
+ -[EDSortableThreadProxyAdditionalProperties hasUnflagged]
+ -[EDSortableThreadProxyAdditionalProperties isAuthenticated]
+ -[EDSortableThreadProxyAdditionalProperties isBlocked]
+ -[EDSortableThreadProxyAdditionalProperties isVIP]
+ -[EDSortableThreadProxyAdditionalProperties mailboxObjectIDs]
+ -[EDSortableThreadProxyAdditionalProperties numberOfMessagesInThread]
+ -[EDSortableThreadProxyAdditionalProperties readLater]
+ -[EDSortableThreadProxyAdditionalProperties sendLaterDate]
+ -[EDSortableThreadProxyAdditionalProperties senderList]
+ -[EDSortableThreadProxyAdditionalProperties setAllowAuthenticationWarning:]
+ -[EDSortableThreadProxyAdditionalProperties setBusinessID:]
+ -[EDSortableThreadProxyAdditionalProperties setBusinessLogoID:]
+ -[EDSortableThreadProxyAdditionalProperties setCategory:]
+ -[EDSortableThreadProxyAdditionalProperties setCcList:]
+ -[EDSortableThreadProxyAdditionalProperties setDisplayDate:]
+ -[EDSortableThreadProxyAdditionalProperties setDisplayMessageGlobalID:]
+ -[EDSortableThreadProxyAdditionalProperties setFlagColors:]
+ -[EDSortableThreadProxyAdditionalProperties setFlags:]
+ -[EDSortableThreadProxyAdditionalProperties setGeneratedSummary:]
+ -[EDSortableThreadProxyAdditionalProperties setHasAttachments:]
+ -[EDSortableThreadProxyAdditionalProperties setHasUnflagged:]
+ -[EDSortableThreadProxyAdditionalProperties setIsAuthenticated:]
+ -[EDSortableThreadProxyAdditionalProperties setIsBlocked:]
+ -[EDSortableThreadProxyAdditionalProperties setIsVIP:]
+ -[EDSortableThreadProxyAdditionalProperties setMailboxObjectIDs:]
+ -[EDSortableThreadProxyAdditionalProperties setNumberOfMessagesInThread:]
+ -[EDSortableThreadProxyAdditionalProperties setReadLater:]
+ -[EDSortableThreadProxyAdditionalProperties setSendLaterDate:]
+ -[EDSortableThreadProxyAdditionalProperties setSenderList:]
+ -[EDSortableThreadProxyAdditionalProperties setToList:]
+ -[EDSortableThreadProxyAdditionalProperties toList]
+ -[EDThreadQueryHandler _addSnippetHintsToExtraInfo:]
+ -[EDThreadQueryHandler initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:delegate:observationResumer:threadMigratorManager:]
+ -[EDThreadQueryHandler initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:delegate:observationResumer:threadMigratorManager:].cold.1
+ -[_EDInMemoryThreadCollectionOldestThreadsState .cxx_destruct]
+ -[_EDInMemoryThreadCollectionOldestThreadsState oldestThreadsByMailboxObjectIDs]
+ -[_EDInMemoryThreadCollectionOldestThreadsState setOldestThreadsByMailboxObjectIDs:]
+ _EDSearchableIndexQueryTransformerThreadDictionaryKeySnippetHints
+ _EFArraysAreEqual
+ _EMMessageListAddedItemsExtraInfoKeySnippetHintsByObjectID
+ _OBJC_CLASS_$_EDInMemoryThread
+ _OBJC_CLASS_$_EDInMemoryThreadCollection
+ _OBJC_CLASS_$_EDSectionQueryItemHelper
+ _OBJC_CLASS_$_EDSortableThreadProxy
+ _OBJC_CLASS_$_EDSortableThreadProxyAdditionalProperties
+ _OBJC_CLASS_$_EFMutableOrderedDictionary
+ _OBJC_CLASS_$_EMSearchableItemSnippetData
+ _OBJC_CLASS_$_EMThreadCollectionItemID
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$__EDInMemoryThreadCollectionOldestThreadsState
+ _OBJC_IVAR_$_EDInMemoryThread._displayMessage
+ _OBJC_IVAR_$_EDInMemoryThread._messages
+ _OBJC_IVAR_$_EDInMemoryThread._originatingQuery
+ _OBJC_IVAR_$_EDInMemoryThread._thread
+ _OBJC_IVAR_$_EDInMemoryThread._threadScope
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._comparator
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._conversationIDs
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._dataSource
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._dateSortOrder
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._delegate
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._inMemoryThreadCache
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._inMemoryThreadClass
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._inMemoryThreadsByConversationID
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._limitedCache
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._logClient
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._mailboxTypeResolver
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._mailboxesByConversationID
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._oldestThreadsByMailboxObjectIDs
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._query
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._sectionQueryHelper
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._threadScope
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._threadsByConversationID
+ _OBJC_IVAR_$_EDInMemoryThreadCollection._threadsLock
+ _OBJC_IVAR_$_EDSectionQueryItemHelper._query
+ _OBJC_IVAR_$_EDSectionQueryItemHelper._sectionComparator
+ _OBJC_IVAR_$_EDSectionQueryItemHelper._sectionIndexesByID
+ _OBJC_IVAR_$_EDSectionQueryItemHelper._sectionPredicates
+ _OBJC_IVAR_$_EDSortableThreadProxy._date
+ _OBJC_IVAR_$_EDSortableThreadProxy._objectID
+ _OBJC_IVAR_$_EDSortableThreadProxy._primarySortValue
+ _OBJC_IVAR_$_EDSortableThreadProxy._properties
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._allowAuthenticationWarning
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._businessID
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._businessLogoID
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._category
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._ccList
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._displayDate
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._displayMessageGlobalID
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._flagColors
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._flags
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._generatedSummary
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._hasAttachments
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._hasUnflagged
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._isAuthenticated
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._isBlocked
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._isVIP
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._mailboxObjectIDs
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._numberOfMessagesInThread
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._readLater
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._sendLaterDate
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._senderList
+ _OBJC_IVAR_$_EDSortableThreadProxyAdditionalProperties._toList
+ _OBJC_IVAR_$__EDInMemoryThreadCollectionOldestThreadsState._oldestThreadsByMailboxObjectIDs
+ _OBJC_METACLASS_$_EDInMemoryThread
+ _OBJC_METACLASS_$_EDInMemoryThreadCollection
+ _OBJC_METACLASS_$_EDSectionQueryItemHelper
+ _OBJC_METACLASS_$_EDSortableThreadProxy
+ _OBJC_METACLASS_$_EDSortableThreadProxyAdditionalProperties
+ _OBJC_METACLASS_$__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_$_CLASS_METHODS_EDInMemoryThread
+ __OBJC_$_CLASS_METHODS_EDInMemoryThreadCollection
+ __OBJC_$_CLASS_METHODS_EDSectionQueryItemHelper
+ __OBJC_$_CLASS_PROP_LIST_EDInMemoryThread
+ __OBJC_$_INSTANCE_METHODS_EDInMemoryThread
+ __OBJC_$_INSTANCE_METHODS_EDInMemoryThreadCollection
+ __OBJC_$_INSTANCE_METHODS_EDSectionQueryItemHelper
+ __OBJC_$_INSTANCE_METHODS_EDSortableThreadProxy
+ __OBJC_$_INSTANCE_METHODS_EDSortableThreadProxyAdditionalProperties
+ __OBJC_$_INSTANCE_METHODS__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_$_INSTANCE_VARIABLES_EDInMemoryThread
+ __OBJC_$_INSTANCE_VARIABLES_EDInMemoryThreadCollection
+ __OBJC_$_INSTANCE_VARIABLES_EDSectionQueryItemHelper
+ __OBJC_$_INSTANCE_VARIABLES_EDSortableThreadProxy
+ __OBJC_$_INSTANCE_VARIABLES_EDSortableThreadProxyAdditionalProperties
+ __OBJC_$_INSTANCE_VARIABLES__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_$_PROP_LIST_EDInMemoryThread
+ __OBJC_$_PROP_LIST_EDInMemoryThreadCollection
+ __OBJC_$_PROP_LIST_EDSectionQueryItemHelper
+ __OBJC_$_PROP_LIST_EDSortableThreadProxy
+ __OBJC_$_PROP_LIST_EDSortableThreadProxyAdditionalProperties
+ __OBJC_$_PROP_LIST_EDThreadQueryHandler.269
+ __OBJC_$_PROP_LIST__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDInMemoryThreadCollectionDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDInMemoryThreadCollectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EDInMemoryThreadCollectionDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EDInMemoryThreadCollectionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_EDInMemoryThread
+ __OBJC_CLASS_PROTOCOLS_$_EDSortableThreadProxy
+ __OBJC_CLASS_RO_$_EDInMemoryThread
+ __OBJC_CLASS_RO_$_EDInMemoryThreadCollection
+ __OBJC_CLASS_RO_$_EDSectionQueryItemHelper
+ __OBJC_CLASS_RO_$_EDSortableThreadProxy
+ __OBJC_CLASS_RO_$_EDSortableThreadProxyAdditionalProperties
+ __OBJC_CLASS_RO_$__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_LABEL_PROTOCOL_$_EDInMemoryThreadCollectionDataSource
+ __OBJC_LABEL_PROTOCOL_$_EDInMemoryThreadCollectionDelegate
+ __OBJC_METACLASS_RO_$_EDInMemoryThread
+ __OBJC_METACLASS_RO_$_EDInMemoryThreadCollection
+ __OBJC_METACLASS_RO_$_EDSectionQueryItemHelper
+ __OBJC_METACLASS_RO_$_EDSortableThreadProxy
+ __OBJC_METACLASS_RO_$_EDSortableThreadProxyAdditionalProperties
+ __OBJC_METACLASS_RO_$__EDInMemoryThreadCollectionOldestThreadsState
+ __OBJC_PROTOCOL_$_EDInMemoryThreadCollectionDataSource
+ __OBJC_PROTOCOL_$_EDInMemoryThreadCollectionDelegate
+ ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke.359
+ ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke.363
+ ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke_2.366
+ ___149-[EDThreadPersistence _persistenceDidUpdateMessages:forFilterPredicate:changedKeyPaths:predicateToIgnore:loggingString:generationWindow:messageTest:]_block_invoke.480
+ ___23+[EDInMemoryThread log]_block_invoke
+ ___32-[EDInMemoryThread addMessages:]_block_invoke
+ ___36-[EDBiomeBlackPearlLogger _database]_block_invoke
+ ___37-[EDInMemoryThreadCollection itemIDs]_block_invoke
+ ___38-[EDSectionQueryItemHelper removeIDs:]_block_invoke
+ ___39-[EDInMemoryThread _combinedFlagColors]_block_invoke
+ ___40+[EDInMemoryThread _dateSortDescriptors]_block_invoke
+ ___40-[EDInMemoryThreadCollection _hasLoaded]_block_invoke
+ ___44-[EDInMemoryThread _maxSearchRelevanceScore]_block_invoke
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke.cold.1
+ ___46-[EDInMemoryThread _createThreadWithObjectID:]_block_invoke_2
+ ___46-[EDInMemoryThread _recalculateDisplayMessage]_block_invoke
+ ___49-[EDInMemoryThreadCollection _didMergeInThreads:]_block_invoke
+ ___49-[EDInMemoryThreadCollection _threadsWereDeleted]_block_invoke
+ ___49-[EDInMemoryThreadCollection _threadsWereDeleted]_block_invoke_2
+ ___49-[EDSectionQueryItemHelper sectionNumbersForIDs:]_block_invoke
+ ___49-[EDSectionQueryItemHelper sectionNumbersForIDs:]_block_invoke_2
+ ___49-[EDSectionQueryItemHelper updateSectionForItem:]_block_invoke
+ ___50-[EDInMemoryThread updateMessage:fromOldObjectID:]_block_invoke
+ ___51-[EDBiomeBlackPearlLogger deleteEventsForMessages:]_block_invoke.23
+ ___52-[EDSectionQueryItemHelper _createSectionComparator]_block_invoke
+ ___52-[EDThreadQueryHandler _addSnippetHintsToExtraInfo:]_block_invoke
+ ___54-[EDThreadPersistence verifyConsistencyOfThreadScope:]_block_invoke.538
+ ___55-[EDSortableThreadProxy _sortValueForRawValue:keyPath:]_block_invoke
+ ___56-[EDSectionQueryItemHelper comparatorForItemComparator:]_block_invoke
+ ___58-[EDInMemoryThreadCollection messagesWereAdded:extraInfo:]_block_invoke
+ ___59-[EDInMemoryThreadCollection _removeThreadProxies:forMove:]_block_invoke
+ ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.48
+ ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.49
+ ___60-[EDSectionQueryItemHelper initWithQuery:sectionPredicates:]_block_invoke
+ ___62-[EDInMemoryThreadCollection inMemoryThreadForConversationID:]_block_invoke
+ ___62-[EDInMemoryThreadCollection initializeOldestThreadsByMailbox]_block_invoke
+ ___62-[EDInMemoryThreadCollection initializeOldestThreadsByMailbox]_block_invoke_2
+ ___63-[EDInMemoryThreadCollection _updateOldestThreadsForMailboxes:]_block_invoke
+ ___63-[EDInMemoryThreadCollection messageListItemForObjectID:error:]_block_invoke
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.234
+ ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.320
+ ___66-[EDInMemoryThread initWithMessages:originatingQuery:threadScope:]_block_invoke
+ ___66-[EDInMemoryThreadCollection clearOldestThreadsByMailboxObjectIDs]_block_invoke
+ ___67-[EDInMemoryThreadCollection _messagesByConversationIDForMessages:]_block_invoke
+ ___67-[EDMessageQueryHelper localSearchDidFindMessages:itemSnippetData:]_block_invoke
+ ___70-[EDInMemoryThreadCollection enumerateObjectIDsInBatchesOfSize:block:]_block_invoke
+ ___70-[EDInMemoryThreadCollection enumerateObjectIDsInBatchesOfSize:block:]_block_invoke_2
+ ___70-[EDInMemoryThreadCollection messagesWereChanged:forKeyPaths:deleted:]_block_invoke
+ ___70-[EDInMemoryThreadCollection messagesWereChanged:forKeyPaths:deleted:]_block_invoke_2
+ ___70-[EDInMemoryThreadQueryHandler itemIDsForStateCaptureWithErrorString:]_block_invoke
+ ___71-[EDMessageQueryHelper _snippetsByObjectIDForMessages:itemSnippetData:]_block_invoke
+ ___72-[EDInMemoryThreadCollection _inMemoryThreadsForObjectIDs:cacheResults:]_block_invoke
+ ___73+[EDInMemoryThreadCollection _comparisonForSortDescriptor:value1:value2:]_block_invoke
+ ___75-[EDThreadPersistence setPriorityForDisplayMessageSenderForThreadObjectID:]_block_invoke.500
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.15
+ ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.15.cold.1
+ ___78-[EDInMemoryThreadCollection _notifyObserverOfOldestThreadsByMailboxObjectIDs]_block_invoke
+ ___78-[EDInMemoryThreadCollection _notifyObserverOfOldestThreadsByMailboxObjectIDs]_block_invoke_2
+ ___79+[EDInMemoryThreadCollection _comparatorForInThreadProxiesWithSortDescriptors:]_block_invoke
+ ___84-[EDInMemoryThreadCollection conversationIDDidChangeForMessages:fromConversationID:]_block_invoke
+ ___85+[EDSectionQueryItemHelper _sectionIndexForItem:sectionPredicates:sectionIdentifier:]_block_invoke
+ ___88-[EDInMemoryThreadCollection objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke
+ ___88-[EDInMemoryThreadCollection objectIDDidChangeForMessage:oldObjectID:oldConversationID:]_block_invoke.69
+ ___89-[EDMessageRepository performQuery:withObserver:observationIdentifier:completionHandler:]_block_invoke
+ ___90-[EDInMemoryThreadCollection _updateCurrentOldestThreadWithThreadIfApplicable:forMailbox:]_block_invoke
+ ___90-[EDInMemoryThreadCollection _updateCurrentOldestThreadWithThreadIfApplicable:forMailbox:]_block_invoke_2
+ ___90-[EDMessageRepository _performQuery:withObserver:observationIdentifier:completionHandler:]_block_invoke
+ ___91-[EDInMemoryThreadCollection _createInMemoryThreadForConversationID:messages:cacheResults:]_block_invoke
+ ___95-[EDMessageQueryHelper localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:]_block_invoke
+ ___97-[EDThreadPersistence _updateThreadForDeleteWithObjectID:threadScopeDatabaseID:generationWindow:]_block_invoke.457
+ ___block_descriptor_32_e31_16?0"EDSortableThreadProxy"8l
+ ___block_descriptor_32_e40_"<EMCollectionItemID>"16?0"NSNumber"8l
+ ___block_descriptor_32_e41_"NSNumber"16?0"EDSortableThreadProxy"8l
+ ___block_descriptor_32_e49_"EMThreadObjectID"16?0"EDSortableThreadProxy"8l
+ ___block_descriptor_32_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8l
+ ___block_descriptor_40_e26_B16?0"EDInMemoryThread"8l
+ ___block_descriptor_40_ea8_32r_e12_v24?0Q8^B16lr32l8
+ ___block_descriptor_40_ea8_32r_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8lr32l8
+ ___block_descriptor_40_ea8_32s_e18_16?0"NSNumber"8ls32l8
+ ___block_descriptor_40_ea8_32s_e30_"EMObjectID"16?0"NSNumber"8ls32l8
+ ___block_descriptor_40_ea8_32s_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8ls32l8
+ ___block_descriptor_40_ea8_32w_e11_q24?0816lw32l8
+ ___block_descriptor_48_ea8_32s40bs_e11_q24?0816ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e21_v24?0"NSArray"8^B16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40r_e26_v32?0"EMMessage"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e44_v32?0"<ECEmailAddressConvertible>"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e57_v32?0"EMMailboxObjectID"8"EDSortableThreadProxy"16^B24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40s_e33_v32?0"CSSearchableItem"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e54_v24?0"EMMessageListItemChange"8"EMThreadObjectID"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e58_v32?0"EMThreadObjectID"8"EMMessageListItemChange"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e23_"EDInMemoryThread"8?0ls32l8
+ ___block_descriptor_48_ea8_32s_e55_v16?0"_EDInMemoryThreadCollectionOldestThreadsState"8ls32l8
+ ___block_descriptor_49_ea8_32s40s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e26_v32?0"EMMessage"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s_e23_"EDInMemoryThread"8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s_e57_q24?0"EDSortableThreadProxy"8"EDSortableThreadProxy"16ls32l8
+ ___block_descriptor_57_ea8_32s40s48r_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8r48l8
+ ___block_descriptor_57_ea8_32s40s48r_e38_v32?0"EDSortableThreadProxy"8Q16^B24ls32l8r48l8s40l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e29_v16?0"NSMutableDictionary"8lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_ea8_32s40s48r_e28_"EDSortableThreadProxy"8?0lr48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e33_v32?0"CSSearchableItem"8Q16^B24lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e27_v16?0"<EMThreadBuilder>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s56s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_89_ea8_32s40s48s56s64s72s_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.21
+ ___block_literal_global.22
+ ___block_literal_global.362
+ ___block_literal_global.374
+ ___block_literal_global.461
+ ___block_literal_global.467
+ ___block_literal_global.472
+ ___block_literal_global.479
+ ___block_literal_global.483
+ ___block_literal_global.492
+ ___block_literal_global.52
+ ___block_literal_global.59
+ ___block_literal_global.83
+ ___block_literal_global.9
+ ___block_literal_global.946
+ __combinedFlagColors.onceToken
+ __combinedFlagColors.sAllFlagColors
+ __database.onceToken
+ __database.s_database
+ __dateSortDescriptors.onceToken
+ __dateSortDescriptors.sDateSortDescriptors
+ __protocol_getMethodTypeEncoding
+ _objc_msgSend$_addMessagesToThread:
+ _objc_msgSend$_addSnippetHintsToExtraInfo:
+ _objc_msgSend$_calculateAndApplyChange
+ _objc_msgSend$_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:
+ _objc_msgSend$_combinedCCList
+ _objc_msgSend$_combinedFlagColors
+ _objc_msgSend$_combinedFlags
+ _objc_msgSend$_combinedHasAttachments
+ _objc_msgSend$_combinedHasUnflagged
+ _objc_msgSend$_combinedIsBlocked
+ _objc_msgSend$_combinedIsVIP
+ _objc_msgSend$_combinedMailboxes
+ _objc_msgSend$_combinedReadLater
+ _objc_msgSend$_combinedSenderList
+ _objc_msgSend$_combinedToList
+ _objc_msgSend$_comparatorForInThreadProxiesWithSortDescriptors:
+ _objc_msgSend$_copySortPropertiesForDescriptors:thread:
+ _objc_msgSend$_createSectionComparator
+ _objc_msgSend$_createThreadWithObjectID:
+ _objc_msgSend$_database
+ _objc_msgSend$_dateSortDescriptors
+ _objc_msgSend$_idForItem:
+ _objc_msgSend$_maxSearchRelevanceScore
+ _objc_msgSend$_newestDisplayDate
+ _objc_msgSend$_performQuery:withObserver:observationIdentifier:completionHandler:
+ _objc_msgSend$_recalculateDisplayMessage
+ _objc_msgSend$_registerSelector:types:
+ _objc_msgSend$_sectionIndexForItem:sectionIdentifier:
+ _objc_msgSend$_sectionIndexForItem:sectionPredicates:sectionIdentifier:
+ _objc_msgSend$_setValueFromThreadAndReturnIfChanged:keyPath:isPrimary:
+ _objc_msgSend$_snippetsByObjectIDForMessages:itemSnippetData:
+ _objc_msgSend$_sortValueForRawValue:keyPath:
+ _objc_msgSend$_targetForSelector:
+ _objc_msgSend$applyToMessageListItem:
+ _objc_msgSend$assertCorrectSchedulerForCollection:
+ _objc_msgSend$cachedObjectForKey:
+ _objc_msgSend$calculateChangeFromThread:
+ _objc_msgSend$changeMessages:forKeyPaths:threadIsEmpty:
+ _objc_msgSend$collection:didMergeInThreadsForMove:newObjectIDs:existingObjectID:extraInfo:hasChanges:
+ _objc_msgSend$collection:messagesInConversationIDs:limit:
+ _objc_msgSend$collection:notifyOfOldestThreadsByMailboxObjectIDs:
+ _objc_msgSend$collection:notifyReplacedExistingObjectID:newObjectID:
+ _objc_msgSend$collection:reportChanges:
+ _objc_msgSend$collection:reportDeletes:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$containsIndexes:
+ _objc_msgSend$dateSortOrder
+ _objc_msgSend$didSendUpdatesInCollection:
+ _objc_msgSend$displayMessage
+ _objc_msgSend$displayMessageGlobalID
+ _objc_msgSend$ef_arrayByAddingAbsentObjectsFromArray:
+ _objc_msgSend$ef_indexOfObject:usingComparator:
+ _objc_msgSend$idForItem:
+ _objc_msgSend$inMemoryThreadCache
+ _objc_msgSend$inMemoryThreadClass
+ _objc_msgSend$inMemoryThreadForConversationID:
+ _objc_msgSend$indexOfKey:
+ _objc_msgSend$initWithConversationID:
+ _objc_msgSend$initWithIdentifiers:snippetData:
+ _objc_msgSend$initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:
+ _objc_msgSend$initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:inMemoryThreadClass:
+ _objc_msgSend$initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:
+ _objc_msgSend$initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:delegate:observationResumer:threadMigratorManager:
+ _objc_msgSend$initWithQuery:sectionPredicates:
+ _objc_msgSend$initWithSearchableItemIdentifier:snippetHints:
+ _objc_msgSend$initWithThread:originatingQuery:
+ _objc_msgSend$isSubclassOfClass:
+ _objc_msgSend$localSearchDidFindMessages:itemSnippetData:
+ _objc_msgSend$localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:
+ _objc_msgSend$localizedCaseInsensitiveCompare:
+ _objc_msgSend$logClient
+ _objc_msgSend$mailboxesInCollection:
+ _objc_msgSend$messageListItem
+ _objc_msgSend$numberOfMessagesInThread
+ _objc_msgSend$oldestThreadsByMailboxObjectIDs
+ _objc_msgSend$originatingQuery
+ _objc_msgSend$prepareToSendUpdatesInCollection:
+ _objc_msgSend$properties
+ _objc_msgSend$removeIDs:
+ _objc_msgSend$removeMessages:threadIsEmpty:
+ _objc_msgSend$removeThreadProxies:forMove:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$sectionComparator
+ _objc_msgSend$sectionIdentifierForID:
+ _objc_msgSend$sectionNumberForID:
+ _objc_msgSend$sectionNumbersForIDs:
+ _objc_msgSend$setDisplayMessage:
+ _objc_msgSend$setDisplayMessageGlobalID:
+ _objc_msgSend$setMailboxObjectIDs:
+ _objc_msgSend$setNumberOfMessagesInThread:
+ _objc_msgSend$setOldestThreadsByMailboxObjectIDs:
+ _objc_msgSend$setOrAddObject:forKey:
+ _objc_msgSend$setOrInsertObject:forKey:atIndex:
+ _objc_msgSend$setPrimarySortValue:
+ _objc_msgSend$setProperties:
+ _objc_msgSend$setThread:
+ _objc_msgSend$setValue:forKeyPath:
+ _objc_msgSend$shouldSectionItemsRemainInSection
+ _objc_msgSend$snippetData
+ _objc_msgSend$updateFromThread:addingAdditionalInformation:query:
+ _objc_msgSend$updateMessage:fromOldObjectID:
- -[EDBiomeBlackPearlLogger database]
- -[EDBiomeBlackPearlLogger setDatabase:]
- -[EDInMemoryThreadQueryHandler initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:helperObserver:]
- -[EDInMemoryThreadQueryHandler initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:helperObserver:].cold.1
- -[EDInMemoryThreadQueryHandler messageQueryHelperDelegateImpl]
- -[EDInMemoryThreadQueryHandler queryHelperDelegate]
- -[EDMessageQueryHelper _mailRankingSignalsAndSnippetsByObjectIDForMessages:data:]
- -[EDMessageQueryHelper localSearchDidFindMessages:mailRankingAndSnippetHintsData:]
- -[EDMessageQueryHelper localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:]
- -[EDMessageRepository _performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:]
- -[EDMessageRepository _performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:].cold.1
- -[EDMessageRepository performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:]
- -[EDPersistenceHookRegistry _forwardStackInvocation:]
- -[EDPersistenceHookRegistry _registerSelector:]
- -[EDThreadQueryHandler _addSnippetHintsAndMailRankingSignalsToExtraInfo:]
- -[EDThreadQueryHandler helperObserver]
- -[EDThreadQueryHandler initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:helperObserver:delegate:observationResumer:threadMigratorManager:]
- -[EDThreadQueryHandler initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:helperObserver:delegate:observationResumer:threadMigratorManager:].cold.1
- -[_EDMessageQueryHelperDelegateImpl .cxx_destruct]
- -[_EDMessageQueryHelperDelegateImpl didFindAllMessagesBlock]
- -[_EDMessageQueryHelperDelegateImpl initWithMessageQueryHelperObserver:didFindAllMessagesBlock:]
- -[_EDMessageQueryHelperDelegateImpl observer]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:businessIDDidChangeForMessages:fromBusinessID:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:conversationIDDidChangeForMessages:fromConversationID:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didAddMessages:extraInfo:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didDeleteMessages:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didFindMessages:extraInfo:forInitialBatch:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didUpdateMessages:forKeyPaths:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:messageFlagsDidChangeForMessages:previousMessages:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:objectIDDidChangeForMessage:oldObjectID:oldConversationID:]
- -[_EDMessageQueryHelperDelegateImpl queryHelperDidFindAllMessages:]
- -[_EDMessageQueryHelperDelegateImpl queryHelperDidFinishRemoteSearch:]
- -[_EDMessageQueryHelperDelegateImpl queryHelperNeedsRestart:]
- -[_EDMessageQueryHelperDelegateImpl setDidFindAllMessagesBlock:]
- _EMMessageListAddedItemsExtraInfoKeyMailRankingAndSnippetHintsByObjectID
- _OBJC_CLASS_$_EMInMemoryThread
- _OBJC_CLASS_$_EMInMemoryThreadCollection
- _OBJC_CLASS_$_EMMessageMailRankingAndSnippetHintsPair
- _OBJC_CLASS_$_EMSearchableItemMailRankingAndSnippetHints
- _OBJC_CLASS_$_EMSectionQueryItemHelper
- _OBJC_CLASS_$__EDMessageQueryHelperDelegateImpl
- _OBJC_IVAR_$_EDBiomeBlackPearlLogger._database
- _OBJC_IVAR_$_EDInMemoryThreadQueryHandler._messageQueryHelperDelegateImpl
- _OBJC_IVAR_$_EDThreadQueryHandler._helperObserver
- _OBJC_IVAR_$__EDMessageQueryHelperDelegateImpl._didFindAllMessagesBlock
- _OBJC_IVAR_$__EDMessageQueryHelperDelegateImpl._observer
- _OBJC_METACLASS_$__EDMessageQueryHelperDelegateImpl
- _SearchFoundationLibraryCore.frameworkLibrary
- __OBJC_$_INSTANCE_METHODS__EDMessageQueryHelperDelegateImpl
- __OBJC_$_INSTANCE_VARIABLES__EDMessageQueryHelperDelegateImpl
- __OBJC_$_PROP_LIST_EDThreadQueryHandler.275
- __OBJC_$_PROP_LIST__EDMessageQueryHelperDelegateImpl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMInMemoryThreadCollectionDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EMInMemoryThreadCollectionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_EMInMemoryThreadCollectionDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_EMInMemoryThreadCollectionDelegate
- __OBJC_CLASS_PROTOCOLS_$__EDMessageQueryHelperDelegateImpl
- __OBJC_CLASS_RO_$__EDMessageQueryHelperDelegateImpl
- __OBJC_LABEL_PROTOCOL_$_EMInMemoryThreadCollectionDataSource
- __OBJC_LABEL_PROTOCOL_$_EMInMemoryThreadCollectionDelegate
- __OBJC_METACLASS_RO_$__EDMessageQueryHelperDelegateImpl
- __OBJC_PROTOCOL_$_EMInMemoryThreadCollectionDataSource
- __OBJC_PROTOCOL_$_EMInMemoryThreadCollectionDelegate
- ___104-[EDMessageRepository performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:]_block_invoke
- ___105-[EDMessageRepository _performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:]_block_invoke
- ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke.358
- ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke.362
- ___113-[EDThreadPersistence nextExistingThreadObjectIDForThreadObjectID:forSortKeys:journaledThreadsToCheck:excluding:]_block_invoke_2.365
- ___149-[EDThreadPersistence _persistenceDidUpdateMessages:forFilterPredicate:changedKeyPaths:predicateToIgnore:loggingString:generationWindow:messageTest:]_block_invoke.479
- ___200-[EDInMemoryThreadQueryHandler initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:helperObserver:]_block_invoke
- ___51-[EDBiomeBlackPearlLogger deleteEventsForMessages:]_block_invoke.21
- ___54-[EDThreadPersistence verifyConsistencyOfThreadScope:]_block_invoke.537
- ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.50
- ___59-[EDInMemoryThreadQueryHandler didSendUpdatesInCollection:]_block_invoke.51
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.232
- ___64-[EDThreadPersistence threadForObjectID:originatingQuery:error:]_block_invoke.319
- ___73-[EDThreadQueryHandler _addSnippetHintsAndMailRankingSignalsToExtraInfo:]_block_invoke
- ___75-[EDThreadPersistence setPriorityForDisplayMessageSenderForThreadObjectID:]_block_invoke.499
- ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.14
- ___76-[EDConcreteLocalSearchProvider topHitsSearchWithQuery:delegate:completion:]_block_invoke.14.cold.1
- ___81-[EDMessageQueryHelper _mailRankingSignalsAndSnippetsByObjectIDForMessages:data:]_block_invoke
- ___82-[EDMessageQueryHelper localSearchDidFindMessages:mailRankingAndSnippetHintsData:]_block_invoke
- ___95-[EDMessageQueryHelper localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:]_block_invoke
- ___97-[EDThreadPersistence _updateThreadForDeleteWithObjectID:threadScopeDatabaseID:generationWindow:]_block_invoke.456
- ___SearchFoundationLibraryCore_block_invoke
- ___block_descriptor_32_e31_16?0"EMSortableThreadProxy"8l
- ___block_descriptor_56_ea8_32s40s48s_e33_v32?0"CSSearchableItem"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s48r56r_e33_v32?0"CSSearchableItem"8Q16^B24lr48l8s32l8r56l8s40l8
- ___block_descriptor_64_ea8_32s40s48s56s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_ea8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.364
- ___block_literal_global.373
- ___block_literal_global.388
- ___block_literal_global.460
- ___block_literal_global.466
- ___block_literal_global.471
- ___block_literal_global.478
- ___block_literal_global.482
- ___block_literal_global.491
- ___block_literal_global.510
- ___block_literal_global.535
- ___block_literal_global.94
- ___block_literal_global.950
- ___getSFMailRankingSignalsClass_block_invoke
- _audit_stringSearchFoundation
- _expectedNumberEmbeddingDistances
- _getSFMailRankingSignalsClass.softClass
- _maxValidSqDistance
- _minValidSqDistance
- _objc_msgSend$_addSnippetHintsAndMailRankingSignalsToExtraInfo:
- _objc_msgSend$_mailRankingSignalsAndSnippetsByObjectIDForMessages:data:
- _objc_msgSend$_performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:
- _objc_msgSend$_registerSelector:
- _objc_msgSend$attributeDictionary
- _objc_msgSend$didFindAllMessagesBlock
- _objc_msgSend$floatValue
- _objc_msgSend$helperObserver
- _objc_msgSend$initWithIdentifiers:mailRankingAndSnippetHintsData:
- _objc_msgSend$initWithMailRankingSignals:snippetHints:
- _objc_msgSend$initWithMessageQueryHelperObserver:didFindAllMessagesBlock:
- _objc_msgSend$initWithQuery:mailboxTypeResolver:dataSource:delgate:scheduler:logClient:limitedCache:
- _objc_msgSend$initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:helperObserver:
- _objc_msgSend$initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:helperObserver:delegate:observationResumer:threadMigratorManager:
- _objc_msgSend$initWithSearchableItemIdentifier:mailRankingSignals:snippetHints:
- _objc_msgSend$isSemanticMatch
- _objc_msgSend$localSearchDidFindMessages:mailRankingAndSnippetHintsData:
- _objc_msgSend$localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:
- _objc_msgSend$mailRankingAndSnippetHintsData
- _objc_msgSend$mailRankingSignals
- _objc_msgSend$mailResultScoreL1
- _objc_msgSend$numberWithFloat:
- _objc_msgSend$observer
- _objc_msgSend$queryHelperBusinessIDDidChangeForMessages:fromBusinessID:
- _objc_msgSend$queryHelperConversationIDDidChangeForMessages:fromConversationID:
- _objc_msgSend$queryHelperConversationNotificationLevelDidChangeForConversation:conversationID:
- _objc_msgSend$queryHelperDelegate
- _objc_msgSend$queryHelperDidAddMessages:
- _objc_msgSend$queryHelperDidDeleteMessages:
- _objc_msgSend$queryHelperDidFindAllMessages
- _objc_msgSend$queryHelperDidFindMessages:
- _objc_msgSend$queryHelperDidFinishRemoteSearch
- _objc_msgSend$queryHelperDidUpdateMessages:forKeyPaths:
- _objc_msgSend$queryHelperMessageFlagsDidChangeForMessages:
- _objc_msgSend$queryHelperNeedsRestart
- _objc_msgSend$queryHelperObjectIDDidChangeForMessage:oldObjectID:oldConversationID:
- _objc_msgSend$setIsSemanticMatch:
- _objc_msgSend$setIsSyntacticMatch:
- _objc_msgSend$setSemanticScore:
- _objc_msgSend$setSyntacticScore:
- _spotlightRetrievalTypeSemantic
- _spotlightRetrievalTypeSyntactic
CStrings:
+ "#"
+ "%p: Changed objectID from %{public}@ for message in thread: %{public}@"
+ "%p: Could not find any messages for conversation ID: %{public}lld"
+ "%p: Created EDInMemoryThreadCollection (%p)"
+ "%p: Fetched %lu messages for %lu threads"
+ "%p: Fetched messageListItem for %{public}@ from cache"
+ "%p: Fetching messages for %{public}@"
+ "%p: Marking thread %{public}@ as deleted"
+ "%p: Marking thread proxy %{public}lld as deleted"
+ "%p: Marking threads from messages %{public}@ as deleted even though no messages were deleted."
+ "%p: Merged in %lu new threads %{public}@ to %{public}@ between existing threads %{public}@ and %{public}@"
+ "%p: Merged in %lu new threads out of order! %{public}@ to %{public}@ between existing threads %{public}@ and %{public}@"
+ "%p: Merged in 1 new thread %{public}@ between existing threads %{public}@ and %{public}@"
+ "%p: Merged in 1 new thread out of order! %{public}@ between existing threads %{public}@ and %{public}@"
+ "%p: Missing threadProxy in %{public}@. Created new threadProxy:%p for itemID:%{public}@"
+ "%p: No change detected for thread proxy with item ID: %lld, keyPaths: %{public}@"
+ "%p: No change detected for thread with item ID: %{public}@, keyPaths: %{public}@"
+ "%p: Oldest threads initialized for %u mailboxes"
+ "%p: Thread %{public}lld no longer exists."
+ "%p: Thread with conversation ID: %@ is not present in _inMemoryThreadsByConversationID."
+ "%p: Thread with conversation ID: %{public}lld is not present in _inMemoryThreadsByConversationID."
+ "%p: Unable to find thread for conversation ID: %lld"
+ "%p: Updating thread (%{public}@) with change: %{public}@, sectionDidChange: %{BOOL}d"
+ "%p: Updating thread proxy (%lld) with change: %{public}@, sectionDidChange: %{BOOL}d"
+ "%{public}@ held the database write connection for %0.05f seconds"
+ "<%@: %p> conversationID:%lld"
+ "@\"<EDInMemoryThreadCollectionDataSource>\""
+ "@\"<EDInMemoryThreadCollectionDelegate>\""
+ "@\"<EMCollectionItemID>\"16@?0@\"NSNumber\"8"
+ "@\"<EMMailboxTypeResolver>\""
+ "@\"EDInMemoryThread\"8@?0"
+ "@\"EDInMemoryThreadCollection\""
+ "@\"EDSectionQueryItemHelper\""
+ "@\"EDSortableThreadProxy\"8@?0"
+ "@\"EDSortableThreadProxyAdditionalProperties\""
+ "@\"EFMutableOrderedDictionary\""
+ "@\"EMGeneratedSummary\""
+ "@\"EMObjectID\"16@?0@\"NSNumber\"8"
+ "@\"EMReadLater\""
+ "@\"EMThreadObjectID\"16@?0@\"EDSortableThreadProxy\"8"
+ "@\"NSArray\"40@0:8@\"EDInMemoryThreadCollection\"16@\"NSArray\"24q32"
+ "@\"NSIndexSet\""
+ "@\"NSNumber\"16@?0@\"EDSortableThreadProxy\"8"
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSSet\"24@0:8@\"EDInMemoryThreadCollection\"16"
+ "@16@?0@\"EDSortableThreadProxy\"8"
+ "@16@?0@\"NSNumber\"8"
+ "@40@0:8@16@24^B32"
+ "@60@0:8@16@24@32@40@48B56"
+ "@68@0:8@16@24@32@40@48B56#60"
+ "@?24@0:8@?16"
+ "Attempting to transform thread %{public}@ with no category"
+ "B16@?0@\"EDInMemoryThread\"8"
+ "B32@0:8@\"EDInMemoryThreadCollection\"16@\"NSDictionary\"24"
+ "B32@0:8@\"EDInMemoryThreadCollection\"16@\"NSOrderedSet\"24"
+ "B36@0:8@\"EDInMemoryThreadCollection\"16@\"NSDictionary\"24B32"
+ "Caching thread for conversationID: %{public}lld displayDate = %@"
+ "Did update isUrgent for precomputed threads"
+ "Didn't find conversationID in Cache: %{public}lld, displayDate = %@"
+ "EDInMemoryThread"
+ "EDInMemoryThreadCollection"
+ "EDInMemoryThreadCollection.m"
+ "EDInMemoryThreadCollectionDataSource"
+ "EDInMemoryThreadCollectionDelegate"
+ "EDSearchableIndexQueryTransformer.snippetHints"
+ "EDSectionQueryItemHelper"
+ "EDSectionQueryItemHelper.m"
+ "EDSortableThreadProxy"
+ "EDSortableThreadProxy.m"
+ "EDSortableThreadProxyAdditionalProperties"
+ "Got a conversationID of 0"
+ "Message %{public}@ had conversationID 0"
+ "Multiple sort descriptors is unexpected"
+ "T#,R,N,V_inMemoryThreadClass"
+ "T@\"<EDInMemoryThreadCollectionDataSource>\",R,W,N,V_dataSource"
+ "T@\"<EDInMemoryThreadCollectionDelegate>\",R,W,N,V_delegate"
+ "T@\"<EMMailboxTypeResolver>\",R,N,V_mailboxTypeResolver"
+ "T@\"<EMMessageListItem>\",R,N"
+ "T@\"ECMessageFlags\",&,D,N"
+ "T@\"ECMessageFlags\",&,N,V_flags"
+ "T@\"EDSectionQueryItemHelper\",R,N,V_sectionQueryHelper"
+ "T@\"EDSortableThreadProxyAdditionalProperties\",&,N,V_properties"
+ "T@\"EFLazyCache\",R,N,V_inMemoryThreadCache"
+ "T@\"EMCategory\",&,D,N"
+ "T@\"EMGeneratedSummary\",&,D,N"
+ "T@\"EMGeneratedSummary\",&,N,V_generatedSummary"
+ "T@\"EMMessage\",&,N,V_displayMessage"
+ "T@\"EMQuery\",R,N,V_originatingQuery"
+ "T@\"EMReadLater\",&,D"
+ "T@\"EMReadLater\",&,V_readLater"
+ "T@\"EMThread\",&,N,V_thread"
+ "T@\"EMThreadObjectID\",R,C,N,V_objectID"
+ "T@\"EMThreadScope\",R,C,N,V_threadScope"
+ "T@\"NSArray\",&,D,N"
+ "T@\"NSArray\",&,N,V_mailboxObjectIDs"
+ "T@\"NSArray\",C,D,N"
+ "T@\"NSArray\",C,N,V_ccList"
+ "T@\"NSArray\",C,N,V_senderList"
+ "T@\"NSArray\",C,N,V_toList"
+ "T@\"NSDate\",&,D"
+ "T@\"NSDate\",&,V_date"
+ "T@\"NSDate\",&,V_displayDate"
+ "T@\"NSDate\",&,V_sendLaterDate"
+ "T@\"NSIndexSet\",C,D,N"
+ "T@\"NSIndexSet\",C,N,V_flagColors"
+ "T@\"NSMutableDictionary\",&,N,V_oldestThreadsByMailboxObjectIDs"
+ "T@\"NSObject<OS_os_log>\",&,N,V_logClient"
+ "T@,&,V_primarySortValue"
+ "T@?,R,C,N,V_sectionComparator"
+ "TB,N,V_allowAuthenticationWarning"
+ "TB,N,V_hasAttachments"
+ "TB,N,V_hasUnflagged"
+ "TB,N,V_isAuthenticated"
+ "TB,N,V_isBlocked"
+ "TB,N,V_limitedCache"
+ "TQ,D,N"
+ "TQ,N,V_numberOfMessagesInThread"
+ "Tq,D,N"
+ "Tq,N,V_displayMessageGlobalID"
+ "Updating isUrgent for precomputed threads"
+ "[%lld - %@]"
+ "[inMemoryThreadClass isSubclassOfClass:EDInMemoryThread.class]"
+ "[rawSortValue isKindOfClass:[NSIndexSet class]]"
+ "_EDInMemoryThreadCollectionOldestThreadsState"
+ "_addMessagesToThread:"
+ "_addSnippetHintsToExtraInfo:"
+ "_allowAuthenticationWarning"
+ "_cachedInMemoryThreadForConversationID called with conversationID %@"
+ "_calculateAndApplyChange"
+ "_calculateChangesAfterRemovingMessages:applyingChanges:threadIsEmpty:"
+ "_ccList"
+ "_combinedCCList"
+ "_combinedFlagColors"
+ "_combinedFlags"
+ "_combinedHasAttachments"
+ "_combinedHasUnflagged"
+ "_combinedIsBlocked"
+ "_combinedIsVIP"
+ "_combinedMailboxes"
+ "_combinedReadLater"
+ "_combinedSenderList"
+ "_combinedToList"
+ "_comparatorForInThreadProxiesWithSortDescriptors:"
+ "_conversationIDs"
+ "_copySortPropertiesForDescriptors:thread:"
+ "_createSectionComparator"
+ "_createThreadWithObjectID:"
+ "_dateSortDescriptors"
+ "_displayMessage"
+ "_displayMessageGlobalID"
+ "_flagColors"
+ "_generatedSummary"
+ "_hasAttachments"
+ "_hasUnflagged"
+ "_idForItem:"
+ "_inMemoryThreadCache"
+ "_inMemoryThreadClass"
+ "_inMemoryThreadsByConversationID"
+ "_isAuthenticated"
+ "_isBlocked"
+ "_isSortedByDate:"
+ "_limitedCache"
+ "_logClient"
+ "_mailboxObjectIDs"
+ "_mailboxTypeResolver"
+ "_mailboxesByConversationID"
+ "_maxSearchRelevanceScore"
+ "_newestDisplayDate"
+ "_numberOfMessagesInThread"
+ "_objectID"
+ "_oldestThreadsByMailboxObjectIDs"
+ "_originatingQuery"
+ "_performQuery:withObserver:observationIdentifier:completionHandler:"
+ "_properties"
+ "_readLater"
+ "_recalculateDisplayMessage"
+ "_registerSelector:types:"
+ "_sectionComparator"
+ "_sectionIndexForItem:sectionIdentifier:"
+ "_sectionIndexForItem:sectionPredicates:sectionIdentifier:"
+ "_sectionIndexesByID"
+ "_sendLaterDate"
+ "_senderList"
+ "_setValueFromThreadAndReturnIfChanged:keyPath:isPrimary:"
+ "_snippetsByObjectIDForMessages:itemSnippetData:"
+ "_sortValueForRawValue:keyPath:"
+ "_targetForSelector:"
+ "_threadsByConversationID"
+ "_threadsLock"
+ "_toList"
+ "applyToMessageListItem:"
+ "assertCorrectSchedulerForCollection:"
+ "cachedObjectForKey:"
+ "calculateChangeFromThread:"
+ "changeMessages:forKeyPaths:threadIsEmpty:"
+ "compare:options:"
+ "containsIndexes:"
+ "displayMessageGlobalID"
+ "ef_arrayByAddingAbsentObjectsFromArray:"
+ "ef_indexOfObject:usingComparator:"
+ "flagColors.lastIndex <= ECMessageFlagColorLast"
+ "forwardingTargetForSelector:"
+ "idForItem:"
+ "inMemoryThreadCache"
+ "inMemoryThreadClass"
+ "inMemoryThreadForConversationID:"
+ "indexOfKey:"
+ "initWithConversationID:"
+ "initWithIdentifiers:snippetData:"
+ "initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:"
+ "initWithQuery:mailboxTypeResolver:dataSource:delgate:logClient:limitedCache:inMemoryThreadClass:"
+ "initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:"
+ "initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:delegate:observationResumer:threadMigratorManager:"
+ "initWithQuery:sectionPredicates:"
+ "initWithSearchableItemIdentifier:snippetHints:"
+ "initWithThread:originatingQuery:"
+ "isSubclassOfClass:"
+ "limitedCache"
+ "localSearchDidFindMessages:itemSnippetData:"
+ "localSearchDidFindTopHits:itemSnippetData:rankingSignals:instantAnswer:"
+ "logClient"
+ "mailboxTypeResolver"
+ "messageListItem"
+ "numberOfMessagesInThread"
+ "oldestMessage"
+ "oldestThreadsByMailboxObjectIDs"
+ "oldestThreadsByMailboxObjectIDs should be only initialized once"
+ "originatingQuery"
+ "performQuery:withObserver:observationIdentifier:completionHandler:"
+ "q24@?0@\"EDSortableThreadProxy\"8@\"EDSortableThreadProxy\"16"
+ "query.targetClass == [EMThread class] || query.targetClass == [EMMessage class]"
+ "r"
+ "removeIDs:"
+ "removeMessages:threadIsEmpty:"
+ "removeThreadProxies:forMove:"
+ "replaceObjectAtIndex:withObject:"
+ "sectionComparator"
+ "sectionIdentifierForID:"
+ "sectionNumberForID:"
+ "sectionNumbersForIDs:"
+ "setDisplayMessage:"
+ "setDisplayMessageGlobalID:"
+ "setLimitedCache:"
+ "setLogClient:"
+ "setMailMessageHeader:"
+ "setMailboxObjectIDs:"
+ "setNumberOfMessagesInThread:"
+ "setOldestThreadsByMailboxObjectIDs:"
+ "setOrAddObject:forKey:"
+ "setOrInsertObject:forKey:atIndex:"
+ "setPrimarySortValue:"
+ "setProperties:"
+ "setThread:"
+ "setValue:forKeyPath:"
+ "shouldSectionItemsRemainInSection"
+ "snippetData"
+ "updateFromThread:addingAdditionalInformation:query:"
+ "updateMessage:fromOldObjectID:"
+ "v16@?0@\"_EDInMemoryThreadCollectionOldestThreadsState\"8"
+ "v24@0:8@\"EDInMemoryThreadCollection\"16"
+ "v24@?0@\"EMMessageListItemChange\"8@\"EMThreadObjectID\"16"
+ "v32@0:8:16r*24"
+ "v32@0:8@\"EDInMemoryThreadCollection\"16@\"NSDictionary\"24"
+ "v32@?0@\"<ECEmailAddressConvertible>\"8Q16^B24"
+ "v32@?0@\"EDSortableThreadProxy\"8Q16^B24"
+ "v32@?0@\"EMMailboxObjectID\"8@\"EDSortableThreadProxy\"16^B24"
+ "v32@?0@\"EMThreadObjectID\"8@\"EMMessageListItemChange\"16^B24"
+ "v40@0:8@\"EDInMemoryThreadCollection\"16@\"EMMessageObjectID\"24@\"EMMessageObjectID\"32"
+ "v48@0:8@\"EMQuery\"16@\"<EMMessageListItemQueryResultsObserver>\"24@\"EMObjectID\"32@?<v@?@\"<EFCancelable>\">40"
+ "v48@0:8@\"NSArray\"16@\"NSArray\"24@\"NSDictionary\"32@\"EMInstantAnswer\"40"
+ "v60@0:8@\"EDInMemoryThreadCollection\"16B24@\"NSArray\"28@\"EMObjectID\"36@\"NSDictionary\"44^B52"
+ "\xd1"
- "%p: Created EMInMemoryThreadCollection (%p)"
- "@\"<EMMessageQueryHelperObserver_xpc>\""
- "@\"BMSQLDatabase\""
- "@\"EMInMemoryThreadCollection\""
- "@\"EMSectionQueryItemHelper\""
- "@\"NSArray\"40@0:8@\"EMInMemoryThreadCollection\"16@\"NSArray\"24q32"
- "@\"NSSet\"24@0:8@\"EMInMemoryThreadCollection\"16"
- "@\"_EDMessageQueryHelperDelegateImpl\""
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "@16@?0@\"EMSortableThreadProxy\"8"
- "B32@0:8@\"EMInMemoryThreadCollection\"16@\"NSDictionary\"24"
- "B32@0:8@\"EMInMemoryThreadCollection\"16@\"NSOrderedSet\"24"
- "B36@0:8@\"EMInMemoryThreadCollection\"16@\"NSDictionary\"24B32"
- "Class getSFMailRankingSignalsClass(void)_block_invoke"
- "EDLocalSearchProvider.m"
- "EMInMemoryThreadCollectionDataSource"
- "EMInMemoryThreadCollectionDelegate"
- "FatClient"
- "SFMailRankingSignals"
- "T@\"<EMMessageQueryHelperObserver_xpc>\",R,N,V_helperObserver"
- "T@\"<EMMessageQueryHelperObserver_xpc>\",R,N,V_observer"
- "T@\"BMSQLDatabase\",&,N,V_database"
- "T@\"EMSectionQueryItemHelper\",R,N,V_sectionQueryHelper"
- "T@\"_EDMessageQueryHelperDelegateImpl\",R,N,V_messageQueryHelperDelegateImpl"
- "T@?,C,N,V_didFindAllMessagesBlock"
- "_EDMessageQueryHelperDelegateImpl"
- "_addSnippetHintsAndMailRankingSignalsToExtraInfo:"
- "_didFindAllMessagesBlock"
- "_forwardStackInvocation:"
- "_helperObserver"
- "_mailRankingSignalsAndSnippetsByObjectIDForMessages:data:"
- "_messageQueryHelperDelegateImpl"
- "_observer"
- "_performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:"
- "_registerSelector:"
- "com_apple_mail_message_id_header"
- "didFindAllMessagesBlock"
- "floatValue"
- "helperObserver"
- "initWithIdentifiers:mailRankingAndSnippetHintsData:"
- "initWithMailRankingSignals:snippetHints:"
- "initWithMessageQueryHelperObserver:didFindAllMessagesBlock:"
- "initWithQuery:mailboxTypeResolver:dataSource:delgate:scheduler:logClient:limitedCache:"
- "initWithQuery:messagePersistence:hookRegistry:remindMeNotificationController:vipManager:searchProvider:observer:observationIdentifier:observationResumer:helperObserver:"
- "initWithQuery:messagePersistence:threadPersistence:hookRegistry:vipManager:searchProvider:remindMeNotificationController:observer:observationIdentifier:helperObserver:delegate:observationResumer:threadMigratorManager:"
- "initWithSearchableItemIdentifier:mailRankingSignals:snippetHints:"
- "isSemanticMatch"
- "localSearchDidFindMessages:mailRankingAndSnippetHintsData:"
- "localSearchDidFindTopHits:mailRankingAndSnippetHintsData:instantAnswer:"
- "mailRankingAndSnippetHintsData"
- "mailRankingSignals"
- "mailResultScoreL1"
- "messageQueryHelperDelegateImpl"
- "numberWithFloat:"
- "observer"
- "performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:"
- "queryHelperBusinessIDDidChangeForMessages:fromBusinessID:"
- "queryHelperConversationIDDidChangeForMessages:fromConversationID:"
- "queryHelperConversationNotificationLevelDidChangeForConversation:conversationID:"
- "queryHelperDelegate"
- "queryHelperDidAddMessages:"
- "queryHelperDidDeleteMessages:"
- "queryHelperDidFindAllMessages"
- "queryHelperDidFindMessages:"
- "queryHelperDidFinishRemoteSearch"
- "queryHelperDidUpdateMessages:forKeyPaths:"
- "queryHelperMessageFlagsDidChangeForMessages:"
- "queryHelperNeedsRestart"
- "queryHelperObjectIDDidChangeForMessage:oldObjectID:oldConversationID:"
- "setDidFindAllMessagesBlock:"
- "setIsSemanticMatch:"
- "setIsSyntacticMatch:"
- "setSemanticScore:"
- "setSyntacticScore:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation"
- "v24@0:8@\"EMInMemoryThreadCollection\"16"
- "v32@0:8@\"EMInMemoryThreadCollection\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSArray\"16@\"NSDictionary\"24"
- "v32@0:8{objc_method_description=:*}16"
- "v40@0:8@\"EMInMemoryThreadCollection\"16@\"EMMessageObjectID\"24@\"EMMessageObjectID\"32"
- "v40@0:8@\"NSArray\"16@\"NSDictionary\"24@\"EMInstantAnswer\"32"
- "v48@0:8@\"NSArray\"16q24@\"EMObjectID\"32@?<v@?@\"NSArray\">40"
- "v56@0:8@\"EMQuery\"16@\"<EMMessageListItemQueryResultsObserver>\"24@\"EMObjectID\"32@\"<EMMessageQueryHelperObserver_xpc>\"40@?<v@?@\"<EFCancelable>\">48"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@\"EMInMemoryThreadCollection\"16B24@\"NSArray\"28@\"EMObjectID\"36@\"NSDictionary\"44^B52"
- "void *SearchFoundationLibrary(void)"
- "\xe1"

```
