## securityd

> Group: ⬆️ Updated

```diff

 			(xpc-service-name "com.apple.TrustedPeersHelper")
 			(xpc-service-name "com.apple.security.KeychainDBMover")
 		))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.SystemConfiguration.configd"))
 		(require-not (global-name "com.apple.SecureBackupDaemon.concurrent"))
```
