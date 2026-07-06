## parsecd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.trial.status"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (require-any
-			(global-name "com.apple.ScreenTimeSettingsAgent.private")
-			(global-name "com.apple.parsec-fbf")
-		))
+		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))
 		(require-not (global-name "com.apple.networkserviceproxy"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.osanalytics.report-services"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (global-name "com.apple.parsec-fbf"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		(require-not (global-name "com.apple.trial.status"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (require-any
-			(global-name "com.apple.ScreenTimeSettingsAgent.private")
-			(global-name "com.apple.parsec-fbf")
-		))
+		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))
 		(require-not (global-name "com.apple.networkserviceproxy"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.private"))
 		(require-not (global-name "com.apple.osanalytics.report-services"))

 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
+		(require-not (global-name "com.apple.parsec-fbf"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (xpc-service-name "com.apple.itunescloud.music-subscription-status-service"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
