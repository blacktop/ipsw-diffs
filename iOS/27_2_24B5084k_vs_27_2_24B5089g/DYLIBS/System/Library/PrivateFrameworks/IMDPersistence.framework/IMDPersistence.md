## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1491.200.63.2.1
-  __TEXT.__text: 0x2f1f54
-  __TEXT.__objc_methlist: 0xa48c
+1491.200.73.0.0
+  __TEXT.__text: 0x2f28b4
+  __TEXT.__objc_methlist: 0xa49c
   __TEXT.__const: 0xc3d0
-  __TEXT.__cstring: 0x5d9d4
-  __TEXT.__oslogstring: 0x3c174
-  __TEXT.__gcc_except_tab: 0xc710
+  __TEXT.__cstring: 0x5db34
+  __TEXT.__oslogstring: 0x3c3c4
+  __TEXT.__gcc_except_tab: 0xc764
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
   __TEXT.__swift5_typeref: 0x5256

   __TEXT.__swift_as_cont: 0x398
   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xd5e0
+  __TEXT.__unwind_info: 0xd5f8
   __TEXT.__eh_frame: 0x9d24
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6500
+  __DATA_CONST.__const: 0x6528
   __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b68
+  __DATA_CONST.__objc_selrefs: 0x6b70
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__got: 0x1c30
-  __AUTH_CONST.__const: 0xe248
-  __AUTH_CONST.__cfstring: 0x130c0
+  __AUTH_CONST.__const: 0xe268
+  __AUTH_CONST.__cfstring: 0x131c0
   __AUTH_CONST.__objc_const: 0x13b20
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x29f8
-  __AUTH.__objc_data: 0x1038
-  __AUTH.__data: 0x1df8
+  __AUTH.__objc_data: 0xfc0
+  __AUTH.__data: 0x1cb0
   __DATA.__objc_ivar: 0x568
-  __DATA.__data: 0x3b40
-  __DATA.__common: 0x288
-  __DATA_DIRTY.__objc_data: 0x3040
-  __DATA_DIRTY.__data: 0x62b0
-  __DATA_DIRTY.__bss: 0x2780
-  __DATA_DIRTY.__common: 0x100
+  __DATA.__data: 0x3a70
+  __DATA.__common: 0x270
+  __DATA_DIRTY.__objc_data: 0x30b8
+  __DATA_DIRTY.__data: 0x6500
+  __DATA_DIRTY.__bss: 0x2a00
+  __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13781
+  Functions: 13788
   Symbols:   2852
-  CStrings:  7534
+  CStrings:  7546
 
CStrings:
+ "Alert watermark dated in the future: %@"
+ "BOOL __IMDDatabasePerformOneMigration(int, CSDBSqliteDatabase *, CSDBSqliteConnection *, int, int *, NSError *__autoreleasing *, __strong MigratorBlock)"
+ "Copying %lu attachment download info entries beforeDate: %@ earliestDate: %lld limit: %lld"
+ "IMDNotificationsController.futureAlertWatermark"
+ "Last alerted failed message date was stored in the future: [%lld]-[%@], now: [%lld]-[%@]. Clamping to now, which restores alerting for failures dated before it."
+ "Last alerted message date was stored in the future: [%lld]-[%@], now: [%lld]-[%@]. Clamping to now, which restores alerting for messages dated before it."
+ "Notifications"
+ "Refusing to advance last alerted failed message date to a future date: [%lld]-[%@], now: [%lld]-[%@]. Clamping it to now instead."
+ "Refusing to advance last alerted message date to a future date: [%lld]-[%@], now: [%lld]-[%@]. Clamping it to now instead."
+ "SELECT a.ROWID, a.guid, a.total_bytes, a.ck_record_id, m.date FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 AND IFNULL(m.date, 0) >= ? ORDER BY m.date DESC, a.ROWID ASC LIMIT ? "
+ "SELECT a.ROWID, a.guid, a.total_bytes, a.ck_record_id, m.date FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 AND m.date < ? AND IFNULL(m.date, 0) >= ? ORDER BY m.date DESC, a.ROWID ASC LIMIT ? "
+ "advance-failed"
+ "advance-received"
+ "earliestDate"
+ "setupFirstLoad-failed"
+ "setupFirstLoad-received"
+ "void IMDMessageRecordAnonymizedUpdate(IMDMessageRecordRef, CFStringRef, CFDataRef, CFStringRef, CFStringRef, CFStringRef, CFDataRef, CFDataRef, CFStringRef, BOOL, BOOL, CFStringRef, CFStringRef, CFStringRef)"
+ "void _IMDPerformBlock(__strong dispatch_block_t, IMFileLocation_t *)"
+ "void _IMDPerformBlockWithDelay(NSTimeInterval, __strong dispatch_block_t, IMFileLocation_t *)"
+ "void _IMDPerformLockedConnectionBlock(__strong CSDBLockedConnection, IMFileLocation_t *)"
+ "void _IMDPerformLockedDatabaseBlock(__strong CSDBLockedDatabase, IMFileLocation_t *)"
+ "void _IMDPerformLockedMessageStoreBlock(__strong CSDBLockedRecordStore, IMFileLocation_t *)"
+ "void _IMDPerformLockedMessageStoreBlockWithoutInitialize(__strong CSDBLockedRecordStore, IMFileLocation_t *)"
+ "void _IMDPerformLockedStatementBlockWithQuery(CFStringRef, __strong CSDBLockedStatement, IMFileLocation_t *)"
- "BOOL __IMDDatabasePerformOneMigration(int, CSDBSqliteDatabase *, CSDBSqliteConnection *, int, int *, NSError **, MigratorBlock)"
- "Copying %lu attachment download info entries beforeDate: %@ limit: %lld"
- "SELECT a.ROWID, a.guid, a.total_bytes, a.ck_record_id, m.date FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 AND m.date < ? ORDER BY m.date DESC, a.ROWID ASC LIMIT ? "
- "SELECT a.ROWID, a.guid, a.total_bytes, a.ck_record_id, m.date FROM attachment a INNER JOIN message_attachment_join ma ON a.ROWID = ma.attachment_id INNER JOIN message m ON m.rowid = ma.message_id WHERE a.ck_sync_state == 1 AND a.transfer_state == 0 ORDER BY m.date DESC, a.ROWID ASC LIMIT ? "
- "void IMDMessageRecordAnonymizedUpdate(IMDMessageRecordRef, CFStringRef, CFDataRef, CFStringRef, CFStringRef, CFStringRef, CFDataRef, CFDataRef, CFStringRef, BOOL, CFStringRef, CFStringRef, CFStringRef)"
- "void _IMDPerformBlock(dispatch_block_t, IMFileLocation_t *)"
- "void _IMDPerformBlockWithDelay(NSTimeInterval, dispatch_block_t, IMFileLocation_t *)"
- "void _IMDPerformLockedConnectionBlock(CSDBLockedConnection, IMFileLocation_t *)"
- "void _IMDPerformLockedDatabaseBlock(CSDBLockedDatabase, IMFileLocation_t *)"
- "void _IMDPerformLockedMessageStoreBlock(CSDBLockedRecordStore, IMFileLocation_t *)"
- "void _IMDPerformLockedMessageStoreBlockWithoutInitialize(CSDBLockedRecordStore, IMFileLocation_t *)"
- "void _IMDPerformLockedStatementBlockWithQuery(CFStringRef, CSDBLockedStatement, IMFileLocation_t *)"
```
