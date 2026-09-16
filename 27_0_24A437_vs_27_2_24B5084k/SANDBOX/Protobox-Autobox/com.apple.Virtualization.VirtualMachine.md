## com.apple.Virtualization.VirtualMachine

> Group: ⬆️ Updated

```diff

 		SYS_geteuid
 		SYS_sendmsg
 		SYS_recvfrom
+		SYS_accept
 		SYS_getsockname
 		SYS_access
 		SYS_kill

 		MSC_pid_for_task
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap

 			mach_vm_remap_external
 			mach_vm_region
 			_mach_make_memory_entry
+			mach_vm_remap_new_external
 			mach_vm_range_create
 			mach_vm_reallocate
 			mach_memory_entry_ownership

 	(deny system-mac-syscall
 		(require-all
 			(require-not (mac-syscall-number 6))
+			(require-not (mac-syscall-number 5))
 			(require-not (mac-syscall-number 4))
 			(require-not (mac-syscall-number 67))
 			(require-not (mac-syscall-number 2))
```
