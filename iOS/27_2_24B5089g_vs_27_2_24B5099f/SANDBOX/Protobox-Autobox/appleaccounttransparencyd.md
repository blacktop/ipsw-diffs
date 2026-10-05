## appleaccounttransparencyd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
+		(require-not (global-name "com.apple.storagekitd"))
+		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.transparencyd.aet"))
 		(require-not (system-attribute developer-mode))
 	)
```
