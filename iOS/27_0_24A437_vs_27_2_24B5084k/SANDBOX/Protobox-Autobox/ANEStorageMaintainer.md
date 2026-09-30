## ANEStorageMaintainer

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (system-attribute developer-mode))

 		SYS_gettid
 		SYS_mkdir_extended
 		SYS_shared_region_check_np
+		SYS_psynch_rw_longrdlock
+		SYS_psynch_rw_yieldwrlock
+		SYS_psynch_rw_downgrade
+		SYS_psynch_rw_upgrade
 		SYS_psynch_mutexwait
 		SYS_psynch_mutexdrop
 		SYS_psynch_cvbroad
 		SYS_psynch_cvwait
+		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
+		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
 		SYS_iopolicysys
 		SYS_issetugid
```
