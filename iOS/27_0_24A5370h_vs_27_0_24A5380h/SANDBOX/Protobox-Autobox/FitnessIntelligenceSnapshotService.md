## FitnessIntelligenceSnapshotService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.seymour"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.seymour"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))

 		SYS_sysctl
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_fgetattrlist
 		SYS_listxattr

 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
 		SYS_fcntl_nocancel
+		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
```
