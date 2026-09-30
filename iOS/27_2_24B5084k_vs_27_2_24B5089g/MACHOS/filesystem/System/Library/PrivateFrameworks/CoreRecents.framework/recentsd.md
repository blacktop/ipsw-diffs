## recentsd

> `/System/Library/PrivateFrameworks/CoreRecents.framework/recentsd`

### Sections with Same Size but Changed Content

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

-1237.200.11.0.0
-  __TEXT.__text: 0x170c8
+1237.200.21.0.0
+  __TEXT.__text: 0x171cc
   __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_stubs: 0x4000
-  __TEXT.__objc_methlist: 0x142c
+  __TEXT.__objc_stubs: 0x40e0
+  __TEXT.__objc_methlist: 0x148c
   __TEXT.__const: 0x10c
-  __TEXT.__objc_methname: 0x3a0f
+  __TEXT.__objc_methname: 0x3b40
   __TEXT.__cstring: 0x489b
   __TEXT.__objc_classname: 0x2fc
   __TEXT.__objc_methtype: 0xaa7
   __TEXT.__gcc_except_tab: 0x30c
-  __TEXT.__oslogstring: 0x133d
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__oslogstring: 0x1373
+  __TEXT.__unwind_info: 0x9b8
   __DATA_CONST.__const: 0xbe0
   __DATA_CONST.__cfstring: 0x1da0
   __DATA_CONST.__objc_classlist: 0xd8

   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x3b0
   __DATA.__objc_const: 0x23c0
-  __DATA.__objc_selrefs: 0x1200
+  __DATA.__objc_selrefs: 0x1240
   __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x870
   __DATA.__data: 0x370

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 578
+  Functions: 587
   Symbols:   340
-  CStrings:  1327
+  CStrings:  1336
 
CStrings:
+ "Unclassified sqlite error %d opening recents database"
+ "_abortForUnclassifiedSQLiteErrorCode:"
+ "_removeDatabaseForCannotOpenAndAbort"
+ "_removeDatabaseForCorruptDatabaseAndAbort"
+ "_removeDatabaseForDiskFullAndAbort"
+ "_removeDatabaseForMigrationFailureAndAbort"
+ "_removeDatabaseForNotADatabaseAndAbort"
+ "_removeDatabaseForPathAndAbort"
+ "_removeDatabaseForUnknownReasonAndAbort"
```
