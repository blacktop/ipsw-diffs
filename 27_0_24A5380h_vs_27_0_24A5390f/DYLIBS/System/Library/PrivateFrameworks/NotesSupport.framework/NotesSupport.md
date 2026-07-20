## NotesSupport

> `/System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2996.0.0.0.0
-  __TEXT.__text: 0x55ce0
+2998.0.0.0.0
+  __TEXT.__text: 0x58404
   __TEXT.__delay_helper: 0x2cc
-  __TEXT.__objc_methlist: 0x4378
-  __TEXT.__const: 0xb6c
-  __TEXT.__cstring: 0x4589
-  __TEXT.__gcc_except_tab: 0xed8
-  __TEXT.__oslogstring: 0x3e86
+  __TEXT.__objc_methlist: 0x43f8
+  __TEXT.__const: 0xb5c
+  __TEXT.__cstring: 0x4749
+  __TEXT.__gcc_except_tab: 0xef0
+  __TEXT.__oslogstring: 0x4496
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x2bb
-  __TEXT.__swift5_capture: 0x210
   __TEXT.__constg_swiftt: 0x228
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0xde
+  __TEXT.__swift5_reflstr: 0xec
   __TEXT.__swift5_fieldmd: 0x1c0
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_capture: 0x210
   __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x2c
   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x1d38
+  __TEXT.__unwind_info: 0x1d40
   __TEXT.__eh_frame: 0x7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1380
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0x13a8
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3178
+  __DATA_CONST.__objc_selrefs: 0x3230
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__objc_arraydata: 0x1a8
+  __DATA_CONST.__got: 0x898
   __AUTH_CONST.__const: 0x16a0
-  __AUTH_CONST.__cfstring: 0x4460
-  __AUTH_CONST.__objc_const: 0x5ed0
+  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__objc_const: 0x5f90
+  __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1050
-  __AUTH.__objc_data: 0x120
+  __AUTH_CONST.__auth_got: 0x1100
+  __AUTH.__objc_data: 0x170
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_ivar: 0x224
   __DATA.__data: 0x6f4
   __DATA.__bss: 0x570
   __DATA_DIRTY.__objc_data: 0x1270

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2539
-  Symbols:   4861
-  CStrings:  1031
+  Functions: 2570
+  Symbols:   4924
+  CStrings:  1080
 
Symbols:
+ +[ICPersistentContainer isOutOfSpaceError:]
+ +[ICPersistentContainer isSHMOpenError:]
+ +[ICSQLiteRecovery recoverDatabaseAtURL:toURL:error:]
+ -[ICPersistentContainer allowsDatabaseRecovery]
+ -[ICPersistentContainer attemptSQLiteRecoveryWithError:]
+ -[ICPersistentContainer failureCountFileURL]
+ -[ICPersistentContainer readFailureCount]
+ -[ICPersistentContainer resetFailureCount]
+ -[ICPersistentContainer setAllowsDatabaseRecovery:]
+ -[ICPersistentContainer writeFailureCount:]
+ _ICArchiveReaderResolveURL
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_ICSQLiteRecovery
+ _OBJC_IVAR_$_ICPersistentContainer._allowsDatabaseRecovery
+ _OBJC_METACLASS_$_ICSQLiteRecovery
+ __OBJC_$_CLASS_METHODS_ICSQLiteRecovery
+ __OBJC_CLASS_RO_$_ICSQLiteRecovery
+ __OBJC_METACLASS_RO_$_ICSQLiteRecovery
+ ___block_descriptor_40_e8_32r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16lr32l8
+ _archive_read_free
+ _archive_read_support_filter_all
+ _archive_write_add_filter_bzip2
+ _archive_write_add_filter_none
+ _archive_write_disk_set_options
+ _archive_write_free
+ _objc_msgSend$URLByResolvingSymlinksInPath
+ _objc_msgSend$_URLByInsertingResolveFlags:
+ _objc_msgSend$_resolveFlags
+ _objc_msgSend$allowsDatabaseRecovery
+ _objc_msgSend$attemptSQLiteRecoveryWithError:
+ _objc_msgSend$failureCountFileURL
+ _objc_msgSend$filePathURL
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isFileReferenceURL
+ _objc_msgSend$isOutOfSpaceError:
+ _objc_msgSend$isSHMOpenError:
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$readFailureCount
+ _objc_msgSend$recoverDatabaseAtURL:toURL:error:
+ _objc_msgSend$removeObjectsInRange:
+ _objc_msgSend$resetFailureCount
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$writeFailureCount:
+ _objc_msgSend$writeToURL:atomically:encoding:error:
+ _sqlite3_bind_blob
+ _sqlite3_bind_double
+ _sqlite3_bind_int64
+ _sqlite3_bind_null
+ _sqlite3_bind_text
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_count
+ _sqlite3_column_double
+ _sqlite3_column_int64
+ _sqlite3_column_text
+ _sqlite3_column_type
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_reset
+ _sqlite3_step
- _archive_read_finish
- _archive_read_support_compression_all
- _archive_write_finish
- _archive_write_set_compression_bzip2
- _archive_write_set_compression_none
CStrings:
+ "%@-recovered-%@.sqlite"
+ ", ?"
+ ".failurecount"
+ "Attempting SQLite recovery after %lu consecutive failures"
+ "BEGIN TRANSACTION"
+ "Beginning SQLite recovery from %@ to %@"
+ "COMMIT"
+ "Crashing to allow relaunch. Failure count: %lu"
+ "Database open failed after all retries. Failure count: %lu"
+ "Database open failed after retries during unit tests; replacing store instead of relaunching. Failure count: %lu"
+ "Database open failed and would exit; surfacing error instead during unit tests: %@"
+ "Database open succeeded on retry attempt %lu"
+ "Entry path '%@' escapes destination directory"
+ "Error reading row from table %@: %s (code %d)"
+ "Failed to create deferred schema object: %s"
+ "Failed to create destination database for recovery: %s (code %d)"
+ "Failed to create destination database: %s"
+ "Failed to create table %@: %s"
+ "Failed to insert row into table %@: %s"
+ "Failed to move recovered database into place: %@"
+ "Failed to open corrupt database for recovery: %s (code %d)"
+ "Failed to open corrupt database: %s"
+ "Failed to prepare INSERT for table %@: %s"
+ "Failed to prepare SELECT for table %@: %s"
+ "Failed to read sqlite_master: %s"
+ "Failed to read sqlite_master: %s (code %d)"
+ "Failed to remove failure count file: %@"
+ "Failed to write failure count file: %@"
+ "INSERT INTO \"%@\" VALUES (?"
+ "No schema entries found in corrupt database"
+ "ROLLBACK"
+ "Recovered database is now in place at %@"
+ "Retry attempt %lu failed: %@"
+ "Retrying database open (attempt %lu of 3)"
+ "SELECT * FROM \"%@\""
+ "SELECT type, name, tbl_name, sql FROM sqlite_master WHERE sql IS NOT NULL ORDER BY rowid"
+ "SQLITE_IOERR_SHMOPEN persisted after retries; not destroying the store. Failure count: %lu"
+ "SQLite recovery completed successfully"
+ "SQLite recovery failed: %@"
+ "SQLite recovery failed: %@. Falling back to database move."
+ "SQLite recovery produced no data"
+ "SQLite recovery succeeded"
+ "SQLite recovery succeeded. Backing up corrupt database and replacing with recovered database."
+ "Table %@: recovered %lu rows, failed %lu rows"
+ "private"
+ "sql"
+ "table"
+ "type"
+ "unknown error"
+ "var"
- "Entry path '%@' contains directory traversal"
```
