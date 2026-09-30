## CDPProximityPairingService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.ak.auth.xpc"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.securityd.sos"))
+		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.containermanagerd.system"))
 		(require-not (global-name "com.apple.lsd.open"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.SBUserNotification"))
 		(require-not (system-attribute developer-mode))
 	)
```
