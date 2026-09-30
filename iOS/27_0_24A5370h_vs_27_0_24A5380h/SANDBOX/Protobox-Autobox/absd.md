## absd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.fairplayd.versioned"))
-		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
```
