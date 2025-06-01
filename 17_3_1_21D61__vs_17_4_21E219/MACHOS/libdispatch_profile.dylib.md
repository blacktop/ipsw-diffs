## libdispatch_profile.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

```diff

-1462.80.1.0.0
-  __TEXT.__text: 0x4949c
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__const: 0x720
-  __TEXT.__cstring: 0x60d4
-  __TEXT.__dof_dispatch: 0x3398
+1477.100.9.0.0
+  __TEXT.__text: 0x49658
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__const: 0x750
+  __TEXT.__cstring: 0x6107
+  __TEXT.__dof_dispatch: 0x31ba
   __TEXT.__dof_voucher: 0x2aa5
-  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__unwind_info: 0xbec
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x6d8
-  __AUTH_CONST.__const: 0x11958
-  __AUTH_CONST.__auth_got: 0x580
+  __DATA_CONST.__const: 0x6e0
+  __AUTH_CONST.__const: 0x11998
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH.__data: 0xb00
   __DATA.__data: 0x290
   __DATA.__crash_info: 0x40

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: 816E379E-8796-3D8D-A75D-AC537581FAC1
-  Functions: 1488
-  Symbols:   1915
-  CStrings:  497
+  UUID: 120719A4-FF1C-3D70-9538-861D58B0F141
+  Functions: 1502
+  Symbols:   1932
+  CStrings:  499
 
Symbols:
+ __dispatch_apply_invoke3
+ __dispatch_no_op
+ __dispatch_source_type_exclaves_notification
+ __dispatch_workloop_activate_simulator_fallback
+ __os_object_alloc_bridged
+ __os_workgroup_get_backing_workinterval
+ __pthread_workqueue_allow_send_signals
+ _dispatch_allow_send_signals
+ _dispatch_event_loop_cancel_waiter.cold.4
+ _dispatch_event_loop_end_ownership.cold.6
+ _dispatch_event_loop_ensure_ownership.cold.4
+ _dispatch_event_loop_leave_immediate.cold.4
+ _dispatch_event_loop_wait_for_ownership.cold.6
+ _dispatch_event_loop_wake_owner.cold.5
+ _dispatch_group_create_and_enter.cold.1
+ _dispatch_workloop_activate_simulator_fallback.cold.1
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _malloc_type_posix_memalign
+ _malloc_type_realloc
+ _pthread_attr_setworkinterval_np
- _calloc
- _dispatch_workloop_activate.cold.1
- _malloc
- _posix_memalign
- _realloc
CStrings:
+ "EVFILT_EXCLAVES_NOTIFICATION"
+ "exclaves_notification"

```
