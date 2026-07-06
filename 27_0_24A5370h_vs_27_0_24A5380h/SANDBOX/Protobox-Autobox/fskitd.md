## fskitd

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.spotlight.userfs"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.spotlight.userfs"))
 		(require-not (require-any
 			(global-name "com.apple.filesystems.smbclientd")
 			(global-name "com.apple.fskit.fskit_helper")
 		))
-		(require-not (global-name "com.apple.filesystems.localLiveFiles"))
-		(require-not (global-name "com.apple.FileProvider"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.filesystems.localLiveFiles"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.research.adtcd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (xpc-service-name "com.apple.extensionkitservice"))
-		(require-not (require-any
-			(xpc-service-name "com.apple.fskit.apfs")
-			(xpc-service-name "com.apple.fskit.exfat")
-			(xpc-service-name "com.apple.fskit.hfs")
-			(xpc-service-name "com.apple.fskit.msdos")
-			(xpc-service-name "com.apple.fskit.passthroughfs")
-			(xpc-service-name "com.apple.fskit.sampleNormieServer")
-		))
 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")

 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
+				(require-not (require-any
+					(xpc-service-name "com.apple.fskit.apfs")
+					(xpc-service-name "com.apple.fskit.exfat")
+					(xpc-service-name "com.apple.fskit.hfs")
+					(xpc-service-name "com.apple.fskit.msdos")
+					(xpc-service-name "com.apple.fskit.passthroughfs")
+					(xpc-service-name "com.apple.fskit.sampleNormieServer")
+				))
+				(require-not (xpc-service-name "com.apple.extensionkitservice"))
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
