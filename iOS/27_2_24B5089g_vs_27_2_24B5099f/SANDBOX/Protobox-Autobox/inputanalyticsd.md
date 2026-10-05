## inputanalyticsd

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ctcategories.service"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_statistics_from_user
 		host_request_notification
+		host_statistics64_from_user
 		host_get_special_port
 		clock_get_time
 		mach_exception_raise
```
