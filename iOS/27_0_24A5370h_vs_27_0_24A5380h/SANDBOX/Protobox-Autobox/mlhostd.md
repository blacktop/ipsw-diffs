## mlhostd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.extensionkitservice"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.userprofiles"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.uservault"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.userprofiles"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.AppleMediaDiscovery.AppStoreEvalLighthouseWorker")
 			(xpc-service-name "com.apple.AppleMediaDiscovery.PFLASLArcadeRetention")
```
