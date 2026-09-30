## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1448.100.1.2.101
-  __TEXT.__text: 0x2237d0
-  __TEXT.__auth_stubs: 0x44e0
-  __TEXT.__objc_methlist: 0x7064
-  __TEXT.__const: 0xa1c8
-  __TEXT.__cstring: 0x478eb
-  __TEXT.__oslogstring: 0x1d6b6
-  __TEXT.__gcc_except_tab: 0xf848
+1450.200.35.2.5
+  __TEXT.__text: 0x224d90
+  __TEXT.__auth_stubs: 0x4500
+  __TEXT.__objc_methlist: 0x7074
+  __TEXT.__const: 0xa1e8
+  __TEXT.__cstring: 0x47aeb
+  __TEXT.__oslogstring: 0x1d7a6
+  __TEXT.__gcc_except_tab: 0xf898
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
   __TEXT.__constg_swiftt: 0x4ccc
-  __TEXT.__swift5_typeref: 0x3220
+  __TEXT.__swift5_typeref: 0x322c
   __TEXT.__swift5_builtin: 0x244
   __TEXT.__swift5_reflstr: 0x2ac1
   __TEXT.__swift5_fieldmd: 0x2d50

   __TEXT.__swift5_proto: 0x664
   __TEXT.__swift5_types: 0x31c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0xf24
+  __TEXT.__swift5_capture: 0xf50
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8c68
+  __TEXT.__unwind_info: 0x8c88
   __TEXT.__eh_frame: 0x6de8
   __TEXT.__objc_classname: 0x11ad
-  __TEXT.__objc_methname: 0x17582
-  __TEXT.__objc_methtype: 0x36a0
+  __TEXT.__objc_methname: 0x175bf
+  __TEXT.__objc_methtype: 0x36e2
   __TEXT.__objc_stubs: 0x11940
-  __DATA_CONST.__got: 0x16f0
+  __DATA_CONST.__got: 0x16f8
   __DATA_CONST.__const: 0x8358
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x2280
-  __AUTH_CONST.__const: 0x96b8
-  __AUTH_CONST.__cfstring: 0x11ee0
-  __AUTH_CONST.__objc_const: 0xf260
+  __AUTH_CONST.__auth_got: 0x2290
+  __AUTH_CONST.__const: 0x9748
+  __AUTH_CONST.__cfstring: 0x11ea0
+  __AUTH_CONST.__objc_const: 0xf278
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AE420F1F-9455-3050-8657-0F66C22F78F5
-  Functions: 10457
-  Symbols:   2554
-  CStrings:  12217
+  UUID: 2363C775-BE46-399F-B3DB-51282511AB84
+  Functions: 10479
+  Symbols:   2557
+  CStrings:  12224
 
Symbols:
+ _IMBalloonBundleIdentifierPolls
+ _IMDatabaseLogHandle
+ _IMOffloadingLogHandle
CStrings:
+ "\nFROM chat c\nJOIN chat_message_join cmj ON\n  cmj.chat_id == c.rowid\nWHERE\n  c.is_archived = 0 AND c.is_filtered = ?\nGROUP BY\n  c.rowid\nORDER BY\n  MAX(cmj.message_date) DESC\nLIMIT ?;"
+ "\nGROUP BY +cm.chat_id;"
+ " AND c.display_name =  ?  "
+ " AND c.style =  ? "
+ "@40@0:8@16Q24@32"
+ "AND (\n    SELECT COUNT(handle_id) FROM chat_handle_join\n    WHERE chat_id = c.ROWID\n) =  ? "
+ "Can mark rowID: %lld file: [%@], cloudKitSyncState: [%lld], is_sticker: [%{BOOL}d], hide_attachment: [%{BOOL}d], isPluginPayload: [%{BOOL}d], bundleID: [%@], purgeable: [%{BOOL}d]"
+ "Finished legacy command %lli async %{bool}d"
+ "Found %lld recent subclassified chats for filter mode %lld having action: %lld and subaction: %lld"
+ "Handled message %ld from (%d) wantsReply %{BOOL}d"
+ "Handling message %ld from (%d) wantsReply %{BOOL}d"
+ "Link metadata summary was nil, using payload text as text content."
+ "NOTIFICATION_PARTICIPANT_CHANGE_SCHEDULED_MESSAGE_PLURAL"
+ "NOTIFICATION_PARTICIPANT_CHANGE_SCHEDULED_MESSAGE_SINGULAR"
+ "SELECT\n    ROWID, guid, flag_group, flag, flag_priority, lane, reason, reason_priority, user_info, retry_count\nFROM persistent_tasks\nINDEXED BY persistent_tasks_exec_sort\nWHERE"
+ "SELECT c.guid FROM chat c\nWHERE ( c.ROWID IN ("
+ "SELECT chat_id FROM chat_handle_join\nWHERE handle_id IN (\n    SELECT ROWID FROM handle\n    WHERE id IN "
+ "Sending legacy command %lli async %{bool}d"
+ "canMarkPurgeableWithCKSyncState:transferState:isAudio:isSticker:isGroupPhoto:isPluginPayload:isRichLink:"
+ "copyAllRecentChatsWithLimitQuery"
+ "copyChatsWithGroupedHandles:style:displayName:completionHandler:"
+ "flag_group =  ? "
+ "im_isPluginPayloadExtension"
+ "initWithGUIDForSpotlight:flag:context:"
+ "persistent_tasks(lane DESC, flag_group ASC, flag_priority DESC, reason_priority DESC, retry_count ASC, ROWID ASC)"
+ "retry_count < 5 "
+ "v48@0:8@\"NSArray\"16q24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16q24@32@?40"
- "\nGROUP BY +cm.chat_id"
- " AND\n    retry_count < 5\nLIMIT "
- "%@ added %@ to the conversation. %lu scheduled messages"
- "@40@0:8@16Q24q32"
- "@48@0:8@16Q24q32@40"
- "Can mark rowID: %lld file: [%@], cloudKitSyncState: [%lld], is_sticker: [%@], hide_attachment: [%@], purgeable: [%@]"
- "Finished legacy command %@ async %{bool}d"
- "Handled message %ld/%@ from (%d: %@) wantsReply %@"
- "Handling message %ld/%@ from (%d: %@) wantsReply %@"
- "Offloading"
- "SELECT\n    ROWID, guid, flag_group, flag, flag_priority, lane, reason, reason_priority, user_info, retry_count\nFROM persistent_tasks\nWHERE\n    "
- "SELECT ROWID from message m WHERE m.item_type == 0 AND m.ROWID in (SELECT message_id FROM chat_message_join where chat_id = ?) ORDER BY date DESC, ROWID DESC LIMIT 1"
- "Sending legacy command %@ async %{bool}d"
- "canMarkPurgeableWithCKSyncState:transferState:isAudio:isSticker:isGroupPhoto:"
- "initWithGUID:flag:spotlightReason:"
- "initWithGUID:flag:spotlightReason:userInfo:"
- "isSOSAlertingEnabled"
- "isScheduledMessagesCoreEnabled"
- "persistent_tasks(lane DESC, flag_priority DESC, reason_priority DESC, retry_count ASC, ROWID ASC)"
- "pluginpayload"
- "pluginpayloadattachment"

```
