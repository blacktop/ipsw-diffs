## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3826.200.46.2.1
-  __TEXT.__text: 0xac5be8
-  __TEXT.__auth_stubs: 0x7df0
-  __TEXT.__objc_methlist: 0x11afc
-  __TEXT.__gcc_except_tab: 0x38420
+3826.200.67.0.0
+  __TEXT.__text: 0xac43d4
+  __TEXT.__auth_stubs: 0x7dd0
+  __TEXT.__objc_methlist: 0x119ac
+  __TEXT.__gcc_except_tab: 0x37f8c
   __TEXT.__const: 0x4a370
-  __TEXT.__cstring: 0x2fa0e
-  __TEXT.__oslogstring: 0x22fe0
+  __TEXT.__cstring: 0x2fafe
+  __TEXT.__oslogstring: 0x22f50
   __TEXT.__ustring: 0x22c0
   __TEXT.__swift5_typeref: 0x11571
   __TEXT.__swift5_capture: 0x2ee88

   __TEXT.__swift5_types: 0x1738
   __TEXT.__swift5_mpenum: 0xcc4
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__unwind_info: 0x23558
-  __TEXT.__eh_frame: 0x1e360
-  __TEXT.__objc_classname: 0x2a7c
-  __TEXT.__objc_methname: 0x2df8f
-  __TEXT.__objc_methtype: 0x676e
-  __TEXT.__objc_stubs: 0x242c0
-  __DATA_CONST.__got: 0x2be8
-  __DATA_CONST.__const: 0x15530
-  __DATA_CONST.__objc_classlist: 0xb28
+  __TEXT.__unwind_info: 0x234c8
+  __TEXT.__eh_frame: 0x1e3d8
+  __TEXT.__objc_classname: 0x2a37
+  __TEXT.__objc_methname: 0x2dc83
+  __TEXT.__objc_methtype: 0x6782
+  __TEXT.__objc_stubs: 0x24160
+  __DATA_CONST.__got: 0x2bc0
+  __DATA_CONST.__const: 0x15548
+  __DATA_CONST.__objc_classlist: 0xb20
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x550
+  __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb158
+  __DATA_CONST.__objc_selrefs: 0xb0d0
   __DATA_CONST.__objc_protorefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0x688
+  __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0xfb8
-  __AUTH_CONST.__auth_got: 0x3f10
-  __AUTH_CONST.__auth_ptr: 0x2eb8
+  __AUTH_CONST.__auth_got: 0x3f00
+  __AUTH_CONST.__auth_ptr: 0x2ee8
   __AUTH_CONST.__const: 0xa2d40
-  __AUTH_CONST.__cfstring: 0x18420
-  __AUTH_CONST.__objc_const: 0x26d20
+  __AUTH_CONST.__cfstring: 0x18360
+  __AUTH_CONST.__objc_const: 0x26a58
   __AUTH_CONST.__objc_arrayobj: 0xba0
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x5178
+  __AUTH.__objc_data: 0x5128
   __AUTH.__data: 0x7df8
-  __DATA.__objc_ivar: 0x13bc
-  __DATA.__data: 0xdda0
+  __DATA.__objc_ivar: 0x1398
+  __DATA.__data: 0xdd10
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4df28
+  __DATA.__bss: 0x4df18
   __DATA.__common: 0xec8
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x18

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 54019
-  Symbols:   14021
-  CStrings:  17139
+  Functions: 54002
+  Symbols:   13990
+  CStrings:  17101
 
