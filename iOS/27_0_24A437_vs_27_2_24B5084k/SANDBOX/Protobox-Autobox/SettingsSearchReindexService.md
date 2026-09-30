## SettingsSearchReindexService

> Group: ⬆️ Updated

```diff

 (allow default)
 
 (deny file-ioctl
-	(with no-report)
 	(process-attribute is-autoboxed)
 )
+(allow file-ioctl
+	(require-all
+		(process-attribute is-autoboxed)
+		(ioctl-command (_IO "h" 4))
+	)
+)
 
 (deny generic-issue-extension
 	(with no-report)

 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
