## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.600.41.2.8
-  __TEXT.__text: 0x11e364
+1402.700.41.0.0
+  __TEXT.__text: 0x11e630
   __TEXT.__auth_stubs: 0x2800
-  __TEXT.__objc_methlist: 0x423c
+  __TEXT.__objc_methlist: 0x4244
   __TEXT.__const: 0xb70
-  __TEXT.__cstring: 0x39ac1
-  __TEXT.__oslogstring: 0x1a205
+  __TEXT.__cstring: 0x39af1
+  __TEXT.__oslogstring: 0x1a285
   __TEXT.__gcc_except_tab: 0xe5d4
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x2a4

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4eb8
+  __TEXT.__unwind_info: 0x4ec8
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0xb5b
-  __TEXT.__objc_methname: 0x10c37
-  __TEXT.__objc_methtype: 0x24b8
-  __TEXT.__objc_stubs: 0xe000
+  __TEXT.__objc_methname: 0x10c67
+  __TEXT.__objc_methtype: 0x24c3
+  __TEXT.__objc_stubs: 0xe020
   __DATA_CONST.__got: 0xf00
   __DATA_CONST.__const: 0x11110
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3dc8
+  __DATA_CONST.__objc_selrefs: 0x3dd0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x1410
-  __AUTH_CONST.__const: 0x1ad0
-  __AUTH_CONST.__cfstring: 0x11560
+  __AUTH_CONST.__const: 0x1af0
+  __AUTH_CONST.__cfstring: 0x11580
   __AUTH_CONST.__objc_const: 0x6028
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x190
   __DATA.__data: 0xae8
-  __DATA.__bss: 0x4c0
+  __DATA.__bss: 0x4d0
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x17a0
   __DATA_DIRTY.__data: 0xf00

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 75A6B764-111E-33AE-BAFD-97DE6FF1B84B
-  Functions: 4668
+  UUID: D6112BC7-939C-32CA-8AE6-BC46C90AA316
+  Functions: 4672
   Symbols:   2372
-  CStrings:  9780
+  CStrings:  9785
 
