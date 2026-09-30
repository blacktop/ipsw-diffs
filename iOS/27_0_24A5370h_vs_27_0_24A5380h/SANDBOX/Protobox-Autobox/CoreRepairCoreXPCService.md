## CoreRepairCoreXPCService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
-		(require-not (global-name "com.apple.runningboard"))
-		(require-not (global-name "com.apple.commcenter.xpc"))
-		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.system.libinfo.muser"))
-		(require-not (global-name "com.apple.system.logger"))
-		(require-not (global-name "com.apple.nfcd.hwmanager"))
 		(require-not (global-name "com.apple.mobilegestalt.xpc"))
+		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.diagnosticd"))
+		(require-not (global-name "com.apple.system.libinfo.muser"))
+		(require-not (global-name "com.apple.commcenter.xpc"))
+		(require-not (global-name "com.apple.nfcd.hwmanager"))
+		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
-		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
 		(require-not (xpc-service-name "com.apple.ZhuGeService"))
+		(require-not (xpc-service-name "com.apple.AppleDeviceQueryService"))
 		(require-not (global-name "com.apple.commcenter.coretelephony.xpc"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
```
