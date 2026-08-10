## airplayd

> Group: ⬆️ Updated

```diff

 		(require-not (global-name "com.apple.mediaexperience.endpoint.xpc"))
 		(require-not (global-name "com.apple.aggregated"))
 		(require-not (global-name "com.apple.coremedia.volumecontroller.xpc"))
+		(require-not (global-name "com.apple.audio.AURemoteIOServer"))
 		(require-not (global-name "com.apple.airplay.endpoint.xpc"))
 		(require-not (xpc-service-name "com.apple.MFAAuthentication.MFAANetwork"))
 		(require-not (xpc-service-name "com.apple.audio.AudioConverterService"))

 		SIOCGIFADDR
 		SIOCGIFAFLAG_IN6
 		SIOCGIFAGENTDATA
+		SIOCGIFCLAT46ADDR
 		SIOCGIFCONSTRAINED
 		SIOCGIFDELEGATE
 		SIOCGIFEFLAGS
```
