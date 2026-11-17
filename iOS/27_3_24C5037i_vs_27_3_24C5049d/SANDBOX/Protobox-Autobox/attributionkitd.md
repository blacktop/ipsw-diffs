## attributionkitd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.corereporting.report-services"))
 		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
