## UARPAssetManagerServiceiCloud

> Group: ⬆️ Updated

```diff

 		(require-any
 			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 			(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+			(iokit-registry-entry-class "AppleKeyStoreUserClient")
 		)
 	)
 )

 (allow ipc-posix-shm-read-data
 	(require-all
 		(process-attribute is-autoboxed)
-		(ipc-posix-name "apple.shm.notification_center")
+		(require-any
+			(ipc-posix-name "apple.cfprefs.daemonv1")
+			(ipc-posix-name "apple.shm.notification_center")
+			(ipc-posix-name "com.apple.featureflags.shm")
+		)
 	)
 )
 

 
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-any
 			(process-attribute is-autoboxed)
 			(require-all
```
