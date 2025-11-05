## BiomeFlexibleStorage

> `/System/Library/PrivateFrameworks/BiomeFlexibleStorage.framework/Versions/A/BiomeFlexibleStorage`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x12040
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x155c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x20af
+166.17.1.0.0
+  __TEXT.__text: 0x12214
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_methlist: 0x18f4
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x2099
   __TEXT.__oslogstring: 0xb25
   __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__dlopen_cstrs: 0xac
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__unwind_info: 0x588
   __TEXT.__objc_classname: 0x23b
   __TEXT.__objc_methname: 0x3170
   __TEXT.__objc_methtype: 0x980

   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf10
+  __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3c0
   __AUTH_CONST.__const: 0x1f0
   __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x2820
+  __AUTH_CONST.__objc_const: 0x21d0
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x130
   __DATA.__data: 0x480

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A211D46E-20EF-3096-88B2-AF4B295B9135
-  Functions: 540
-  Symbols:   1382
-  CStrings:  1213
+  UUID: 642D5FEF-94B6-3C58-815E-9F0BFD412259
+  Functions: 547
+  Symbols:   1389
+  CStrings:  1202
 
Symbols:
+ +[_bmFMResultSet resultSetWithStatement:usingParentDatabase:shouldAutoClose:].cold.1
+ -[BMRemoteSQLStoreManager hasReadWriteAccessToURL:].cold.1
+ -[BMSQLStoreManager addManagedTable:derivedFromSource:].cold.1
+ -[BMSQLStoreManager beginManagedSessionWithEvent:].cold.1
+ -[BMSQLStoreManager deleteRowsDerivedFromEvent:].cold.1
+ -[_bmFMDatabase releaseSavePointWithName:error:].cold.1
+ -[_bmFMDatabase rollbackToSavePointWithName:error:].cold.1
+ -[_bmFMDatabase setCachedStatement:forQuery:].cold.1
+ -[_bmFMDatabase startSavePointWithName:error:].cold.1
- _strcmp
CStrings:
- "C"
- "I"
- "S"
- "c"
- "f"
- "s"

```
