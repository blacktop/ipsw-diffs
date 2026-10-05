## EmailDaemon

> `/System/Library/PrivateFrameworks/EmailDaemon.framework/EmailDaemon`

```diff

-3901.200.41.0.0
-  __TEXT.__text: 0x28c55c
-  __TEXT.__objc_methlist: 0x13634
-  __TEXT.__const: 0x53cc
-  __TEXT.__gcc_except_tab: 0x4aed4
-  __TEXT.__cstring: 0x2976a
-  __TEXT.__oslogstring: 0x1b614
+3901.200.66.2.1
+  __TEXT.__text: 0x28e0d8
+  __TEXT.__objc_methlist: 0x136b4
+  __TEXT.__const: 0x53fc
+  __TEXT.__gcc_except_tab: 0x4afc0
+  __TEXT.__cstring: 0x2989a
+  __TEXT.__oslogstring: 0x1b684
   __TEXT.__dlopen_cstrs: 0x415
   __TEXT.__ustring: 0x26
-  __TEXT.__swift5_typeref: 0x1856
+  __TEXT.__swift5_typeref: 0x18a2
   __TEXT.__constg_swiftt: 0x1128
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_reflstr: 0x114f

   __TEXT.__swift5_assocty: 0x260
   __TEXT.__swift5_proto: 0x3a8
   __TEXT.__swift5_types: 0x1e0
-  __TEXT.__swift5_capture: 0x880
+  __TEXT.__swift5_capture: 0x89c
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x48
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x127e8
+  __TEXT.__unwind_info: 0x12878
   __TEXT.__eh_frame: 0x16f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x95d0
   __DATA_CONST.__objc_classlist: 0x9f8
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x430
+  __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb380
-  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_selrefs: 0xb3a8
+  __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x6d8
   __DATA_CONST.__got: 0x1ed0
-  __AUTH_CONST.__const: 0x7c03
-  __AUTH_CONST.__cfstring: 0xff60
-  __AUTH_CONST.__objc_const: 0x228d0
+  __AUTH_CONST.__const: 0x7c58
+  __AUTH_CONST.__cfstring: 0xffa0
+  __AUTH_CONST.__objc_const: 0x229a0
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x1820
-  __AUTH.__objc_data: 0xcd8
-  __AUTH.__data: 0x390
-  __DATA.__objc_ivar: 0x1490
-  __DATA.__data: 0x3a10
+  __AUTH_CONST.__auth_got: 0x1828
+  __DATA.__objc_ivar: 0x149c
+  __DATA.__data: 0xcf0
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5c28
-  __DATA_DIRTY.__data: 0x1aa0
-  __DATA_DIRTY.__bss: 0x1b98
+  __DATA_DIRTY.__objc_data: 0x6900
+  __DATA_DIRTY.__data: 0x4bc0
+  __DATA_DIRTY.__bss: 0x1d38
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11686
-  Symbols:   15306
-  CStrings:  5539
+  Functions: 11707
+  Symbols:   15331
+  CStrings:  5546
 
Symbols:
+ +[EDFoundationModelContextGenerator originalContentMessageForMessage:limitOfInReplyToAncestors:condenseEmptyLines:messagePersistence:htmlStringFromMessage:error:]
+ -[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:options:completionPromise:]
+ -[EDDiagnosticInfoGatherer _shouldCollectIndexingDiagnostics:]
+ -[EDMessageChangeManager hasCompletedInitialSyncForMailboxURL:]
+ -[EDPersistenceDatabaseConnection rowIDPropertyForKey:]
+ -[EDPersistenceDatabaseConnection selectLowestUnresolvedAttachmentID]
+ -[EDPersistenceDatabaseConnection setLowestUnresolvedAttachmentID:]
+ -[EDPersistenceDatabaseConnection setRowIDProperty:forKey:]
+ -[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]
+ -[EDSearchableIndexPersistence _noteLowestUnresolvedAttachmentID:]
+ -[EDSearchableIndexPersistence _rewindAttachmentScanToRetryUnresolvedAttachments]
+ -[EDSearchableIndexPersistence lowestUnresolvedAttachmentID]
+ -[EDSearchableIndexPersistence setLowestUnresolvedAttachmentID:]
+ _OBJC_IVAR_$_EDSearchableIndexPersistence._lastAttachmentScanRewindDate
+ _OBJC_IVAR_$_EDSearchableIndexPersistence._lowestUnresolvedAttachmentID
+ _OBJC_IVAR_$_EDSearchableIndexPersistence._lowestUnresolvedAttachmentIDLock
+ __OBJC_$_INSTANCE_METHODS_EDMessageChangeManager(Swift)
+ __OBJC_$_PROP_LIST_EDServerSyncedMessage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EDServerSyncedMessage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EDServerSyncedMessage
+ __OBJC_$_PROTOCOL_REFS_EDServerSyncedMessage
+ __OBJC_LABEL_PROTOCOL_$_EDServerSyncedMessage
+ __OBJC_PROTOCOL_$_EDServerSyncedMessage
+ ___103-[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:options:completionPromise:]_block_invoke
+ ___143-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]_block_invoke
+ ___143-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]_block_invoke_2
+ ___143-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]_block_invoke_3
+ ___143-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]_block_invoke_4
+ ___162+[EDFoundationModelContextGenerator originalContentMessageForMessage:limitOfInReplyToAncestors:condenseEmptyLines:messagePersistence:htmlStringFromMessage:error:]_block_invoke
+ ___60-[EDSearchableIndexPersistence lowestUnresolvedAttachmentID]_block_invoke
+ ___64-[EDSearchableIndexPersistence setLowestUnresolvedAttachmentID:]_block_invoke
+ ___85-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) rowIDPropertyForKey:]_block_invoke
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e53_v20?0"EDSearchableIndexAttachmentItemMetadatum"8B16ls32l8s40l8s48l8r64l8s56l8
+ _flat unique So21EDServerSyncedMessage_p
+ _swift_dynamicCastObjCProtocolConditional
+ _symbolic Say______pG So21EDServerSyncedMessageP
+ _symbolic So22EDMessageChangeManagerC
+ _symbolic ______p So21EDServerSyncedMessageP
- +[EDFoundationModelContextGenerator originalContentMessageForMessage:limitOfInReplyToAncestors:checkForForwardedMessages:condenseEmptyLines:messagePersistence:htmlStringFromMessage:error:]
- -[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:]
- -[EDDiagnosticInfoGatherer _shouldCollectIndexingDiagnostics]
- -[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]
- __OBJC_$_INSTANCE_METHODS_EDMessageChangeManager
- ___188+[EDFoundationModelContextGenerator originalContentMessageForMessage:limitOfInReplyToAncestors:checkForForwardedMessages:condenseEmptyLines:messagePersistence:htmlStringFromMessage:error:]_block_invoke
- ___90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke
- ___90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke_2
- ___90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke_3
- ___90-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]_block_invoke_4
- ___95-[EDDiagnosticInfoGatherer _copyIndexingDiagnosticsDatabaseIntoDirectoryURL:completionPromise:]_block_invoke
- ___96-[EDPersistenceDatabaseConnection(EDSearchableIndexPersistence) selectLastProcessedAttachmentID]_block_invoke
- ___block_descriptor_64_ea8_32s40s48s56s_e53_v20?0"EDSearchableIndexAttachmentItemMetadatum"8B16ls32l8s40l8s48l8s56l8
CStrings:
+ "-[EDMessageChangeManager hasCompletedInitialSyncForMailboxURL:]"
+ "-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:lastVisitedAttachmentID:lowestUnresolvedAttachmentID:cancelationToken:]"
+ "-[EDSearchableIndexPersistence lowestUnresolvedAttachmentID]"
+ "-[EDSearchableIndexPersistence setLowestUnresolvedAttachmentID:]"
+ "DELETE FROM properties WHERE key = :key"
+ "Reached the end of the attachment table, rewinding indexing cursor to %lld to retry attachments whose data was missing"
+ "SELECT ma.ROWID, m.ROWID, ma.mime_part_number, ma.name, m.mailbox FROM messages AS m LEFT OUTER JOIN message_attachments AS ma ON (ma.global_message_id = m.global_message_id) LEFT OUTER JOIN searchable_attachments AS s ON (ma.ROWID = s.attachment_id) WHERE ma.ROWID > %lld AND s.attachment_id IS NULL AND ma.attachment IS NOT NULL ORDER BY ma.ROWID"
+ "Selecting %@ property"
+ "Setting %@ property"
+ "com.apple.mail.IMAP.newMessageLatency"
+ "com.apple.mail.searchableIndex.lowestUnresolvedAttachmentIDKey"
+ "\xb1"
- "-[EDSearchableIndexPersistence _attachmentItemsFromAttachmentData:limit:cancelationToken:]"
- "Replying to forwarded message, failed to generate any original-content messages"
- "SELECT ma.ROWID, m.ROWID, ma.mime_part_number, ma.name, m.mailbox FROM messages AS m LEFT OUTER JOIN message_attachments AS ma ON (ma.global_message_id = m.global_message_id) LEFT OUTER JOIN searchable_attachments AS s ON (ma.ROWID = s.attachment_id) WHERE ma.ROWID > %lld AND s.attachment_id IS NULL AND ma.attachment IS NOT NULL ORDER BY m.ROWID"
- "Setting latest value for lastProcessAttachmentID"
- "\x81"
```
