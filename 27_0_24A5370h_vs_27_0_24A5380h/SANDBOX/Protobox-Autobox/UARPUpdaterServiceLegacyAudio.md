## UARPUpdaterServiceLegacyAudio

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.iapd.xpc"))
-		(require-not (global-name "com.apple.SBUserNotification"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.ExternalAccessory.distributednotification.server"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
 			(global-name "com.apple.iaptransportd.ExternalAccessory.distributednotification.server")
 		))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (xpc-service-name "com.apple.corespeech.xpc"))
-		(require-not (global-name "com.apple.erm.logging"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.corespeech.corespeechservices"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.iapd.xpc"))
+		(require-not (xpc-service-name "com.apple.corespeech.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.corespeech.corespeechservices"))
+		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.debug.telemetry"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (system-attribute developer-mode))
 	)
```
