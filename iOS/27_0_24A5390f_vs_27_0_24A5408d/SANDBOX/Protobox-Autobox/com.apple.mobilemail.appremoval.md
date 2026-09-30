## com.apple.mobilemail.appremoval

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.gputools.service"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		SYS_proc_rlimit_control
 		SYS_getattrlistbulk
 		SYS_openat
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
