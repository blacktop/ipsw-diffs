## mlruntimed

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.networkscored"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.trial.status"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.pluginkit.pkd"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.parsecd"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.biome.access.user"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.networkscored"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.photoanalysisd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.pluginkit.pkd"))
+		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.photoanalysisd"))
+		(require-not (global-name "com.apple.trial.status"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.parsecd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.AppleMediaDiscovery.AppStoreEvalLighthousePlugin")
 			(xpc-service-name "com.apple.MediaMLPluginApp.MediaMLPlugin")
```
