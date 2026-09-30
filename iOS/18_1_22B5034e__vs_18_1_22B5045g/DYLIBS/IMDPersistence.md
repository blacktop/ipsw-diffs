## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.200.35.0.0
-  __TEXT.__text: 0x1148e0
+1402.200.57.0.0
+  __TEXT.__text: 0x11499c
   __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_methlist: 0x3734
   __TEXT.__const: 0xb5a
-  __TEXT.__cstring: 0x383a1
+  __TEXT.__cstring: 0x39151
   __TEXT.__oslogstring: 0x19a55
-  __TEXT.__gcc_except_tab: 0xd2c0
+  __TEXT.__gcc_except_tab: 0xd2cc
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__unwind_info: 0x4c98
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xaac
-  __TEXT.__objc_methname: 0xff55
-  __TEXT.__objc_methtype: 0x23e1
+  __TEXT.__objc_methname: 0xff5c
+  __TEXT.__objc_methtype: 0x2414
   __TEXT.__objc_stubs: 0xd400
   __DATA_CONST.__got: 0xdd8
-  __DATA_CONST.__const: 0x10d50
+  __DATA_CONST.__const: 0x10d78
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108

   __AUTH_CONST.__auth_got: 0x1368
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x1aa8
-  __AUTH_CONST.__cfstring: 0x10b80
+  __AUTH_CONST.__cfstring: 0x10c00
   __AUTH_CONST.__objc_const: 0x68a0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 4456
   Symbols:   2308
-  CStrings:  7314
+  CStrings:  7322
 
