## SensorKitALSHelper

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.accessoryupdater.launchauhelper"))
-		(require-not (global-name "com.apple.icloud.searchpartyd.ownersession"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.routined.registration"))
-		(require-not (global-name "com.apple.FileCoordination"))
-		(require-not (global-name "com.apple.HearingModeService"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.BluetoothCloudServices"))
-		(require-not (global-name "com.apple.locationd.registration"))
-		(require-not (global-name "com.apple.bluetooth.xpc"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.bluetooth.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.accessoryupdater.launchauhelper"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.FileCoordination"))
+		(require-not (global-name "com.apple.icloud.searchpartyd.ownersession"))
+		(require-not (global-name "com.apple.BluetoothCloudServices"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.SensorKit.writer"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.HearingModeService"))
 		(require-not (global-name "com.apple.bluetoothuser.xpc"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.access.system"))
-		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
+		(require-not (global-name "com.apple.routined.registration"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.SensorKit.writer"))
-		(require-not (xpc-service-name "com.apple.siri.context.service"))
-		(require-not (xpc-service-name "com.apple.ctcategories.service"))
-		(require-not (xpc-service-name "com.apple.SensorKit.CHSupportService"))
 		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
+		(require-not (xpc-service-name "com.apple.siri.context.service"))
+		(require-not (xpc-service-name "com.apple.SensorKit.CHSupportService"))
+		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (global-name "com.apple.AudioAccessoryServices"))
 		(require-not (system-attribute developer-mode))
 	)

 (deny system-fcntl)
 (allow system-fcntl
 	(fcntl-command
+		F_GETFD
 		F_SETFD
 		F_GETFL
 		F_NOCACHE
```
