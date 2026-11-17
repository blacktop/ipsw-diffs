## recentsd

> `/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1237.200.31.0.0
-  __TEXT.__text: 0x171cc
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_stubs: 0x40e0
-  __TEXT.__objc_methlist: 0x148c
-  __TEXT.__const: 0x10c
-  __TEXT.__objc_methname: 0x3b40
-  __TEXT.__cstring: 0x489b
+1237.300.2.0.0
+  __TEXT.__text: 0x18420
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_methlist: 0x1534
+  __TEXT.__const: 0x11c
+  __TEXT.__objc_methname: 0x3daf
+  __TEXT.__cstring: 0x496c
   __TEXT.__objc_classname: 0x2fc
-  __TEXT.__objc_methtype: 0xaa7
-  __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__oslogstring: 0x1373
-  __TEXT.__unwind_info: 0x9b8
-  __DATA_CONST.__const: 0xbe0
+  __TEXT.__objc_methtype: 0xb1c
+  __TEXT.__gcc_except_tab: 0x370
+  __TEXT.__oslogstring: 0x168e
+  __TEXT.__unwind_info: 0xa10
+  __DATA_CONST.__const: 0xc08
   __DATA_CONST.__cfstring: 0x1da0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0x3b0
-  __DATA.__objc_const: 0x23c0
-  __DATA.__objc_selrefs: 0x1240
-  __DATA.__objc_ivar: 0x184
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x3c8
+  __DATA.__objc_const: 0x24f0
+  __DATA.__objc_selrefs: 0x12c8
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 587
-  Symbols:   340
-  CStrings:  1336
+  Functions: 606
+  Symbols:   346
+  CStrings:  1385
 
Symbols:
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSProcessInfo
+ _objc_retain_x24
+ _objc_retain_x4
+ _sqlite3_extended_errcode
+ _sqlite3_system_errno
+ _statfs
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ " - volume is out of space"
+ "-[_CRRecentsLibrary _deleteRecentsWithRecentIDs:storeKeys:recentsDomain:deleteInUbiquitousStore:error:]"
+ "@24@0:8^{?=iiBBB}16"
+ "Another connection already replaced the damaged recents database, not deleting it again"
+ "B24@0:8^{sqlite3_stmt=}16"
+ "B24@0:8i16i20"
+ "B32@0:8@16^@24"
+ "B36@0:8@?16B24^@28"
+ "Could not delete %lu recent(s) from '%{public}@', leaving them in place"
+ "Could not open the recents database (%{public}s): sqlite error %d, system error %d (%{public}s), attempt %lu, trying again in %.0fs"
+ "Error %d (extended %d) on connection %p %{public}@: %{public}s"
+ "Error %d (extended %d) on connection %p %{public}@: %{public}s - system error %d (%{public}s)%{public}s"
+ "Error removing records for domain %{public}@: %{public}@"
+ "Migrating the recents database failed (sqlite error %d)"
+ "Opened the recents database after %lu failed attempts"
+ "Q32@0:8@16^B24"
+ "Q56@0:8@16@24@32@40^@48"
+ "SQLite error %d on the recents database, system error %d (%{public}s): %{public}s"
+ "TB,N,V_diskFull"
+ "The recents database is damaged, deleting it and creating a new one"
+ "Treating sqlite error %d as the volume being out of space: almost no free space left"
+ "Treating the failed migration as the volume being out of space: almost no free space left"
+ "_consecutiveOpenFailures"
+ "_currentRecoveryCount"
+ "_databasePropertyValueByKey:didRead:"
+ "_databaseUnavailableError"
+ "_databaseUnavailableErrorForDiskFull:"
+ "_deleteRecentsWithRecentIDs:storeKeys:recentsDomain:deleteInUbiquitousStore:error:"
+ "_diskFull"
+ "_isDiskFullError:systemErrno:"
+ "_lastOpenFailureWasDiskFull"
+ "_mayAttemptToOpenDatabase"
+ "_newOpenedConnectionReportingFailure:"
+ "_nextOpenAttemptTime"
+ "_noteDatabaseOpenFailed:"
+ "_noteDatabaseOpenSucceeded"
+ "_openErrorCode"
+ "_openStateLock"
+ "_openSystemErrno"
+ "_performTransaction:forWriting:error:"
+ "_recoveryCount"
+ "_recoveryLock"
+ "_removeDamagedDatabaseUnlessRecoveredSince:"
+ "_removeLocalRecordsForDomain:removeInUbiquitousStore:error:"
+ "_saveRecentContacts:error:"
+ "_stepToCompletion:"
+ "aborting"
+ "carrying on"
+ "diskFull"
+ "extendedErrorCode"
+ "fileSystemRepresentation"
+ "lastSystemErrno"
+ "processInfo"
+ "recordContactEvents:recentsDomain:sendingAddress:source:error:"
+ "schema migration failed"
+ "see the sqlite error"
+ "setDiskFull:"
+ "systemUptime"
+ "the database is damaged, deleting it and aborting"
+ "the volume is out of space"
+ "the volume is out of space, failing the transaction"
+ "v28@0:8{?=iiBBB}16"
- "-[_CRRecentsLibrary _deleteRecentsWithRecentIDs:storeKeys:recentsDomain:deleteInUbiquitousStore:]"
- "Error %d on connection %p %{public}@: %s"
- "Error %d on connection %p %{public}@: %s - I/O error %d (%s)"
- "Unclassified sqlite error %d opening recents database"
- "_abortForUnclassifiedSQLiteErrorCode:"
- "_deleteRecentsWithRecentIDs:storeKeys:recentsDomain:deleteInUbiquitousStore:"
- "_performTransaction:forWriting:"
- "_removeDatabaseForCannotOpenAndAbort"
- "_removeDatabaseForDiskFullAndAbort"
- "_removeDatabaseForMigrationFailureAndAbort"
- "nil != connection"
- "v28@0:8@?16B24"
- "v44@0:8@16@24@32B40"
```
