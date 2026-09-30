## deleted_helper

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.gputools.producer"))
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.cache_delete"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.cache_delete.public"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.OSASubmission.client"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.cache_delete.public"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.gputools.producer"))
+		(require-not (global-name "com.apple.cache_delete"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (system-attribute developer-mode))
 	)
```
