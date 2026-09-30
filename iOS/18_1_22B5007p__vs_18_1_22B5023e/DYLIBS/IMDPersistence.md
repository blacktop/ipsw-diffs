## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1301.200.8.2.1
-  __TEXT.__text: 0x112f74
-  __TEXT.__auth_stubs: 0x2670
-  __TEXT.__objc_methlist: 0x365c
-  __TEXT.__const: 0xb3a
-  __TEXT.__cstring: 0x379e1
-  __TEXT.__oslogstring: 0x198d5
-  __TEXT.__gcc_except_tab: 0xd128
+1402.200.8.0.0
+  __TEXT.__text: 0x114930
+  __TEXT.__auth_stubs: 0x26b0
+  __TEXT.__objc_methlist: 0x3734
+  __TEXT.__const: 0xb5a
+  __TEXT.__cstring: 0x38331
+  __TEXT.__oslogstring: 0x19a65
+  __TEXT.__gcc_except_tab: 0xd2cc
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4be0
+  __TEXT.__unwind_info: 0x4c88
   __TEXT.__eh_frame: 0x130
-  __TEXT.__objc_classname: 0xa59
-  __TEXT.__objc_methname: 0xfdbd
+  __TEXT.__objc_classname: 0xaac
+  __TEXT.__objc_methname: 0xff46
   __TEXT.__objc_methtype: 0x23e1
-  __TEXT.__objc_stubs: 0xd1e0
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__const: 0x10cf8
-  __DATA_CONST.__objc_classlist: 0x258
+  __TEXT.__objc_stubs: 0xd400
+  __DATA_CONST.__got: 0xdd8
+  __DATA_CONST.__const: 0x10d48
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3900
+  __DATA_CONST.__objc_selrefs: 0x3978
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x1348
+  __AUTH_CONST.__auth_got: 0x1368
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x1a68
-  __AUTH_CONST.__cfstring: 0x109c0
-  __AUTH_CONST.__objc_const: 0x66e0
+  __AUTH_CONST.__const: 0x1aa8
+  __AUTH_CONST.__cfstring: 0x10b40
+  __AUTH_CONST.__objc_const: 0x68a0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x490
+  __AUTH.__objc_data: 0x358
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x170
   __DATA.__data: 0xac0
   __DATA.__bss: 0x3f8
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1578
-  __DATA_DIRTY.__data: 0xe58
-  __DATA_DIRTY.__bss: 0x5b8
+  __DATA_DIRTY.__objc_data: 0x17a0
+  __DATA_DIRTY.__data: 0xe88
+  __DATA_DIRTY.__bss: 0x5c8
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4424
-  Symbols:   2297
-  CStrings:  7280
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4455
+  Symbols:   2307
+  CStrings:  7313
 
