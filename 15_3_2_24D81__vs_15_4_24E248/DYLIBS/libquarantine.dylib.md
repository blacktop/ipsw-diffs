## libquarantine.dylib

> `/usr/lib/system/libquarantine.dylib`

```diff

-181.80.2.0.0
-  __TEXT.__text: 0x2270
+181.100.13.0.0
+  __TEXT.__text: 0x2264
   __TEXT.__auth_stubs: 0x210
-  __TEXT.__const: 0x6f
+  __TEXT.__const: 0x77
   __TEXT.__cstring: 0x114
   __TEXT.__unwind_info: 0x148
   __DATA_CONST.__got: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 90D46A44-087C-3900-8509-EA90C6CFAD58
-  Functions: 100
-  Symbols:   146
+  UUID: BDFA4A83-BBE1-31F1-A27D-C433CF12BE54
+  Functions: 101
+  Symbols:   147
   CStrings:  19
 
Symbols:
+ qtn_spawnattrs_alloc.cold.1
Functions:
~ _unparse_label : 276 -> 272
~ _macsafestring_decode : 248 -> 252
~ _responsibility_get_responsible_for_pid : 72 -> 64
~ __qtn_file_clone : 84 -> 96
~ __qtn_proc_set_tracking_data : 56 -> 60
~ __qtn_proc_init_with_data : 416 -> 408
~ _qtn_spawnattrs_alloc : 256 -> 240
~ _responsibility_get_attribution_for_audittoken : 964 -> 948

```
