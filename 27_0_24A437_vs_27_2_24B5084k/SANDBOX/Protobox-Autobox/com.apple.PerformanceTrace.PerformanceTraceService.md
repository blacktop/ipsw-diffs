## com.apple.PerformanceTrace.PerformanceTraceService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.logd.admin"))

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.swiftuitracingsupport.xpc"))
 		(require-not (xpc-service-name "com.apple.swiftuitracingsupport.xpc"))
-		(require-not (global-name "com.apple.SystemConfiguration.configd"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )

 		SYS_getattrlistbulk
 		SYS_openat
 		SYS_openat_nocancel
+		SYS_renameat
 		SYS_faccessat
 		SYS_fstatat
 		SYS_fstatat64
```
