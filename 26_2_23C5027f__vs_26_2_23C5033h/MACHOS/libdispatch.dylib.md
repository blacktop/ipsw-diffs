## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

 1542.0.4.0.0
-  __TEXT.__text: 0x42b50
+  __TEXT.__text: 0x42b18
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x800

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 2E3FFC56-25C3-3A25-ABB0-4DFE3EE72BF5
-  Functions: 1452
-  Symbols:   2564
+  UUID: 2CF9D5CC-EBCA-334F-B8AD-DBD3C10EB430
+  Functions: 1453
+  Symbols:   2565
   CStrings:  639
 
Symbols:
+ _OUTLINED_FUNCTION_31
Functions:
~ _OUTLINED_FUNCTION_17 : 24 -> 16
~ _OUTLINED_FUNCTION_18 : 12 -> 24
~ _OUTLINED_FUNCTION_23 : 20 -> 12
~ _OUTLINED_FUNCTION_27 : 12 -> 20
~ _OUTLINED_FUNCTION_29 : 32 -> 12
+ _OUTLINED_FUNCTION_31
~ _OUTLINED_FUNCTION_3 : 16 -> 20
~ _OUTLINED_FUNCTION_6 : 12 -> 16
~ _OUTLINED_FUNCTION_7 : 24 -> 12
~ _OUTLINED_FUNCTION_8 : 28 -> 24
~ _OUTLINED_FUNCTION_9 : 20 -> 28
~ __dispatch_last_resort_autorelease_pool_push : 56 -> 52
~ __dispatch_last_resort_autorelease_pool_pop : 60 -> 56
~ _dispatch_once_wait.cold.1 : 212 -> 208
~ dispatch_assert_queue_barrier.cold.1 : 36 -> 40
~ _dispatch_queue_compute_priority_and_wlh.cold.1 : 128 -> 120
~ _dispatch_lane_legacy_set_target_queue.cold.1 : 96 -> 88
~ _dispatch_workloop_wakeup.cold.2 : 120 -> 116
~ _dispatch_workloop_invoke.cold.2 : 48 -> 44
~ _dispatch_mgr_queue_push.cold.1 : 108 -> 112
~ _dispatch_root_queue_drain_deferred_wlh.cold.5 : 80 -> 76
~ __dispatch_mach_handoff_set_wlh : 296 -> 284
~ _dispatch_event_loop_drain_timers.cold.4 : 72 -> 68
~ __dispatch_io_create_with_path_block_invoke.cold.3 : 100 -> 80
~ _dispatch_data_get_flattened_bytes_4libxpc : 164 -> 160

```
