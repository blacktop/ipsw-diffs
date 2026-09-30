## com.apple.SensorKit.CHSupportService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.mobileasset.autoasset"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
```