Symbols:
+ _IMAttachmentEmojiImagePreviewFileURL
+ _IMBrowserSnapshotCacheDirectoryURL
+ _IMDMessageRecordCopyNewParticipantChangeItems
+ _IMDMigrateTo18014
+ _IMDMigrateTo18015
+ _IMGetCachedDomainValueForKey
+ _IMMessagePropertyPendingSatelliteSend
+ _IMStickerCacheDirectoryURL
+ __IMStringStrippingControlCharacters
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _IMSharedHelperDeleteOrphanedStickerMMCSDownloadTokens
- _kIMDBrowserSnapshotCachePath
- _kIMDStickerCachePath
- _kStickerTransferInfoPlistFileFolder
- _kUTTypeAudio
- _kUTTypeImage
- _kUTTypeVideo
CStrings:
+ "%!@(MISSING) added %!@(MISSING) and chat has scheduled message count: %!l(MISSING)u"
+ "%!@(MISSING) added %!@(MISSING) to the conversation. %!l(MISSING)u scheduled messages"
+ "%!K(MISSING) > %!@(MISSING)"
+ "Deleting previews at %!@(MISSING)"
+ "Failed to create IMItem from IMMessageRecord: %!@(MISSING)"
+ "Failed to fetch chat for chatRecord: %!@(MISSING)"
+ "Failed to find plain text for spotlight because no message was found for guid %!@(MISSING)"
+ "Failed to load contact plist at: %!@(MISSING) (error: %!@(MISSING))"
+ "IMDMessageRecordCopyNewParticipantChangeItems"
+ "IMDMessageRecordCopyNewParticipantChangeItems got back %!l(MISSING)d rows"
+ "IMDSpotlightDataProvider"
+ "IMDSpotlightLinkDataProvider"
+ "IMDSpotlightTextDataProvider"
+ "LastPendingSatelliteSendDate"
+ "MessagesQueries"
+ "Not generating notification because chat %!@(MISSING) doesn't have scheduled messages in it"
+ "Not generating notification for participantChangeItem from myself: %!@(MISSING)"
+ "Not generating notification for participantChangeItem with changeType: %!l(MISSING)ld"
+ "Retracting all unread message notifications"
+ "SELECT   message_id FROM chat_message_join WHERE message_id in (SELECT rowid FROM message INDEXED BY message_idx_isRead_isFromMe_itemType  WHERE (is_read == 0     AND is_finished == 1     AND is_from_me == 0     AND (item_type == 0         OR item_type == 1)     AND is_system_message == 0     %!s(MISSING) )) AND chat_id %!@(MISSING)"
+ "SELECT count(rowid) FROM Attachment WHERE is_sticker = 1 AND filename LIKE ?;"
+ "SELECT m.ROWID, m.guid, m.text, m.replace, m.service_center, m.handle_id, m.subject, m.country, m.attributedBody, m.version, m.type, m.service, m.account, m.account_guid, m.error, m.date, m.date_read, m.date_delivered, m.is_delivered, m.is_finished, m.is_emote, m.is_from_me, m.is_empty, m.is_delayed, m.is_auto_reply, m.is_prepared, m.is_read, m.is_system_message, m.is_sent, m.has_dd_results, m.is_service_message, m.is_forward, m.was_downgraded, m.is_archive, m.cache_has_attachments, m.cache_roomnames, m.was_data_detected, m.was_deduplicated, m.is_audio_message, m.is_played, m.date_played, m.item_type, m.other_handle, m.group_title, m.group_action_type, m.share_status, m.share_direction, m.is_expirable, m.expire_state, m.message_action_type, m.message_source, m.associated_message_guid, m.associated_message_type, m.balloon_bundle_id, m.payload_data, m.expressive_send_style_id, m.associated_message_range_location, m.associated_message_range_length, m.time_expressive_send_played, m.message_summary_info, m.ck_sync_state, m.ck_record_id, m.ck_record_change_tag, m.destination_caller_id, m.is_corrupt, m.reply_to_guid, m.sort_id, m.is_spam, m.has_unseen_mention, m.thread_originator_guid, m.thread_originator_part, m.syndication_ranges, m.synced_syndication_ranges, m.was_delivered_quietly, m.did_notify_recipient, m.date_retracted, m.date_edited, m.was_detonated, m.part_count, m.is_stewie, m.is_sos, m.is_critical, m.bia_reference_id, m.is_kt_verified, m.fallback_hash, m.associated_message_emoji, m.is_pending_satellite_send, m.needs_relay, m.schedule_type, m.schedule_state, m.sent_or_received_off_grid FROM message m  INDEXED BY message_idx_isRead_isFromMe_itemType  INNER JOIN chat_message_join cm ON cm.message_id = m.rowid  INNER JOIN chat c ON c.ROWID = cm.chat_id  WHERE m.is_read == 0  AND m.is_from_me == 0  AND m.item_type == 1  ORDER BY m.date DESC;"
+ "Successfully loaded contact plist at: %!@(MISSING)"
+ "UPDATE message SET is_read = 1, date_read = %!l(MISSING)ld WHERE (is_read == 0 AND is_finished == 1 AND is_from_me == 0 AND item_type == 1 AND is_system_message == 0);"
+ "UPDATE message SET schedule_state = 4 WHERE (is_sent = 0 AND is_from_me = 1 AND error = 39)"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByAppendingPathExtension:"
+ "_createDataProviders"
+ "_dataProviders"
+ "_displayNameForHandle:"
+ "_failedMessageRecordsAfterDateInNanoseconds:"
+ "_notificationsSafePreviewFileURLForTransferURL:utiType:knownSender:"
+ "_removeAllDeliveredMessageNotifications"
+ "_userNotificationForParticipantChangeMessageRecord:"
+ "attachment(is_sticker)"
+ "attachmentPathsFromMessageRecord:"
+ "attachment_idx_is_sticker"
+ "attributedSubstringFromRange:"
+ "com.apple.madrid"
+ "com.apple.metadata-importer.messages.plain-text"
+ "contactForHandleRecord:"
+ "contactFormatterTitle"
+ "dataForGUID:error:"
+ "dataProviderForIdentifier:"
+ "decontainerizedPathString:"
+ "dictionaryWithContentsOfURL:error:"
+ "new messages number: [%!l(MISSING)u] new participant changes number: [%!l(MISSING)u] lastAlertedDate: [%!l(MISSING)ld]-[%!@(MISSING)] lastFailedMessageAlertDate: [%!l(MISSING)ld]-[%!@(MISSING)] lastFailedMessageDate: [%!l(MISSING)ld]-[%!@(MISSING)]"
+ "organizationNameTitle"
+ "otherHandleRecord"
+ "plist"
+ "typeIdentifier"
+ "useThreadOriginator = %!d(MISSING), messageGUID = %!@(MISSING), onlyMessageItems= %!d(MISSING), onlyUnread= %!d(MISSING), limit= %!l(MISSING)ld, Query: %!@(MISSING)"
- "%!@(MISSING) was a failed message identifier, don't remove all delivered notifications"
- "Cleansing browser snapshot cache"
- "Cleansing orphaned sticker attachments"
- "Cleansing orphaned sticker transfer user info"
- "Deleting previews older than last 200"
- "Failed to deserialize contact for message %!@(MISSING), error %!@(MISSING)"
- "Finished previews older than last 200"
- "Retracting of all delivered notifications, as we had nothing unread"
- "SELECT   message_id FROM chat_message_join WHERE message_id in (SELECT rowid FROM message INDEXED BY message_idx_isRead_isFromMe_itemType  WHERE (is_read == 0     AND is_finished == 1     AND is_from_me == 0     AND item_type == 0     AND is_system_message == 0     %!s(MISSING) )) AND chat_id %!@(MISSING)"
- "SELECT count(rowid) FROM Attachment WHERE filename LIKE ?;"
- "We had nothing unread, inspecting the posted notifications"
- "_previewFileURLForTransferURL:utiType:knownSender:"
- "caseInsensitiveCompare:"
- "decontainerizePathString:"
- "getAttachmentPathsFromMessageRecord:"
- "new messages number: [%!l(MISSING)u] lastAlertedDate: [%!l(MISSING)ld]-[%!@(MISSING)] lastFailedMessageAlertDate: [%!l(MISSING)ld]-[%!@(MISSING)] lastFailedMessageDate: [%!l(MISSING)ld]-[%!@(MISSING)]"
- "public.vlocation"
- "removeAllDeliveredNotifications"
- "v32@?0@\"UNNotification\"8Q16^B24"

```
