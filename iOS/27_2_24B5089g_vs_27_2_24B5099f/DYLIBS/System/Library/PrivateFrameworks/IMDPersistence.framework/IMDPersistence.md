## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1491.200.73.0.0
-  __TEXT.__text: 0x2f28b4
-  __TEXT.__objc_methlist: 0xa49c
+1491.200.95.0.0
+  __TEXT.__text: 0x2f42c0
+  __TEXT.__objc_methlist: 0xa584
   __TEXT.__const: 0xc3d0
-  __TEXT.__cstring: 0x5db34
-  __TEXT.__oslogstring: 0x3c3c4
-  __TEXT.__gcc_except_tab: 0xc764
+  __TEXT.__cstring: 0x5eba4
+  __TEXT.__oslogstring: 0x3c244
+  __TEXT.__gcc_except_tab: 0xc5ec
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
-  __TEXT.__swift5_typeref: 0x5256
-  __TEXT.__swift5_capture: 0x1ff4
-  __TEXT.__constg_swiftt: 0x594c
+  __TEXT.__swift5_typeref: 0x5278
+  __TEXT.__swift5_capture: 0x2044
+  __TEXT.__constg_swiftt: 0x5988
   __TEXT.__swift5_builtin: 0x348
   __TEXT.__swift5_reflstr: 0x3879
   __TEXT.__swift5_fieldmd: 0x36c4

   __TEXT.__swift5_proto: 0x4c0
   __TEXT.__swift5_types: 0x390
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift_as_entry: 0x160
-  __TEXT.__swift_as_ret: 0x180
-  __TEXT.__swift_as_cont: 0x398
+  __TEXT.__swift_as_entry: 0x168
+  __TEXT.__swift_as_ret: 0x184
+  __TEXT.__swift_as_cont: 0x3a8
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xd5f8
-  __TEXT.__eh_frame: 0x9d24
+  __TEXT.__unwind_info: 0xd698
+  __TEXT.__eh_frame: 0x9ddc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6528
-  __DATA_CONST.__objc_classlist: 0x6e8
+  __DATA_CONST.__const: 0x6548
+  __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x308
+  __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b70
+  __DATA_CONST.__objc_selrefs: 0x6ba8
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __DATA_CONST.__got: 0x1c30
-  __AUTH_CONST.__const: 0xe268
+  __DATA_CONST.__got: 0x1c40
+  __AUTH_CONST.__const: 0xe330
   __AUTH_CONST.__cfstring: 0x131c0
-  __AUTH_CONST.__objc_const: 0x13b20
+  __AUTH_CONST.__objc_const: 0x13d80
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x29f8
-  __AUTH.__objc_data: 0xfc0
+  __AUTH_CONST.__auth_got: 0x2a10
+  __AUTH.__objc_data: 0x1060
   __AUTH.__data: 0x1cb0
-  __DATA.__objc_ivar: 0x568
-  __DATA.__data: 0x3a70
+  __DATA.__objc_ivar: 0x56c
+  __DATA.__data: 0x3bb0
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0x30b8
-  __DATA_DIRTY.__data: 0x6500
+  __DATA_DIRTY.__data: 0x6560
   __DATA_DIRTY.__bss: 0x2a00
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13788
-  Symbols:   2852
-  CStrings:  7546
+  Functions: 13842
+  Symbols:   2859
+  CStrings:  7543
 
