## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

-1542.0.4.0.0
-  __TEXT.__text: 0x3bdd8
+1542.100.32.0.0
+  __TEXT.__text: 0x3c11c
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x730
-  __TEXT.__cstring: 0x6115
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__const: 0x760
+  __TEXT.__cstring: 0x6189
+  __TEXT.__unwind_info: 0xdb0
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9

   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x610
-  __AUTH_CONST.__const: 0x10c68
+  __AUTH_CONST.__const: 0x10cb8
   __AUTH_CONST.__objc_const: 0x1f00
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x18
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0xd50
+  __DATA_DIRTY.__objc_data: 0xdf8
   __DATA_DIRTY.__data: 0xc50
   __DATA_DIRTY.__common: 0x188
-  __DATA_DIRTY.__bss: 0x6c0
+  __DATA_DIRTY.__bss: 0x6b8
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 904D48A3-D99E-3962-BFA9-C3DFB66BBA83
-  Functions: 1372
-  Symbols:   3850
-  CStrings:  627
+  UUID: 3D5728FA-E526-35E7-A766-E8AA3BE35C3B
+  Functions: 1385
+  Symbols:   3893
+  CStrings:  630
 
Symbols:
+ ___block_descriptor_tmp.4146
+ ___block_descriptor_tmp.4150
+ ___block_descriptor_tmp.4154
+ ___block_literal_global.4148
+ ___block_literal_global.4152
+ ___block_literal_global.4156
+ __dispatch_event_loop_drain_timers.cold.5
+ __dispatch_event_loop_wait_for_ownership.cold.7
+ __dispatch_free_deferred_items
+ __dispatch_free_deferred_items.cold.1
+ __dispatch_free_deferred_items.cold.2
+ __dispatch_free_deferred_items.cold.3
+ __dispatch_kevent_mach_msg_recv.cold.6
+ __dispatch_mach_dealloc
+ __dispatch_main_queue_drain.cold.7
+ __dispatch_root_queue_drain.cold.5
+ __dispatch_runloop_root_queue_perform_4CF.cold.7
+ __dispatch_source_dealloc
+ __dispatch_thread_bound_kqwl_count
+ __dispatch_thread_main_event_signal_slow
+ __dispatch_thread_main_event_signal_slow.cold.1
+ __dispatch_thread_main_event_wait_slow
+ __dispatch_thread_main_event_wait_slow.cold.1
+ __dispatch_thread_main_event_wait_slow.cold.2
+ __dispatch_unote_dealloc
+ __dispatch_wait_compute_wlh.cold.3
+ __dispatch_wlh_cleanup.cold.2
+ __dispatch_workloop_dispose.cold.3
- _OUTLINED_FUNCTION_14
- ___block_descriptor_tmp.4128
- ___block_descriptor_tmp.4132
- ___block_descriptor_tmp.4136
- ___block_literal_global.4130
- ___block_literal_global.4134
- ___block_literal_global.4138
- __dispatch_free_deferred_unotes
- __dispatch_free_deferred_unotes.cold.1
- __dispatch_thread_bound_kqwl_enabled
- __dispatch_unote_dispose
- __dispatch_unote_dispose_defer
- __dispatch_unote_dispose_defer.cold.1
- __dispatch_workloop_bound_thread_init_once
- __dispatch_workloop_bound_thread_pred
CStrings:
+ "BUG IN CLIENT OF LIBDISPATCH: Bound thread attribute set multiple times"
+ "BUG IN LIBDISPATCH: Corrupt thread event value"
+ "BUG IN LIBDISPATCH: Too many deferred free items"
+ "BUG IN LIBDISPATCH: Underflow of tbkqwl count"
+ "BUG IN LIBDISPATCH: Unexpected __ulock_wait error"
+ "MallocStackLogging"
- "BUG IN LIBDISPATCH: Disposing a direct unote while deferring an event"
- "BUG IN LIBDISPATCH: Too many defer-free unotes"
- "kern.kern_event.thread_bound_kqwl_support_enabled"

```
