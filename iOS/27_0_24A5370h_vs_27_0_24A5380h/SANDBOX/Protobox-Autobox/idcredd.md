## idcredd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
+		(require-not (global-name "com.apple.trustd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.mobileactivationd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.timed.xpc"))
+		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.seld.tsmmanager"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.trustd"))
-		(require-not (global-name "com.apple.mobileactivationd"))
-		(require-not (global-name "com.apple.nfcd.hwmanager"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.tccd"))
-		(require-not (global-name "com.apple.timed.xpc"))
-		(require-not (global-name "com.apple.seld.tsmmanager"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.diagd"))
 		(require-not (global-name "com.apple.ctkd.token-client"))
-		(require-not (global-name "com.apple.analyticsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.CoreAuthentication.daemon"))
 		(require-not (system-attribute developer-mode))
 	)
```
