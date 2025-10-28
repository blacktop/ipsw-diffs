## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.200.61.0.0
-  __TEXT.__text: 0x7536c
-  __TEXT.__auth_stubs: 0x2200
+12851.200.61.2.4
+  __TEXT.__text: 0x75624
+  __TEXT.__auth_stubs: 0x2220
   __TEXT.__objc_methlist: 0x2fac
   __TEXT.__const: 0x339
-  __TEXT.__cstring: 0x2677a
-  __TEXT.__oslogstring: 0x25d6
+  __TEXT.__cstring: 0x268f6
+  __TEXT.__oslogstring: 0x24b2
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c

   __DATA_CONST.__objc_selrefs: 0x24d0
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1110
-  __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0xd980
+  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__const: 0xe80
+  __AUTH_CONST.__cfstring: 0xd9e0
   __AUTH_CONST.__objc_const: 0x4b40
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   __DATA.__objc_ivar: 0x3f4
   __DATA.__data: 0x2c8
   __DATA.__common: 0x4
-  __DATA.__bss: 0x340
+  __DATA.__bss: 0x358
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3EA85F5A-2C0E-3B0E-B137-77EE71ED4F92
-  Functions: 2524
-  Symbols:   7140
-  CStrings:  6057
+  UUID: 4012257C-91A2-3E43-9D9C-202247A69D75
+  Functions: 2522
+  Symbols:   7141
+  CStrings:  6061
 
Symbols:
+ GCC_except_table56
+ GCC_except_table64
+ GCC_except_table70
+ _ABPersonSizeForFormat
+ _CFURLCreateCopyAppendingPathComponent
+ _CFURLGetString
+ ____imageStoreMigrationMigrateDatabase_block_invoke
+ ___block_literal_global.117
+ __imageStoreMigrationMigrateDatabase.cold.1
+ __imageStoreMigrationMigrateDatabase.maxThumbnailSize.0
+ __imageStoreMigrationMigrateDatabase.maxThumbnailSize.1
+ __imageStoreMigrationMigrateDatabase.onceToken
- GCC_except_table55
- GCC_except_table60
- GCC_except_table63
- GCC_except_table69
- _ABAddressBookCopyAllPeopleForBufferPredicate.cold.1
- _ABAddressBookCopyAllPeopleForBufferPredicate.cold.2
- _ABAddressBookCopyAllPeopleForBufferPredicate.cold.3
- _ABAddressBookCopyAllPeopleForBufferPredicate.cold.4
CStrings:
+ "AB Migration - Attempting to compress thumbnail image of original size {%d x %d}"
+ "AB Migration - Compressed %ld oversized thumbnails"
+ "AB Migration - Compressed thumbnail for record_id %ld: %d bytes -> %ld bytes"
+ "CPSqliteMigrationContinuation _imageStoreMigrationMigrateDatabase(CPSqliteDatabase *, CPSqliteConnection *, int, void *)"
+ "UPDATE ABThumbnailImage SET data=? WHERE ROWID=?;"
- "ABAddressBookCopyAllPeopleForBufferPredicate: ABCPersonClass is NULL"
- "ABAddressBookCopyAllPeopleForBufferPredicate: Failed to create query string"
- "ABAddressBookCopyAllPeopleForBufferPredicate: addressBook->dbContext is NULL"
- "ABAddressBookCopyAllPeopleForBufferPredicate: predicate.query is NULL"

```
