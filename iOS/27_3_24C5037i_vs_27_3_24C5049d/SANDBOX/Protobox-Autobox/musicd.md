## musicd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.xpc.amsengagementd"))
+		(require-not (require-any
+			(global-name "com.apple.musicd.ConcertRankingService")
+			(global-name "com.apple.musicd.ConcertsRankingService")
+		))
 		(require-not (global-name "com.apple.tccd"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.kvsd"))

 		(require-not (global-name "com.apple.usernotifications.listener"))
 		(require-not (global-name "com.apple.itunescloud.remote-request-execution-service"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (xpc-service-name "com.apple.musicd.ConcertRankingService"))
 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.SystemConfiguration.DNSConfiguration"))
+		(require-not (global-name "com.apple.fairplayd"))
 		(require-not (global-name "com.apple.medialibraryd.xpc"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))

 		SYS_unlinkat
 		SYS_mkdirat
 		SYS_bsdthread_ctl
+		SYS_thread_selfusage
 		SYS_guarded_open_dprotected_np
 		SYS_guarded_write_np
 		SYS_guarded_pwrite_np
```
