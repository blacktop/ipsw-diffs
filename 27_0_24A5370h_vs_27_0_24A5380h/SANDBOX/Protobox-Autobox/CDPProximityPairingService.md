## CDPProximityPairingService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.securityd.sos"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.security.octagon"))
-		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.securityd.sos"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.security.octagon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.SBUserNotification"))

 		SYS_readv
 		SYS_writev
 		SYS_sendto
+		SYS_mkdir
 		SYS_pread
 		SYS_pwrite
 		SYS_statfs

 		SYS_lstat_extended
 		SYS_fstat_extended
 		SYS_gettid
+		SYS_mkdir_extended
 		SYS_shared_region_check_np
 		SYS_psynch_rw_longrdlock
 		SYS_psynch_rw_yieldwrlock

 		SYS_openat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
