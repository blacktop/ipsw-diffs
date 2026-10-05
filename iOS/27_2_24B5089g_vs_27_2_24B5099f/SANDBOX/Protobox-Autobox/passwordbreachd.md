## passwordbreachd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.AutomaticSecurityUpgrade"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
+		(require-not (global-name "com.apple.FileCoordination"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (system-attribute developer-mode))
 	)
```
