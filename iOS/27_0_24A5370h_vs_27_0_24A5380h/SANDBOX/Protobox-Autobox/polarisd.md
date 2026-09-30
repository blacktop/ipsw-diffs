## polarisd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.polaris.offloadd"))
-		(require-not (global-name "com.apple.polaris.daemon_default"))
-		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd.admin"))
 		(require-not (global-name "com.apple.polaris.systemgraph"))
+		(require-not (global-name "com.apple.polaris.daemon_default"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.tailspind"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.iokit.powerdxpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.logd.admin"))
+		(require-not (global-name "com.apple.polaris.offloadd"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
```
