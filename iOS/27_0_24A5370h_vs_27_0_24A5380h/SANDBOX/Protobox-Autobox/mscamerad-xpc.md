## mscamerad-xpc

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.PowerManagement.control"))
-		(require-not (global-name "com.apple.coremedia.cameraviewfinder"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.coremedia.cameraviewfinder"))
+		(require-not (global-name "com.apple.coremedia.videocodecd.decompressionsession"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
+		(require-not (global-name "com.apple.gpumemd.source"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.FileProvider"))
 		(require-not (system-attribute developer-mode))
```
