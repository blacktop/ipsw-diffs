## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.600.53.2.3
-  __TEXT.__text: 0x2642a0
-  __TEXT.__auth_stubs: 0x4ec0
-  __TEXT.__objc_methlist: 0x7f74
+1450.600.61.2.7
+  __TEXT.__text: 0x265454
+  __TEXT.__auth_stubs: 0x4f20
+  __TEXT.__objc_methlist: 0x7ff4
   __TEXT.__const: 0xc888
-  __TEXT.__cstring: 0x48b64
-  __TEXT.__oslogstring: 0x1e816
-  __TEXT.__gcc_except_tab: 0xb678
+  __TEXT.__cstring: 0x48e94
+  __TEXT.__oslogstring: 0x1e9b6
+  __TEXT.__gcc_except_tab: 0xb6c0
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
   __TEXT.__swift5_typeref: 0x3fb8

   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x95a8
+  __TEXT.__unwind_info: 0x95c0
   __TEXT.__eh_frame: 0x8b88
   __TEXT.__objc_classname: 0x28fa
-  __TEXT.__objc_methname: 0x1bb54
-  __TEXT.__objc_methtype: 0x4627
-  __TEXT.__objc_stubs: 0x13c60
-  __DATA_CONST.__got: 0x18e8
-  __DATA_CONST.__const: 0x8228
+  __TEXT.__objc_methname: 0x1bcf5
+  __TEXT.__objc_methtype: 0x4667
+  __TEXT.__objc_stubs: 0x13e40
+  __DATA_CONST.__got: 0x1908
+  __DATA_CONST.__const: 0x8230
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5820
+  __DATA_CONST.__objc_selrefs: 0x5898
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__auth_got: 0x2770
+  __AUTH_CONST.__auth_got: 0x27a0
   __AUTH_CONST.__const: 0xadd8
-  __AUTH_CONST.__cfstring: 0x12480
-  __AUTH_CONST.__objc_const: 0x11998
+  __AUTH_CONST.__cfstring: 0x124c0
+  __AUTH_CONST.__objc_const: 0x119b8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x22b0
   __AUTH.__data: 0x4c20
-  __DATA.__objc_ivar: 0x4cc
+  __DATA.__objc_ivar: 0x4d0
   __DATA.__data: 0x34c0
   __DATA.__bss: 0xae78
   __DATA.__common: 0x210

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88B37552-A572-31EF-AD09-C71E648A4E90
-  Functions: 11737
-  Symbols:   2648
-  CStrings:  12854
+  UUID: 06FDAF3C-39D7-36A1-91E6-2C8E05134074
+  Functions: 11753
+  Symbols:   2659
+  CStrings:  12884
 
