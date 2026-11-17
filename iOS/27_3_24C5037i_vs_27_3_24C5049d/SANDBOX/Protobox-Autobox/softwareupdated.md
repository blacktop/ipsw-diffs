## softwareupdated

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.mobile.NRDUpdated"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.MobileSoftwareUpdate.CleanupPreparePathService")
 			(xpc-service-name "com.apple.MobileSoftwareUpdate.UpdateBrainService")
 		))
-		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
```
