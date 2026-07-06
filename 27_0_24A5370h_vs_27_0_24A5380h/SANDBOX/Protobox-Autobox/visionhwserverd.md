## visionhwserverd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.systemstatus.publisher"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.iohideventsystem"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
-		(require-not (global-name "com.apple.appleh16camerad"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.iohideventsystem"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.appleh13camerad"))
+		(require-not (global-name "com.apple.appleh16camerad"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
