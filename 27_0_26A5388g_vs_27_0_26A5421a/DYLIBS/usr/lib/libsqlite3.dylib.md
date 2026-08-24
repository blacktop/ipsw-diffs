## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x1e14d4
+406.0.0.0.0
+  __TEXT.__text: 0x1e16ac
   __TEXT.__const: 0x873c
-  __TEXT.__cstring: 0xce51
-  __TEXT.__oslogstring: 0x7c0
+  __TEXT.__cstring: 0xce9c
+  __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x1e60
   __TEXT.__eh_frame: 0x88
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   Functions: 2536
   Symbols:   2933
-  CStrings:  2389
+  CStrings:  2394
 
Functions:
~ _sqlite3VdbeExec : 52552 -> 52556
~ _balance : 10292 -> 10288
~ _sqlite3_next_stmt : 308 -> 304
~ _defragmentPage : 980 -> 976
~ _ptrmapPut : 520 -> 516
~ _sqlite3ErrorMsg : 1396 -> 1780
~ _sqlite3_db_config : 904 -> 908
~ ___appendOnePathElement_block_invoke : 112 -> 192
~ _getPageNormal : 876 -> 880
~ _incrVacuumStep : 1136 -> 1140
~ _modifyPagePointer : 612 -> 616
~ _freeSpace : 728 -> 724
~ _rebuildPage : 564 -> 568
~ _sessionReadRecord : 1148 -> 1152
CStrings:
+ "Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s"
+ "SetStoreUpdateService"
+ "biomesyncd"
+ "hybridsearchd"
+ "spotlightknowledged.updater"
```
