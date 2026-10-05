## healthrecordsd

> Group: ⬆️ Updated

```diff

 		SYS_recvfrom_nocancel
 		SYS_fcntl_nocancel
 		SYS_select_nocancel
+		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 		SYS_connectx
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )
```
