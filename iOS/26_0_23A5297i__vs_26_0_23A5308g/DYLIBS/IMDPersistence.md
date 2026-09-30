## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1445.100.6.2.4
-  __TEXT.__text: 0x220214
-  __TEXT.__auth_stubs: 0x44c0
-  __TEXT.__objc_methlist: 0x6fd4
-  __TEXT.__const: 0xa1d8
-  __TEXT.__cstring: 0x479fb
-  __TEXT.__oslogstring: 0x1d5d6
-  __TEXT.__gcc_except_tab: 0xf7f4
+1447.100.7.2.3
+  __TEXT.__text: 0x221030
+  __TEXT.__auth_stubs: 0x44d0
+  __TEXT.__objc_methlist: 0x702c
+  __TEXT.__const: 0xa1c8
+  __TEXT.__cstring: 0x477ab
+  __TEXT.__oslogstring: 0x1d686
+  __TEXT.__gcc_except_tab: 0xf818
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4ccc

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8c10
-  __TEXT.__eh_frame: 0x6d78
+  __TEXT.__unwind_info: 0x8c48
+  __TEXT.__eh_frame: 0x6db0
   __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x17342
-  __TEXT.__objc_methtype: 0x35f2
-  __TEXT.__objc_stubs: 0x11880
-  __DATA_CONST.__got: 0x16e8
-  __DATA_CONST.__const: 0x8298
+  __TEXT.__objc_methname: 0x17528
+  __TEXT.__objc_methtype: 0x369d
+  __TEXT.__objc_stubs: 0x11920
+  __DATA_CONST.__got: 0x16f0
+  __DATA_CONST.__const: 0x8300
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5158
+  __DATA_CONST.__objc_selrefs: 0x5188
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x2270
-  __AUTH_CONST.__const: 0x94d0
-  __AUTH_CONST.__cfstring: 0x11d20
-  __AUTH_CONST.__objc_const: 0xf258
+  __AUTH_CONST.__auth_got: 0x2278
+  __AUTH_CONST.__const: 0x95f0
+  __AUTH_CONST.__cfstring: 0x11e20
+  __AUTH_CONST.__objc_const: 0xf278
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1ac0
-  __AUTH.__data: 0x4078
+  __AUTH.__objc_data: 0x1b10
+  __AUTH.__data: 0x4088
   __DATA.__objc_ivar: 0x47c
-  __DATA.__data: 0x2c10
-  __DATA.__bss: 0xa5c0
-  __DATA.__common: 0x190
-  __DATA_DIRTY.__objc_data: 0x1670
-  __DATA_DIRTY.__data: 0x3cd0
-  __DATA_DIRTY.__bss: 0x18f0
-  __DATA_DIRTY.__common: 0x28
+  __DATA.__data: 0x2bc0
+  __DATA.__bss: 0xa2d0
+  __DATA.__common: 0x178
+  __DATA_DIRTY.__objc_data: 0x1620
+  __DATA_DIRTY.__data: 0x3d30
+  __DATA_DIRTY.__bss: 0x1be8
+  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F20FB337-3705-3038-AE5B-F3CEC724E98C
-  Functions: 10419
-  Symbols:   2553
-  CStrings:  12164
+  UUID: B0C41051-7F57-320D-95EF-1024D8BA6DDA
+  Functions: 10436
+  Symbols:   2554
+  CStrings:  12199
 