Symbols:
+ _EMPersistenceStatisticsKeyMessageBodiesIndexed
- _MFAccountsWithErrorsKey
- OBJC_IVAR_$_MFSMTPConnection._saveSentMbox
- OBJC_IVAR_$_MFSMTPConnection._dislikesSaveSentMbox
- OBJC_IVAR_$_MFPlainTextDocument._fragments
- _MFMessageCriterionCompareRelativeToOtherPrefix
- OBJC_IVAR_$_MFIMAPCommandPipeline._fetchUnits
- OBJC_IVAR_$_MFSMTPConnection._useSaveSent
CStrings:
+ "%!@(MISSING) Fetching headers for UID %!{(MISSING)public}@"
+ "searchResultsWithRemoteIDs:requiresBody:inMailbox:"
+ "NSArray<id> *fetchArgumentsForCriterion(MFMessageCriterion *__strong, BOOL)"
+ "prepareToPersistCategorizationResultMap:"
+ "%!@(MISSING) FROM messages %!@(MISSING) %!s(MISSING) WHERE remote_mailbox = (SELECT ROWID FROM mailboxes WHERE url = %!@(MISSING)) AND messages.remote_id IN (%!@(MISSING)) AND (messages.searchable_message IS NULL %!@(MISSING))"
+ "@36@0:8@16B24@28"
+ " OR NOT searchable_messages.message_body_indexed"
+ " WITH index_status AS (   SELECT server_messages.remote_id,     (NOT (       messages.searchable_message IS NULL%!@(MISSING)     )) as done_indexing   FROM messages        INNER JOIN server_messages ON messages.ROWID = server_messages.message        %!@(MISSING)   WHERE messages.mailbox == :mailbox     AND server_messages.remote_id >= :min_uid     AND server_messages.remote_id <= :max_uid ), marked AS (   SELECT *,          (done_indexing AND           (done_indexing != LAG(done_indexing) OVER (ORDER BY remote_id DESC) OR            LAG(done_indexing) OVER (ORDER BY remote_id DESC) IS NULL)) as is_start,          (done_indexing AND           (done_indexing != LEAD(done_indexing) OVER (ORDER BY remote_id DESC) OR            LEAD(done_indexing) OVER (ORDER BY remote_id DESC) IS NULL)) as is_end   FROM index_status ), ranges AS (   SELECT *,          SUM(is_start) OVER (ORDER BY remote_id DESC) as group_id   FROM marked ) SELECT MIN(remote_id), MAX(remote_id), count(), done_indexing   FROM ranges   GROUP BY group_id   ORDER BY MIN(remote_id) DESC   LIMIT :limit;"
+ "\x02\x11\x13\x12\x129"
+ "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL then 1 ELSE 0 END) as indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed then 1 ELSE 0 END) as message_bodies_indexed  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %!@(MISSING)"
+ "@52@0:8{_NSRange=QQ}16B32@36q44"
+ "-[MFMailMessageLibrary searchResultsWithRemoteIDs:requiresBody:inRemoteMailbox:]"
+ "searchResultsWithRemoteIDs:requiresBody:inRemoteMailbox:"
+ "LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID"
+ "prepareToChangeCategoryType:messages:"
+ "requiresBody"
+ "rangesOfIndexedUIDsInRange:requiresBody:forMailbox:limit:"
+ "-[MFMailMessageLibrary rangesOfIndexedUIDsInRange:requiresBody:forMailbox:limit:]"
+ "@16@?0@\"<EDPersistedMessage>\"8"
- "messageSet"
- "@16@?0@\"<ECMessage>\"8"
- "Finished database query for indexable messages"
- "NSArray *fetchArgumentsForCriterion(MFMessageCriterion *__strong, BOOL)"
- "recordPasteboardAttachmentsForURLs:forContextID:"
- "SELECT COUNT(*) FROM messages WHERE messages.searchable_message IS NOT NULL AND deleted = '0' %!@(MISSING)"
- "searchResultsWithRemoteIDs:inMailbox:"
- "%!@(MISSING) %!@(MISSING) (%!@(MISSING) + %!l(MISSING)f)"
- " WITH index_status AS (   SELECT server_messages.remote_id,     (NOT (       messages.searchable_message IS NULL     )) as done_indexing   FROM messages INNER JOIN server_messages ON messages.ROWID = server_messages.message   WHERE messages.mailbox == :mailbox     AND server_messages.remote_id >= :min_uid     AND server_messages.remote_id <= :max_uid ), marked AS (   SELECT *,          (done_indexing AND           (done_indexing != LAG(done_indexing) OVER (ORDER BY remote_id DESC) OR            LAG(done_indexing) OVER (ORDER BY remote_id DESC) IS NULL)) as is_start,          (done_indexing AND           (done_indexing != LEAD(done_indexing) OVER (ORDER BY remote_id DESC) OR            LEAD(done_indexing) OVER (ORDER BY remote_id DESC) IS NULL)) as is_end   FROM index_status ), ranges AS (   SELECT *,          SUM(is_start) OVER (ORDER BY remote_id DESC) as group_id   FROM marked ) SELECT MIN(remote_id), MAX(remote_id), count(), done_indexing   FROM ranges   GROUP BY group_id   ORDER BY MIN(remote_id) DESC   LIMIT :limit;"
- "setUseSaveSent:toFolder:"
- "recordUndoDataForAttachments:"
- "copyDataForRemoteEncryptionCertificatesForAddress:error:"
- "searchResultsWithRemoteIDs:inRemoteMailbox:"
- "createMessageWithHtmlString:plainTextAlternative:otherHtmlStringsAndAttachments:headers:"
- "\x02\x11\x13\x12\x12:"
- "Swift/FloatingPointTypes.swift"
- "%!@(MISSING) FROM messages %!s(MISSING) WHERE remote_mailbox = (SELECT ROWID FROM mailboxes WHERE url = %!@(MISSING)) AND messages.remote_id IN (%!@(MISSING)) AND messages.searchable_message IS NULL"
- "_isAppleServiceDeliveryHostname:"
- "Starting database query for indexable messages"
- "_handler"
- "_useSaveSent"
- "_dislikesSaveSentMbox"
- "-[MFMailMessageLibrary searchResultsWithRemoteIDs:inRemoteMailbox:]"
- "MFAccountsWithErrorsKey"
- "_ispAccountInfo"
- "T@\"NSArray\",R,C,N,V_serverCertificates"
- "registerAppleServiceDeliveryHostname:"
- "@48@0:8{_NSRange=QQ}16@32q40"
- "englishHeadersFromLocalizedHeaders:"
- "_attachmentsUndoData"
- "recordPasteboardDataForAttachments:"
- "_serverCertificates"
- "_MFFlushableMessageSetIterator"
- "criterionFromDefaultsDictionary:"
- " imapmailbox=\"%!@(MISSING)\""
- "SELECT COUNT(*) FROM messages WHERE deleted = '0' %!@(MISSING)"
- "shouldUseSaveSentForAccount:"
- "persistCategorizationResultMap:"
- "SELECT COUNT(*) FROM messages WHERE messages.searchable_message IS NULL AND deleted = '0' %!@(MISSING)"
- "Starting database query for messages indexed"
- "_messageSet"
- "rangesOfIndexedUIDsInRange:forMailbox:limit:"
- "_attachmentsPasteboardData"
- "_MFPersistedMessageForwardingIterator"
- "recordUndoAttachmentsForURLs:forContextID:"
- "createMessageWithHtmlString:attachments:headers:"
- "Magic comparision must be $magicString,$field,$offset"
- "newDefaultInstance"
- "Only =, <, > are supported for date comparision"
- "--compare-field"
- "serverCertificates"
- "Finished database query for messages indexed"
- "isVIPCriterion"
- "localizedHeadersFromEnglishHeaders:"
- "-[MFMailMessageLibrary rangesOfIndexedUIDsInRange:forMailbox:limit:]"
- "T@\"NSMutableIndexSet\",R,N,V_messageSet"
- "_saveSentMbox"

```
