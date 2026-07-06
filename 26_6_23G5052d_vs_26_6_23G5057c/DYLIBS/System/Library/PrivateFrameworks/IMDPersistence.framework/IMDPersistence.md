## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-  __TEXT.__text: 0x267aac
-  __TEXT.__auth_stubs: 0x4f60
-  __TEXT.__objc_methlist: 0x817c
+  __TEXT.__text: 0x26769c
+  __TEXT.__auth_stubs: 0x4f40
+  __TEXT.__objc_methlist: 0x8154
   __TEXT.__const: 0xc848
-  __TEXT.__cstring: 0x49244
-  __TEXT.__oslogstring: 0x1ebb6
-  __TEXT.__gcc_except_tab: 0xb7e4
+  __TEXT.__cstring: 0x49204
+  __TEXT.__oslogstring: 0x1ea96
+  __TEXT.__gcc_except_tab: 0xb834
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
   __TEXT.__swift5_typeref: 0x3f8a

   __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x9640
+  __TEXT.__unwind_info: 0x9648
   __TEXT.__eh_frame: 0x8ab0
   __TEXT.__objc_classname: 0x28fa
-  __TEXT.__objc_methname: 0x1c495
-  __TEXT.__objc_methtype: 0x4627
-  __TEXT.__objc_stubs: 0x14240
-  __DATA_CONST.__got: 0x1928
+  __TEXT.__objc_methname: 0x1c3e5
+  __TEXT.__objc_methtype: 0x4637
+  __TEXT.__objc_stubs: 0x14220
+  __DATA_CONST.__got: 0x1920
   __DATA_CONST.__const: 0x82d0
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5998
+  __DATA_CONST.__objc_selrefs: 0x5990
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__auth_got: 0x27c0
-  __AUTH_CONST.__const: 0xadc8
-  __AUTH_CONST.__cfstring: 0x12580
-  __AUTH_CONST.__objc_const: 0x11b48
+  __AUTH_CONST.__auth_got: 0x27b0
+  __AUTH_CONST.__const: 0xada8
+  __AUTH_CONST.__cfstring: 0x12540
+  __AUTH_CONST.__objc_const: 0x11b40
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 11792
   Symbols:   2667
-  CStrings:  12951
+  CStrings:  12942
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _IMDCNDisplayNameAndShortNameForHandleID
+ ___XPCServerIMDCNDisplayNameAndShortNameForHandleID_IPCAction
+ ___syncXPCIMDCNDisplayNameAndShortNameForHandleID_IPCAction
- __xpc_type_array
- _xpc_array_get_int64
- _xpc_int64_create
CStrings:
+ "Action: Get contact display name and short name for handle id"
+ "IMDCNDisplayNameAndShortNameForHandleID returning total Contact keys: %lu"
+ "INSERT INTO recoverable_message_part (chat_id, message_id, part_index, delete_date, part_text, ck_sync_state)   SELECT cmj.chat_id, cmj.message_id, ?, ?, ?, 0   FROM chat_message_join AS cmj   JOIN message AS m   ON m.ROWID = cmj.message_id AND m.guid = ?;"
+ "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT chat_id, message_id, message_date FROM chat_message_join WHERE message_date < ? AND chat_id IN ("
+ "Recently Deleted | Will begin permanently deleting recoverable messages for %lu chatGUIDs"
+ "SELECT urrm.chat_guid, urrm.message_guid, urrm.part_index FROM unsynced_removed_recoverable_messages AS urrm LIMIT ?;"
+ "_fetchContactDisplayNameAndShortNameForHandleID:"
+ "getContactDisplayNameAndShortNameForHandleID:"
+ "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:"
+ "v40@0:8@\"NSAttributedString\"16@\"NSString\"24@\"NSDate\"32"
- "DELETE FROM unsynced_removed_recoverable_messages WHERE ROWID IN"
- "INSERT INTO recoverable_message_part (chat_id, message_id, part_index, delete_date, part_text, ck_sync_state)   SELECT cmj.chat_id, cmj.message_id, ?, ?, ?, ?   FROM chat_message_join AS cmj   JOIN message AS m   ON m.ROWID = cmj.message_id AND m.guid = ?;"
- "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT chat_id, message_id, ? FROM chat_message_join WHERE message_date < ? AND chat_id IN ("
- "Overriding recently deleted expiration to %lld days based on default com.apple.Messages days-to-deleted-cleanup"
- "Recently Deleted | Failed to clear tombstones by ROWIDs: %@"
- "Recently Deleted | Finished clearing %lu specific recoverable message tombstones by ROWID"
- "Recently Deleted | Will begin clearing %lu specific recoverable message tombstones by ROWID"
- "Recently Deleted | Will begin permanently deleting recoverable messages for %lu chatGUIDs, beforeDate: %@"
- "SELECT urrm.chat_guid, urrm.message_guid, urrm.part_index, urrm.ROWID FROM unsynced_removed_recoverable_messages AS urrm LIMIT ?;"
- "clearRecoverableMessageTombStonesForRowIDs:"
- "days-to-deleted-cleanup"
- "fromSync"
- "handleIMDMessageRecordClearUnsyncedRemovedRecoverableMessagesForRowIDs_IPCActionWithXPCConnection:requestMessage:responseMessage:completionHandler:"
- "messagesAppDomain"
- "storeRecoverableMessagePartWithBody:forMessageWithGUID:deleteDate:fromSync:"
- "tombstoneRowID"
- "v44@0:8@\"NSAttributedString\"16@\"NSString\"24@\"NSDate\"32B40"

```
