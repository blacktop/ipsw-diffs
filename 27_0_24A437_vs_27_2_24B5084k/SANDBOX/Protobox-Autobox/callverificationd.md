## callverificationd

> Group: ⬆️ Updated

```diff

 		SYS_getpid
 		SYS_getuid
 		SYS_geteuid
+		SYS_recvmsg
 		SYS_sendmsg
+		SYS_recvfrom
 		SYS_access
 		SYS_crossarch_trap
 		SYS_dup

 		SYS_write_nocancel
 		SYS_open_nocancel
 		SYS_close_nocancel
+		SYS_recvmsg_nocancel
 		SYS_sendmsg_nocancel
+		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
 		SYS_connect_nocancel

 		MSC_task_name_for_pid
 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
+		MSC_swtch_pri
 		MSC_syscall_thread_switch
 		MSC_host_create_mach_voucher_trap
 		MSC__kernelrpc_mach_port_type_trap

 	(fcntl-command
 		F_SETFD
 		F_GETFL
+		F_SETFL
 		F_SETLKW
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
