## libsqlite3.dylib

> `/usr/lib/libsqlite3.dylib`

```diff

-405.0.0.0.0
-  __TEXT.__text: 0x19fd10
+406.0.0.0.0
+  __TEXT.__text: 0x19fee0
   __TEXT.__const: 0x876c
-  __TEXT.__cstring: 0xcf1b
-  __TEXT.__oslogstring: 0x7c0
+  __TEXT.__cstring: 0xcf66
+  __TEXT.__oslogstring: 0x835
   __TEXT.__unwind_info: 0x1e28
   __TEXT.__eh_frame: 0x48
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   Functions: 2535
   Symbols:   607
-  CStrings:  2397
+  CStrings:  2402
 
Functions:
~ sub_19ea6ef98 -> sub_19e20ff98 : 44392 -> 44396
~ sub_19ea8d4d8 -> sub_19e22e4dc : 9376 -> 9372
~ _sqlite3_next_stmt : 284 -> 280
~ sub_19eaa32b8 -> sub_19e2442b4 : 980 -> 976
~ sub_19eaa368c -> sub_19e244684 : 520 -> 516
~ sub_19eac51cc -> sub_19e2661c0 : 924 -> 1300
~ _sqlite3_db_config : 896 -> 900
~ sub_19eaea304 -> sub_19e28b474 : 100 -> 180
~ sub_19eaec8a0 -> sub_19e28da60 : 800 -> 804
~ sub_19eaf0d6c -> sub_19e291f30 : 984 -> 988
~ sub_19eaf1f54 -> sub_19e29311c : 572 -> 576
~ sub_19eafea84 -> sub_19e29fc50 : 728 -> 724
~ sub_19eaff05c -> sub_19e2a0224 : 564 -> 568
~ sub_19ebd8284 -> sub_19e379450 : 940 -> 944
CStrings:
+ "Error: %{errorMessage,public}s coalition: %{coalition,public}s database: %{database,public}s query: %{query,public}s"
+ "SetStoreUpdateService"
+ "biomesyncd"
+ "hybridsearchd"
+ "spotlightknowledged.updater"
```
