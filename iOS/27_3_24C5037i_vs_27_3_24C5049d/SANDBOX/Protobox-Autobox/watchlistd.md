## watchlistd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.adid"))
 		(require-not (xpc-service-name "com.apple.VideoSubscriberAccount.DeveloperService"))
 		(require-not (global-name "com.apple.VideoSubscriberAccount.videosubscriptionsd"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.servicesanalytics.xpc"))
 		(require-not (global-name "com.apple.chronoservices"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
