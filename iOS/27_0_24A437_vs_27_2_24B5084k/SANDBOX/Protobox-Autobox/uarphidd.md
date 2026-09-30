## uarphidd

> Group: ⬆️ Updated

```diff

 			SYS_sysctl
 			SYS_getumask
 			SYS_open_dprotected_np
+			SYS_openat_dprotected_np
 			SYS_fsctl
 			SYS_sysctlbyname
 			SYS_gettid

 			SYS_fsgetpath
 			SYS_memorystatus_control
 			SYS_openat
+			SYS_renameat
 			SYS_fstatat
 			SYS_fstatat64
 			SYS_mkdirat
+			SYS_guarded_open_dprotected_np
 			SYS_persona
 			SYS_terminate_with_payload
 			SYS_abort_with_payload

 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_signal_trap
 		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_get_attributes_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
```
