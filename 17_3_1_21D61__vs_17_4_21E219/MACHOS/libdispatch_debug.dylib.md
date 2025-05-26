## libdispatch_debug.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_debug.dylib`

```diff

-1462.80.1.0.0
-  __TEXT.__text: 0xcb00c
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__const: 0x548
-  __TEXT.__cstring: 0x8547
-  __TEXT.__dof_dispatch: 0x2ae0
+1477.100.9.0.0
+  __TEXT.__text: 0xca654
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__const: 0x550
+  __TEXT.__cstring: 0x857a
+  __TEXT.__dof_dispatch: 0x2902
   __TEXT.__dof_voucher: 0x940
-  __TEXT.__unwind_info: 0xa64
+  __TEXT.__unwind_info: 0xa78
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x6a0
-  __AUTH_CONST.__const: 0x11958
-  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__const: 0x11998
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__data: 0xb00
   __DATA.__data: 0x288
   __DATA.__crash_info: 0x40

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  Functions: 1284
-  Symbols:   1713
-  CStrings:  764
+  Functions: 1291
+  Symbols:   1723
+  CStrings:  766
 
Symbols:
+ __dispatch_apply_invoke3
+ __dispatch_no_op
+ __dispatch_source_type_exclaves_notification
+ __dispatch_workloop_activate_tg_unsupported_fallback
+ __os_objc_alloc
+ __os_object_alloc_bridged
+ __os_workgroup_get_backing_workinterval
+ __pthread_workqueue_allow_send_signals
+ _dispatch_allow_send_signals
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _malloc_type_posix_memalign
+ _malloc_type_realloc
+ _pthread_attr_setworkinterval_np
- _calloc
- _malloc
- _posix_memalign
- _realloc
CStrings:
+ "EVFILT_EXCLAVES_NOTIFICATION"
+ "exclaves_notification"

```
