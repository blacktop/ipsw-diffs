## trustd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.biome.compute.source"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.biome.access.system"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
+		(require-not (global-name "com.apple.securityuploadd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (require-any
 			(global-name "com.apple.ValidUpdater")
 			(global-name "com.apple.trustdFileHelper")
 		))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.securityuploadd"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.biome.access.system"))
 		(require-not (global-name "com.apple.cloudtelemetryd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