Symbols:
+ _CGImageDestinationCreateWithData
+ _IMDLastMessageCandidateSQLFilter
+ _IMMessagePropertyAssociatedMessageType
+ _IMServerBagValueForKnownSender
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSThread
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
- _CGImageDestinationCreateWithURL
CStrings:
+ "\n    GROUP BY cmj.chat_id\n), recent_chats AS (\n    SELECT "
+ "\nFROM chat c\nJOIN chat_message_join cmj ON\n  cmj.chat_id == c.rowid\nINNER JOIN message m ON m.ROWID = cmj.message_id\nWHERE\n  c.is_archived = 0 AND c.is_filtered = ?\n  AND "
+ "\nGROUP BY\n  c.rowid\nORDER BY\n  MAX(cmj.message_date) DESC\nLIMIT ?;"
+ "\nGROUP BY cmj.chat_id\nORDER BY max(cmj.message_date) DESC;"
+ "Beginning blocking index extension on file transfer download for %lu GUIDs"
+ "Beginning blocking index extension on file transfer download for GUID %@"
+ "Failed to create image destination for %s"
+ "Failed to create image destination for %{private}@"
+ "Failed to finalize image for %s"
+ "Failed to write transcoded preview to %s: %@"
+ "Failed to write transcoded preview to %{private}@"
+ "Finished blocking index extension on file transfer download for %lu GUIDs, elapsed: %.3fs, responded: %lu/%lu, timedOut: %@"
+ "Finished blocking index extension on file transfer download for GUID %@, elapsed: %.3fs, timedOut: %@"
+ "IMDNotificationsController-force-notify"
+ "Main timer not started, can't measure timing: %@"
+ "New message received"
+ "SELECT ROWID, guid, style, state, account_id, properties, chat_identifier, service_name, room_name, account_login, is_archived, last_addressed_handle, display_name, group_id, is_filtered, successful_query, engram_id, server_change_token, ck_sync_state, original_group_id, last_read_message_timestamp, cloudkit_record_id, last_addressed_sim_id, is_blackholed, syndication_date, syndication_type, is_recovered, is_deleting_incoming_messages FROM chat LEFT OUTER JOIN chat_message_join ON    chat_message_join.chat_id == chat.rowid    AND chat_message_join.message_date = (       SELECT MAX(cmj_inner.message_date)        FROM chat_message_join cmj_inner        INNER JOIN message m ON m.ROWID = cmj_inner.message_id        WHERE cmj_inner.chat_id = chat.rowid            AND m.is_finished = 1 AND m.item_type = 0 AND m.associated_message_type != 3 AND NOT (m.schedule_type = 2 AND (m.schedule_state = 1 OR m.schedule_state = 2)) )WHERE    chat.is_archived = 0 %@ GROUP BY    chat.rowid HAVING    chat_message_join.message_date < ? ORDER BY    chat_message_join.message_date %@ LIMIT    ?;"
+ "SELECT ROWID, guid, style, state, account_id, properties, chat_identifier, service_name, room_name, account_login, is_archived, last_addressed_handle, display_name, group_id, is_filtered, successful_query, engram_id, server_change_token, ck_sync_state, original_group_id, last_read_message_timestamp, cloudkit_record_id, last_addressed_sim_id, is_blackholed, syndication_date, syndication_type, is_recovered, is_deleting_incoming_messages FROM chat LEFT OUTER JOIN chat_message_join ON    chat_message_join.chat_id == chat.rowid    AND chat_message_join.message_date = (       SELECT MAX(cmj_inner.message_date)        FROM chat_message_join cmj_inner        INNER JOIN message m ON m.ROWID = cmj_inner.message_id        WHERE cmj_inner.chat_id = chat.rowid            AND m.is_finished = 1 AND m.item_type = 0 AND m.associated_message_type != 3 AND NOT (m.schedule_type = 2 AND (m.schedule_state = 1 OR m.schedule_state = 2)) )WHERE    chat.is_archived = 0 %@ GROUP BY    chat.rowid ORDER BY    chat_message_join.message_date %@ LIMIT    ?;"
+ "SELECT cmj.chat_id, max(cmj.message_date)\nFROM chat_message_join cmj\nINNER JOIN message m ON m.ROWID = cmj.message_id\nWHERE "
+ "SELECT m.ROWID FROM message m INNER JOIN chat_message_join cm ON cm.chat_id = ? AND cm.message_id = m.ROWID WHERE m.is_finished = 1 AND m.item_type = 0 AND m.associated_message_type != 3 AND NOT (m.schedule_type = 2 AND (m.schedule_state = 1 OR m.schedule_state = 2)) ORDER BY cm.message_date DESC, cm.message_id DESC LIMIT 1"
+ "WITH chat_times AS (\n    SELECT cmj.chat_id, MAX(cmj.message_date) AS latest_date\n    FROM chat_message_join cmj\n    INNER JOIN message m ON m.ROWID = cmj.message_id\n    WHERE "
+ "__abortCurrentTimers"
+ "__elapsedTimingForKey:"
+ "__logResults:"
+ "__startMainTimerWithExpectedTimeoutInterval:"
+ "__startTimingForKey:"
+ "__stopMainTimerAndLogAfterFailure"
+ "__stopMainTimerAndLogAfterSuccess"
+ "__stopProfilingAfterIndexersBailed"
+ "__stopTimingForKey:"
+ "d24@0:8@16"
+ "elapsedTimingForKey:"
+ "elapsedTimingForMainTimer"
+ "m.is_finished = 1 AND m.item_type = 0 AND m.associated_message_type != 3 AND NOT (m.schedule_type = 2 AND (m.schedule_state = 1 OR m.schedule_state = 2)) "
+ "simulateRecipientIndexerTimeoutRace"
+ "sleepForTimeInterval:"
+ "threadSafeIndexProfiler"
+ "writeToURL:atomically:"
+ "writeToURL:options:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\nFROM chat c\nJOIN chat_message_join cmj ON\n  cmj.chat_id == c.rowid\nWHERE\n  c.is_archived = 0 AND c.is_filtered = ?\nGROUP BY\n  c.rowid\nORDER BY\n  MAX(cmj.message_date) DESC\nLIMIT ?;"
- "Beginning blocking index extension on file transfer download."
- "Failed to create image destination at URL: %s"
- "Failed to create image destination with %{private}@"
- "Finished blocking index extension on file transfer download."
- "SELECT ROWID from message m                 INNER JOIN chat_message_join cm ON cm.chat_id = ? AND cm.message_id = m.ROWID                 WHERE m.item_type == 0                 AND (m.schedule_type == 0                     OR (m.schedule_type == 2 AND (m.schedule_state != 1 AND m.schedule_state != 2)))                 ORDER BY cm.message_date DESC, cm.message_id DESC LIMIT 1"
- "SELECT ROWID, guid, style, state, account_id, properties, chat_identifier, service_name, room_name, account_login, is_archived, last_addressed_handle, display_name, group_id, is_filtered, successful_query, engram_id, server_change_token, ck_sync_state, original_group_id, last_read_message_timestamp, cloudkit_record_id, last_addressed_sim_id, is_blackholed, syndication_date, syndication_type, is_recovered, is_deleting_incoming_messages FROM chat LEFT OUTER JOIN chat_message_join ON    chat_message_join.chat_id == chat.rowid    AND chat_message_join.message_date = (SELECT MAX(message_date) FROM chat_message_join WHERE chat_message_join.chat_id = chat.rowid) WHERE    chat.is_archived = 0 %@ GROUP BY    chat.rowid HAVING    chat_message_join.message_date < ? ORDER BY    chat_message_join.message_date %@ LIMIT    ?;"
- "SELECT ROWID, guid, style, state, account_id, properties, chat_identifier, service_name, room_name, account_login, is_archived, last_addressed_handle, display_name, group_id, is_filtered, successful_query, engram_id, server_change_token, ck_sync_state, original_group_id, last_read_message_timestamp, cloudkit_record_id, last_addressed_sim_id, is_blackholed, syndication_date, syndication_type, is_recovered, is_deleting_incoming_messages FROM chat LEFT OUTER JOIN chat_message_join ON    chat_message_join.chat_id == chat.rowid    AND chat_message_join.message_date = (SELECT MAX(message_date) FROM chat_message_join WHERE chat_message_join.chat_id = chat.rowid) WHERE    chat.is_archived = 0 %@ GROUP BY    chat.rowid ORDER BY    chat_message_join.message_date %@ LIMIT    ?;"
- "SELECT chat_id, max(message_date)\nFROM chat_message_join\nGROUP BY chat_id\nORDER BY message_date DESC;"
- "SELECT cm.message_id from chat_message_join cm where cm.chat_id = ? ORDER BY cm.message_date DESC, cm.message_id DESC LIMIT 1;"
- "WITH chat_times AS (\n    SELECT chat_id, MAX(message_date) AS latest_date\n    FROM chat_message_join\n    GROUP BY chat_id\n), recent_chats AS (\n    SELECT "
- "logResults:"

```
