## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.500.178.2.5
-  __TEXT.__text: 0x247abc
+1450.500.206.0.0
+  __TEXT.__text: 0x24a9a8
   __TEXT.__auth_stubs: 0x4a00
-  __TEXT.__objc_methlist: 0x7c64
-  __TEXT.__const: 0xc658
-  __TEXT.__cstring: 0x4857d
-  __TEXT.__oslogstring: 0x1e166
-  __TEXT.__gcc_except_tab: 0xb664
+  __TEXT.__objc_methlist: 0x7c84
+  __TEXT.__const: 0xc6a8
+  __TEXT.__cstring: 0x4881d
+  __TEXT.__oslogstring: 0x1e2d6
+  __TEXT.__gcc_except_tab: 0xb670
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
   __TEXT.__constg_swiftt: 0x556c
-  __TEXT.__swift5_typeref: 0x3b8c
+  __TEXT.__swift5_typeref: 0x3c40
   __TEXT.__swift5_builtin: 0x294
-  __TEXT.__swift5_reflstr: 0x3074
-  __TEXT.__swift5_fieldmd: 0x331c
+  __TEXT.__swift5_reflstr: 0x3084
+  __TEXT.__swift5_fieldmd: 0x3328
   __TEXT.__swift5_assocty: 0x6c8
   __TEXT.__swift5_capture: 0x12a8
   __TEXT.__swift5_proto: 0x770

   __TEXT.__swift_as_entry: 0xb4
   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9178
-  __TEXT.__eh_frame: 0x83d8
+  __TEXT.__unwind_info: 0x91b8
+  __TEXT.__eh_frame: 0x8430
   __TEXT.__objc_classname: 0x279b
-  __TEXT.__objc_methname: 0x1b497
-  __TEXT.__objc_methtype: 0x44fc
-  __TEXT.__objc_stubs: 0x13960
-  __DATA_CONST.__got: 0x17d8
+  __TEXT.__objc_methname: 0x1b4f7
+  __TEXT.__objc_methtype: 0x450c
+  __TEXT.__objc_stubs: 0x139c0
+  __DATA_CONST.__got: 0x17e0
   __DATA_CONST.__const: 0x81f0
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56f0
+  __DATA_CONST.__objc_selrefs: 0x5708
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x2510
-  __AUTH_CONST.__const: 0xac30
-  __AUTH_CONST.__cfstring: 0x12520
+  __AUTH_CONST.__const: 0xaca8
+  __AUTH_CONST.__cfstring: 0x12540
   __AUTH_CONST.__objc_const: 0x10fc0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH.__objc_data: 0x2158
   __AUTH.__data: 0x47c0
   __DATA.__objc_ivar: 0x4c0
-  __DATA.__data: 0x3110
-  __DATA.__bss: 0xb3c0
+  __DATA.__data: 0x3130
+  __DATA.__bss: 0xb3d0
   __DATA.__common: 0x228
   __DATA_DIRTY.__objc_data: 0x1738
   __DATA_DIRTY.__data: 0x4150

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2FD34217-5FF1-31B5-A98B-8CFE80823BAC
-  Functions: 11371
-  Symbols:   2642
-  CStrings:  12730
+  UUID: A696F1BF-0ACA-3926-BAE2-68BB4806E777
+  Functions: 11393
+  Symbols:   2643
+  CStrings:  12743
 
