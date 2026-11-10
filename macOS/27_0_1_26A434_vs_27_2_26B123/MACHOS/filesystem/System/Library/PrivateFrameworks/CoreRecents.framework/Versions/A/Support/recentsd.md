## recentsd

> `/System/Library/PrivateFrameworks/CoreRecents.framework/Versions/A/Support/recentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1234.100.1.0.0
-  __TEXT.__text: 0x16f80
+1237.200.31.0.0
+  __TEXT.__text: 0x1720c
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_stubs: 0x3ea0
-  __TEXT.__objc_methlist: 0x142c
+  __TEXT.__objc_stubs: 0x3f60
+  __TEXT.__objc_methlist: 0x147c
   __TEXT.__const: 0x114
-  __TEXT.__objc_methname: 0x3975
+  __TEXT.__objc_methname: 0x3a87
   __TEXT.__cstring: 0x46b2
   __TEXT.__objc_classname: 0x2fc
   __TEXT.__objc_methtype: 0xaa5
   __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__oslogstring: 0x12f7
+  __TEXT.__oslogstring: 0x145e
   __TEXT.__info_plist: 0x303
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__unwind_info: 0x9b0
   __DATA_CONST.__const: 0xbe0
   __DATA_CONST.__cfstring: 0x1ce0
   __DATA_CONST.__objc_classlist: 0xd8

   __DATA_CONST.__auth_got: 0x548
   __DATA_CONST.__got: 0x3a0
   __DATA.__objc_const: 0x2330
-  __DATA.__objc_selrefs: 0x11d0
+  __DATA.__objc_selrefs: 0x1208
   __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x368

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 592
+  Functions: 603
   Symbols:   292
-  CStrings:  1299
+  CStrings:  1313
 
CStrings:
+ "Deleting recents database: SQLITE_CANTOPEN/PERM/READONLY/AUTH"
+ "Deleting recents database: SQLITE_CORRUPT"
+ "Deleting recents database: SQLITE_FULL (volume out of space)"
+ "Deleting recents database: SQLITE_NOTADB"
+ "Deleting recents database: cause not classified"
+ "Deleting recents database: schema migration failed"
+ "Unclassified sqlite error %d opening recents database"
+ "_abortForUnclassifiedSQLiteErrorCode:"
+ "_removeDatabaseForCannotOpenAndAbort"
+ "_removeDatabaseForCorruptDatabaseAndAbort"
+ "_removeDatabaseForDiskFullAndAbort"
+ "_removeDatabaseForMigrationFailureAndAbort"
+ "_removeDatabaseForNotADatabaseAndAbort"
+ "_removeDatabaseForUnknownReasonAndAbort"
```
