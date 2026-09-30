## symptomsd-diag

> Group: ⬆️ Updated

```diff

 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
 		SYS_mkdirat

 		MSC__kernelrpc_mach_port_type_trap
 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
-		MSC_mk_timer_create)
+		MSC_mk_timer_create
+		MSC_mk_timer_destroy)
 )
 
 (deny syscall-mig)
```
