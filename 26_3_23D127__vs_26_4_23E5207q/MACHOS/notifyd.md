## notifyd

> `/usr/sbin/notifyd`

```diff

-344.0.1.0.0
-  __TEXT.__text: 0xb4f4
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x1bf5
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x78
+348.100.6.502.1
+  __TEXT.__text: 0xb2b0
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0x1b94
+  __DATA_CONST.__auth_got: 0x498
+  __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xb30
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2c8
+  __DATA.__bss: 0x2d0
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 8E516451-27B4-317E-B8DF-BE12148505F0
-  Functions: 135
-  Symbols:   168
-  CStrings:  284
+  UUID: 6FB3209A-7170-3F06-B032-156334E5EEB1
+  Functions: 134
+  Symbols:   164
+  CStrings:  279
 
Symbols:
+ __os_assert_log
+ __os_crash
- _gL1CacheEnabled
- _getgroups
- _getpwuid
- _initgroups
- _pthread_setugid_np
- _syscall
CStrings:
+ "--- NAME COUNT %zu ---\n"
+ "--- PRIVATE SERVICE COUNT %zu ---\n"
+ "--- PUBLIC SERVICE COUNT %zu ---\n"
+ "--- SUBSCRIPTION COUNT %zu ---\n"
+ "_port_proc_cancel_client"
+ "port count   %zu\n"
+ "proc count   %zu\n"
- "--- NAME COUNT %u ---\n"
- "--- PRIVATE SERVICE COUNT %u ---\n"
- "--- PUBLIC SERVICE COUNT %u ---\n"
- "--- SUBSCRIPTION COUNT %u ---\n"
- "_nc_table_delete"
- "_nc_table_delete_64"
- "_nc_table_delete_n"
- "os_set_delete(&t->set, key) == expected"
- "port count   %u\n"
- "port_proc_cancel_client"
- "proc count   %u\n"
- "table.c"

```
