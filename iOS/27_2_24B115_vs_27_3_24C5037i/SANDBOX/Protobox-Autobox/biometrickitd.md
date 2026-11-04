## biometrickitd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.awdd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
+		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.iohideventsystem"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))

 
 (deny system-kas-info)
 
-(with-filter (mac-policy-name "Sandbox")
-	(deny system-mac-syscall
-		(require-all
-			(require-not (mac-syscall-number 5))
-			(require-not (mac-syscall-number 6))
-			(require-not (mac-syscall-number (_IO "" 5)))
-			(require-not (mac-syscall-number 4))
-			(require-not (mac-syscall-number 67))
-			(require-not (mac-syscall-number 12))
-			(require-not (mac-syscall-number 2))
-		)
-	)
-)
-(deny system-mac-syscall
-	(require-any
-		(require-not (mac-policy-name "AMFI"))
-		(require-not (mac-syscall-number 90))
-	)
-)
+(deny system-mac-syscall)
 
 (deny system-memorystatus-control)
 (allow system-memorystatus-control
```
