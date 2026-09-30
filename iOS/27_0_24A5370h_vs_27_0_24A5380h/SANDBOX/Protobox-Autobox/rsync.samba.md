## rsync.samba

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (system-attribute developer-mode))
 	)
```
