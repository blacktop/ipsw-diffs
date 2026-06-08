## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

-1542.100.32.0.0
-  __TEXT.__text: 0x3c11c
-  __TEXT.__auth_stubs: 0xc00
+1601.0.0.0.1
+  __TEXT.__text: 0x3dcf0
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x760
-  __TEXT.__cstring: 0x6189
-  __TEXT.__unwind_info: 0xdb0
+  __TEXT.__cstring: 0x61a0
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x499
-  __TEXT.__objc_methname: 0x2b9
-  __TEXT.__objc_methtype: 0x118
-  __TEXT.__objc_stubs: 0x1e0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0xc78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xc90
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_nlclslist: 0xb8
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__auth_got: 0x610
+  __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x10cb8
   __AUTH_CONST.__objc_const: 0x1f00
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH.__data: 0x70
   __DATA.__data: 0x11b8
   __DATA.__crash_info: 0x148

   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xdf8
   __DATA_DIRTY.__data: 0xc50
-  __DATA_DIRTY.__common: 0x188
+  __DATA_DIRTY.__common: 0x190
   __DATA_DIRTY.__bss: 0x6b8
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: E1A24FA0-2160-3366-AE7E-420F0FA3C5BC
-  Functions: 1385
-  Symbols:   3893
-  CStrings:  630
+  UUID: 27082A1E-6824-3F76-8CAB-6183F8BE7689
+  Functions: 1377
+  Symbols:   3858
+  CStrings:  512
 
