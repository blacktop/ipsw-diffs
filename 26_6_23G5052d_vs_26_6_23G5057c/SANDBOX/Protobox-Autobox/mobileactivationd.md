## mobileactivationd

> Group: ⬆️ Updated

```diff

 	(require-any
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.exception.iokit-user-client-class}")
 		(iokit-registry-entry-class "${ENTITLEMENT:com.apple.security.iokit-user-client-class}")
+		(iokit-registry-entry-class "AppleKeyStoreUserClient")
 	)
 )
 

 
 (deny ipc*)
 
+(deny ipc-posix-shm-read-data)
+(allow ipc-posix-shm-read-data
+	(require-any
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+		(ipc-posix-name "apple.shm.notification_center")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 (deny mach-lookup
 	(with no-report)
 	(require-all
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 )
 (deny mach-lookup
 	(require-all
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
```
