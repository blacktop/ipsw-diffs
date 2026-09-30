## symptomsd-distributed

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.duetactivityscheduler"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.symptom_analytics"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
-		(require-not (global-name "com.apple.cloudd"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.duetactivityscheduler"))
-		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.tccd"))
+		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.cloudd"))
+		(require-not (global-name "com.apple.symptom_analytics"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
+		(require-not (global-name "com.apple.research.adtcd"))
+		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.apsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (system-attribute developer-mode))
 	)

 		SYS_getsockopt
 		SYS_readv
 		SYS_writev
+		SYS_rename
 		SYS_sendto
 		SYS_mkdir
 		SYS_rmdir
```
