## NTKFaceSnapshotService

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.diagnosticd"))
 		(require-not (global-name "com.apple.appconduitd.device-connection"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
+		(require-not (global-name "com.apple.muranod.listener"))
 		(require-not (global-name "com.apple.carkit.app.service"))
 		(require-not (global-name "com.apple.distributed_notifications@1v3"))
 		(require-not (global-name "com.apple.coremedia.routingcontext.xpc"))

 		(require-not (global-name "com.apple.cfprefsd.daemon.system"))
 		(require-not (global-name "com.apple.contacts.poster.api"))
 		(require-not (global-name "com.apple.coremedia.mediaplaybackd.figmetriceventtimeline.xpc"))
+		(require-not (global-name "com.apple.conversation-intelligence.service"))
 		(require-not (require-any
 			(xpc-service-name "com.apple.WebKit.Networking")
 			(xpc-service-name "com.apple.WebKit.WebContent")
```
