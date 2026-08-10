## linkd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(require-not (global-name "com.apple.linkd.registry"))
 		(require-not (global-name "com.apple.linkd.extension"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (require-any
+			(global-name "appevent-observer-5555494431be1e7467b03c4ca2ecb2488c22328b.appevent")
 			(global-name "com.apple.corespeech.corespeechd.uaapservice")
 			(global-name "com.apple.remoteappintentsd..appevent")
 			(global-name "com.apple.remoteappintentsd.appevent")
+			(global-name "com.apple.traj2intent.appeventobserver.appevent")
 		))
 		(require-not (global-name "com.apple.iap2d.xpc"))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.uservault"))
 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))
 			)
 			(require-all
 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
-				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
-				(require-not (global-name "com.apple.CARenderServer"))
 				(require-not (system-attribute developer-mode))
 			)
 		)
```
