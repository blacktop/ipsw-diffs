## ScreenTimeAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.storagekitd"))
 		(require-not (global-name "com.apple.inputservice.keyboardui"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 			(global-name "/var/mobile/Library/Preferences/com.apple.eyereliefd")
 			(global-name "/var/mobile/Library/Preferences/com.apple.springboard.gsEvents")
 		))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cloudd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
```
