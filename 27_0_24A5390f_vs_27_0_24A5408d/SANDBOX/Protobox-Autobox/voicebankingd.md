## voicebankingd

> Group: ⬆️ Updated

```diff

 		(require-any
 			(require-all
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
-				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.GSSCred"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CARenderServer"))

 				(xpc-service-name "*")
 				(global-name "com.apple.dt.testmanagerd.uiprocess")
 				(require-not (extension "com.apple.pluginkit.plugin-service"))
-				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.GSSCred"))
+				(require-not (global-name "com.apple.FileCoordination"))
 				(require-not (global-name "com.apple.DiskArbitration.diskarbitrationd"))
 				(require-not (global-name "com.apple.CoreServices.coreservicesd"))
 				(require-not (global-name "com.apple.CARenderServer"))
```
