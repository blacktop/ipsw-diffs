## EscrowSecurityAlert

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.cdp.daemon"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
+		(require-not (global-name "com.apple.accountsd.accountmanager"))
 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.system.libinfo.muser"))
 		(require-not (global-name "com.apple.dasd.end-prewarm"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.securityd.ckks"))
+		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.securityd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))

 		(require-not (global-name "com.apple.analyticsd"))
 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
-		(require-not (global-name "com.apple.accountsd.accountmanager"))
-		(require-not (global-name "com.apple.SecureBackupDaemon"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
