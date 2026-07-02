## NFReportingService

> Group: ⬆️ Updated

```diff

 	(with no-report)
 	(require-all
 		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.SystemConfiguration.NetworkInformation"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.runningboard"))
 		(require-not (global-name "com.apple.system.notification_center"))

 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.analyticsd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.ctkd.token-client"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.ak.anisette.xpc"))
```
