## lockdownd

> Group: ⬆️ Updated

```diff

 
 (allow mach-derive-port)
 
+(allow mach-lookup
+	(require-all
+		(global-name "com.apple.system.notification_center")
+		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
+	)
+)
 (allow mach-lookup
 	(require-all
 		(global-name "com.apple.internal.*")

 		(system-attribute internal-build)
 	)
 )
-(allow mach-lookup
-	(require-all
-		(global-name "com.apple.system.notification_center")
-		(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
-	)
-)
 (allow mach-lookup
 	(require-all
 		(require-any

 			(global-name "com.apple.pgtrace")
 			(global-name "com.apple.xdcd")
 		)
-		(require-any
-			(global-name "com.apple.internal.devicecompute.CoreDeviceProxy")
-			(system-attribute internal-build)
-		)
+		(system-attribute internal-build)
 	)
 )
 (allow mach-lookup

 		(global-name "com.apple.idamd")
 		(global-name "com.apple.instruments.deviceservice.lockdown")
 		(global-name "com.apple.instruments.deviceservice.lockdown.secure")
+		(global-name "com.apple.internal.devicecompute.CoreDeviceProxy")
 		(global-name "com.apple.iokit.powerdxpc")
 		(global-name "com.apple.lockdown.*")
 		(global-name "com.apple.lsd.advertisingidentifiers")
```
