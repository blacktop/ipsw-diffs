## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64561.91.2.0.0
-  __TEXT.__text: 0x7b88
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x14a9
-  __TEXT.__unwind_info: 0x228
+64565.70.2.0.0
+  __TEXT.__text: 0x8b58
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__const: 0x138
+  __TEXT.__cstring: 0x1567
+  __TEXT.__unwind_info: 0x25c
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x310
-  __DATA.__data: 0xc4
-  __DATA.__bss: 0x38a8
-  __DATA.__common: 0x10
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__auth_got: 0x340
+  __AUTH.__data: 0x88
+  __DATA.__data: 0x5c
+  __DATA.__bss: 0x38d0
+  __DATA.__common: 0x88
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 148
-  Symbols:   386
-  CStrings:  111
+  Functions: 179
+  Symbols:   460
+  CStrings:  114
 
Symbols:
+ _active_lite_zone
+ _add_stack_to_ptr.num_mallocs
+ _legacy_create_and_insert_lite_zone
+ _legacy_lite_is_enabled_on_current_thread
+ _legacy_malloc_msl_lite_hooks
+ _legacy_msl_lite_block_size
+ _legacy_stack_logging_lite_batch_free
+ _legacy_stack_logging_lite_batch_malloc
+ _legacy_stack_logging_lite_calloc
+ _legacy_stack_logging_lite_free
+ _legacy_stack_logging_lite_free_definite_size
+ _legacy_stack_logging_lite_malloc
+ _legacy_stack_logging_lite_memalign
+ _legacy_stack_logging_lite_realloc
+ _legacy_stack_logging_lite_size
+ _legacy_stack_logging_lite_valloc
+ _lite_helper_zone
+ _malloc_create_zone
+ _malloc_destroy_zone
+ _malloc_set_zone_name
+ _malloc_zone_register
+ _malloc_zone_unregister
+ _max_lite_mallocs
+ _mprotect
+ _msl_get_lite_wrapped_zone
+ _stack_logging_lite_claimed_address
+ _stack_logging_lite_destroy
+ _stack_logging_lite_introspect_check
+ _stack_logging_lite_introspect_enumerator
+ _stack_logging_lite_introspect_force_lock
+ _stack_logging_lite_introspect_force_unlock
+ _stack_logging_lite_introspect_good_size
+ _stack_logging_lite_introspect_log
+ _stack_logging_lite_introspect_print
+ _stack_logging_lite_introspect_print_task
+ _stack_logging_lite_introspect_reinit_lock
+ _stack_logging_lite_introspect_statistics
+ _stack_logging_lite_introspect_task_statistics
+ _stack_logging_lite_introspect_zone_locked
+ _stack_logging_lite_pressure_relief
+ _stack_logging_lite_zone_introspect
+ _uniquing_table_initialize.process_wide_generation
CStrings:
+ "MallocStackLoggingLiteZone_Wrapper"
+ "MallocStackLoggingLiteZone_Wrapper (empty))\n"
+ "PROC_LIMIT_WARN mode: Too many allocations have been tracked by lite stack logging. Disabling stack logging.\n"

```
