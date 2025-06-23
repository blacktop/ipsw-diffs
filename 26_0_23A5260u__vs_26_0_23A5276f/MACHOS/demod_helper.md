## demod_helper

> `/usr/libexec/demod_helper`

```diff

-1604.0.0.0.0
-  __TEXT.__text: 0x2fb6c
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x41c0
-  __TEXT.__objc_methlist: 0x1ad0
-  __TEXT.__const: 0xe0
+1611.0.0.0.0
+  __TEXT.__text: 0x316b0
+  __TEXT.__auth_stubs: 0x1180
+  __TEXT.__objc_stubs: 0x4320
+  __TEXT.__objc_methlist: 0x1b60
+  __TEXT.__cstring: 0x5eee
+  __TEXT.__objc_classname: 0x1fb
+  __TEXT.__objc_methname: 0x4aab
+  __TEXT.__objc_methtype: 0x5cf
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x318
-  __TEXT.__oslogstring: 0x5d44
-  __TEXT.__cstring: 0x5d35
-  __TEXT.__objc_classname: 0x1ee
-  __TEXT.__objc_methtype: 0x58c
-  __TEXT.__objc_methname: 0x491d
+  __TEXT.__oslogstring: 0x610e
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x910
-  __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0x310
+  __TEXT.__unwind_info: 0x948
+  __DATA_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x4ba0
+  __DATA_CONST.__cfstring: 0x4d20
   __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x2c0
-  __DATA_CONST.__objc_arrayobj: 0x2a0
+  __DATA_CONST.__objc_arraydata: 0x2d8
+  __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1908
-  __DATA.__objc_selrefs: 0x14b0
+  __DATA.__objc_const: 0x1948
+  __DATA.__objc_selrefs: 0x1510
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x85c

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 98E30AB6-786D-336C-B1EF-011A735EB24B
-  Functions: 991
-  Symbols:   376
-  CStrings:  2710
+  UUID: 0608A8BC-2DBB-3D4E-9198-435B00AD35D2
+  Functions: 1025
+  Symbols:   393
+  CStrings:  2772
 
Symbols:
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_NSError
+ _copyfile_state_alloc
+ _copyfile_state_free
+ _copyfile_state_set
+ _pread
+ _sqlite3_backup_finish
+ _sqlite3_backup_init
+ _sqlite3_backup_step
+ _sqlite3_close
+ _sqlite3_errcode
+ _sqlite3_errmsg
+ _sqlite3_open_v2
CStrings:
+ "%s - SQLite3 file %s was copied to %s using SQLite3 libraries"
+ "%s - file %s is sqlite3"
+ "-journal"
+ "-shm"
+ "-wal"
+ "@32@0:8q16@24"
+ "@40@0:8q16@24@32"
+ "An error occurred while checking if file %s is a SQLite3 DB: %{public}@"
+ "B48@0:8@16@24d32^@40"
+ "Copy of SQLite DB from %{public}@ to %{public}@ failed."
+ "Copying SQLite database at %{public}@ to %{public}@ (%lld bytes)"
+ "Could not retrieve file handle for file %@"
+ "Error initializing backup connection. code: %d, msg: %s"
+ "Error opening SQLite file: %s (%d)"
+ "Error removing copied SQLite file journal %{public}@"
+ "Failed to close the SQLite backup connection: %d"
+ "Failed to close the SQLite database at %{public}@: %d"
+ "Failed to copy db with status %d"
+ "Failed to remove the SQLite database at %{public}@"
+ "Failed to restore the source db's attributes to target"
+ "Finished copying SQLite database from %{public}@ to %{public}@ in %0.3fs (%lld bytes)"
+ "Invalid file protection level for file %{public}@ - %{public}@. Defaulting to 'None'"
+ "MSDDemodErrorDomain"
+ "MSDExtension"
+ "MSDMasterServerErrorDomain"
+ "Opened SQLite database at %{public}@"
+ "Opened destination db at %{public}@ with flags 0x%x"
+ "Removed copied SQLite file journal at %{public}@"
+ "RetryAfter"
+ "SQLite copy error: on file %s - %{public}@"
+ "SQLite format 3"
+ "_getProtectionClassForFile:error:"
+ "copySQLiteFile:toPath:timeout:error:"
+ "errorDomainMSDWithCode:message:"
+ "errorDomainMSDWithCode:message:reason:"
+ "falling back to default copyfile() behavior"
+ "i32@0:8@16^@24"
+ "initWithDomain:code:userInfo:"
+ "initWithDomainMSDCode:message:"
+ "initWithDomainMSDCode:message:reason:"
+ "int copyfile_callback(int, int, copyfile_state_t, const char *, const char *, void *)"
+ "isSQLiteFile:error:"
+ "main"
+ "masterServerErrorRetryAfter:"
+ "masterServerErrorWithCode:mesage:reason:"
+ "pread() error errno: %d - file: %@"
+ "pread() failed at %{public}@: %{errno}d"
+ "removeJournalsForSQLiteFileAtPaths:"
+ "sqlite3_backup operation completed successfully"
+ "timeIntervalSinceReferenceDate"

```
