## PowerlogDatabaseReader

> `/System/Library/PrivateFrameworks/PowerlogDatabaseReader.framework/PowerlogDatabaseReader`

```diff

-3031.122.1.0.0
-  __TEXT.__text: 0xa7c
-  __TEXT.__auth_stubs: 0x250
+3468.0.0.502.1
+  __TEXT.__text: 0xa28
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x251
   __TEXT.__unwind_info: 0x88
-  __TEXT.__objc_classname: 0x11
-  __TEXT.__objc_methname: 0x1cc
-  __TEXT.__objc_methtype: 0x7d
-  __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x130
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4217F41C-854D-36C7-AFC8-27A732640194
+  UUID: B135CF20-892F-3B38-A768-F5C8F7E6527C
   Functions: 9
-  Symbols:   96
-  CStrings:  77
+  Symbols:   98
+  CStrings:  41
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x21
+ _objc_release_x27
+ _objc_retain_x2
+ _objc_retain_x21
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
Functions:
~ -[PLDatabaseReader prepareStatementAndPerformWithString:] : 208 -> 204
~ -[PLDatabaseReader performStatement:] : 788 -> 748
~ -[PLDatabaseReader tableNamesFromDatabase] : 264 -> 248
~ -[PLDatabaseReader stringValueOfTable:] : 952 -> 928
CStrings:
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^{sqlite3_stmt=}16"
- "PLDatabaseReader"
- "T^{sqlite3=},V_dbConnection"
- "UTF8String"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "^{sqlite3=}24@0:8@16"
- "_dbConnection"
- "addObject:"
- "appendFormat:"
- "appendString:"
- "array"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dbConnection"
- "dealloc"
- "init"
- "initWithDatabaseFile:"
- "null"
- "numberWithDouble:"
- "numberWithLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "openDatabaseFile:"
- "performStatement:"
- "prepareStatementAndPerformWithString:"
- "setDbConnection:"
- "string"
- "stringValueOfTable:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "tableNamesFromDatabase"
- "v16@0:8"
- "v24@0:8^{sqlite3=}16"

```
