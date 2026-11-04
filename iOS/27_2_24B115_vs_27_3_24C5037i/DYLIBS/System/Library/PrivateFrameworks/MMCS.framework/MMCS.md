## MMCS

> `/System/Library/PrivateFrameworks/MMCS.framework/MMCS`

```diff

-2700.112.0.0.0
-  __TEXT.__text: 0x7e568
+2730.0.0.0.0
+  __TEXT.__text: 0x7f254
   __TEXT.__objc_methlist: 0xbe0
-  __TEXT.__const: 0x9ac
+  __TEXT.__const: 0x9bc
   __TEXT.__oslogstring: 0x442c
-  __TEXT.__cstring: 0x178c2
+  __TEXT.__cstring: 0x1797b
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__unwind_info: 0x20b8
+  __TEXT.__unwind_info: 0x2130
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5410
+  __DATA_CONST.__const: 0x5420
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x898
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__got: 0x2c8
-  __AUTH_CONST.__const: 0x2d88
+  __AUTH_CONST.__const: 0x2da0
   __AUTH_CONST.__cfstring: 0xce80
   __AUTH_CONST.__objc_const: 0x11f0
-  __AUTH_CONST.__auth_got: 0xe88
+  __AUTH_CONST.__auth_got: 0xed8
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x50
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__data: 0x988
+  __DATA_DIRTY.__data: 0x990
   __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2418
-  Symbols:   3310
-  CStrings:  2990
+  Functions: 2444
+  Symbols:   3345
+  CStrings:  2997
 
Symbols:
+ _CFRunLoopAddObserver
+ _CFRunLoopObserverCreate
+ _CFRunLoopRemoveObserver
+ _MMCSResetEngineInitializedState
+ __mmcs_compute_signature_and_register_item_with_descriptor
+ __mmcs_duplicate_registered_file
+ __mmcs_engine_append_requests_description
+ __mmcs_engine_cancel_requests_if_not_closing
+ __mmcs_engine_destroy_begin_closing
+ __mmcs_engine_is_active
+ __mmcs_engine_set_metrics_enabled
+ __mmcs_get_items
+ __mmcs_get_registered_items
+ __mmcs_put_items
+ __mmcs_put_section_with_items
+ __mmcs_register_files_with_options
+ __mmcs_register_items
+ __mmcs_registered_item_count
+ __mmcs_unregister_files_in_working_directory
+ __mmcs_update_items
+ _class_getSuperclass
+ _dispatch_async_f
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_sync_f
+ _mmcs_dispatch_queue_is_concurrent
+ _mmcs_perform_dispatch_serial_queue_key
+ _mmcs_perform_dispatch_target_async_f
+ _mmcs_perform_dispatch_target_is_current
+ _mmcs_perform_dispatch_target_queue_key
+ _mmcs_perform_dispatch_target_sync_f
+ _mmcs_perform_run_loop_async_f_fire
+ _mmcs_perform_run_loop_sync_f_trampoline
+ _mmcs_perform_run_loop_target_async_f
+ _mmcs_perform_run_loop_target_is_current
+ _mmcs_perform_run_loop_target_sync_f
+ _mmcs_perform_target_assert_current
+ _mmcs_perform_target_sync_f
+ _objc_getClass
+ _object_getClass
- _MMCSDuplicateRegisteredfile2
- _mmcs_perform_dispatch_target_assert_current_debug
- _mmcs_perform_dispatch_target_assert_not_current_debug
- _mmcs_perform_run_loop_target_assert_current_debug
- _mmcs_perform_run_loop_target_assert_not_current_debug
CStrings:
+ "OS_dispatch_queue_concurrent"
+ "_mmcs_get_items"
+ "_mmcs_register_items"
+ "_mmcs_update_items"
+ "function"
+ "mmcs_dispatch_queue_is_concurrent"
+ "mmcs_perform_target: current thread is not exclusively confined"
+ "mmcs_perform_target_sync_f"
+ "mmcs_util.m"
+ "target"
- "mmcs_get_items"
- "mmcs_register_items"
- "mmcs_update_items"
```
