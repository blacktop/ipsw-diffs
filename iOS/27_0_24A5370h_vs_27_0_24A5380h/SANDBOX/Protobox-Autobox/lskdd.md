## lskdd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.mobileassetd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.rtcreportingd"))
-		(require-not (global-name "com.apple.mobileassetd.v2"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.mobileassetd"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.fpassetmanagerd"))
+		(require-not (global-name "com.apple.fairplayd.versioned"))
 		(require-not (global-name "com.apple.fairplayd.xpc"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.containermanagerd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)
```
