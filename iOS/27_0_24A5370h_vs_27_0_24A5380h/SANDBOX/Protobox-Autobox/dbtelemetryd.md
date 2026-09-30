## dbtelemetryd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.logd.admin"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.accessibility.AXBackBoardServer"))
 		(require-not (system-attribute developer-mode))
```
