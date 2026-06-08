## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64575.70.1.0.0
-  __TEXT.__text: 0x9248
-  __TEXT.__auth_stubs: 0x730
+64578.81.1.0.0
+  __TEXT.__text: 0x92e4
   __TEXT.__const: 0x148
   __TEXT.__cstring: 0x2107
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__got: 0x50
+  __TEXT.__unwind_info: 0x280
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x98
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x398
   __AUTH.__data: 0x88
   __DATA.__data: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: 707ADC83-0F86-3D18-845D-47FADFBF85AC
-  Functions: 234
-  Symbols:   602
+  UUID: 37B91EC4-C50D-3785-8BE9-2C94F5C403F9
+  Functions: 235
+  Symbols:   603
   CStrings:  213
 
Symbols:
+ _msl_current_timestamp
Functions:
~ _uniquing_table_unwind_stack_remote : 304 -> 308
~ _uniquing_table_create : 368 -> 372
~ _uniquing_table_stack_retain_internal : 2608 -> 2620
~ _flush_data : 560 -> 564
~ _update_cache_for_file_streams : 1308 -> 1316
~ _msl_payload_for_malloc_address_in_task_helper : 432 -> 440
~ _msl_disk_stack_logs_enumerate_from_task_with_block : 672 -> 668
~ _my_mkstemps : 500 -> 508
~ _reap_orphaned_log_files_in_hierarchy : 824 -> 828
~ _msl_payload_create : 204 -> 232
+ _msl_current_timestamp

```
