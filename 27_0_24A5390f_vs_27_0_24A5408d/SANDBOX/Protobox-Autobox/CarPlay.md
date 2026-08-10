## CarPlay

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.audioanalyticsd"))
+		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.siri.audiopowerupdate.xpc"))
 		(require-not (global-name "com.apple.CarAssetUtils.variants"))

 				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (global-name "UIASTNotificationCenter"))
 				(require-not (global-name "PurplePPTServer"))
 				(require-not (system-attribute developer-mode))
 			)

 				(require-not (global-name "com.apple.ABDatabaseDoctor"))
 				(require-not (global-name "com.apple.AccessibilityUIServer"))
 				(require-not (global-name "com.apple.AppSSO.service-xpc"))
+				(require-not (global-name "UIASTNotificationCenter"))
 				(require-not (global-name "PurplePPTServer"))
 				(require-not (system-attribute developer-mode))
 			)

 		SYS_munlock
 		SYS_getumask
 		SYS_open_dprotected_np
+		SYS_openat_dprotected_np
 		SYS_getattrlist
 		SYS_setattrlist
 		SYS_fgetattrlist

 		SYS_guarded_kqueue_np
 		SYS_change_fdguard_np
 		SYS_proc_rlimit_control
+		SYS_connectx
 		SYS_getattrlistbulk
 		SYS_clonefileat
 		SYS_openat

 		NECP_CLIENT_ACTION_COPY_RESULT
 		NECP_CLIENT_ACTION_COPY_ROUTE_STATISTICS
 		NECP_CLIENT_ACTION_COPY_UPDATED_RESULT
-		NECP_CLIENT_ACTION_REMOVE)
+		NECP_CLIENT_ACTION_REMOVE
+		NECP_CLIENT_ACTION_REMOVE_FLOW)
 )
 
 (allow process-exec-update-label)
```
