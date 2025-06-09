## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

-1521.120.4.0.0
-  __TEXT.__text: 0x3b838
-  __TEXT.__auth_stubs: 0xbd0
+1542.0.2.0.0
+  __TEXT.__text: 0x3be04
+  __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x740
-  __TEXT.__cstring: 0x600a
-  __TEXT.__unwind_info: 0xda0
+  __TEXT.__const: 0x730
+  __TEXT.__cstring: 0x6115
+  __TEXT.__unwind_info: 0xdb8
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9
   __TEXT.__objc_methtype: 0x118
   __TEXT.__objc_stubs: 0x1e0
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__const: 0xc78
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_nlclslist: 0xb8
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x608
   __AUTH_CONST.__const: 0x10c68
   __AUTH_CONST.__objc_const: 0x1f00
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__common: 0x18
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xd50

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 395DA84F-715D-334E-8D41-A16CD93FC83C
-  Functions: 1360
-  Symbols:   3829
-  CStrings:  622
+  UUID: CD7FE92D-4D9D-32A5-A120-4141AF3240FB
+  Functions: 1369
+  Symbols:   3844
+  CStrings:  627
 
Symbols:
+ __dispatch_deferred_items_cleanup.cold.1
+ __dispatch_free_deferred_unotes
+ __dispatch_free_deferred_unotes.cold.1
+ __dispatch_unote_dispose_defer
+ __dispatch_unote_dispose_defer.cold.1
+ _dispatch_queue_get_threadid_4wdt
+ _dispatch_verify_current_queue_4swiftonly
+ _dispatch_verify_current_queue_4swiftonly.cold.1
+ _os_workgroup_interval_data_set_complexity
+ _pthread_from_mach_thread_np
+ _pthread_threadid_np
+ _voucher_activity_get_logging_preferences_with_port
+ _voucher_copy_with_persona_mach_voucher_and_error
- _OUTLINED_FUNCTION_14
- __dispatch_event_update_all_deferred
CStrings:
+ "BUG IN CLIENT OF LIBDISPATCH: invalid queue passed to dispatch_am_i_on_queue_4swiftonly()"
+ "BUG IN LIBDISPATCH: Disposing a direct unote while deferring an event"
+ "BUG IN LIBDISPATCH: Too many defer-free unotes"
+ "com.apple.backboardd.displaythread"
+ "com.apple.backboardd.hid"

```
