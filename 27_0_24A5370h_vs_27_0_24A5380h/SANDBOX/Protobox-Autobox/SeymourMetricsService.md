## SeymourMetricsService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.xpc.amstoold"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
-		(require-not (global-name "com.apple.seymour"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.healthd.server"))
-		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.carousel.connectionstatusservice"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.xpc.amstoold"))
+		(require-not (global-name "com.apple.seymour"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
