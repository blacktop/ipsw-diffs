## familynotificationd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mediaremoted.xpc"))
+		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (require-any
 			(global-name "com.apple.askpermission.familynotification")
 			(global-name "com.apple.family.notifier")
 			(global-name "com.apple.familyctl.familynotification")
 			(global-name "com.apple.ind.notifier")
 		))
-		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.familycircle.agent"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.lsd.open"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (system-attribute developer-mode))
 	)
```
