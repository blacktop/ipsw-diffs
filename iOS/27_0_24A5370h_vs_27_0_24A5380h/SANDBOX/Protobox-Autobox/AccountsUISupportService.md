## AccountsUISupportService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
```
