## healthappd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.donotdisturb.service"))
 		(require-not (global-name "com.apple.adid"))
 		(require-not (global-name "com.apple.accessories.externalaccessory-server"))
+		(require-not (global-name "com.apple.siri.uaf.subscription.service"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.passd.library"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
