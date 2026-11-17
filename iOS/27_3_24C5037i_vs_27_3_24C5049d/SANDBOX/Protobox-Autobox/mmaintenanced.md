## mmaintenanced

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.coresymbolicationd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))

 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.research.adtcd"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
