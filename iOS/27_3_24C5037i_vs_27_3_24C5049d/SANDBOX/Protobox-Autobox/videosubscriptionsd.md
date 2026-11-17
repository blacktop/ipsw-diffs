## videosubscriptionsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.webinspector"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
 		(require-not (global-name "com.apple.lsd.icons"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))

 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.PineBoardRiseServices"))
 		(require-not (global-name "com.apple.adid"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.VideoSubscriberAccount.AnalyticsService"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_fstatat64
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
