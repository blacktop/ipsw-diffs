## nanoappregistryd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.tailspind"))
 		(require-not (global-name "com.apple.nano.nanoregistry.paireddeviceregistry"))
 		(require-not (global-name "com.apple.system.notification_center"))
-		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.logd.events"))
 		(require-not (global-name "com.apple.system.logger"))
 		(require-not (global-name "com.apple.logd"))
 		(require-not (global-name "com.apple.identityservicesd.embedded.auth"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
+		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.cfprefsd.daemon"))
 		(require-not (global-name "com.apple.FileCoordination"))
```
