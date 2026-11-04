## devicerecoveryd

> Group: ⬆️ Updated

```diff

 			(xpc-service-name "com.apple.DeviceRecoveryBrain")
 			(xpc-service-name "com.apple.DeviceRecoveryBuiltinBrain")
 		))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)

 
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
