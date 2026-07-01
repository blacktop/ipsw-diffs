# akd

Group: Updated

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
+		(ipc-posix-name "apple.cfprefs.system.daemonv1")
+		(ipc-posix-name "apple.cfprefs.user.daemonv1")
+	)
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.security.kcsharing"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))

 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.eligibilityd"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.security.octagon"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.devicecheckd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))

 (deny mach-lookup
 	(require-all
 		(require-not (global-name "com.apple.security.kcsharing"))
+		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.pluginkit.pkd"))
 		(require-not (global-name "com.apple.coreidvd.proofing"))

 		(require-not (global-name "com.apple.SharedWebCredentials"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.eligibilityd"))
+		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.appstorecomponentsd.xpc"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (require-any

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.erm.logging"))
 		(require-not (global-name "com.apple.security.octagon"))

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.devicecheckd"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (xpc-service-name "com.apple.AppleVirtualPlatform.IdentityService"))
```
