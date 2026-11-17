## remindd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.spotlight.IndexAgent"))
 		(require-not (global-name "com.apple.timed.xpc"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.webprivacyd"))
 		(require-not (global-name "com.apple.cache_delete"))
 		(require-not (global-name "com.apple.usymptomsd"))

 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.siri-distributed-evaluation"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
-		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))

 		MSC_mk_timer_create
 		MSC_mk_timer_destroy
 		MSC_mk_timer_arm
-		MSC_mk_timer_cancel)
+		MSC_mk_timer_cancel
+		MSC_mk_timer_arm_leeway)
 )
 
 (deny syscall-mig)
```
