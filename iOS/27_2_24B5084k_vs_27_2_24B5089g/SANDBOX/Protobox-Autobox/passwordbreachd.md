## passwordbreachd

> Group: ⬆️ Updated

```diff

 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.AuthenticationServices.AutoFill"))
+		(require-not (global-name "com.apple.timed.xpc"))
 		(require-not (global-name "com.apple.AuthenticationServices.AuthenticationServicesAgent.AutomaticSecurityUpgrade"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
```
