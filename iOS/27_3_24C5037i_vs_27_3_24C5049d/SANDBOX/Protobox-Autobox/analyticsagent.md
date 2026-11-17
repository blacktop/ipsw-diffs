## analyticsagent

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.coreanalyticsd.agent")
 		))
 		(require-not (global-name "com.apple.geod"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (system-attribute developer-mode))
 	)
```
