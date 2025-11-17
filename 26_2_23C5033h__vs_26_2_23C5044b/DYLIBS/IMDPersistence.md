## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.300.27.0.0
-  __TEXT.__text: 0x22cc04
-  __TEXT.__auth_stubs: 0x46b0
-  __TEXT.__objc_methlist: 0x72b4
-  __TEXT.__const: 0xaed8
-  __TEXT.__cstring: 0x4824b
-  __TEXT.__oslogstring: 0x1dae1
-  __TEXT.__gcc_except_tab: 0xd0d4
+1450.300.41.2.7
+  __TEXT.__text: 0x232b78
+  __TEXT.__auth_stubs: 0x46d0
+  __TEXT.__objc_methlist: 0x73b4
+  __TEXT.__const: 0xb648
+  __TEXT.__cstring: 0x4873b
+  __TEXT.__oslogstring: 0x1e0c6
+  __TEXT.__gcc_except_tab: 0xd0e4
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x360
-  __TEXT.__constg_swiftt: 0x4ddc
-  __TEXT.__swift5_typeref: 0x339c
-  __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x2b31
-  __TEXT.__swift5_fieldmd: 0x2dd4
-  __TEXT.__swift5_assocty: 0x530
-  __TEXT.__swift5_proto: 0x668
-  __TEXT.__swift5_types: 0x328
-  __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0x1074
+  __TEXT.__constg_swiftt: 0x4ec4
+  __TEXT.__swift5_typeref: 0x359e
+  __TEXT.__swift5_builtin: 0x258
+  __TEXT.__swift5_reflstr: 0x2b94
+  __TEXT.__swift5_fieldmd: 0x2ebc
+  __TEXT.__swift5_assocty: 0x548
+  __TEXT.__swift5_capture: 0x10e8
+  __TEXT.__swift5_proto: 0x6d0
+  __TEXT.__swift5_types: 0x340
+  __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x68
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x89a0
-  __TEXT.__eh_frame: 0x71d0
-  __TEXT.__objc_classname: 0x11ce
-  __TEXT.__objc_methname: 0x17b47
-  __TEXT.__objc_methtype: 0x37a1
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__unwind_info: 0x8b30
+  __TEXT.__eh_frame: 0x7348
+  __TEXT.__objc_classname: 0x11e5
+  __TEXT.__objc_methname: 0x17c76
+  __TEXT.__objc_methtype: 0x381d
   __TEXT.__objc_stubs: 0x11c60
-  __DATA_CONST.__got: 0x1760
-  __DATA_CONST.__const: 0x8450
-  __DATA_CONST.__objc_classlist: 0x610
+  __DATA_CONST.__got: 0x1770
+  __DATA_CONST.__const: 0x8470
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x238
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52a0
-  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_selrefs: 0x52e0
+  __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x2368
-  __AUTH_CONST.__const: 0x9b90
+  __AUTH_CONST.__auth_got: 0x2378
+  __AUTH_CONST.__const: 0xa010
   __AUTH_CONST.__cfstring: 0x12200
-  __AUTH_CONST.__objc_const: 0xf5d8
+  __AUTH_CONST.__objc_const: 0xf738
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1ca0
-  __AUTH.__data: 0x40b0
+  __AUTH.__objc_data: 0x1d10
+  __AUTH.__data: 0x40f0
   __DATA.__objc_ivar: 0x488
-  __DATA.__data: 0x2ea0
-  __DATA.__bss: 0xa060
-  __DATA.__common: 0x180
+  __DATA.__data: 0x2ff8
+  __DATA.__bss: 0xac60
+  __DATA.__common: 0x198
   __DATA_DIRTY.__objc_data: 0x1620
-  __DATA_DIRTY.__data: 0x3d40
+  __DATA_DIRTY.__data: 0x3d30
   __DATA_DIRTY.__bss: 0x1ee8
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B9F30FD0-4D7D-39D1-AA24-D77655B5DF7B
-  Functions: 10663
-  Symbols:   2577
-  CStrings:  12358
+  UUID: D8E73ECA-6372-3CCF-8D24-238161334BFE
+  Functions: 10814
+  Symbols:   2580
+  CStrings:  12406
 
