## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.600.22.2.1
-  __TEXT.__text: 0x11e6c0
+1402.600.31.0.0
+  __TEXT.__text: 0x11e394
   __TEXT.__auth_stubs: 0x2800
   __TEXT.__objc_methlist: 0x423c
-  __TEXT.__const: 0xb80
-  __TEXT.__cstring: 0x39c31
-  __TEXT.__oslogstring: 0x1a405
-  __TEXT.__gcc_except_tab: 0xe68c
+  __TEXT.__const: 0xb70
+  __TEXT.__cstring: 0x39ac1
+  __TEXT.__oslogstring: 0x1a205
+  __TEXT.__gcc_except_tab: 0xe5d4
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x2a4
   __TEXT.__swift5_typeref: 0x1fc

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4ea8
+  __TEXT.__unwind_info: 0x4eb8
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0xb5b
-  __TEXT.__objc_methname: 0x10c22
+  __TEXT.__objc_methname: 0x10c37
   __TEXT.__objc_methtype: 0x24b8
-  __TEXT.__objc_stubs: 0xdfe0
-  __DATA_CONST.__got: 0xf28
-  __DATA_CONST.__const: 0x110a0
+  __TEXT.__objc_stubs: 0xe000
+  __DATA_CONST.__got: 0xf00
+  __DATA_CONST.__const: 0x11110
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3dc0
+  __DATA_CONST.__objc_selrefs: 0x3dc8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0x190
+  __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x1410
   __AUTH_CONST.__auth_ptr: 0xa0
   __AUTH_CONST.__const: 0x1ad0
-  __AUTH_CONST.__cfstring: 0x114c0
+  __AUTH_CONST.__cfstring: 0x11560
   __AUTH_CONST.__objc_const: 0x6028
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x4e8
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x190

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4667
-  Symbols:   2378
-  CStrings:  7570
+  Functions: 4668
+  Symbols:   2372
+  CStrings:  7572
 
Symbols:
+ _IMDMessageRecordCalculateLocalCloudKitStatisticsAsync
+ _OBJC_CLASS_$_NSConstantDictionary
- _IMDMessageRecordCalculateTotalCounts
- _IMDMessageRecordCloudKitStatisticUnresolvedAttachmentCountKey
- _IMDMessageRecordCloudKitStatisticUnresolvedChatCountKey
- _IMDMessageRecordCloudKitStatisticUnresolvedCountKey
- _IMDMessageRecordCloudKitStatisticUnresolvedMessageCountKey
- _IMDMessageRecordCloudKitStatisticUnresolvedRecoverableMessageCountKey
- ___XPCServerIMDMessageRecordCalculateTotalCounts_IPCAction
- ___syncXPCIMDMessageRecordCalculateTotalCounts_IPCAction
CStrings:
+ "Calculated sync stats in %f seconds. All Records: %lld of %lld, %lld remaining. All Stats: %@"
+ "att"
+ "delAtt"
+ "delChat"
+ "delMsg"
+ "delRecovMsg"
+ "recovMsg"
+ "removeObjectAtIndex:"
+ "updT1"
+ "updT2"
- "Calculated sync stats in %f seconds. All Records: %lld of %lld, %lld remaining, %lld unresolved. Messages : %lld of %lld, %lld remaining, %lld unresolved. Chats : %lld of %lld, %lld remaining, %lld unresolved. Attachments : %lld of %lld, %lld remaining, %lld unresolved."
- "Calculated total counts in %f seconds. All Records: %lld, Messages: %lld, Chats: %lld, Attachments: %lld, RecoverableMessages: %lld"
- "Expected dictionary of record totals is nil"
- "Expecting statistics dictionary to calculate unresolved counts, but found nil, returning 0"
- "IMDMessageRecordCalculateTotalCounts loaded totals: %@"
- "SELECT COUNT(*) FROM attachment;"
- "SELECT COUNT(*) FROM chat;"
- "SELECT SUM(total_count) AS total_count FROM ( SELECT COUNT(*) AS total_count FROM chat_recoverable_message_join AS crmj JOIN chat AS c ON c.ROWID = crmj.chat_id JOIN message AS m ON m.ROWID = crmj.message_id UNION ALL SELECT COUNT(1) AS total_count FROM recoverable_message_part AS rmp JOIN chat AS c ON c.ROWID = rmp.chat_id JOIN message AS m ON m.ROWID = rmp.message_id);"

```
