## atc

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.Carousel.CSLSBackgroundTaskRequestService"))
 		(require-not (global-name "com.apple.backupd"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.managedconfiguration.profiled"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
