## aia_controllerd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(require-not (syscall-number
 			SYS_exit
+			SYS_write
 			SYS_open
+			SYS_close
 			SYS_getfsstat
 			SYS_getpid
 			SYS_getuid

 			SYS_sigpending
 			SYS_sigaltstack
 			SYS_umask
+			SYS_munmap
 			SYS_mprotect
 			SYS_fcntl
 			SYS_sigsuspend
+			SYS_sendto
 			SYS_pread
 			SYS_kdebug_typefilter
 			SYS_kdebug_trace_string
 			SYS_kdebug_trace64
 			SYS_kdebug_trace
 			SYS_sigreturn
+			SYS_mmap
 			SYS_lseek
 			SYS_sysctl
 			SYS_getumask

 			SYS___pthread_fchdir
 			SYS_thread_selfid
 			SYS___mac_syscall
+			SYS_read_nocancel
 			SYS_fcntl_nocancel
 			SYS_sigsuspend_nocancel
 			SYS_pread_nocancel

 			SYS_openat
 			SYS_fstatat
 			SYS_fstatat64
+			SYS_persona
 			SYS_terminate_with_payload
 			SYS_abort_with_payload
 			SYS_os_fault_with_payload

 		MSC__kernelrpc_mach_vm_deallocate_trap
 		MSC__kernelrpc_mach_vm_protect_trap
 		MSC__kernelrpc_mach_vm_map_trap
+		MSC__kernelrpc_mach_port_allocate_trap
 		MSC__kernelrpc_mach_port_deallocate_trap
 		MSC__kernelrpc_mach_port_mod_refs_trap
+		MSC__kernelrpc_mach_port_insert_member_trap
 		MSC__kernelrpc_mach_port_construct_trap
+		MSC__kernelrpc_mach_port_destruct_trap
 		MSC_mach_reply_port
 		MSC_task_self_trap
 		MSC_host_self_trap
+		MSC__kernelrpc_mach_port_guard_trap
 		MSC_mach_generate_activity_id
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port

 			mach_exception_raise_state
 			mach_exception_raise_state_identity
 			io_service_open_extended
+			mach_port_set_attributes
 			mach_port_get_context_from_user
 			task_info_from_user
 			task_get_special_port_from_user
```
