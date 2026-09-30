## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-1542.0.4.0.0
-  __TEXT.__text: 0x42b18
+1542.100.32.0.0
+  __TEXT.__text: 0x42d88
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x800
-  __TEXT.__cstring: 0x63f8
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__const: 0x830
+  __TEXT.__cstring: 0x646c
+  __TEXT.__unwind_info: 0xe60
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9

   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x698
-  __AUTH_CONST.__const: 0x10c98
+  __AUTH_CONST.__const: 0x10ce8
   __AUTH_CONST.__objc_const: 0x1f00
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0xe0
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
-  UUID: 618E669F-4AD9-38EB-972D-7EECE089B14C
-  Functions: 1453
-  Symbols:   2565
-  CStrings:  639
+  UUID: 4E13F035-6A7A-35C8-9817-DD3ACBBA197E
+  Functions: 1474
+  Symbols:   2594
+  CStrings:  642
 
Symbols:
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ __block_descriptor_tmp.4146
+ __block_descriptor_tmp.4150
+ __block_descriptor_tmp.4154
+ __block_literal_global.4148
+ __block_literal_global.4152
+ __block_literal_global.4156
+ __dispatch_free_deferred_items
+ __dispatch_mach_dealloc
+ __dispatch_source_dealloc
+ __dispatch_thread_bound_kqwl_count
+ __dispatch_thread_main_event_signal_slow
+ __dispatch_thread_main_event_wait_slow
+ __dispatch_unote_dealloc
+ _dispatch_event_loop_drain_timers.cold.5
+ _dispatch_event_loop_wait_for_ownership.cold.7
+ _dispatch_free_deferred_items.cold.1
+ _dispatch_free_deferred_items.cold.2
+ _dispatch_free_deferred_items.cold.3
+ _dispatch_kevent_mach_msg_recv.cold.6
+ _dispatch_main_queue_drain.cold.7
+ _dispatch_root_queue_drain.cold.6
+ _dispatch_runloop_root_queue_perform_4CF.cold.6
+ _dispatch_thread_main_event_signal_slow.cold.1
+ _dispatch_thread_main_event_wait_slow.cold.1
+ _dispatch_thread_main_event_wait_slow.cold.2
+ _dispatch_wait_compute_wlh.cold.3
+ _dispatch_wlh_cleanup.cold.2
+ _dispatch_workloop_dispose.cold.3
- __block_descriptor_tmp.4128
- __block_descriptor_tmp.4132
- __block_descriptor_tmp.4136
- __block_literal_global.4130
- __block_literal_global.4134
- __block_literal_global.4138
- __dispatch_free_deferred_unotes
- __dispatch_thread_bound_kqwl_enabled
- __dispatch_unote_dispose
- __dispatch_unote_dispose_defer
- __dispatch_workloop_bound_thread_init_once
- __dispatch_workloop_bound_thread_pred
- _dispatch_free_deferred_unotes.cold.1
- _dispatch_unote_dispose_defer.cold.1
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
