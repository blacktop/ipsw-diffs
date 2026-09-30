## uarpd

> Group: ⬆️ Updated

```diff

 	(require-all
 		(global-name "com.apple.dt.testmanagerd.uiprocess")
 		(require-not (global-name "com.apple.iokit.powerdxpc"))
-		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.TapToRadarKit.service"))
-		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
+		(require-not (global-name "com.apple.geod"))
 		(require-not (global-name "com.apple.corespeech.corespeechservices"))
+		(require-not (global-name "com.apple.nesessionmanager.content-filter"))
 		(require-not (xpc-service-name "com.apple.corespeech.xpc"))
 		(require-not (global-name "com.apple.PowerManagement.control"))
 		(require-not (global-name "com.apple.FileCoordination"))
```
