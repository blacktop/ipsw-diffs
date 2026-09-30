## SyncedDefaultsDaemon

> `/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/SyncedDefaultsDaemon`

```diff

-2260.11.0.0.0
-  __TEXT.__text: 0x378b4
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x171c
+2260.12.0.0.0
+  __TEXT.__text: 0x37708
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x1724
   __TEXT.__const: 0x126
-  __TEXT.__gcc_except_tab: 0x1154
-  __TEXT.__cstring: 0x2139
-  __TEXT.__oslogstring: 0x6d42
+  __TEXT.__gcc_except_tab: 0x1138
+  __TEXT.__cstring: 0x2169
+  __TEXT.__oslogstring: 0x6c7f
   __TEXT.__dlopen_cstrs: 0xb5
   __TEXT.__swift5_typeref: 0x5
   __TEXT.__unwind_info: 0xc38
   __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x5dba
+  __TEXT.__objc_methname: 0x5dd5
   __TEXT.__objc_methtype: 0xd3b
-  __TEXT.__objc_stubs: 0x4fc0
+  __TEXT.__objc_stubs: 0x4fe0
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__const: 0xd48
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1728
+  __DATA_CONST.__objc_selrefs: 0x1730
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x1f8
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x21e0
   __AUTH_CONST.__objc_const: 0x1908

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1137
-  Symbols:   3740
-  CStrings:  1920
+  Functions: 1135
+  Symbols:   3736
+  CStrings:  1919
 
Symbols:
+ -[SYDKeyValue mergeDataFromRecord:].cold.11
+ -[SYDKeyValue updateWithServerRecord:]
+ -[SYDKeyValue updateWithServerRecord:].cold.1
+ -[SYDKeyValue updateWithServerRecord:].cold.2
+ -[SYDSyncManager getSyncEngineStateSerialization:error:]
+ GCC_except_table115
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table22
+ GCC_except_table29
+ GCC_except_table48
+ GCC_except_table74
+ ___26-[SYDDaemon uploadContent]_block_invoke.100
+ ___26-[SYDDaemon uploadContent]_block_invoke.100.cold.1
+ ___26-[SYDDaemon uploadContent]_block_invoke.98
+ ___26-[SYDDaemon uploadContent]_block_invoke.98.cold.1
+ ___26-[SYDDaemon uploadContent]_block_invoke.98.cold.2
+ _objc_msgSend$getSyncEngineStateSerialization:error:
+ _objc_msgSend$updateWithServerRecord:
+ _os_transaction_create
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:]
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:].cold.1
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:].cold.2
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:].cold.3
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:].cold.4
- -[SYDKeyValue setServerSystemFieldsRecordIfNewer:].cold.5
- -[SYDSyncManager initializeSyncEngineWithError:].cold.3
- GCC_except_table113
- GCC_except_table3
- GCC_except_table73
- ___26-[SYDDaemon uploadContent]_block_invoke.97
- ___26-[SYDDaemon uploadContent]_block_invoke.97.cold.1
- ___26-[SYDDaemon uploadContent]_block_invoke.97.cold.2
- ___26-[SYDDaemon uploadContent]_block_invoke.99
- ___26-[SYDDaemon uploadContent]_block_invoke.99.cold.1
- _objc_msgSend$setServerSystemFieldsRecordIfNewer:
CStrings:
+ "B32@0:8^@16^@24"
+ "Mismatched recordIDs. Keeping current record: %@, ignoring new record: %@"
+ "No current record, using new record: %@"
+ "No record provided to compare."
+ "Replacing current system fields record: %@ with new system fields record: %@"
+ "com.apple.kvs.daemon.initializeKnownSyncManagers"
+ "getSyncEngineStateSerialization:error:"
+ "updateWithServerRecord:"
- "B32@0:8^B16^@24"
- "Failed to unarchive state serialization: %@"
- "No current modification date on system fields record for %@"
- "No current system fields record for %@"
- "Not replacing local system fields record for %@: current=%@ other=%@"
- "Replacing local system fields record for %@: current=%@ other=%@"
- "Trying to set server record if newer, but no other record"
- "Trying to set server record using record with a different ID. current=%@ other=%@"
- "setServerSystemFieldsRecordIfNewer:"

```