Symbols:
+ _IMMessagePropertyIsSOS
+ _IMMessagePropertyReplaceID
+ _IMSharedHelperReadMessagePriorityTimeout
+ ___IMDPersistenceCheckAnyEntitlementsForInitialConnection
- _IMDMessageRecordCopySortedMessagesFilteredUsingPredicateWithLimitQuery
- _IMDMessageRecordCopySortedMessagesForChatGUIDFilteredUsingPredicateWithLimitQuery
- _NSKeyValueChangeNewKey
CStrings:
+ "\n                    ELSE "
+ "\n                END\n            )\n            ELSE NULL\n        END AS time_sensitive_expiration\n    FROM message\n    INNER JOIN chat_message_join ON chat_message_join.message_id = message.rowid\n    WHERE\n        NOT (message.ROWID in (SELECT message_id FROM chat_recoverable_message_join)) AND\n        (\n            message.is_read == 0 AND\n            message.is_finished == 1 AND\n            message.is_from_me == 0 AND\n            message.item_type == 0 AND\n            message.is_system_message == 0\n        )\n),\n--- Gets all interesting messages\ninteresting_messages AS (\n    SELECT * FROM unread_messages\n    UNION\n    SELECT * FROM time_sensitive_messages\n),\n-- Get an unread count per-chat, where unreads are present\nchat_unreads AS (\n    SELECT\n        interesting_messages.chat_id,\n        MIN(CASE WHEN interesting_messages.is_time_sensitive AND interesting_messages.time_sensitive_expiration > "
+ "\n                END\n            )\n            ELSE NULL\n        END AS time_sensitive_expiration\n    FROM message\n    INNER JOIN chat_message_join ON chat_message_join.message_id = message.rowid\n    WHERE\n        NOT (message.ROWID in (SELECT message_id FROM chat_recoverable_message_join)) AND\n        is_time_sensitive == 1 AND\n        time_sensitive_expiration > "
+ "\n),\n--- Gets all unread messages along with some message state\nunread_messages AS (\n    SELECT\n        chat_message_join.message_id,\n        chat_message_join.chat_id,\n        message.is_read,\n        message.is_time_sensitive,\n        CASE WHEN message.is_time_sensitive\n            THEN CAST(message.date AS float) / 1e9 + 978307200 + (\n                CASE WHEN message.is_read\n                    THEN "
+ " THEN 0\n    ELSE ck_sync_state\nEND\nWHERE guid IN "
+ "%@ JOIN chat_message_join ON chat_message_join.message_id = message.rowid %@ JOIN chat ON chat.rowid = chat_message_join.chat_id  "
+ "%K == %@"
+ "%K == %ld"
+ ",\nck_sync_state = CASE\n    WHEN is_pending_review != "
+ "-- Get a concatenated list of chat participants delimited by commas\nWITH chat_participants AS (\n    SELECT\n        chat_handle_join.chat_id,\n        group_concat(handle.id) AS participants\n    FROM handle\n    INNER JOIN chat_handle_join ON chat_handle_join.handle_id = handle.rowid\n    GROUP BY chat_handle_join.chat_id\n),\n--- Gets all time sensitive messages along with some message state\ntime_sensitive_messages AS (\n    SELECT\n        chat_message_join.message_id,\n        chat_message_join.chat_id,\n        message.is_read,\n        message.is_time_sensitive,\n        CASE WHEN message.is_time_sensitive\n            THEN CAST(message.date AS float) / 1e9 + 978307200 + (\n                CASE WHEN message.is_read\n                    THEN "
+ "-[IMDDatabase(LegacyMessages) _fetchMessageRecordsFilteredUsingPredicate:sortedUsingDescriptors:inChatsFilteredUsingPredicate:fromHandlesUsingPredicate:parentedOnly:limit:completionHandler:]"
+ "@\"OS_dispatch_queue\""
+ "@52@0:8@16@24@32@40B48"
+ "Bad chat predicate provided to %s (%@)"
+ "Bad handle predicate provided to %s (%@)"
+ "Bad message predicate provided to %s (%@)"
+ "Connection from %d has no IMDP entitlements, denying connection"
+ "IMCSLastIndexDeleteReason"
+ "IMDPersistenceServiceResettingNotification"
+ "INNER"
+ "INNER JOIN chat_message_join ON chat_message_join.message_id = message.rowid "
+ "INNER JOIN handle ON handle.rowid = message.handle_id "
+ "SELECT %@ FROM message %@ %@ %@ LIMIT ?;"
+ "SELECT COUNT(1) FROM message;"
+ "SELECT m.guid, m.rowid FROM message m\nINNER JOIN chat c\n    ON c.rowid = (\n        SELECT CASE\n            WHEN instr(m.ck_chat_id, ';') > 0\n            THEN (\n                /* ck_chat_id matches to a guid (for 1:1 chats) */\n                SELECT chat.rowid\n                FROM chat\n                WHERE chat.chat_identifier = SUBSTR(m.ck_chat_id, INSTR(SUBSTR(m.ck_chat_id, INSTR(m.ck_chat_id, ';') + 1), ';') + INSTR(m.ck_chat_id, ';') + 1)\n            )\n            ELSE (\n                /* ck_chat_id matches to an identifier in the appropriate service based domain (for group chats) */\n                SELECT cl.chat\n                FROM chat_lookup cl\n                WHERE cl.identifier = m.ck_chat_id\n                AND cl.domain = domain_for_service(m.service)\n            )\n        END\n    )\nWHERE m.rowid >=  ?  AND m.rowid <  ? \n/* Do not match any chats that are already associated with a chat */\nAND NOT EXISTS (\n    SELECT 1\n    FROM chat_message_join cmj\n    WHERE cmj.message_id = m.rowid\n    UNION\n    SELECT 1\n    FROM chat_recoverable_message_join crmj\n    WHERE crmj.message_id = m.rowid\n)\nORDER BY m.rowid ASC\nLIMIT  ? ;"
+ "T@\"NSNumber\",&,N,S_setLastIndexDeleteReason:"
+ "UPDATE chat\nSET is_pending_review = "
+ "UPDATE message\nSET is_time_sensitive = 0\nWHERE is_time_sensitive == 1 AND message.date < (\n    CASE WHEN message.is_read\n        THEN  ? \n        ELSE  ? \n    END\n)"
+ "_deleteAllSearchableItemsWithReason:completionHandler:"
+ "_fetchMessageRecordsFilteredUsingPredicate:sortedUsingDescriptors:inChatsFilteredUsingPredicate:fromHandlesUsingPredicate:parentedOnly:limit:completionHandler:"
+ "_lastIndexDeleteReason"
+ "_queryForMessageRecordFetchWithMessageWhereClause:chatWhereClause:handleWhereClause:orderByClauses:parentedOnly:"
+ "_setLastIndexDeleteReason:"
+ "fetchLastSpotlightIndexDeleteReasonWithCompletion:"
+ "fetchMessageRecordsFilteredUsingPredicate:sortedUsingDescriptors:inChatsFilteredUsingPredicate:fromHandlesUsingPredicate:limit:completionHandler:"
+ "handle(id, rowid)"
+ "handle."
+ "handle_idx_id"
+ "png"
+ "v24@0:8@?<v@?@\"NSNumber\">16"
+ "v64@0:8@\"NSPredicate\"16@\"NSArray\"24@\"NSPredicate\"32@\"NSPredicate\"40Q48@?<v@?@\"NSArray\">56"
+ "v64@0:8@16@24@32@40Q48@?56"
+ "v68@0:8@16@24@32@40B48Q52@?60"
- "\n),\n--- Gets all unread messages along with some message state\nunread_messages AS (\n    SELECT\n        chat_message_join.message_id,\n        chat_message_join.chat_id,\n        message.is_read,\n        message.is_time_sensitive,\n        CASE WHEN message.is_time_sensitive THEN CAST(message.date AS float) / 1e9 + 978307200 + "
- " ELSE NULL END AS time_sensitive_expiration\n    FROM message\n    INNER JOIN chat_message_join ON chat_message_join.message_id = message.rowid\n    WHERE\n        NOT (message.ROWID in (SELECT message_id FROM chat_recoverable_message_join)) AND\n        (\n            message.is_read == 0 AND\n            message.is_finished == 1 AND\n            message.is_from_me == 0 AND\n            message.item_type == 0 AND\n            message.is_system_message == 0\n        )\n),\n--- Gets all interesting messages\ninteresting_messages AS (\n    SELECT * FROM unread_messages\n    UNION\n    SELECT * FROM time_sensitive_messages\n),\n-- Get an unread count per-chat, where unreads are present\nchat_unreads AS (\n    SELECT\n        interesting_messages.chat_id,\n        MIN(CASE WHEN interesting_messages.is_time_sensitive AND interesting_messages.time_sensitive_expiration > "
- " ELSE NULL END AS time_sensitive_expiration\n    FROM message\n    INNER JOIN chat_message_join ON chat_message_join.message_id = message.rowid\n    WHERE\n        NOT (message.ROWID in (SELECT message_id FROM chat_recoverable_message_join)) AND\n        is_time_sensitive == 1 AND\n        time_sensitive_expiration > "
- ", ck_sync_state = 1 WHERE guid IN "
- "-- Get a concatenated list of chat participants delimited by commas\nWITH chat_participants AS (\n    SELECT\n        chat_handle_join.chat_id,\n        group_concat(handle.id) AS participants\n    FROM handle\n    INNER JOIN chat_handle_join ON chat_handle_join.handle_id = handle.rowid\n    GROUP BY chat_handle_join.chat_id\n),\n--- Gets all time sensitive messages along with some message state\ntime_sensitive_messages AS (\n    SELECT\n        chat_message_join.message_id,\n        chat_message_join.chat_id,\n        message.is_read,\n        message.is_time_sensitive,\n        CASE WHEN message.is_time_sensitive THEN CAST(message.date AS float) / 1e9 + 978307200 + "
- "-[IMDDatabase(LegacyMessages) _fetchMessageRecordsFilteredUsingPredicate:sortedUsingDescriptors:inChatsFilteredUsingPredicate:parentedOnly:limit:completionHandler:]"
- "1"
- "INNER JOIN chat_message_join cmj ON cmj.message_id = message.rowid"
- "SELECT %@ FROM message JOIN chat_message_join ON chat_message_join.message_id == message.rowid JOIN chat ON chat.rowid = chat_message_join.chat_id AND %@ %@ %@ LIMIT ?;"
- "SELECT ROWID, guid, text, replace, service_center, handle_id, subject, country, attributedBody, version, type, service, account, account_guid, error, date, date_read, date_delivered, is_delivered, is_finished, is_emote, is_from_me, is_empty, is_delayed, is_auto_reply, is_prepared, is_read, is_system_message, is_sent, has_dd_results, is_service_message, is_forward, was_downgraded, is_archive, cache_has_attachments, cache_roomnames, was_data_detected, was_deduplicated, is_audio_message, is_played, date_played, item_type, other_handle, group_title, group_action_type, share_status, share_direction, is_expirable, expire_state, message_action_type, message_source, associated_message_guid, associated_message_type, balloon_bundle_id, payload_data, expressive_send_style_id, associated_message_range_location, associated_message_range_length, time_expressive_send_played, message_summary_info, ck_sync_state, ck_record_id, ck_record_change_tag, destination_caller_id, is_corrupt, reply_to_guid, sort_id, is_spam, has_unseen_mention, thread_originator_guid, thread_originator_part, syndication_ranges, synced_syndication_ranges, was_delivered_quietly, did_notify_recipient, date_retracted, date_edited, date_recovered, was_detonated, part_count, is_stewie, is_sos, is_critical, bia_reference_id, is_kt_verified, fallback_hash, associated_message_emoji, is_pending_satellite_send, needs_relay, schedule_type, schedule_state, sent_or_received_off_grid, is_time_sensitive, ck_chat_id FROM message %@ WHERE %@ %@ LIMIT    ?;"
- "SELECT m.guid, m.rowid FROM message m\nINNER JOIN chat c\n    /* ck_chat_id matches to an identifier in the appropriate service based domain (for group chats) */\n    ON c.rowid = (\n        SELECT cl.chat FROM chat_lookup cl\n        WHERE cl.identifier = m.ck_chat_id\n        AND cl.domain = domain_for_service(m.service)\n    )\n    /* ck_chat_id matches to a guid (for 1:1 chats) */\n    OR c.guid LIKE '%' || (\n        SELECT CASE\n            WHEN instr(m.ck_chat_id, ';') > 0\n            THEN substr(m.ck_chat_id, instr(m.ck_chat_id, ';') + 1)\n            ELSE NULL\n        END\n    )\nWHERE m.rowid >  ? \n/* Do not match any chats that are already associated with a chat */\nAND NOT EXISTS (\n    SELECT 1\n    FROM chat_message_join cmj\n    WHERE cmj.message_id = m.rowid\n)\nAND NOT EXISTS (\n    SELECT 1\n    FROM chat_recoverable_message_join crmj\n    WHERE crmj.message_id = m.rowid\n)\nLIMIT  ? ;"
- "Simulated indexing error"
- "UPDATE chat SET is_pending_review = "
- "UPDATE message\nSET is_time_sensitive = 0\nWHERE is_time_sensitive == 1 AND message.date <  ? "
- "_fetchMessageRecordsFilteredUsingPredicate:sortedUsingDescriptors:inChatsFilteredUsingPredicate:parentedOnly:limit:completionHandler:"
- "jpg"
- "v60@0:8@16@24@32B40Q44@?52"

```
