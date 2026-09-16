## remoteappintentsd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.linkd.registry"))
+		(require-not (global-name "com.apple.callkit.callcontrollerhost"))
 		(require-not (global-name "com.apple.linkd.extension"))
 		(require-not (global-name "com.apple.appprotectiond.guard"))
 		(require-not (global-name "com.apple.mobile.keybagd.UserManager.xpc"))

 		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.linkd.observationStatusRegistry"))
 		(require-not (global-name "com.apple.usernotifications.listener"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callcapabilities"))
 		(require-not (global-name "com.apple.findmy.findmylocate.locationservice"))
 		(require-not (global-name "com.apple.biometrickitd"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callprovidermanager"))
+		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))
```
