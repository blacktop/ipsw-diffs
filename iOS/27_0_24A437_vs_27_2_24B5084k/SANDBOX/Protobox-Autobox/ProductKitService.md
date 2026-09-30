## ProductKitService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (xpc-service-name "com.apple.ProductKitService"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))

 		host_info
 		host_get_clock_service
 		host_get_special_port
+		clock_get_time
 		mach_exception_raise
 		mach_exception_raise_state
 		mach_exception_raise_state_identity
```
