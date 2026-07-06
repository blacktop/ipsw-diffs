## pairedunlockd

> Group: ⬆️ Updated

```diff

 (deny mach-lookup
 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
-		(require-not (global-name "com.apple.securityd"))
-		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.mobile.keybagd.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
-		(require-not (global-name "com.apple.mobile.keybagd.xpc"))
-		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.mobile.usermanagerd.xpc"))
 		(require-not (global-name "com.apple.sharingd.nsxpc"))
-		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
+		(require-not (global-name "com.apple.securityd"))
+		(require-not (global-name "com.apple.logd.events"))
+		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
+		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
```
