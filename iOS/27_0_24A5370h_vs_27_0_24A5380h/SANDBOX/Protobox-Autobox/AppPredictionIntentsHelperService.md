## AppPredictionIntentsHelperService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.lsd.icons"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.lsd.xpc"))
-		(require-not (global-name "com.apple.calaccessd"))
-		(require-not (global-name "com.apple.debug.telemetry"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.remindd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.lsd.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.remindd"))
+		(require-not (global-name "com.apple.debug.telemetry"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
```
