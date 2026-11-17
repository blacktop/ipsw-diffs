## ScreenTimeSettingsAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.ScreenTimeAgent.persistence"))
+		(require-not (global-name "com.apple.springboard.backgroundappservices"))
 		(require-not (global-name "com.apple.nehelper"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))

 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.ScreenTimeSettingsAgent.private"))
 		(require-not (global-name "com.apple.dnssd.service"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.family.ageRange.xpc"))
 		(require-not (global-name "com.apple.coreduetd.context"))

 		SYS_open_dprotected_np
 		SYS_openat_dprotected_np
 		SYS_getattrlist
+		SYS_setattrlist
 		SYS_fgetattrlist
 		SYS_fsetattrlist
 		SYS_getxattr
```
