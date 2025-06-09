## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-1521.120.4.0.0
-  __TEXT.__text: 0x425a4
-  __TEXT.__auth_stubs: 0xcf0
+1542.0.2.0.0
+  __TEXT.__text: 0x42b3c
+  __TEXT.__auth_stubs: 0xd00
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x810
-  __TEXT.__cstring: 0x62ed
-  __TEXT.__unwind_info: 0xe58
+  __TEXT.__const: 0x800
+  __TEXT.__cstring: 0x63f8
+  __TEXT.__unwind_info: 0xe78
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x688
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0x10c98
   __AUTH_CONST.__objc_const: 0x1f00
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0xe0
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xd50

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 9CCEB404-956D-368A-97CA-064E0EE51BB4
-  Functions: 1441
-  Symbols:   2552
-  CStrings:  634
+  UUID: 74F7BC81-C9FA-352C-BD49-7311EA31B8E4
+  Functions: 1450
+  Symbols:   2562
+  CStrings:  639
 
Symbols:
+ __dispatch_free_deferred_unotes
+ __dispatch_unote_dispose_defer
+ _dispatch_deferred_items_cleanup.cold.1
+ _dispatch_free_deferred_unotes.cold.1
+ _dispatch_queue_get_threadid_4wdt
+ _dispatch_unote_dispose_defer.cold.1
+ _dispatch_verify_current_queue_4swiftonly
+ _os_workgroup_interval_data_set_complexity
+ _pthread_threadid_np
+ _voucher_activity_get_logging_preferences_with_port
+ _voucher_copy_with_persona_mach_voucher_and_error
+ dispatch_verify_current_queue_4swiftonly.cold.1
- _OUTLINED_FUNCTION_31
- __dispatch_event_update_all_deferred
CStrings:
+ "BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()"
+ "BUG IN LIBDISPATCH: Disposing a direct unote while deferring an event"
+ "BUG IN LIBDISPATCH: Too many defer-free unotes"
+ "com.apple.backboardd.displaythread"
+ "com.apple.backboardd.hid"

```
