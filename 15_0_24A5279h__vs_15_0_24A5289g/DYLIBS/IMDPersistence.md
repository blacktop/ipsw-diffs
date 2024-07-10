## IMDPersistence

> `/System/iOSSupport/System/Library/PrivateFrameworks/IMDPersistence.framework/Versions/A/IMDPersistence`

```diff

-1297.100.12.1.2
-  __TEXT.__text: 0x10e100
+1299.100.9.0.0
+  __TEXT.__text: 0x10ec84
   __TEXT.__auth_stubs: 0x2620
   __TEXT.__objc_methlist: 0x359c
   __TEXT.__const: 0xb3a
-  __TEXT.__cstring: 0x37aa1
-  __TEXT.__oslogstring: 0x192f5
-  __TEXT.__gcc_except_tab: 0xcbbc
+  __TEXT.__cstring: 0x37a61
+  __TEXT.__oslogstring: 0x19315
+  __TEXT.__gcc_except_tab: 0xcc7c
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x166
   __TEXT.__swift5_typeref: 0x206

   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_reflstr: 0x6f
-  __TEXT.__unwind_info: 0x4a40
+  __TEXT.__unwind_info: 0x4a88
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0xa48
-  __TEXT.__objc_methname: 0xf868
-  __TEXT.__objc_methtype: 0x23d9
-  __TEXT.__objc_stubs: 0xca00
-  __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x10b60
+  __TEXT.__objc_methname: 0xf8d2
+  __TEXT.__objc_methtype: 0x23cb
+  __TEXT.__objc_stubs: 0xcb20
+  __DATA_CONST.__got: 0xe00
+  __DATA_CONST.__const: 0x10b40
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3728
+  __DATA_CONST.__objc_selrefs: 0x3760
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0x1320
   __AUTH_CONST.__auth_ptr: 0x90
   __AUTH_CONST.__const: 0x1a28
-  __AUTH_CONST.__cfstring: 0x107c0
+  __AUTH_CONST.__cfstring: 0x107e0
   __AUTH_CONST.__objc_const: 0x66e0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4353
-  Symbols:   2285
-  CStrings:  2980
+  Functions: 4365
+  Symbols:   2292
+  CStrings:  2981
 
Symbols:
+ _IMCMMAssetIndexFromIMFileTransferGUID
+ _IMChatPropertyLastAddressedLocalHandle
+ _IMChatPropertyLastAddressedSIMID
+ _IMChatPropertyProperties
+ _IMDChatRecordRowIDsWithChatGUIDsQuery
+ _IMDDeleteFromChatMessageJoinWhereMessageInRecoveryForChatsWithGUIDsQuery
+ _IMDInsertMessagesFromChatsWihGUIDsIntoRecoverableMessageJoinQuery
+ _IMFileTransferGUIDForAttachmentMessagePartAtMessageGUIDAndMessagePartIndex
+ _IMFileTransferGUIDIsTemporary
+ _OBJC_CLASS_$_IMDiagnosticNotification
+ _OBJC_CLASS_$_IMDiagnosticNotifier
+ ___XPCServerIMDChatRecordCopyChatRecordForIdentifier_IPCAction
+ ___syncXPCIMDChatRecordCopyChatRecordForIdentifier_IPCAction
- _IMAttachmentIndexFromIMFileTransferGuid
- _IMFileTransferGuidIsLegacyGuid
- _IMFileTransferGuidWithAssociatedMessageGUIDAndIndex
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationAlertTopMostKey
CStrings:
+ "(nil)"
+ ") AND message_id IN (SELECT message_id FROM chat_recoverable_message_join WHERE chat_id IN ("
+ ");"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Binaries/MessagesCore_iosmac/install/Symbols/BuiltProducts/IMDPersistence.framework/PrivateHeaders/IMDUtils.h"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDCNPersonAliasResolver.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDMessageQueries.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDPersistenceTests/IMDSqlQuery.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMAbstractDatabaseArchiver.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFAttachmentRecord.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFChatRecord.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFHandleRecord.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFMessageRecord.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCoreSpotlightIndexHelpers.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDDatabaseMigration.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDIndexes.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDMessageStore_PersistenceUtilities.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDNotificationsController.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperation.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperationCoreSDB.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperationUtilities.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlStatement.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqliteUtilities.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDTables.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDTriggers.m"
+ "DELETE FROM chat_message_join WHERE chat_id IN ("
+ "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT chat_id, message_id, message_date FROM chat_message_join WHERE message_date < ? AND chat_id IN ("
+ "Messages Indexing %!@(MISSING)"
+ "Query: Copy Chat Record for Identifier"
+ "SELECT rowid FROM chat WHERE guid IN ("
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/MessagesCore_iosmac/install/Symbols/BuiltProducts/IMDPersistence.framework/PrivateHeaders/IMDUtils.h"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDCNPersonAliasResolver.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDMessageQueries.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/IMDPersistenceTests/IMDSqlQuery.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMAbstractDatabaseArchiver.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFAttachmentRecord.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFChatRecord.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFHandleRecord.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCFMessageRecord.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDCoreSpotlightIndexHelpers.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDDatabaseMigration.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDIndexes.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDMessageStore_PersistenceUtilities.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDNotificationsController.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperation.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperationCoreSDB.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlOperationUtilities.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqlStatement.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDSqliteUtilities.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDTables.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/MessagesCore_iosmac/IMCore/IMDPersistence/Source/IMDTriggers.m"
- "DELETE FROM chat_message_join WHERE chat_id = ? AND message_id IN ( SELECT message_id FROM chat_recoverable_message_join WHERE chat_id = ?);"
- "INSERT OR REPLACE INTO chat_recoverable_message_join (chat_id, message_id, delete_date) SELECT cmj.chat_id, cmj.message_id, ? FROM chat_message_join AS cmj JOIN chat ON cmj.chat_id = chat.ROWID AND chat.guid = ? AND cmj.message_date < ?;"
- "SBUserNotificationDontDismissOnUnlock"
- "SBUserNotificationExtensionIdentifierKey"
- "[Internal] Messages Spotlight Indexing %!@(MISSING)"
- "amr"
- "caf"

```
