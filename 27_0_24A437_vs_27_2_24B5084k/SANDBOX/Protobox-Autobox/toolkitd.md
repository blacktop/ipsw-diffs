## toolkitd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))

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
+		SYS_psynch_cvsignal
 		SYS_psynch_cvwait
 		SYS_psynch_rw_rdlock
+		SYS_psynch_rw_wrlock
 		SYS_psynch_rw_unlock
+		SYS_psynch_rw_unlock2
 		SYS_psynch_cvclrprepost
 		SYS_iopolicysys
 		SYS_issetugid

 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 
```
