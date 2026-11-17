## SettingsSearchReindexService

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.SettingsHostAgent.search-reindex"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
```
