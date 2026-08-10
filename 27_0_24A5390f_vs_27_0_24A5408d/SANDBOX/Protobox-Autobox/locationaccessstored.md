## locationaccessstored

> Group: ⬆️ Updated

```diff

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_unlinkat

 		MSC__kernelrpc_mach_port_mod_refs_trap
 		MSC__kernelrpc_mach_port_insert_right_trap
 		MSC__kernelrpc_mach_port_insert_member_trap
+		MSC__kernelrpc_mach_port_extract_member_trap
 		MSC__kernelrpc_mach_port_construct_trap
 		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC_semaphore_wait_trap
+		MSC_semaphore_timedwait_trap
 		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
```
