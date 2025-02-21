## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-1504.60.7.0.0
-  __TEXT.__text: 0x42700
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x57c
-  __TEXT.__const: 0x7c0
-  __TEXT.__cstring: 0x628f
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__unwind_info: 0xd80
+1521.100.4.0.0
+  __TEXT.__text: 0x42468
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x684
+  __TEXT.__const: 0x810
+  __TEXT.__cstring: 0x62ed
+  __TEXT.__unwind_info: 0xe58
+  __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_classname: 0x499
   __TEXT.__objc_methname: 0x2b9
   __TEXT.__objc_methtype: 0x118

   __DATA_CONST.__objc_nlclslist: 0xb8
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x10c98
-  __AUTH_CONST.__objc_const: 0x20f0
+  __AUTH_CONST.__objc_const: 0x1f00
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
   __DATA.__crash_info: 0x40
   __DATA.__common: 0xe0
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xd50
   __DATA_DIRTY.__data: 0xc50
   __DATA_DIRTY.__common: 0x188
-  __DATA_DIRTY.__bss: 0x6b8
+  __DATA_DIRTY.__bss: 0x6c0
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  Functions: 1320
-  Symbols:   2392
-  CStrings:  634
+  Functions: 1440
+  Symbols:   2551
+  CStrings:  635
 
