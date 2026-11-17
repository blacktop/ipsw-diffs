## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3901.300.26.0.0
-  __TEXT.__text: 0x28b8b4
-  __TEXT.__objc_methlist: 0x138e4
-  __TEXT.__const: 0x525c
-  __TEXT.__gcc_except_tab: 0x4b5ec
-  __TEXT.__cstring: 0x2a17a
-  __TEXT.__oslogstring: 0x1b354
+3901.300.60.0.0
+  __TEXT.__text: 0x2911f4
+  __TEXT.__objc_methlist: 0x13a34
+  __TEXT.__const: 0x52ac
+  __TEXT.__gcc_except_tab: 0x4b980
+  __TEXT.__cstring: 0x2a81a
+  __TEXT.__oslogstring: 0x1b404
   __TEXT.__dlopen_cstrs: 0x415
   __TEXT.__ustring: 0x26
-  __TEXT.__constg_swiftt: 0x10e0
-  __TEXT.__swift5_typeref: 0x1766
+  __TEXT.__constg_swiftt: 0x1118
+  __TEXT.__swift5_typeref: 0x17fc
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x10df
-  __TEXT.__swift5_fieldmd: 0x15fc
+  __TEXT.__swift5_reflstr: 0x10ef
+  __TEXT.__swift5_fieldmd: 0x1618
   __TEXT.__swift5_assocty: 0x260
-  __TEXT.__swift5_capture: 0x8ec
-  __TEXT.__swift5_proto: 0x3a4
-  __TEXT.__swift5_types: 0x1d0
+  __TEXT.__swift5_capture: 0x9d8
+  __TEXT.__swift5_proto: 0x3a8
+  __TEXT.__swift5_types: 0x1d4
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x12950
-  __TEXT.__eh_frame: 0x15f8
+  __TEXT.__unwind_info: 0x12b20
+  __TEXT.__eh_frame: 0x16a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x96d8
-  __DATA_CONST.__objc_classlist: 0xa00
+  __DATA_CONST.__const: 0x9720
+  __DATA_CONST.__objc_classlist: 0xa08
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb500
+  __DATA_CONST.__objc_selrefs: 0xb5b8
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_arraydata: 0x6d8
-  __DATA_CONST.__got: 0x1ee0
-  __AUTH_CONST.__const: 0x7ad0
-  __AUTH_CONST.__cfstring: 0x10320
-  __AUTH_CONST.__objc_const: 0x22c50
+  __DATA_CONST.__objc_arraydata: 0x6e0
+  __DATA_CONST.__got: 0x1ef8
+  __AUTH_CONST.__const: 0x7d60
+  __AUTH_CONST.__cfstring: 0x10540
+  __AUTH_CONST.__objc_const: 0x22d70
   __AUTH_CONST.__objc_intobj: 0xa38
-  __AUTH_CONST.__objc_arrayobj: 0x2a0
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1828
-  __AUTH.__objc_data: 0xc0
-  __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x14c0
-  __DATA.__data: 0xd70
+  __AUTH_CONST.__auth_got: 0x1860
+  __AUTH.__objc_data: 0x130
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x14cc
+  __DATA.__data: 0xda0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x6890
-  __DATA_DIRTY.__data: 0x4ac0
+  __DATA_DIRTY.__data: 0x4ad0
   __DATA_DIRTY.__bss: 0x1d48
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11720
-  Symbols:   15387
-  CStrings:  5570
+  Functions: 11811
+  Symbols:   15440
+  CStrings:  5599
 
