## remoteappintentsd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.biometrickitd"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callprovidermanager"))
 		(require-not (global-name "com.apple.telephonyutilities.callservicesdaemon.callstatecontroller"))
+		(require-not (global-name "com.apple.siri.orchestration.capabilities"))
 		(require-not (xpc-service-name "com.apple.intents.intents-helper"))
 		(require-not (global-name "com.apple.locationd.registration"))
 		(require-not (global-name "com.apple.coremedia.systemcontroller.xpc"))

 	(fcntl-command
 		F_GETFD
 		F_GETFL
+		F_RDADVISE
 		F_NOCACHE
 		F_GETPATH
 		F_GETPROTECTIONCLASS
```
