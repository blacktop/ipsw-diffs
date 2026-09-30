## emergencyd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.sessionservices"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.lsd.xpc"))
 		(require-not (global-name "com.apple.watchnotificationsui.alertservice"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.sessionservices"))
 		(require-not (global-name "com.apple.backboard.hid.services"))
-		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.CARenderServer"))
```