Symbols:
+ _IMMessagePropertyAssociatedMessageEmoji
+ _OBJC_CLASS_$_IMDImportPlaceholderReplacementPair
+ _OBJC_METACLASS_$_IMDImportPlaceholderReplacementPair
CStrings:
+ "\n    UNION\n    SELECT message_id FROM recoverable_message_part WHERE message_id IN "
+ "    UPDATE OR IGNORE message SET handle_id =         (SELECT ROWID from handle where id ==  ?  AND service ==  ? )     WHERE\n        (SELECT ROWID from handle where id ==  ?  AND service ==  ? )     ;"
+ "', replacement: '"
+ "All Migrations completed successfully"
+ "AssociateMessageWithGUIDToAttachmentWithGUID failed: attachment for guid: %@ is nil"
+ "AssociateMessageWithGUIDToAttachmentWithGUID failed: message for guid: %@ is nil"
+ "BEGIN TRANSACTION;"
+ "Beginning %ld import placeholder migrations for the 'chat' table..."
+ "Beginning %ld import placeholder migrations for the 'message' table..."
+ "Beginning import placeholder migrations for:\n    chat pairs: %s\n message pairs: %s"
+ "Finished %ld of %ld import placeholder migrations for the 'chat' table."
+ "IMDImportExportQueries"
+ "IMDPersistence.IMDImportPlaceholderReplacementPair"
+ "ImportExport"
+ "ImportExport.ImportAccountPlaceholderMigrator"
+ "Migration failed with error: %@"
+ "Not creating searchable item for sensitive attachment. attachmentGUID: %@ messageGUID: %@"
+ "Performing 1 migration step to migrate '%s' to '%s' in the 'chat' table (%ld of %ld migrations)..."
+ "Performing 2 migration steps to migrate '%s' to '%s' in the 'message' table (%ld of %ld migrations)..."
+ "SELECT COUNT(*) FROM (\n    SELECT 1 FROM chat c\n    INNER JOIN chat_message_join cm ON c.rowid = cm.chat_id\n    WHERE c.guid =  ? \n    LIMIT  ? \n);"
+ "SELECT DISTINCT message_id FROM (\n    SELECT message_id FROM chat_recoverable_message_join WHERE message_id IN "
+ "SELECT m.guid FROM chat c\nINNER JOIN chat_message_join cm ON c.rowid = cm.chat_id\nINNER JOIN message m ON cm.message_id = m.rowid\nWHERE c.guid =  ? ;"
+ "SStep 1 of 1: migrating all of the 'chat' table's 'account_id' columns from '%s' to '%s' failed with error: %@..."
+ "Step 1 of 1: migrating all of the 'chat' table's 'account_id' columns from '%s' to '%s'..."
+ "Step 1 of 2: migrating all 'message' table 'account' columns from '%s' to '%s'..."
+ "Step 2 of 2: Migrating all 'message' table 'handle_id' columns from ROWID for '%s' to ROWID for '%s..."
+ "Step 2 of 2: migrating 'message; table 'handle_id; rowIDs for '%s' to '%s' failed with error: %@..."
+ "Successfully migrated:\n    chat pairs: %s\n message pairs: %s"
+ "Tq,N,R"
+ "UPDATE OR IGNORE chat SET account_id =  ?  WHERE account_id ==  ? ;"
+ "UPDATE OR IGNORE message SET account =  ?  WHERE account ==  ? ;"
+ "fetchDeletedMessageRowIDs:completionHandler:"
+ "fetchMessageGUIDsForChatWithGUID:chatMessageLimit:completionHandler:"
+ "handleCreationFailed"
+ "handleRowIDLookupFailed"
+ "initWithPlaceholder:replacement:"
+ "performImportedAccountMigrationsWithChatReplacementPairs:messageReplacementPairs:completionHandler:"
+ "placeholder"
+ "replacement"
+ "serviceNameError"
+ "setPlaceholder:"
+ "setReplacement:"
+ "unable to extract serviceName from placeholder: "
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSArray\"@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSArray\"@\"NSError\">32"

```
