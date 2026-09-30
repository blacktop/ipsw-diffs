## healthappd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationsettingsservice"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		SYS_preadv_nocancel
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np)
 )
 

 		F_SETCONFINED
 		F_GETCONFINED
 		F_ADDFILESIGS_RETURN
-		F_CHECK_LV)
+		F_CHECK_LV
+		F_ASSERT_BG_ACCESS
+		F_RELEASE_BG_ACCESS)
 )
 
 (deny system-fsctl)
```
