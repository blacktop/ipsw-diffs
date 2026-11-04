## silent-nse

> Group: ⬆️ Updated

```diff

 	(require-all
 		(require-not (xpc-service-name "*"))
 		(require-any
+			(global-name "com.apple.lsd.advertisingidentifiers")
+			(global-name "com.apple.lsd.openurl")
 			(global-name "com.apple.tccd")
 			(require-all
 				(global-name "com.apple.system.notification_center")
 				(require-not (%entitlement-is-bool-true "com.apple.security.on-demand-install-capable"))
 			)
-			(require-any
-				(global-name "com.apple.lsd.advertisingidentifiers")
-				(global-name "com.apple.lsd.openurl")
-			)
 		)
 	)
 )
```
