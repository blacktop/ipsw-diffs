## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0x28e0d8
-  __TEXT.__objc_methlist: 0x136b4
-  __TEXT.__const: 0x53fc
-  __TEXT.__gcc_except_tab: 0x4afc0
-  __TEXT.__cstring: 0x2989a
-  __TEXT.__oslogstring: 0x1b684
+3901.300.26.0.0
+  __TEXT.__text: 0x28b8b4
+  __TEXT.__objc_methlist: 0x138e4
+  __TEXT.__const: 0x525c
+  __TEXT.__gcc_except_tab: 0x4b5ec
+  __TEXT.__cstring: 0x2a17a
+  __TEXT.__oslogstring: 0x1b354
   __TEXT.__dlopen_cstrs: 0x415
   __TEXT.__ustring: 0x26
-  __TEXT.__swift5_typeref: 0x18a2
-  __TEXT.__constg_swiftt: 0x1128
+  __TEXT.__constg_swiftt: 0x10e0
+  __TEXT.__swift5_typeref: 0x1766
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x114f
-  __TEXT.__swift5_fieldmd: 0x16b0
+  __TEXT.__swift5_reflstr: 0x10df
+  __TEXT.__swift5_fieldmd: 0x15fc
   __TEXT.__swift5_assocty: 0x260
-  __TEXT.__swift5_proto: 0x3a8
-  __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift5_capture: 0x89c
+  __TEXT.__swift5_capture: 0x8ec
+  __TEXT.__swift5_proto: 0x3a4
+  __TEXT.__swift5_types: 0x1d0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x12878
-  __TEXT.__eh_frame: 0x16f8
+  __TEXT.__unwind_info: 0x12950
+  __TEXT.__eh_frame: 0x15f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x95d0
-  __DATA_CONST.__objc_classlist: 0x9f8
+  __DATA_CONST.__const: 0x96d8
+  __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb3a8
+  __DATA_CONST.__objc_selrefs: 0xb500
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x6d8
-  __DATA_CONST.__got: 0x1ed0
-  __AUTH_CONST.__const: 0x7c58
-  __AUTH_CONST.__cfstring: 0xffa0
-  __AUTH_CONST.__objc_const: 0x229a0
+  __DATA_CONST.__got: 0x1ee0
+  __AUTH_CONST.__const: 0x7ad0
+  __AUTH_CONST.__cfstring: 0x10320
+  __AUTH_CONST.__objc_const: 0x22c50
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__auth_got: 0x1828
-  __DATA.__objc_ivar: 0x149c
-  __DATA.__data: 0xcf0
+  __AUTH.__objc_data: 0xc0
+  __AUTH.__data: 0xb8
+  __DATA.__objc_ivar: 0x14c0
+  __DATA.__data: 0xd70
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x6900
-  __DATA_DIRTY.__data: 0x4bc0
-  __DATA_DIRTY.__bss: 0x1d38
+  __DATA_DIRTY.__objc_data: 0x6890
+  __DATA_DIRTY.__data: 0x4ac0
+  __DATA_DIRTY.__bss: 0x1d48
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11707
-  Symbols:   15331
-  CStrings:  5546
+  Functions: 11720
+  Symbols:   15387
+  CStrings:  5570
 
