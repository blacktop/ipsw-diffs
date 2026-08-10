## powerexceptionsd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.spindump"))

 		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_shared_region_map_and_slide_2_np
+		SYS_task_read_for_pid
 		SYS_preadv
 		SYS_pwritev
 		SYS_preadv_nocancel

 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_task_name_for_pid
+		MSC_task_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_swtch_pri

 		task_set_special_port
 		semaphore_create
 		semaphore_destroy
+		task_get_mach_voucher
 		task_set_exc_guard_behavior
 		thread_terminate
 		thread_suspend
 		thread_resume
 		thread_info
+		thread_get_mach_voucher
 		vm_remap_external
 		vm_reallocate
 		mach_vm_copy

 		mach_vm_region_recurse
 		mach_vm_region
 		_mach_make_memory_entry
+		mach_vm_page_range_query
 		mach_vm_range_create
 		mach_vm_reallocate
 		mach_memory_entry_ownership
```
