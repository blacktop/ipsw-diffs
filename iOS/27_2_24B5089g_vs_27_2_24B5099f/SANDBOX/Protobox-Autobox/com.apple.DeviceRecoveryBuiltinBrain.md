## com.apple.DeviceRecoveryBuiltinBrain

> Group: ⬆️ Updated

```diff

 		SYS_fcntl
 		SYS_fsync
 		SYS_socket
+		SYS_connect
 		SYS_sigsuspend
 		SYS_gettimeofday
 		SYS_readv

 		SYS_close_nocancel
 		SYS_fcntl_nocancel
 		SYS_fsync_nocancel
+		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel
 		SYS_writev_nocancel

 		MSC_mach_msg2_trap
 		MSC_thread_get_special_reply_port
 		MSC_host_create_mach_voucher_trap
+		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap)
 )

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_SETFD
 		F_GETFL
 		F_GETPATH
 		F_SETPROTECTIONCLASS
```