Symbols:
+ +[EDAddMailboxRemoteIDUpgradeStep log]
+ +[EDAddMailboxRemoteIDUpgradeStep runWithConnection:error:]
+ -[EDAccountRepository bestAccountMatchForMaskedEmailAddress:completionHandler:]
+ -[EDAccountRepository receivingAccounts]
+ -[EDFetchController expectingOneTimeCodeUntilDateWithReply:]
+ -[EDFetchController performDelayedTasks]
+ -[EDFetchController startExpectingOneTimeCode]
+ -[EDFetchController stopExpectingOneTimeCode]
+ -[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]
+ -[EDMessagePersistence enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMin:block:]
+ -[EDMessagePersistence enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox:excluding:inLatest:dateReceivedMin:kind:block:]
+ -[EDOutgoingMessageRepository canCancelLastDelayedMessage:]
+ -[EDSearchableIndex _indexItems:fromRefresh:immediately:completion:]
+ -[EDSearchableIndex _runCompletionHandlersForPendingItems:]
+ -[EDSearchableIndex accountDonationGeneration]
+ -[EDSearchableIndex accountDonationPendingToken]
+ -[EDSearchableIndex accountDonationRetryAttempt]
+ -[EDSearchableIndex accountDonationRetryToken]
+ -[EDSearchableIndex accountDonationScheduler]
+ -[EDSearchableIndex accountsProvider]
+ -[EDSearchableIndex indexItems:fromRefresh:immediately:completion:]
+ -[EDSearchableIndex indexItems:immediately:completion:]
+ -[EDSearchableIndex searchIndexScheduler]
+ -[EDSearchableIndex setAccountDonationGeneration:]
+ -[EDSearchableIndex setAccountDonationPendingToken:]
+ -[EDSearchableIndex setAccountDonationRetryAttempt:]
+ -[EDSearchableIndex setAccountDonationRetryToken:]
+ -[EDSearchableIndex setAccountDonationScheduler:]
+ -[EDSearchableIndex setAccountsProvider:]
+ -[EDSearchableIndexManager _donateAccountsIfPossible]
+ -[EDSearchableIndexManager accountsProvider]
+ -[EDSearchableIndexManager downloadStatistics]
+ -[EDSearchableIndexManager initWithDatabase:messagePersistence:richLinkPersistence:hookRegistry:accountsProvider:]
+ -[EDSearchableIndexPendingItem addCompletionHandler:]
+ -[EDSearchableIndexPendingItem completionHandlers]
+ -[EDSearchableIndexPendingItem runCompletionHandlers]
+ -[EDSearchableIndexPendingItem setCompletionHandlers:]
+ -[NSIndexSet(EDServerMessagePersistence) _singleUIDQueryExpressionWithTableName:]
+ -[NSIndexSet(EDServerMessagePersistence) ed_enumerateUIDsWithLimit:reverseEnumeration:uidCountLimit:batchLimit:usingBlock:]
+ -[NSIndexSet(EDServerMessagePersistence) ed_nextRangesWithUIDCountLimit:reverseEnumeration:]
+ -[NSIndexSet(EDServerMessagePersistence) ed_uidQueryExpressionWithTableName:allowingSubExpressions:]
+ GCC_except_table186
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table315
+ GCC_except_table327
+ GCC_except_table340
+ GCC_except_table349
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table356
+ _EDMailboxRoleFromSpecialUseAttributes
+ _EMStringForAccountMatch
+ _OBJC_CLASS_$_EDAccountMatcher
+ _OBJC_CLASS_$_EDAddMailboxRemoteIDUpgradeStep
+ _OBJC_CLASS_$_EMAccountMatchResult
+ _OBJC_CLASS_$_EMOneTimeCodeAccelerator
+ _OBJC_IVAR_$_EDSearchableIndex._accountDonationGeneration
+ _OBJC_IVAR_$_EDSearchableIndex._accountDonationPendingToken
+ _OBJC_IVAR_$_EDSearchableIndex._accountDonationRetryAttempt
+ _OBJC_IVAR_$_EDSearchableIndex._accountDonationRetryToken
+ _OBJC_IVAR_$_EDSearchableIndex._accountDonationScheduler
+ _OBJC_IVAR_$_EDSearchableIndex._accountsProvider
+ _OBJC_IVAR_$_EDSearchableIndex._searchIndexScheduler
+ _OBJC_IVAR_$_EDSearchableIndexManager._accountsProvider
+ _OBJC_IVAR_$_EDSearchableIndexManager._downloadStatistics
+ _OBJC_IVAR_$_EDSearchableIndexPendingItem._completionHandlers
+ _OBJC_METACLASS_$_EDAccountMatcher
+ _OBJC_METACLASS_$_EDAddMailboxRemoteIDUpgradeStep
+ __CLASS_METHODS_EDAccountMatcher
+ __DATA_EDAccountMatcher
+ __INSTANCE_METHODS_EDAccountMatcher
+ __METACLASS_DATA_EDAccountMatcher
+ __OBJC_$_CLASS_METHODS_EDAddMailboxRemoteIDUpgradeStep
+ __OBJC_$_CLASS_METHODS_EDSearchableIndex(AccountDonation|SwiftAPIs)
+ __OBJC_$_INSTANCE_METHODS_EDMailboxPersistence(ServerMetadata|SyncInfo|RemoteID)
+ __OBJC_$_INSTANCE_METHODS_EDSearchableIndex(AccountDonation|SwiftAPIs)
+ __OBJC_$_PROP_LIST_EDAddMailboxRemoteIDUpgradeStep
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EFScheduler
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EFScheduler
+ __OBJC_$_PROTOCOL_REFS_EFScheduler
+ __OBJC_CLASS_PROTOCOLS_$_EDAddMailboxRemoteIDUpgradeStep
+ __OBJC_CLASS_RO_$_EDAddMailboxRemoteIDUpgradeStep
+ __OBJC_LABEL_PROTOCOL_$_EFScheduler
+ __OBJC_METACLASS_RO_$_EDAddMailboxRemoteIDUpgradeStep
+ __OBJC_PROTOCOL_$_EFScheduler
+ ___126-[EDMessagePersistence enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox:excluding:inLatest:dateReceivedMin:kind:block:]_block_invoke
+ ___137-[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke
+ ___137-[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_2
+ ___137-[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_3
+ ___137-[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]_block_invoke_4
+ ___38+[EDAddMailboxRemoteIDUpgradeStep log]_block_invoke
+ ___40-[EDAccountRepository receivingAccounts]_block_invoke
+ ___61-[EDSearchableIndexState removeIdentifiersFromPendingQueues:]_block_invoke_2
+ ___67-[EDSearchableIndex indexItems:fromRefresh:immediately:completion:]_block_invoke
+ ___68-[EDSearchableIndex _indexItems:fromRefresh:immediately:completion:]_block_invoke
+ ___68-[EDSearchableIndex _indexItems:fromRefresh:immediately:completion:]_block_invoke_2
+ ___79-[EDAccountRepository bestAccountMatchForMaskedEmailAddress:completionHandler:]_block_invoke
+ ___81-[NSIndexSet(EDServerMessagePersistence) _singleUIDQueryExpressionWithTableName:]_block_invoke
+ ___92-[NSIndexSet(EDServerMessagePersistence) ed_nextRangesWithUIDCountLimit:reverseEnumeration:]_block_invoke
+ ___block_descriptor_32_e30_B16?0"<EDReceivingAccount>"8l
+ ___block_descriptor_32_e43_"<EDReceivingAccount>"16?0"<EDAccount>"8l
+ ___block_descriptor_48_ea8_32r_e42_B48?0{EDMessageRemoteIDAndGlobal=IIqqqq}8lr32l8
+ ___block_descriptor_48_ea8_32s40r_e12_v24?0Q8^B16ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40s_e24_v32?0{_NSRange=QQ}8^B24ls32l8s40l8
+ ___block_descriptor_56_ea8_32bs40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_58_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_96_ea8_32s40bs_e41_B16?0"EDPersistenceDatabaseConnection"8ls32l8s40l8
+ ___swift_closure_destructorTm
+ ___swift_get_extra_inhabitant_index.40Tm
+ ___swift_memcpy65_8
+ ___swift_store_extra_inhabitant_index.41Tm
+ _associated conformance 11EmailDaemon17SearchableAccountVSHAASQ
+ _flat unique So11EFScheduler_p
+ _flat unique So18EDReceivingAccount_p
+ _symbolic SJ
+ _symbolic So17EDSearchableIndexC
+ _symbolic So17EDSearchableIndexCSgXw
+ _symbolic So17EDSearchableIndexCSgXwz_Xx
+ _symbolic _____ 11EmailDaemon17SearchableAccountV
+ _symbolic _____ 11EmailDaemon20MaskedAddressPattern33_61DA52624BA157F7E3EED8CCB8825D69LLV
+ _symbolic _____ So17EDSearchableIndexC11EmailDaemonE22AccountDonationTriggerO
+ _symbolic _____Sg 11EmailDaemon20MaskedAddressPattern33_61DA52624BA157F7E3EED8CCB8825D69LLV
+ _symbolic ______p So11EFSchedulerP
+ _symbolic ______p So18EDReceivingAccountP
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____y_____G 17_StringProcessing5RegexV AA03AnyC6OutputV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 11EmailDaemon17SearchableAccountV
+ _symbolic _____y_____GSg 17_StringProcessing5RegexV AA03AnyC6OutputV
+ _symbolic _____y______G 17_StringProcessing5RegexV5MatchV AA03AnyC6OutputV
+ _symbolic _____y______GSg 17_StringProcessing5RegexV5MatchV AA03AnyC6OutputV
+ _type_layout_string 11EmailDaemon17SearchableAccountV
- -[EDFetchController performFetchForOTC]
- -[EDSearchableIndex _indexItems:fromRefresh:immediately:]
- -[EDSearchableIndexManager downloadRequestQueue]
- -[EDSearchableIndexManager initWithDatabase:messagePersistence:richLinkPersistence:hookRegistry:]
- -[EDSearchableIndexManager setDownloadRequestQueue:]
- -[NSIndexSet(EDServerMessagePersistence) ed_enumerateUIDsWithLimit:reverseEnumeration:queryRangeCountLimit:batchLimit:usingBlock:]
- -[NSIndexSet(EDServerMessagePersistence) ed_nextRangesWithRangeCountLimit:reverseEnumeration:]
- GCC_except_table301
- GCC_except_table308
- GCC_except_table310
- GCC_except_table323
- GCC_except_table335
- GCC_except_table348
- _OBJC_CLASS_$_EDSearchableIndexDownloadRequestQueue
- _OBJC_IVAR_$_EDSearchableIndexManager._downloadRequestQueue
- _OBJC_METACLASS_$_EDSearchableIndexDownloadRequestQueue
- __DATA_EDSearchableIndexDownloadRequestQueue
- __INSTANCE_METHODS_EDSearchableIndexDownloadRequestQueue
- __IVARS_EDSearchableIndexDownloadRequestQueue
- __METACLASS_DATA_EDSearchableIndexDownloadRequestQueue
- __OBJC_$_CLASS_METHODS_EDSearchableIndex(SwiftAPIs)
- __OBJC_$_INSTANCE_METHODS_EDMailboxPersistence(ServerMetadata|SyncInfo)
- __OBJC_$_INSTANCE_METHODS_EDSearchableIndex(SwiftAPIs)
- __OBJC_$_PROP_LIST_EDSearchableIndexStateProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDSearchableIndexStateProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_EDSearchableIndexStateProvider
- __OBJC_$_PROTOCOL_REFS_EDSearchableIndexStateProvider
- __OBJC_LABEL_PROTOCOL_$_EDSearchableIndexStateProvider
- __OBJC_PROTOCOL_$_EDSearchableIndexStateProvider
- __PROPERTIES_EDSearchableIndexDownloadRequestQueue
- __PROTOCOLS_EDSearchableIndexDownloadRequestQueue
- ___56-[EDSearchableIndex indexItems:fromRefresh:immediately:]_block_invoke
- ___57-[EDSearchableIndex _indexItems:fromRefresh:immediately:]_block_invoke
- ___94-[NSIndexSet(EDServerMessagePersistence) ed_nextRangesWithRangeCountLimit:reverseEnumeration:]_block_invoke
- ___block_descriptor_50_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___swift_closure_destructor.20Tm
- ___swift_closure_destructor.32Tm
- ___swift_get_extra_inhabitant_index.39Tm
- ___swift_memcpy20_8
- ___swift_memcpy36_8
- ___swift_store_extra_inhabitant_index.40Tm
- _associated conformance So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0C0VSHACSQ
- _flat unique So18EDIndexableAccount_p
- _symbolic SDySo20EDPersistedMessageIDCSSG
- _symbolic SDySo20EDPersistedMessageIDC_____G 11EmailDaemon30EDSearchableIndexDownloadStateV19IndexingMessageInfoV
- _symbolic SaySo16EDIndexedMessageCG
- _symbolic SaySo20EDPersistedMessageIDCG
- _symbolic Say_____G 11EmailDaemon30EDSearchableIndexDownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _symbolic Say_____G So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0C0V
- _symbolic Shy_____G s6UInt32V
- _symbolic So37EDSearchableIndexDownloadRequestQueueC
- _symbolic So37EDSearchableIndexDownloadRequestQueueCXDXMT
- _symbolic _____ 11EmailDaemon30EDSearchableIndexDownloadStateV
- _symbolic _____ 11EmailDaemon30EDSearchableIndexDownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _symbolic _____ 11EmailDaemon30EDSearchableIndexDownloadStateV16ProcessedRequestV
- _symbolic _____ 11EmailDaemon30EDSearchableIndexDownloadStateV19IndexingMessageInfoV
- _symbolic _____ So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0C0V
- _symbolic _____ So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0D6ResultO
- _symbolic _____Iegn_ So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0D6ResultO
- _symbolic ______p So18EDIndexableAccountP
- _symbolic _____ySay_____GG s18DiscontiguousSliceV 11EmailDaemon30EDSearchableIndexDownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _symbolic _____ySay_____G_G s18DiscontiguousSliceV5IndexV 11EmailDaemon012EDSearchableC13DownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _symbolic _____ySiG s8RangeSetV
- _symbolic _____ySi_G s8RangeSetV6RangesV
- _symbolic _____ySo20EDPersistedMessageIDCSSG s18_DictionaryStorageC
- _symbolic _____ySo20EDPersistedMessageIDC_____G s18_DictionaryStorageC 11EmailDaemon30EDSearchableIndexDownloadStateV19IndexingMessageInfoV
- _symbolic _____y_____G s11_SetStorageC s6UInt32V
- _symbolic _____y_____G s23_ContiguousArrayStorageC 11EmailDaemon30EDSearchableIndexDownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 11EmailDaemon30EDSearchableIndexDownloadStateV16ProcessedRequestV
- _symbolic _____y_____ySi_GG s5SliceV s8RangeSetV6RangesV
- _symbolic _____y_____y_____ySi_GGG s16IndexingIteratorV s5SliceV s8RangeSetV6RangesV
- _symbolic _____yy_____cG s23_ContiguousArrayStorageC So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0G6ResultO
- _symbolic y_____c So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0D6ResultO
- _symbolic yyc
- _type_layout_string 11EmailDaemon30EDSearchableIndexDownloadStateV
- _type_layout_string 11EmailDaemon30EDSearchableIndexDownloadStateV14PendingRequest33_D1C92A0F222AE7180EED8636CF6AA8DCLLV
- _type_layout_string 11EmailDaemon30EDSearchableIndexDownloadStateV16ProcessedRequestV
- _type_layout_string 11EmailDaemon30EDSearchableIndexDownloadStateV19IndexingMessageInfoV
- _type_layout_string So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0C0V
- _type_layout_string So37EDSearchableIndexDownloadRequestQueueC11EmailDaemonE0D6ResultO
CStrings:
+ " AND "
+ " messages.date_received <= %llu"
+ " messages.date_received >= %llu"
+ "%p: fetching %llu UIDs, limit %llu, reverse %{BOOL}d, UID count limit %llu, batch limit %llu."
+ "(%@ = %lu)"
+ "(%@ IN ("
+ "(server_messages.remote_id < %llu OR %llu <= server_messages.remote_id)"
+ "))"
+ ", %lu"
+ ",%llu"
+ "-[EDFetchController expectingOneTimeCodeUntilDateWithReply:]"
+ "-[EDFetchController startExpectingOneTimeCode]"
+ "-[EDFetchController stopExpectingOneTimeCode]"
+ "-[EDMessagePersistence _enumerateMessageRemoteIDAndGlobalForMailbox:excluding:inLatest:dateReceivedMax:dateReceivedMin:limit:kind:block:]"
+ "-[EDOutgoingMessageRepository canCancelLastDelayedMessage:]"
+ "@\"<EDReceivingAccount>\"16@?0@\"<EDAccount>\"8"
+ "ALTER TABLE mailboxes ADD COLUMN remote_id TEXT COLLATE BINARY;"
+ "Account %s is active with no email address"
+ "B16@?0@\"<EDReceivingAccount>\"8"
+ "B48@?0{EDMessageRemoteIDAndGlobal=IIqqqq}8"
+ "Best match for masked email address %{public}s: %{public}s (matchingAccountIsActive=%{bool,public}d)"
+ "Could not execute sqlite statement: %@"
+ "Donated %{public}ld account item(s): %s"
+ "EDAccountMatcher"
+ "EXISTS (  SELECT global_message_id     FROM message_attachments LEFT OUTER     JOIN searchable_attachments ON message_attachments.rowid = searchable_attachments.attachment_id     WHERE message_attachments.global_message_id = messages.global_message_id       AND searchable_attachments.attachment_id IS NULL       AND message_attachments.attachment IS NOT NULL )"
+ "Enabling indexing (beginScheduling: %{public}d)"
+ "Failed to collapse runs of mask characters in the masked address: %{public}s"
+ "Failed to donate %{public}ld account item(s) of type(s) [%{public}s] [%s]: %{public}s"
+ "Failed to get a valid Unicode scalar for the mask character, so cannot match masked email addresses"
+ "Giving up on account donation after %{public}ld attempts"
+ "Not donating accounts: no accounts provider is set"
+ "Not reconciling account items: the accounts provider went away"
+ "Reconciling account items (trigger: %{public}s)"
+ "Retrying account donation in %{public}fs (attempt %{public}ld)"
+ "SELECT messages.global_message_id, server_messages.remote_id, messages.size, messages.date_received, messages.ROWID, messages.flags FROM (SELECT * FROM messages WHERE mailbox == %llu AND deleted = '0'       ORDER BY date_received DESC LIMIT %llu) AS messages INNER JOIN server_messages ON messages.ROWID = server_messages.message LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE %@ ORDER BY messages.date_received DESC"
+ "SELECT messages.global_message_id, server_messages.remote_id, messages.size, messages.date_received, messages.ROWID, messages.flags FROM messages INNER JOIN server_messages ON messages.ROWID = server_messages.message LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE messages.mailbox == %llu AND %@ ORDER BY messages.date_received DESC"
+ "SELECT remote_id\nFROM mailboxes\nWHERE rowid = ?"
+ "UPDATE mailboxes\nSET remote_id = ?\nWHERE rowid = ?"
+ "UPDATE mailboxes\nSET remote_id = NULL\nWHERE rowid = ?"
+ "Updating remote_id for %llu but no such row."
+ "\\All"
+ "\\Archive"
+ "\\Drafts"
+ "\\Flagged"
+ "\\Important"
+ "\\Junk"
+ "\\Sent"
+ "\\Trash"
+ "_enumerateMessageRemoteIDAndGlobalUsingBatchesForMailbox took %.3g s (%zi iterations)"
+ "accountDonation"
+ "com.apple.email.SearchableIndexDownloadStatistics"
+ "consuming %lu items out of a potential %lu new processingItems"
+ "error adding remote_id column"
+ "handler"
+ "messages.deleted = '0'"
+ "messages.searchable_message IS NULL"
+ "searchIndex"
+ "searchable_messages.message_body_indexed = 0"
+ "searchable_messages.transaction_id IN (%@, %@)"
+ "server_messages.remote_id NOT IN (%@)"
+ "\x81"
+ "\xf0R1"
- "%ld pending requests remaining"
- "%p: fetching %llu UIDs, limit %llu, reverse %{BOOL}d, range count limit %llu, batch limit %llu."
- "-[EDFetchController performFetchForOTC]"
- "Added %ld messages (skipped: %ld duplicate, stopped: %s)"
- "Adding %ld messages for persisting"
- "Daily download limit reached (%ld >= %ld), completing request with no messages"
- "EmailDaemon_Private.EDSearchableIndexDownloadRequestQueue"
- "Marking %ld messages as downloaded and persisted"
- "No capacity available, queuing request (%ld existing requests) (current pressure: %{iec-bytes}d / %{iec-bytes}d, %ld items)"
- "Over quota for indexing"
- "Persisted message IDs requested = %s"
- "Processing %ld pending requests"
- "Remaining messages being downloaded for persisting: %ld"
- "Removed %ld handlers for abandoned requests"
- "Removed %ld indexed messages, freed %{iec-bytes}d (current pressure: %{iec-bytes}d / %{iec-bytes}d, %ld items)"
- "Requesting to download %ld messages for indexing (requested memory: %lld bytes)"
- "Resolved download policy for account %{public}s host=%s quota=%{public}s"
- "Resolving download policy for account %{public}s with no hostname, expected an IMAP account"
- "Returning %ld messages for indexing"
- "Returning %s messages for indexing"
- "Returning over quota for indexing"
- "Searchable index abandoning %ld requests"
- "Searchable index failed to index %ld messages"
- "Searchable index indexed %ld messages"
- "SearchableIndexDownloadPolicy"
- "SearchableIndexDownloadState"
- "Server unavailable, completing request with no messages"
- "Stopped adding: download quota limit reached (%ld >= %ld)"
- "Stopped adding: inflight message limit reached (%ld >= %ld)"
- "Stopped adding: memory pressure limit reached (would be %{iec-bytes}d > %{iec-bytes}d)"
- "Stopped adding: server was recently unavailable"
- "Stopped adding: total count limit reached (%ld >= %ld)"
- "Total messages being downloaded for persisting: %ld"
- "Total pending requests: %ld"
- "Trying to add %ld messages (max total: %ld, current total: %ld)"
- "com.apple.email.SearchableIndexDownloadState"
- "consuming %lu items out of a potential %lu new processingItems: %{public}@"
- "\xf0R"
```
