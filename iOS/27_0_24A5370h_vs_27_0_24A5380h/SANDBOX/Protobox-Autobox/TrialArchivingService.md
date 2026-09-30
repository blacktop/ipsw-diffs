## TrialArchivingService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.ap.promotedcontent.trialbucketid"))
+		(require-not (global-name "com.apple.appleneuralengine"))
+		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.ap.promotedcontent.trialbucketid"))
+		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
-		(require-not (global-name "com.apple.xpc.amsaccountsd"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.symptom_diagnostics"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3-debug"))
-		(require-not (global-name "com.apple.geod"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.xpc.amsaccountsd"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.appleneuralengine"))
-		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.FSEvents"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))

 (with-filter (mac-policy-name "Sandbox")
 	(deny system-mac-syscall
 		(require-all
+			(require-not (mac-syscall-number 80))
 			(require-not (mac-syscall-number 7))
 			(require-not (mac-syscall-number 6))
 			(require-not (mac-syscall-number 4))
```
