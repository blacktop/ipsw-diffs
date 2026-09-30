## SetStoreUpdateService

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.diagnosticd"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.translation.text"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.diagd"))
-		(require-not (global-name "com.apple.uservault"))
-		(require-not (global-name "com.apple.cfprefsd.daemon"))
-		(require-not (global-name "com.apple.lsd.mapdb"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.userprofiles"))
-		(require-not (global-name "com.apple.logd"))
-		(require-not (global-name "com.apple.cascade.SetChangeRelayService"))
-		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.uservault"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
+		(require-not (global-name "com.apple.containermanagerd"))
+		(require-not (global-name "com.apple.cascade.SetChangeRelayService"))
+		(require-not (global-name "com.apple.diagd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.cfprefsd.daemon"))
+		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
```
