## libtclsqlite3.dylib

> `/System/Library/Tcl/sqlite3/libtclsqlite3.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x105100
+406.0.0.0.0
+  __TEXT.__text: 0x1051d0
   __TEXT.__auth_stubs: 0xf10
-  __TEXT.__const: 0x9358
-  __TEXT.__cstring: 0xd2ac
-  __TEXT.__oslogstring: 0x7c0
+  __TEXT.__const: 0x9368
+  __TEXT.__cstring: 0xd2f7
+  __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x2188
   __DATA_CONST.__const: 0x3588
   __DATA_CONST.__auth_got: 0x788

   - /usr/lib/libSystem.B.dylib
   Functions: 2788
   Symbols:   3334
-  CStrings:  2425
+  CStrings:  2430
 
Functions:
~ _sqlite3SafetyCheckOk : 104 -> 128
~ _sqlite3_next_stmt : 188 -> 184
~ _sqlite3ErrorMsg : 672 -> 772
~ _sqlite3_db_config : 620 -> 624
~ ___appendOnePathElement_block_invoke : 100 -> 180
~ _getPageNormal : 652 -> 656
~ _incrVacuumStep : 776 -> 780
~ _ptrmapPut : 404 -> 400
~ _modifyPagePointer : 568 -> 572
~ _sqlite3VdbeExec : 33280 -> 33284
~ _balance : 6132 -> 6128
~ _freeSpace : 708 -> 704
~ _defragmentPage : 976 -> 972
~ _rebuildPage : 564 -> 568
CStrings:
+ "Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s"
+ "SetStoreUpdateService"
+ "biomesyncd"
+ "hybridsearchd"
+ "spotlightknowledged.updater"
```
