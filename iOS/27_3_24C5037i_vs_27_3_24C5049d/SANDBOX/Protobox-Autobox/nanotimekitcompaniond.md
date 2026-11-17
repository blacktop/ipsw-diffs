## nanotimekitcompaniond

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.coremedia.admin"))
 		(require-not (global-name "com.apple.coremedia.endpoint.xpc"))
 		(require-not (global-name "com.apple.SBUserNotification"))
+		(require-not (global-name "com.apple.idsremoteurlconnectionagent.embedded.auth"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (require-any
 			(global-name "com.apple.iap2d.ExternalAccessory.distributednotification.server")
```
