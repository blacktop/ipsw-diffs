## alwaysonexclavesd

> Group: ⬆️ Updated

```diff

 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
 		SYS_persona
+		SYS_work_interval_ctl
 		SYS_getentropy
 		SYS_ulock_wait
 		SYS_ulock_wake
 		SYS_terminate_with_payload
 		SYS_abort_with_payload
 		SYS_os_fault_with_payload
+		SYS_kqueue_workloop_ctl
 		SYS_memorystatus_available_memory
 		SYS_preadv
 		SYS_pwritev

 		MSC_host_self_trap
 		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_wait_signal_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```
