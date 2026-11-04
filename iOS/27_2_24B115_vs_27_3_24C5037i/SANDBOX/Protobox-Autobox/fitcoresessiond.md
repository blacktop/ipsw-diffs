## fitcoresessiond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.conversationmanager"))
 		(require-not (global-name "com.apple.heartratecoordinatord.requestor"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.lskdd.xpc"))
 		(require-not (global-name "com.apple.lskdd"))
 		(require-not (global-name "com.apple.logd.events"))

 
 (deny system-kas-info)
 
+(deny system-mac-syscall
+	(require-all
+		(mac-syscall-number 96)
+		(require-not (mac-policy-name "AMFI"))
+	)
+)
 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
```
