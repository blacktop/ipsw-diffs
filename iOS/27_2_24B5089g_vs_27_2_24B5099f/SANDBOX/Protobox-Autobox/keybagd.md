## keybagd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))

 		SYS_kdebug_trace64
 		SYS_kdebug_trace
 		SYS_sigreturn
+		SYS_stat
+		SYS_fstat
+		SYS_lstat
 		SYS_pathconf
 		SYS_getrlimit
 		SYS_setrlimit

 		SYS_fsctl
 		SYS_shm_open
 		SYS_sysctlbyname
+		SYS_stat_extended
+		SYS_lstat_extended
+		SYS_fstat_extended
 		SYS_gettid
 		SYS_shared_region_check_np
 		SYS_psynch_rw_longrdlock
```
