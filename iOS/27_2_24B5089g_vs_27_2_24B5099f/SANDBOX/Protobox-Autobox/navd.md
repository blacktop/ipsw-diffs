## navd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.Maps.MapsSync.store"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.locationd.simulation"))

 		(require-not (global-name "com.apple.sirittsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.iphone.axserver-systemwide"))
 		(require-not (global-name "com.apple.Maps.mapspushd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.audio.AudioQueueServer"))
```
