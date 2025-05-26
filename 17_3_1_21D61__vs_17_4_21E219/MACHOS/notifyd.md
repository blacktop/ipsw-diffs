## notifyd

> `/usr/sbin/notifyd`

```diff

-317.0.0.0.0
-  __TEXT.__text: 0xaff4
+317.100.2.0.0
+  __TEXT.__text: 0xb4c0
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1a88
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x1afd
   __TEXT.__unwind_info: 0x48
   __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x78

   __DATA.__bss: 0x2c8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 130
+  Functions: 135
   Symbols:   163
-  CStrings:  274
+  CStrings:  281
 
CStrings:
+ "\n"
+ "-- END --\n"
+ "_nc_table_delete"
+ "_nc_table_delete_64"
+ "_nc_table_delete_n"
+ "os_set_delete(&t->set, key) == expected"
+ "table.c"

```
