## audioclocksyncd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.timesync.expositor"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.timesync.expositor"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
```
