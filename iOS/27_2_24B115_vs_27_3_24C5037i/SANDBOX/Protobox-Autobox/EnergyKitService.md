## EnergyKitService

> Group: ⬆️ Updated

```diff

 			(global-name "com.apple.energykit.sharedStore")
 		))
 		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 
 (deny system-kas-info)
 
-(deny system-mac-syscall
-	(require-all
-		(mac-syscall-number 1)
-		(require-not (mac-policy-name "vnguard"))
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
