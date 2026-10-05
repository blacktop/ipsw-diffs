## CategoriesService

> Group: ⬆️ Updated

```diff

 	)
 )
 
+(deny ipc-posix-shm-write-data)
+(allow ipc-posix-shm-write-data
+	(ipc-posix-name "apple.cfprefs.daemonv1")
+)
+
 (deny job-creation)
 
 (deny mach-issue-extension)

 		(require-not (global-name "com.apple.siri.context.service"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.networkd_privileged"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))

 		(require-not (global-name "com.apple.cfnetwork.cfnetworkagent"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.adid"))
-		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
-		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.fairplaydeviceidentityd"))
 		(require-not (global-name "com.apple.securityd"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (xpc-service-name "com.apple.siri.context.service"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.ak.anisette.xpc"))
+		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
+		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
 		(require-not (global-name "com.apple.GSSCred"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (system-attribute developer-mode))
 	)
```
