## healthd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.Carousel.CSLSBackgroundTaskRequestService"))
 		(require-not (global-name "com.apple.server.bluetooth.le.att.xpc"))
 		(require-not (global-name "com.apple.carousel.backlightxpc"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.misagent"))
 		(require-not (global-name "com.apple.siriknowledged.koa.donate"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.xpc.activity.unmanaged"))

 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