Symbols:
+ _IMAttachmentPreflightPreviewFileURL
+ _IMCoreSpotlightIndexBehaviorFromReason
+ _IMSharedHelperCurrentRegionForcesFilterUnknownSenders
+ _OBJC_CLASS_$_IMDCoreSpotlightIndexerProvider
+ _OBJC_CLASS_$_IMDCoreSpotlightSearchableItemGeneratorDependencyProvider
+ _OBJC_METACLASS_$_IMDCoreSpotlightIndexerProvider
+ _OBJC_METACLASS_$_IMDCoreSpotlightSearchableItemGeneratorDependencyProvider
CStrings:
+ ")) AND\n        mU.is_finished == 1 AND\n        mU.is_from_me == 0 AND\n        mU.item_type == 0 AND\n        mU.is_system_message == 0\n)"
+ "EXISTS (\n    SELECT 1 FROM chat_message_join cmjU\n    INNER JOIN message mU ON mU.rowid = cmjU.message_id\n    WHERE cmjU.chat_id = c.rowid AND\n        mU.is_read == 0 AND\n        NOT (mU.ROWID in (SELECT message_id FROM "
+ "EXISTS (\n    SELECT 1 FROM chat_part cpU\n    INNER JOIN chat_part_message_join cmjU ON cpU.rowid = cmjU.chat_part_id\n    INNER JOIN message mU ON mU.rowid = cmjU.message_id\n    WHERE cpU.chat_id = c.rowid AND\n        mU.is_read == 0 AND\n        NOT (mU.ROWID in (SELECT message_id FROM "
+ "Filename was null (%@) for file transfer %@ -- did not generate attachment preview"
+ "Final preview unavailable, falling back to preview-stage preview for transfer %{private}@"
+ "INSERT OR IGNORE INTO chat_message_join (chat_id, message_id, message_date, filter_action, filter_sub_action) SELECT ?, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM chat_recoverable_message_join WHERE chat_id = ? AND message_id = ?);"
+ "INSERT OR IGNORE INTO chat_part_message_join (chat_part_id, message_id, message_date, filter_action, filter_sub_action)\nSELECT ?, ?, ?, ?, ?\nWHERE NOT EXISTS (SELECT 1 FROM chat_part_recoverable_message_join WHERE chat_part_id = ? AND message_id = ?);"
+ "Not attaching a preview for transfer %@ to the notification (sensitive %{BOOL}d, adaptive image glyph %{BOOL}d, rejected %{BOOL}d); with all three false, no preview was on disk"
+ "PersistentTaskBatchTimeoutSeconds"
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a INNER JOIN message_attachment_join ma ON   a.ROWID = ma.attachment_id INNER JOIN chat_message_join cm ON   ma.message_id = cm.message_id INNER JOIN message m ON   ma.message_id = m.ROWID WHERE   m.cache_has_attachments   AND m.expire_state != %d   AND cm.chat_id IN (%@)   AND a.hide_attachment == 0   AND a.ck_sync_state == 1   AND a.transfer_state == 0 ORDER BY m.date DESC limit %d"
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') ORDER BY a.ROWID LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' ORDER BY a.ROWID LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.created_date, a.start_date, a.filename, a.uti, a.mime_type, a.transfer_state, a.is_outgoing, a.user_info, a.transfer_name, a.total_bytes, a.is_sticker, a.sticker_user_info, a.attribution_info, a.hide_attachment, a.ck_sync_state, a.ck_server_change_token_blob, a.ck_record_id, a.original_guid, a.is_commsafety_sensitive, a.emoji_image_content_identifier, a.emoji_image_short_description, a.preview_generation_state, a.preflight_info, a.sensitivity_analysis, a.fields_needing_sync  FROM attachment a WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 ORDER BY a.ROWID LIMIT ? "
- ")) AND\nm.is_finished == 1 AND\nm.is_from_me == 0 AND\nm.item_type == 0 AND\nm.is_system_message == 0"
- "Bailing early from _IMDCoreSpotlightNicknameForAddress: Shared Name and Photo is not enabled"
- "Bailing early from _IMDKVStoreForHandledNicknames: Shared Name and Photo is not enabled"
- "Bailing early from _IMDKVStoreForPendingNicknames: Shared Name and Photo is not enabled"
- "Bailing early from _IMDNicknameInfoForAddress: Shared Name and Photo is not enabled"
- "Bailing early from _IMNicknameInfoForKVStore: Shared Name and Photo is not enabled"
- "Bailing early from _nicknameDisplayNameForID: Shared Name and Photo is not enabled"
- "Filename was null (%@) or transfer state was not finished (%@) for file transfer %@ -- did not generate attachment preview"
- "INSERT OR IGNORE INTO chat_message_join (chat_id, message_id, message_date, filter_action, filter_sub_action) VALUES (?, ?, ?, ?, ?);"
- "INSERT OR IGNORE INTO chat_part_message_join (chat_part_id, message_id, message_date, filter_action, filter_sub_action)\nVALUES (?, ?, ?, ?, ?);"
- "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON   a.ROWID = ma.attachment_id INNER JOIN chat_message_join cm ON   ma.message_id = cm.message_id INNER JOIN message m ON   ma.message_id = m.ROWID WHERE   m.cache_has_attachments   AND m.expire_state != %d   AND cm.chat_id IN (%@)   AND a.hide_attachment == 0   AND a.ck_sync_state == 1   AND a.transfer_state == 0 ORDER BY m.date DESC limit %d"
- "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
- "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.chatbot') ORDER BY a.ROWID LIMIT ? "
- "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
- "SELECT * FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 0 AND m.balloon_bundle_id == 'com.apple.messages.chatbot' ORDER BY a.ROWID LIMIT ? "
- "SELECT * FROM attachment a WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 AND a.ROWID > ? ORDER BY a.ROWID LIMIT ? "
- "SELECT * FROM attachment a WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 ORDER BY a.ROWID LIMIT ? "
- "We didn't generate a previewFileURL for transfer %@ to generate a notification preview"
- "m.is_read == 0 AND\nNOT (m.ROWID in (SELECT message_id FROM "
```
