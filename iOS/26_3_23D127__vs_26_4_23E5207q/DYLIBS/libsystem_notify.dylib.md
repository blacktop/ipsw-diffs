## libsystem_notify.dylib

> `/usr/lib/system/libsystem_notify.dylib`

```diff

-344.0.1.0.0
-  __TEXT.__text: 0xa040
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0xc86
+348.100.6.502.1
+  __TEXT.__text: 0x9ff0
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__const: 0x120
+  __TEXT.__cstring: 0xc1e
   __TEXT.__dof_notify: 0x5a6
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x248
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0xa0
   __DATA.__data: 0x20
   __DATA.__crash_info: 0x148

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 9A76997B-117C-3FC6-ACB7-19C3ABEDDA6C
+  UUID: 7253CC00-A271-33B6-BD86-B00DB7EAF74F
   Functions: 89
-  Symbols:   133
-  CStrings:  87
+  Symbols:   135
+  CStrings:  82
 
Symbols:
+ __os_assert_log
+ __os_crash
Functions:
~ sub_29e5911d0 -> sub_2a5e321d0 : 1224 -> 1200
~ _notify_post : 2036 -> 2064
~ sub_29e5928d0 -> sub_2a5e338d4 : 324 -> 316
~ sub_29e5935cc -> sub_2a5e345c8 : 1836 -> 1828
~ sub_29e5949d8 -> sub_2a5e359cc : 1632 -> 1628
~ sub_29e595038 -> sub_2a5e36028 : 696 -> 692
~ sub_29e59615c -> sub_2a5e37148 : 76 -> 60
~ sub_29e596ea0 -> sub_2a5e37e7c : 148 -> 144
~ sub_29e596f34 -> sub_2a5e37f0c : 452 -> 420
~ sub_29e5970f8 -> sub_2a5e380b0 : 864 -> 860
~ sub_29e597544 -> sub_2a5e384f8 : 76 -> 60
~ sub_29e597590 -> sub_2a5e38534 : 260 -> 272
~ sub_29e598474 -> sub_2a5e39424 : 1300 -> 1308
~ _notify_register_signal : 1504 -> 1500
~ _notify_register_file_descriptor : 1724 -> 1720
CStrings:
- "_nc_table_delete"
- "_nc_table_delete_64"
- "_nc_table_delete_n"
- "os_set_delete(&t->set, key) == expected"
- "table.c"

```
