## com.apple.DocumentManagerCore.Rename

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.revisiond"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (global-name "com.apple.DesktopServicesHelper"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))

 		SYS_stat_extended
 		SYS_lstat_extended
 		SYS_fstat_extended
+		SYS_access_extended
 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np

 		SYS___sigwait_nocancel
 		SYS___semwait_signal_nocancel
 		SYS_fsgetpath
+		SYS_fileport_makeport
 		SYS_fileport_makefd
 		SYS_memorystatus_control
 		SYS_guarded_close_np

 
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
