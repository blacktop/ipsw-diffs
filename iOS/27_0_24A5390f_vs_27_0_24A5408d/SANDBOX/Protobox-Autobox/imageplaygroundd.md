## imageplaygroundd

> Group: ⬆️ Updated

```diff

 		(require-not (xpc-service-name "com.apple.MTLCompilerService"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (global-name "com.apple.accountsd.accountmanager"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 		(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 		(require-not (system-attribute developer-mode))
```