Symbols:
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ ___dispatch_fd_entry_create_with_fd_block_invoke.cold.1
+ ___dispatch_io_stop_block_invoke_2.cold.3
+ ___dispatch_noexcept_personality
+ ___dispatch_operation_deliver_data_block_invoke.cold.2
+ __destroy_helper_block_8_32c35_ZTS29dispatch_block_private_data_s.cold.1
+ __dispatch_build
+ __dispatch_build_pred
+ __dispatch_calloc_typed
+ __dispatch_io_create_with_path_block_invoke.cold.3
+ __dispatch_logv_pred
+ __dispatch_mgr_sched_qos2prio
+ __dispatch_timer_heap_shrink
+ _dispatch_apply_with_attr_f.cold.5
+ _dispatch_block_create.cold.1
+ _dispatch_block_create.cold.2
+ _dispatch_bug.db_last_seen
+ _dispatch_bug_deprecated.dbd_last_seen
+ _dispatch_bug_kevent_client.dbkc_last_seen_1
+ _dispatch_bug_kevent_client.dbkc_last_seen_2
+ _dispatch_bug_kevent_client.dbkc_last_seen_3
+ _dispatch_bug_kevent_vanished.dbkv_last_seen
+ _dispatch_bug_mach_client.dbmc_last_seen
+ _dispatch_channel_invoke.cold.10
+ _dispatch_channel_invoke.cold.11
+ _dispatch_channel_invoke.cold.12
+ _dispatch_channel_invoke.cold.7
+ _dispatch_channel_invoke.cold.8
+ _dispatch_channel_invoke.cold.9
+ _dispatch_continuation_alloc_from_heap.cold.1
+ _dispatch_disk_init.cold.2
+ _dispatch_event_loop_drain_timers.cold.3
+ _dispatch_event_loop_drain_timers.cold.4
+ _dispatch_event_loop_timer_arm.cold.1
+ _dispatch_fd_entry_cleanup_operations.cold.3
+ _dispatch_fd_entry_init_async.cold.1
+ _dispatch_get_mach_host_port.cold.1
+ _dispatch_get_main_queue_handle_4CF.cold.1
+ _dispatch_get_main_queue_port_4CF.cold.1
+ _dispatch_introspection_init.cold.1
+ _dispatch_introspection_init.cold.2
+ _dispatch_introspection_order_record.cold.1
+ _dispatch_introspection_queue_create.cold.1
+ _dispatch_introspection_queue_dispose.cold.1
+ _dispatch_introspection_thread_add.cold.1
+ _dispatch_introspection_thread_remove.cold.1
+ _dispatch_kevent_mach_msg_recv.cold.4
+ _dispatch_kevent_mach_msg_recv.cold.5
+ _dispatch_kevent_mach_notify_resume.cold.5
+ _dispatch_kevent_workqueue_init.cold.1
+ _dispatch_kevent_workqueue_init.cold.2
+ _dispatch_kq_init.cold.2
+ _dispatch_lane_dispose.cold.1
+ _dispatch_lane_legacy_set_target_queue.cold.3
+ _dispatch_log_disabled
+ _dispatch_log_file.cold.1
+ _dispatch_mach_host_notify_update.cold.2
+ _dispatch_mach_host_notify_update.cold.3
+ _dispatch_mach_merge_msg.cold.3
+ _dispatch_mach_merge_msg.cold.4
+ _dispatch_mach_msg_async_reply_wrap.cold.2
+ _dispatch_main_queue_drain.cold.6
+ _dispatch_mgr_queue_push.cold.2
+ _dispatch_operation_create.cold.4
+ _dispatch_operation_dispose.cold.2
+ _dispatch_operation_should_enqueue.cold.2
+ _dispatch_pthread_root_queue_create.cold.1
+ _dispatch_pthread_root_queue_dispose.cold.1
+ _dispatch_queue_atfork_child.cold.1
+ _dispatch_queue_compute_priority_and_wlh.cold.1
+ _dispatch_queue_compute_priority_and_wlh.cold.2
+ _dispatch_queue_invoke_finish.cold.1
+ _dispatch_root_queue_drain.cold.4
+ _dispatch_root_queue_drain.cold.5
+ _dispatch_root_queue_drain_deferred_item.cold.2
+ _dispatch_root_queue_drain_deferred_item.cold.3
+ _dispatch_root_queue_drain_deferred_wlh.cold.5
+ _dispatch_root_queues_init_once.cold.5
+ _dispatch_runloop_queue_dispose.cold.1
+ _dispatch_runloop_queue_handle_init.cold.2
+ _dispatch_runloop_root_queue_perform_4CF.cold.4
+ _dispatch_runloop_root_queue_perform_4CF.cold.5
+ _dispatch_sema4_create_slow.cold.7
+ _dispatch_source_activate.cold.2
+ _dispatch_source_dispose.cold.1
+ _dispatch_source_latch_and_call.cold.2
+ _dispatch_source_latch_and_call.cold.3
+ _dispatch_source_latch_and_call.cold.4
+ _dispatch_source_latch_and_call.cold.5
+ _dispatch_time_init.cold.1
+ _dispatch_unote_register.cold.1
+ _dispatch_wait_compute_wlh.cold.2
+ _dispatch_workloop_activate.cold.2
+ _dispatch_workloop_activate.cold.3
+ _dispatch_workloop_activate.cold.4
+ _dispatch_workloop_barrier_complete.cold.2
+ _dispatch_workloop_barrier_complete.cold.3
+ _dispatch_workloop_invoke.cold.10
+ _dispatch_workloop_invoke.cold.3
+ _dispatch_workloop_invoke.cold.4
+ _dispatch_workloop_invoke.cold.5
+ _dispatch_workloop_invoke.cold.6
+ _dispatch_workloop_invoke.cold.7
+ _dispatch_workloop_invoke.cold.8
+ _dispatch_workloop_invoke.cold.9
+ _dispatch_workloop_wakeup.cold.3
+ _dispatch_workloop_wakeup.cold.4
+ _os_workgroup_lookup_type_from_workload_id.cold.2
+ _voucher_atfork_prepare.cold.1
+ _voucher_find_and_retain.cold.2
+ _voucher_get_mach_voucher.cold.1
+ _voucher_insert.cold.4
+ _voucher_process_can_use_arbitrary_personas_init.cold.2
+ _voucher_xref_dispose.cold.3
+ dispatch_apply_attr_query.cold.5
+ dispatch_assert_queue$V2.cold.2
+ dispatch_assert_queue_barrier.cold.1
+ dispatch_group_notify.cold.3
+ dispatch_io_barrier.cold.2
+ dispatch_io_close.cold.3
+ dispatch_io_close.cold.4
+ dispatch_io_set_high_water.cold.2
+ dispatch_io_set_interval.cold.2
+ dispatch_io_set_low_water.cold.2
+ dispatch_source_cancel.cold.2
+ dispatch_source_cancel_and_wait.cold.5
+ dispatch_source_cancel_and_wait.cold.6
+ dispatch_source_merge_data.cold.2
+ dispatch_workloop_set_uses_bound_thread.cold.2
+ firehose_buffer_tracepoint_reserve_slow.cold.1
+ voucher_activity_create_with_data_2.cold.2
+ voucher_activity_flush.cold.2
+ voucher_activity_get_logging_preferences.cold.1
+ voucher_activity_get_metadata_buffer.cold.1
+ voucher_mach_msg_set.cold.1
+ voucher_process_can_use_arbitrary_personas.cold.1
+ voucher_replace_default_voucher.cold.2
- GCC_except_table84
- GCC_except_table85
- GCC_except_table86
- GCC_except_table87
- GCC_except_table88
- __MergedGlobals
- __Unwind_Resume
- ___objc_personality_v0
- __dispatch_calloc
- __dispatch_io_create_with_io_block_invoke.cold.3
- __dispatch_io_create_with_io_block_invoke_2.cold.6
- _dispatch_bug_deprecated.last_seen
- _dispatch_bug_kevent_vanished.last_seen
- _dispatch_bug_mach_client.last_seen
- _dispatch_lane_class_dispose.cold.3
- _dispatch_lane_set_target_queue.cold.5
- _dispatch_lane_set_target_queue.cold.6
- _dispatch_lane_set_target_queue.cold.7
- _dispatch_mach_arm_no_senders.cold.3
- _dispatch_queue_override_invoke.cold.1
- _dispatch_queue_xref_dispose.cold.2
- _dispatch_sema4_timedwait.cold.1
- _dispatch_sema4_timedwait.cold.2
- _dispatch_sema4_timedwait.cold.3
- _dispatch_unote_unregister_direct.cold.1
- _dispatch_unote_unregister_muxed.cold.1
- _dispatch_workloop_dispose.cold.3
- _objc_begin_catch
- _objc_end_catch
- _objc_terminate
- dispatch_mach_handoff_reply.cold.1
CStrings:
+ "BUG IN LIBDISPATCH: Invalid workload ID type"
+ "BUG IN LIBDISPATCH: Unexpected error from mach recv"
- "NO"

```
