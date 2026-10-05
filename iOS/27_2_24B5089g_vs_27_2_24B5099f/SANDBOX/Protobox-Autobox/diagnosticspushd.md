## diagnosticspushd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.enhancedloggingd.xpc"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
 		(require-not (global-name "com.apple.apsd"))
+		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
 		(require-not (global-name "com.apple.usernotifications.listener"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
```
