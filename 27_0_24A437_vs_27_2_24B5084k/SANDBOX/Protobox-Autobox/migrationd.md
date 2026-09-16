## migrationd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.icons"))
 		(require-not (global-name "com.apple.accessibility.mediaaccessibilityd"))
 		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.identityservicesd.idquery.embedded.auth"))
 		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (global-name "com.apple.iap2d.xpc"))

 		host_info
 		host_get_io_master
 		host_get_clock_service
+		host_request_notification
 		host_get_special_port
 		clock_get_time
 		mach_exception_raise
```
