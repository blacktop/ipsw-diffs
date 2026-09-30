## com.apple.photos.PCCService

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.privatecloudcompute"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
