## IMAutomaticHistoryDeletionAgent

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.trustd"))
 		(require-not (global-name "com.apple.system.notification_center"))
+		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.businessservicesd"))
 		(require-not (global-name "com.apple.tccd"))

 		(require-not (global-name "com.apple.mediaremoted.xpc"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.runningboard"))
+		(require-not (global-name "com.apple.identityservicesd.nsxpc"))
 		(require-not (global-name "com.apple.dnssd.service"))
 		(require-not (global-name "com.apple.usymptomsd"))
 		(require-not (global-name "com.apple.imagent.embedded.auth"))

 		(require-not (global-name "com.apple.lsd.open"))
 		(require-not (xpc-service-name "com.apple.ImageIOXPCService"))
 		(require-not (xpc-service-name "com.apple.imdpersistence.IMDPersistenceAgent"))
+		(require-not (global-name "com.apple.CARenderServer"))
 		(require-not (global-name "com.apple.AppSSO.service-xpc"))
 		(require-not (global-name "com.apple.ABDatabaseDoctor"))
 		(require-not (system-attribute developer-mode))
```
