## trustd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.runningboard"))
-		(require-not (require-any
-			(global-name "com.apple.ValidUpdater")
-			(global-name "com.apple.trustdFileHelper")
-		))
+		(require-not (global-name "com.apple.trustdFileHelper"))
 		(require-not (global-name "com.apple.cloudtelemetryd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
-		(require-not (global-name "com.apple.containermanagerd.system"))
+		(require-not (global-name "com.apple.ValidUpdater"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		SYS_ioctl
 		SYS_readlink
 		SYS_umask
+		SYS_msync
 		SYS_munmap
 		SYS_mprotect
 		SYS_madvise
```
