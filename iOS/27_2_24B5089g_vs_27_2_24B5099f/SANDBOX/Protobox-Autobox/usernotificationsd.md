## usernotificationsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (require-any
 			(global-name "com.apple.chrono.accessoryLiveActivities")
+			(global-name "com.apple.linkd.application-service")
 			(global-name "com.apple.usernotifications.accessorynotifications")
 			(global-name "com.apple.usernotifications.systemservice")
 		))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.erm.logging"))
+		(require-not (global-name "com.apple.linkd.autoShortcut"))
 		(require-not (global-name "com.apple.eligibilityd"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled.public"))
 		(require-not (global-name "com.apple.SharingServices"))

 		(require-not (global-name "com.apple.sharingd.nsxpc"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.gpumemd.source"))
 		(require-not (global-name "com.apple.securityd"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.DeviceAccess.xpc"))

 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
 		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
-		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
```
