## healthd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.Carousel.contextuallock"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.diagnosticd"))

 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.Carousel.wristmonitor"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationsettingsservice"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.powerd.lowpowermode"))
 		(require-not (global-name "com.apple.biome.compute.source.user"))
 		(require-not (require-any
```
