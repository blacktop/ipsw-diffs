## CoreThreadCommissionerServiced

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.matter.support.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.wifi.manager"))
-		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.awdd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.wifi.manager"))
+		(require-not (global-name "com.apple.matter.support.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.awdd"))
+		(require-not (global-name "com.apple.private.corewifi.mobilewifi-xpc"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (system-attribute developer-mode))
```
