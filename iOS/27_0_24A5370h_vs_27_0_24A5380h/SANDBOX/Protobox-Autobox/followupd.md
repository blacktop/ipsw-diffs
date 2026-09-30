## followupd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
-		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
-		(require-not (global-name "com.apple.corefollowup.agent"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.usernotifications.listener"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.corefollowup.agent"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.NewDeviceOutreach.TVExtension")
 			(xpc-service-name "com.apple.health.HealthAppSupport.HealthFollowUpExtension")

 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
 				(require-not (global-name "com.apple.SBUserNotification"))
 				(require-not (system-attribute developer-mode))
```
