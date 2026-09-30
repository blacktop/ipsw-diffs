## locationaccessstored

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.mobilegestalt.xpc"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.locationd.synchronous"))
+		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
```
