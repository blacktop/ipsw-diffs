## com.apple.MobileAsset.DownloadService.Builtin

> Group: ⬆️ Updated

```diff

 			SYS_fgetattrlist
 			SYS_fsetattrlist
 			SYS_listxattr
+			SYS_flistxattr
 			SYS_fsctl
 			SYS_posix_spawn
 			SYS_sysctlbyname

 		MSC__kernelrpc_mach_port_request_notification_trap
 		MSC_mach_timebase_info_trap
 		MSC_mk_timer_create
+		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
 		MSC_mk_timer_cancel)
 )

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
