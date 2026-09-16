## carkitd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.iapd.xpc"))
 		(require-not (global-name "com.apple.SharingServices"))
 		(require-not (global-name "com.apple.BTServer.le"))
-		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (xpc-service-name "com.apple.SharePlay.NearbyInvitationsService"))
 		(require-not (global-name "com.apple.locationd.synchronous"))
 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.carkit.service"))
+		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.containermanagerd"))
 		(require-not (global-name "com.apple.usernotifications.usernotificationservice"))
 		(require-not (global-name "com.apple.runningboard"))

 		(require-not (global-name "com.apple.dmd.policy"))
 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.aggregated"))
+		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
+		(require-not (global-name "com.apple.contactsd"))
 		(require-not (system-attribute developer-mode))
 	)
 )
```
