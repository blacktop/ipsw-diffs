## heartratecoordinatord

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.healthlited"))
 		(require-not (global-name "com.apple.healthd.server"))
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
 		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.healthlited"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (xpc-service-name "com.apple.HeartRateCoordinator.RecordingService"))
 		(require-not (global-name "com.apple.AudioAccessoryServices"))
```
