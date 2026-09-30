## demod_helper

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.bird"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.sysdiagnose.service.xpc"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.bird"))
+		(require-not (global-name "com.apple.sysdiagnose.service.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
