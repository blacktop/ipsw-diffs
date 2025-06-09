## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61439.122.1.0.0
-  __TEXT.__text: 0x2cac
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0x360
-  __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x2a0
-  __TEXT.__objc_methtype: 0xfa
-  __TEXT.__cstring: 0x709
+61901.0.9.0.1
+  __TEXT.__text: 0x381c
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_stubs: 0x500
+  __TEXT.__objc_methlist: 0xd0
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__objc_classname: 0x3d
+  __TEXT.__objc_methname: 0x3f8
+  __TEXT.__objc_methtype: 0x17e
+  __TEXT.__cstring: 0xd90
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0x780
+  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0xf0
-  __DATA.__objc_selrefs: 0x110
+  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x190
+  __DATA.__objc_selrefs: 0x188
+  __DATA.__objc_data: 0x50
   __DATA.__data: 0x60
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97BB6C0A-D639-39F4-9676-3A49F7324426
-  Functions: 31
-  Symbols:   154
-  CStrings:  208
+  - /usr/lib/libsqlite3.dylib
+  UUID: 71DD171B-3409-3E2A-978D-B18EDB5271D0
+  Functions: 32
+  Symbols:   173
+  CStrings:  276
 
Symbols:
+ _NSLog
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_METACLASS_$_NSObject
+ _SecKeychainCopyDatabasePath
+ __objc_empty_cache
+ _objc_release
+ _objc_retain_x2
+ _sqlite3_close
+ _sqlite3_column_count
+ _sqlite3_column_name
+ _sqlite3_column_text
+ _sqlite3_errmsg
+ _sqlite3_finalize
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_step
CStrings:
+ "\n (Total agrps: %lu, Total Non-tombstone items: %lu, Total tombstone items: %lu)\n"
+ "\n -----------------------------------------------------------------\n"
+ "\n Keychain <access Group, #items> Information \n"
+ "\n Keychain <access Group, (#non-tombstone, #tombstone)> information for %@ item Class\n"
+ "\n Keychain Database Table Size Information \n"
+ "\n%@\n"
+ "\n%@, %@\n"
+ "\nError: %@ while creating second party regex \n"
+ "\nError: DB Path should not be null \n"
+ "\nError: Failed to get Keychain DB Path %@ \n"
+ "\nError: Failed to open SQL DB %s \n"
+ "\nError: Failed to prepare statement %s \n"
+ "\nError: SQL query should not be null \n"
+ ", "
+ "<REDACTED-AGRP-%lu>"
+ "@32@0:8@16@24"
+ "Failed to fetch DB path with status error: %@"
+ "SELECT agrp,                                 SUM(CASE WHEN tomb = 0 THEN 1 ELSE 0 END) AS count_tomb_0,                                  SUM(CASE WHEN tomb = 1 THEN 1 ELSE 0 END) AS count_tomb_1                                  FROM %@                                  GROUP BY agrp                                  ORDER BY (SUM(CASE WHEN tomb = 0 THEN 1 ELSE 0 END) + SUM(CASE WHEN tomb = 1 THEN 1 ELSE 0 END)) DESC"
+ "SELECT name, CASE                            WHEN sum(pgsize) >= 1073741824 THEN ROUND(sum(pgsize)/1073741824.0, 2) || ' GB'                            WHEN sum(pgsize) >= 1048576 THEN ROUND(sum(pgsize)/1048576.0, 2) || ' MB'                            WHEN sum(pgsize) >= 1024 THEN ROUND(sum(pgsize)/1024.0, 2) || ' KB'                            ELSE sum(pgsize) || ' bytes'                        END AS size                        FROM dbstat                        GROUP BY name                        ORDER BY sum(pgsize) DESC"
+ "SQLiteManager"
+ "\\b(iWork|freeform|Xcode)\\b"
+ "^[0-9A-Z]{10}\\."
+ "arrayWithCapacity:"
+ "cert"
+ "componentsJoinedByString:"
+ "count"
+ "executeQuery:onDatabaseAtPath:"
+ "firstMatchInString:options:range:"
+ "firstObject"
+ "genp"
+ "getSFACollectionForCollection:reply:"
+ "inet"
+ "intValue"
+ "keys"
+ "localizedDescription"
+ "null"
+ "objectAtIndexedSubscript:"
+ "regularExpressionWithPattern:options:error:"
+ "setSFACollection:forTopic:reply:"
+ "stringWithUTF8String:"
+ "subarrayWithRange:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"

```
