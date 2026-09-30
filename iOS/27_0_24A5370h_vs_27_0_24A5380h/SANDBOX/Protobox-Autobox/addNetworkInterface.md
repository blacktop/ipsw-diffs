## addNetworkInterface

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.hangtracerd"))
-		(require-not (global-name "com.apple.hangtracermonitor"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.hangtracermonitor"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
