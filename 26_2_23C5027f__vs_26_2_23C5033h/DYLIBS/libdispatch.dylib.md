## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

 1542.0.4.0.0
-  __TEXT.__text: 0x3be18
+  __TEXT.__text: 0x3bdd8
   __TEXT.__auth_stubs: 0xc00
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x730

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 78DBB857-5D53-3C43-80D5-33E628C9225A
-  Functions: 1371
-  Symbols:   3848
+  UUID: 99D1B6C0-3652-3A0F-9012-2A06B2586651
+  Functions: 1372
+  Symbols:   3850
   CStrings:  627
 
Symbols:
+ _OUTLINED_FUNCTION_14
Functions:
~ _OUTLINED_FUNCTION_9 : 24 -> 16
~ _OUTLINED_FUNCTION_10 : 20 -> 24
~ _OUTLINED_FUNCTION_12 : 12 -> 20
+ _OUTLINED_FUNCTION_14
~ _OUTLINED_FUNCTION_3 : 16 -> 20
~ _OUTLINED_FUNCTION_6 : 12 -> 16
~ _OUTLINED_FUNCTION_7 : 24 -> 12
~ _OUTLINED_FUNCTION_8 : 28 -> 24
~ _OUTLINED_FUNCTION_9 : 20 -> 28
~ __dispatch_last_resort_autorelease_pool_push : 56 -> 52
~ __dispatch_last_resort_autorelease_pool_pop : 60 -> 56
~ __dispatch_once_wait.cold.1 : 212 -> 208
~ _dispatch_assert_queue_barrier.cold.1 : 36 -> 40
~ __dispatch_queue_compute_priority_and_wlh.cold.2 : 112 -> 104
~ __dispatch_lane_legacy_set_target_queue.cold.1 : 96 -> 88
~ __dispatch_workloop_wakeup.cold.2 : 80 -> 76
~ __dispatch_workloop_invoke.cold.5 : 48 -> 44
~ __dispatch_workloop_barrier_complete.cold.3 : 100 -> 96
~ __dispatch_root_queue_drain_deferred_wlh.cold.5 : 80 -> 76
~ __dispatch_mach_handoff_set_wlh : 296 -> 284
~ __dispatch_event_loop_drain_timers.cold.4 : 72 -> 68
~ ___dispatch_io_write_block_invoke.cold.2 : 100 -> 80
~ _dispatch_data_get_flattened_bytes_4libxpc : 164 -> 160

```
