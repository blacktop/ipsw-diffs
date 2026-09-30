## IOMFB_bics_daemon

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
```
