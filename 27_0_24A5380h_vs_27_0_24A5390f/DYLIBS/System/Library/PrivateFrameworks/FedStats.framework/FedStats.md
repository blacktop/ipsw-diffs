## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-83.0.0.0.0
-  __TEXT.__text: 0x179e0
-  __TEXT.__objc_methlist: 0x177c
+84.0.0.0.0
+  __TEXT.__text: 0x17ec8
+  __TEXT.__objc_methlist: 0x1794
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x307f
+  __TEXT.__cstring: 0x30e9
   __TEXT.__oslogstring: 0x604
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__unwind_info: 0x470
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc98
+  __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x3d0
   __DATA_CONST.__got: 0x2a0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x2dc0
+  __AUTH_CONST.__cfstring: 0x2e40
   __AUTH_CONST.__objc_const: 0x3120
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 434
-  Symbols:   1419
-  CStrings:  404
+  Functions: 437
+  Symbols:   1426
+  CStrings:  408
 
Symbols:
+ -[FedStatsSQLiteDatabase execute:withParameters:error:]
+ -[FedStatsSQLiteDatabase runQuery:withParameters:error:]
+ _bindTextParameters
+ _objc_msgSend$execute:withParameters:error:
+ _objc_msgSend$runQuery:withParameters:error:
+ _sqlite3_bind_text
+ _sqlite3_free
CStrings:
+ "?"
+ "Cannot bind query parameter: %s"
+ "Cannot prepare command: %s"
+ "INSERT INTO '%@' VALUES (%lu, ?)"
+ "Query parameters must be strings"
+ "SELECT %@ FROM '%@' WHERE %@ == ? ORDER BY RANDOM() LIMIT 1"
+ "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == ?"
+ "SELECT COUNT(1) AS %@ FROM '%@' WHERE ? LIKE '%%' || %@ || '%%'"
+ "`command` should be a string"
- "\"%@\""
- "INSERT INTO '%@' VALUES (%lu, \"%@\")"
- "SELECT %@ FROM '%@' WHERE %@ == \"%@\" ORDER BY RANDOM() LIMIT 1"
- "SELECT COUNT(1) AS %@ FROM '%@' WHERE %@ == \"%@\""
- "SELECT COUNT(1) AS %@ FROM '%@' WHERE '%@' LIKE '%%' || %@ || '%%'"
```
