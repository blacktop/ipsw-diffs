## installd

> Group: ⬆️ Updated

```diff

 (deny iokit-open-service)
 (allow iokit-open-service
 	(require-any
+		(iokit-registry-entry-class "AppleImage4")
 		(iokit-registry-entry-class "AppleKeyStore")
 		(iokit-registry-entry-class "AppleMobileFileIntegrity")
 	)

 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.lsd.rebuild"))
-		(require-not (global-name "com.apple.lsd.system.modifydb"))
+		(require-not (require-any
+			(global-name "com.apple.lsd.system.modifydb")
+			(global-name "com.apple.security.cryptex.xpc")
+		))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.online-auth-agent.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.misagent"))
 		(require-not (xpc-service-name "com.apple.MobileInstallationHelperService"))
-		(require-not (xpc-service-name "com.apple.datamigrator"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))

 		SYS_fstat
 		SYS_lstat
 		SYS_pathconf
+		SYS_fpathconf
 		SYS_getrlimit
 		SYS_setrlimit
 		SYS_mmap
```
