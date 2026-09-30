## AUHostingServiceXPC_arrow

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.audioanalyticsd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_listxattr
 		SYS_fsctl

 		SYS_open_nocancel
 		SYS_close_nocancel
 		SYS_sendmsg_nocancel
+		SYS_msync_nocancel
 		SYS_fcntl_nocancel
+		SYS_fsync_nocancel
 		SYS_connect_nocancel
 		SYS_sigsuspend_nocancel
 		SYS_readv_nocancel

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
 		SYS_guarded_writev_np
```
