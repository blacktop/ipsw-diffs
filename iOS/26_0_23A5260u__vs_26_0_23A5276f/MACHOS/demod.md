## demod

> `/usr/libexec/demod`

```diff

-1604.0.0.0.0
-  __TEXT.__text: 0xe4bb8
-  __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_stubs: 0x18a00
-  __TEXT.__objc_methlist: 0xc04c
-  __TEXT.__const: 0x292
+1611.0.0.0.0
+  __TEXT.__text: 0xe614c
+  __TEXT.__auth_stubs: 0x1bd0
+  __TEXT.__objc_stubs: 0x18ac0
+  __TEXT.__objc_methlist: 0xc084
+  __TEXT.__const: 0x29a
   __TEXT.__gcc_except_tab: 0x48f0
-  __TEXT.__oslogstring: 0x18abc
-  __TEXT.__cstring: 0xedba
+  __TEXT.__oslogstring: 0x18e5c
+  __TEXT.__cstring: 0xef5a
   __TEXT.__objc_classname: 0x1605
-  __TEXT.__objc_methtype: 0x3858
-  __TEXT.__objc_methname: 0x1cdd3
+  __TEXT.__objc_methtype: 0x387c
+  __TEXT.__objc_methname: 0x1ce75
   __TEXT.__swift5_typeref: 0x87
   __TEXT.__swift5_capture: 0x84
   __TEXT.__constg_swiftt: 0x38

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x3378
+  __TEXT.__unwind_info: 0x3398
   __TEXT.__eh_frame: 0x1d0
-  __DATA_CONST.__auth_got: 0xda0
-  __DATA_CONST.__got: 0xcc8
+  __DATA_CONST.__auth_got: 0xdf8
+  __DATA_CONST.__got: 0xce0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2db0
-  __DATA_CONST.__cfstring: 0xd6e0
+  __DATA_CONST.__const: 0x2d90
+  __DATA_CONST.__cfstring: 0xd820
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_intobj: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x858
-  __DATA_CONST.__objc_arrayobj: 0x420
+  __DATA_CONST.__objc_arraydata: 0x870
+  __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA.__objc_const: 0x16ef0
-  __DATA.__objc_selrefs: 0x7210
+  __DATA.__objc_selrefs: 0x7238
   __DATA.__objc_ivar: 0xa14
   __DATA.__objc_data: 0x41b0
   __DATA.__data: 0x26d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 57B7E563-F82A-3C75-AE2B-518CD5C07426
-  Functions: 5288
-  Symbols:   887
-  CStrings:  11536
+  UUID: 24EE4116-45D4-3DD1-8A6C-6468C1DC8C56
+  Functions: 5310
+  Symbols:   897
+  CStrings:  11583
 
Symbols:
+ _NSFileProtectionComplete
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
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
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%s - SQLite3 file %s was copied to %s using SQLite3 libraries"
+ "%s - file %s is sqlite3"
+ "-journal"
+ "-shm"
+ "-wal"
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
+ "Opened SQLite database at %{public}@"
+ "Opened destination db at %{public}@ with flags 0x%x"
+ "Removed copied SQLite file journal at %{public}@"
+ "SQLite copy error: on file %s - %{public}@"
+ "SQLite format 3"
+ "_getProtectionClassForFile:error:"
+ "com.apple.retailtech.experiences.mac"
+ "copySQLiteFile:toPath:timeout:error:"
+ "falling back to default copyfile() behavior"
+ "fileHandleForReadingFromURL:error:"
+ "i32@0:8@16^@24"
+ "int copyfile_callback(int, int, copyfile_state_t, const char *, const char *, void *)"
+ "isSQLiteFile:error:"
+ "pread() error errno: %d - file: %@"
+ "pread() failed at %{public}@: %{errno}d"
+ "removeJournalsForSQLiteFileAtPaths:"
+ "sqlite3_backup operation completed successfully"
- "Store hour not in right order - %{public}@"

```
