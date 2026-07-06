## CarPlayScreenshotService

> Group: ⬆️ Updated

```diff

 
 (deny mach-lookup
 	(require-all
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.CARenderServer"))
-		(require-not (global-name "com.apple.iapd.xpc"))
-		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.photos.service"))
-		(require-not (global-name "com.apple.backboard.hid.services"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (global-name "com.apple.iap2d.xpc"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.distributed_notifications@1v3"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.distributed_notifications@1v3"))
+		(require-not (global-name "com.apple.iapd.xpc"))
+		(require-not (global-name "com.apple.photos.service"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.coremedia.endpointremotecontrolsession.xpc"))
+		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.backboard.hid.services"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
