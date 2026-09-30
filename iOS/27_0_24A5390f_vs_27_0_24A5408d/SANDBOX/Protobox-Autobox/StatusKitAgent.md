## StatusKitAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.homed.xpc"))
+		(require-not (global-name "com.apple.StatusKit.presence"))
 		(require-not (global-name "com.apple.familycircled.sharing"))
 		(require-not (global-name "com.apple.locationd.registration"))
+		(require-not (global-name "com.apple.homed.xpc"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
