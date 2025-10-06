## CalendarDatabase

> `/System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase`

```diff

-1232.2.3.0.0
-  __TEXT.__text: 0xd0318
+1232.4.4.0.0
+  __TEXT.__text: 0xd0b78
   __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__objc_methlist: 0x19a0
-  __TEXT.__cstring: 0x1c157
-  __TEXT.__const: 0x5f4
+  __TEXT.__cstring: 0x1c3a5
+  __TEXT.__const: 0x614
   __TEXT.__gcc_except_tab: 0xcf8
-  __TEXT.__oslogstring: 0xb409
+  __TEXT.__oslogstring: 0xb471
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__unwind_info: 0x2a98
+  __TEXT.__unwind_info: 0x2aa8
   __TEXT.__objc_classname: 0x567
-  __TEXT.__objc_methname: 0x8ab6
+  __TEXT.__objc_methname: 0x8aca
   __TEXT.__objc_methtype: 0x44d1
   __TEXT.__objc_stubs: 0x7e20
   __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0xd740
+  __DATA_CONST.__const: 0xdb50
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x46f8
   __DATA_CONST.__objc_selrefs: 0x22f8
+  __DATA_CONST.__objc_classrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__cfstring: 0xbda0
+  __AUTH_CONST.__cfstring: 0xbde0
   __AUTH_CONST.__const: 0x2088
   __AUTH_CONST.__objc_const: 0x1000
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0xfe0
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_classrefs: 0x3e0
-  __DATA.__objc_superrefs: 0xc8
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x768
   __DATA.__bss: 0x230

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F961DC44-80E7-3456-9D1C-AB00737DE2BD
-  Functions: 4071
-  Symbols:   9253
-  CStrings:  5975
+  UUID: 136F5AED-1910-3A35-B209-A9A66B6DA322
+  Functions: 4075
+  Symbols:   9274
+  CStrings:  5994
 
Symbols:
+ GCC_except_table94
+ __CalCalendarItemInvalidateAllRecurrenceRuleCachedEndDates
+ __CalMigrationCreateIndexes
+ __CalRecurrenceGetWeekStartRaw
+ ____buildDictionariesWithChangeTablePropertiesForEntityType_block_invoke.187
+ ___block_literal_global.232
+ _countRow
+ _kCalAlarmChangesIndexes
+ _kCalAttachmentChangesIndexes
+ _kCalAuxDatabaseChangesIndexes
+ _kCalCalendarChangesIndexes
+ _kCalContactChangesIndexes
+ _kCalContactUpgradeInfo
+ _kCalEventActionChangesIndexes
+ _kCalEventChangesIndexes
+ _kCalExceptionDateChangesIndexes
+ _kCalNotificationChangesIndexes
+ _kCalParticipantChangesIndexes
+ _kCalRecurrenceChangesIndexes
+ _kCalShareeChangesIndexes
+ _kCalStoreChangesIndexes
- GCC_except_table56
- GCC_except_table88
- GCC_except_table93
- GCC_except_table95
- ____buildDictionariesWithChangeTablePropertiesForEntityType_block_invoke.184
CStrings:
+ "AlarmChangesSequenceNumber"
+ "AttachmentChangesSequenceNumber"
+ "AuxDatabaseChangesSequenceNumber"
+ "CalendarChangesSequenceNumber"
+ "CalendarItemChangesSequenceNumber"
+ "Changes"
+ "ContactChangesSequenceNumber"
+ "Couldn't create statement for finding appropriate sequence number; using latest sequence number instead"
+ "EventActionChangesSequenceNumber"
+ "ExceptionDateChangesSequenceNumber"
+ "NotificationChangesSequenceNumber"
+ "ParticipantChangesSequenceNumber"
+ "RecurrenceChangesSequenceNumber"
+ "SELECT sequence_number FROM CalendarItemChanges WHERE sequence_number > ? AND sequence_number NOT IN (SELECT sequence_number FROM ClientSequence WHERE client_identifier = ?)"
+ "ShareeChangesSequenceNumber"
+ "StoreChangesSequenceNumber"
+ "T@\"NSString\",?,R,C"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4190"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2808"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1561"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1603"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1649"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1858"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2885"
+ "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:451"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1048"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1673"
+ "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1057"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2810"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2834"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4533"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1154"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1742"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1059"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2893"
+ "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:456"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4167"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2581"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1551"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1570"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1619"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1814"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2821"
+ "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:445"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4184"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2805"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1476"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1518"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1564"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1773"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2873"
- "commit at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:443"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1588"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:988"
- "read at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1048"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2807"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2831"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:4530"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1075"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1657"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalRecurrence.m:1050"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2881"
- "rollback at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:448"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalCalendar.m:4161"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabase.m:2578"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1466"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1485"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1534"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalDatabasePersistentChangeTracking.m:1729"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:2809"
- "write at /Library/Caches/com.apple.xbs/Sources/CalendarDatabase/CalendarDatabase/CalStore.m:437"

```
