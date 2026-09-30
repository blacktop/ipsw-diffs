## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64570.58.1.0.0
-  __TEXT.__text: 0x912c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x1f69
-  __TEXT.__unwind_info: 0x278
+64572.120.2.0.0
+  __TEXT.__text: 0x9140
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x1f73
+  __TEXT.__unwind_info: 0x270
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH.__data: 0x88
   __DATA.__data: 0x8
   __DATA.__bss: 0x3100

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: D87A8EDB-91F9-394B-9789-A0609B4C055D
-  Functions: 229
-  Symbols:   584
-  CStrings:  206
+  UUID: E3D59629-3816-3833-810C-F5212C3545D8
+  Functions: 228
+  Symbols:   582
+  CStrings:  207
 
Symbols:
+ _MSL_EnableAtLimitWarning_Envvar
- _proc_pidinfo
- _processIsEligibleForMemoryPressureMSLEnablement
Functions:
~ _msl_set_flags_from_environment : 368 -> 448
~ _initialize_no_footprint_for_debug_flag : 128 -> 148
~ _msl_handle_memory_event : 628 -> 640
- _processIsEligibleForMemoryPressureMSLEnablement
~ ___disk_stack_logging_log_stack : 1032 -> 1040
~ _update_cache_for_file_streams : 1248 -> 1256
~ _msl_disk_stack_logs_enumerate_from_buffer : 240 -> 244
~ _msl_disk_stack_logs_enumerate_from_task_with_block : 672 -> 680
~ _open_log_file_at_path : 140 -> 148
CStrings:
+ "could not tag MSL-related memory as no_footprint, so those pages will be included in process footprint - %s (%d)\n"
+ "full"
- "could not tag MSL-related memory as no_footprint, so those pages will be included in process footprint - %s\n"

```
