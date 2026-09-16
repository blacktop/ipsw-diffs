## appmanagedfeaturesd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.managedconfiguration.teslad"))
+		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.mobileactivationd"))
 		(require-not (global-name "com.apple.appstored.xpc"))
 		(require-not (global-name "com.apple.manageddeviced"))

 			SYS_guarded_open_np
 			SYS_change_fdguard_np
 			SYS_openat
+			SYS_renameat
 			SYS_faccessat
 			SYS_fstatat
 			SYS_fstatat64
```
