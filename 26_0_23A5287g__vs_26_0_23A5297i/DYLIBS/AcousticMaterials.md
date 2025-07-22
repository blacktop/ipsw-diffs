## AcousticMaterials

> `/System/Library/PrivateFrameworks/AcousticMaterials.framework/AcousticMaterials`

```diff

-23.0.2.0.0
-  __TEXT.__text: 0x8d28
-  __TEXT.__auth_stubs: 0x410
+24.0.1.0.0
+  __TEXT.__text: 0x8fb4
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x344
   __TEXT.__const: 0x51
-  __TEXT.__cstring: 0x696
+  __TEXT.__cstring: 0x7c4
   __TEXT.__gcc_except_tab: 0x7ec
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__unwind_info: 0x3a8
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x1857
+  __TEXT.__objc_methname: 0x1870
   __TEXT.__objc_methtype: 0x1c2b
-  __TEXT.__objc_stubs: 0x9c0
+  __TEXT.__objc_stubs: 0xa00
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x8b0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x180

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: BDBE1A89-3992-384C-906A-99BC84D2BF07
+  UUID: 15A66E23-9379-3BC2-8606-A08BFD600AE0
   Functions: 150
-  Symbols:   637
-  CStrings:  273
+  Symbols:   641
+  CStrings:  284
 
Symbols:
+ _DBIOErrorDomain
+ _objc_msgSend$absoluteString
+ _objc_msgSend$isFileURL
+ _sqlite3_close_v2
+ _sqlite3_errstr
- _sqlite3_close
Functions:
~ _DBIOOpenDatabaseFromURL : 380 -> 988
~ _DBIOCloseDatabase : 316 -> 360
CStrings:
+ "Could not get file system path from URL: %@"
+ "Failed to allocate memory for database structure."
+ "Failed to close SQLite database: %s (SQLite error code: %d). If the error is SQLITE_BUSY, there are likely unfinalized statements or active backups."
+ "Failed to open SQLite database at '%@': %s (code: %d)"
+ "URL is not a file URL: %@"
+ "Unknown SQLite error"
+ "absoluteString"
+ "com.apple.databaseIO.ErrorDomain"
+ "isFileURL"
- "Failed to close SQLite database [%s]"
- "Failed to open SQLite database: '%s'."

```
