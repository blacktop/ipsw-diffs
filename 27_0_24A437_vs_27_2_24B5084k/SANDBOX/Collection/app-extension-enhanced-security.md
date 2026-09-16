## app-extension-enhanced-security

> Group: ⬆️ Updated

```diff

 
 (allow mach-lookup
 	(require-any
+		(global-name "com.apple.analyticsd")
 		(global-name "com.apple.logd")
 		(global-name "com.apple.system.notification_center")
 	)

 		SYS_pwritev
 		SYS_pwritev_nocancel
 		SYS_ulock_wait2
+		SYS_proc_info_extended_id
 		SYS_map_with_linking_np
 		SYS_freadlink)
 )
```
