## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-1462.80.1.0.0
-  __TEXT.__text: 0x431cc
-  __TEXT.__auth_stubs: 0xd10
+1477.100.9.0.0
+  __TEXT.__text: 0x434a8
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_methlist: 0x57c
-  __TEXT.__const: 0x7a0
-  __TEXT.__cstring: 0x60f7
+  __TEXT.__const: 0x7d0
+  __TEXT.__cstring: 0x612a
   __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__unwind_info: 0xd64
-  __TEXT.__objc_classname: 0x470
-  __TEXT.__objc_methname: 0x2a6
+  __TEXT.__unwind_info: 0xd7c
+  __TEXT.__objc_classname: 0x499
+  __TEXT.__objc_methname: 0x2ba
   __TEXT.__objc_methtype: 0x118
   __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x116e8
+  __DATA_CONST.__const: 0x11730
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_nlclslist: 0xb8
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20d0
+  __DATA_CONST.__objc_const: 0x20f0
   __DATA_CONST.__objc_selrefs: 0xd8
-  __DATA.__objc_classrefs: 0x8
-  __DATA.__objc_superrefs: 0xe8
-  __DATA.__data: 0x11c0
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA.__data: 0x1220
   __DATA.__crash_info: 0x40
   __DATA.__common: 0xe0
   __DATA.__bss: 0x88

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 75237D6A-FD17-319B-B34C-191A3896E6F5
-  Functions: 1584
-  Symbols:   2390
-  CStrings:  622
+  UUID: 81C1EA12-B653-342E-9431-B633ECC199F9
+  Functions: 1599
+  Symbols:   2411
+  CStrings:  626
 
Symbols:
+ GCC_except_table88
+ __OBJC_$_PROTOCOL_REFS_OS_dispatch_source_exclaves_notification
+ __OBJC_LABEL_PROTOCOL_$_OS_dispatch_source_exclaves_notification
+ __OBJC_PROTOCOL_$_OS_dispatch_source_exclaves_notification
+ __dispatch_apply_invoke3
+ __dispatch_no_op
+ __dispatch_object_alloc_bridged
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
+ _pthread_attr_setworkinterval_np
- GCC_except_table83
- _dispatch_workloop_activate.cold.1
CStrings:
+ "EVFILT_EXCLAVES_NOTIFICATION"
+ "OS_dispatch_source_exclaves_notification"
+ "T@\"NSString\",?,R,C"
+ "exclaves_notification"

```