Symbols:
+ _IMMessageSummaryInfoContainsWarnState
CStrings:
+ " AND NOT EXISTS (     SELECT 1 FROM message m     WHERE m.ROWID = cmj.message_id     AND m.balloon_bundle_id IN ('com.apple.DigitalTouchBalloonProvider', 'com.apple.Handwriting.HandwritingProvider') ) ORDER BY cmj.message_id "
+ " LIKE ?\nORDER BY "
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/IMDCNPersonAliasResolver.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/IMDMessageQueries.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/IMDPersistenceTests/IMDSqlQuery.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMAbstractDatabaseArchiver.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFAttachmentRecord.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFChatRecord.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFHandleRecord.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFMessageRecord.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDDatabaseMigration.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDIndexes.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDMessageStore_PersistenceUtilities.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDNotificationsController.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperation.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperationCoreSDB.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperationUtilities.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlStatement.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqliteUtilities.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDTables.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDTriggers.m"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDAttachmentRecordExporter.swift"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDChatRecordExporter.swift"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDMessageRecordExporter.swift"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDParticipantExporter.swift"
+ "/Library/Caches/com.apple.xbs/1A61886C-2F21-41AF-B6CD-8F1CED0C9479/TemporaryDirectory.DESwtF/Sources/MessagesCore/IMCore/IMDPersistence/Source/Indexing/Spotlight/IMDCoreSpotlightIndexHelpers.m"
+ "AND cmj.chat_id IN ("
+ "B24@0:8q16"
+ "Donating TrustKit warn state to Spotlight for Time Sensitivity"
+ "Failed to check siblings for chat ROWID %lld: %@"
+ "Failed to check siblings for participant ROWID %lld: %@"
+ "SELECT COUNT(a.ROWID), SUM(total_bytes) FROM attachment a WHERE EXISTS (     SELECT 1 FROM message_attachment_join maj     INNER JOIN message m ON maj.message_id = m.ROWID     WHERE maj.attachment_id = a.ROWID     AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.URLBalloonProvider') );"
+ "SELECT DISTINCT c.ROWID, c.chat_identifier\nFROM chat c\nINNER JOIN chat_message_join cmj ON c.ROWID = cmj.chat_id\nWHERE c.ROWID > ?\nORDER BY c.ROWID "
+ "SELECT ROWID\nFROM chat\nWHERE chat_identifier = ? OR chat_identifier LIKE ?\nORDER BY ROWID ASC;"
+ "SELECT a.ROWID FROM attachment a WHERE a.ROWID > ? AND EXISTS (     SELECT 1 FROM message_attachment_join maj     INNER JOIN message m ON maj.message_id = m.ROWID     WHERE maj.attachment_id = a.ROWID     AND (m.balloon_bundle_id IS NULL OR m.balloon_bundle_id != 'com.apple.messages.URLBalloonProvider') ) ORDER BY a.ROWID "
+ "SELECT cmj.message_id FROM chat_message_join cmj WHERE cmj.message_id > ? "
+ "Skipping chat ROWID %lld with identifier '%s' - already processed with siblings"
+ "Skipping participant ROWID %lld with address '%s' - already processed with siblings"
+ "__imdp_isEntitledForMessageType:"
+ "_trustKitWarnStateCustomKey"
+ "com_apple_mobilesms_trustkit_warn_state"
+ "connection:isEntitledForMessageType:"
- ") ORDER BY cmj.message_id "
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/IMDCNPersonAliasResolver.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/IMDMessageQueries.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/IMDPersistenceTests/IMDSqlQuery.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMAbstractDatabaseArchiver.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFAttachmentRecord.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFChatRecord.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFHandleRecord.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDCFMessageRecord.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDDatabaseMigration.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDIndexes.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDMessageStore_PersistenceUtilities.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDNotificationsController.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperation.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperationCoreSDB.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlOperationUtilities.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqlStatement.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDSqliteUtilities.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDTables.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/IMDTriggers.m"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDAttachmentRecordExporter.swift"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDChatRecordExporter.swift"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDMessageRecordExporter.swift"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/ImportExport/Exporting/Exporters/IMDParticipantExporter.swift"
- "/Library/Caches/com.apple.xbs/C59F1F7E-B63D-4392-8655-00BC45C2C68C/TemporaryDirectory.NA0Fpt/Sources/MessagesCore/IMCore/IMDPersistence/Source/Indexing/Spotlight/IMDCoreSpotlightIndexHelpers.m"
- "SELECT COUNT(DISTINCT a.ROWID), SUM(total_bytes) FROM attachment a INNER JOIN message_attachment_join maj ON a.ROWID = maj.attachment_id;"
- "SELECT DISTINCT a.ROWID FROM attachment a INNER JOIN message_attachment_join maj ON a.ROWID = maj.attachment_id WHERE a.ROWID > ? ORDER BY a.ROWID "
- "SELECT DISTINCT c.ROWID FROM chat c INNER JOIN chat_message_join cmj ON c.ROWID = cmj.chat_id WHERE c.ROWID > ? ORDER BY c.ROWID "
- "SELECT message_id FROM chat_message_join WHERE message_id > ? ORDER BY message_id "
- "SELECT message_id FROM chat_message_join cmj WHERE cmj.message_id > ? AND cmj.chat_id IN ("

```
