## ManagementTestSubscriber

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.RemoteManagementAgent.store"))
 		(require-not (system-attribute developer-mode))
 	)
```
