## NFReportingService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(with no-report)
 	(require-all
+		(require-not (global-name "com.apple.networkscored"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.logd.events"))
```