Symbols:
+ _OUTLINED_FUNCTION_14
+ ____dispatch_transform_from_utf16_block_invoke.cold.1
+ ____dispatch_transform_from_utf16_block_invoke.cold.2
+ ____dispatch_transform_from_utf16_block_invoke.cold.3
+ ___dispatch_io_create_with_io_block_invoke.cold.3
+ ___dispatch_io_create_with_io_block_invoke_2.cold.6
+ __dispatch_apply_with_attr_f.cold.8
+ __dispatch_channel_dispose.cold.1
+ __dispatch_channel_dispose.cold.2
+ __dispatch_channel_dispose.cold.3
+ __dispatch_event_loop_wake_owner.cold.6
+ __dispatch_kevent_has_machmsg_rcv_error
+ __dispatch_kevent_has_machmsg_rcv_error.cold.1
+ __dispatch_lane_activate.cold.1
+ __dispatch_lane_dispose.cold.1
+ __dispatch_lane_dispose.cold.2
+ __dispatch_lane_legacy_set_target_queue.cold.4
+ __dispatch_mach_activate.cold.1
+ __dispatch_mach_arm_no_senders.cold.3
+ __dispatch_mach_handoff_set_wlh.cold.1
+ __dispatch_mach_msg_create_reply_disconnected.cold.4
+ __dispatch_mach_msg_disconnected
+ __dispatch_mach_reply_merge_msg.cold.1
+ __dispatch_mach_reply_merge_msg.cold.2
+ __dispatch_mach_send_and_wait_for_reply.cold.7
+ __dispatch_main_queue_drain.cold.8
+ __dispatch_main_queue_drain.cold.9
+ __dispatch_pthread_root_queue_dispose.cold.1
+ __dispatch_pthread_root_queue_dispose.cold.2
+ __dispatch_pthread_root_queue_dispose.cold.3
+ __dispatch_queue_specific_head_dispose_slow.cold.1
+ __dispatch_queue_xref_dispose.cold.2
+ __dispatch_runloop_queue_dispose.cold.1
+ __dispatch_runloop_queue_dispose.cold.2
+ __dispatch_runloop_queue_dispose.cold.3
+ __dispatch_sema4_timedwait.cold.1
+ __dispatch_sema4_timedwait.cold.2
+ __dispatch_sema4_timedwait.cold.3
+ __dispatch_source_registration_callout.cold.1
+ __dispatch_thread_event_wait_slow.cold.2
+ __dispatch_timer_heap_max_target_before
+ __dispatch_timer_unote_disarm.cold.1
+ __dispatch_transform_detect_utf
+ __dispatch_unote_register_muxed.cold.1
+ __dispatch_unote_unregister_direct.cold.1
+ __dispatch_workloop_activate_tg_unsupported_fallback
+ __mach_error_to_errno
+ __voucher_create_mach_voucher
+ __voucher_create_with_mach_voucher.cold.4
+ __voucher_create_with_mach_voucher.cold.5
+ __voucher_create_without_importance.cold.4
+ __voucher_create_without_importance.cold.5
+ __voucher_create_without_importance.cold.6
+ __voucher_create_without_importance.cold.7
+ __voucher_dispose.cold.3
+ __voucher_launch_persona_id
+ __voucher_launch_persona_id_init
+ __voucher_launch_persona_id_pred
+ _dispatch_apply_attr_query.cold.6
+ _dispatch_apply_attr_set_per_cluster_parallelism
+ _dispatch_apply_attr_set_per_cluster_parallelism.cold.1
+ _dispatch_apply_attr_set_per_cluster_parallelism.cold.2
+ _dispatch_apply_attr_set_per_cluster_parallelism.cold.3
+ _dispatch_mach_handoff_reply.cold.1
+ _dispatch_mach_handoff_reply.cold.2
+ _dispatch_queue_attr_make_initially_inactive.cold.1
+ _dispatch_queue_attr_make_with_autorelease_frequency.cold.1
+ _dispatch_queue_attr_make_with_overcommit.cold.1
+ _dispatch_queue_attr_make_with_qos_class.cold.1
+ _dispatch_thread_override_self_with_base
+ _dispatch_thread_reset_override_self
+ _kpersona_pidinfo
+ _os_eventlink_activate.cold.1
+ _os_eventlink_extract_remote_port.cold.1
+ _os_eventlink_extract_remote_port.cold.2
+ _os_eventlink_signal_and_wait.cold.1
+ _os_eventlink_signal_and_wait_until.cold.1
+ _os_eventlink_signal_and_wait_until.cold.2
+ _os_eventlink_wait_until_internal.cold.3
+ _voucher_activity_initialize_4libtrace.cold.3
+ _voucher_create_with_mach_msg.cold.1
+ _voucher_create_with_mach_msg.cold.2
+ _voucher_create_with_mach_msg.cold.3
+ _voucher_mach_msg_set.cold.2
- ____dispatch_fd_entry_create_with_fd_block_invoke.cold.1
- ____dispatch_io_stop_block_invoke_2.cold.3
- ____dispatch_operation_deliver_data_block_invoke.cold.2
- ___dispatch_io_create_with_path_block_invoke.cold.3
- __dispatch_channel_invoke.cold.5
- __dispatch_channel_invoke.cold.6
- __dispatch_channel_invoke.cold.7
- __dispatch_channel_invoke.cold.8
- __dispatch_channel_invoke.cold.9
- __dispatch_continuation_alloc_from_heap.cold.1
- __dispatch_disk_init.cold.2
- __dispatch_event_loop_drain_timers.cold.4
- __dispatch_event_loop_drain_timers.cold.5
- __dispatch_event_loop_wait_for_ownership.cold.4
- __dispatch_event_loop_wait_for_ownership.cold.5
- __dispatch_event_loop_wait_for_ownership.cold.6
- __dispatch_event_loop_wait_for_ownership.cold.7
- __dispatch_fd_entry_cleanup_operations.cold.3
- __dispatch_fd_entry_init_async.cold.1
- __dispatch_free_deferred_items.cold.3
- __dispatch_get_main_queue_handle_4CF.cold.1
- __dispatch_kevent_mach_msg_recv.cold.5
- __dispatch_kevent_mach_msg_recv.cold.6
- __dispatch_log_file
- __dispatch_log_file.cold.1
- __dispatch_mach_host_notify_update.cold.2
- __dispatch_mach_host_notify_update.cold.3
- __dispatch_mach_msg_async_reply_wrap.cold.1
- __dispatch_mach_msg_async_reply_wrap.cold.2
- __dispatch_mgr_queue_push.cold.2
- __dispatch_operation_create.cold.4
- __dispatch_operation_dispose.cold.2
- __dispatch_operation_should_enqueue.cold.2
- __dispatch_queue_atfork_child.cold.1
- __dispatch_queue_attr_from_info
- __dispatch_queue_priority_inherit_from_target
- __dispatch_queue_priority_inherit_from_target.cold.1
- __dispatch_root_queue_drain.cold.5
- __dispatch_root_queue_drain_deferred_item.cold.2
- __dispatch_root_queue_drain_deferred_wlh.cold.5
- __dispatch_runloop_root_queue_perform_4CF.cold.7
- __dispatch_sema4_create_slow.cold.6
- __dispatch_sema4_create_slow.cold.7
- __dispatch_sema4_dispose_slow.cold.2
- __dispatch_sema4_dispose_slow.cold.3
- __dispatch_source_activate.cold.2
- __dispatch_timer_heap_grow
- __dispatch_timer_heap_shrink
- __dispatch_wlh_cleanup.cold.2
- __dispatch_workloop_activate.cold.3
- __dispatch_workloop_activate.cold.4
- __dispatch_workloop_invoke.cold.4
- __dispatch_workloop_invoke.cold.5
- __dispatch_workloop_invoke.cold.6
- __dispatch_workloop_invoke.cold.7
- __dispatch_workloop_wakeup.cold.3
- __dispatch_workloop_wakeup.cold.4
- __voucher_atfork_prepare.cold.1
- __voucher_dealloc_mach_voucher.cold.1
- __voucher_find_and_retain.cold.2
- __voucher_insert.cold.4
- __voucher_process_can_use_arbitrary_personas_init.cold.2
- __voucher_xref_dispose.cold.3
- _dispatch_apply_attr_set_parallelism.cold.3
- _dispatch_apply_attr_set_parallelism.cold.4
- _dispatch_apply_attr_set_parallelism.cold.5
- _dispatch_assert_queue$V2.cold.2
- _dispatch_assert_queue_barrier.cold.1
- _dispatch_io_barrier.cold.2
- _dispatch_io_close.cold.3
- _dispatch_io_close.cold.4
- _dispatch_io_set_high_water.cold.2
- _dispatch_io_set_interval.cold.2
- _dispatch_io_set_low_water.cold.2
- _dispatch_mach_mig_demux.cold.3
- _dispatch_mach_msg_create.cold.1
- _dispatch_mach_msg_create.cold.2
- _dispatch_set_target_queue.cold.3
- _dispatch_source_cancel.cold.2
- _dispatch_source_merge_data.cold.2
- _firehose_client_merge_updates
- _mach_voucher_persona_for_originator.cold.1
- _mach_voucher_persona_self.cold.1
- _os_eventlink_signal_and_wait_until_internal
- _os_eventlink_signal_and_wait_until_internal.cold.1
- _os_eventlink_signal_and_wait_until_internal.cold.2
- _voucher_activity_create_with_data_2.cold.3
- _voucher_copy_with_persona_mach_voucher.cold.3
- _voucher_process_can_use_arbitrary_personas.cold.1
- _voucher_replace_default_voucher.cold.2
CStrings:
+ "BUG in libdispatch: %s - %lu - 0x%llx"
+ "com.apple.coremedia"
+ "target = %s[%p], ident = 0x%llx, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s"
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@44@0:8^v16Q24B32B36B40"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "BUG in libdispatch: %s - %lu - 0x%lx"
- "NSObject"
- "OS_dispatch_channel"
- "OS_dispatch_data"
- "OS_dispatch_data_empty"
- "OS_dispatch_disk"
- "OS_dispatch_group"
- "OS_dispatch_io"
- "OS_dispatch_mach"
- "OS_dispatch_mach_msg"
- "OS_dispatch_object"
- "OS_dispatch_operation"
- "OS_dispatch_queue"
- "OS_dispatch_queue_attr"
- "OS_dispatch_queue_concurrent"
- "OS_dispatch_queue_cooperative"
- "OS_dispatch_queue_global"
- "OS_dispatch_queue_main"
- "OS_dispatch_queue_mgr"
- "OS_dispatch_queue_pthread_root"
- "OS_dispatch_queue_runloop"
- "OS_dispatch_queue_serial"
- "OS_dispatch_queue_serial_executor"
- "OS_dispatch_semaphore"
- "OS_dispatch_source"
- "OS_dispatch_source_data_add"
- "OS_dispatch_source_data_or"
- "OS_dispatch_source_data_replace"
- "OS_dispatch_source_exclaves_notification"
- "OS_dispatch_source_interval"
- "OS_dispatch_source_mach_recv"
- "OS_dispatch_source_mach_send"
- "OS_dispatch_source_memorypressure"
- "OS_dispatch_source_memorystatus"
- "OS_dispatch_source_nw_channel"
- "OS_dispatch_source_proc"
- "OS_dispatch_source_read"
- "OS_dispatch_source_signal"
- "OS_dispatch_source_sock"
- "OS_dispatch_source_timer"
- "OS_dispatch_source_vfs"
- "OS_dispatch_source_vm"
- "OS_dispatch_source_vnode"
- "OS_dispatch_source_write"
- "OS_dispatch_workloop"
- "OS_object"
- "OS_os_eventlink"
- "OS_os_workgroup"
- "OS_os_workgroup_interval"
- "OS_os_workgroup_parallel"
- "OS_voucher"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "TQ,R,N"
- "Tr^v,R,N"
- "Vv16@0:8"
- "^v16@0:8"
- "^{_NSZone=}16@0:8"
- "_activate"
- "_bytesAreVM"
- "_getContext"
- "_isCompact"
- "_resume"
- "_setContext:"
- "_setFinalizer:"
- "_setTargetQueue:"
- "_suspend"
- "_xref_dispose"
- "allocWithZone:"
- "allowsWeakReference"
- "autorelease"
- "bytes"
- "class"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "getBytes:maxLength:usedLength:encoding:options:range:remainingRange:"
- "hash"
- "init"
- "initWithBytes:length:copy:freeWhenDone:bytesAreVM:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "r^v16@0:8"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retainWeakReference"
- "self"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "target = %s[%p], ident = 0x%x, mask = 0x%x, pending_data = 0x%llx, registered = %d, armed = %d, %s%s%s"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8^?16"
- "v24@0:8^v16"
- "zone"

```