Symbols:
+ +[EDSearchableIndexPersistence searchableAccountsTableSchema]
+ -[EDLocalActionPersistence remoteIDsBeingMovedOutOfMailboxURL:amongRemoteIDs:]
+ -[EDLocalSearchInfoCollector _combinedQuerySafety]
+ -[EDLocalSearchInfoCollector liveSearchQuerySafety]
+ -[EDLocalSearchInfoCollector setLiveSearchQuerySafety:]
+ -[EDLocalSearchInfoCollector setTopHitsQuerySafety:]
+ -[EDLocalSearchInfoCollector topHitsQuerySafety]
+ -[EDMessageQueryHelper localSearchDidDetermineQuerySafety:]
+ -[EDMessageQueryHelper localSearchDidDetermineTopHitsQuerySafety:]
+ -[EDMessageRepository _performOneOffQuery:limit:completionHandler:]
+ -[EDMessageRepository oneOffQueryScheduler]
+ -[EDOutgoingMessageRepository invalidateLastDelayedMessageTimer:]
+ -[EDOutgoingMessageRepository outboxPresenceOfUnsentMessageWithMessageIDHeaderHash:completion:]
+ -[EDOutgoingMessageRepository restartLastDelayedMessageTimer:]
+ -[EDSearchableIndexPersistence fetchDonatedAccountItems]
+ -[EDSearchableIndexPersistence recordDonatedAccountItems:deletedIdentifiers:]
+ -[EDSearchableIndexPersistence removeAllDonatedAccountItems]
+ _EMQuerySafetyByCombining
+ _OBJC_CLASS_$_ECMessageBodyParsingUtils
+ _OBJC_CLASS_$_EDAddSearchableAccountsTableUpgradeStep
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._liveSearchQuerySafety
+ _OBJC_IVAR_$_EDLocalSearchInfoCollector._topHitsQuerySafety
+ _OBJC_IVAR_$_EDMessageRepository._oneOffQueryScheduler
+ _OBJC_METACLASS_$_EDAddSearchableAccountsTableUpgradeStep
+ __CLASS_METHODS_EDAddSearchableAccountsTableUpgradeStep
+ __DATA_EDAddSearchableAccountsTableUpgradeStep
+ __INSTANCE_METHODS_EDAddSearchableAccountsTableUpgradeStep
+ __METACLASS_DATA_EDAddSearchableAccountsTableUpgradeStep
+ __PROTOCOLS_EDAddSearchableAccountsTableUpgradeStep
+ ___36-[EDMessageRepository test_tearDown]_block_invoke_2
+ ___55-[EDMessageRepository logCategoryMetadataForObjectIDs:]_block_invoke
+ ___56-[EDSearchableIndexPersistence fetchDonatedAccountItems]_block_invoke
+ ___56-[EDSearchableIndexPersistence fetchDonatedAccountItems]_block_invoke_2
+ ___60-[EDSearchableIndexPersistence removeAllDonatedAccountItems]_block_invoke
+ ___67-[EDMessageRepository _performOneOffQuery:limit:completionHandler:]_block_invoke
+ ___77-[EDSearchableIndexPersistence recordDonatedAccountItems:deletedIdentifiers:]_block_invoke
+ ___78-[EDLocalActionPersistence remoteIDsBeingMovedOutOfMailboxURL:amongRemoteIDs:]_block_invoke
+ ___78-[EDLocalActionPersistence remoteIDsBeingMovedOutOfMailboxURL:amongRemoteIDs:]_block_invoke_2
+ ___98-[EDSearchableIndex searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:]_block_invoke_6
+ ___98-[EDSearchableIndex searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:]_block_invoke_7
+ ___block_descriptor_32_e41_B16?0"EDPersistenceDatabaseConnection"8l
+ ___block_descriptor_40_ea8_32w_e8_v16?0q8lw32l8
+ ___swift_closure_destructor.19Tm
+ ___swift_closure_destructor.38Tm
+ _swift_release_x3
+ _symbolic Ieg_
+ _symbolic SDyS2SG
+ _symbolic ShySSG
+ _symbolic So26EDSearchableIndexTelemetryC
+ _symbolic So39EDAddSearchableAccountsTableUpgradeStepC
+ _symbolic _____ So39EDAddSearchableAccountsTableUpgradeStepC11EmailDaemonE3run4withySo31EDPersistenceDatabaseConnectionC_tKFZ8SQLErrorL_V
+ _symbolic ______pSgIegg_ s5ErrorP
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
+ _symbolic ytSgIegd_
+ _symbolic ytSgyc
- ___swift_closure_destructor.25Tm
- ___swift_closure_destructor.44Tm
CStrings:
+ "-[EDLocalActionPersistence remoteIDsBeingMovedOutOfMailboxURL:amongRemoteIDs:]"
+ "-[EDOutgoingMessageRepository invalidateLastDelayedMessageTimer:]"
+ "-[EDOutgoingMessageRepository outboxPresenceOfUnsentMessageWithMessageIDHeaderHash:completion:]"
+ "-[EDOutgoingMessageRepository restartLastDelayedMessageTimer:]"
+ "-[EDSearchableIndexPersistence fetchDonatedAccountItems]"
+ "-[EDSearchableIndexPersistence recordDonatedAccountItems:deletedIdentifiers:]"
+ "-[EDSearchableIndexPersistence removeAllDonatedAccountItems]"
+ ":identifiers"
+ ":items"
+ ":remote_ids"
+ "Account items are up to date"
+ "B"
+ "CREATE TABLE IF NOT EXISTS searchable_accounts (ROWID INTEGER PRIMARY KEY,\nidentifier TEXT COLLATE BINARY NOT NULL,\ncontent_hash TEXT COLLATE BINARY NOT NULL,\nUNIQUE(identifier) ON CONFLICT ABORT);"
+ "Clearing searchable_accounts"
+ "DELETE FROM searchable_accounts"
+ "DELETE FROM searchable_accounts WHERE identifier IN (SELECT value FROM json_each(:identifiers))"
+ "Deleting from searchable_accounts"
+ "Donated %{public}ld account item(s): %s; deleted %{public}ld: %s"
+ "Failed to donate %{public}ld account item(s) of type(s) [%{public}s] [%s] or delete %{public}ld [%s]: %{public}s"
+ "Finding remote IDs being moved out of a mailbox"
+ "INSERT OR REPLACE INTO searchable_accounts (identifier, content_hash) SELECT key, value FROM json_each(:items)"
+ "No record of donated account items; deleting earlier builds' account items"
+ "Reading searchable_accounts"
+ "SELECT action_messages.remote_id AS remote_id FROM action_messages  JOIN local_message_actions ON action_messages.action = local_message_actions.ROWID WHERE local_message_actions.source_mailbox = :mailbox   AND local_message_actions.action_type IN (%ld, %ld)   AND CAST(action_messages.remote_id AS TEXT) IN (SELECT value FROM json_each(:remote_ids))"
+ "SELECT identifier, content_hash FROM searchable_accounts"
+ "Unable to add searchable_accounts table"
+ "Writing searchable_accounts"
+ "[]"
+ "com.apple.email.EDMessageRepository.oneOffQueryScheduler"
+ "content_hash"
+ "searchable_accounts"
+ "\xf0\xf0q"
- "Donated %{public}ld account item(s): %s"
- "Failed to donate %{public}ld account item(s) of type(s) [%{public}s] [%s]: %{public}s"
- "\xf0\xf0a"
```
