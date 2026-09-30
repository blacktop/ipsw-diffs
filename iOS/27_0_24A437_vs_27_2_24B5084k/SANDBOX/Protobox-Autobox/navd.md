## navd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.locationd.simulation"))
 		(require-not (global-name "com.apple.Maps.xpc.connectionBroker.endpointRecorder"))
 		(require-not (global-name "com.apple.systemstatus"))
+		(require-not (global-name "com.apple.mobileassetd.v2"))
 		(require-not (global-name "com.apple.lsd.mapdb"))
 		(require-not (global-name "com.apple.geoanalyticsd"))
 		(require-not (global-name "com.apple.NetworkLinkConditioner"))
+		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.frontboard.systemappservices"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))
 		(require-not (global-name "com.apple.relatived.status"))

 		(require-not (global-name "com.apple.contactsd"))
 		(require-not (global-name "com.apple.calaccessd"))
 		(require-not (global-name "com.apple.appprotectiond.read"))
+		(require-not (xpc-service-name "com.apple.SiriTTSService.TrialProxy"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
+		(require-not (xpc-service-name "com.apple.SetStoreUpdateService"))
 		(require-not (xpc-service-name "com.apple.SpatialAudioProfileXPCService"))
 		(require-any
 			(require-all
```
