## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1262.500.151.2.5
-  __TEXT.__text: 0xfcf4c
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_methlist: 0x2d8c
-  __TEXT.__const: 0x6aa
-  __TEXT.__cstring: 0x4a681
-  __TEXT.__oslogstring: 0x17f8d
+1262.600.61.2.9
+  __TEXT.__text: 0xfe6a0
+  __TEXT.__auth_stubs: 0x24f0
+  __TEXT.__objc_methlist: 0x2dfc
+  __TEXT.__const: 0x6ea
+  __TEXT.__cstring: 0x4aa61
+  __TEXT.__oslogstring: 0x17fae
   __TEXT.__gcc_except_tab: 0x9468
   __TEXT.__ustring: 0x430
   __TEXT.__dlopen_cstrs: 0x2a4
-  __TEXT.__swift5_typeref: 0x1ce
-  __TEXT.__constg_swiftt: 0x140
-  __TEXT.__swift5_fieldmd: 0xb0
+  __TEXT.__swift5_typeref: 0x1fa
+  __TEXT.__constg_swiftt: 0x188
+  __TEXT.__swift5_fieldmd: 0xe4
   __TEXT.__swift5_capture: 0xe4
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_reflstr: 0x4f
-  __TEXT.__unwind_info: 0x45d4
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_reflstr: 0x6f
+  __TEXT.__unwind_info: 0x4634
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_classname: 0x870
-  __TEXT.__objc_methname: 0xd63b
+  __TEXT.__objc_methname: 0xd691
   __TEXT.__objc_methtype: 0x1c1d
-  __TEXT.__objc_stubs: 0xb6c0
-  __DATA_CONST.__got: 0x610
+  __TEXT.__objc_stubs: 0xb740
+  __DATA_CONST.__got: 0x640
   __DATA_CONST.__const: 0xfc48
-  __DATA_CONST.__objc_classlist: 0x208
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3f20
-  __DATA_CONST.__objc_selrefs: 0x31a8
+  __DATA_CONST.__objc_const: 0x3fc0
+  __DATA_CONST.__objc_selrefs: 0x31d0
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_classrefs: 0x628
+  __DATA_CONST.__objc_classrefs: 0x630
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__cfstring: 0xff80
-  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__cfstring: 0x10000
+  __AUTH_CONST.__objc_const: 0x110
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH_CONST.__const: 0xe58
+  __AUTH_CONST.__const: 0xe38
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1228
-  __AUTH.__objc_data: 0xc0
-  __AUTH.__data: 0x30
+  __AUTH_CONST.__auth_got: 0x1288
+  __AUTH.__objc_data: 0x170
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x8e0
-  __DATA.__bss: 0x2f8
-  __DATA.__common: 0x11
-  __DATA_DIRTY.__const: 0x15e8
-  __DATA_DIRTY.__objc_const: 0x1668
-  __DATA_DIRTY.__objc_data: 0x15a0
-  __DATA_DIRTY.__data: 0x298
+  __DATA.__data: 0x950
+  __DATA.__bss: 0x2e8
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__const: 0xc40
+  __DATA_DIRTY.__objc_const: 0x15e8
+  __DATA_DIRTY.__objc_data: 0x15c8
+  __DATA_DIRTY.__data: 0xd18
   __DATA_DIRTY.__bss: 0x5b8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/SharedWithYouCore.framework/SharedWithYouCore
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreRecents.framework/CoreRecents
   - /System/Library/PrivateFrameworks/CoreSDB.framework/CoreSDB

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3178A22-DAC1-32D1-A5EB-F15B4A0CC0E2
-  Functions: 4179
-  Symbols:   2173
-  CStrings:  8754
+  UUID: 5CCD2E7C-CAFB-3AEE-A68F-48635DDCC257
+  Functions: 4215
+  Symbols:   2184
+  CStrings:  8781
 
Symbols:
+ _IMChatPropertyGUID
+ _IMDMigrateTo17011
+ _IMDMigrateTo17012
+ _IMDMigrateTo17013
+ _OBJC_CLASS_$_IMDAskToParser
+ _OBJC_METACLASS_$_IMDAskToParser
+ __IMDDatabaseCompleteMigration
+ __IMDDatabasePerformOneMigration
+ __IMDGetMigrators
+ __IMDInitializeMessagesRecordStoreWithVersion
+ __swift_stdlib_bridgeErrorToNSError
CStrings:
+ "%s got mapURL %{sensitive}@ value %{sensitive}@"
+ "%s urls %{sensitive}@"
+ "Could not parse ATPayload from url. error: %@, url:%s"
+ "DELETE FROM message WHERE associated_message_guid IS NOT NULL AND LENGTH(SUBSTR(associated_message_guid, -36)) = 36 AND SUBSTR(associated_message_guid, -36) IN (SELECT guid FROM message WHERE associated_message_guid IS NULL AND error != 0 AND ROWID NOT IN (SELECT message_id FROM chat_message_join))"
+ "DELETE FROM message WHERE error != 0 AND ROWID NOT IN (SELECT message_id FROM chat_message_join);"
+ "IMDAskToParser"
+ "IMDPersistence.AskToParser"
+ "INSERT INTO deleted_messages (guid) SELECT guid FROM message WHERE error != 0 AND ROWID NOT IN (SELECT message_id FROM chat_message_join);"
+ "INSERT INTO sync_deleted_messages (guid, recordID) SELECT guid, ck_record_id FROM message WHERE error != 0 AND ROWID NOT IN (SELECT message_id FROM chat_message_join);"
+ "Provided payload URL was nil"
+ "TB,N,R"
+ "deprecatedReferenceURLForMessageGUID:"
+ "initWithUrl:"
+ "isValid"
+ "notificationText"
+ "payload"
+ "summary"
+ "url"
+ "urlParser"
- "%s got mapURL %@ value %@"
- "%s urls %@"

```
