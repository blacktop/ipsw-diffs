## app-extension-enhanced-security

> Group: ⬆️ Updated

```diff

 (allow mach-lookup
 	(global-name "com.apple.logd")
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.analyticsd")
-		(require-not (global-name "com.apple.logd"))
-	)
-)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.system.notification_center")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 	)
 	(apply-message-filter
 		(allow mach-message-send

 	(require-all
 		(global-name "com.apple.mobilegestalt.xpc")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 	)

 	(require-all
 		(global-name "com.apple.CARenderServer")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	(require-all
 		(global-name "com.apple.mobileassetd.v2")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	(require-all
 		(global-name "com.apple.coremedia.mediaparserd.utilities")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	(require-all
 		(global-name "com.apple.powerlog.plxpclogger.xpc")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	(require-all
 		(global-name "com.apple.audio.AudioComponentRegistrar")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 	(require-all
 		(global-name "com.apple.system.logger")
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (xpc-service-name "*"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))

 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 	)
 )
+(deny mach-lookup
+	(with no-report)
+	(require-all
+		(global-name "com.apple.analyticsd")
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (xpc-service-name "*"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.CARenderServer"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.coremedia.mediaparserd.utilities"))
+		(require-not (global-name "com.apple.powerlog.plxpclogger.xpc"))
+		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
+		(require-not (global-name "com.apple.system.logger"))
+	)
+)
 
 (allow mach-task-inspect
 	(target self)
```