CStrings:
+ "@20@0:8B16"
+ "IMDDatabaseClient | Early return: Recently Deleted:storeRecoverableMessagePartWithBody given messageGUID: %@ partBody: %@"
+ "Recently Deleted | Bailing:storeRecoverableMessagePartWithBody will not store empty part"
+ "Recently Deleted | Cannot recover: Could not find attributed body for messageGUID: %@, rebuilding from scratch"
+ "SELECT ROWID from message m                 INNER JOIN chat_message_join cm ON cm.chat_id = ? AND cm.message_id = m.ROWID                 WHERE m.item_type == 0                 AND (m.schedule_type == 0                     OR (m.schedule_type == 2 AND (m.schedule_state != 1 AND m.schedule_state != 2)))                 ORDER BY cm.message_date DESC, cm.message_id DESC LIMIT 1"
+ "SELECT m.ROWID, m.guid, m.text, m.replace, m.service_center, m.handle_id, m.subject, m.country, m.attributedBody, m.version, m.type, m.service, m.account, m.account_guid, m.error, m.date, m.date_read, m.date_delivered, m.is_delivered, m.is_finished, m.is_emote, m.is_from_me, m.is_empty, m.is_delayed, m.is_auto_reply, m.is_prepared, m.is_read, m.is_system_message, m.is_sent, m.has_dd_results, m.is_service_message, m.is_forward, m.was_downgraded, m.is_archive, m.cache_has_attachments, m.cache_roomnames, m.was_data_detected, m.was_deduplicated, m.is_audio_message, m.is_played, m.date_played, m.item_type, m.other_handle, m.group_title, m.group_action_type, m.share_status, m.share_direction, m.is_expirable, m.expire_state, m.message_action_type, m.message_source, m.associated_message_guid, m.associated_message_type, m.balloon_bundle_id, m.payload_data, m.expressive_send_style_id, m.associated_message_range_location, m.associated_message_range_length, m.time_expressive_send_played, m.message_summary_info, m.ck_sync_state, m.ck_record_id, m.ck_record_change_tag, m.destination_caller_id, m.is_corrupt, m.reply_to_guid, m.sort_id, m.is_spam, m.has_unseen_mention, m.thread_originator_guid, m.thread_originator_part, m.syndication_ranges, m.synced_syndication_ranges, m.was_delivered_quietly, m.did_notify_recipient, m.date_retracted, m.date_edited, m.date_recovered, m.was_detonated, m.part_count, m.is_stewie, m.is_sos, m.is_critical, m.bia_reference_id, m.is_kt_verified, m.fallback_hash, m.associated_message_emoji, m.is_pending_satellite_send, m.needs_relay, m.schedule_type, m.schedule_state, m.sent_or_received_off_grid FROM message m  INNER JOIN chat_message_join cm ON cm.message_id = m.rowid  INNER JOIN chat c ON c.ROWID = cm.chat_id  WHERE c.guid = ?  AND m.schedule_type == 2  AND (m.schedule_state == 1 OR m.schedule_state == 2)  ORDER BY cm.message_date ASC LIMIT ?"
+ "SELECT m.ROWID, m.guid, m.text, m.replace, m.service_center, m.handle_id, m.subject, m.country, m.attributedBody, m.version, m.type, m.service, m.account, m.account_guid, m.error, m.date, m.date_read, m.date_delivered, m.is_delivered, m.is_finished, m.is_emote, m.is_from_me, m.is_empty, m.is_delayed, m.is_auto_reply, m.is_prepared, m.is_read, m.is_system_message, m.is_sent, m.has_dd_results, m.is_service_message, m.is_forward, m.was_downgraded, m.is_archive, m.cache_has_attachments, m.cache_roomnames, m.was_data_detected, m.was_deduplicated, m.is_audio_message, m.is_played, m.date_played, m.item_type, m.other_handle, m.group_title, m.group_action_type, m.share_status, m.share_direction, m.is_expirable, m.expire_state, m.message_action_type, m.message_source, m.associated_message_guid, m.associated_message_type, m.balloon_bundle_id, m.payload_data, m.expressive_send_style_id, m.associated_message_range_location, m.associated_message_range_length, m.time_expressive_send_played, m.message_summary_info, m.ck_sync_state, m.ck_record_id, m.ck_record_change_tag, m.destination_caller_id, m.is_corrupt, m.reply_to_guid, m.sort_id, m.is_spam, m.has_unseen_mention, m.thread_originator_guid, m.thread_originator_part, m.syndication_ranges, m.synced_syndication_ranges, m.was_delivered_quietly, m.did_notify_recipient, m.date_retracted, m.date_edited, m.date_recovered, m.was_detonated, m.part_count, m.is_stewie, m.is_sos, m.is_critical, m.bia_reference_id, m.is_kt_verified, m.fallback_hash, m.associated_message_emoji, m.is_pending_satellite_send, m.needs_relay, m.schedule_type, m.schedule_state, m.sent_or_received_off_grid FROM message m  INNER JOIN chat_message_join cm ON cm.message_id = m.rowid  INNER JOIN chat c ON c.ROWID = cm.chat_id  WHERE m.schedule_type == 2  AND (m.schedule_state == 1 OR m.schedule_state == 2)  ORDER BY cm.message_date ASC LIMIT ?"
+ "_messageKeyPathsToColumnsQueryingChatJoinTable:"
+ "chat_message_join.message_date"
- "IMDDatabaseClient | Early return: Recently Deleted:storeRecoverableMessagePartWithBody given messageGUID: %@"
- "Recently Deleted | Cannot recover: Could not find attributed body for messageGUID: %@"
- "SELECT ROWID from message m                 WHERE m.item_type == 0                 AND (m.schedule_type == 0                     OR (m.schedule_type == 2 AND (m.schedule_state != 1 AND m.schedule_state != 2)))                 AND m.ROWID in                     (SELECT message_id FROM chat_message_join where chat_id = ?)                 ORDER BY date DESC, ROWID DESC LIMIT 1"
- "SELECT m.ROWID, m.guid, m.text, m.replace, m.service_center, m.handle_id, m.subject, m.country, m.attributedBody, m.version, m.type, m.service, m.account, m.account_guid, m.error, m.date, m.date_read, m.date_delivered, m.is_delivered, m.is_finished, m.is_emote, m.is_from_me, m.is_empty, m.is_delayed, m.is_auto_reply, m.is_prepared, m.is_read, m.is_system_message, m.is_sent, m.has_dd_results, m.is_service_message, m.is_forward, m.was_downgraded, m.is_archive, m.cache_has_attachments, m.cache_roomnames, m.was_data_detected, m.was_deduplicated, m.is_audio_message, m.is_played, m.date_played, m.item_type, m.other_handle, m.group_title, m.group_action_type, m.share_status, m.share_direction, m.is_expirable, m.expire_state, m.message_action_type, m.message_source, m.associated_message_guid, m.associated_message_type, m.balloon_bundle_id, m.payload_data, m.expressive_send_style_id, m.associated_message_range_location, m.associated_message_range_length, m.time_expressive_send_played, m.message_summary_info, m.ck_sync_state, m.ck_record_id, m.ck_record_change_tag, m.destination_caller_id, m.is_corrupt, m.reply_to_guid, m.sort_id, m.is_spam, m.has_unseen_mention, m.thread_originator_guid, m.thread_originator_part, m.syndication_ranges, m.synced_syndication_ranges, m.was_delivered_quietly, m.did_notify_recipient, m.date_retracted, m.date_edited, m.date_recovered, m.was_detonated, m.part_count, m.is_stewie, m.is_sos, m.is_critical, m.bia_reference_id, m.is_kt_verified, m.fallback_hash, m.associated_message_emoji, m.is_pending_satellite_send, m.needs_relay, m.schedule_type, m.schedule_state, m.sent_or_received_off_grid FROM message m  INNER JOIN chat_message_join cm ON cm.message_id = m.rowid  INNER JOIN chat c ON c.ROWID = cm.chat_id  WHERE c.guid = ?  AND m.schedule_type == 2  AND (m.schedule_state == 1 OR m.schedule_state == 2)  ORDER BY m.date ASC LIMIT ?"
- "SELECT m.ROWID, m.guid, m.text, m.replace, m.service_center, m.handle_id, m.subject, m.country, m.attributedBody, m.version, m.type, m.service, m.account, m.account_guid, m.error, m.date, m.date_read, m.date_delivered, m.is_delivered, m.is_finished, m.is_emote, m.is_from_me, m.is_empty, m.is_delayed, m.is_auto_reply, m.is_prepared, m.is_read, m.is_system_message, m.is_sent, m.has_dd_results, m.is_service_message, m.is_forward, m.was_downgraded, m.is_archive, m.cache_has_attachments, m.cache_roomnames, m.was_data_detected, m.was_deduplicated, m.is_audio_message, m.is_played, m.date_played, m.item_type, m.other_handle, m.group_title, m.group_action_type, m.share_status, m.share_direction, m.is_expirable, m.expire_state, m.message_action_type, m.message_source, m.associated_message_guid, m.associated_message_type, m.balloon_bundle_id, m.payload_data, m.expressive_send_style_id, m.associated_message_range_location, m.associated_message_range_length, m.time_expressive_send_played, m.message_summary_info, m.ck_sync_state, m.ck_record_id, m.ck_record_change_tag, m.destination_caller_id, m.is_corrupt, m.reply_to_guid, m.sort_id, m.is_spam, m.has_unseen_mention, m.thread_originator_guid, m.thread_originator_part, m.syndication_ranges, m.synced_syndication_ranges, m.was_delivered_quietly, m.did_notify_recipient, m.date_retracted, m.date_edited, m.date_recovered, m.was_detonated, m.part_count, m.is_stewie, m.is_sos, m.is_critical, m.bia_reference_id, m.is_kt_verified, m.fallback_hash, m.associated_message_emoji, m.is_pending_satellite_send, m.needs_relay, m.schedule_type, m.schedule_state, m.sent_or_received_off_grid FROM message m  INNER JOIN chat_message_join cm ON cm.message_id = m.rowid  INNER JOIN chat c ON c.ROWID = cm.chat_id  WHERE m.schedule_type == 2  AND (m.schedule_state == 1 OR m.schedule_state == 2)  ORDER BY m.date ASC LIMIT ?"

```