CStrings:
+ "recoverableMessagesMetadataPendingCloudKitSaveWithLimit:filter:"
+ "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
+ "@\"NSArray\"32@0:8q16Q24"
+ "filter"
+ "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') ORDER BY a.ROWID LIMIT ? "
+ "SELECT c.guid, crmj.message_id, m.guid, crmj.delete_date, -1, NULL FROM chat_recoverable_message_join AS crmj JOIN chat AS c  ON c.ROWID = crmj.chat_id JOIN message AS m  ON m.ROWID = crmj.message_id WHERE crmj.ck_sync_state = 0 AND balloon_bundle_id == 'com.apple.messages.chatbot'   UNION ALL SELECT c.guid, rmp.message_id, m.guid, rmp.delete_date, rmp.part_index, rmp.part_text  FROM recoverable_message_part AS rmp  JOIN chat AS c   ON c.ROWID = rmp.chat_id  JOIN message AS m   ON m.ROWID = rmp.message_id  WHERE rmp.ck_sync_state = 0 AND balloon_bundle_id == 'com.apple.messages.chatbot'  LIMIT ?;"
+ "@32@0:8Q16Q24"
+ "@32@0:8q16Q24"
+ "SELECT ROWID, guid, text, replace, service_center, handle_id, subject, country, attributedBody, version, type, service, account, account_guid, error, date, date_read, date_delivered, is_delivered, is_finished, is_emote, is_from_me, is_empty, is_delayed, is_auto_reply, is_prepared, is_read, is_system_message, is_sent, has_dd_results, is_service_message, is_forward, was_downgraded, is_archive, cache_has_attachments, cache_roomnames, was_data_detected, was_deduplicated, is_audio_message, is_played, date_played, item_type, other_handle, group_title, group_action_type, share_status,  share_direction, is_expirable, expire_state, message_action_type, message_source, associated_message_guid, associated_message_type, balloon_bundle_id, payload_data, expressive_send_style_id,  associated_message_range_location, associated_message_range_length, time_expressive_send_played, message_summary_info, ck_sync_state, ck_record_id, ck_record_change_tag, destination_caller_id, is_corrupt, reply_to_guid, sort_id, is_spam, has_unseen_mention, thread_originator_guid, thread_originator_part, syndication_ranges, synced_syndication_ranges, was_delivered_quietly, did_notify_recipient, date_retracted, date_edited, was_detonated, part_count, is_stewie, is_sos, is_critical, bia_reference_id, is_kt_verified, fallback_hash, associated_message_emoji, is_pending_satellite_send, needs_relay, schedule_type, schedule_state, sent_or_received_off_grid FROM message WHERE ck_sync_state == 0 AND TRIM(guid) <> '' AND (service in ('iMessage', 'SMS', 'RCS', 'SatelliteSMS', 'iMessageLite'))AND was_detonated == 0 AND schedule_type != 2 AND (balloon_bundle_id IS NULL OR balloon_bundle_id != 'com.apple.messages.chatbot') ORDER BY date LIMIT ? ;"
+ "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
+ "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' ORDER BY a.ROWID LIMIT ? "
+ "SELECT ROWID, guid, text, replace, service_center, handle_id, subject, country, attributedBody, version, type, service, account, account_guid, error, date, date_read, date_delivered, is_delivered, is_finished, is_emote, is_from_me, is_empty, is_delayed, is_auto_reply, is_prepared, is_read, is_system_message, is_sent, has_dd_results, is_service_message, is_forward, was_downgraded, is_archive, cache_has_attachments, cache_roomnames, was_data_detected, was_deduplicated, is_audio_message, is_played, date_played, item_type, other_handle, group_title, group_action_type, share_status,  share_direction, is_expirable, expire_state, message_action_type, message_source, associated_message_guid, associated_message_type, balloon_bundle_id, payload_data, expressive_send_style_id,  associated_message_range_location, associated_message_range_length, time_expressive_send_played, message_summary_info, ck_sync_state, ck_record_id, ck_record_change_tag, destination_caller_id, is_corrupt, reply_to_guid, sort_id, is_spam, has_unseen_mention, thread_originator_guid, thread_originator_part, syndication_ranges, synced_syndication_ranges, was_delivered_quietly, did_notify_recipient, date_retracted, date_edited, was_detonated, part_count, is_stewie, is_sos, is_critical, bia_reference_id, is_kt_verified, fallback_hash, associated_message_emoji, is_pending_satellite_send, needs_relay, schedule_type, schedule_state, sent_or_received_off_grid FROM message WHERE ck_sync_state == 0 AND TRIM(guid) <> '' AND (service in ('iMessage', 'SMS', 'RCS', 'SatelliteSMS', 'iMessageLite'))AND was_detonated == 0 AND schedule_type != 2 AND balloon_bundle_id == 'com.apple.messages.chatbot' ORDER BY date LIMIT ? ;"
+ "SELECT c.guid, crmj.message_id, m.guid, crmj.delete_date, -1, NULL FROM chat_recoverable_message_join AS crmj JOIN chat AS c  ON c.ROWID = crmj.chat_id JOIN message AS m  ON m.ROWID = crmj.message_id WHERE crmj.ck_sync_state = 0  AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot')  UNION ALL SELECT c.guid, rmp.message_id, m.guid, rmp.delete_date, rmp.part_index, rmp.part_text  FROM recoverable_message_part AS rmp  JOIN chat AS c   ON c.ROWID = rmp.chat_id  JOIN message AS m   ON m.ROWID = rmp.message_id  WHERE rmp.ck_sync_state = 0  AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') LIMIT ?;"
- "SELECT * FROM attachment a WHERE a.ck_sync_state == 0 ORDER BY a.ROWID LIMIT ? "
- "recoverableMessagesMetadataPendingCloudKitSaveWithLimit:"
- "SELECT c.guid, crmj.message_id, m.guid, crmj.delete_date, -1, NULL FROM chat_recoverable_message_join AS crmj JOIN chat AS c  ON c.ROWID = crmj.chat_id JOIN message AS m  ON m.ROWID = crmj.message_id WHERE crmj.ck_sync_state = 0  UNION ALL SELECT c.guid, rmp.message_id, m.guid, rmp.delete_date, rmp.part_index, rmp.part_text  FROM recoverable_message_part AS rmp  JOIN chat AS c   ON c.ROWID = rmp.chat_id  JOIN message AS m   ON m.ROWID = rmp.message_id  WHERE rmp.ck_sync_state = 0 LIMIT ?;"
- "SELECT ROWID, guid, text, replace, service_center, handle_id, subject, country, attributedBody, version, type, service, account, account_guid, error, date, date_read, date_delivered, is_delivered, is_finished, is_emote, is_from_me, is_empty, is_delayed, is_auto_reply, is_prepared, is_read, is_system_message, is_sent, has_dd_results, is_service_message, is_forward, was_downgraded, is_archive, cache_has_attachments, cache_roomnames, was_data_detected, was_deduplicated, is_audio_message, is_played, date_played, item_type, other_handle, group_title, group_action_type, share_status,  share_direction, is_expirable, expire_state, message_action_type, message_source, associated_message_guid, associated_message_type, balloon_bundle_id, payload_data, expressive_send_style_id,  associated_message_range_location, associated_message_range_length, time_expressive_send_played, message_summary_info, ck_sync_state, ck_record_id, ck_record_change_tag, destination_caller_id, is_corrupt, reply_to_guid, sort_id, is_spam, has_unseen_mention, thread_originator_guid, thread_originator_part, syndication_ranges, synced_syndication_ranges, was_delivered_quietly, did_notify_recipient, date_retracted, date_edited, was_detonated, part_count, is_stewie, is_sos, is_critical, bia_reference_id, is_kt_verified, fallback_hash, associated_message_emoji, is_pending_satellite_send, needs_relay, schedule_type, schedule_state, sent_or_received_off_grid FROM message WHERE ck_sync_state == 0 AND TRIM(guid) <> '' AND (service in ('iMessage', 'SMS', 'RCS', 'SatelliteSMS', 'iMessageLite'))AND was_detonated == 0 AND schedule_type != 2 ORDER BY date LIMIT ? ;"
- "SELECT * FROM attachment a WHERE a.ck_sync_state == 0 and a.ROWID > ? ORDER BY a.ROWID LIMIT ? "

```
