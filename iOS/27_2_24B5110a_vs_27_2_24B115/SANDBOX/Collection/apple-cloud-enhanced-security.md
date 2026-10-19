## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.logd.events"))
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.analyticsd")
-		(require-not (global-name "com.apple.cloudos.cb_bridged"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.logd"))
-	)
-)
 (allow mach-lookup
 	(require-all
 		(extension "com.apple.security.exception.mach-lookup.local-name")
 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 	)
 )
 (allow mach-lookup

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 	)
 )

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 	)

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.audio.AudioComponentRegistrar"))
 	)
 )
+(deny mach-lookup
+	(with no-report)
+	(require-all
+		(global-name "com.apple.analyticsd")
+		(require-not (global-name "com.apple.cloudos.cb_bridged"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
+		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
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
 (deny mach-lookup
 	(require-all
 		(xpc-service-name "*")
 		(require-not (global-name "com.apple.cloudos.cb_bridged"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.local-name"))
 		(require-not (extension "com.apple.security.exception.mach-lookup.global-name"))
 		(require-not (global-name "com.apple.system.notification_center"))
```
