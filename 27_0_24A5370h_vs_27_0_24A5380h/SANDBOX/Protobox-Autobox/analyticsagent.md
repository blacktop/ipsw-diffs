## analyticsagent

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.biome.access.user"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (require-any
 			(global-name "com.apple.analyticsd.agent")
 			(global-name "com.apple.coreanalyticsd.agent")
 		))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.biome.access.user"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.geod"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (system-attribute developer-mode))
 	)
```
