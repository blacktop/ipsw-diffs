## devicerecoveryd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.OTATaskingAgent"))
+		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.wifi.manager"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.OSASubmission.client"))

 		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
 		SYS_psynch_rw_unlock2
+		SYS_psynch_cvclrprepost
 		SYS_issetugid
 		SYS___pthread_kill
 		SYS___pthread_sigmask

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_fstatat
 		SYS_fstatat64
+		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
 		SYS_guarded_write_np
```
