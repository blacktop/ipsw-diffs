## ReportCrash

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.ReportCrashService")
+			(xpc-service-name "com.apple.ReportCrashService2")
 			(xpc-service-name "com.apple.ReportCrashXPC")
 		))
+		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
```
