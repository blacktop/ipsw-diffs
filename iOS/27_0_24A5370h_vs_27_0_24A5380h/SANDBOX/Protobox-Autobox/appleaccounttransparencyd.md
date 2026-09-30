## appleaccounttransparencyd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.transparencyd.aet"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
