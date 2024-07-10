## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/Versions/A/EmailDaemon`

```diff

-3812.100.13.1.1
-  __TEXT.__text: 0x241798
-  __TEXT.__auth_stubs: 0x2050
-  __TEXT.__objc_methlist: 0x11af4
-  __TEXT.__gcc_except_tab: 0x429a0
-  __TEXT.__const: 0x17f8
-  __TEXT.__cstring: 0x1d347
-  __TEXT.__oslogstring: 0x14666
+3810.100.6.0.0
+  __TEXT.__text: 0x23ee7c
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0x119e4
+  __TEXT.__gcc_except_tab: 0x42424
+  __TEXT.__const: 0x17e8
+  __TEXT.__cstring: 0x1d177
+  __TEXT.__oslogstring: 0x14496
   __TEXT.__ustring: 0x2c
   __TEXT.__dlopen_cstrs: 0x57
   __TEXT.__swift5_typeref: 0x629

   __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_capture: 0xb0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe970
+  __TEXT.__unwind_info: 0xe850
   __TEXT.__eh_frame: 0x670
   __TEXT.__objc_classname: 0x2b3c
-  __TEXT.__objc_methname: 0x34365
-  __TEXT.__objc_methtype: 0x79fb
-  __TEXT.__objc_stubs: 0x21b80
-  __DATA_CONST.__got: 0x1910
-  __DATA_CONST.__const: 0x1ac8
+  __TEXT.__objc_methname: 0x33f52
+  __TEXT.__objc_methtype: 0x7a01
+  __TEXT.__objc_stubs: 0x21880
+  __DATA_CONST.__got: 0x18f8
+  __DATA_CONST.__const: 0x1aa0
   __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa900
+  __DATA_CONST.__objc_selrefs: 0xa838
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x538
-  __AUTH_CONST.__auth_got: 0x1038
+  __AUTH_CONST.__auth_got: 0xfb0
   __AUTH_CONST.__auth_ptr: 0x2a8
-  __AUTH_CONST.__const: 0xa280
-  __AUTH_CONST.__cfstring: 0xf6c0
-  __AUTH_CONST.__objc_const: 0x247b0
+  __AUTH_CONST.__const: 0xa1f0
+  __AUTH_CONST.__cfstring: 0xf560
+  __AUTH_CONST.__objc_const: 0x246d0
   __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x2d98
   __AUTH.__data: 0xa18
-  __DATA.__objc_ivar: 0x14ec
+  __DATA.__objc_ivar: 0x14d8
   __DATA.__data: 0x2ef8
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x2300

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9557
-  Symbols:   23719
-  CStrings:  3005
+  Functions: 9520
+  Symbols:   23605
+  CStrings:  2987
 
Symbols:
+ -[EDInMemoryThreadQueryHandler queryHelper:didFindMessages:]
+ -[EDMessageQueryHandler queryHelper:didFindMessages:]
+ -[EDPrecomputedThreadQueryHandler _extaInfoPrefetchedThreadsForObjectIDs:]
+ -[EDPrecomputedThreadQueryHandler _extaInfoPrefetchedThreadsForObjectIDs:].cold.1
+ -[_EDMessageItemIDCollector queryHelper:didFindMessages:]
+ -[_EDMessageQueryHelperDelegateImpl queryHelper:didFindMessages:]
+ GCC_except_table260
+ GCC_except_table290
+ GCC_except_table319
+ _EMMessageListChangedItemsExtraInfoKeyPrefetchedItems
+ __105-[EDSenderPersistence _addressesGroupedByContactForAddresses:unmatchedAddresses:otherAddressesByContact:]_block_invoke.185
+ __106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.40
+ __110-[EDMessageRepository startCountingQuery:includingServerCountsForMailboxScope:withObserver:completionHandler:]_block_invoke.225
+ __119-[EDSenderPersistence _blockOrUnblockSendersForAddresses:block:blockedAddressDatabaseIDs:connection:addressesToUpdate:]_block_invoke.170
+ __136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.259
+ __138-[EDCategorySubsystem initWithPersistence:userProfileProvider:vipManager:sourceApplicationBundleIdentifier:categorizationAnalyticsLogger:]_block_invoke.20
+ __140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.205
+ __140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.213
+ __41-[_EDThreadPositionChangeSet description]_block_invoke.374
+ __41-[_EDThreadPositionChangeSet description]_block_invoke.381
+ __48-[EDSenderPersistence _blockedSendersDidChange:]_block_invoke.155
+ __49-[EDLocalActionPersistence removeMessageActions:]_block_invoke.261
+ __50-[EDMessageCategorizer _categorizeMappedMessages:]_block_invoke.143
+ __52-[EDMessageQueryHandler queryHelper:didAddMessages:]_block_invoke.20
+ __54-[EDMessageCategorizer persistenceWillAddNewMessages:]_block_invoke.92
+ __54-[EDMessageCategorizer persistenceWillAddNewMessages:]_block_invoke.96
+ __55-[_EDThreadPositionChangeSet addObjectIDToMove:before:]_block_invoke.407
+ __57-[EDSenderPersistence _combineDictionary:withDictionary:]_block_invoke.178
+ __58-[EDSenderPersistence _reloadBlockedSendersWithAddresses:]_block_invoke.161
+ __60-[EDMessageChangeManager _persistResults:forTransferAction:]_block_invoke.230
+ __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.70
+ __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.70.cold.1
+ __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.74
+ __61-[EDBusinessPersistence persistenceDidReconcileProtectedData]_block_invoke.123
+ __61-[EDMessageRepository _enumerateObjectIDsByScope:usingBlock:]_block_invoke.246
+ __64-[EDLocalActionPersistence _labelChangeActionForRow:connection:]_block_invoke.131
+ __67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.34
+ __67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.232
+ __72-[EDMessageChangeManager _persistFlagChangeResults:forFlagChangeAction:]_block_invoke.216
+ __75-[EDMessageChangeManager _storeServerMessages:mailboxURL:generationWindow:]_block_invoke.239
+ __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.53
+ __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.58
+ __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.62
+ __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.118
+ __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.121
+ __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.127
+ __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.27
+ __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.27.cold.1
+ __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.38
+ __99-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:categoryType:connection:newSenders:]_block_invoke.137
+ __99-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:categoryType:connection:newSenders:]_block_invoke_2.138
+ ___138-[EDCategorySubsystem initWithPersistence:userProfileProvider:vipManager:sourceApplicationBundleIdentifier:categorizationAnalyticsLogger:]_block_invoke
+ ___53-[EDMessageQueryHandler queryHelper:didFindMessages:]_block_invoke
+ ___59-[EDMessageChangeManager deleteLocalMessageActionsWithIDs:]_block_invoke
+ ___74-[EDPrecomputedThreadQueryHandler _extaInfoPrefetchedThreadsForObjectIDs:]_block_invoke
+ ___block_descriptor_32_e28_"NSNumber"16?0"NSString"8l
+ ___block_descriptor_48_ea8_32s40w_e30_v16?0"BGFastPassSystemTask"8l
+ ___block_descriptor_48_ea8_32s40w_e31_v16?0"BGRepeatingSystemTask"8l
+ ___block_descriptor_56_ea8_32r40r48w_e5_v8?0l
+ __block_literal_global.136
+ __block_literal_global.174
+ __block_literal_global.181
+ __block_literal_global.199
+ __block_literal_global.206
+ __block_literal_global.223
+ __block_literal_global.233
+ __block_literal_global.244
+ __block_literal_global.386
+ __block_literal_global.469
+ __block_literal_global.530
+ __block_literal_global.77
+ __block_literal_global.927
+ __block_literal_global.929
+ __block_literal_global.99
+ _objc_msgSend$_extaInfoPrefetchedThreadsForObjectIDs:
+ _objc_msgSend$messageActionPersistentID
+ _objc_msgSend$queryHelper:didFindMessages:
+ _objc_msgSend$setMessageActionPersistentID:
- -[EDBusinessPersistence _businessesTablesNeedBackfillWithConnection:]
- -[EDBusinessPersistence backfillBusinessesTables]
- -[EDCategorySubsystem _startCategoryMigrationWithBGTask:andReason:]
- -[EDCategorySubsystem activityPersistence]
- -[EDCategorySubsystem categoryPersistence]
- -[EDCategorySubsystem messagePersistence]
- -[EDCategorySubsystem start]
- -[EDDiagnosticInfoGatherer _compressDatabaseAtURL:intoDirectoryURL:]
- -[EDDiagnosticInfoGatherer _compressDirectoryAtURL:intoArchiveWithURL:]
- -[EDDiagnosticInfoGatherer _copyDatabaseFromURL:intoDatabaseAtURL:]
- -[EDDiagnosticInfoGatherer _copyFromDatabase:intoDatabase:]
- -[EDDiagnosticInfoGatherer _copySearchIndexerDatabaseIntoDirectoryURL:]
- -[EDDiagnosticInfoGatherer _copySearchIndexerDatabaseIntoDirectoryURL:].cold.1
- -[EDDiagnosticInfoGatherer _copySearchIndexerDatabaseIntoDirectoryURL:].cold.2
- -[EDInMemoryThreadQueryHandler queryHelper:didFindMessages:forInitialBatch:]
- -[EDLocalActionPersistence latestActionID]
- -[EDMessageQueryHandler _extraInfoForMessages:messagesToPrecache:outObjectIDs:]
- -[EDMessageQueryHandler _messagesBeforeMessageWithObjectID:fromMessagesFromQueryHelper:afterRequestedMessage:]
- -[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:]
- -[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:]
- -[EDMessageQueryHandler _requestedItemObjectID]
- -[EDMessageQueryHandler didFindRequestedItemForInitialBatch]
- -[EDMessageQueryHandler queryHelper:didFindMessages:forInitialBatch:]
- -[EDMessageQueryHandler setDidFindRequestedItemForInitialBatch:]
- -[EDMessageRepository _performQuery:withObserver:observationIdentifier:helperObserver:completionHandler:].cold.1
- -[EDMessageRepository setSharedOneTimeCodeUserDefaults:]
- -[EDMessageRepository sharedOneTimeCodeUserDefaults]
- -[EDPrecomputedThreadQueryHandler _extaInfoPrecachedThreadsForInitialObjectIDs:]
- -[EDPrecomputedThreadQueryHandler _extaInfoPrecachedThreadsForInitialObjectIDs:].cold.1
- -[_EDMessageItemIDCollector queryHelper:didFindMessages:forInitialBatch:]
- -[_EDMessageQueryHelperDelegateImpl queryHelper:didFindMessages:forInitialBatch:]
- GCC_except_table211
- GCC_except_table316
- GCC_except_table320
- GCC_except_table321
- GCC_except_table322
- OBJC_IVAR_$_EDCategorySubsystem._activityPersistence
- OBJC_IVAR_$_EDCategorySubsystem._categoryPersistence
- OBJC_IVAR_$_EDCategorySubsystem._messagePersistence
- OBJC_IVAR_$_EDMessageQueryHandler._didFindRequestedItemForInitialBatch
- OBJC_IVAR_$_EDMessageRepository._sharedOneTimeCodeUserDefaults
- _AAArchiveStreamClose
- _AAArchiveStreamWritePathList
- _AAByteStreamClose
- _AACompressionOutputStreamOpen
- _AAEncodeArchiveOutputStreamOpen
- _AAFieldKeySetCreateWithString
- _AAFieldKeySetDestroy
- _AAFileStreamOpenWithPath
- _AAPathListCreateWithDirectoryContents
- _AAPathListDestroy
- _EDCategoryPersistenceUserCategoryTemporarilyCategorizedMarker
- _EMMessageListChangedItemsExtraInfoKeyPrecachedItems
- _EMMessageListQueryOptionPrecacheAndIncludeItemWithObjectIDInInitialBatch
- _EMMessageListQueryOptionPrecacheItemsInInitialBatchWithCount
- _OBJC_CLASS_$_ECLocalMessageActionID
- __105-[EDSenderPersistence _addressesGroupedByContactForAddresses:unmatchedAddresses:otherAddressesByContact:]_block_invoke.189
- __106-[EDMessageQueryHandler queryHelper:conversationNotificationLevelDidChangeForConversation:conversationID:]_block_invoke.46
- __110-[EDMessageRepository startCountingQuery:includingServerCountsForMailboxScope:withObserver:completionHandler:]_block_invoke.226
- __119-[EDSenderPersistence _blockOrUnblockSendersForAddresses:block:blockedAddressDatabaseIDs:connection:addressesToUpdate:]_block_invoke.174
- __136-[EDMessageRepository messageListItemsForObjectIDs:requestID:observationIdentifier:loadSummaryForAdditionalObjectIDs:completionHandler:]_block_invoke.260
- __140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.209
- __140-[EDSenderPersistence handleReconciliationMergeErrorForTable:columnName:statement:journalRowID:protectedRowID:connection:rowsUpdated:error:]_block_invoke.217
- __28-[EDCategorySubsystem start]_block_invoke.17
- __41-[_EDThreadPositionChangeSet description]_block_invoke.372
- __41-[_EDThreadPositionChangeSet description]_block_invoke.379
- __48-[EDSenderPersistence _blockedSendersDidChange:]_block_invoke.159
- __49-[EDBusinessPersistence backfillBusinessesTables]_block_invoke.67
- __49-[EDLocalActionPersistence removeMessageActions:]_block_invoke.259
- __50-[EDMessageCategorizer _categorizeMappedMessages:]_block_invoke.146
- __50-[EDMessageCategorizer _categorizeMappedMessages:]_block_invoke.cold.3
- __52-[EDMessageQueryHandler queryHelper:didAddMessages:]_block_invoke.28
- __54-[EDMessageCategorizer persistenceWillAddNewMessages:]_block_invoke.95
- __54-[EDMessageCategorizer persistenceWillAddNewMessages:]_block_invoke.99
- __55-[_EDThreadPositionChangeSet addObjectIDToMove:before:]_block_invoke.405
- __57-[EDSenderPersistence _combineDictionary:withDictionary:]_block_invoke.182
- __58-[EDSenderPersistence _reloadBlockedSendersWithAddresses:]_block_invoke.165
- __60-[EDMessageChangeManager _persistResults:forTransferAction:]_block_invoke.227
- __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.71
- __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.71.cold.1
- __60-[EDMessageRepository performQuery:limit:completionHandler:]_block_invoke.75
- __61-[EDBusinessPersistence persistenceDidReconcileProtectedData]_block_invoke.131
- __61-[EDMessageRepository _enumerateObjectIDsByScope:usingBlock:]_block_invoke.247
- __64-[EDLocalActionPersistence _labelChangeActionForRow:connection:]_block_invoke.132
- __67-[EDMessageQueryHandler queryHelper:didUpdateMessages:forKeyPaths:]_block_invoke.40
- __67-[EDMessageRepository startObservingOneTimeCode:completionHandler:]_block_invoke.233
- __72-[EDMessageChangeManager _persistFlagChangeResults:forFlagChangeAction:]_block_invoke.212
- __75-[EDMessageChangeManager _storeServerMessages:mailboxURL:generationWindow:]_block_invoke.236
- __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.59
- __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.68
- __86+[EDMessageQueryHandler findMessagesByPreviousObjectIDForAddedMessages:messageSource:]_block_invoke.70
- __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.122
- __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.129
- __86-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:connection:newSenders:]_block_invoke.135
- __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.54
- __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.54.cold.1
- __90-[EDDiagnosticInfoGatherer _downloadMessagesWithObjectIDs:directoryURL:completionPromise:]_block_invoke.64
- __99-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:categoryType:connection:newSenders:]_block_invoke.141
- __99-[EDSenderPersistence _addNewSendersForEmailAddresses:toBucket:categoryType:connection:newSenders:]_block_invoke_2.142
- ___102-[EDMessagePersistence _predicatesSeparatedByMailboxOrAccountForOrPredicate:containsMailboxPredicate:]_block_invoke
- ___110-[EDMessageQueryHandler _messagesBeforeMessageWithObjectID:fromMessagesFromQueryHelper:afterRequestedMessage:]_block_invoke
- ___28-[EDCategorySubsystem start]_block_invoke
- ___42-[EDLocalActionPersistence latestActionID]_block_invoke
- ___42-[EDLocalActionPersistence latestActionID]_block_invoke_2
- ___49-[EDBusinessPersistence backfillBusinessesTables]_block_invoke
- ___49-[EDBusinessPersistence backfillBusinessesTables]_block_invoke_2
- ___71-[EDDiagnosticInfoGatherer _compressDirectoryAtURL:intoArchiveWithURL:]_block_invoke
- ___72-[EDMessageQueryHandler _reportFoundMessages:before:messagesToPrecache:]_block_invoke
- ___80-[EDPrecomputedThreadQueryHandler _extaInfoPrecachedThreadsForInitialObjectIDs:]_block_invoke
- ___94-[EDMessageQueryHandler _messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:]_block_invoke
- ___block_descriptor_32_e16_i28?0I8r*12^v20l
- ___block_descriptor_32_e42_"NSString"16?0"ECLocalMessageActionID"8l
- ___block_descriptor_40_ea8_32s_e26_B32?0"EMMessage"8Q16^B24l
- ___block_descriptor_40_ea8_32w_e30_v16?0"BGFastPassSystemTask"8l
- ___block_descriptor_40_ea8_32w_e31_v16?0"BGRepeatingSystemTask"8l
- ___block_descriptor_48_ea8_32s40s_e54_v32?0"NSNumber"8"<ECEmailAddressConvertible>"16^B24l
- ___block_descriptor_64_ea8_32s40r48r56w_e5_v8?0l
- ___block_descriptor_64_ea8_32s40s48r56r_e28_v32?0"NSPredicate"8Q16^B24l
- ___copy_helper_block_ea8_32s40r48r56w
- ___destroy_helper_block_ea8_32s40r48r56w
- __block_literal_global.125
- __block_literal_global.185
- __block_literal_global.203
- __block_literal_global.221
- __block_literal_global.230
- __block_literal_global.241
- __block_literal_global.339
- __block_literal_global.384
- __block_literal_global.466
- __block_literal_global.532
- __block_literal_global.67
- __block_literal_global.80
- __block_literal_global.931
- __block_literal_global.933
- _entryMessageProc
- _kMCCCategoryIsNonPersonalAccountKey
- _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
- _objc_msgSend$_businessesTablesNeedBackfillWithConnection:
- _objc_msgSend$_compressDatabaseAtURL:intoDirectoryURL:
- _objc_msgSend$_compressDirectoryAtURL:intoArchiveWithURL:
- _objc_msgSend$_copyDatabaseFromURL:intoDatabaseAtURL:
- _objc_msgSend$_copyFromDatabase:intoDatabase:
- _objc_msgSend$_copySearchIndexerDatabaseIntoDirectoryURL:
- _objc_msgSend$_extaInfoPrecachedThreadsForInitialObjectIDs:
- _objc_msgSend$_extraInfoForMessages:messagesToPrecache:outObjectIDs:
- _objc_msgSend$_messagesBeforeMessageWithObjectID:fromMessagesFromQueryHelper:afterRequestedMessage:
- _objc_msgSend$_messagesForInitialBatchWithMessagesFromQueryHelper:requestedMessage:
- _objc_msgSend$_reportFoundMessages:before:messagesToPrecache:
- _objc_msgSend$_requestedItemObjectID
- _objc_msgSend$_startCategoryMigrationWithBGTask:andReason:
- _objc_msgSend$accountPropertyForKey:
- _objc_msgSend$didFindRequestedItemForInitialBatch
- _objc_msgSend$findOrCreateBusinessIDForAddress:connection:
- _objc_msgSend$isNonPersonalAccount
- _objc_msgSend$nullIf:second:
- _objc_msgSend$queryHelper:didFindMessages:forInitialBatch:
- _objc_msgSend$receiverEmail
- _objc_msgSend$setBusiness:forAddress:connection:
- _objc_msgSend$setDidFindRequestedItemForInitialBatch:
- _objc_msgSend$setIsNonPersonalAccount:
- _objc_msgSend$sharedOneTimeCodeUserDefaults
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$systemAccount
- _objc_msgSend$temporaryDirectory
- _sqlite3_backup_finish
- _sqlite3_backup_init
- _sqlite3_backup_step
- _sqlite3_close
- _sqlite3_close_v2
- _sqlite3_open_v2
- _sqlite3_sleep
CStrings:
+ "@\"NSNumber\"16@?0@\"NSString\"8"
- "%!x(MISSING)%!x(MISSING)"
- "%!x(MISSING)%!x(MISSING).aar"
- "-[EDBusinessPersistence backfillBusinessesTables]"
- "-[EDLocalActionPersistence latestActionID]"
- ".aar"
- "@\"NSString\"16@?0@\"ECLocalMessageActionID\"8"
- "B32@?0@\"EMMessage\"8Q16^B24"
- "FLG,MTM,CTM,DAT,SH5"
- "SELECT MAX(ROWID) as latest FROM local_message_actions"
- "SearchIndexer"
- "SearchIndexer-database"
- "com.apple.email.EDSenderPersistence.updateSentToFilter"
- "database"
- "i28@?0I8r*12^v20"
- "kMCCCategoryIsNonPersonalAccountKey"
- "latest"
- "main"
- "nop_sa"
- "v32@?0@\"NSNumber\"8@\"<ECEmailAddressConvertible>\"16^B24"

```
